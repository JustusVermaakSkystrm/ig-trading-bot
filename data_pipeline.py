"""
data_pipeline.py
----------------
Fetches historical 15-minute EURUSD price data from the IG API
and stores it as a CSV file in the data/ folder.

Key features:
  - Paginated requests (IG caps at 1000 candles per call)
  - Automatic gap-filling from Yahoo Finance (yfinance) as a fallback
  - Mid-price calculated as (bid + ask) / 2
  - Deduplication and sorting

Usage:
    python data_pipeline.py

Or import and call programmatically:
    from data_pipeline import fetch_and_save
    df = fetch_and_save(months=6)
"""

import json
import logging
import os
import time
from datetime import datetime, timedelta, timezone

import pandas as pd
import yfinance as yf

from ig_client import IGClient

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

# ------------------------------------------------------------------
# Configuration
# ------------------------------------------------------------------

# How many months of 15-min history to fetch
DEFAULT_MONTHS = 6

# IG resolution string for 15-minute candles
RESOLUTION = "MINUTE_15"

# IG limits each /prices request to 1000 candles
MAX_CANDLES_PER_REQUEST = 1000

# Path to save/load the CSV
DATA_DIR  = os.path.join(os.path.dirname(__file__), "data")
CSV_PATH  = os.path.join(DATA_DIR, "eurusd_15min.csv")

# IG epic for EUR/USD spread bet (daily funded)
# If this doesn't work for your account, run find_eurusd_epic() below
DEFAULT_EPIC = "CS.D.EURUSD.TODAY.IP"

# Small pause between paginated API calls to avoid rate-limit errors
REQUEST_DELAY_SECONDS = 0.5


# ------------------------------------------------------------------
# Epic discovery helper
# ------------------------------------------------------------------

def find_eurusd_epic(client: IGClient) -> str:
    """
    Search the IG API for EURUSD markets and print matching epics.
    Run this once if DEFAULT_EPIC doesn't match your account type.
    """
    results = client.search_markets("EURUSD")
    markets = results.get("markets", [])

    if not markets:
        logger.warning("No markets found for 'EURUSD'. Check your credentials.")
        return None

    logger.info("Found %d EURUSD markets:", len(markets))
    for m in markets:
        logger.info("  Epic: %-40s  Name: %s", m.get("epic"), m.get("instrumentName"))

    # Return the first result (usually the daily funded spread bet)
    return markets[0]["epic"]


# ------------------------------------------------------------------
# Date range helpers
# ------------------------------------------------------------------

def _split_date_range(start: datetime, end: datetime, candles_per_chunk: int,
                      minutes_per_candle: int = 15):
    """
    Split a date range into chunks that each contain at most
    candles_per_chunk candles, yielding (chunk_start, chunk_end) pairs.
    """
    chunk_duration = timedelta(minutes=minutes_per_candle * candles_per_chunk)
    current = start
    while current < end:
        chunk_end = min(current + chunk_duration, end)
        yield current, chunk_end
        current = chunk_end


def _to_ig_date(dt: datetime) -> str:
    """Convert a datetime to the format IG expects: YYYY-MM-DDTHH:MM:SS"""
    return dt.strftime("%Y-%m-%dT%H:%M:%S")


# ------------------------------------------------------------------
# IG data fetching
# ------------------------------------------------------------------

def _safe_div(value, divisor):
    """Divide value by divisor, returning None if value is None."""
    return value / divisor if value is not None else None


def _fetch_chunk(client: IGClient, epic: str, start: datetime, end: datetime) -> pd.DataFrame:
    """
    Fetch a single chunk of 15-min candles from IG for the given date range.
    Returns a DataFrame with columns: datetime, open, high, low, close, volume
    """
    params = {
        "resolution": RESOLUTION,
        "from":       _to_ig_date(start),
        "to":         _to_ig_date(end),
        "max":        MAX_CANDLES_PER_REQUEST,
        "pageSize":   0,  # 0 = return all in one go (up to max)
    }

    try:
        data = client.get(f"/prices/{epic}", params=params, version="3")
    except Exception as e:
        logger.error("API error fetching %s to %s: %s", start, end, e)
        return pd.DataFrame()

    candles = data.get("prices", [])
    if not candles:
        return pd.DataFrame()

    rows = []
    for c in candles:
        # IG returns bid/ask for each OHLC point — we use the mid
        def mid(price_obj):
            if price_obj is None:
                return None
            bid = price_obj.get("bid")
            ask = price_obj.get("ask")
            if bid is None or ask is None:
                return None
            return (bid + ask) / 2

        # IG snapshot time format: "2024/01/15 09:15:00:000"
        raw_time = c.get("snapshotTime", "")
        try:
            # Strip milliseconds and parse
            dt = datetime.strptime(raw_time[:19], "%Y/%m/%d %H:%M:%S")
            dt = dt.replace(tzinfo=timezone.utc)
        except ValueError:
            continue

        # IG spread betting prices for EURUSD are quoted in points
        # (e.g. 11572.2 = actual rate 1.15722), so divide by 10,000
        scale = 10_000.0
        rows.append({
            "datetime": dt,
            "open":     _safe_div(mid(c.get("openPrice")),  scale),
            "high":     _safe_div(mid(c.get("highPrice")),  scale),
            "low":      _safe_div(mid(c.get("lowPrice")),   scale),
            "close":    _safe_div(mid(c.get("closePrice")), scale),
            "volume":   c.get("lastTradedVolume", 0),
        })

    return pd.DataFrame(rows)


def fetch_from_ig(client: IGClient, epic: str, months: int = DEFAULT_MONTHS) -> pd.DataFrame:
    """
    Fetch all available 15-min candles for the last `months` months
    by making multiple paginated requests.
    """
    end   = datetime.now(tz=timezone.utc)
    start = end - timedelta(days=months * 30)

    logger.info("Fetching 15-min data for %s from %s to %s", epic, start.date(), end.date())

    chunks = list(_split_date_range(start, end, MAX_CANDLES_PER_REQUEST))
    logger.info("Splitting into %d API requests...", len(chunks))

    all_frames = []
    for i, (chunk_start, chunk_end) in enumerate(chunks):
        logger.info("  Request %d/%d: %s → %s", i + 1, len(chunks),
                    chunk_start.strftime("%Y-%m-%d %H:%M"),
                    chunk_end.strftime("%Y-%m-%d %H:%M"))

        df = _fetch_chunk(client, epic, chunk_start, chunk_end)
        if not df.empty:
            all_frames.append(df)

        time.sleep(REQUEST_DELAY_SECONDS)

    if not all_frames:
        logger.warning("No data returned from IG API.")
        return pd.DataFrame()

    combined = pd.concat(all_frames, ignore_index=True)
    combined = combined.drop_duplicates(subset="datetime").sort_values("datetime")
    combined = combined.reset_index(drop=True)

    logger.info("Fetched %d candles from IG.", len(combined))
    return combined


# ------------------------------------------------------------------
# Yahoo Finance fallback for gap-filling
# ------------------------------------------------------------------

def fetch_from_yfinance(months: int = DEFAULT_MONTHS) -> pd.DataFrame:
    """
    Fetch 15-min EURUSD data from Yahoo Finance as a gap-fill fallback.
    Note: Yahoo Finance only returns ~60 days of 15-min history.
    """
    logger.info("Fetching fallback data from Yahoo Finance (yfinance)...")

    # Yahoo Finance caps 15-min history at ~60 days, so clip if needed
    days = min(months * 30, 59)
    end   = datetime.now(tz=timezone.utc)
    start = end - timedelta(days=days)

    ticker = yf.Ticker("EURUSD=X")
    df = ticker.history(start=start, end=end, interval="15m")

    if df.empty:
        logger.warning("yfinance returned no data.")
        return pd.DataFrame()

    df = df.reset_index()
    df = df.rename(columns={
        "Datetime": "datetime",
        "Open":     "open",
        "High":     "high",
        "Low":      "low",
        "Close":    "close",
        "Volume":   "volume",
    })

    # Ensure UTC timezone
    if df["datetime"].dt.tz is None:
        df["datetime"] = df["datetime"].dt.tz_localize("UTC")
    else:
        df["datetime"] = df["datetime"].dt.tz_convert("UTC")

    df = df[["datetime", "open", "high", "low", "close", "volume"]]
    df = df.drop_duplicates(subset="datetime").sort_values("datetime").reset_index(drop=True)

    logger.info("Fetched %d candles from Yahoo Finance.", len(df))
    return df


# ------------------------------------------------------------------
# Gap detection and filling
# ------------------------------------------------------------------

def _find_gaps(df: pd.DataFrame, interval_minutes: int = 15) -> pd.DataFrame:
    """
    Identify gaps in a time series larger than `interval_minutes`.
    Returns a DataFrame listing each gap's start and end time.
    """
    expected = timedelta(minutes=interval_minutes)
    diffs = df["datetime"].diff()
    gaps = diffs[diffs > expected * 1.5]  # allow a small tolerance

    gap_info = []
    for idx in gaps.index:
        gap_info.append({
            "gap_start": df.loc[idx - 1, "datetime"],
            "gap_end":   df.loc[idx, "datetime"],
            "bars_missing": int(diffs[idx] / expected) - 1,
        })

    return pd.DataFrame(gap_info)


def fill_gaps_with_yfinance(ig_df: pd.DataFrame) -> pd.DataFrame:
    """
    Find gaps in the IG data and fill them using Yahoo Finance data.
    """
    if ig_df.empty:
        return ig_df

    gaps = _find_gaps(ig_df)

    if gaps.empty:
        logger.info("No gaps detected in the data.")
        return ig_df

    total_missing = gaps["bars_missing"].sum()
    logger.info("Found %d gap(s) totalling ~%d missing candles. Fetching yfinance fallback...",
                len(gaps), total_missing)

    yf_df = fetch_from_yfinance()
    if yf_df.empty:
        logger.warning("Could not fetch yfinance data for gap filling.")
        return ig_df

    # Keep only yfinance rows that fall inside a known gap
    fill_rows = []
    for _, gap in gaps.iterrows():
        mask = (yf_df["datetime"] > gap["gap_start"]) & (yf_df["datetime"] < gap["gap_end"])
        fill_rows.append(yf_df[mask])

    if not fill_rows:
        return ig_df

    filler = pd.concat(fill_rows, ignore_index=True)
    combined = pd.concat([ig_df, filler], ignore_index=True)
    combined = combined.drop_duplicates(subset="datetime").sort_values("datetime").reset_index(drop=True)

    logger.info("After gap filling: %d candles total.", len(combined))
    return combined


# ------------------------------------------------------------------
# Save / load
# ------------------------------------------------------------------

def save_data(df: pd.DataFrame, path: str = CSV_PATH):
    """Save the DataFrame to CSV."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)
    logger.info("Saved %d rows to %s", len(df), path)


def load_data(path: str = CSV_PATH) -> pd.DataFrame:
    """
    Load the saved CSV and return a DataFrame with a proper datetime index.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"Data file not found: {path}\nRun data_pipeline.py first.")

    df = pd.read_csv(path, parse_dates=["datetime"])

    # Make sure datetime is UTC-aware
    if df["datetime"].dt.tz is None:
        df["datetime"] = df["datetime"].dt.tz_localize("UTC")

    df = df.sort_values("datetime").reset_index(drop=True)
    logger.info("Loaded %d candles from %s", len(df), path)
    return df


# ------------------------------------------------------------------
# Main entry point
# ------------------------------------------------------------------

def _fetch_ig_since(client: IGClient, epic: str, since: datetime) -> pd.DataFrame:
    """
    Fetch IG candles from `since` until now — used to top up Yahoo data
    with the most recent bars that Yahoo hasn't published yet.
    Conserves IG weekly quota by only fetching the small recent window.
    """
    end = datetime.now(tz=timezone.utc)
    if since >= end:
        return pd.DataFrame()

    chunks = list(_split_date_range(since, end, MAX_CANDLES_PER_REQUEST))
    all_frames = []
    for chunk_start, chunk_end in chunks:
        df = _fetch_chunk(client, epic, chunk_start, chunk_end)
        if not df.empty:
            all_frames.append(df)
        time.sleep(REQUEST_DELAY_SECONDS)

    if not all_frames:
        return pd.DataFrame()

    combined = pd.concat(all_frames, ignore_index=True)
    combined = combined.drop_duplicates(subset="datetime").sort_values("datetime").reset_index(drop=True)
    return combined


def fetch_rolling_15min_bar(client: "IGClient" = None,
                            epic: str = DEFAULT_EPIC) -> pd.DataFrame:
    """
    Fetch the latest completed 15-min bar with zero delay.

    Strategy (in order):
      1. IG /prices endpoint — real-time, no delay. Requests only the last
         3 bars (45 min) so quota usage is negligible and no 403 risk.
      2. Yahoo Finance fallback — builds a synthetic 15-min bar from the
         last three 5-min candles (~15 min delayed). Used only if IG fails.

    Returns a one-row DataFrame: datetime, open, high, low, close, volume.
    """
    # ── 1. Try IG directly (real-time) ───────────────────────────────
    if client is not None:
        try:
            end   = datetime.now(tz=timezone.utc)
            start = end - timedelta(minutes=60)   # last 60 min → max 4 bars, tiny request
            df_ig = _fetch_chunk(client, epic, start, end)
            if not df_ig.empty:
                df_ig = df_ig.dropna().sort_values("datetime").reset_index(drop=True)
                latest = df_ig.tail(1)
                logger.info("Live bar from IG: close=%.5f  @%s",
                            float(latest["close"].iloc[0]),
                            latest["datetime"].iloc[0].strftime("%H:%M UTC"))
                return latest
        except Exception as exc:
            logger.warning("IG real-time bar failed (%s) — falling back to Yahoo", exc)

    # ── 2. Yahoo fallback (synthetic from 3 × 5-min bars) ────────────
    logger.info("fetch_rolling_15min_bar: using Yahoo Finance fallback (~15 min delay)")
    import yfinance as yf

    ticker  = yf.Ticker("EURUSD=X")
    df_5min = ticker.history(period="1d", interval="5m")

    if df_5min.empty or len(df_5min) < 3:
        logger.warning("fetch_rolling_15min_bar: Yahoo returned %d bars — skipping", len(df_5min))
        return pd.DataFrame()

    last3 = df_5min.tail(3).reset_index()
    col_map = {"Datetime": "datetime", "Date": "datetime",
               "Open": "open", "High": "high", "Low": "low",
               "Close": "close", "Volume": "volume"}
    last3 = last3.rename(columns={k: v for k, v in col_map.items() if k in last3.columns})

    if "datetime" in last3.columns:
        if last3["datetime"].dt.tz is None:
            last3["datetime"] = last3["datetime"].dt.tz_localize("UTC")
        else:
            last3["datetime"] = last3["datetime"].dt.tz_convert("UTC")

    return pd.DataFrame([{
        "datetime": last3["datetime"].iloc[-1],
        "open":     float(last3["open"].iloc[0]),
        "high":     float(last3["high"].max()),
        "low":      float(last3["low"].min()),
        "close":    float(last3["close"].iloc[-1]),
        "volume":   float(last3["volume"].sum()),
    }])


def fetch_and_save(months: int = DEFAULT_MONTHS, epic: str = DEFAULT_EPIC,
                   client: "IGClient" = None) -> pd.DataFrame:
    """
    Full pipeline — Yahoo-first strategy:
      1. Yahoo Finance provides the bulk history (~60 days of 15-min data, free).
      2. IG API tops up the most recent gap (bars Yahoo hasn't published yet).
         This preserves the weekly IG quota for recent data only.

    Parameters
    ----------
    client : IGClient, optional
        An already-authenticated IGClient instance.  When called from the
        live loop in main.py, always pass the existing client so we never
        create a second concurrent session (which causes IG to suspend the
        API key).  If None, a new client is created and logged in — only
        acceptable when running this file standalone.

    Returns the final DataFrame.
    """
    # --- Step 1: Yahoo as the historical base ---
    df = fetch_from_yfinance(months=months)

    # --- Step 2: Try IG only for the recent gap ---
    try:
        if client is None:
            # Standalone usage only — create a fresh session
            client = IGClient.from_credentials_file(
                os.path.join(os.path.dirname(__file__), "credentials.json")
            )
            client.login()

        if not df.empty:
            # Ask IG only from Yahoo's last timestamp onwards
            ig_since = df["datetime"].max()
            logger.info("Topping up with IG data since %s ...", ig_since.strftime("%Y-%m-%d %H:%M"))
            ig_recent = _fetch_ig_since(client, epic, ig_since)
            if not ig_recent.empty:
                df = pd.concat([df, ig_recent], ignore_index=True)
                df = df.drop_duplicates(subset="datetime").sort_values("datetime").reset_index(drop=True)
                logger.info("IG top-up added %d recent candles.", len(ig_recent))
            else:
                logger.info("IG returned no new candles (quota may be exhausted — Yahoo data is sufficient).")
        else:
            # Yahoo failed entirely — fall back to full IG fetch
            logger.warning("Yahoo returned no data. Falling back to full IG fetch.")
            df = fetch_from_ig(client, epic, months=months)

    except Exception as e:
        logger.warning("IG top-up skipped (%s). Proceeding with Yahoo data only.", e)

    if df.empty:
        logger.error("Could not retrieve any data. Check credentials and epic.")
        return df

    save_data(df)
    return df


if __name__ == "__main__":
    import sys
    months = int(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_MONTHS
    df = fetch_and_save(months=months)  # standalone: creates its own session

    if not df.empty:
        print(f"\nData summary:")
        print(f"  Rows:       {len(df)}")
        print(f"  From:       {df['datetime'].min()}")
        print(f"  To:         {df['datetime'].max()}")
        print(f"  Columns:    {list(df.columns)}")
        print(f"\nFirst few rows:")
        print(df.head())
