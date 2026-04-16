"""
model.py
--------
Trains an XGBoost classifier to predict directional moves using the features
from features.py.

Key design decisions:
  - Walk-forward validation (no look-ahead bias)
  - 3-class labels: BUY (+1), SELL (-1), HOLD (0)
  - Optional Optuna hyperparameter optimisation
  - generate_test_signals() exports predictions on the out-of-sample test set
    for use by the backtester

Usage (train):
    python model.py
    python model.py --optimize        # run Optuna HPO first

Usage (programmatic):
    from model import TradingModel, optimize_hyperparams
    model = TradingModel()
    model.train(df_features)
    model.save()
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

LOOKAHEAD_BARS         = 4      # bars ahead to predict (4 × 15 min = 1 hour)
ATR_THRESHOLD_MULTIPLIER = 0.5  # price must move > ATR×this to be labelled BUY/SELL

TRAIN_RATIO = 0.70
VAL_RATIO   = 0.15   # remaining 0.15 = out-of-sample test

MODEL_PATH = os.path.join(os.path.dirname(__file__), "data", "xgb_model.pkl")

# Default XGBoost hyperparameters
XGB_PARAMS = {
    "n_estimators":     300,
    "max_depth":        4,
    "learning_rate":    0.05,
    "subsample":        0.8,
    "colsample_bytree": 0.8,
    "min_child_weight": 5,
    "eval_metric":      "mlogloss",
    "random_state":     42,
    "n_jobs":           -1,
}


# ------------------------------------------------------------------
# Label creation
# ------------------------------------------------------------------

def create_labels(df: pd.DataFrame,
                  lookahead: int = LOOKAHEAD_BARS,
                  atr_multiplier: float = ATR_THRESHOLD_MULTIPLIER) -> pd.Series:
    """
    Classify each bar as BUY (+1), SELL (-1), or HOLD (0) based on
    how far the price moves over the next `lookahead` bars relative to ATR.
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
# Walk-forward split
# ------------------------------------------------------------------

def walk_forward_split(df: pd.DataFrame,
                       train_ratio: float = TRAIN_RATIO,
                       val_ratio: float   = VAL_RATIO):
    """
    Chronological train / validation / test split. No shuffling.
    """
    n       = len(df)
    n_train = int(n * train_ratio)
    n_val   = int(n * val_ratio)
    train   = df.iloc[:n_train]
    val     = df.iloc[n_train: n_train + n_val]
    test    = df.iloc[n_train + n_val:]
    logger.info("Walk-forward split: train=%d  val=%d  test=%d",
                len(train), len(val), len(test))
    return train, val, test


# ------------------------------------------------------------------
# Optuna hyperparameter optimisation
# ------------------------------------------------------------------

def optimize_hyperparams(df_features: pd.DataFrame,
                         n_trials: int = 50) -> dict:
    """
    Use Optuna to search for better XGBoost hyperparameters.
    Returns the best parameter dict (ready to pass to XGBClassifier).

    Requires:  pip install optuna
    """
    try:
        import optuna
        optuna.logging.set_verbosity(optuna.logging.WARNING)
    except ImportError:
        logger.warning("optuna not installed — skipping HPO. Run: pip install optuna")
        return XGB_PARAMS.copy()

    df = df_features.copy()
    df["label"] = create_labels(df)
    df = df.dropna(subset=["label"] + FEATURE_COLUMNS)

    train_df, val_df, _ = walk_forward_split(df)

    X_train = train_df[FEATURE_COLUMNS].values
    X_val   = val_df[FEATURE_COLUMNS].values

    # Encode labels: XGBoost needs 0-based integers
    enc = LabelEncoder()
    enc.fit(np.concatenate([train_df["label"].astype(int).values,
                            val_df["label"].astype(int).values]))
    y_train = enc.transform(train_df["label"].astype(int).values)
    y_val   = enc.transform(val_df["label"].astype(int).values)

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
            "eval_metric":      "mlogloss",
            "random_state":     42,
            "n_jobs":           -1,
        }
        clf = XGBClassifier(**params)
        clf.fit(
            X_train, y_train,
            eval_set=[(X_val, y_val)],
            verbose=False,
            early_stopping_rounds=20,
        )
        # Return best validation loss
        return clf.best_score

    logger.info("Running Optuna with %d trials...", n_trials)
    study = optuna.create_study(direction="minimize")
    study.optimize(objective, n_trials=n_trials, show_progress_bar=True)

    best = study.best_params
    best["eval_metric"] = "mlogloss"
    best["random_state"] = 42
    best["n_jobs"]       = -1
    logger.info("Best params: %s  (val loss=%.4f)", best, study.best_value)
    return best


# ------------------------------------------------------------------
# TradingModel
# ------------------------------------------------------------------

class TradingModel:
    """
    Wraps an XGBClassifier with label encoding and convenience methods
    for prediction, signal generation, and persistence.
    """

    def __init__(self, params: dict = None):
        self.params  = params or XGB_PARAMS.copy()
        self.clf     = XGBClassifier(**self.params)
        self.encoder = LabelEncoder()
        self.trained = False
        # Store the test split for generate_test_signals
        self._test_df: pd.DataFrame = None

    # ------------------------------------------------------------------
    # Training
    # ------------------------------------------------------------------

    def train(self, df_features: pd.DataFrame) -> dict:
        """
        Train using walk-forward splits. Returns classification reports.
        """
        df = df_features.copy()
        df["label"] = create_labels(df)
        df = df.dropna(subset=["label"] + FEATURE_COLUMNS)

        train_df, val_df, test_df = walk_forward_split(df)
        self._test_df = test_df  # save for generate_test_signals

        X_train = train_df[FEATURE_COLUMNS].values
        y_train = train_df["label"].astype(int).values
        X_val   = val_df[FEATURE_COLUMNS].values
        y_val   = val_df["label"].astype(int).values
        X_test  = test_df[FEATURE_COLUMNS].values
        y_test  = test_df["label"].astype(int).values

        all_labels = np.concatenate([y_train, y_val, y_test])
        self.encoder.fit(all_labels)

        y_train_enc = self.encoder.transform(y_train)
        y_val_enc   = self.encoder.transform(y_val)

        logger.info("Training XGBoost on %d samples (%d features)...",
                    len(X_train), len(FEATURE_COLUMNS))

        self.clf.fit(
            X_train, y_train_enc,
            eval_set=[(X_val, y_val_enc)],
            verbose=50,
            early_stopping_rounds=30,
        )
        self.trained = True

        reports = {}
        for name, X, y_raw in [("train", X_train, y_train),
                                ("val",   X_val,   y_val),
                                ("test",  X_test,  y_test)]:
            preds     = self.encoder.inverse_transform(self.clf.predict(X))
            report    = classification_report(y_raw, preds,
                                              target_names=["SELL", "HOLD", "BUY"],
                                              output_dict=True, zero_division=0)
            reports[name] = report
            logger.info("\n%s set:\n%s", name.upper(),
                        classification_report(y_raw, preds,
                                              target_names=["SELL", "HOLD", "BUY"],
                                              zero_division=0))

        importance = pd.Series(
            self.clf.feature_importances_, index=FEATURE_COLUMNS
        ).sort_values(ascending=False)
        logger.info("\nTop 15 features:\n%s", importance.head(15).to_string())

        return reports

    # ------------------------------------------------------------------
    # Test-set signal generation (for backtesting)
    # ------------------------------------------------------------------

    def generate_test_signals(self, df_features: pd.DataFrame = None) -> pd.DataFrame:
        """
        Return a DataFrame of model predictions on the out-of-sample test set.

        Columns: datetime, close, atr, signal, confidence, true_label

        If df_features is provided, the test split is recomputed from it.
        Otherwise the cached split from the last train() call is used.
        """
        if not self.trained:
            raise RuntimeError("Model must be trained before generating signals.")

        if df_features is not None:
            df = df_features.copy()
            df["label"] = create_labels(df)
            df = df.dropna(subset=["label"] + FEATURE_COLUMNS)
            _, _, test_df = walk_forward_split(df)
        else:
            if self._test_df is None:
                raise RuntimeError("No cached test set — pass df_features explicitly.")
            test_df = self._test_df

        X_test = test_df[FEATURE_COLUMNS].values
        probs  = self.clf.predict_proba(X_test)          # (N, 3)

        class_enc   = np.argmax(probs, axis=1)
        signals     = self.encoder.inverse_transform(class_enc).astype(int)
        confidence  = probs[np.arange(len(probs)), class_enc]

        result = pd.DataFrame({
            "datetime":   test_df["datetime"].values,
            "close":      test_df["close"].values,
            "atr":        test_df["atr"].values,
            "signal":     signals,
            "confidence": confidence,
        })

        if "label" in test_df.columns:
            result["true_label"] = test_df["label"].astype(int).values

        logger.info("Generated %d test-set signals  (BUY: %d, SELL: %d, HOLD: %d)",
                    len(result),
                    (result["signal"] == 1).sum(),
                    (result["signal"] == -1).sum(),
                    (result["signal"] == 0).sum())
        return result

    # ------------------------------------------------------------------
    # Live prediction
    # ------------------------------------------------------------------

    def predict_latest(self, df_features: pd.DataFrame) -> tuple:
        if not self.trained:
            raise RuntimeError("Model has not been trained yet.")
        row       = df_features[FEATURE_COLUMNS].dropna().iloc[[-1]]
        probs     = self.clf.predict_proba(row)[0]
        class_enc = np.argmax(probs)
        signal    = int(self.encoder.inverse_transform([class_enc])[0])
        prob      = float(probs[class_enc])
        label     = {1: "BUY", -1: "SELL", 0: "HOLD"}.get(signal, "UNKNOWN")
        logger.info("Signal: %s  (confidence: %.1f%%)", label, prob * 100)
        return signal, prob

    def predict_proba_latest(self, df_features: pd.DataFrame) -> dict:
        row    = df_features[FEATURE_COLUMNS].dropna().iloc[[-1]]
        probs  = self.clf.predict_proba(row)[0]
        classes = self.encoder.inverse_transform([0, 1, 2])
        return dict(zip([int(c) for c in classes], probs.tolist()))

    # ------------------------------------------------------------------
    # Persistence
    # ------------------------------------------------------------------

    def save(self, path: str = MODEL_PATH):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        joblib.dump({"clf": self.clf, "encoder": self.encoder, "params": self.params}, path)
        logger.info("Model saved to %s", path)

    @classmethod
    def load(cls, path: str = MODEL_PATH) -> "TradingModel":
        if not os.path.exists(path):
            raise FileNotFoundError(
                f"Model file not found: {path}\nRun model.py to train first."
            )
        obj = joblib.load(path)
        m         = cls(params=obj.get("params", XGB_PARAMS))
        m.clf     = obj["clf"]
        m.encoder = obj["encoder"]
        m.trained = True
        logger.info("Model loaded from %s", path)
        return m


# ------------------------------------------------------------------
# Entry point
# ------------------------------------------------------------------

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s [%(levelname)s] %(message)s")

    parser = argparse.ArgumentParser(description="Train the XGBoost trading model")
    parser.add_argument("--optimize", action="store_true",
                        help="Run Optuna HPO before training (requires optuna package)")
    parser.add_argument("--trials", type=int, default=50,
                        help="Number of Optuna trials (default: 50)")
    args = parser.parse_args()

    logger.info("Loading price data...")
    df_raw = load_data()

    logger.info("Computing features...")
    df_feat = compute_features(df_raw)

    params = XGB_PARAMS
    if args.optimize:
        logger.info("Running hyperparameter optimisation (%d trials)...", args.trials)
        params = optimize_hyperparams(df_feat, n_trials=args.trials)

    logger.info("Training model...")
    model   = TradingModel(params=params)
    reports = model.train(df_feat)
    model.save()

    # Quick sanity check
    signal, prob = model.predict_latest(df_feat)
    label = {1: "BUY", -1: "SELL", 0: "HOLD"}.get(signal, "UNKNOWN")
    print(f"\nLatest signal: {label}  (confidence: {prob:.1%})")
    print(f"\nTest-set accuracy: {reports['test']['accuracy']:.3f}")
