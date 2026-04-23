"""
sg_crossover_research.py
------------------------
Walk-forward research: are SG crossover signals meaningful directional
indicators for EURUSD hourly data?

Three families of crossover tested
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1. SG(fast) vs SG(slow)  — "SG MACD"
   signal = +1 when fast SG line is above slow SG line (uptrend regime)
   Also tests the SLOPE crossover: when fast slope > slow slope
   (momentum accelerating faster in the short term than long term)

2. Price vs SG line
   signal = +1 when close is above the SG smoothed line (price leading trend)

3. SG line vs MA (SMA or EMA)
   signal = +1 when SG is above the moving average

All signals are causal (right-aligned SG, no future data).
Sharpe uses H-bar FORWARD returns to avoid the past-return look-ahead bug.

Grid
~~~~
  SG windows    : 11, 21, 31, 41, 61, 81, 101
  Polyorders    : 2, 3, 4
  Fast/slow pairs: all (fast, slow) combos where fast < slow
  MA periods    : 10, 20, 50, 100, 200
  Horizons      : 1, 3, 5 bars ahead

Walk-forward: 5 expanding folds (60 % → 92 % training, 8 % test each)

Usage
~~~~~
    python3 sg_crossover_research.py
    python3 sg_crossover_research.py --horizon 3
    python3 sg_crossover_research.py --no-xgb
"""

import argparse
import warnings
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.signal import savgol_coeffs
from sklearn.metrics import accuracy_score
import xgboost as xgb

warnings.filterwarnings("ignore")

# ------------------------------------------------------------------
# Config
# ------------------------------------------------------------------

DATA_PATH = Path(__file__).parent / "data" / "eurusd_1h_2y.csv"
OUT_PATH  = Path(__file__).parent / "data" / "sg_crossover_results.csv"

WINDOWS    = [11, 21, 31, 41, 61, 81, 101]
POLYORDERS = [2, 3, 4]
MA_PERIODS = [10, 20, 50, 100, 200]
HORIZONS   = [1, 3, 5]

N_FOLDS         = 5
TRAIN_START_PCT = 0.60
FOLD_STEP_PCT   = 0.08
BARS_PER_YEAR   = 6048   # hourly forex ≈ 252 days × 24 h

# ------------------------------------------------------------------
# Causal SG helpers
# ------------------------------------------------------------------

def _causal_sg(close: np.ndarray, window: int, polyorder: int,
               deriv: int = 0) -> np.ndarray:
    """Right-aligned (causal) SG filter at deriv=0 (level) or deriv=1 (slope)."""
    if polyorder >= window:
        return np.full(len(close), np.nan)
    try:
        coeffs = savgol_coeffs(window, polyorder, deriv=deriv, pos=window - 1)
    except Exception:
        return np.full(len(close), np.nan)
    conv   = np.convolve(close, coeffs[::-1], mode="full")
    result = np.full(len(close), np.nan)
    result[window - 1:] = conv[window - 1: len(close)]
    return result


def _sma(close: np.ndarray, period: int) -> np.ndarray:
    out = np.full(len(close), np.nan)
    cs  = np.cumsum(close)
    out[period - 1:] = (cs[period - 1:] - np.concatenate([[0], cs[:-(period)]])) / period
    return out


def _ema(close: np.ndarray, period: int) -> np.ndarray:
    alpha = 2.0 / (period + 1)
    out   = np.full(len(close), np.nan)
    # Seed with first valid SMA
    if len(close) < period:
        return out
    out[period - 1] = close[:period].mean()
    for i in range(period, len(close)):
        out[i] = alpha * close[i] + (1 - alpha) * out[i - 1]
    return out


# ------------------------------------------------------------------
# Load data
# ------------------------------------------------------------------

def load_close(data_path: Path = DATA_PATH) -> np.ndarray:
    df = pd.read_csv(data_path, parse_dates=["datetime"])
    df = df.sort_values("datetime").reset_index(drop=True)
    if hasattr(df["datetime"].dt, "tz") and df["datetime"].dt.tz is not None:
        df["datetime"] = df["datetime"].dt.tz_convert(None)
    close = df["close"].values.astype(float)
    print(f"Loaded {len(close):,} bars  "
          f"({df['datetime'].iloc[0].date()} → {df['datetime'].iloc[-1].date()})")
    return close


# ------------------------------------------------------------------
# Build feature matrix
# ------------------------------------------------------------------

def build_features(close: np.ndarray) -> pd.DataFrame:
    """
    Returns a DataFrame where every column is a ±1 crossover signal.

    Column naming:
      sgXvsgY_wF_wS_pP  — SG level crossover (fast window F, slow window S, polyorder P)
      slpXvslpY_wF_wS_pP — SG slope crossover
      pvsg_wW_pP        — price vs SG level
      sgXsma_wW_pP_mN   — SG vs SMA(N)
      sgXema_wW_pP_mN   — SG vs EMA(N)
    """
    feats = {}
    n     = len(close)

    # Pre-compute all SG levels and slopes
    sg_level = {}
    sg_slope = {}
    for W in WINDOWS:
        for P in POLYORDERS:
            key = (W, P)
            sg_level[key] = _causal_sg(close, W, P, deriv=0)
            sg_slope[key] = _causal_sg(close, W, P, deriv=1)

    # Pre-compute MAs
    sma_arr = {N: _sma(close, N)  for N in MA_PERIODS}
    ema_arr = {N: _ema(close, N)  for N in MA_PERIODS}

    # 1. SG(fast) vs SG(slow) — level crossover
    for P in POLYORDERS:
        for i, Wf in enumerate(WINDOWS):
            for Ws in WINDOWS[i + 1:]:          # Ws > Wf always
                key_f, key_s = (Wf, P), (Ws, P)
                diff = sg_level[key_f] - sg_level[key_s]
                name = f"sgXsg_wf{Wf:03d}_ws{Ws:03d}_p{P}"
                feats[name] = np.sign(diff)

    # 2. SG(fast) SLOPE vs SG(slow) SLOPE — slope crossover
    for P in POLYORDERS:
        for i, Wf in enumerate(WINDOWS):
            for Ws in WINDOWS[i + 1:]:
                diff = sg_slope[(Wf, P)] - sg_slope[(Ws, P)]
                name = f"slpXslp_wf{Wf:03d}_ws{Ws:03d}_p{P}"
                feats[name] = np.sign(diff)

    # 3. Price vs SG level
    for W in WINDOWS:
        for P in POLYORDERS:
            diff = close - sg_level[(W, P)]
            feats[f"pvsg_w{W:03d}_p{P}"] = np.sign(diff)

    # 4. SG vs SMA
    for W in WINDOWS:
        for P in POLYORDERS:
            for N in MA_PERIODS:
                diff = sg_level[(W, P)] - sma_arr[N]
                feats[f"sgXsma_w{W:03d}_p{P}_m{N:03d}"] = np.sign(diff)

    # 5. SG vs EMA
    for W in WINDOWS:
        for P in POLYORDERS:
            for N in MA_PERIODS:
                diff = sg_level[(W, P)] - ema_arr[N]
                feats[f"sgXema_w{W:03d}_p{P}_m{N:03d}"] = np.sign(diff)

    total = len(feats)
    print(f"Built {total} crossover features  "
          f"(SG×SG: {len([k for k in feats if k.startswith('sgXsg')])}  "
          f"slope×slope: {len([k for k in feats if k.startswith('slpXslp')])}  "
          f"P×SG: {len([k for k in feats if k.startswith('pvsg')])}  "
          f"SG×SMA: {len([k for k in feats if k.startswith('sgXsma')])}  "
          f"SG×EMA: {len([k for k in feats if k.startswith('sgXema')])})")
    return pd.DataFrame(feats)


# ------------------------------------------------------------------
# Targets & splits (same as sg_research.py)
# ------------------------------------------------------------------

def build_targets(close: np.ndarray, horizons: list) -> pd.DataFrame:
    targets = {}
    for H in horizons:
        fwd = np.full(len(close), np.nan)
        fwd[:-H] = close[H:] - close[:-H]
        targets[f"y_h{H}"] = np.where(np.isnan(fwd), np.nan,
                                       np.where(fwd > 0, 1.0, -1.0))
    return pd.DataFrame(targets)


def wf_splits(n: int) -> list:
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
                  test_indices: np.ndarray, horizon: int) -> float:
    valid = test_indices + horizon < len(close)
    if valid.sum() < 10:
        return 0.0
    t_v = test_indices[valid]
    ret = close[t_v + horizon] - close[t_v]
    pnl = y_pred[valid] * ret
    if pnl.std() == 0:
        return 0.0
    return float(pnl.mean() / pnl.std() * np.sqrt(BARS_PER_YEAR / horizon))


# ------------------------------------------------------------------
# Evaluate every feature individually
# ------------------------------------------------------------------

def evaluate_features(feat_df, target_df, close, horizons):
    splits = wf_splits(len(close))
    cols   = feat_df.columns.tolist()
    total  = len(cols) * len(horizons)
    done   = 0
    print(f"\nEvaluating {len(cols)} features × {len(horizons)} horizons "
          f"({total:,} evals, {len(splits)} folds)…")

    results = []
    for H in horizons:
        y_all = target_df[f"y_h{H}"].values
        for col in cols:
            x_all = feat_df[col].values
            yt_all, yp_all, idx_all = [], [], []
            for train_end, test_start, test_end in splits:
                x_te = x_all[test_start:test_end]
                y_te = y_all[test_start:test_end]
                mask = np.isfinite(x_te) & np.isfinite(y_te)
                if mask.sum() < 10:
                    continue
                yt_all.append(y_te[mask])
                yp_all.append(x_te[mask])
                idx_all.append(np.arange(test_start, test_end)[mask])

            if not yt_all:
                continue
            yt = np.concatenate(yt_all)
            yp = np.concatenate(yp_all)
            idx = np.concatenate(idx_all)

            acc    = accuracy_score(yt, yp)
            sharpe = signal_sharpe(yp, close, idx, H)

            # Parse feature type from name prefix
            if col.startswith("sgXsg"):    ftype = "sg_level_cross"
            elif col.startswith("slpXslp"):ftype = "slope_cross"
            elif col.startswith("pvsg"):   ftype = "price_vs_sg"
            elif col.startswith("sgXsma"): ftype = "sg_vs_sma"
            elif col.startswith("sgXema"): ftype = "sg_vs_ema"
            else:                          ftype = "other"

            results.append({
                "feature": col, "type": ftype,
                "horizon": H, "accuracy": round(acc, 4),
                "sharpe":  round(sharpe, 3), "n_bars": len(yt),
            })
            done += 1
            if done % 200 == 0:
                print(f"  {done}/{total}  …")

    print(f"  Done ({total:,} evals).")
    return pd.DataFrame(results).sort_values("sharpe", ascending=False).reset_index(drop=True)


# ------------------------------------------------------------------
# XGBoost
# ------------------------------------------------------------------

def run_xgb(feat_df, target_df, close, horizon, top_feats, top_n=50):
    splits = wf_splits(len(close))
    cols   = [c for c in top_feats if c in feat_df.columns][:top_n]
    X_all  = feat_df[cols].values.astype(float)
    y_all  = target_df[f"y_h{horizon}"].values

    yt_acc, yp_acc, idx_acc = [], [], []
    imp_acc = np.zeros(len(cols))

    for train_end, test_start, test_end in splits:
        X_tr, y_tr = X_all[:train_end],       y_all[:train_end]
        X_te, y_te = X_all[test_start:test_end], y_all[test_start:test_end]
        mtr = np.all(np.isfinite(X_tr), axis=1) & np.isfinite(y_tr)
        mte = np.all(np.isfinite(X_te), axis=1) & np.isfinite(y_te)
        if mtr.sum() < 50 or mte.sum() < 10:
            continue
        clf = xgb.XGBClassifier(
            n_estimators=300, max_depth=4, learning_rate=0.03,
            subsample=0.8, colsample_bytree=0.7,
            eval_metric="logloss", random_state=42, verbosity=0,
        )
        clf.fit(X_tr[mtr], (y_tr[mtr] == 1).astype(int))
        yp  = np.where(clf.predict(X_te[mte]) == 1, 1.0, -1.0)
        yt_acc.append(y_te[mte])
        yp_acc.append(yp)
        idx_acc.append(np.arange(test_start, test_end)[mte])
        imp_acc += clf.feature_importances_

    if not yt_acc:
        return {}
    yt  = np.concatenate(yt_acc)
    yp  = np.concatenate(yp_acc)
    idx = np.concatenate(idx_acc)
    imp_norm = imp_acc / (imp_acc.sum() + 1e-9)
    imp_df   = pd.DataFrame({"feature": cols, "importance": imp_norm}
                            ).sort_values("importance", ascending=False).reset_index(drop=True)
    return {
        "accuracy":    round(accuracy_score(yt, yp), 4),
        "sharpe":      round(signal_sharpe(yp, close, idx, horizon), 3),
        "n_bars":      len(yt),
        "importances": imp_df,
    }


# ------------------------------------------------------------------
# Reporting
# ------------------------------------------------------------------

def banner(title):
    print(); print("=" * 70); print(f"  {title}"); print("=" * 70)


def summarise_by_type(df_res, H):
    sub = df_res[df_res["horizon"] == H]
    tbl = sub.groupby("type")["sharpe"].agg(
        mean="mean", std="std", max="max",
        pct_pos=lambda x: (x > 0).mean() * 100,
        n="count",
    ).round(3).sort_values("mean", ascending=False)
    tbl.columns = ["mean_sharpe", "std", "best_sharpe", "pct_positive(%)", "n_signals"]
    return tbl


# ------------------------------------------------------------------
# Main
# ------------------------------------------------------------------

def main(horizons=HORIZONS, run_xgb_flag=True, data_path=DATA_PATH):
    banner("SG Crossover Research — EURUSD hourly (2 years)")
    close      = load_close(data_path)
    feat_df    = build_features(close)
    target_df  = build_targets(close, horizons)
    df_res     = evaluate_features(feat_df, target_df, close, horizons)

    df_res.to_csv(OUT_PATH, index=False)
    print(f"\nFull results → {OUT_PATH}")

    # ── Summary by signal type ────────────────────────────────────────
    for H in horizons:
        banner(f"Signal-type summary  (horizon = {H} bars)")
        print(summarise_by_type(df_res, H).to_string())

    # ── Top 25 per horizon ────────────────────────────────────────────
    for H in horizons:
        banner(f"Top 25 crossover signals  (horizon = {H} bars)")
        top = df_res[df_res["horizon"] == H].head(25)
        print(top[["feature", "type", "accuracy", "sharpe", "n_bars"]].to_string(index=False))

    # ── Best within each type per horizon ─────────────────────────────
    banner("Best signal per type × horizon")
    for H in horizons:
        print(f"\n  Horizon {H}:")
        sub  = df_res[df_res["horizon"] == H]
        best = (sub.sort_values("sharpe", ascending=False)
                   .drop_duplicates("type")
                   [["type", "feature", "accuracy", "sharpe"]])
        print(best.to_string(index=False))

    # ── Offset stability across horizons for the top-10 features ──────
    banner("Consistency check: top-10 signals across all horizons")
    top10_h1 = df_res[df_res["horizon"] == horizons[0]].head(10)["feature"].tolist()
    pivot = df_res[df_res["feature"].isin(top10_h1)].pivot_table(
        index="feature", columns="horizon", values="sharpe"
    ).round(3)
    print(pivot.to_string())

    # ── XGBoost ───────────────────────────────────────────────────────
    if not run_xgb_flag:
        return

    banner("XGBoost combined model (walk-forward)")
    for H in horizons:
        print(f"\n  Horizon {H}:")
        top_feats = df_res[df_res["horizon"] == H].head(50)["feature"].tolist()
        r = run_xgb(feat_df, target_df, close, H, top_feats, top_n=50)
        if not r:
            print("    Not enough data.")
            continue
        print(f"    Accuracy : {r['accuracy']:.4f}")
        print(f"    Sharpe   : {r['sharpe']:.3f}")
        print(f"    Test bars: {r['n_bars']}")
        print(f"\n    Top 15 importances:")
        print(r["importances"].head(15).to_string(index=False))

    banner("Research complete")
    print(f"Results saved → {OUT_PATH}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--horizon", type=int, default=None)
    parser.add_argument("--no-xgb", action="store_true")
    parser.add_argument("--data",   type=str, default=None)
    args = parser.parse_args()

    horizons  = [args.horizon] if args.horizon else HORIZONS
    data_path = Path(args.data) if args.data else DATA_PATH
    main(horizons=horizons, run_xgb_flag=not args.no_xgb, data_path=data_path)
