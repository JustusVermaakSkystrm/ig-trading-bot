"""
optimize.py
-----------
Full pipeline: load data → compute features → (optionally) HPO →
train model → (optionally) regime-gate → backtest → sensitivity sweep.

NEW FLAGS vs previous version:
  --no-binary       Use legacy 3-class labels (default: binary Triple Barrier)
  --regime          Enable HMM regime gating (only trade in trending regime)
  --rolling N       Rolling walk-forward: training window = N bars (default: expanding)

Usage:
    # Standard: triple-barrier binary model, single backtest
    python optimize.py

    # Walk-forward (5 folds, expanding window)
    python optimize.py --walk-forward 5

    # Walk-forward with HMM regime gating
    python optimize.py --walk-forward 5 --regime

    # Rolling walk-forward (3000-bar training window, weekly step)
    python optimize.py --walk-forward 5 --rolling 3000

    # Optuna HPO + all features
    python optimize.py --optimize --trials 50 --walk-forward 5 --regime --plot equity.png
"""

import argparse
import logging
import os
import sys

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

from data_pipeline import load_data
from features import compute_features, FEATURE_COLUMNS
from model import (
    TradingModel, optimize_hyperparams, XGB_PARAMS,
    triple_barrier_labels, create_labels, TB_MAX_BARS,
    walk_forward_split,
)
from backtest import Backtester, walk_forward_backtest

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)


# ------------------------------------------------------------------
# CLI
# ------------------------------------------------------------------

def parse_args():
    p = argparse.ArgumentParser(
        description="Train, optimise, and backtest the EURUSD ML trading bot"
    )
    p.add_argument("--optimize",    action="store_true",
                   help="Run Optuna HPO before training")
    p.add_argument("--trials",      type=int, default=50)
    p.add_argument("--walk-forward", type=int, default=0, metavar="N",
                   help="N-fold walk-forward backtest (0 = single train/test)")
    p.add_argument("--rolling",     type=int, default=0, metavar="BARS",
                   help="Rolling walk-forward: fixed training window in bars "
                        "(0 = expanding, default)")
    p.add_argument("--regime",      action="store_true",
                   help="Enable HMM regime gating (only trade in trending regime)")
    p.add_argument("--no-binary",   action="store_true",
                   help="Use legacy 3-class labels (not recommended)")
    p.add_argument("--plot",        type=str, default=None, metavar="PATH")
    p.add_argument("--risk",        type=float, default=0.01)
    p.add_argument("--stop-mult",   type=float, default=1.5,
                   help="Stop-loss ATR multiple (default: 1.5 — matches TB_SL_MULT)")
    p.add_argument("--tp-mult",     type=float, default=1.5,
                   help="Take-profit ATR multiple (default: 1.5 — matches TB_TP_MULT)")
    p.add_argument("--confidence",  type=float, default=0.55,
                   help="Min model confidence to trade (default: 0.55)")
    p.add_argument("--capital",     type=float, default=10_000.0)
    p.add_argument("--spread",      type=float, default=0.0001)
    return p.parse_args()


# ------------------------------------------------------------------
# Feature importance printer
# ------------------------------------------------------------------

def print_feature_importance(model: TradingModel, top_n: int = 20) -> None:
    importance = pd.Series(
        model.clf.feature_importances_, index=FEATURE_COLUMNS
    ).sort_values(ascending=False)

    print(f"\n{'='*50}")
    print(f"  TOP {top_n} FEATURES BY IMPORTANCE")
    print(f"{'='*50}")
    for i, (feat, val) in enumerate(importance.head(top_n).items(), 1):
        bar = "█" * int(val * 300)
        print(f"  {i:>2}. {feat:<32s} {val:.4f}  {bar}")
    print(f"{'='*50}\n")


# ------------------------------------------------------------------
# Parameter sensitivity sweep
# ------------------------------------------------------------------

def sensitivity_sweep(df_feat, model, base_args) -> None:
    signals = model.generate_test_signals(df_feat)

    stop_mults = [1.0, 1.5, 2.0, 2.5]
    tp_mults   = [1.5, 2.0, 3.0]
    confs      = [0.50, 0.55, 0.60, 0.65]

    print(f"\n{'='*80}")
    print("  PARAMETER SENSITIVITY SWEEP")
    print(f"{'='*80}")
    print(f"  {'stop_mult':>9}  {'tp_mult':>7}  {'conf':>5}  "
          f"{'ret%':>7}  {'sharpe':>7}  {'wr%':>6}  {'pf':>6}  {'dd%':>6}  {'n':>5}")
    print(f"  {'-'*9}  {'-'*7}  {'-'*5}  "
          f"{'-'*7}  {'-'*7}  {'-'*6}  {'-'*6}  {'-'*6}  {'-'*5}")

    rows = []
    for sm in stop_mults:
        for tm in tp_mults:
            for cf in confs:
                bt = Backtester(
                    initial_capital=base_args.capital,
                    risk_pct=base_args.risk,
                    stop_atr_mult=sm, tp_atr_mult=tm,
                    spread_pips=base_args.spread,
                    min_confidence=cf,
                )
                r = bt.run(df_feat, signals)
                m = r.metrics
                if "error" in m or m.get("n_trades", 0) == 0:
                    continue
                rows.append(dict(
                    stop_mult=sm, tp_mult=tm, conf=cf,
                    ret_pct=m["total_return_pct"], sharpe=m["sharpe"],
                    wr_pct=m["win_rate_pct"], pf=m["profit_factor"],
                    dd_pct=m["max_drawdown_pct"], n_trades=m["n_trades"],
                ))
                print(f"  {sm:>9.1f}  {tm:>7.1f}  {cf:>5.2f}  "
                      f"{m['total_return_pct']:>+7.2f}  {m['sharpe']:>7.3f}  "
                      f"{m['win_rate_pct']:>6.1f}  {m['profit_factor']:>6.3f}  "
                      f"{m['max_drawdown_pct']:>+6.2f}  {m['n_trades']:>5}")

    print(f"{'='*80}")
    if rows:
        best = max(rows, key=lambda r: r["sharpe"])
        print(f"\n  Best by Sharpe: stop={best['stop_mult']:.1f}  "
              f"tp={best['tp_mult']:.1f}  conf={best['conf']:.2f}  "
              f"sharpe={best['sharpe']:.3f}  ret={best['ret_pct']:+.2f}%\n")


# ------------------------------------------------------------------
# Rolling walk-forward with regime gating
# ------------------------------------------------------------------

def rolling_walk_forward(
    df_features:  pd.DataFrame,
    n_splits:     int,
    train_window: int,
    backtester:   Backtester,
    model_params: dict,
    binary:       bool  = True,
    embargo:      int   = TB_MAX_BARS,
    use_regime:   bool  = False,
) -> None:
    """
    Rolling-window walk-forward backtest.

    Each fold:
      train  = df[test_start - train_window : test_start - embargo]
      test   = df[test_start : test_start + fold_size]

    Regime gating (--regime):
      After each fold's model predictions, suppress signals in non-trending
      regime bars.  The HMM is fitted on the training window only.
    """
    from model import triple_barrier_labels, create_labels

    df = df_features.copy()
    if binary:
        df["label"] = triple_barrier_labels(df)
    else:
        df["label"] = create_labels(df)
    df = df.dropna(subset=["label"] + FEATURE_COLUMNS)

    n = len(df)
    if train_window >= n:
        logger.error("train_window (%d) >= total rows (%d) — aborting", train_window, n)
        return

    # Split remaining data after the first training window into n_splits
    available = n - train_window
    fold_size = available // n_splits

    logger.info(
        "Rolling walk-forward: %d folds, %d-bar train window, %d-bar test folds",
        n_splits, train_window, fold_size,
    )

    all_results = []
    for fold in range(n_splits):
        test_start = train_window + fold * fold_size
        test_end   = min(test_start + fold_size, n)
        train_start = max(0, test_start - train_window)
        train_end   = test_start - embargo

        train_df = df.iloc[train_start:train_end]
        test_df  = df.iloc[test_start:test_end]

        if len(train_df) < 200 or len(test_df) < 10:
            logger.warning("Fold %d: insufficient data — skipping", fold + 1)
            continue

        logger.info("Fold %d/%d: train=[%d:%d] (%d rows)  test=[%d:%d] (%d rows)  [%s → %s]",
                    fold + 1, n_splits,
                    train_start, train_end, len(train_df),
                    test_start, test_end, len(test_df),
                    test_df["datetime"].iloc[0].strftime("%Y-%m-%d"),
                    test_df["datetime"].iloc[-1].strftime("%Y-%m-%d"))

        # ---- Train --------------------------------------------------------
        params = model_params or {}
        model  = TradingModel(params=params if params else None,
                              binary=binary, embargo=0)

        n_val       = max(int(len(train_df) * 0.15), 50)
        inner_train = train_df.iloc[:-n_val]
        inner_val   = train_df.iloc[-n_val:]

        enc = LabelEncoder()
        enc.fit(np.concatenate([
            inner_train["label"].astype(int).values,
            inner_val["label"].astype(int).values,
            test_df["label"].astype(int).values,
        ]))
        model.encoder = enc

        X_tr = inner_train[FEATURE_COLUMNS].values
        X_vl = inner_val[FEATURE_COLUMNS].values
        X_te = test_df[FEATURE_COLUMNS].values

        if binary:
            y_tr = ((inner_train["label"].astype(int).values + 1) // 2)
            y_vl = ((inner_val["label"].astype(int).values   + 1) // 2)
        else:
            y_tr = enc.transform(inner_train["label"].astype(int).values)
            y_vl = enc.transform(inner_val["label"].astype(int).values)

        if len(X_vl) >= 50:
            model.clf.set_params(early_stopping_rounds=20)
            model.clf.fit(X_tr, y_tr, eval_set=[(X_vl, y_vl)], verbose=False)
        else:
            model.clf.fit(X_tr, y_tr, verbose=False)
        model.trained = True

        # ---- Generate signals on test_df -----------------------------------
        probs  = model.clf.predict_proba(X_te)
        if binary:
            p_buy   = probs[:, 1]
            p_sell  = probs[:, 0]
            sigs    = np.where(p_buy >= p_sell, 1, -1).astype(int)
            confs   = np.where(sigs == 1, p_buy, p_sell)
        else:
            cls   = np.argmax(probs, axis=1)
            sigs  = enc.inverse_transform(cls).astype(int)
            confs = probs[np.arange(len(probs)), cls]

        signals = pd.DataFrame({
            "datetime":   test_df["datetime"].values,
            "close":      test_df["close"].values,
            "atr":        test_df["atr"].values,
            "signal":     sigs,
            "confidence": confs,
        })

        # ---- HMM regime gating -------------------------------------------
        if use_regime:
            try:
                from regime import RegimeDetector
                detector = RegimeDetector()
                detector.fit(train_df)
                is_trending = detector.is_trending(test_df)
                is_trending.index = signals.index
                suppressed = (~is_trending).sum()
                signals.loc[~is_trending.values, "signal"] = 0  # HOLD in ranging regime
                logger.info("Regime gating: suppressed %d/%d signals in ranging regime",
                            suppressed, len(signals))
            except Exception as exc:
                logger.warning("Regime gating failed: %s — continuing without", exc)

        # ---- Backtest -------------------------------------------------------
        results = backtester.run(test_df, signals)
        backtester.print_report(results)
        all_results.append(results.metrics)

    # ---- Summary --------------------------------------------------------
    _print_wf_summary(all_results)


# ------------------------------------------------------------------
# Walk-forward summary printer (shared)
# ------------------------------------------------------------------

def _print_wf_summary(all_results: list) -> None:
    valid = [m for m in all_results
             if "error" not in m and m.get("n_trades", 0) > 0]
    print(f"\n{'='*60}")
    print("  WALK-FORWARD SUMMARY")
    print(f"{'='*60}")
    if not valid:
        print("  No folds produced trades.")
        print(f"{'='*60}\n")
        return

    metrics_to_show = [
        ("total_return_pct", "Total return %"),
        ("sharpe",           "Sharpe"),
        ("win_rate_pct",     "Win rate %"),
        ("profit_factor",    "Profit factor"),
        ("max_drawdown_pct", "Max drawdown %"),
        ("n_trades",         "Trades"),
    ]
    for key, label in metrics_to_show:
        vals = [m[key] for m in valid if key in m]
        if vals:
            print(f"  {label:<20s}: avg={np.mean(vals):>8.3f}  "
                  f"min={np.min(vals):>8.3f}  max={np.max(vals):>8.3f}")
    print(f"{'='*60}\n")


# ------------------------------------------------------------------
# Main
# ------------------------------------------------------------------

def main():
    args   = parse_args()
    binary = not args.no_binary

    # ---- 1. Load & featurise ------------------------------------------
    logger.info("Loading price data...")
    price_df = load_data()
    logger.info("Loaded %d bars  (%s → %s)",
                len(price_df),
                price_df["datetime"].iloc[0].strftime("%Y-%m-%d"),
                price_df["datetime"].iloc[-1].strftime("%Y-%m-%d"))

    logger.info("Computing features...")
    df_feat = compute_features(price_df)
    logger.info("Feature matrix: %d bars × %d columns", *df_feat.shape)

    # ---- 2. (Optional) Optuna HPO -------------------------------------
    params = XGB_PARAMS.copy()
    if args.optimize:
        logger.info("Running Optuna HPO with %d trials...", args.trials)
        params = optimize_hyperparams(df_feat, n_trials=args.trials, binary=binary)
        print("\nBest hyperparameters:")
        for k, v in params.items():
            print(f"  {k}: {v}")

    # ---- 3. Build backtester ------------------------------------------
    bt = Backtester(
        initial_capital=args.capital,
        risk_pct=args.risk,
        stop_atr_mult=args.stop_mult,
        tp_atr_mult=args.tp_mult,
        spread_pips=args.spread,
        min_confidence=args.confidence,
    )

    # ---- 4. Walk-forward or single train/test -------------------------
    if args.walk_forward > 1:
        if args.rolling > 0:
            logger.info("Running rolling walk-forward (%d folds, %d-bar window)...",
                        args.walk_forward, args.rolling)
            rolling_walk_forward(
                df_features  = df_feat,
                n_splits     = args.walk_forward,
                train_window = args.rolling,
                backtester   = bt,
                model_params = params,
                binary       = binary,
                embargo      = TB_MAX_BARS,
                use_regime   = args.regime,
            )
        else:
            logger.info("Running %d-fold expanding walk-forward...", args.walk_forward)
            walk_forward_backtest(
                df_features  = df_feat,
                price_df     = price_df,
                n_splits     = args.walk_forward,
                backtester   = bt,
                model_params = params,
                binary       = binary,
                embargo      = TB_MAX_BARS,
                use_regime   = args.regime,
            )
        # Train a final model on all data for feature importance
        model = TradingModel(params=params, binary=binary)
        model.train(df_feat)

    else:
        logger.info("Training model (binary=%s)...", binary)
        model = TradingModel(params=params, binary=binary)
        model.train(df_feat)
        model.save()

        logger.info("Generating test signals...")
        signals = model.generate_test_signals(df_feat)

        # Optional regime gating for single-fold
        if args.regime:
            logger.info("Applying HMM regime gating...")
            try:
                from regime import RegimeDetector
                df = df_feat.copy()
                if binary:
                    df["label"] = triple_barrier_labels(df)
                else:
                    df["label"] = create_labels(df)
                df = df.dropna(subset=["label"] + FEATURE_COLUMNS)
                train_df, _, _ = walk_forward_split(df, embargo_bars=TB_MAX_BARS)
                detector = RegimeDetector()
                detector.fit(train_df)

                test_mask = df_feat["datetime"].isin(signals["datetime"])
                test_feat = df_feat[test_mask].reset_index(drop=True)
                is_trending = detector.is_trending(test_feat)
                suppressed = (~is_trending).sum()
                signals.loc[~is_trending.values, "signal"] = 0
                logger.info("Regime gating: suppressed %d/%d signals", suppressed, len(signals))
            except Exception as exc:
                logger.warning("Regime gating failed: %s", exc)

        logger.info("Running backtest on %d bars...", len(signals))
        results = bt.run(df_feat, signals)
        bt.print_report(results)

        if args.plot:
            bt.plot_equity(results, save_path=args.plot)

    # ---- 5. Feature importance ----------------------------------------
    print_feature_importance(model, top_n=20)

    # ---- 6. Sensitivity sweep (single-fold only) ----------------------
    if args.walk_forward <= 1:
        logger.info("Running sensitivity sweep...")
        sensitivity_sweep(df_feat, model, args)

    # ---- 7. Latest signal ---------------------------------------------
    signal, prob = model.predict_latest(df_feat)
    label = {1: "BUY", -1: "SELL", 0: "HOLD"}.get(signal, "UNKNOWN")
    print(f"\nLatest signal on most recent bar: {label}  (confidence: {prob:.1%})")


if __name__ == "__main__":
    main()
