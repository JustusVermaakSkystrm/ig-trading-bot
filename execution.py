"""
execution.py
------------
Handles order placement and position management via the IG API.

Features:
  - Open a spread bet position (BUY or SELL)
  - Automatic stop-loss and take-profit based on ATR
  - Close an existing position
  - Position size calculated from account balance + risk %

Risk management:
  - Risk a fixed % of account balance per trade (default 1%)
  - Stop loss = ATR × STOP_ATR_MULTIPLE
  - Take profit = ATR × TP_ATR_MULTIPLE

Usage:
    from execution import ExecutionEngine
    engine = ExecutionEngine(client)
    deal_ref = engine.open_trade(signal=1, atr=0.0010, current_price=1.0950)
"""

import logging
from datetime import datetime, timezone

from ig_client import IGClient

logger = logging.getLogger(__name__)

# ------------------------------------------------------------------
# Risk management constants
# ------------------------------------------------------------------

RISK_PER_TRADE_PCT   = 1.0     # % of account balance to risk per trade
STOP_ATR_MULTIPLE    = 2.0     # stop loss = ATR × this
TP_ATR_MULTIPLE      = 3.0     # take profit = ATR × this (risk:reward = 1:1.5)
MIN_SIZE             = 0.5     # minimum spread bet size (£ per pip — check IG for your market)
MAX_SIZE             = 10.0    # safety cap on position size (£ per pip)

# IG epic and pip value for EUR/USD
EPIC            = "CS.D.EURUSD.TODAY.IP"
PIP_VALUE_GBP   = 10.0    # £10 per pip for a £1/pip bet (EUR/USD pip = 0.0001)
# Adjust PIP_VALUE_GBP if IG shows a different figure for your account currency


class ExecutionEngine:
    """
    Places and manages spread bet positions through the IG API.
    """

    def __init__(self, client: IGClient, epic: str = EPIC):
        self.client = client
        self.epic   = epic

    # ------------------------------------------------------------------
    # Account helpers
    # ------------------------------------------------------------------

    def get_account_balance(self) -> float:
        """Fetch the current available funds from the IG account."""
        accounts = self.client.get_accounts()
        for acc in accounts.get("accounts", []):
            if acc.get("accountId") == self.client.account_id:
                return float(acc.get("balance", {}).get("available", 0))
        # Fallback: first account
        first = accounts.get("accounts", [{}])[0]
        return float(first.get("balance", {}).get("available", 0))

    # ------------------------------------------------------------------
    # Position sizing
    # ------------------------------------------------------------------

    def calculate_size(self, atr: float, balance: float = None) -> float:
        """
        Calculate position size (£ per pip) using fixed fractional risk.

        Formula:
            risk_amount = balance × risk_pct
            stop_distance_pips = ATR × STOP_ATR_MULTIPLE / 0.0001
            size = risk_amount / (stop_distance_pips × pip_value_per_unit)

        For EUR/USD spread betting, 1 pip = 0.0001.
        """
        if balance is None:
            balance = self.get_account_balance()

        risk_amount        = balance * (RISK_PER_TRADE_PCT / 100)
        stop_distance_pips = (atr * STOP_ATR_MULTIPLE) / 0.0001
        raw_size           = risk_amount / (stop_distance_pips * 1.0)  # £ per pip

        # Clamp to sensible bounds
        size = max(MIN_SIZE, min(raw_size, MAX_SIZE))
        size = round(size, 1)  # IG typically accepts 1 decimal place

        logger.info(
            "Position sizing: balance=£%.2f  risk=£%.2f  ATR=%.5f  "
            "stop_pips=%.1f  size=£%.1f/pip",
            balance, risk_amount, atr, stop_distance_pips, size
        )
        return size

    # ------------------------------------------------------------------
    # Trade entry
    # ------------------------------------------------------------------

    def open_trade(self, signal: int, atr: float, current_price: float,
                   size: float = None) -> dict:
        """
        Open a spread bet position.

        Parameters
        ----------
        signal        : 1 = BUY, -1 = SELL
        atr           : current ATR (used for stop/TP calculation)
        current_price : current mid price
        size          : override position size (if None, calculated automatically)

        Returns
        -------
        dict from IG API with deal reference and status.
        """
        if signal not in (1, -1):
            raise ValueError(f"signal must be 1 (BUY) or -1 (SELL), got {signal}")

        direction = "BUY" if signal == 1 else "SELL"

        if size is None:
            size = self.calculate_size(atr)

        stop_distance = round(atr * STOP_ATR_MULTIPLE, 5)
        tp_distance   = round(atr * TP_ATR_MULTIPLE,   5)

        # Convert price distances to pips (EUR/USD: 1 pip = 0.0001)
        stop_pips = round(stop_distance / 0.0001, 1)
        tp_pips   = round(tp_distance   / 0.0001, 1)

        payload = {
            "epic":                 self.epic,
            "expiry":               "DFB",        # daily funded bet (rolling)
            "direction":            direction,
            "size":                 str(size),
            "orderType":            "MARKET",
            "timeInForce":          "FILL_OR_KILL",
            "guaranteedStop":       False,
            "trailingStop":         False,
            "stopDistance":         str(stop_pips),
            "profitDistance":       str(tp_pips),
            "forceOpen":            True,          # allow hedging
            "currencyCode":         "GBP",
        }

        logger.info(
            "Opening %s  size=£%.1f/pip  stop=%.1fpips  tp=%.1fpips  price=%.5f",
            direction, size, stop_pips, tp_pips, current_price
        )

        response = self.client.post("/positions/otc", payload, version="2")

        deal_ref = response.get("dealReference", "UNKNOWN")
        logger.info("Deal reference: %s", deal_ref)

        # Confirm the trade
        confirm = self._confirm_deal(deal_ref)
        return confirm

    def _confirm_deal(self, deal_reference: str) -> dict:
        """Fetch the deal confirmation from IG."""
        try:
            confirm = self.client.get(f"/confirms/{deal_reference}")
            status  = confirm.get("dealStatus", "UNKNOWN")
            reason  = confirm.get("reason", "")
            logger.info("Deal status: %s  reason: %s", status, reason)
            return confirm
        except Exception as e:
            logger.error("Could not confirm deal %s: %s", deal_reference, e)
            return {"dealReference": deal_reference, "dealStatus": "UNKNOWN"}

    # ------------------------------------------------------------------
    # Trade exit
    # ------------------------------------------------------------------

    def close_all_positions(self) -> list:
        """
        Close all open positions for this account.
        Returns a list of close confirmations.
        """
        positions = self.client.get_open_positions()
        open_pos  = positions.get("positions", [])

        if not open_pos:
            logger.info("No open positions to close.")
            return []

        results = []
        for pos in open_pos:
            deal_id   = pos["position"]["dealId"]
            direction = pos["position"]["direction"]
            size      = pos["position"]["size"]
            epic      = pos["market"]["epic"]

            # To close: trade in the OPPOSITE direction
            close_dir = "SELL" if direction == "BUY" else "BUY"

            payload = {
                "dealId":    deal_id,
                "epic":      epic,
                "expiry":    "DFB",
                "direction": close_dir,
                "size":      str(size),
                "orderType": "MARKET",
                "timeInForce": "FILL_OR_KILL",
            }

            logger.info("Closing position %s (%s %s)...", deal_id, direction, epic)

            try:
                result = self.client.delete("/positions/otc", payload, version="1")
                results.append(result)
            except Exception as e:
                logger.error("Failed to close position %s: %s", deal_id, e)

        return results

    def close_position(self, deal_id: str) -> dict:
        """Close a single position by deal ID."""
        positions = self.client.get_open_positions()
        for pos in positions.get("positions", []):
            if pos["position"]["dealId"] == deal_id:
                direction = pos["position"]["direction"]
                size      = pos["position"]["size"]
                epic      = pos["market"]["epic"]
                close_dir = "SELL" if direction == "BUY" else "BUY"

                payload = {
                    "dealId":    deal_id,
                    "epic":      epic,
                    "expiry":    "DFB",
                    "direction": close_dir,
                    "size":      str(size),
                    "orderType": "MARKET",
                    "timeInForce": "FILL_OR_KILL",
                }
                return self.client.delete("/positions/otc", payload, version="1")

        raise ValueError(f"Deal ID {deal_id} not found in open positions.")
