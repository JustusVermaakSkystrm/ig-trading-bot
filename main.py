"""
main.py
-------
The live trading loop. Runs continuously, checking for a new 15-minute
candle every minute and placing trades when a high-confidence signal fires.

Flow:
  1. Login to IG
  2. Load or train the XGBoost model
  3. Every 15 minutes (on the bar close):
     a. Fetch recent prices
     b. Compute features
     c. Get signal from model
     d. If actionable → place trade via execution engine
  4. Log all activity

Usage:
    python main.py

Optional flags:
    python main.py --retrain        # retrain model before starting loop
    python main.py --dry-run        # log signals but do NOT place real trades
"""

import argparse
import logging
import os
import sys
import time
from datetime import datetime, timezone

import pandas as pd

from ig_client import IGClient
from data_pipeline import fetch_and_save, load_data, fetch_rolling_15min_bar, CSV_PATH
from features import compute_features
from model import TradingModel
from signal_engine import SignalEngine
from execution import ExecutionEngine

# ------------------------------------------------------------------
# Logging setup
# ------------------------------------------------------------------

LOG_PATH = os.path.join(os.path.dirname(__file__), "data", "trading_log.txt")
os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(LOG_PATH),
    ]
)
logger = logging.getLogger(__name__)

# ------------------------------------------------------------------
# Configuration
# ------------------------------------------------------------------

# Seconds to wait between each loop iteration
LOOP_INTERVAL_SECONDS = 60

# Retrain the model every N days (0 = never auto-retrain)
RETRAIN_EVERY_N_DAYS = 7

# Refresh historical data every N hours
DATA_REFRESH_HOURS = 12

# Maximum number of open positions at one time
MAX_OPEN_POSITIONS = 1

# Minimum gap (in bars) between consecutive trades to avoid overtrading
# With 5-min bars, 12 bars = 1 hour cooling-off between trades
MIN_BARS_BETWEEN_TRADES = 12  # = 1 hour at 5-min bars


# ------------------------------------------------------------------
# Helpers
# ------------------------------------------------------------------

def _market_is_open() -> bool:
    """
    Return True during forex market hours, False over the weekend.

    Spot forex trades roughly Monday 00:00 UTC through Friday 22:00 UTC.
    The weekend gap (Fri 22:00 → Sun 22:00 UTC) is treated as closed.
    """
    now     = datetime.now(tz=timezone.utc)
    weekday = now.weekday()   # 0=Mon … 6=Sun
    hour    = now.hour

    if weekday == 5:          # Saturday — always closed
        return False
    if weekday == 6 and hour < 22:   # Sunday before 22:00 UTC — still closed
        return False
    if weekday == 4 and hour >= 22:  # Friday after 22:00 UTC — closed
        return False
    return True


def _seconds_until_market_open() -> int:
    """
    Return seconds until the next Sunday 22:00 UTC market open.
    Only called when the market is currently closed.
    """
    now    = datetime.now(tz=timezone.utc)
    # Find next Sunday 22:00 UTC
    days_until_sunday = (6 - now.weekday()) % 7
    if days_until_sunday == 0 and now.hour >= 22:
        days_until_sunday = 7   # already past Sunday 22:00 — next week
    open_time = now.replace(hour=22, minute=0, second=0, microsecond=0)
    open_time = open_time + timedelta(days=days_until_sunday)
    return max(int((open_time - now).total_seconds()), 0)


def _seconds_until_next_5min_bar() -> int:
    """
    Return seconds until the next 5-minute candle closes.
    We loop every 5 minutes and build a rolling 15-min synthetic bar
    from the last three 5-min bars, giving signals 3× more often.
    """
    now     = datetime.now(tz=timezone.utc)
    minutes = now.minute % 5
    seconds = now.second
    wait    = (5 - minutes) * 60 - seconds
    return max(wait, 0)


def _append_rolling_bar(df_hist: pd.DataFrame) -> pd.DataFrame:
    """
    Fetch the latest three 5-minute candles, aggregate them into a
    synthetic 15-minute bar, and append it to the historical DataFrame.

    If the timestamp already exists (same 5-min close as last time),
    we overwrite it so the close price stays current.

    Returns the updated DataFrame.
    """
    new_bar = fetch_rolling_15min_bar()
    if new_bar.empty:
        logger.warning("Could not build rolling 15-min bar — using last historical bar.")
        return df_hist

    # Overwrite any row with the same timestamp, then sort
    df = pd.concat([df_hist, new_bar], ignore_index=True)
    df = df.drop_duplicates(subset="datetime", keep="last")
    df = df.sort_values("datetime").reset_index(drop=True)
    logger.info("Rolling 15-min bar appended: close=%.5f  ts=%s",
                new_bar["close"].iloc[0],
                new_bar["datetime"].iloc[0].strftime("%H:%M UTC"))
    return df


def _should_retrain(model_path: str, every_n_days: int) -> bool:
    """Return True if the model file is older than every_n_days days."""
    if not os.path.exists(model_path):
        return True
    if every_n_days == 0:
        return False
    age_seconds = time.time() - os.path.getmtime(model_path)
    return age_seconds > every_n_days * 86400


def _should_refresh_data(csv_path: str, every_n_hours: int) -> bool:
    """Return True if the CSV data file is older than every_n_hours hours."""
    if not os.path.exists(csv_path):
        return True
    age_seconds = time.time() - os.path.getmtime(csv_path)
    return age_seconds > every_n_hours * 3600


# ------------------------------------------------------------------
# Main loop
# ------------------------------------------------------------------

def run(dry_run: bool = False, retrain: bool = False):
    """
    Main entry point. Runs the live trading loop indefinitely.

    Parameters
    ----------
    dry_run : bool — if True, signals are logged but no orders are placed
    retrain : bool — if True, force retrain model before starting
    """
    logger.info("=" * 60)
    logger.info("IG EURUSD Automated Spread Betting System")
    logger.info("Mode: %s", "DRY RUN (no trades)" if dry_run else "LIVE TRADING")
    logger.info("=" * 60)

    # --- Login ---
    creds_path = os.path.join(os.path.dirname(__file__), "credentials.json")
    client = IGClient.from_credentials_file(creds_path)
    client.login()
    logger.info("Logged in to IG. Account: %s", client.account_id)

    # --- Initial data fetch ---
    if _should_refresh_data(CSV_PATH, DATA_REFRESH_HOURS) or retrain:
        logger.info("Fetching historical data...")
        fetch_and_save(months=6, client=client)   # reuse existing session

    # --- Train or load model ---
    from model import MODEL_PATH
    if retrain or _should_retrain(MODEL_PATH, RETRAIN_EVERY_N_DAYS):
        logger.info("Training model...")
        df_raw  = load_data()
        df_feat = compute_features(df_raw)
        model   = TradingModel()
        model.train(df_feat)
        model.save()
    else:
        logger.info("Loading existing model...")
        model = TradingModel.load()

    # --- Set up engines ---
    signal_engine = SignalEngine(client)
    signal_engine.model = model   # use the model we just trained/loaded

    exec_engine = ExecutionEngine(client)

    # --- State tracking ---
    last_signal_bar  = None    # datetime of last bar where a trade was placed
    bars_since_trade = 99      # high initial value = allow trade immediately

    logger.info("Entering live loop. Waiting for bar closes...")

    while True:
        try:
            # Pause over the weekend
            if not _market_is_open():
                wait = _seconds_until_market_open()
                logger.info(
                    "Market closed (weekend). Sleeping %.1f hours until Sunday 22:00 UTC.",
                    wait / 3600
                )
                time.sleep(wait)
                continue

            # Wait until the next 5-min bar closes
            wait = _seconds_until_next_5min_bar()
            logger.info("Next 5-min bar in %d seconds (%d min %d sec).",
                        wait, wait // 60, wait % 60)
            time.sleep(wait + 5)   # +5s buffer for the bar to fully settle

            now = datetime.now(tz=timezone.utc)
            logger.info("--- 5-min close: %s ---", now.strftime("%Y-%m-%d %H:%M UTC"))

            # Periodically refresh historical data and retrain
            if _should_refresh_data(CSV_PATH, DATA_REFRESH_HOURS):
                logger.info("Refreshing historical data...")
                fetch_and_save(months=6, client=client)   # reuse existing session

            if _should_retrain(MODEL_PATH, RETRAIN_EVERY_N_DAYS):
                logger.info("Scheduled model retrain...")
                df_raw  = load_data()
                df_feat = compute_features(df_raw)
                model.train(df_feat)
                model.save()
                signal_engine.model = model

            # --- Build rolling 15-min bar from latest 5-min data ---
            # Load saved history, then append a fresh synthetic 15-min bar
            # built from the last 3 × 5-min candles.  This gives a signal
            # every 5 minutes without waiting for a full 15-min close.
            df_base = load_data()
            df_base = _append_rolling_bar(df_base)

            # Compute features on the extended series and generate signal
            df_feat = compute_features(df_base)
            sig     = signal_engine.get_signal(df_feat=df_feat)
            bars_since_trade += 1

            logger.info(
                "Signal: %-4s  conf=%.1f%%  actionable=%s  price=%.5f",
                sig["label"], sig["confidence"] * 100,
                sig["actionable"], sig["latest_price"]
            )

            # --- Decide whether to trade ---
            if not sig["actionable"]:
                logger.info("Signal not actionable — skipping.")
                continue

            if bars_since_trade < MIN_BARS_BETWEEN_TRADES:
                logger.info("Too soon since last trade (%d bars). Waiting.", bars_since_trade)
                continue

            # Check existing positions (gracefully handle API errors)
            try:
                open_pos = client.get_open_positions().get("positions", [])
            except Exception as e:
                logger.warning("Could not fetch open positions (%s) — assuming 0 open.", e)
                open_pos = []
            n_open = len(open_pos)

            if n_open >= MAX_OPEN_POSITIONS:
                logger.info("%d position(s) already open (max=%d). Skipping new entry.",
                            n_open, MAX_OPEN_POSITIONS)
                continue

            # --- Place trade ---
            if dry_run:
                logger.info(
                    "[DRY RUN] Would place %s at %.5f (conf=%.1f%%)",
                    sig["label"], sig["latest_price"], sig["confidence"] * 100
                )
            else:
                logger.info("Placing %s trade...", sig["label"])
                atr = sig.get("atr", 0.0010)   # fallback ATR if not in signal dict

                # Try to get ATR from the feature data
                try:
                    df_raw  = load_data()
                    df_feat = compute_features(df_raw)
                    atr     = float(df_feat["atr"].iloc[-1])
                except Exception:
                    pass

                confirm = exec_engine.open_trade(
                    signal        = sig["signal"],
                    atr           = atr,
                    current_price = sig["latest_price"],
                )

                deal_status = confirm.get("dealStatus", "UNKNOWN")
                logger.info("Trade result: %s", deal_status)

                if deal_status == "ACCEPTED":
                    last_signal_bar  = sig["timestamp"]
                    bars_since_trade = 0

        except KeyboardInterrupt:
            logger.info("Shutting down — KeyboardInterrupt received.")
            break

        except Exception as e:
            logger.error("Unexpected error in main loop: %s", e, exc_info=True)
            logger.info("Sleeping 60s before retrying...")
            time.sleep(60)


# ------------------------------------------------------------------
# Entry point
# ------------------------------------------------------------------

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="IG EURUSD Automated Trading System")
    parser.add_argument("--dry-run",  action="store_true",
                        help="Log signals without placing real trades")
    parser.add_argument("--retrain",  action="store_true",
                        help="Force model retrain before starting")
    args = parser.parse_args()

    run(dry_run=args.dry_run, retrain=args.retrain)
