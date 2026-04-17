"""
backtest.py
-----------
Event-driven backtesting engine for the EURUSD spread betting bot.

Simulation rules:
  - Signals are consumed at the CLOSE of bar T (model outputs on bar-close data)
  - Entry is at the OPEN of bar T+1 (realistic — we act on the next bar)
  - Stop-loss and take-profit are checked intrabar using high/low
  - When both SL and TP are hit on the same bar, we assume the one closer
    to the prior close is hit first (conservative rule = SL wins on gap bars)
  - One position at a time; new signals are ignored while a position is open
  - Spread cost applied on entry (flat pips constant, configurable)

Performance metrics returned:
  - Total return %
  - Annualized return (CAGR)
  - Sharpe ratio (annualized)
  - Sortino ratio
  - Maximum drawdown %
  - Max drawdown duration (bars)
  - Win rate %
  - Profit factor
  - Average win / average loss
  - Expectancy per trade
  - Number of trades
  - Calmar ratio (CAGR / max drawdown)

Usage:
    from backtest import Backtester
    bt = Backtester()
    results = bt.run(df_with_prices, signals_df)
    bt.print_report(results)
    bt.plot_equity(results)           # requires matplotlib
"""

import logging
from dataclasses import dataclass, field
from typing import List

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

logger = logging.getLogger(__name__)

# 15-min bars per year (forex trades ~24h on weekdays)
# Approx 252 trading days × 24h × 4 bars/hour = 24 192
BARS_PER_YEAR: float = 252 * 24 * 4


@dataclass
class Trade:
    entry_bar:    int
    exit_bar:     int
    direction:    int        # +1 = long, -1 = short
    entry_price:  float
    exit_price:   float
    stop_price:   float
    tp_price:     float
    exit_reason:  str        # "TP", "SL", "EOD"
    pnl_pct:      float      # % of capital at entry
    pnl_abs:      float      # absolute currency units


@dataclass
class BacktestResults:
    trades:       List[Trade]
    equity_curve: pd.DataFrame   # columns: datetime, equity, drawdown_pct
    metrics:      dict


class Backtester:
    """
    Configurable bar-by-bar backtesting engine.

    Parameters
    ----------
    initial_capital   : Starting account balance (arbitrary currency units)
    risk_pct          : Fraction of capital risked per trade (e.g. 0.01 = 1%)
    stop_atr_mult     : Initial stop-loss distance as multiple of ATR
    tp_atr_mult       : Take-profit distance as multiple of ATR
    spread_pips       : Fixed spread cost in price units (e.g. 0.0001 for 1 pip)
    min_confidence    : Only trade if model confidence ≥ this threshold
    exit_method       : One of:
        "fixed"           — hard SL + TP set at entry (default)
        "trailing"        — Chandelier trailing stop; SL ratchets with price,
                            no fixed TP (tp_atr_mult ignored)
        "breakeven_trail" — move SL to entry (breakeven) once price reaches
                            +1R; then switch to Chandelier trailing stop
    trail_atr_mult    : ATR multiple for the trailing stop distance
                        (used for "trailing" and "breakeven_trail" modes)
    """

    EXIT_FIXED          = "fixed"
    EXIT_TRAILING       = "trailing"
    EXIT_BREAKEVEN_TRAIL = "breakeven_trail"

    def __init__(
        self,
        initial_capital:  float = 10_000.0,
        risk_pct:          float = 0.01,
        stop_atr_mult:     float = 2.0,
        tp_atr_mult:       float = 3.0,
        spread_pips:       float = 0.0001,
        min_confidence:    float = 0.55,
        exit_method:       str   = "fixed",
        trail_atr_mult:    float = 1.5,
    ):
        self.initial_capital  = initial_capital
        self.risk_pct         = risk_pct
        self.stop_atr_mult    = stop_atr_mult
        self.tp_atr_mult      = tp_atr_mult
        self.spread_pips      = spread_pips
        self.min_confidence   = min_confidence
        self.exit_method      = exit_method
        self.trail_atr_mult   = trail_atr_mult
        if exit_method not in (self.EXIT_FIXED, self.EXIT_TRAILING,
                               self.EXIT_BREAKEVEN_TRAIL):
            raise ValueError(f"exit_method must be one of: fixed, trailing, "
                             f"breakeven_trail.  Got: {exit_method!r}")

    # ------------------------------------------------------------------
    # Main simulation
    # ------------------------------------------------------------------

    def run(self, price_df: pd.DataFrame, signals_df: pd.DataFrame) -> BacktestResults:
        """
        Simulate trades on historical data.

        Parameters
        ----------
        price_df    : DataFrame with columns [datetime, open, high, low, close, atr]
                      Must be aligned with signals_df (same index/length after merge).
        signals_df  : DataFrame from TradingModel.generate_test_signals()
                      columns: [datetime, close, atr, signal, confidence]

        Returns
        -------
        BacktestResults with trades list, equity curve, and metrics dict.
        """
        # Merge on datetime so bars align correctly.
        # ATR can come from either price_df (if it has the column) or signals_df.
        price_cols = ["datetime", "open", "high", "low", "close"]
        if "atr" in price_df.columns:
            price_cols.append("atr")
        sig_cols = ["datetime", "signal", "confidence"]
        if "atr" in signals_df.columns and "atr" not in price_cols:
            sig_cols.append("atr")

        # Normalise both datetime columns to tz-naive UTC to avoid merge errors
        # when one side is tz-aware and the other is tz-naive.
        def _to_utc_naive(df_in: pd.DataFrame) -> pd.DataFrame:
            df_out = df_in.copy()
            col    = df_out["datetime"]
            if hasattr(col.dt, "tz") and col.dt.tz is not None:
                df_out["datetime"] = col.dt.tz_convert("UTC").dt.tz_localize(None)
            else:
                df_out["datetime"] = pd.to_datetime(col)
            return df_out

        left  = _to_utc_naive(price_df[price_cols])
        right = _to_utc_naive(signals_df[sig_cols])

        df = pd.merge(left, right, on="datetime", how="inner") \
               .sort_values("datetime").reset_index(drop=True)

        if df.empty:
            logger.error("No overlapping bars between price_df and signals_df.")
            return BacktestResults(trades=[], equity_curve=pd.DataFrame(),
                                   metrics={"error": "No overlapping bars between price and signal data."})

        n               = len(df)
        capital         = self.initial_capital
        position        = 0          # +1 long, -1 short, 0 flat
        entry_bar       = -1
        entry_price     = 0.0
        stop_price      = 0.0        # current active SL (may move for trailing)
        tp_price        = 0.0        # current active TP (inf for trailing modes)
        initial_sl      = 0.0        # SL at entry (used for breakeven trigger)
        trail_extreme   = 0.0        # highest high (long) / lowest low (short) since entry
        at_breakeven    = False       # has SL been moved to entry?
        position_size   = 0.0

        trades:       List[Trade]  = []
        equity_curve: List[dict]   = []

        for i in range(n):
            row     = df.iloc[i]
            bar_o   = float(row["open"])
            bar_h   = float(row["high"])
            bar_l   = float(row["low"])
            bar_c   = float(row["close"])
            bar_atr = float(row["atr"]) if float(row["atr"]) > 0 else 1e-6

            # ----------------------------------------------------------
            # 1a. Update trailing / breakeven stop BEFORE checking exit
            #     (uses the current bar's high/low to ratchet the SL)
            # ----------------------------------------------------------
            if position != 0 and self.exit_method != self.EXIT_FIXED:
                stop_dist_orig = abs(entry_price - initial_sl)

                if position == 1:   # long: trail from highest high
                    trail_extreme = max(trail_extreme, bar_h)
                    new_trail_sl  = trail_extreme - bar_atr * self.trail_atr_mult

                    if self.exit_method == self.EXIT_TRAILING:
                        # Pure trailing: SL can only move up (ratchet)
                        stop_price = max(stop_price, new_trail_sl)

                    elif self.exit_method == self.EXIT_BREAKEVEN_TRAIL:
                        if not at_breakeven:
                            # Activate breakeven once price reaches +1R
                            if bar_h >= entry_price + stop_dist_orig:
                                stop_price   = entry_price   # move to breakeven
                                at_breakeven = True
                        else:
                            # Already at breakeven: apply Chandelier trail
                            stop_price = max(stop_price, new_trail_sl)

                elif position == -1:  # short: trail from lowest low
                    trail_extreme = min(trail_extreme, bar_l)
                    new_trail_sl  = trail_extreme + bar_atr * self.trail_atr_mult

                    if self.exit_method == self.EXIT_TRAILING:
                        stop_price = min(stop_price, new_trail_sl)

                    elif self.exit_method == self.EXIT_BREAKEVEN_TRAIL:
                        if not at_breakeven:
                            if bar_l <= entry_price - stop_dist_orig:
                                stop_price   = entry_price
                                at_breakeven = True
                        else:
                            stop_price = min(stop_price, new_trail_sl)

            # ----------------------------------------------------------
            # 1b. Check if existing position exits via SL or TP
            # ----------------------------------------------------------
            if position != 0:
                exit_price  = None
                exit_reason = None

                if position == 1:   # long
                    sl_hit = bar_l <= stop_price
                    tp_hit = (tp_price < 1e18) and (bar_h >= tp_price)
                    if sl_hit and tp_hit:
                        sl_dist = abs(bar_o - stop_price)
                        tp_dist = abs(bar_o - tp_price)
                        exit_price, exit_reason = (
                            (stop_price, "SL") if sl_dist <= tp_dist else (tp_price, "TP")
                        )
                    elif sl_hit:
                        exit_price, exit_reason = stop_price, "SL"
                    elif tp_hit:
                        exit_price, exit_reason = tp_price, "TP"

                elif position == -1:  # short
                    sl_hit = bar_h >= stop_price
                    tp_hit = (tp_price > -1e18) and (bar_l <= tp_price)
                    if sl_hit and tp_hit:
                        sl_dist = abs(bar_o - stop_price)
                        tp_dist = abs(bar_o - tp_price)
                        exit_price, exit_reason = (
                            (stop_price, "SL") if sl_dist <= tp_dist else (tp_price, "TP")
                        )
                    elif sl_hit:
                        exit_price, exit_reason = stop_price, "SL"
                    elif tp_hit:
                        exit_price, exit_reason = tp_price, "TP"

                if exit_price is not None:
                    pnl_abs = position * (exit_price - entry_price) * position_size
                    pnl_pct = pnl_abs / capital
                    capital += pnl_abs

                    trades.append(Trade(
                        entry_bar   = entry_bar,
                        exit_bar    = i,
                        direction   = position,
                        entry_price = entry_price,
                        exit_price  = exit_price,
                        stop_price  = stop_price,
                        tp_price    = tp_price,
                        exit_reason = exit_reason,
                        pnl_pct     = pnl_pct,
                        pnl_abs     = pnl_abs,
                    ))
                    position     = 0
                    at_breakeven = False

            # ----------------------------------------------------------
            # 2. Enter new position if flat and signal is actionable.
            #    Signal from bar T-1 is acted on at bar T open.
            # ----------------------------------------------------------
            if position == 0 and i > 0:
                prev  = df.iloc[i - 1]
                sig   = int(prev["signal"])
                conf  = float(prev["confidence"])
                p_atr = float(prev["atr"]) if float(prev["atr"]) > 0 else 1e-6

                if sig != 0 and conf >= self.min_confidence:
                    entry_price = bar_o + sig * self.spread_pips
                    stop_dist   = p_atr * self.stop_atr_mult
                    tp_dist     = p_atr * self.tp_atr_mult

                    if sig == 1:    # long
                        initial_sl    = entry_price - stop_dist
                        stop_price    = initial_sl
                        trail_extreme = bar_o          # start trailing from entry bar
                        if self.exit_method == self.EXIT_FIXED:
                            tp_price = entry_price + tp_dist
                        else:
                            tp_price = float("inf")    # no hard TP for trailing modes
                    else:           # short
                        initial_sl    = entry_price + stop_dist
                        stop_price    = initial_sl
                        trail_extreme = bar_o
                        if self.exit_method == self.EXIT_FIXED:
                            tp_price = entry_price - tp_dist
                        else:
                            tp_price = float("-inf")

                    risk_amount   = capital * self.risk_pct
                    position_size = risk_amount / stop_dist if stop_dist > 0 else 0.0
                    position      = sig
                    entry_bar     = i
                    at_breakeven  = False

            # ----------------------------------------------------------
            # 3. Mark-to-market equity
            # ----------------------------------------------------------
            if position == 1:
                unrealised = (bar_c - entry_price) * position_size
            elif position == -1:
                unrealised = (entry_price - bar_c) * position_size
            else:
                unrealised = 0.0

            equity_curve.append({
                "datetime": row["datetime"],
                "equity":   capital + unrealised,
            })

        # Close any open position at last bar's close
        if position != 0:
            last       = df.iloc[-1]
            exit_price = float(last["close"])
            pnl_abs    = position * (exit_price - entry_price) * position_size
            pnl_pct    = pnl_abs / capital
            capital    += pnl_abs
            trades.append(Trade(
                entry_bar   = entry_bar,
                exit_bar    = n - 1,
                direction   = position,
                entry_price = entry_price,
                exit_price  = exit_price,
                stop_price  = stop_price,
                tp_price    = tp_price,
                exit_reason = "EOD",
                pnl_pct     = pnl_pct,
                pnl_abs     = pnl_abs,
            ))

        eq_df = pd.DataFrame(equity_curve)
        if not eq_df.empty:
            eq_df["peak"]         = eq_df["equity"].cummax()
            eq_df["drawdown_pct"] = (eq_df["equity"] - eq_df["peak"]) / eq_df["peak"] * 100

        metrics = self._compute_metrics(trades, eq_df)
        return BacktestResults(trades=trades, equity_curve=eq_df, metrics=metrics)

    # ------------------------------------------------------------------
    # Performance metrics
    # ------------------------------------------------------------------

    def _compute_metrics(self, trades: List[Trade], eq_df: pd.DataFrame) -> dict:
        if not trades or eq_df.empty:
            return {"error": "No trades or equity data."}

        equity      = eq_df["equity"]
        bar_returns = equity.pct_change().dropna()

        # ---- Returns --------------------------------------------------
        total_return_pct = (equity.iloc[-1] / self.initial_capital - 1) * 100

        n_bars = len(eq_df)
        years  = n_bars / BARS_PER_YEAR
        if years > 0 and equity.iloc[-1] > 0:
            cagr = ((equity.iloc[-1] / self.initial_capital) ** (1 / years) - 1) * 100
        else:
            cagr = 0.0

        # ---- Risk-adjusted returns ------------------------------------
        mean_r = bar_returns.mean()
        std_r  = bar_returns.std()
        sharpe = (mean_r / std_r * np.sqrt(BARS_PER_YEAR)) if std_r > 0 else 0.0

        downside_r = bar_returns[bar_returns < 0]
        sortino_std = downside_r.std()
        sortino = (mean_r / sortino_std * np.sqrt(BARS_PER_YEAR)) if sortino_std > 0 else 0.0

        # ---- Drawdown -------------------------------------------------
        max_dd_pct = eq_df["drawdown_pct"].min()  # most negative value

        # Drawdown duration (consecutive bars underwater)
        in_dd          = (eq_df["drawdown_pct"] < 0)
        dd_groups      = (in_dd != in_dd.shift()).cumsum()
        dd_durations   = in_dd.groupby(dd_groups).sum()
        max_dd_bars    = int(dd_durations.max()) if len(dd_durations) > 0 else 0

        calmar = (cagr / abs(max_dd_pct)) if max_dd_pct < 0 else float("inf")

        # ---- Trade statistics -----------------------------------------
        n_trades   = len(trades)
        wins       = [t for t in trades if t.pnl_abs > 0]
        losses     = [t for t in trades if t.pnl_abs <= 0]
        win_rate   = len(wins) / n_trades * 100 if n_trades > 0 else 0.0

        gross_profit = sum(t.pnl_abs for t in wins)
        gross_loss   = abs(sum(t.pnl_abs for t in losses))
        profit_factor = gross_profit / gross_loss if gross_loss > 0 else float("inf")

        avg_win  = gross_profit / len(wins)  if wins   else 0.0
        avg_loss = gross_loss   / len(losses) if losses else 0.0
        expectancy = (win_rate / 100 * avg_win) - ((1 - win_rate / 100) * avg_loss)

        tp_exits = sum(1 for t in trades if t.exit_reason == "TP")
        sl_exits = sum(1 for t in trades if t.exit_reason == "SL")

        longs  = [t for t in trades if t.direction ==  1]
        shorts = [t for t in trades if t.direction == -1]

        return {
            "total_return_pct":   round(total_return_pct, 2),
            "cagr_pct":           round(cagr, 2),
            "sharpe":             round(sharpe, 3),
            "sortino":            round(sortino, 3),
            "max_drawdown_pct":   round(max_dd_pct, 2),
            "max_dd_duration_bars": max_dd_bars,
            "calmar":             round(calmar, 3),
            "n_trades":           n_trades,
            "win_rate_pct":       round(win_rate, 1),
            "profit_factor":      round(profit_factor, 3),
            "avg_win":            round(avg_win, 4),
            "avg_loss":           round(avg_loss, 4),
            "expectancy":         round(expectancy, 4),
            "tp_exits":           tp_exits,
            "sl_exits":           sl_exits,
            "long_trades":        len(longs),
            "short_trades":       len(shorts),
            "final_capital":      round(equity.iloc[-1], 2),
        }

    # ------------------------------------------------------------------
    # Reporting
    # ------------------------------------------------------------------

    def print_report(self, results: BacktestResults) -> None:
        m = results.metrics
        if "error" in m:
            print(f"Backtest error: {m['error']}")
            return

        print("\n" + "=" * 60)
        print("  BACKTEST RESULTS")
        print("=" * 60)
        print(f"  Initial capital :  {self.initial_capital:>10,.2f}")
        print(f"  Final capital   :  {m['final_capital']:>10,.2f}")
        print(f"  Total return    :  {m['total_return_pct']:>+9.2f} %")
        print(f"  CAGR            :  {m['cagr_pct']:>+9.2f} %")
        print("-" * 60)
        print(f"  Sharpe ratio    :  {m['sharpe']:>10.3f}")
        print(f"  Sortino ratio   :  {m['sortino']:>10.3f}")
        print(f"  Calmar ratio    :  {m['calmar']:>10.3f}")
        print(f"  Max drawdown    :  {m['max_drawdown_pct']:>+9.2f} %")
        print(f"  Max DD duration :  {m['max_dd_duration_bars']:>7d}  bars")
        print("-" * 60)
        print(f"  Trades          :  {m['n_trades']:>10d}")
        print(f"    Long          :  {m['long_trades']:>10d}")
        print(f"    Short         :  {m['short_trades']:>10d}")
        print(f"    TP exits      :  {m['tp_exits']:>10d}")
        print(f"    SL exits      :  {m['sl_exits']:>10d}")
        print(f"  Win rate        :  {m['win_rate_pct']:>9.1f} %")
        print(f"  Profit factor   :  {m['profit_factor']:>10.3f}")
        print(f"  Avg win         :  {m['avg_win']:>10.4f}")
        print(f"  Avg loss        :  {m['avg_loss']:>10.4f}")
        print(f"  Expectancy      :  {m['expectancy']:>10.4f}")
        print("=" * 60 + "\n")

    def plot_equity(self, results: BacktestResults, save_path: str = None) -> None:
        """Plot equity curve and drawdown.  Requires matplotlib."""
        try:
            import matplotlib.pyplot as plt
        except ImportError:
            logger.warning("matplotlib not available — skipping plot.")
            return

        if results.equity_curve.empty:
            logger.warning("Empty equity curve — nothing to plot.")
            return

        eq    = results.equity_curve
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 8), sharex=True,
                                       gridspec_kw={"height_ratios": [3, 1]})

        ax1.plot(eq["datetime"], eq["equity"], color="steelblue", linewidth=1.2)
        ax1.axhline(self.initial_capital, color="grey", linestyle="--", linewidth=0.8)
        ax1.set_ylabel("Equity")
        ax1.set_title("Backtest Equity Curve")
        ax1.grid(True, alpha=0.3)

        ax2.fill_between(eq["datetime"], eq["drawdown_pct"], 0,
                         color="crimson", alpha=0.4)
        ax2.set_ylabel("Drawdown %")
        ax2.set_xlabel("Date")
        ax2.grid(True, alpha=0.3)

        plt.tight_layout()
        if save_path:
            plt.savefig(save_path, dpi=150, bbox_inches="tight")
            logger.info("Plot saved to %s", save_path)
        else:
            plt.show()


# ------------------------------------------------------------------
# Walk-forward backtest
# ------------------------------------------------------------------

def walk_forward_backtest(
    df_features:    pd.DataFrame,
    price_df:       pd.DataFrame,
    n_splits:       int   = 5,
    train_pct:      float = 0.70,
    backtester:     Backtester = None,
    model_params:   dict  = None,
    binary:         bool  = True,
    embargo:        int   = 12,
    use_regime:     bool  = False,
) -> list:
    """
    Roll a train/test window across the dataset and backtest each fold.

    For each fold:
      1. Train a fresh model on the training portion
      2. Generate signals on the test portion
      3. Run backtest on the test portion
      4. Record metrics

    Returns a list of dicts, one per fold.
    """
    from model import (TradingModel, create_labels, triple_barrier_labels,
                       FEATURE_COLUMNS)  # local import

    if backtester is None:
        backtester = Backtester()

    df = df_features.copy()
    if binary:
        df["label"] = triple_barrier_labels(df)
    else:
        df["label"] = create_labels(df)
    df = df.dropna(subset=["label"] + FEATURE_COLUMNS)

    n = len(df)

    # Expanding-window walk-forward with embargo.
    # Reserve the first `train_pct` fraction as the minimum training set.
    # Split the remaining data into n_splits equal test windows.
    min_train_n  = int(n * train_pct)
    test_n       = n - min_train_n
    fold_size    = test_n // n_splits

    logger.info("Label distribution:\n  BUY (+1): %d\n  SELL (-1): %d%s",
                (df["label"] == 1).sum(), (df["label"] == -1).sum(),
                "" if binary else f"\n  HOLD (0): {(df['label'] == 0).sum()}")

    all_results = []
    for fold in range(n_splits):
        test_start = min_train_n + fold * fold_size
        test_end   = test_start + fold_size
        if test_end > n:
            test_end = n

        # Embargo: skip `embargo` bars before the test window
        train_df = df.iloc[:max(0, test_start - embargo)]
        test_df  = df.iloc[test_start:test_end]

        if len(train_df) < 200 or len(test_df) < 10:
            logger.warning("Fold %d: insufficient data (%d train / %d test) — skipping",
                           fold + 1, len(train_df), len(test_df))
            continue

        logger.info("Fold %d/%d: train=%d  test=%d  [%s → %s]",
                    fold + 1, n_splits, len(train_df), len(test_df),
                    test_df["datetime"].iloc[0].strftime("%Y-%m-%d"),
                    test_df["datetime"].iloc[-1].strftime("%Y-%m-%d"))

        # Train on train_df, using its last 15% for early stopping validation
        params = model_params or {}
        model  = TradingModel(params=params if params else None,
                              binary=binary, embargo=0)

        n_val        = max(int(len(train_df) * 0.15), 50)
        inner_train  = train_df.iloc[:-n_val] if n_val < len(train_df) else train_df
        inner_val    = train_df.iloc[-n_val:] if n_val < len(train_df) else train_df.iloc[:0]

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

        # Generate signals on test_df
        probs  = model.clf.predict_proba(X_te)
        if binary:
            p_buy  = probs[:, 1]
            p_sell = probs[:, 0]
            sigs   = np.where(p_buy >= p_sell, 1, -1).astype(int)
            confs  = np.where(sigs == 1, p_buy, p_sell)
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
        if signals.empty:
            continue

        # HMM regime gating
        if use_regime:
            try:
                from regime import RegimeDetector
                detector = RegimeDetector()
                detector.fit(train_df)
                is_trending = detector.is_trending(test_df)
                is_trending.index = signals.index
                suppressed = (~is_trending).sum()
                signals.loc[~is_trending.values, "signal"] = 0
                logger.info("Regime gating fold %d: suppressed %d/%d signals",
                            fold + 1, suppressed, len(signals))
            except Exception as exc:
                logger.warning("Regime gating failed: %s", exc)

        # Align price data with test window dates — normalise to tz-naive
        def _tz_naive_series(s: pd.Series) -> pd.Series:
            if hasattr(s.dt, "tz") and s.dt.tz is not None:
                return s.dt.tz_convert("UTC").dt.tz_localize(None)
            return pd.to_datetime(s)

        test_dt_naive  = _tz_naive_series(test_df["datetime"])
        price_dt_naive = _tz_naive_series(price_df["datetime"])
        test_dates     = set(test_dt_naive)
        price_test     = price_df[price_dt_naive.isin(test_dates)].copy()

        result = backtester.run(price_test if not price_test.empty else test_df, signals)
        m      = result.metrics.copy()
        m["fold"]       = fold + 1
        m["train_bars"] = len(train_df)
        m["test_bars"]  = len(test_df)
        m["test_start"] = str(test_df["datetime"].iloc[0].date())
        m["test_end"]   = str(test_df["datetime"].iloc[-1].date())
        all_results.append(m)

        backtester.print_report(result)

    if all_results:
        valid = [r for r in all_results if "error" not in r and r.get("n_trades", 0) > 0]
        print("\n" + "=" * 60)
        print("  WALK-FORWARD SUMMARY")
        print("=" * 60)
        if valid:
            metrics_to_avg = ["total_return_pct", "sharpe", "win_rate_pct",
                              "profit_factor", "max_drawdown_pct", "calmar"]
            for k in metrics_to_avg:
                vals = [r[k] for r in valid if k in r]
                if vals:
                    print(f"  {k:<22s}:  avg={np.mean(vals):>7.3f}  "
                          f"min={np.min(vals):>7.3f}  max={np.max(vals):>7.3f}")
        else:
            print("  No folds produced trades — try lowering --confidence")
        print("=" * 60 + "\n")

    return all_results
