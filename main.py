"""
main.py
-------
Live automated trading loop for the EURUSD spread betting bot.

Architecture
------------
  Every 5 minutes (on bar close):
    1. Fetch latest 15-min candles from IG (or rebuild from 5-min bars)
    2. Compute all features (incl. DXY cross-asset, refreshed hourly)
    3. Run the binary XGBoost model (Triple Barrier trained, conf ≥ 0.65)
    4. If signal is actionable AND no position is open → place trade
    5. IG manages exit via native trailing stop (1.5 ATR initial distance)
    6. Log everything; weekly model retrain from fresh data

Optimal parameters (from 5-fold walk-forward, Oct 2025–Mar 2026):
  trailing_stop_atr_mult = 1.5 | min_confidence = 0.65
  → avg +49.8% per fold | Sharpe 22.6 | win rate 59.9%

Usage:
    python main.py                      # live trading
    python main.py --dry-run            # log signals, no orders
    python main.py --retrain            # retrain model then go live
    python main.py --dry-run --retrain  # retrain + dry run
"""

import argparse
import json
import logging
import os
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pandas as pd

from ig_client import IGClient
from data_pipeline import fetch_and_save, load_data, fetch_rolling_15min_bar, CSV_PATH
from features import compute_features
from model import TradingModel, MODEL_PATH
from signal_engine import SignalEngine
from execution import ExecutionEngine, STOP_ATR_MULTIPLE, TRAIL_INCREMENT_PIPS, MIN_CONFIDENCE
from notifier import Notifier

# ------------------------------------------------------------------
# Logging — console + file
# ------------------------------------------------------------------

DATA_DIR = Path(__file__).parent / "data"
DATA_DIR.mkdir(exist_ok=True)

LOG_PATH   = DATA_DIR / "trading_log.txt"
TRADE_LOG  = DATA_DIR / "trade_history.json"  # persisted trade records

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(LOG_PATH),
    ],
)
logger = logging.getLogger(__name__)

# ------------------------------------------------------------------
# Configuration
# ------------------------------------------------------------------

LOOP_INTERVAL_SECONDS  = 60     # how often to check for bar close
RETRAIN_EVERY_N_DAYS   = 7      # weekly scheduled retrain (0 = never)
DATA_REFRESH_HOURS     = 12     # re-fetch historical data every 12 h
MAX_OPEN_POSITIONS     = 1      # only 1 trade at a time
MIN_BARS_BETWEEN_TRADES = 12   # ≈ 1 hour cooldown between entries
HEARTBEAT_HOURS        = 4      # send Telegram status every N hours
CREDS_PATH             = Path(__file__).parent / "credentials.json"

# ------------------------------------------------------------------
# Helpers
# ------------------------------------------------------------------

def _market_is_open() -> bool:
    """True during forex market hours (Mon 00:00 – Fri 22:00 UTC)."""
    now     = datetime.now(tz=timezone.utc)
    weekday = now.weekday()  # 0=Mon … 6=Sun
    hour    = now.hour
    if weekday == 5:                     return False   # Saturday
    if weekday == 6 and hour < 22:       return False   # Sunday pre-open
    if weekday == 4 and hour >= 22:      return False   # Friday post-close
    return True


def _seconds_until_market_open() -> int:
    now = datetime.now(tz=timezone.utc)
    days_until_sunday = (6 - now.weekday()) % 7 or 7
    open_time = (now + timedelta(days=days_until_sunday)).replace(
        hour=22, minute=0, second=0, microsecond=0)
    return max(int((open_time - now).total_seconds()), 0)


def _seconds_until_next_5min_close() -> int:
    """Seconds until the next 5-minute boundary."""
    now     = datetime.now(tz=timezone.utc)
    minutes = now.minute % 5
    seconds = now.second
    return max((5 - minutes) * 60 - seconds, 0)


def _append_rolling_bar(df_hist: pd.DataFrame, client: IGClient) -> pd.DataFrame:
    """
    Build a synthetic 15-min bar from the last three 5-min candles
    and append it to the historical DataFrame.
    """
    try:
        new_bar = fetch_rolling_15min_bar(client=client)
    except Exception as exc:
        logger.warning("Rolling bar build failed (%s) — using historical tail", exc)
        return df_hist

    if new_bar is None or new_bar.empty:
        return df_hist

    df = pd.concat([df_hist, new_bar], ignore_index=True)
    df = df.drop_duplicates(subset="datetime", keep="last")
    df = df.sort_values("datetime").reset_index(drop=True)
    logger.debug("Rolling 15-min bar: close=%.5f  @%s",
                 float(new_bar["close"].iloc[0]),
                 new_bar["datetime"].iloc[0].strftime("%H:%M UTC"))
    return df


def _stale(path: str, max_seconds: float) -> bool:
    if not os.path.exists(path):
        return True
    return (time.time() - os.path.getmtime(path)) > max_seconds


def _train_model(client: IGClient = None) -> TradingModel:
    """Fetch fresh data, compute features, train binary model, save."""
    logger.info("Fetching historical data for model training...")
    if client:
        fetch_and_save(months=6, client=client)
    df_raw  = load_data()
    df_feat = compute_features(df_raw)
    logger.info("Training binary XGBoost model (Triple Barrier labels)...")
    model = TradingModel(binary=True)
    model.train(df_feat)
    model.save()
    logger.info("Model trained and saved → %s", MODEL_PATH)
    return model


# ------------------------------------------------------------------
# Trade-history persistence
# ------------------------------------------------------------------

def _load_trade_history() -> list:
    if TRADE_LOG.exists():
        try:
            return json.loads(TRADE_LOG.read_text())
        except Exception:
            pass
    return []


def _save_trade(record: dict) -> None:
    history = _load_trade_history()
    history.append(record)
    TRADE_LOG.write_text(json.dumps(history, indent=2, default=str))


def _print_session_stats(history: list) -> None:
    if not history:
        return
    total_pnl = sum(r.get("pnl_est", 0) for r in history)
    wins  = sum(1 for r in history if r.get("pnl_est", 0) > 0)
    total = len(history)
    logger.info("Session stats: %d trades | %d wins (%.0f%%) | est. P&L: £%.2f",
                total, wins, 100 * wins / total if total else 0, total_pnl)


# ------------------------------------------------------------------
# Main trading loop
# ------------------------------------------------------------------

def run(dry_run: bool = False, retrain: bool = False, fixed_size: float = None) -> None:
    logger.info("=" * 60)
    logger.info("  IG EURUSD Automated Spread Betting System")
    logger.info("  Mode: %s", "DRY RUN (no real orders)" if dry_run else "LIVE TRADING")
    logger.info("  TrailingStop=%.1f×ATR  Increment=%.1f pts  Confidence≥%.0f%%",
                STOP_ATR_MULTIPLE, TRAIL_INCREMENT_PIPS, MIN_CONFIDENCE * 100)
    if fixed_size:
        logger.info("  Fixed size: £%.2f/point (override)", fixed_size)
    logger.info("=" * 60)

    # ── 1. Connect to IG ──────────────────────────────────────────────
    client = IGClient.from_credentials_file(str(CREDS_PATH))
    client.login()
    logger.info("Connected to IG. Account: %s", client.account_id)

    # ── 2. Train or load model ────────────────────────────────────────
    if retrain or not os.path.exists(MODEL_PATH):
        model = _train_model(client=client)
    else:
        logger.info("Loading saved model from %s", MODEL_PATH)
        model = TradingModel.load()
        # Quick sanity: confirm it's binary-mode
        if not getattr(model, "binary", False):
            logger.warning("Saved model is not binary mode — retraining...")
            model = _train_model(client=client)

    # ── 3. Wire up engines ────────────────────────────────────────────
    sig_engine  = SignalEngine(client)
    sig_engine.model = model
    exec_engine = ExecutionEngine(client)
    notifier    = Notifier()
    # Fixed-size override (e.g. --min-size for testing with 0.01 £/point)
    _fixed_size = fixed_size

    notifier.bot_started(
        mode       = "DRY RUN" if dry_run else "LIVE TRADING",
        account_id = client.account_id,
    )

    # ── 4. State ─────────────────────────────────────────────────────
    bars_since_trade = 99          # start high so first signal can fire
    session_history  = []
    open_deal_id        = None        # track our deal so we can report P&L on close
    open_deal_direction = None        # "BUY" or "SELL"
    last_heartbeat      = datetime.now(tz=timezone.utc)
    last_sig            = {"label": "—", "confidence": 0.0, "latest_price": 0.0}

    logger.info("Live loop started. Waiting for bar closes...")

    while True:
        try:
            # ── Weekend check ──────────────────────────────────────────
            if not _market_is_open():
                wait = _seconds_until_market_open()
                logger.info("Market closed. Resuming in %.1f hours (Sunday 22:00 UTC).",
                            wait / 3600)
                _print_session_stats(session_history)
                time.sleep(min(wait, 3600))  # wake every hour max to re-check
                continue

            # ── Wait for next 5-min bar close ─────────────────────────
            wait = _seconds_until_next_5min_close()
            logger.debug("Next 5-min bar close in %ds", wait)
            time.sleep(wait + 3)   # +3s buffer for bar to settle

            now = datetime.now(tz=timezone.utc)
            logger.info("── %s ──", now.strftime("%Y-%m-%d %H:%M UTC"))

            # ── Periodic data refresh ─────────────────────────────────
            if _stale(CSV_PATH, DATA_REFRESH_HOURS * 3600):
                logger.info("Refreshing historical data...")
                try:
                    fetch_and_save(months=6, client=client)
                except Exception as exc:
                    logger.warning("Data refresh failed: %s", exc)

            # ── Scheduled model retrain ───────────────────────────────
            if RETRAIN_EVERY_N_DAYS > 0 and _stale(MODEL_PATH, RETRAIN_EVERY_N_DAYS * 86400):
                logger.info("Scheduled weekly retrain...")
                try:
                    model = _train_model(client=client)
                    sig_engine.model = model
                except Exception as exc:
                    logger.error("Retrain failed: %s", exc)

            # ── Build feature matrix ──────────────────────────────────
            try:
                df_base = load_data()
                df_base = _append_rolling_bar(df_base, client)
                df_feat = compute_features(df_base)
            except Exception as exc:
                logger.error("Feature computation failed: %s", exc)
                time.sleep(60)
                continue

            # ── Get signal ────────────────────────────────────────────
            sig = sig_engine.get_signal(df_feat=df_feat)
            bars_since_trade += 1
            last_sig = sig

            logger.info(
                "Signal: %-4s  conf=%.1f%%  p_buy=%.1f%%  p_sell=%.1f%%  "
                "regime=%-7s  actionable=%s  price=%.5f  ATR=%.5f",
                sig["label"], sig["confidence"] * 100,
                sig["p_buy"] * 100, sig["p_sell"] * 100,
                sig.get("regime", "?"), sig["actionable"],
                sig["latest_price"], sig["atr"],
            )

            # ── Periodic heartbeat ────────────────────────────────────
            if (datetime.now(tz=timezone.utc) - last_heartbeat).total_seconds() >= HEARTBEAT_HOURS * 3600:
                notifier.heartbeat(
                    label            = last_sig["label"],
                    confidence       = last_sig["confidence"],
                    price            = last_sig["latest_price"],
                    bars_since_trade = bars_since_trade,
                    open_deal_id     = open_deal_id,
                    open_direction   = open_deal_direction,
                    regime           = last_sig.get("regime", "NEUTRAL"),
                )
                last_heartbeat = datetime.now(tz=timezone.utc)

            # ── Check if our open position has been closed by IG ──────
            if open_deal_id:
                try:
                    open_positions = client.get_open_positions().get("positions", [])
                    open_ids = {p["position"]["dealId"] for p in open_positions}
                    if open_deal_id not in open_ids:
                        logger.info("Position %s closed by IG (SL or TP hit).",
                                    open_deal_id)
                        # Try to get P&L from confirms endpoint
                        try:
                            closed_info = client.get(f"/confirms/{open_deal_id}")
                            profit   = closed_info.get("profit") or 0.0
                            currency = closed_info.get("profitCurrency", "GBP")
                            close_level = closed_info.get("level", 0.0)
                        except Exception:
                            profit, currency, close_level = 0.0, "GBP", 0.0
                        notifier.trade_closed(
                            deal_id     = open_deal_id,
                            close_level = close_level,
                            profit      = profit,
                            currency    = currency,
                        )
                        open_deal_id        = None
                        open_deal_direction = None
                        bars_since_trade    = 0
                except Exception as exc:
                    logger.warning("Could not check position status: %s", exc)

            # ── Entry logic ───────────────────────────────────────────
            if not sig["actionable"]:
                # Log why specifically if a confident signal was regime-blocked
                if (sig["signal"] != 0
                        and sig["confidence"] >= MIN_CONFIDENCE
                        and not sig.get("regime_ok", True)):
                    logger.info(
                        "Regime filter blocked %s (conf=%.0f%%) — SG regime is %s",
                        sig["label"], sig["confidence"] * 100, sig.get("regime", "?"),
                    )
                    notifier.trade_rejected(
                        sig["label"],
                        f"SG regime filter: model says {sig['label']} but "
                        f"SG(11/61) regime is {sig.get('regime', '?')}",
                    )
                continue

            if bars_since_trade < MIN_BARS_BETWEEN_TRADES:
                logger.info("Cooldown: %d/%d bars since last trade.",
                            bars_since_trade, MIN_BARS_BETWEEN_TRADES)
                continue

            # Count open positions
            try:
                n_open = exec_engine.get_open_position_count()
            except Exception:
                n_open = 0

            if n_open >= MAX_OPEN_POSITIONS:
                logger.info("%d position(s) open (max %d) — skipping.",
                            n_open, MAX_OPEN_POSITIONS)
                continue

            # ── Place or simulate trade ───────────────────────────────
            trade_record = {
                "timestamp":    sig["timestamp"],
                "signal":       sig["label"],
                "confidence":   sig["confidence"],
                "price":        sig["latest_price"],
                "atr":          sig["atr"],
                "dry_run":      dry_run,
            }

            if dry_run:
                trail_pips = round((sig["atr"] * STOP_ATR_MULTIPLE) / 0.0001, 1)
                logger.info(
                    "[DRY RUN] %s @ %.5f  trailing_stop=%.1f pts  "
                    "ATR=%.5f  conf=%.1f%%",
                    sig["label"], sig["latest_price"],
                    trail_pips,
                    sig["atr"], sig["confidence"] * 100,
                )
                notifier.trade_opened(
                    direction      = sig["label"],
                    size           = _fixed_size or 0.01,
                    fill_level     = sig["latest_price"],
                    trail_distance = trail_pips,
                    confidence     = sig["confidence"],
                    atr            = sig["atr"],
                    deal_id        = "DRY-RUN",
                )
                trade_record["status"] = "DRY_RUN"
                session_history.append(trade_record)
                bars_since_trade = 0

            else:
                logger.info("Placing %s trade...", sig["label"])
                try:
                    confirm     = exec_engine.open_trade(
                        signal        = sig["signal"],
                        atr           = sig["atr"],
                        current_price = sig["latest_price"],
                        size          = _fixed_size,   # None = auto-size from balance
                    )
                    deal_status = confirm.get("dealStatus", "UNKNOWN")
                    deal_id     = confirm.get("dealId", "")
                    fill_level  = confirm.get("level", sig["latest_price"])

                    logger.info("Trade result: %s  dealId=%s  level=%s",
                                deal_status, deal_id, fill_level)

                    trade_record.update({
                        "deal_status": deal_status,
                        "deal_id":     deal_id,
                        "fill_level":  fill_level,
                    })

                    if deal_status == "ACCEPTED":
                        trail_pips = round((sig["atr"] * STOP_ATR_MULTIPLE) / 0.0001, 1)
                        notifier.trade_opened(
                            direction      = sig["label"],
                            size           = confirm.get("size", _fixed_size or 0.01),
                            fill_level     = fill_level,
                            trail_distance = trail_pips,
                            confidence     = sig["confidence"],
                            atr            = sig["atr"],
                            deal_id        = deal_id,
                        )
                        open_deal_id        = deal_id
                        open_deal_direction = sig["label"]   # "BUY" or "SELL"
                        bars_since_trade    = 0
                        session_history.append(trade_record)
                        _save_trade(trade_record)
                    else:
                        reason = confirm.get("reason", "")
                        logger.warning("Trade rejected: %s", reason)
                        notifier.trade_rejected(sig["label"], reason)

                except Exception as exc:
                    logger.error("Trade execution failed: %s", exc)

        except KeyboardInterrupt:
            logger.info("Shutdown requested (Ctrl+C).")
            break

        except Exception as exc:
            logger.error("Unhandled error: %s", exc, exc_info=True)
            logger.info("Sleeping 60s before retrying...")
            time.sleep(60)

    # ── Graceful shutdown ─────────────────────────────────────────────
    logger.info("Bot stopped.")
    _print_session_stats(session_history)


# ------------------------------------------------------------------
# Entry point
# ------------------------------------------------------------------

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="IG EURUSD Automated Trading Bot")
    parser.add_argument("--dry-run",  action="store_true",
                        help="Log signals but do NOT place real trades")
    parser.add_argument("--retrain",  action="store_true",
                        help="Force model retrain before starting the loop")
    parser.add_argument("--min-size", action="store_true",
                        help="Force minimum position size (0.01 £/point) — useful for testing")
    args = parser.parse_args()

    fixed_size = 0.01 if args.min_size else None
    run(dry_run=args.dry_run, retrain=args.retrain, fixed_size=fixed_size)
