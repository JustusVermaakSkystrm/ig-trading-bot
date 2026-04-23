"""
notifier.py
-----------
Sends trade notifications via Telegram.

Setup (one-time):
  1. Message @BotFather on Telegram → /newbot → copy the token
  2. Message @userinfobot on Telegram → copy your Chat ID
  3. Set environment variables (or add to credentials.json):
       TELEGRAM_BOT_TOKEN = 123456789:ABCdef...
       TELEGRAM_CHAT_ID   = 987654321

The notifier silently no-ops if the env vars are not set, so the bot
continues trading even if Telegram is not configured.
"""

import html as _html
import logging
import os
import requests

logger = logging.getLogger(__name__)

TELEGRAM_API = "https://api.telegram.org/bot{token}/sendMessage"


class Notifier:
    """Sends Telegram messages on trade events."""

    def __init__(self, token: str = None, chat_id: str = None):
        self.token   = token   or os.environ.get("TELEGRAM_BOT_TOKEN", "")
        self.chat_id = chat_id or os.environ.get("TELEGRAM_CHAT_ID",   "")
        self.enabled = bool(self.token and self.chat_id)
        if not self.enabled:
            logger.info("Notifier: TELEGRAM_BOT_TOKEN / TELEGRAM_CHAT_ID not set — notifications disabled.")

    # ------------------------------------------------------------------

    def send(self, message: str) -> bool:
        """Send a Telegram message with HTML formatting. Returns True on success.

        If Telegram rejects the HTML (400), automatically retries as plain text
        so the notification always arrives even if formatting is broken.
        """
        if not self.enabled:
            return False
        url = TELEGRAM_API.format(token=self.token)
        try:
            resp = requests.post(
                url,
                json={"chat_id": self.chat_id, "text": message, "parse_mode": "HTML"},
                timeout=10,
            )
            if resp.ok:
                return True
            # HTML parse error → strip tags and retry as plain text
            if resp.status_code == 400:
                logger.warning(
                    "Telegram HTML parse error — retrying as plain text. "
                    "Detail: %s", resp.text[:200],
                )
                import re
                plain = re.sub(r"<[^>]+>", "", message)
                resp2 = requests.post(
                    url,
                    json={"chat_id": self.chat_id, "text": plain},
                    timeout=10,
                )
                if resp2.ok:
                    return True
                logger.warning("Telegram plain-text retry also failed: %s %s",
                               resp2.status_code, resp2.text[:200])
            else:
                logger.warning("Telegram send failed: %s %s",
                               resp.status_code, resp.text[:200])
            return False
        except Exception as exc:
            logger.warning("Telegram notification error: %s", exc)
            return False

    # ------------------------------------------------------------------
    # Trade event helpers
    # ------------------------------------------------------------------

    def trade_opened(self, direction: str, size: float, fill_level: float,
                     trail_distance: float,
                     confidence: float, atr: float, deal_id: str) -> None:
        emoji = "🟢" if direction == "BUY" else "🔴"
        msg = (
            f"{emoji} <b>TRADE OPENED — {direction}</b>\n"
            f"Fill:           <b>{fill_level:.5f}</b>\n"
            f"Size:           £{size:.2f}/point\n"
            f"Trailing stop:  {trail_distance:.1f} pts (moves with price)\n"
            f"Confidence:     {confidence*100:.1f}%\n"
            f"ATR:            {atr:.5f}\n"
            f"Deal ID:        <code>{deal_id}</code>"
        )
        self.send(msg)

    def trade_closed(self, deal_id: str, close_level: float,
                     profit: float, currency: str = "GBP") -> None:
        emoji = "💰" if profit >= 0 else "💸"
        sign  = "+" if profit >= 0 else ""
        msg = (
            f"{emoji} <b>TRADE CLOSED</b>\n"
            f"Close:   <b>{close_level:.5f}</b>\n"
            f"P&L:     <b>{sign}{profit:.2f} {currency}</b>\n"
            f"Deal ID: <code>{deal_id}</code>"
        )
        self.send(msg)

    def trade_rejected(self, direction: str, reason: str) -> None:
        msg = (
            f"⚠️ <b>TRADE REJECTED — {direction}</b>\n"
            f"Reason: {_html.escape(str(reason))}"
        )
        self.send(msg)

    def bot_started(self, mode: str, account_id: str) -> None:
        msg = (
            f"🤖 <b>Bot started</b>\n"
            f"Mode:    {mode}\n"
            f"Account: {account_id}\n"
            f"Size:    0.01 £/point (minimum)"
        )
        self.send(msg)

    def bot_error(self, error: str) -> None:
        self.send(f"🚨 <b>Bot error</b>\n<code>{_html.escape(str(error)[:300])}</code>")

    def heartbeat(self, label: str, confidence: float, price: float,
                  bars_since_trade: int, open_deal_id: str = None,
                  open_direction: str = None, regime: str = "NEUTRAL") -> None:
        if open_deal_id:
            position_str = f"📌 {open_direction} open — trailing stop active"
            signal_note = ""
            if open_direction and label not in ("HOLD", "—"):
                if label != open_direction:
                    signal_note = f"\n⚠️ Model now prefers {label} but position held — trailing stop manages exit"
                else:
                    signal_note = f"\n✅ Model agrees: stay {open_direction}"
        else:
            position_str = "No open position"
            signal_note  = ""

        regime_emoji = {"BULL": "📈", "BEAR": "📉", "NEUTRAL": "➡️"}.get(regime, "➡️")

        msg = (
            f"🫀 <b>Bot heartbeat</b>\n"
            f"Position:    {position_str}\n"
            f"Last signal: <b>{label}</b> ({confidence*100:.1f}% conf)\n"
            f"SG regime:   {regime_emoji} {regime}\n"
            f"Price:       {price:.5f}"
            f"{signal_note}"
        )
        self.send(msg)
