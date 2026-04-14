"""
signal_engine.py
----------------
Generates trading signals by fetching the latest price bar from IG,
computing features, and running the XGBoost model.

A signal is only actioned if the model's confidence exceeds MIN_CONFIDENCE.

Usage:
    from signal_engine import SignalEngine
    engine = SignalEngine(client)
    signal = engine.get_signal()   # returns dict with signal, confidence, etc.
"""

import logging
import os
from datetime import datetime, timedelta, timezone

import pandas as pd

from ig_client import IGClient
from features import compute_features
from model import TradingModel
from data_pipeline import load_data, CSV_PATH

logger = logging.getLogger(__name__)

# Minimum model confidence before we act on a signal
MIN_CONFIDENCE = 0.55   # 55% — tune this after backtesting

# How many recent bars to use for feature computation
# (needs to be long enough for all SG windows + warmup)
LOOKBACK_BARS = 200

# EUR/USD spread bet epic
EPIC = "CS.D.EURUSD.TODAY.IP"


class SignalEngine:
    """
    Fetches latest prices, computes features, and returns a trading signal.
    """

    def __init__(self, client: IGClient, epic: str = EPIC,
                 min_confidence: float = MIN_CONFIDENCE):
        self.client         = client
        self.epic           = epic
        self.min_confidence = min_confidence
        self.model          = TradingModel.load()

    def _fetch_recent_bars(self, n_bars: int = LOOKBACK_BARS) -> pd.DataFrame:
        """
        Fetch the most recent `n_bars` 15-min candles from IG.
        Falls back to cached CSV if the API call fails.
        """
        end   = datetime.now(tz=timezone.utc)
        start = end - timedelta(minutes=15 * n_bars)

        from_str = start.strftime("%Y-%m-%dT%H:%M:%S")
        to_str   = end.strftime("%Y-%m-%dT%H:%M:%S")

        try:
            data = self.client.get(
                f"/prices/{self.epic}",
                params={"resolution": "MINUTE_15", "from": from_str, "to": to_str, "max": n_bars},
                version="3",
            )
        except Exception as e:
            logger.error("Failed to fetch live prices: %s. Falling back to CSV.", e)
            return load_data(CSV_PATH).tail(n_bars)

        candles = data.get("prices", [])
        rows = []
        for c in candles:
            def mid(p):
                if not p:
                    return None
                b, a = p.get("bid"), p.get("ask")
                return (b + a) / 2 if b and a else None

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
            logger.warning("No live candles returned. Using cached CSV.")
            return load_data(CSV_PATH).tail(n_bars)

        df = pd.DataFrame(rows)
        df = df.dropna().sort_values("datetime").reset_index(drop=True)
        return df

    def get_signal(self, df_feat: pd.DataFrame = None) -> dict:
        """
        Main method: fetch latest bars → compute features → run model.

        Parameters
        ----------
        df_feat : pd.DataFrame, optional
            Pre-computed feature DataFrame (e.g. built from a rolling 15-min
            synthetic bar in the main loop).  If None, the engine fetches
            its own recent bars from IG and computes features internally.

        Returns
        -------
        dict with keys:
            signal      : int   — 1=BUY, -1=SELL, 0=HOLD
            label       : str   — "BUY" / "SELL" / "HOLD"
            confidence  : float — model probability for the predicted class
            actionable  : bool  — True if confidence >= min_confidence and signal != HOLD
            timestamp   : datetime
            latest_price: float
            probabilities: dict — full {1: p_buy, 0: p_hold, -1: p_sell}
        """
        if df_feat is None:
            df_raw  = self._fetch_recent_bars()
            df_feat = compute_features(df_raw)

        if df_feat.empty:
            logger.warning("Feature DataFrame is empty — cannot generate signal.")
            return {"signal": 0, "label": "HOLD", "confidence": 0.0,
                    "actionable": False, "timestamp": datetime.now(tz=timezone.utc)}

        signal, confidence = self.model.predict_latest(df_feat)
        probabilities      = self.model.predict_proba_latest(df_feat)
        label              = {1: "BUY", -1: "SELL", 0: "HOLD"}.get(signal, "HOLD")
        actionable         = (signal != 0) and (confidence >= self.min_confidence)

        latest_price = float(df_feat["close"].iloc[-1])
        timestamp    = df_feat["datetime"].iloc[-1]

        result = {
            "signal":        signal,
            "label":         label,
            "confidence":    round(confidence, 4),
            "actionable":    actionable,
            "timestamp":     timestamp,
            "latest_price":  latest_price,
            "probabilities": {k: round(v, 4) for k, v in probabilities.items()},
        }

        logger.info(
            "[Signal] %s  conf=%.1f%%  actionable=%s  price=%.5f  @%s",
            label, confidence * 100, actionable, latest_price,
            timestamp.strftime("%Y-%m-%d %H:%M")
        )

        return result
