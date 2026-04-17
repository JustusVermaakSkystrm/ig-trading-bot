"""
model.py
--------
Trains an XGBoost classifier to predict directional moves using the features
from features.py.

Labeling modes
--------------
  triple_barrier (default)
    For each bar find which barrier fires first within `max_bars`:
      +1  = price touches TP (+tp_mult × ATR)
      -1  = price touches SL (-sl_mult × ATR)
      NaN = neither fires within max_bars (time-expired — DROPPED, not HOLD)
    Model is a BINARY classifier (BUY vs SELL); time-expired bars are excluded.

  fixed_horizon
    Classic 3-class: BUY/SELL/HOLD based on close-to-close over lookahead bars.
    Retained for comparison; not recommended for live use.

Walk-forward split
------------------
  Supports a `embargo_bars` gap between train and test to prevent label leakage
  (the label for bar t uses future prices up to t+max_bars, so those bars must
  not appear in the training set for bar t).

Usage (train):
    python model.py
    python model.py --optimize

Usage (programmatic):
    from model import TradingModel, create_labels, triple_barrier_labels
    model = TradingModel(binary=True)
    model.train(df_features)
    signals_df = model.generate_test_signals(df_features)
"""

import argparse
import logging
import os

import joblib
import numpy as np
import pandas as pd
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBClassifier

from features import FEATURE_COLUMNS, compute_features
from data_pipeline import load_data

logger = logging.getLogger(__name__)

# ------------------------------------------------------------------
# Configuration
# ------------------------------------------------------------------

# Triple-barrier defaults
TB_TP_MULT  = 1.5   # take-profit barrier: TP_MULT × ATR above entry
TB_SL_MULT  = 1.5   # stop-loss barrier:   SL_MULT × ATR below entry
TB_MAX_BARS = 12    # time horizon (12 × 15 min = 3 hours)

# Fixed-horizon fallback (legacy)
LOOKAHEAD_BARS           = 4
ATR_THRESHOLD_MULTIPLIER = 0.5

TRAIN_RATIO = 0.70
VAL_RATIO   = 0.15   # remaining 0.15 = out-of-sample test

MODEL_PATH = os.path.join(os.path.dirname(__file__), "data", "xgb_model.pkl")

# Default XGBoost hyperparameters (binary mode uses binary:logistic automatically)
XGB_PARAMS = {
    "n_estimators":     300,
    "max_depth":        4,
    "learning_rate":    0.05,
    "subsample":        0.8,
    "colsample_bytree": 0.8,
    "min_child_weight": 5,
    "random_state":     42,
    "n_jobs":           -1,
}


# ------------------------------------------------------------------
# Labeling: Triple Barrier Method
# ------------------------------------------------------------------

def triple_barrier_labels(
    df: pd.DataFrame,
    tp_mult:  float = TB_TP_MULT,
    sl_mult:  float = TB_SL_MULT,
    max_bars: int   = TB_MAX_BARS,
) -> pd.Series:
    """
    Triple Barrier Method (López de Prado, 2018).

    For each bar i:
      - Upper barrier: entry_price + tp_mult × ATR(i)
      - Lower barrier: entry_price - sl_mult × ATR(i)
      - Time barrier: i + max_bars

    Check intrabar using high/low — same convention as the backtester.
    If both barriers are touched on the same bar, SL wins (conservative).

    Returns pd.Series with +1 / -1 / NaN (NaN = time-expired).
    NaN rows should be *dropped*, not labeled as HOLD.
    """
    close  = df["close"].values
    high   = df["high"].values
    low    = df["low"].values
    atrs   = df["atr"].values
    n      = len(close)
    labels = np.full(n, np.nan)

    for i in range(n - 1):
        entry = close[i]
        atr_i = atrs[i]
        if np.isnan(atr_i) or atr_i <= 0:
            continue
        tp = entry + tp_mult * atr_i
        sl = entry - sl_mult * atr_i

        end = min(i + max_bars + 1, n)
        for j in range(i + 1, end):
            tp_hit = high[j] >= tp
            sl_hit = low[j]  <= sl
            if sl_hit:          # SL wins when both hit
                labels[i] = -1.0
                break
            elif tp_hit:
                labels[i] = 1.0
                break
            # else: continue looking

    series = pd.Series(labels, index=df.index, name="label")
    n_buy  = (series ==  1).sum()
    n_sell = (series == -1).sum()
    n_exp  = series.isna().sum()
    logger.info(
        "Triple Barrier labels — BUY: %d  SELL: %d  time-expired(dropped): %d",
        n_buy, n_sell, n_exp,
    )
    return series


# ------------------------------------------------------------------
# Labeling: Fixed-horizon (legacy 3-class)
# ------------------------------------------------------------------

def create_labels(
    df: pd.DataFrame,
    lookahead:      int   = LOOKAHEAD_BARS,
    atr_multiplier: float = ATR_THRESHOLD_MULTIPLIER,
) -> pd.Series:
    """
    Legacy 3-class labeling: BUY (+1) / SELL (-1) / HOLD (0).
    Kept for backward compatibility and comparison.
    """
    future_close = df["close"].shift(-lookahead)
    threshold    = df["atr"] * atr_multiplier

    labels = pd.Series(0, index=df.index, name="label")
    labels[future_close > df["close"] + threshold] =  1
    labels[future_close < df["close"] - threshold] = -1
    labels.iloc[-lookahead:] = np.nan

    counts = labels.dropna().value_counts()
    logger.info("Label distribution:\n  BUY (+1): %d\n  HOLD (0): %d\n  SELL (-1): %d",
                counts.get(1, 0), counts.get(0, 0), counts.get(-1, 0))
    return labels


# ------------------------------------------------------------------
# Walk-forward split (with optional embargo)
# ------------------------------------------------------------------

def walk_forward_split(
    df:            pd.DataFrame,
    train_ratio:   float = TRAIN_RATIO,
    val_ratio:     float = VAL_RATIO,
    embargo_bars:  int   = 0,
):
    """
    Chronological train / validation / test split.

    embargo_bars: number of rows dropped between train/val and val/test
    boundaries to prevent label leakage (should equal max_bars for TB labels).
    """
    n       = len(df)
    n_train = int(n * train_ratio)
    n_val   = int(n * val_ratio)

    train = df.iloc[:n_train]
    val   = df.iloc[n_train + embargo_bars : n_train + embargo_bars + n_val]
    test  = df.iloc[n_train + embargo_bars + n_val + embargo_bars:]

    logger.info("Walk-forward split: train=%d  val=%d  test=%d  (embargo=%d)",
                len(train), len(val), len(test), embargo_bars)
    return train, val, test


# ------------------------------------------------------------------
# Optuna hyperparameter optimisation
# ------------------------------------------------------------------

def optimize_hyperparams(
    df_features: pd.DataFrame,
    n_trials:    int  = 50,
    binary:      bool = True,
    embargo:     int  = TB_MAX_BARS,
) -> dict:
    """
    Use Optuna to search for better XGBoost hyperparameters.
    Returns the best parameter dict ready to pass to TradingModel.
    """
    try:
        import optuna
        optuna.logging.set_verbosity(optuna.logging.WARNING)
    except ImportError:
        logger.warning("optuna not installed — skipping HPO. Run: pip install optuna")
        return XGB_PARAMS.copy()

    df = df_features.copy()
    if binary:
        df["label"] = triple_barrier_labels(df)
    else:
        df["label"] = create_labels(df)
    df = df.dropna(subset=["label"] + FEATURE_COLUMNS)

    train_df, val_df, _ = walk_forward_split(df, embargo_bars=embargo)

    X_train = train_df[FEATURE_COLUMNS].values
    X_val   = val_df[FEATURE_COLUMNS].values

    if binary:
        # Map +1 → 1, -1 → 0
        y_train = ((train_df["label"].astype(int) + 1) // 2).values
        y_val   = ((val_df["label"].astype(int)   + 1) // 2).values
        metric  = "logloss"
        obj     = "binary:logistic"
    else:
        enc = LabelEncoder()
        enc.fit(np.concatenate([train_df["label"].astype(int).values,
                                val_df["label"].astype(int).values]))
        y_train = enc.transform(train_df["label"].astype(int).values)
        y_val   = enc.transform(val_df["label"].astype(int).values)
        metric  = "mlogloss"
        obj     = "multi:softmax"

    def objective(trial):
        params = {
            "n_estimators":     trial.suggest_int("n_estimators", 100, 600),
            "max_depth":        trial.suggest_int("max_depth", 3, 7),
            "learning_rate":    trial.suggest_float("learning_rate", 0.01, 0.2, log=True),
            "subsample":        trial.suggest_float("subsample", 0.5, 1.0),
            "colsample_bytree": trial.suggest_float("colsample_bytree", 0.4, 1.0),
            "min_child_weight": trial.suggest_int("min_child_weight", 1, 20),
            "gamma":            trial.suggest_float("gamma", 0.0, 5.0),
            "reg_alpha":        trial.suggest_float("reg_alpha", 0.0, 2.0),
            "reg_lambda":       trial.suggest_float("reg_lambda", 0.5, 4.0),
            "eval_metric":      metric,
            "objective":        obj,
            "random_state":     42,
            "n_jobs":           -1,
        }
        clf = XGBClassifier(**params, early_stopping_rounds=20)
        clf.fit(X_train, y_train, eval_set=[(X_val, y_val)], verbose=False)
        return clf.best_score

    logger.info("Running Optuna with %d trials...", n_trials)
    study = optuna.create_study(direction="minimize")
    study.optimize(objective, n_trials=n_trials, show_progress_bar=True)

    best = study.best_params
    best["random_state"] = 42
    best["n_jobs"]       = -1
    logger.info("Best params: %s  (val loss=%.4f)", best, study.best_value)
    return best


# ------------------------------------------------------------------
# TradingModel
# ------------------------------------------------------------------

class TradingModel:
    """
    Wraps an XGBClassifier with binary or 3-class operation.

    binary=True  (default, recommended)
        Uses Triple Barrier labels (+1/−1 only).
        XGBoost objective: binary:logistic.
        predict_proba returns P(BUY); signal is BUY if P>thresh, SELL if P<1-thresh.

    binary=False  (legacy)
        Uses fixed-horizon 3-class labels (BUY/SELL/HOLD).
        XGBoost objective: multi:softmax.
    """

    def __init__(
        self,
        params:  dict = None,
        binary:  bool = True,
        embargo: int  = TB_MAX_BARS,
    ):
        self.binary  = binary
        self.embargo = embargo
        self.params  = (params or XGB_PARAMS).copy()

        # Inject the correct objective & metric based on mode
        if binary:
            self.params.setdefault("objective",   "binary:logistic")
            self.params.setdefault("eval_metric", "logloss")
        else:
            self.params.setdefault("objective",   "multi:softmax")
            self.params.setdefault("eval_metric", "mlogloss")

        init_params = {k: v for k, v in self.params.items()
                       if k not in ("early_stopping_rounds",)}
        self.clf     = XGBClassifier(**init_params)
        self.encoder = LabelEncoder()   # only used in multi-class mode
        self.trained = False
        self._test_df: pd.DataFrame = None

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _encode_labels(self, labels_int: np.ndarray) -> np.ndarray:
        """Convert raw int labels to XGBoost target format."""
        if self.binary:
            # +1 → 1,  -1 → 0
            return ((labels_int + 1) // 2).astype(int)
        return self.encoder.transform(labels_int)

    def _decode_labels(self, encoded: np.ndarray) -> np.ndarray:
        """Convert XGBoost output back to +1/−1 (binary) or original classes."""
        if self.binary:
            return np.where(encoded == 1, 1, -1).astype(int)
        return self.encoder.inverse_transform(encoded).astype(int)

    def _prepare_data(self, df: pd.DataFrame):
        """Apply labeling and drop invalid rows. Returns clean df."""
        df = df.copy()
        if self.binary:
            df["label"] = triple_barrier_labels(df)
        else:
            df["label"] = create_labels(df)
        return df.dropna(subset=["label"] + FEATURE_COLUMNS)

    # ------------------------------------------------------------------
    # Training
    # ------------------------------------------------------------------

    def train(self, df_features: pd.DataFrame) -> dict:
        """Train using walk-forward splits. Returns classification reports."""
        df = self._prepare_data(df_features)
        train_df, val_df, test_df = walk_forward_split(df, embargo_bars=self.embargo)
        self._test_df = test_df

        X_train = train_df[FEATURE_COLUMNS].values
        y_train = train_df["label"].astype(int).values
        X_val   = val_df[FEATURE_COLUMNS].values
        y_val   = val_df["label"].astype(int).values
        X_test  = test_df[FEATURE_COLUMNS].values
        y_test  = test_df["label"].astype(int).values

        # Fit encoder (multi-class only; still harmless in binary mode)
        all_labels = np.concatenate([y_train, y_val, y_test])
        self.encoder.fit(all_labels)

        y_train_enc = self._encode_labels(y_train)
        y_val_enc   = self._encode_labels(y_val)

        logger.info("Training XGBoost (%s) on %d samples (%d features)...",
                    "binary" if self.binary else "3-class",
                    len(X_train), len(FEATURE_COLUMNS))

        use_early_stop = len(X_val) >= 50
        if use_early_stop:
            self.clf.set_params(early_stopping_rounds=30)
            self.clf.fit(X_train, y_train_enc,
                         eval_set=[(X_val, y_val_enc)], verbose=False)
        else:
            self.clf.fit(X_train, y_train_enc, verbose=False)
        self.trained = True

        # Reports
        reports = {}
        tgt_names = ["SELL", "BUY"] if self.binary else ["SELL", "HOLD", "BUY"]
        for name, X, y_raw in [("train", X_train, y_train),
                                ("val",   X_val,   y_val),
                                ("test",  X_test,  y_test)]:
            enc_pred = self.clf.predict(X)
            preds    = self._decode_labels(enc_pred)
            report   = classification_report(y_raw, preds,
                                             labels=[-1, 1] if self.binary else [-1, 0, 1],
                                             target_names=tgt_names,
                                             output_dict=True, zero_division=0)
            reports[name] = report
            logger.info("\n%s set:\n%s", name.upper(),
                        classification_report(y_raw, preds,
                                              labels=[-1, 1] if self.binary else [-1, 0, 1],
                                              target_names=tgt_names,
                                              zero_division=0))

        importance = pd.Series(
            self.clf.feature_importances_, index=FEATURE_COLUMNS
        ).sort_values(ascending=False)
        logger.info("\nTop 15 features:\n%s", importance.head(15).to_string())

        return reports

    # ------------------------------------------------------------------
    # Signal generation (for backtesting)
    # ------------------------------------------------------------------

    def generate_test_signals(self, df_features: pd.DataFrame = None) -> pd.DataFrame:
        """
        Return model predictions on the out-of-sample test set.

        Columns: datetime, close, atr, signal, confidence, true_label
          signal:     +1 (BUY) / -1 (SELL) / 0 (HOLD — below confidence threshold)
          confidence: P(predicted class); for binary = P(BUY) if BUY, else P(SELL)
        """
        if not self.trained:
            raise RuntimeError("Model must be trained before generating signals.")

        if df_features is not None:
            df = self._prepare_data(df_features)
            _, _, test_df = walk_forward_split(df, embargo_bars=self.embargo)
        else:
            if self._test_df is None:
                raise RuntimeError("No cached test set — pass df_features.")
            test_df = self._test_df

        X_test = test_df[FEATURE_COLUMNS].values
        probs  = self.clf.predict_proba(X_test)   # (N,2) binary or (N,3) multi

        if self.binary:
            # probs[:,0] = P(SELL), probs[:,1] = P(BUY)
            p_buy    = probs[:, 1]
            p_sell   = probs[:, 0]
            # Signal = direction of higher probability (raw, before confidence filter)
            signals  = np.where(p_buy >= p_sell, 1, -1).astype(int)
            # Confidence = probability of the predicted class
            confidence = np.where(signals == 1, p_buy, p_sell)
        else:
            class_enc  = np.argmax(probs, axis=1)
            signals    = self.encoder.inverse_transform(class_enc).astype(int)
            confidence = probs[np.arange(len(probs)), class_enc]

        result = pd.DataFrame({
            "datetime":   test_df["datetime"].values,
            "close":      test_df["close"].values,
            "atr":        test_df["atr"].values,
            "signal":     signals,
            "confidence": confidence,
        })
        if "label" in test_df.columns:
            result["true_label"] = test_df["label"].astype(int).values

        logger.info("Generated %d test-set signals  (BUY: %d, SELL: %d)",
                    len(result),
                    (result["signal"] == 1).sum(),
                    (result["signal"] == -1).sum())
        return result

    # ------------------------------------------------------------------
    # Live prediction
    # ------------------------------------------------------------------

    def predict_latest(self, df_features: pd.DataFrame) -> tuple:
        if not self.trained:
            raise RuntimeError("Model has not been trained yet.")
        row   = df_features[FEATURE_COLUMNS].dropna().iloc[[-1]]
        probs = self.clf.predict_proba(row)[0]

        if self.binary:
            p_buy  = float(probs[1])
            p_sell = float(probs[0])
            signal = 1 if p_buy >= p_sell else -1
            prob   = p_buy if signal == 1 else p_sell
        else:
            class_enc = int(np.argmax(probs))
            signal    = int(self.encoder.inverse_transform([class_enc])[0])
            prob      = float(probs[class_enc])

        label = {1: "BUY", -1: "SELL", 0: "HOLD"}.get(signal, "UNKNOWN")
        logger.info("Signal: %s  (confidence: %.1f%%)", label, prob * 100)
        return signal, prob

    def predict_proba_latest(self, df_features: pd.DataFrame) -> dict:
        row   = df_features[FEATURE_COLUMNS].dropna().iloc[[-1]]
        probs = self.clf.predict_proba(row)[0]
        if self.binary:
            return {1: float(probs[1]), -1: float(probs[0])}
        classes = self.encoder.inverse_transform([0, 1, 2])
        return dict(zip([int(c) for c in classes], probs.tolist()))

    # ------------------------------------------------------------------
    # Persistence
    # ------------------------------------------------------------------

    def save(self, path: str = MODEL_PATH):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        joblib.dump({
            "clf":     self.clf,
            "encoder": self.encoder,
            "params":  self.params,
            "binary":  self.binary,
            "embargo": self.embargo,
        }, path)
        logger.info("Model saved to %s", path)

    @classmethod
    def load(cls, path: str = MODEL_PATH) -> "TradingModel":
        if not os.path.exists(path):
            raise FileNotFoundError(f"Model not found: {path}")
        obj = joblib.load(path)
        m          = cls(params=obj.get("params"), binary=obj.get("binary", True),
                         embargo=obj.get("embargo", TB_MAX_BARS))
        m.clf      = obj["clf"]
        m.encoder  = obj["encoder"]
        m.trained  = True
        logger.info("Model loaded from %s", path)
        return m


# ------------------------------------------------------------------
# Entry point
# ------------------------------------------------------------------

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s [%(levelname)s] %(message)s")

    parser = argparse.ArgumentParser(description="Train the XGBoost trading model")
    parser.add_argument("--optimize",   action="store_true",
                        help="Run Optuna HPO before training")
    parser.add_argument("--trials",     type=int, default=50)
    parser.add_argument("--no-binary",  action="store_true",
                        help="Use legacy 3-class labels instead of Triple Barrier")
    args = parser.parse_args()

    binary = not args.no_binary

    logger.info("Loading price data...")
    df_raw  = load_data()
    logger.info("Computing features...")
    df_feat = compute_features(df_raw)

    params = XGB_PARAMS.copy()
    if args.optimize:
        logger.info("Running HPO (%d trials)...", args.trials)
        params = optimize_hyperparams(df_feat, n_trials=args.trials, binary=binary)

    logger.info("Training model (binary=%s)...", binary)
    model   = TradingModel(params=params, binary=binary)
    reports = model.train(df_feat)
    model.save()

    signal, prob = model.predict_latest(df_feat)
    label = {1: "BUY", -1: "SELL", 0: "HOLD"}.get(signal, "UNKNOWN")
    print(f"\nLatest signal: {label}  (confidence: {prob:.1%})")
    print(f"\nTest-set accuracy: {reports['test']['accuracy']:.3f}")
