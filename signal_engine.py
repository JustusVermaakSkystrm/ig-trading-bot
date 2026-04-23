"""
signal_engine.py
----------------
Generates live trading signals by:
  1. Fetching the latest 15-min candles from IG
  2. Computing all features (SG, Hilbert, 20 TIs, DXY cross-asset, etc.)
  3. Running the binary XGBoost model (BUY vs SELL, Triple Barrier trained)
  4. Returning an actionable signal dict

Usage:
    from signal_engine import SignalEngine
    engine = SignalEngine(client)
    sig = engine.get_signal()
    if sig["actionable"]:
        exec_engine.open_trade(sig["signal"], sig["atr"], sig["latest_price"])
"""

import logging
from datetime import datetime, timedelta, timezone

import numpy as np
import pandas as pd

from ig_client import IGClient
from features import compute_features, _causal_savgol
from model import TradingModel
from data_pipeline import load_data, CSV_PATH

logger = logging.getLogger(__name__)

# Minimum model confidence to act on a signal.
# 0.65 is the backtested optimum for the binary Triple Barrier model.
MIN_CONFIDENCE = 0.65

# How many recent bars to pass to compute_features().
# Must exceed warmup (240 bars for SMA-200 + RV-240) plus indicator look-backs.
LOOKBACK_BARS = 500

EPIC = "CS.D.EURUSD.TODAY.IP"

# ------------------------------------------------------------------
# SG regime filter
# ------------------------------------------------------------------
# Walk-forward research (sg_crossover_research.py) on 2 years of hourly
# EURUSD found that SG(11, P=2) vs SG(61, P=2) level crossover has
# annualised Sharpe ≈ 1.99–2.13 across 1–5 bar horizons.
# We use it as a pre-trade regime gate: only take BUY signals when the
# fast SG is above the slow SG, and only SELL when below.
# ------------------------------------------------------------------
SG_REGIME_FAST   = 11   # fast window (bars)
SG_REGIME_SLOW   = 61   # slow window (bars)
SG_REGIME_POLY   =  2   # polyorder — research optimum for this crossover


class SignalEngine:
    """Fetches live prices, computes features, and returns a trading signal."""

    def __init__(
        self,
        client:         IGClient,
        epic:           str   = EPIC,
        min_confidence: float = MIN_CONFIDENCE,
    ):
        self.client         = client
        self.epic           = epic
        self.min_confidence = min_confidence
        self.model          = TradingModel.load()   # loads saved binary model

    # ------------------------------------------------------------------
    # SG regime filter
    # ------------------------------------------------------------------

    @staticmethod
    def _sg_regime(df_feat: pd.DataFrame) -> str:
        """
        Compute causal SG(11, P=2) vs SG(61, P=2) crossover on close prices.

        Returns
        -------
        "BULL"    — fast SG above slow SG  (favour BUY signals)
        "BEAR"    — fast SG below slow SG  (favour SELL signals)
        "NEUTRAL" — insufficient data or NaN
        """
        close    = df_feat["close"].values.astype(float)
        sg_fast  = _causal_savgol(close, SG_REGIME_FAST, SG_REGIME_POLY, deriv=0)
        sg_slow  = _causal_savgol(close, SG_REGIME_SLOW, SG_REGIME_POLY, deriv=0)
        f_val, s_val = sg_fast[-1], sg_slow[-1]
        if np.isnan(f_val) or np.isnan(s_val):
            return "NEUTRAL"
        return "BULL" if f_val > s_val else "BEAR"

    # ------------------------------------------------------------------
    # Price fetch
    # ------------------------------------------------------------------

    def _fetch_recent_bars(self, n_bars: int = LOOKBACK_BARS) -> pd.DataFrame:
        """
        Return the last n_bars of 15-min candles with the most recent bar
        always sourced directly from IG (zero delay).

        Strategy:
          1. Load bulk history from the cached CSV (Yahoo-sourced, fine for
             computing indicators on older bars).
          2. Top up the tail with the last 60 min of bars from IG directly,
             so the most recent 1-4 candles are always real-time.
          3. Fall back to CSV-only if IG fails.
        """
        from data_pipeline import load_data, CSV_PATH, _fetch_chunk, DEFAULT_EPIC

        # Step 1 — bulk history from CSV
        try:
            df = load_data(CSV_PATH).tail(n_bars).copy()
        except Exception as exc:
            logger.error("Could not load CSV: %s", exc)
            df = pd.DataFrame()

        # Step 2 — top up with live IG bars (last 60 min = max 4 bars)
        try:
            end   = datetime.now(tz=timezone.utc)
            start = end - timedelta(minutes=60)
            df_live = _fetch_chunk(self.client, EPIC, start, end)
            if not df_live.empty:
                df_live = df_live.dropna()
                if not df.empty:
                    df = pd.concat([df, df_live], ignore_index=True)
                    df = df.drop_duplicates(subset="datetime", keep="last")
                    df = df.sort_values("datetime").reset_index(drop=True)
                else:
                    df = df_live
                logger.info("Signal engine: %d bars loaded (%d live from IG, latest: %s)",
                            len(df), len(df_live),
                            df["datetime"].iloc[-1].strftime("%Y-%m-%d %H:%M UTC"))
        except Exception as exc:
            logger.warning("IG live top-up failed (%s) — using CSV only", exc)
            if df.empty:
                logger.error("No data available at all.")

        return df.tail(n_bars) if not df.empty else df

    # ------------------------------------------------------------------
    # Signal generation
    # ------------------------------------------------------------------

    def get_signal(self, df_feat: pd.DataFrame = None) -> dict:
        """
        Compute the latest signal.

        Parameters
        ----------
        df_feat : pre-computed feature DataFrame (optional).
                  If None, bars are fetched from IG and features computed here.

        Returns
        -------
        dict with keys:
            signal       int    +1 BUY / -1 SELL / 0 HOLD
            label        str    "BUY" / "SELL" / "HOLD"
            confidence   float  P(predicted class)
            p_buy        float  P(BUY)
            p_sell       float  P(SELL)
            actionable   bool   signal != 0, conf >= min_confidence,
                                AND SG regime agrees with direction
            regime       str    "BULL" / "BEAR" / "NEUTRAL"
            regime_ok    bool   True when regime matches signal direction
            atr          float  latest ATR value (used for sizing)
            latest_price float  latest close price
            timestamp    datetime
        """
        if df_feat is None:
            df_raw  = self._fetch_recent_bars()
            df_feat = compute_features(df_raw)

        if df_feat.empty:
            logger.warning("Feature DataFrame is empty — returning HOLD")
            return self._hold_result()

        signal, confidence = self.model.predict_latest(df_feat)
        probabilities      = self.model.predict_proba_latest(df_feat)

        # In binary mode predict_proba_latest returns {1: p_buy, -1: p_sell}
        p_buy  = float(probabilities.get(1,  0.5))
        p_sell = float(probabilities.get(-1, 0.5))

        label = {1: "BUY", -1: "SELL", 0: "HOLD"}.get(signal, "HOLD")

        # ── SG regime filter ──────────────────────────────────────────
        # Only act when SG(11,P=2) vs SG(61,P=2) crossover agrees with
        # the model's direction. NEUTRAL (warm-up) passes through.
        regime    = self._sg_regime(df_feat)
        regime_ok = (
            regime == "NEUTRAL"                         # not enough bars yet
            or signal == 0                              # HOLD — no direction to check
            or (signal ==  1 and regime == "BULL")      # BUY in uptrend
            or (signal == -1 and regime == "BEAR")      # SELL in downtrend
        )

        actionable = (signal != 0) and (confidence >= self.min_confidence) and regime_ok

        if (signal != 0) and (confidence >= self.min_confidence) and not regime_ok:
            logger.info(
                "[Regime filter] %s blocked — model wants %s but SG regime is %s "
                "(SG11/P2 vs SG61/P2 crossover disagrees)",
                label, label, regime,
            )

        atr          = float(df_feat["atr"].iloc[-1])
        latest_price = float(df_feat["close"].iloc[-1])
        timestamp    = df_feat["datetime"].iloc[-1]

        result = {
            "signal":       signal,
            "label":        label,
            "confidence":   round(confidence, 4),
            "p_buy":        round(p_buy,  4),
            "p_sell":       round(p_sell, 4),
            "actionable":   actionable,
            "regime":       regime,
            "regime_ok":    regime_ok,
            "atr":          atr,
            "latest_price": latest_price,
            "timestamp":    timestamp,
        }

        logger.info(
            "[Signal] %-4s  conf=%.1f%%  p_buy=%.1f%%  p_sell=%.1f%%  "
            "regime=%-7s  actionable=%s  ATR=%.5f  price=%.5f  @%s",
            label, confidence * 100, p_buy * 100, p_sell * 100,
            regime, actionable, atr, latest_price,
            timestamp.strftime("%Y-%m-%d %H:%M") if hasattr(timestamp, "strftime")
            else str(timestamp),
        )
        return result

    def _hold_result(self) -> dict:
        return {
            "signal": 0, "label": "HOLD", "confidence": 0.0,
            "p_buy": 0.5, "p_sell": 0.5, "actionable": False,
            "regime": "NEUTRAL", "regime_ok": True,
            "atr": 0.0, "latest_price": 0.0,
            "timestamp": datetime.now(tz=timezone.utc),
        }
