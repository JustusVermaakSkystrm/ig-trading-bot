"""
sg_research.py
--------------
Walk-forward research study: can Savitzky-Golay slope direction predict
the next price move in EURUSD 15-min data?

Research design
~~~~~~~~~~~~~~~
The key insight the study tests:
  - SG is computed causally (right-aligned, no future data).
  - At each bar t, slope_k = sign(sg[t-k] - sg[t-k-1]).
  - k=0 is the "freshest" slope; k=4 is four bars ago.
  - Older slopes may be more stable (polynomial better settled)
    and still carry directional information.

Grid tested
~~~~~~~~~~~
  Windows  : 11, 21, 31, 41, 51, 61, 71, 81, 101  (odd, 10–100)
  Polyorder: 1, 2, 3, 4   (linear → cubic, "number of turning points")
  Offset k : 0, 1, 2, 3, 4  (how many bars back to read slope)
  Horizons : 1, 3, 5 bars ahead (what we're trying to predict)

That gives 9 × 4 × 5 = 180 binary features per horizon.

Walk-forward CV
~~~~~~~~~~~~~~~
  5 expanding folds.  Fold i trains on the first 60+i*8 % of bars,
  tests on the next 8 %.  Metrics accumulated across all test bars.

Outputs (printed + saved to data/sg_research_results.csv)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  1. Per-feature accuracy, precision, Sharpe table (sorted by Sharpe)
  2. Top-20 individual signals
  3. XGBoost combined model: accuracy, Sharpe, feature importances
  4. Heatmaps: accuracy vs (window, polyorder) for each horizon & offset

Usage
~~~~~
    python3 sg_research.py                        # all horizons
    python3 sg_research.py --horizon 1            # 1-bar-ahead only (faster)
    python3 sg_research.py --no-xgb               # skip XGBoost
"""

import argparse
import sys
import warnings
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.signal import savgol_coeffs
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import xgboost as xgb

warnings.filterwarnings("ignore")

# ------------------------------------------------------------------
# Configuration
# ------------------------------------------------------------------

DATA_PATH_15M = Path(__file__).parent / "data" / "eurusd_15min.csv"
DATA_PATH_1H  = Path(__file__).parent / "data" / "eurusd_1h_2y.csv"
DATA_PATH     = DATA_PATH_1H          # default — overridden by --data arg
OUT_PATH      = Path(__file__).parent / "data" / "sg_research_results.csv"

# SG grid
WINDOWS    = [11, 21, 31, 41, 51, 61, 71, 81, 101]   # must be odd
POLYORDERS = [1, 2, 3, 4]
OFFSETS    = [0, 1, 2, 3, 4]                           # bars from end of signal
HORIZONS   = [1, 3, 5]                                 # bars ahead to predict

# Walk-forward
N_FOLDS       = 5
TRAIN_START_PCT = 0.60    # first fold: train on first 60 % of data
FOLD_STEP_PCT   = 0.08    # each fold adds another 8 %
# Fold sizes (fraction of total bars):
#   Fold 0: train 60%, test 8%
#   Fold 1: train 68%, test 8%
#   ...
#   Fold 4: train 92%, test 8%


# ------------------------------------------------------------------
# Causal SG filter
# ------------------------------------------------------------------

def _causal_savgol_slope_k(close: np.ndarray, window: int,
                            polyorder: int, offset: int) -> np.ndarray:
    """
    Causal SG slope at offset k.

    At each bar t:
      sg_t   = causal SG value at t   (polynomial fit on bars t-W+1..t)
      sg_tm1 = causal SG value at t-1 (fit on bars t-W..t-1)
      slope  = sg_t - sg_tm1
      feature[t] = sign(slope) at time t - offset

    Returns float array (NaN for warm-up bars).
    """
    if polyorder >= window:
        return np.full(len(close), np.nan)

    # Right-aligned convolution coefficients (deriv=1 gives slope directly)
    try:
        coeffs_d1 = savgol_coeffs(window, polyorder, deriv=1, pos=window - 1)
    except Exception:
        return np.full(len(close), np.nan)

    # Convolve: full mode, then trim to original length
    conv = np.convolve(close, coeffs_d1[::-1], mode="full")
    slope = np.full(len(close), np.nan)
    start = window - 1
    slope[start:] = conv[start: len(close)]

    # Shift by offset: feature at t = slope computed at t-offset
    if offset == 0:
        return slope

    shifted = np.full(len(close), np.nan)
    shifted[offset:] = slope[:-offset]
    return shifted


# ------------------------------------------------------------------
# Load data
# ------------------------------------------------------------------

def load_price_data(data_path: Path = None) -> pd.Series:
    """Return a clean close price Series indexed by bar number."""
    path = data_path or DATA_PATH
    df = pd.read_csv(path, parse_dates=["datetime"])
    df = df.sort_values("datetime").reset_index(drop=True)
    # Strip timezone if present (keep naive UTC)
    if hasattr(df["datetime"].dtype, "tz") or str(df["datetime"].dtype) == "datetime64[ns, UTC]":
        df["datetime"] = df["datetime"].dt.tz_localize(None) if df["datetime"].dt.tz is None \
                         else df["datetime"].dt.tz_convert(None)
    print(f"Loaded {len(df):,} bars  "
          f"({df['datetime'].iloc[0].date()} → {df['datetime'].iloc[-1].date()})"
          f"  [{path.name}]")
    return df["close"].values.astype(float)


# ------------------------------------------------------------------
# Feature matrix
# ------------------------------------------------------------------

def build_feature_matrix(close: np.ndarray) -> pd.DataFrame:
    """
    Build the full feature matrix: one column per (window, polyorder, offset).
    Column name: sg_w{W}_p{P}_k{K}
    Value: causal slope sign at offset k  (+1 up / -1 down / NaN warm-up)
    """
    rows = {}
    total = len(WINDOWS) * len(POLYORDERS) * len(OFFSETS)
    done  = 0
    for W in WINDOWS:
        for P in POLYORDERS:
            if P >= W:
                continue
            for K in OFFSETS:
                col = f"sg_w{W:03d}_p{P}_k{K}"
                slope = _causal_savgol_slope_k(close, W, P, K)
                rows[col] = np.sign(slope)
                done += 1
    print(f"Built {done} SG feature series.")
    return pd.DataFrame(rows)


# ------------------------------------------------------------------
# Targets
# ------------------------------------------------------------------

def build_targets(close: np.ndarray, horizons: list) -> pd.DataFrame:
    """
    y[t] = +1 if close[t+H] > close[t], -1 otherwise.
    NaN for last H bars.
    """
    targets = {}
    for H in horizons:
        future_ret         = np.empty(len(close))
        future_ret[:]      = np.nan
        future_ret[:-H]    = close[H:] - close[:-H]
        targets[f"y_h{H}"] = np.where(
            np.isnan(future_ret), np.nan,
            np.where(future_ret > 0, 1.0, -1.0)
        )
    return pd.DataFrame(targets)


# ------------------------------------------------------------------
# Walk-forward splits
# ------------------------------------------------------------------

def wf_splits(n: int) -> list:
    """
    Returns list of (train_end, test_start, test_end) index tuples.
    Each fold expands the training window by FOLD_STEP_PCT.
    """
    splits = []
    for i in range(N_FOLDS):
        train_frac = TRAIN_START_PCT + i * FOLD_STEP_PCT
        test_frac  = train_frac + FOLD_STEP_PCT
        train_end  = int(n * train_frac)
        test_start = train_end
        test_end   = min(int(n * test_frac), n)
        if test_start >= test_end:
            break
        splits.append((train_end, test_start, test_end))
    return splits


# ------------------------------------------------------------------
# Metrics
# ------------------------------------------------------------------

def signal_sharpe(y_pred: np.ndarray, close: np.ndarray,
                  test_indices: np.ndarray, horizon: int = 1,
                  bars_per_year: int = 6048) -> float:
    """
    Sharpe of strategy using H-bar FORWARD returns.

    At each bar t in test_indices:
      position  = y_pred (long +1 / short -1)
      P&L       = position × (close[t+H] - close[t])   ← forward return

    Annualised with bars_per_year / H trades per year.
    Default bars_per_year=6048 assumes hourly forex (252 days × 24 h).
    """
    if len(y_pred) < 10:
        return 0.0

    # Only keep bars where t + H stays within the array
    valid = test_indices + horizon < len(close)
    if valid.sum() < 10:
        return 0.0

    t_v   = test_indices[valid]
    p_v   = y_pred[valid]
    # H-bar forward return
    ret   = close[t_v + horizon] - close[t_v]
    pnl   = p_v * ret

    if pnl.std() == 0:
        return 0.0

    # Each trade lasts H bars → trades_per_year = bars_per_year / H
    trades_per_year = bars_per_year / horizon
    return float(pnl.mean() / pnl.std() * np.sqrt(trades_per_year))


# ------------------------------------------------------------------
# Evaluate individual features
# ------------------------------------------------------------------

def evaluate_features(
    feat_df: pd.DataFrame,
    target_df: pd.DataFrame,
    close: np.ndarray,
    horizons: list,
) -> pd.DataFrame:
    """
    Walk-forward accuracy + Sharpe for every (feature, horizon) pair.
    Returns a DataFrame sorted by Sharpe descending.
    """
    splits = wf_splits(len(close))
    results = []

    feature_cols = feat_df.columns.tolist()
    total_evals  = len(feature_cols) * len(horizons)
    done = 0

    print(f"\nEvaluating {len(feature_cols)} features × {len(horizons)} horizons "
          f"over {len(splits)} folds ({total_evals:,} evals)...")

    for H in horizons:
        y_col = f"y_h{H}"
        y_all = target_df[y_col].values

        for col in feature_cols:
            x_all = feat_df[col].values

            # Accumulate predictions across all folds
            y_true_all  = []
            y_pred_all  = []
            test_idx_all = []

            for train_end, test_start, test_end in splits:
                # Use sign of feature directly as prediction (no model needed)
                x_test  = x_all[test_start:test_end]
                y_test  = y_all[test_start:test_end]
                mask    = np.isfinite(x_test) & np.isfinite(y_test)
                if mask.sum() < 10:
                    continue
                y_pred = x_test[mask]   # +1 up, -1 down
                y_true = y_test[mask]
                idx    = np.arange(test_start, test_end)[mask]

                y_true_all.append(y_true)
                y_pred_all.append(y_pred)
                test_idx_all.append(idx)

            if not y_true_all:
                continue

            y_true_cat  = np.concatenate(y_true_all)
            y_pred_cat  = np.concatenate(y_pred_all)
            test_idx_cat = np.concatenate(test_idx_all)

            acc    = accuracy_score(y_true_cat, y_pred_cat)
            sharpe = signal_sharpe(y_pred_cat, close, test_idx_cat, horizon=H)
            n_bars = len(y_true_cat)

            # Parse col name for metadata
            parts = col.split("_")   # sg_w011_p1_k0
            W = int(parts[1][1:])
            P = int(parts[2][1:])
            K = int(parts[3][1:])

            results.append({
                "feature":   col,
                "window":    W,
                "polyorder": P,
                "offset":    K,
                "horizon":   H,
                "accuracy":  round(acc, 4),
                "sharpe":    round(sharpe, 3),
                "n_bars":    n_bars,
            })

            done += 1
            if done % 100 == 0:
                print(f"  {done}/{total_evals}  …")

    print(f"  Done ({total_evals} evals).")
    df_res = pd.DataFrame(results)
    return df_res.sort_values("sharpe", ascending=False).reset_index(drop=True)


# ------------------------------------------------------------------
# XGBoost combined model (walk-forward)
# ------------------------------------------------------------------

def run_xgb_combined(
    feat_df: pd.DataFrame,
    target_df: pd.DataFrame,
    close: np.ndarray,
    horizon: int,
    top_n_features: int = 40,
    top_feats: list = None,
) -> dict:
    """
    Walk-forward XGBoost using the top_n_features SG features.
    Returns accuracy, Sharpe, and feature importances.
    """
    splits = wf_splits(len(close))
    y_col  = f"y_h{horizon}"
    y_all  = target_df[y_col].values

    # Feature selection: use top_n from individual eval if supplied
    if top_feats:
        cols = [c for c in top_feats if c in feat_df.columns][:top_n_features]
    else:
        cols = feat_df.columns.tolist()[:top_n_features]

    X_all = feat_df[cols].values.astype(float)

    y_true_acc  = []
    y_pred_acc  = []
    test_idx_acc = []
    importances_acc = np.zeros(len(cols))

    for fold_i, (train_end, test_start, test_end) in enumerate(splits):
        X_tr = X_all[:train_end]
        y_tr = y_all[:train_end]
        X_te = X_all[test_start:test_end]
        y_te = y_all[test_start:test_end]

        # Drop NaN rows from training
        mask_tr = np.all(np.isfinite(X_tr), axis=1) & np.isfinite(y_tr)
        mask_te = np.all(np.isfinite(X_te), axis=1) & np.isfinite(y_te)

        if mask_tr.sum() < 50 or mask_te.sum() < 10:
            continue

        X_tr_c, y_tr_c = X_tr[mask_tr], y_tr[mask_tr]
        X_te_c, y_te_c = X_te[mask_te], y_te[mask_te]
        idx_te = np.arange(test_start, test_end)[mask_te]

        # XGBoost (binary classification: +1 vs -1, map to 1 vs 0)
        y_tr_bin = (y_tr_c == 1).astype(int)
        y_te_bin = (y_te_c == 1).astype(int)

        clf = xgb.XGBClassifier(
            n_estimators     = 200,
            max_depth        = 4,
            learning_rate    = 0.05,
            subsample        = 0.8,
            colsample_bytree = 0.8,
            eval_metric      = "logloss",
            random_state     = 42,
            verbosity        = 0,
        )
        clf.fit(X_tr_c, y_tr_bin)

        y_pred_bin = clf.predict(X_te_c)
        y_pred     = np.where(y_pred_bin == 1, 1.0, -1.0)

        y_true_acc.append(y_te_c)
        y_pred_acc.append(y_pred)
        test_idx_acc.append(idx_te)
        importances_acc += clf.feature_importances_

    if not y_true_acc:
        return {}

    y_true_cat   = np.concatenate(y_true_acc)
    y_pred_cat   = np.concatenate(y_pred_acc)
    test_idx_cat = np.concatenate(test_idx_acc)

    acc    = accuracy_score(y_true_cat, y_pred_cat)
    sharpe = signal_sharpe(y_pred_cat, close, test_idx_cat, horizon=horizon)

    # Feature importance
    imp_norm = importances_acc / (importances_acc.sum() + 1e-9)
    imp_df   = pd.DataFrame({"feature": cols, "importance": imp_norm})
    imp_df   = imp_df.sort_values("importance", ascending=False).reset_index(drop=True)

    return {
        "accuracy":    round(acc, 4),
        "sharpe":      round(sharpe, 3),
        "n_bars":      len(y_true_cat),
        "importances": imp_df,
    }


# ------------------------------------------------------------------
# Reporting helpers
# ------------------------------------------------------------------

def print_section(title: str) -> None:
    print()
    print("=" * 70)
    print(f"  {title}")
    print("=" * 70)


def print_heatmap(df_res: pd.DataFrame, horizon: int, offset: int,
                  metric: str = "accuracy") -> None:
    """Print accuracy/Sharpe as window × polyorder table."""
    sub = df_res[(df_res["horizon"] == horizon) & (df_res["offset"] == offset)]
    if sub.empty:
        return
    pivot = sub.pivot_table(index="window", columns="polyorder",
                            values=metric, aggfunc="mean")
    print(f"\n  {metric.upper()}  |  horizon={horizon}  offset k={offset}")
    print(pivot.to_string(float_format=lambda x: f"{x:6.3f}"))


# ------------------------------------------------------------------
# Main
# ------------------------------------------------------------------

def main(horizons: list = HORIZONS, run_xgb: bool = True,
         data_path: Path = None) -> None:

    print_section("SG Direction Research — EURUSD")
    close = load_price_data(data_path)

    # Build features and targets
    feat_df   = build_feature_matrix(close)
    target_df = build_targets(close, horizons)

    # ------------------------------------------------------------------
    # 1. Evaluate every individual (W, P, k, H) combination
    # ------------------------------------------------------------------
    df_res = evaluate_features(feat_df, target_df, close, horizons)

    # Save full results
    df_res.to_csv(OUT_PATH, index=False)
    print(f"\nFull results saved → {OUT_PATH}")

    # ------------------------------------------------------------------
    # 2. Summary statistics
    # ------------------------------------------------------------------
    print_section("Summary: accuracy vs offset (averaged over all W, P, H)")
    by_offset = (df_res.groupby("offset")[["accuracy", "sharpe"]]
                 .agg(["mean", "std"])
                 .round(4))
    print(by_offset.to_string())

    print_section("Summary: accuracy vs polyorder (averaged over all W, k, H)")
    by_poly = (df_res.groupby("polyorder")[["accuracy", "sharpe"]]
               .agg(["mean", "std"])
               .round(4))
    print(by_poly.to_string())

    print_section("Summary: accuracy vs window (averaged over all P, k, H)")
    by_window = (df_res.groupby("window")[["accuracy", "sharpe"]]
                 .agg(["mean", "std"])
                 .round(4))
    print(by_window.to_string())

    # ------------------------------------------------------------------
    # 3. Top-20 individual features per horizon
    # ------------------------------------------------------------------
    for H in horizons:
        print_section(f"Top 20 individual SG signals  (horizon = {H} bars ahead)")
        top = df_res[df_res["horizon"] == H].head(20)
        print(top[["feature", "window", "polyorder", "offset",
                    "accuracy", "sharpe", "n_bars"]].to_string(index=False))

    # ------------------------------------------------------------------
    # 4. Heatmaps: accuracy by window × polyorder for each (horizon, offset)
    # ------------------------------------------------------------------
    print_section("Accuracy Heatmaps (window × polyorder)")
    for H in horizons:
        for K in [0, 1, 2, 3, 4]:
            print_heatmap(df_res, horizon=H, offset=K, metric="accuracy")

    print_section("Sharpe Heatmaps (window × polyorder)")
    for H in horizons:
        for K in [0, 1, 2, 3, 4]:
            print_heatmap(df_res, horizon=H, offset=K, metric="sharpe")

    # ------------------------------------------------------------------
    # 5. Offset stability analysis: does k>0 outperform k=0?
    # ------------------------------------------------------------------
    print_section("Offset Stability: does trusting an earlier bar help?")
    for H in horizons:
        print(f"\n  Horizon {H} — mean Sharpe by offset:")
        sub = df_res[df_res["horizon"] == H]
        tbl = sub.groupby("offset")["sharpe"].agg(
            mean="mean", std="std", max="max",
            pct_positive=lambda x: (x > 0).mean() * 100,
        ).round(3)
        tbl.columns = ["mean_sharpe", "std_sharpe", "best_sharpe", "pct_positive(%)"]
        print(tbl.to_string())

    # ------------------------------------------------------------------
    # 6. XGBoost combined model
    # ------------------------------------------------------------------
    if not run_xgb:
        print("\n(XGBoost step skipped — pass --xgb to enable)")
        return

    print_section("XGBoost Combined Model (walk-forward)")
    for H in horizons:
        print(f"\n  Horizon {H} bars ahead:")
        # Feed top-40 features by Sharpe for this horizon into XGBoost
        top_feats = (df_res[df_res["horizon"] == H]
                     .head(40)["feature"]
                     .tolist())
        result = run_xgb_combined(feat_df, target_df, close,
                                   horizon=H, top_n_features=40,
                                   top_feats=top_feats)
        if not result:
            print("    Not enough data.")
            continue
        print(f"    Accuracy : {result['accuracy']:.4f}")
        print(f"    Sharpe   : {result['sharpe']:.3f}")
        print(f"    Test bars: {result['n_bars']}")
        print(f"\n    Top 15 feature importances:")
        print(result["importances"].head(15).to_string(index=False))

    print_section("Research Complete")
    print(f"Full results CSV: {OUT_PATH}")


# ------------------------------------------------------------------
# Entry point
# ------------------------------------------------------------------

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SG Direction Research")
    parser.add_argument("--horizon", type=int, default=None,
                        help="Single horizon to test (default: all = 1,3,5)")
    parser.add_argument("--no-xgb", action="store_true",
                        help="Skip XGBoost combined model")
    parser.add_argument("--data", type=str, default=None,
                        help="Path to CSV data file (default: eurusd_1h_2y.csv)")
    parser.add_argument("--15m", dest="use_15m", action="store_true",
                        help="Use 15-min data instead of 1h")
    args = parser.parse_args()

    if args.use_15m:
        data_path = DATA_PATH_15M
    elif args.data:
        data_path = Path(args.data)
    else:
        data_path = DATA_PATH_1H

    horizons = [args.horizon] if args.horizon else HORIZONS
    main(horizons=horizons, run_xgb=not args.no_xgb, data_path=data_path)
