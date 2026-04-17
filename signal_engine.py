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

import pandas as pd

from ig_client import IGClient
from features import compute_features
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
    # Price fetch
    # ------------------------------------------------------------------

    def _fetch_recent_bars(self, n_bars: int = LOOKBACK_BARS) -> pd.DataFrame:
        """
        Fetch the last n_bars × 15-min candles from IG.
        Falls back to the cached CSV if the API call fails.
        """
        end   = datetime.now(tz=timezone.utc)
        start = end - timedelta(minutes=15 * n_bars)

        from_str = start.strftime("%Y-%m-%dT%H:%M:%S")
        to_str   = end.strftime("%Y-%m-%dT%H:%M:%S")

        try:
            data = self.client.get(
                f"/prices/{self.epic}",
                params={"resolution": "MINUTE_15", "from": from_str,
                        "to": to_str, "max": n_bars},
                version="3",
            )
        except Exception as exc:
            logger.error("Live price fetch failed: %s — using cached CSV", exc)
            return load_data(CSV_PATH).tail(n_bars)

        candles = data.get("prices", [])
        rows = []
        for c in candles:
            def mid(p):
                if not p:
                    return None
                b, a = p.get("bid"), p.get("ask")
                return (b + a) / 2 if (b is not None and a is not None) else None

            raw_time = c.get("snapshotTime", "")
            try:
                dt = datetime.strptime(raw_time[:19], "%Y/%m/%d %H:%M:%S")
                dt = dt.replace(tzinfo=timezone.utc)
            except ValueError:
                continue

            rows.append({
                "datetime": dt,
                "open":     mid(c.get("openPrice")),
                "high":     mid(c.get("highPrice")),
                "low":      mid(c.get("lowPrice")),
                "close":    mid(c.get("closePrice")),
                "volume":   c.get("lastTradedVolume", 0),
            })

        if not rows:
            logger.warning("Empty price response from IG — using cached CSV")
            return load_data(CSV_PATH).tail(n_bars)

        df = pd.DataFrame(rows).dropna().sort_values("datetime").reset_index(drop=True)
        logger.info("Fetched %d live 15-min bars from IG (latest: %s)",
                    len(df), df["datetime"].iloc[-1].strftime("%Y-%m-%d %H:%M UTC"))
        return df

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
            actionable   bool   signal != 0 and confidence >= min_confidence
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

        label      = {1: "BUY", -1: "SELL", 0: "HOLD"}.get(signal, "HOLD")
        actionable = (signal != 0) and (confidence >= self.min_confidence)

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
            "atr":          atr,
            "latest_price": latest_price,
            "timestamp":    timestamp,
        }

        logger.info(
            "[Signal] %-4s  conf=%.1f%%  p_buy=%.1f%%  p_sell=%.1f%%  "
            "actionable=%s  ATR=%.5f  price=%.5f  @%s",
            label, confidence * 100, p_buy * 100, p_sell * 100,
            actionable, atr, latest_price,
            timestamp.strftime("%Y-%m-%d %H:%M") if hasattr(timestamp, "strftime")
            else str(timestamp),
        )
        return result

    def _hold_result(self) -> dict:
        return {
            "signal": 0, "label": "HOLD", "confidence": 0.0,
            "p_buy": 0.5, "p_sell": 0.5, "actionable": False,
            "atr": 0.0, "latest_price": 0.0,
            "timestamp": datetime.now(tz=timezone.utc),
        }
