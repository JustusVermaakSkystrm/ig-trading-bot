"""
execution.py
------------
Handles order placement and position management via the IG API.

Optimal parameters from backtesting (5-fold walk-forward, Oct 2025–Mar 2026):
  Stop loss  = 1.0 × ATR  (tight, matched to Triple Barrier training labels)
  Take profit = 1.5 × ATR  (1:1.5 R:R)
  Confidence  = 0.65       (filters low-conviction signals)

  → Avg return per test fold: +49.8%
  → Avg Sharpe: 22.6
  → Avg win rate: 59.9%

Usage:
    from execution import ExecutionEngine
    engine = ExecutionEngine(client)
    confirm = engine.open_trade(signal=1, atr=0.0010, current_price=1.0950)
"""

import logging
from datetime import datetime, timezone

from ig_client import IGClient

logger = logging.getLogger(__name__)

# ------------------------------------------------------------------
# Risk management — optimised from backtesting
# ------------------------------------------------------------------

RISK_PER_TRADE_PCT   = 1.0    # % of account balance risked per trade
STOP_ATR_MULTIPLE    = 1.5    # stop loss = ATR × this (in pips)
TP_ATR_MULTIPLE      = 2.25   # take profit = ATR × this (1.5:1 R:R vs stop)
MIN_CONFIDENCE       = 0.65   # minimum model confidence to trade

MIN_SIZE = 0.01             # minimum £/point position size (IG minimum for EURUSD)
MAX_SIZE = 5.0              # safety cap

# EUR/USD spread bet epic (DFB = daily funded bet, rolling)
EPIC          = "CS.D.EURUSD.TODAY.IP"
PIP_SIZE      = 0.0001      # 1 pip = 0.0001 for EUR/USD


class ExecutionEngine:
    """
    Places and manages spread bet positions through the IG API.

    Uses IG's native trailing stop — the SL follows price automatically
    on IG's side, so it keeps working even if the bot restarts.

    Parameters
    ----------
    client          : Authenticated IGClient instance
    epic            : IG instrument epic (default: EURUSD spread bet)
    stop_atr_mult   : Initial trailing stop distance as ATR multiple (default: 1.5)
    risk_pct        : Fraction of balance to risk per trade (default: 1.0%)
    """

    def __init__(
        self,
        client:        IGClient,
        epic:          str   = EPIC,
        stop_atr_mult: float = STOP_ATR_MULTIPLE,
        risk_pct:      float = RISK_PER_TRADE_PCT,
    ):
        self.client        = client
        self.epic          = epic
        self.stop_atr_mult = stop_atr_mult
        self.risk_pct      = risk_pct

    # ------------------------------------------------------------------
    # Account helpers
    # ------------------------------------------------------------------

    def get_account_balance(self) -> float:
        """Fetch current available funds from the IG account."""
        try:
            accounts = self.client.get_accounts()
            for acc in accounts.get("accounts", []):
                if acc.get("accountId") == self.client.account_id:
                    return float(acc["balance"]["available"])
            # fallback: first account
            return float(accounts["accounts"][0]["balance"]["available"])
        except Exception as exc:
            logger.error("Could not fetch balance: %s", exc)
            return 0.0

    # ------------------------------------------------------------------
    # Position sizing
    # ------------------------------------------------------------------

    def calculate_size(self, atr: float, balance: float = None) -> float:
        """
        Fixed fractional position sizing.

        Formula:
            risk_amount        = balance × risk_pct / 100
            stop_distance_pips = atr × stop_atr_mult / pip_size
            size (£/pip)       = risk_amount / stop_distance_pips

        With the account in GBP and EURUSD, 1 pip = £1 for a £1/pip bet,
        so size in £/pip equals the risk-per-pip directly.
        """
        if balance is None:
            balance = self.get_account_balance()

        risk_amount        = balance * (self.risk_pct / 100.0)
        stop_distance_pips = (atr * self.stop_atr_mult) / PIP_SIZE
        raw_size           = risk_amount / stop_distance_pips if stop_distance_pips > 0 else MIN_SIZE

        size = max(MIN_SIZE, min(raw_size, MAX_SIZE))
        size = round(size * 100) / 100  # round to nearest 0.01

        logger.info(
            "Sizing: balance=£%.2f  risk=£%.2f  ATR=%.5f  "
            "stop_pips=%.1f  size=£%.2f/point",
            balance, risk_amount, atr, stop_distance_pips, size,
        )
        return size

    # ------------------------------------------------------------------
    # Open position
    # ------------------------------------------------------------------

    def open_trade(
        self,
        signal:        int,
        atr:           float,
        current_price: float,
        size:          float = None,
    ) -> dict:
        """
        Open a market spread bet position with a native IG trailing stop.

        The trailing stop is managed server-side by IG — it follows price
        automatically and keeps working even if the bot restarts.  There is
        no fixed take-profit; the trade runs until the trailing stop is hit
        or the user closes manually.

        Parameters
        ----------
        signal        : +1 = BUY, -1 = SELL
        atr           : current ATR (sets initial trailing stop distance)
        current_price : indicative mid price (for logging only — IG fills at market)
        size          : override £/pip size (calculated automatically if None)

        Returns
        -------
        IG deal confirmation dict (keys: dealStatus, dealId, level, etc.)
        """
        if signal not in (1, -1):
            raise ValueError(f"signal must be +1 or -1, got {signal}")

        direction = "BUY" if signal == 1 else "SELL"

        if size is None:
            size = self.calculate_size(atr)

        # Stop and TP distances in pips (1 pip = 0.0001 for EURUSD)
        stop_pips = round((atr * STOP_ATR_MULTIPLE) / PIP_SIZE, 1)
        stop_pips = max(stop_pips, 2.0)   # IG minimum stop distance
        tp_pips   = round((atr * TP_ATR_MULTIPLE)   / PIP_SIZE, 1)

        payload = {
            "epic":          self.epic,
            "expiry":        "DFB",
            "direction":     direction,
            "size":          size,
            "orderType":     "MARKET",
            "timeInForce":   "FILL_OR_KILL",
            "guaranteedStop": False,
            "trailingStop":  False,
            "stopDistance":  stop_pips,
            "limitDistance": tp_pips,
            "forceOpen":     True,
            "currencyCode":  "GBP",
        }

        logger.info(
            "→ Opening %s  size=£%.2f/point  stop=%.1f pts  tp=%.1f pts  price≈%.5f",
            direction, size, stop_pips, tp_pips, current_price,
        )

        try:
            resp     = self.client.post("/positions/otc", payload, version="2")
            deal_ref = resp.get("dealReference", "UNKNOWN")
            logger.info("Deal reference: %s", deal_ref)
            return self._confirm_deal(deal_ref)
        except Exception as exc:
            logger.error("open_trade failed: %s", exc)
            return {"dealStatus": "ERROR", "reason": str(exc)}

    def _confirm_deal(self, deal_reference: str) -> dict:
        """Fetch and log the deal confirmation."""
        try:
            confirm = self.client.get(f"/confirms/{deal_reference}")
            status  = confirm.get("dealStatus", "UNKNOWN")
            reason  = confirm.get("reason", "")
            level   = confirm.get("level", "?")
            logger.info("Deal confirmed: status=%s  level=%s  reason=%s",
                        status, level, reason)
            return confirm
        except Exception as exc:
            logger.error("Could not confirm deal %s: %s", deal_reference, exc)
            return {"dealReference": deal_reference, "dealStatus": "UNKNOWN"}

    # ------------------------------------------------------------------
    # Close positions
    # ------------------------------------------------------------------

    def close_position(self, deal_id: str) -> dict:
        """Close a single open position by deal ID."""
        import time as _time
        # Retry once with a brief pause for IG post-fill propagation delay
        for attempt in range(2):
            positions = self.client.get_open_positions()
            for pos in positions.get("positions", []):
                if pos["position"]["dealId"] == deal_id:
                    direction = pos["position"]["direction"]
                    size      = pos["position"]["size"]
                    close_dir = "SELL" if direction == "BUY" else "BUY"
                    # dealId and epic/expiry are mutually exclusive in IG's API
                    payload = {
                        "dealId":      deal_id,
                        "direction":   close_dir,
                        "size":        str(size),
                        "orderType":   "MARKET",
                        "timeInForce": "FILL_OR_KILL",
                    }
                    logger.info("Closing position %s (%s, size=%s)", deal_id, direction, size)
                    resp     = self.client.delete("/positions/otc", payload, version="1")
                    deal_ref = resp.get("dealReference", "")
                    return self.client.get(f"/confirms/{deal_ref}") if deal_ref else resp
            if attempt == 0:
                _time.sleep(2)  # brief wait then retry
        raise ValueError(f"Deal ID {deal_id} not found in open positions.")

    def close_all_positions(self) -> list:
        """Close all open positions. Returns list of confirmations."""
        positions = self.client.get_open_positions().get("positions", [])
        if not positions:
            logger.info("No open positions to close.")
            return []

        results = []
        for pos in positions:
            deal_id = pos["position"]["dealId"]
            try:
                results.append(self.close_position(deal_id))
            except Exception as exc:
                logger.error("Failed to close %s: %s", deal_id, exc)
        return results

    # ------------------------------------------------------------------
    # Position query helpers
    # ------------------------------------------------------------------

    def get_open_position_count(self) -> int:
        """Return the number of currently open positions for this epic."""
        try:
            positions = self.client.get_open_positions().get("positions", [])
            return sum(1 for p in positions if p["market"]["epic"] == self.epic)
        except Exception:
            return 0

    def get_open_position_direction(self) -> str | None:
        """Return 'BUY', 'SELL', or None if no position open."""
        try:
            positions = self.client.get_open_positions().get("positions", [])
            for p in positions:
                if p["market"]["epic"] == self.epic:
                    return p["position"]["direction"]
        except Exception:
            pass
        return None
