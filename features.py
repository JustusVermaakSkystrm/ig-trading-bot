"""
features.py
-----------
Computes all technical features from raw OHLCV price data.

Features generated:
  1. Savitzky-Golay (SG) smoothed price at 3 window sizes
     - First derivative  (momentum / velocity)
     - Second derivative (acceleration)
     - Crossover signals between fast and slow SG lines
  2. Piecewise linear regression
     - Trend slope at current segment
     - Detrended residuals (price minus trend)
  3. Hilbert Transform on detrended residuals
     - Instantaneous phase  (cycle position 0-360°)
     - Instantaneous amplitude (cycle strength)
     - Cycle buy/sell zone flags
  4. Classic indicators
     - RSI (14)
     - ATR (14) — volatility measure
     - Hour of day, day of week (market session context)
     - London / New York session flags

Usage:
    from features import compute_features
    df_features = compute_features(df_price)
"""

import logging

import numpy as np
import pandas as pd
from scipy.signal import savgol_filter, savgol_coeffs, hilbert
from scipy.stats import linregress

logger = logging.getLogger(__name__)


# ------------------------------------------------------------------
# Savitzky-Golay features
# ------------------------------------------------------------------

# Window sizes in bars (15-min bars):
#   SHORT  = 10 bars =  2.5 hours
#   MEDIUM = 30 bars =  7.5 hours
#   LONG   = 60 bars = 15.0 hours
SG_WINDOWS = {
    "short":  11,   # must be odd
    "medium": 31,   # must be odd
    "long":   61,   # must be odd
}
SG_POLY_ORDER = 3  # polynomial degree for SG filter


def _causal_savgol(close: np.ndarray, window: int, polyorder: int, deriv: int) -> np.ndarray:
    """
    Apply Savitzky-Golay filter in a truly causal (look-back only) fashion.

    The standard savgol_filter is a CENTRED filter — for bar i it uses bars
    [i - window//2, ..., i, ..., i + window//2], meaning it always peeks at
    future prices.  Left-padding the array doesn't fix this for interior bars.

    The correct approach:
      1. Use savgol_coeffs(pos=window-1) to get RIGHT-ALIGNED coefficients.
         These describe the polynomial evaluated at the LAST point of the
         window, so result[i] = dot(coeffs, close[i-window+1 : i+1]).
         No future data is used at any position.
      2. Apply via np.convolve, which is O(N log N) — fast for 4000+ bars.

    Derivation of the convolution:
        result[i] = sum_{j=0}^{W-1} coeffs[j] * close[i-W+1+j]
                  = (close  ★  coeffs_reversed)[i]      (★ = convolve)
    The full convolution has length N+W-1; we take the first N values and
    mark the first W-1 as NaN (not enough look-back history yet).
    """
    coeffs    = savgol_coeffs(window, polyorder, deriv=deriv, pos=window - 1)
    conv_full = np.convolve(close, coeffs[::-1], mode="full")
    result    = np.full(len(close), np.nan)
    result[window - 1:] = conv_full[window - 1: len(close)]
    return result


def _savgol_features(close: np.ndarray) -> dict:
    """
    Compute SG-smoothed values and their first + second derivatives
    for each window size.

    Uses _causal_savgol so features at bar t only depend on bars <= t
    (no look-ahead / data leakage).
    """
    feats = {}
    for name, window in SG_WINDOWS.items():
        if len(close) < window:
            # Not enough data for this window — fill with NaN
            feats[f"sg_{name}"]       = np.full(len(close), np.nan)
            feats[f"sg_{name}_d1"]    = np.full(len(close), np.nan)
            feats[f"sg_{name}_d2"]    = np.full(len(close), np.nan)
            continue

        feats[f"sg_{name}"]    = _causal_savgol(close, window, SG_POLY_ORDER, deriv=0)
        feats[f"sg_{name}_d1"] = _causal_savgol(close, window, SG_POLY_ORDER, deriv=1)
        feats[f"sg_{name}_d2"] = _causal_savgol(close, window, SG_POLY_ORDER, deriv=2)

    # Crossover: short SG minus long SG (positive = uptrend)
    if "sg_short" in feats and "sg_long" in feats:
        feats["sg_cross"] = feats["sg_short"] - feats["sg_long"]

    return feats


# ------------------------------------------------------------------
# Piecewise regression (trend extraction)
# ------------------------------------------------------------------

TREND_WINDOW = 60   # bars to use for rolling linear regression (= 15 hours of 15-min bars)


def _piecewise_trend(close: np.ndarray, n_breakpoints: int = 5,
                     causal_window: int = TREND_WINDOW) -> tuple:
    """
    Estimate the local trend using a rolling linear regression over a
    look-back window of `causal_window` bars.

    Replaces the original full-series piecewise regression (ruptures/PELT),
    which was non-causal — it detected breakpoints using all future data,
    introducing severe look-ahead bias during training.

    A rolling linear regression is inherently causal: the slope and trend
    value at bar t are computed using only bars [t-window+1 … t].

    Returns:
        trend     : np.ndarray — fitted trend values at each bar
        residuals : np.ndarray — price minus trend (the detrended data)
        slope     : np.ndarray — slope (price units per bar) at each bar
    """
    n         = len(close)
    trend     = np.empty(n)
    slope_arr = np.empty(n)
    trend[:]     = np.nan
    slope_arr[:] = np.nan

    x_cache = {}   # reuse the x-vectors to avoid rebuilding them each loop

    for i in range(n):
        start   = max(0, i - causal_window + 1)
        seg     = close[start: i + 1]
        seg_len = len(seg)

        if seg_len < 2:
            trend[i]     = close[i]
            slope_arr[i] = 0.0
            continue

        if seg_len not in x_cache:
            x_cache[seg_len] = np.arange(seg_len, dtype=float)
        x = x_cache[seg_len]

        sl, intercept, *_ = linregress(x, seg)
        # Trend value at the last (current) bar
        trend[i]     = sl * (seg_len - 1) + intercept
        slope_arr[i] = sl

    residuals = close - trend
    return trend, residuals, slope_arr


# ------------------------------------------------------------------
# Hilbert Transform cycle analysis
# ------------------------------------------------------------------

HILBERT_WINDOW = 64   # must be a power of 2 for best FFT performance


def _hilbert_features(residuals: np.ndarray) -> dict:
    """
    Estimate instantaneous phase and amplitude using a rolling Hilbert Transform.

    The original code called scipy.signal.hilbert() on the entire residuals
    array at once.  That function is non-causal — the result at bar t depends
    on residuals after t — which causes look-ahead bias in training.

    Fix: apply hilbert() to a rolling window of `HILBERT_WINDOW` bars and
    take only the LAST value from each window.  Everything the model sees at
    bar t is derived purely from bars <= t.

    Phase interpretation:
        0°   = cycle starting to rise
        90°  = cycle peak  → potential sell zone
        180° = cycle starting to fall
        270° = cycle trough → potential buy zone
    """
    n             = len(residuals)
    phase_deg     = np.full(n, np.nan)
    amplitude     = np.full(n, np.nan)
    freq          = np.full(n, np.nan)

    for i in range(HILBERT_WINDOW - 1, n):
        window = residuals[i - HILBERT_WINDOW + 1: i + 1]

        analytic   = hilbert(window)
        amp_window = np.abs(analytic)
        ph_rad     = np.unwrap(np.angle(analytic))

        # Only keep the value for the CURRENT (last) bar in the window
        amplitude[i] = amp_window[-1]
        phase_deg[i] = np.degrees(ph_rad[-1]) % 360

        # Instantaneous frequency: rate of phase change at the last bar
        if len(ph_rad) >= 2:
            freq[i] = (ph_rad[-1] - ph_rad[-2]) / (2 * np.pi)

    feats = {
        "hilbert_phase":     phase_deg,
        "hilbert_amplitude": amplitude,
        "hilbert_buy_zone":  (phase_deg >= 225) & (phase_deg <= 315),   # near trough
        "hilbert_sell_zone": (phase_deg >= 45)  & (phase_deg <= 135),   # near peak
        "hilbert_freq":      freq,
    }
    return feats


# ------------------------------------------------------------------
# Classic indicators
# ------------------------------------------------------------------

def _rsi(close: pd.Series, period: int = 14) -> pd.Series:
    delta = close.diff()
    gain  = delta.clip(lower=0)
    loss  = -delta.clip(upper=0)
    avg_gain = gain.ewm(com=period - 1, min_periods=period).mean()
    avg_loss = loss.ewm(com=period - 1, min_periods=period).mean()
    rs  = avg_gain / avg_loss.replace(0, np.nan)
    rsi = 100 - (100 / (1 + rs))
    return rsi


def _atr(df: pd.DataFrame, period: int = 14) -> pd.Series:
    """Average True Range — measures market volatility."""
    high_low   = df["high"] - df["low"]
    high_close = (df["high"] - df["close"].shift()).abs()
    low_close  = (df["low"]  - df["close"].shift()).abs()
    true_range = pd.concat([high_low, high_close, low_close], axis=1).max(axis=1)
    return true_range.ewm(com=period - 1, min_periods=period).mean()


# ------------------------------------------------------------------
# Session helpers
# ------------------------------------------------------------------

def _session_flags(dt_series: pd.Series) -> pd.DataFrame:
    """
    Return boolean columns for London and New York trading sessions (UTC).
    London: 08:00 – 17:00 UTC
    New York: 13:00 – 22:00 UTC
    """
    hour = dt_series.dt.hour
    return pd.DataFrame({
        "session_london":   ((hour >= 8)  & (hour < 17)).astype(int),
        "session_newyork":  ((hour >= 13) & (hour < 22)).astype(int),
        "session_overlap":  ((hour >= 13) & (hour < 17)).astype(int),
    })


# ------------------------------------------------------------------
# Master feature builder
# ------------------------------------------------------------------

def compute_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Take a raw OHLCV DataFrame (from data_pipeline.load_data)
    and return a new DataFrame with all computed features appended.

    Parameters
    ----------
    df : DataFrame with columns [datetime, open, high, low, close, volume]

    Returns
    -------
    DataFrame with all original columns plus feature columns.
    Rows with NaN features (due to warm-up periods) are dropped.
    """
    df = df.copy()

    # Ensure the datetime column is usable
    if not pd.api.types.is_datetime64_any_dtype(df["datetime"]):
        df["datetime"] = pd.to_datetime(df["datetime"])

    # Drop any rows with NaN in core price columns before computing features
    df = df.dropna(subset=["open", "high", "low", "close"]).reset_index(drop=True)

    # Interpolate any remaining gaps in close (shouldn't be needed after above,
    # but guards against edge cases)
    df["close"] = df["close"].interpolate(method="linear").ffill().bfill()
    df["high"]  = df["high"].interpolate(method="linear").ffill().bfill()
    df["low"]   = df["low"].interpolate(method="linear").ffill().bfill()

    close = df["close"].values

    # ---- 1. Savitzky-Golay features ------------------------------------
    logger.info("Computing Savitzky-Golay features...")
    sg_feats = _savgol_features(close)
    for col, values in sg_feats.items():
        df[col] = values

    # ---- 2. Piecewise regression + detrend ----------------------------
    logger.info("Computing piecewise regression trend...")
    trend, residuals, slope = _piecewise_trend(close)
    df["trend"]          = trend
    df["residuals"]      = residuals
    df["trend_slope"]    = slope                      # positive = uptrend segment

    # ---- 3. Hilbert on detrended residuals ----------------------------
    logger.info("Computing Hilbert Transform on residuals...")
    h_feats = _hilbert_features(residuals)
    for col, values in h_feats.items():
        df[col] = values.astype(float)

    # ---- 4. Classic indicators ----------------------------------------
    logger.info("Computing RSI and ATR...")
    df["rsi"]  = _rsi(df["close"])
    df["atr"]  = _atr(df)

    # ---- 5. Time / session features -----------------------------------
    sessions = _session_flags(df["datetime"])
    df = pd.concat([df, sessions], axis=1)
    df["hour_of_day"]  = df["datetime"].dt.hour
    df["day_of_week"]  = df["datetime"].dt.dayofweek   # 0=Monday … 4=Friday

    # ---- 6. Price normalisation helpers -------------------------------
    # Express features relative to recent ATR so they're scale-invariant
    # (makes XGBoost slightly more robust across different volatility regimes)
    df["residuals_norm"] = df["residuals"] / df["atr"].replace(0, np.nan)
    df["sg_cross_norm"]  = df["sg_cross"]  / df["atr"].replace(0, np.nan)

    # ---- 7. Drop warm-up rows -----------------------------------------
    warmup = max(SG_WINDOWS.values()) + 14  # SG window + ATR/RSI period
    df = df.iloc[warmup:].reset_index(drop=True)

    logger.info("Feature matrix shape: %s", df.shape)
    return df


# ------------------------------------------------------------------
# Feature column list (used by model.py)
# ------------------------------------------------------------------

FEATURE_COLUMNS = [
    # Savitzky-Golay
    "sg_short",    "sg_medium",    "sg_long",
    "sg_short_d1", "sg_medium_d1", "sg_long_d1",
    "sg_short_d2", "sg_medium_d2", "sg_long_d2",
    "sg_cross",    "sg_cross_norm",
    # Trend
    "trend_slope",
    "residuals",   "residuals_norm",
    # Hilbert
    "hilbert_phase", "hilbert_amplitude", "hilbert_freq",
    "hilbert_buy_zone", "hilbert_sell_zone",
    # Classic
    "rsi", "atr",
    # Time
    "hour_of_day", "day_of_week",
    "session_london", "session_newyork", "session_overlap",
]
