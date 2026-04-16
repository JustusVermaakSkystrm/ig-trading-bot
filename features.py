"""
features.py
-----------
Computes all technical features from raw OHLCV price data.

Features generated:
  1.  Savitzky-Golay (SG) smoothed price at 3 window sizes
      - First & second derivatives (momentum / acceleration)
      - Crossover signals between fast and slow SG lines
  2.  Piecewise linear regression
      - Trend slope and detrended residuals
  3.  Hilbert Transform on detrended residuals
      - Instantaneous phase, amplitude, cycle buy/sell zone flags
  4.  Classic indicators
      - RSI (14), ATR (14)
  5.  Session context
      - Hour, day-of-week, London/NY session flags
  6.  20 popular technical indicators (all causal, normalised by ATR):
      - MACD, Bollinger Bands, EMA (12/26/50/200), SMA (20/50/200)
      - Stochastic (%K/%D), ADX (+DI/-DI), Williams %R, CCI
      - OBV, VWAP, Parabolic SAR, Rate-of-Change
      - MFI, Donchian Channels, Keltner Channels, CMF
      - TRIX, Ultimate Oscillator, Ichimoku Cloud

Usage:
    from features import compute_features
    df_features = compute_features(df_price)
"""

import logging

import numpy as np
import pandas as pd
from scipy.signal import savgol_filter, savgol_coeffs, hilbert  # noqa: F401
from scipy.stats import linregress

logger = logging.getLogger(__name__)


# ------------------------------------------------------------------
# Savitzky-Golay features
# ------------------------------------------------------------------

SG_WINDOWS = {
    "short":  11,
    "medium": 31,
    "long":   61,
}
SG_POLY_ORDER = 3


def _causal_savgol(close: np.ndarray, window: int, polyorder: int, deriv: int) -> np.ndarray:
    """Right-aligned (causal) Savitzky-Golay filter."""
    coeffs    = savgol_coeffs(window, polyorder, deriv=deriv, pos=window - 1)
    conv_full = np.convolve(close, coeffs[::-1], mode="full")
    result    = np.full(len(close), np.nan)
    result[window - 1:] = conv_full[window - 1: len(close)]
    return result


def _savgol_features(close: np.ndarray) -> dict:
    feats = {}
    for name, window in SG_WINDOWS.items():
        if len(close) < window:
            feats[f"sg_{name}"]       = np.full(len(close), np.nan)
            feats[f"sg_{name}_d1"]    = np.full(len(close), np.nan)
            feats[f"sg_{name}_d2"]    = np.full(len(close), np.nan)
            continue
        feats[f"sg_{name}"]    = _causal_savgol(close, window, SG_POLY_ORDER, deriv=0)
        feats[f"sg_{name}_d1"] = _causal_savgol(close, window, SG_POLY_ORDER, deriv=1)
        feats[f"sg_{name}_d2"] = _causal_savgol(close, window, SG_POLY_ORDER, deriv=2)
    if "sg_short" in feats and "sg_long" in feats:
        feats["sg_cross"] = feats["sg_short"] - feats["sg_long"]
    return feats


# ------------------------------------------------------------------
# Piecewise regression (trend extraction)
# ------------------------------------------------------------------

TREND_WINDOW = 60


def _piecewise_trend(close: np.ndarray, causal_window: int = TREND_WINDOW) -> tuple:
    n         = len(close)
    trend     = np.empty(n)
    slope_arr = np.empty(n)
    trend[:]     = np.nan
    slope_arr[:] = np.nan
    x_cache = {}
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
        trend[i]     = sl * (seg_len - 1) + intercept
        slope_arr[i] = sl
    residuals = close - trend
    return trend, residuals, slope_arr


# ------------------------------------------------------------------
# Hilbert Transform cycle analysis
# ------------------------------------------------------------------

HILBERT_WINDOW = 64


def _hilbert_features(residuals: np.ndarray) -> dict:
    n             = len(residuals)
    phase_deg     = np.full(n, np.nan)
    amplitude     = np.full(n, np.nan)
    freq          = np.full(n, np.nan)
    for i in range(HILBERT_WINDOW - 1, n):
        window     = residuals[i - HILBERT_WINDOW + 1: i + 1]
        analytic   = hilbert(window)
        amp_window = np.abs(analytic)
        ph_rad     = np.unwrap(np.angle(analytic))
        amplitude[i] = amp_window[-1]
        phase_deg[i] = np.degrees(ph_rad[-1]) % 360
        if len(ph_rad) >= 2:
            freq[i] = (ph_rad[-1] - ph_rad[-2]) / (2 * np.pi)
    feats = {
        "hilbert_phase":     phase_deg,
        "hilbert_amplitude": amplitude,
        "hilbert_buy_zone":  (phase_deg >= 225) & (phase_deg <= 315),
        "hilbert_sell_zone": (phase_deg >= 45)  & (phase_deg <= 135),
        "hilbert_freq":      freq,
    }
    return feats


# ------------------------------------------------------------------
# Classic indicators
# ------------------------------------------------------------------

def _rsi(close: pd.Series, period: int = 14) -> pd.Series:
    delta    = close.diff()
    gain     = delta.clip(lower=0)
    loss     = -delta.clip(upper=0)
    avg_gain = gain.ewm(com=period - 1, min_periods=period).mean()
    avg_loss = loss.ewm(com=period - 1, min_periods=period).mean()
    rs       = avg_gain / avg_loss.replace(0, np.nan)
    return 100 - (100 / (1 + rs))


def _atr(df: pd.DataFrame, period: int = 14) -> pd.Series:
    high_low   = df["high"] - df["low"]
    high_close = (df["high"] - df["close"].shift()).abs()
    low_close  = (df["low"]  - df["close"].shift()).abs()
    true_range = pd.concat([high_low, high_close, low_close], axis=1).max(axis=1)
    return true_range.ewm(com=period - 1, min_periods=period).mean()


# ------------------------------------------------------------------
# Session helpers
# ------------------------------------------------------------------

def _session_flags(dt_series: pd.Series) -> pd.DataFrame:
    hour = dt_series.dt.hour
    return pd.DataFrame({
        "session_london":  ((hour >= 8)  & (hour < 17)).astype(int),
        "session_newyork": ((hour >= 13) & (hour < 22)).astype(int),
        "session_overlap": ((hour >= 13) & (hour < 17)).astype(int),
    })


# ------------------------------------------------------------------
# Parabolic SAR (causal, iterative)
# ------------------------------------------------------------------

def _parabolic_sar(df: pd.DataFrame, af_step: float = 0.02, af_max: float = 0.2) -> pd.Series:
    """
    Standard Wilder Parabolic SAR, computed bar-by-bar (fully causal).
    Returns the SAR value at each bar.
    """
    high = df["high"].values
    low  = df["low"].values
    n    = len(high)
    sar  = np.full(n, np.nan)

    if n < 2:
        return pd.Series(sar, index=df.index)

    # Initialise: detect trend from first two bars
    is_long = high[1] >= high[0]
    ep      = high[0] if is_long else low[0]
    af      = af_step
    sar[0]  = low[0] if is_long else high[0]

    for i in range(1, n):
        prev_sar = sar[i - 1]

        if is_long:
            new_sar = prev_sar + af * (ep - prev_sar)
            # SAR must be at or below the two prior lows
            new_sar = min(new_sar, low[i - 1])
            if i >= 2:
                new_sar = min(new_sar, low[i - 2])

            if low[i] < new_sar:
                # Reversal to short
                is_long = False
                new_sar = ep
                ep      = low[i]
                af      = af_step
            else:
                if high[i] > ep:
                    ep = high[i]
                    af = min(af + af_step, af_max)
        else:
            new_sar = prev_sar + af * (ep - prev_sar)
            # SAR must be at or above the two prior highs
            new_sar = max(new_sar, high[i - 1])
            if i >= 2:
                new_sar = max(new_sar, high[i - 2])

            if high[i] > new_sar:
                # Reversal to long
                is_long = True
                new_sar = ep
                ep      = high[i]
                af      = af_step
            else:
                if low[i] < ep:
                    ep = low[i]
                    af = min(af + af_step, af_max)

        sar[i] = new_sar

    return pd.Series(sar, index=df.index)


# ------------------------------------------------------------------
# 20 popular technical indicators (all causal)
# ------------------------------------------------------------------

def _technical_indicators(df: pd.DataFrame) -> dict:
    """
    Compute 20 widely-used technical indicators.

    All price-based indicators are normalised by ATR so features remain
    scale-invariant across different volatility regimes.  Bounded oscillators
    (RSI, Stochastic, etc.) are returned as-is.

    Requires df to already contain 'atr' (from _atr) and 'rsi' (from _rsi)
    columns so we can normalise and compute divergence features.
    """
    close  = df["close"]
    high   = df["high"]
    low    = df["low"]
    volume = df["volume"]
    atr    = df["atr"].replace(0, np.nan)

    feats: dict = {}

    # ---- 1. MACD (12, 26, 9) ------------------------------------------
    ema12       = close.ewm(span=12, adjust=False).mean()
    ema26       = close.ewm(span=26, adjust=False).mean()
    macd_line   = ema12 - ema26
    macd_signal = macd_line.ewm(span=9, adjust=False).mean()
    macd_hist   = macd_line - macd_signal
    feats["macd_norm"]        = macd_line   / atr
    feats["macd_signal_norm"] = macd_signal / atr
    feats["macd_hist_norm"]   = macd_hist   / atr

    # ---- 2. Bollinger Bands (20, 2σ) -----------------------------------
    sma20    = close.rolling(20).mean()
    std20    = close.rolling(20).std()
    bb_upper = sma20 + 2 * std20
    bb_lower = sma20 - 2 * std20
    bb_range = (bb_upper - bb_lower).replace(0, np.nan)
    feats["bb_pct"]        = (close - bb_lower) / bb_range         # 0=lower, 1=upper
    feats["bb_width"]      = bb_range / sma20.replace(0, np.nan)   # relative bandwidth
    feats["bb_upper_dist"] = (bb_upper - close) / atr
    feats["bb_lower_dist"] = (close - bb_lower) / atr

    # ---- 3. EMA crossovers (12 / 26 / 50 / 200) ------------------------
    for span in (12, 26, 50, 200):
        ema = close.ewm(span=span, adjust=False).mean()
        feats[f"ema_{span}_dist"] = (close - ema) / atr
    feats["ema_12_26_cross"] = (ema12 - ema26) / atr  # positive = fast above slow

    # ---- 4. SMA distance (20 / 50 / 200) --------------------------------
    for period in (20, 50, 200):
        sma = close.rolling(period).mean()
        feats[f"sma_{period}_dist"] = (close - sma) / atr

    # ---- 5. Stochastic Oscillator (14, 3) --------------------------------
    low14    = low.rolling(14).min()
    high14   = high.rolling(14).max()
    stoch_k  = 100 * (close - low14) / (high14 - low14).replace(0, np.nan)
    stoch_d  = stoch_k.rolling(3).mean()
    feats["stoch_k"]      = stoch_k
    feats["stoch_d"]      = stoch_d
    feats["stoch_kd_diff"] = stoch_k - stoch_d  # positive = K above D = momentum

    # ---- 6. ADX (14) + Directional Indicators --------------------------
    tr1 = high - low
    tr2 = (high - close.shift()).abs()
    tr3 = (low  - close.shift()).abs()
    true_range = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)

    up_move  = high.diff()
    dn_move  = -low.diff()
    plus_dm  = np.where((up_move > dn_move) & (up_move > 0), up_move, 0.0)
    minus_dm = np.where((dn_move > up_move) & (dn_move > 0), dn_move, 0.0)

    plus_dm_s  = pd.Series(plus_dm,  index=df.index).ewm(com=13, min_periods=14).mean()
    minus_dm_s = pd.Series(minus_dm, index=df.index).ewm(com=13, min_periods=14).mean()
    tr_s       = true_range.ewm(com=13, min_periods=14).mean()

    plus_di  = 100 * plus_dm_s  / tr_s.replace(0, np.nan)
    minus_di = 100 * minus_dm_s / tr_s.replace(0, np.nan)
    dx       = 100 * (plus_di - minus_di).abs() / (plus_di + minus_di).replace(0, np.nan)
    adx      = dx.ewm(com=13, min_periods=14).mean()

    feats["adx"]          = adx
    feats["di_diff"]      = plus_di - minus_di          # positive = bullish trend
    feats["adx_di_bull"]  = adx * (plus_di - minus_di)  # strength × direction

    # ---- 7. Williams %R (14) -------------------------------------------
    feats["williams_r"] = -100 * (high14 - close) / (high14 - low14).replace(0, np.nan)

    # ---- 8. CCI (20) ---------------------------------------------------
    tp      = (high + low + close) / 3
    sma_tp  = tp.rolling(20).mean()
    mad     = tp.rolling(20).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)
    feats["cci"] = (tp - sma_tp) / (0.015 * mad.replace(0, np.nan))

    # ---- 9. OBV (z-scored over rolling 50 bars) ------------------------
    direction = np.sign(close.diff())
    direction.iloc[0] = 0.0
    obv       = (direction * volume).cumsum()
    obv_mean  = obv.rolling(50).mean()
    obv_std   = obv.rolling(50).std().replace(0, np.nan)
    feats["obv_zscore"] = (obv - obv_mean) / obv_std

    # ---- 10. VWAP (daily reset) ----------------------------------------
    tp_vwap  = (high + low + close) / 3
    tpv      = tp_vwap * volume
    dates    = df["datetime"].dt.normalize()   # group key = midnight timestamp
    cum_tpv  = tpv.groupby(dates).transform("cumsum")
    cum_vol  = volume.groupby(dates).transform("cumsum")
    vwap     = cum_tpv / cum_vol.replace(0, np.nan)
    feats["vwap_dist"] = (close - vwap) / atr

    # ---- 11. Parabolic SAR ---------------------------------------------
    psar = _parabolic_sar(df)
    feats["psar_dist"] = (close - psar) / atr   # positive = price above SAR (bullish)

    # ---- 12. Rate of Change (10 bars) ----------------------------------
    feats["roc_10"] = 100 * (close - close.shift(10)) / close.shift(10).replace(0, np.nan)

    # ---- 13. Money Flow Index (14) -------------------------------------
    tp_mfi  = (high + low + close) / 3
    mf      = tp_mfi * volume
    pos_mf  = mf.where(tp_mfi > tp_mfi.shift(), 0.0)
    neg_mf  = mf.where(tp_mfi < tp_mfi.shift(), 0.0)
    pos_sum = pos_mf.rolling(14).sum()
    neg_sum = neg_mf.rolling(14).sum()
    mfr     = pos_sum / neg_sum.replace(0, np.nan)
    feats["mfi"] = 100 - (100 / (1 + mfr))

    # ---- 14. Donchian Channels (20) ------------------------------------
    dc_upper = high.rolling(20).max()
    dc_lower = low.rolling(20).min()
    dc_range = (dc_upper - dc_lower).replace(0, np.nan)
    feats["dc_pct"]   = (close - dc_lower) / dc_range   # 0=at bottom, 1=at top
    feats["dc_width"] = dc_range / atr                  # channel width in ATR units

    # ---- 15. Keltner Channels (20, 2×ATR10) ----------------------------
    ema20       = close.ewm(span=20, adjust=False).mean()
    atr10       = true_range.ewm(com=9, min_periods=10).mean()
    kc_upper    = ema20 + 2 * atr10
    kc_lower    = ema20 - 2 * atr10
    kc_range    = (kc_upper - kc_lower).replace(0, np.nan)
    feats["kc_pct"]   = (close - kc_lower) / kc_range
    # Volatility squeeze: BB inside Keltner = low volatility / potential breakout
    feats["squeeze"] = ((bb_lower > kc_lower) & (bb_upper < kc_upper)).astype(float)

    # ---- 16. Chaikin Money Flow (20) -----------------------------------
    hl      = (high - low).replace(0, np.nan)
    mfm     = ((close - low) - (high - close)) / hl
    mfv     = mfm * volume
    feats["cmf"] = mfv.rolling(20).sum() / volume.rolling(20).sum().replace(0, np.nan)

    # ---- 17. TRIX (14) -------------------------------------------------
    ema1 = close.ewm(span=14, adjust=False).mean()
    ema2 = ema1.ewm(span=14, adjust=False).mean()
    ema3 = ema2.ewm(span=14, adjust=False).mean()
    feats["trix"] = 100 * ema3.pct_change()

    # ---- 18. Ultimate Oscillator (7, 14, 28) ---------------------------
    true_low  = pd.concat([low,  close.shift()], axis=1).min(axis=1)
    true_high = pd.concat([high, close.shift()], axis=1).max(axis=1)
    bp        = close - true_low
    tr_uo     = true_high - true_low
    avg7  = bp.rolling(7).sum()  / tr_uo.rolling(7).sum().replace(0, np.nan)
    avg14 = bp.rolling(14).sum() / tr_uo.rolling(14).sum().replace(0, np.nan)
    avg28 = bp.rolling(28).sum() / tr_uo.rolling(28).sum().replace(0, np.nan)
    feats["uo"] = 100 * (4 * avg7 + 2 * avg14 + avg28) / 7

    # ---- 19. Ichimoku Cloud (9 / 26 / 52) — causal version --------------
    # Tenkan-sen (Conversion Line): (9-period high + 9-period low) / 2
    tenkan = (high.rolling(9).max() + low.rolling(9).min()) / 2
    # Kijun-sen (Base Line): (26-period high + 26-period low) / 2
    kijun  = (high.rolling(26).max() + low.rolling(26).min()) / 2
    # Senkou Span A projected 26 bars forward — for ML we use the value
    # that was computed 26 bars ago and is "visible" on the chart NOW.
    # .shift(26) lags the series by 26 bars — fully causal.
    senkou_a = ((tenkan + kijun) / 2).shift(26)
    senkou_b = ((high.rolling(52).max() + low.rolling(52).min()) / 2).shift(26)
    cloud_top    = pd.concat([senkou_a, senkou_b], axis=1).max(axis=1)
    cloud_bottom = pd.concat([senkou_a, senkou_b], axis=1).min(axis=1)

    feats["ichi_tenkan_dist"]    = (close - tenkan) / atr
    feats["ichi_kijun_dist"]     = (close - kijun)  / atr
    # +1 = above cloud (bullish), -1 = below cloud (bearish), 0 = inside
    feats["ichi_cloud_pos"]      = (
        (close > cloud_top).astype(float) - (close < cloud_bottom).astype(float)
    )
    feats["ichi_cloud_thickness"] = (cloud_top - cloud_bottom) / atr
    feats["ichi_tk_cross"]       = (tenkan - kijun) / atr  # > 0 = bullish crossover

    # Chikou momentum proxy: current close vs close 26 bars ago
    feats["chikou_mom"] = (close - close.shift(26)) / atr

    # ---- 20. RSI divergence (price ROC vs RSI ROC over 5 bars) ---------
    rsi_series       = df["rsi"]
    feats["rsi_5roc"]       = rsi_series.diff(5)
    feats["price_rsi_div"]  = close.pct_change(5) * 100 - rsi_series.diff(5)

    return feats


# ------------------------------------------------------------------
# Master feature builder
# ------------------------------------------------------------------

def compute_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Take a raw OHLCV DataFrame and return a new DataFrame with all
    computed features appended.  Warm-up rows (where features are NaN
    due to insufficient look-back history) are dropped.

    Parameters
    ----------
    df : DataFrame with columns [datetime, open, high, low, close, volume]

    Returns
    -------
    DataFrame with all original columns plus feature columns.
    """
    df = df.copy()

    if not pd.api.types.is_datetime64_any_dtype(df["datetime"]):
        df["datetime"] = pd.to_datetime(df["datetime"])

    df = df.dropna(subset=["open", "high", "low", "close"]).reset_index(drop=True)
    df["close"] = df["close"].interpolate(method="linear").ffill().bfill()
    df["high"]  = df["high"].interpolate(method="linear").ffill().bfill()
    df["low"]   = df["low"].interpolate(method="linear").ffill().bfill()

    # Fill volume NaNs with 0 (forex data often has sparse volume)
    df["volume"] = df["volume"].fillna(0)

    close = df["close"].values

    # ---- 1. Savitzky-Golay features ------------------------------------
    logger.info("Computing Savitzky-Golay features...")
    sg_feats = _savgol_features(close)
    for col, values in sg_feats.items():
        df[col] = values

    # ---- 2. Piecewise regression + detrend ----------------------------
    logger.info("Computing piecewise regression trend...")
    trend, residuals, slope = _piecewise_trend(close)
    df["trend"]       = trend
    df["residuals"]   = residuals
    df["trend_slope"] = slope

    # ---- 3. Hilbert on detrended residuals ----------------------------
    logger.info("Computing Hilbert Transform on residuals...")
    h_feats = _hilbert_features(residuals)
    for col, values in h_feats.items():
        df[col] = values.astype(float)

    # ---- 4. Classic indicators (RSI + ATR needed for normalisation) ---
    logger.info("Computing RSI and ATR...")
    df["rsi"] = _rsi(df["close"])
    df["atr"] = _atr(df)

    # ---- 5. Session features ------------------------------------------
    sessions = _session_flags(df["datetime"])
    df = pd.concat([df, sessions], axis=1)
    df["hour_of_day"] = df["datetime"].dt.hour
    df["day_of_week"] = df["datetime"].dt.dayofweek

    # ---- 6. Normalised SG cross / residuals ---------------------------
    df["residuals_norm"] = df["residuals"] / df["atr"].replace(0, np.nan)
    df["sg_cross_norm"]  = df["sg_cross"]  / df["atr"].replace(0, np.nan)

    # ---- 7. 20 popular technical indicators ---------------------------
    logger.info("Computing 20 technical indicators...")
    ti_feats = _technical_indicators(df)
    for col, values in ti_feats.items():
        df[col] = values

    # ---- 8. Drop warm-up rows ----------------------------------------
    # SMA-200 needs 200 bars; Ichimoku Senkou-B + shift needs 52+26=78.
    # Use whichever is largest.
    warmup = max(max(SG_WINDOWS.values()), 200) + 14
    df = df.iloc[warmup:].reset_index(drop=True)

    logger.info("Feature matrix shape: %s", df.shape)
    return df


# ------------------------------------------------------------------
# Feature column list (used by model.py and signal_engine.py)
# ------------------------------------------------------------------

FEATURE_COLUMNS = [
    # ---- Savitzky-Golay -----------------------------------------------
    "sg_short",    "sg_medium",    "sg_long",
    "sg_short_d1", "sg_medium_d1", "sg_long_d1",
    "sg_short_d2", "sg_medium_d2", "sg_long_d2",
    "sg_cross",    "sg_cross_norm",
    # ---- Trend --------------------------------------------------------
    "trend_slope",
    "residuals",   "residuals_norm",
    # ---- Hilbert ------------------------------------------------------
    "hilbert_phase", "hilbert_amplitude", "hilbert_freq",
    "hilbert_buy_zone", "hilbert_sell_zone",
    # ---- Classic ------------------------------------------------------
    "rsi", "atr",
    # ---- Time / session -----------------------------------------------
    "hour_of_day", "day_of_week",
    "session_london", "session_newyork", "session_overlap",
    # ---- MACD ---------------------------------------------------------
    "macd_norm", "macd_signal_norm", "macd_hist_norm",
    # ---- Bollinger Bands ----------------------------------------------
    "bb_pct", "bb_width", "bb_upper_dist", "bb_lower_dist",
    # ---- EMA crossovers -----------------------------------------------
    "ema_12_dist", "ema_26_dist", "ema_50_dist", "ema_200_dist",
    "ema_12_26_cross",
    # ---- SMA distances ------------------------------------------------
    "sma_20_dist", "sma_50_dist", "sma_200_dist",
    # ---- Stochastic ---------------------------------------------------
    "stoch_k", "stoch_d", "stoch_kd_diff",
    # ---- ADX ----------------------------------------------------------
    "adx", "di_diff", "adx_di_bull",
    # ---- Oscillators --------------------------------------------------
    "williams_r", "cci", "roc_10", "mfi", "cmf", "trix", "uo",
    # ---- Volume -------------------------------------------------------
    "obv_zscore",
    # ---- Price channels -----------------------------------------------
    "vwap_dist", "psar_dist",
    "dc_pct", "dc_width",
    "kc_pct", "squeeze",
    # ---- Ichimoku -----------------------------------------------------
    "ichi_tenkan_dist", "ichi_kijun_dist",
    "ichi_cloud_pos", "ichi_cloud_thickness",
    "ichi_tk_cross", "chikou_mom",
    # ---- RSI divergence -----------------------------------------------
    "rsi_5roc", "price_rsi_div",
]
