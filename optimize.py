"""
optimize.py
-----------
Full pipeline: load data → compute features → (optionally) run Optuna HPO →
train model → backtest on out-of-sample data → print report.

Usage:
    # Standard run: train + single backtest
    python optimize.py

    # With Optuna hyperparameter optimisation (50 trials)
    python optimize.py --optimize --trials 50

    # Walk-forward backtest across 5 folds
    python optimize.py --walk-forward 5

    # Save equity-curve plot
    python optimize.py --plot equity.png

    # All options combined
    python optimize.py --optimize --trials 30 --walk-forward 5 --plot equity.png
"""

import argparse
import logging
import os
import sys

import numpy as np
import pandas as pd

# ---- project imports ----
from data_pipeline import load_data
from features import compute_features
from model import TradingModel, optimize_hyperparams, XGB_PARAMS
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
    p.add_argument("--optimize", action="store_true",
                   help="Run Optuna HPO before training (requires: pip install optuna)")
    p.add_argument("--trials", type=int, default=50,
                   help="Number of Optuna trials (default: 50)")
    p.add_argument("--walk-forward", type=int, default=0, metavar="N",
                   help="Run N-fold walk-forward backtest (0 = single train/test)")
    p.add_argument("--plot", type=str, default=None, metavar="PATH",
                   help="Save equity-curve plot to PATH (e.g. equity.png)")
    p.add_argument("--risk", type=float, default=0.01,
                   help="Risk per trade as fraction of capital (default: 0.01 = 1%%)")
    p.add_argument("--stop-mult", type=float, default=2.0,
                   help="Stop-loss as multiple of ATR (default: 2.0)")
    p.add_argument("--tp-mult", type=float, default=3.0,
                   help="Take-profit as multiple of ATR (default: 3.0)")
    p.add_argument("--confidence", type=float, default=0.55,
                   help="Minimum model confidence to trade (default: 0.55)")
    p.add_argument("--capital", type=float, default=10_000.0,
                   help="Starting capital (default: 10000)")
    p.add_argument("--spread", type=float, default=0.0001,
                   help="Spread cost in price units per trade (default: 0.0001 = 1 pip)")
    return p.parse_args()


# ------------------------------------------------------------------
# Helper: feature importance table
# ------------------------------------------------------------------

def print_feature_importance(model: TradingModel, top_n: int = 20) -> None:
    from features import FEATURE_COLUMNS
    importance = pd.Series(
        model.clf.feature_importances_,
        index=FEATURE_COLUMNS
    ).sort_values(ascending=False)

    print(f"\n{'='*50}")
    print(f"  TOP {top_n} FEATURES BY IMPORTANCE")
    print(f"{'='*50}")
    for i, (feat, val) in enumerate(importance.head(top_n).items(), 1):
        bar = "█" * int(val * 300)
        print(f"  {i:>2}. {feat:<30s} {val:.4f}  {bar}")
    print(f"{'='*50}\n")


# ------------------------------------------------------------------
# Helper: parameter sensitivity table
# ------------------------------------------------------------------

def sensitivity_sweep(df_feat: pd.DataFrame, price_df: pd.DataFrame,
                      model: TradingModel, base_args) -> None:
    """
    Quick sweep of stop/TP multipliers and confidence thresholds to
    show how backtest metrics change with parameter choice.
    """
    from features import FEATURE_COLUMNS
    from model import create_labels

    signals = model.generate_test_signals(df_feat)

    stop_mults = [1.5, 2.0, 2.5, 3.0]
    tp_mults   = [2.0, 3.0, 4.0]
    confs      = [0.50, 0.55, 0.60, 0.65]

    print(f"\n{'='*80}")
    print("  PARAMETER SENSITIVITY SWEEP")
    print(f"{'='*80}")
    print(f"  {'stop_mult':>9}  {'tp_mult':>7}  {'conf':>5}  "
          f"{'ret%':>7}  {'sharpe':>7}  {'wr%':>6}  {'pf':>6}  {'dd%':>6}  {'n':>5}")
    print(f"  {'-'*9}  {'-'*7}  {'-'*5}  {'-'*7}  {'-'*7}  {'-'*6}  {'-'*6}  {'-'*6}  {'-'*5}")

    rows = []
    for sm in stop_mults:
        for tm in tp_mults:
            for cf in confs:
                bt = Backtester(
                    initial_capital = base_args.capital,
                    risk_pct        = base_args.risk,
                    stop_atr_mult   = sm,
                    tp_atr_mult     = tm,
                    spread_pips     = base_args.spread,
                    min_confidence  = cf,
                )
                r = bt.run(price_df, signals)
                m = r.metrics
                if "error" in m or m.get("n_trades", 0) == 0:
                    continue
                rows.append({
                    "stop_mult": sm, "tp_mult": tm, "conf": cf,
                    "ret_pct":   m["total_return_pct"],
                    "sharpe":    m["sharpe"],
                    "wr_pct":    m["win_rate_pct"],
                    "pf":        m["profit_factor"],
                    "dd_pct":    m["max_drawdown_pct"],
                    "n_trades":  m["n_trades"],
                })
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
# Main
# ------------------------------------------------------------------

def main():
    args = parse_args()

    # ---- 1. Load data ------------------------------------------------
    logger.info("Loading price data...")
    price_df = load_data()
    logger.info("Loaded %d bars  (%s → %s)",
                len(price_df),
                price_df["datetime"].iloc[0].strftime("%Y-%m-%d"),
                price_df["datetime"].iloc[-1].strftime("%Y-%m-%d"))

    # ---- 2. Compute features -----------------------------------------
    logger.info("Computing features (20 technical indicators + custom)...")
    df_feat = compute_features(price_df)
    logger.info("Feature matrix: %d bars × %d columns", *df_feat.shape)

    # ---- 3. (Optional) Optuna HPO ------------------------------------
    params = XGB_PARAMS.copy()
    if args.optimize:
        logger.info("Running Optuna HPO with %d trials...", args.trials)
        params = optimize_hyperparams(df_feat, n_trials=args.trials)
        print(f"\nBest hyperparameters:")
        for k, v in params.items():
            print(f"  {k}: {v}")

    # ---- 4. Walk-forward or single train/test -------------------------
    bt = Backtester(
        initial_capital = args.capital,
        risk_pct        = args.risk,
        stop_atr_mult   = args.stop_mult,
        tp_atr_mult     = args.tp_mult,
        spread_pips     = args.spread,
        min_confidence  = args.confidence,
    )

    if args.walk_forward > 1:
        logger.info("Running %d-fold walk-forward backtest...", args.walk_forward)
        walk_forward_backtest(
            df_features  = df_feat,
            price_df     = price_df,
            n_splits     = args.walk_forward,
            backtester   = bt,
            model_params = params,
        )
        # Single final model for feature importance
        model = TradingModel(params=params)
        model.train(df_feat)

    else:
        # Single train + backtest
        logger.info("Training model on full data...")
        model = TradingModel(params=params)
        model.train(df_feat)
        model.save()

        logger.info("Generating test-set signals...")
        signals = model.generate_test_signals(df_feat)

        logger.info("Running backtest on %d bars...", len(signals))
        results = bt.run(price_df, signals)
        bt.print_report(results)

        if args.plot:
            bt.plot_equity(results, save_path=args.plot)

    # ---- 5. Feature importance ----------------------------------------
    print_feature_importance(model, top_n=20)

    # ---- 6. Parameter sensitivity sweep ------------------------------
    # Only run sensitivity sweep for single-fold mode (fast)
    if args.walk_forward <= 1:
        logger.info("Running parameter sensitivity sweep...")
        sensitivity_sweep(df_feat, price_df, model, args)

    # ---- 7. Latest signal for sanity check ---------------------------
    signal, prob = model.predict_latest(df_feat)
    label = {1: "BUY", -1: "SELL", 0: "HOLD"}.get(signal, "UNKNOWN")
    print(f"\nLatest signal on most recent bar: {label}  (confidence: {prob:.1%})")


if __name__ == "__main__":
    main()
