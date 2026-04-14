"""
model.py
--------
Trains an XGBoost classifier to predict the direction of the next
candle move (up / down / flat) using the features from features.py.

Key design decisions:
  - Walk-forward validation (avoids look-ahead bias / overfitting)
  - 3-class labels: BUY (1), SELL (-1), HOLD (0)
  - Label is based on price change over the next N bars vs ATR threshold
  - Feature importance printed after training

Usage (train):
    python model.py

Usage (programmatic):
    from model import TradingModel
    model = TradingModel()
    model.train(df_features)          # df_features from features.compute_features()
    model.save()

    # Later / in signal engine:
    model = TradingModel.load()
    signal, probability = model.predict_latest(df_features)
"""

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

# How many bars ahead to predict (4 bars × 15 min = 1 hour ahead)
LOOKAHEAD_BARS = 4

# Signal threshold as a multiple of ATR
# e.g. if ATR = 0.0010, threshold = 0.0010 * 0.5 = 0.0005 (0.5 pip)
ATR_THRESHOLD_MULTIPLIER = 0.5

# Walk-forward: train on this fraction of data, test on remainder
TRAIN_RATIO = 0.70
VAL_RATIO   = 0.15   # validation (used for early stopping)
# remaining (0.15) is the out-of-sample test set

MODEL_PATH = os.path.join(os.path.dirname(__file__), "data", "xgb_model.pkl")

# XGBoost hyperparameters (good starting point — tune later)
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
    For each bar, look `lookahead` bars into the future and classify:
        +1  (BUY)  if future_close > current_close + threshold
        -1  (SELL) if future_close < current_close - threshold
         0  (HOLD) otherwise

    threshold = ATR × atr_multiplier

    We use ATR as the threshold so the signal adapts to volatility —
    in a volatile session, price needs to move more to count as a real signal.
    """
    future_close = df["close"].shift(-lookahead)
    threshold    = df["atr"] * atr_multiplier

    labels = pd.Series(0, index=df.index, name="label")
    labels[future_close > df["close"] + threshold] =  1
    labels[future_close < df["close"] - threshold] = -1

    # The last `lookahead` rows have no valid label — drop them
    labels.iloc[-lookahead:] = np.nan

    counts = labels.dropna().value_counts()
    logger.info("Label distribution:\n  BUY (+1): %d\n  HOLD (0): %d\n  SELL (-1): %d",
                counts.get(1, 0), counts.get(0, 0), counts.get(-1, 0))

    return labels


# ------------------------------------------------------------------
# Walk-forward split
# ------------------------------------------------------------------

def walk_forward_split(df: pd.DataFrame, train_ratio: float = TRAIN_RATIO,
                       val_ratio: float = VAL_RATIO):
    """
    Split data chronologically into train / validation / test sets.
    Never shuffle — that would introduce look-ahead bias.
    """
    n       = len(df)
    n_train = int(n * train_ratio)
    n_val   = int(n * val_ratio)

    train = df.iloc[:n_train]
    val   = df.iloc[n_train: n_train + n_val]
    test  = df.iloc[n_train + n_val:]

    logger.info("Walk-forward split: train=%d  val=%d  test=%d", len(train), len(val), len(test))
    return train, val, test


# ------------------------------------------------------------------
# TradingModel class
# ------------------------------------------------------------------

class TradingModel:
    """
    Wraps an XGBClassifier with label encoding and a simple predict interface.
    """

    def __init__(self):
        self.clf     = XGBClassifier(**XGB_PARAMS)
        self.encoder = LabelEncoder()
        self.trained = False

    # ------------------------------------------------------------------
    # Training
    # ------------------------------------------------------------------

    def train(self, df_features: pd.DataFrame) -> dict:
        """
        Train the XGBoost model using walk-forward splits.
        Returns a dict with train/val/test classification reports.
        """
        # Create labels
        df = df_features.copy()
        df["label"] = create_labels(df)
        df = df.dropna(subset=["label"] + FEATURE_COLUMNS)

        # Walk-forward split
        train_df, val_df, test_df = walk_forward_split(df)

        X_train = train_df[FEATURE_COLUMNS].values
        y_train = train_df["label"].astype(int).values

        X_val   = val_df[FEATURE_COLUMNS].values
        y_val   = val_df["label"].astype(int).values

        X_test  = test_df[FEATURE_COLUMNS].values
        y_test  = test_df["label"].astype(int).values

        # Encode labels: XGBoost needs 0, 1, 2 not -1, 0, 1
        all_labels = np.concatenate([y_train, y_val, y_test])
        self.encoder.fit(all_labels)

        y_train_enc = self.encoder.transform(y_train)
        y_val_enc   = self.encoder.transform(y_val)

        logger.info("Training XGBoost on %d samples...", len(X_train))

        self.clf.fit(
            X_train, y_train_enc,
            eval_set=[(X_val, y_val_enc)],
            verbose=50,
            early_stopping_rounds=30,  # stop if val loss doesn't improve for 30 rounds
        )

        self.trained = True

        # Evaluate
        reports = {}
        for name, X, y_raw in [("train", X_train, y_train),
                                ("val",   X_val,   y_val),
                                ("test",  X_test,  y_test)]:
            preds_enc = self.clf.predict(X)
            preds     = self.encoder.inverse_transform(preds_enc)
            report    = classification_report(y_raw, preds,
                                              target_names=["SELL", "HOLD", "BUY"],
                                              output_dict=True)
            reports[name] = report
            logger.info("\n%s set performance:\n%s", name.upper(),
                        classification_report(y_raw, preds,
                                              target_names=["SELL", "HOLD", "BUY"]))

        # Feature importance
        importance = pd.Series(
            self.clf.feature_importances_,
            index=FEATURE_COLUMNS
        ).sort_values(ascending=False)

        logger.info("\nTop 10 most important features:\n%s", importance.head(10).to_string())

        return reports

    # ------------------------------------------------------------------
    # Prediction
    # ------------------------------------------------------------------

    def predict_latest(self, df_features: pd.DataFrame) -> tuple:
        """
        Predict the signal for the most recent complete bar.

        Returns
        -------
        signal      : int   — 1 = BUY, -1 = SELL, 0 = HOLD
        probability : float — confidence of the predicted class (0.0 – 1.0)
        """
        if not self.trained:
            raise RuntimeError("Model has not been trained yet. Call train() first.")

        # Use the last available row with all features present
        row = df_features[FEATURE_COLUMNS].dropna().iloc[[-1]]

        probs     = self.clf.predict_proba(row)[0]           # shape: (3,)
        class_enc = np.argmax(probs)
        signal    = int(self.encoder.inverse_transform([class_enc])[0])
        prob      = float(probs[class_enc])

        class_name = {1: "BUY", -1: "SELL", 0: "HOLD"}.get(signal, "UNKNOWN")
        logger.info("Signal: %s  (confidence: %.1f%%)", class_name, prob * 100)

        return signal, prob

    def predict_proba_latest(self, df_features: pd.DataFrame) -> dict:
        """
        Return full probability distribution for the latest bar.
        Useful for setting confidence thresholds before trading.
        """
        row   = df_features[FEATURE_COLUMNS].dropna().iloc[[-1]]
        probs = self.clf.predict_proba(row)[0]

        classes = self.encoder.inverse_transform([0, 1, 2])
        return dict(zip([int(c) for c in classes], probs.tolist()))

    # ------------------------------------------------------------------
    # Persistence
    # ------------------------------------------------------------------

    def save(self, path: str = MODEL_PATH):
        """Save the trained model and label encoder to disk."""
        os.makedirs(os.path.dirname(path), exist_ok=True)
        joblib.dump({"clf": self.clf, "encoder": self.encoder}, path)
        logger.info("Model saved to %s", path)

    @classmethod
    def load(cls, path: str = MODEL_PATH) -> "TradingModel":
        """Load a previously saved model from disk."""
        if not os.path.exists(path):
            raise FileNotFoundError(
                f"Model file not found: {path}\nRun model.py to train first."
            )
        obj = joblib.load(path)
        m = cls()
        m.clf     = obj["clf"]
        m.encoder = obj["encoder"]
        m.trained = True
        logger.info("Model loaded from %s", path)
        return m


# ------------------------------------------------------------------
# Entry point: train and save
# ------------------------------------------------------------------

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s [%(levelname)s] %(message)s")

    logger.info("Loading price data...")
    df_raw = load_data()

    logger.info("Computing features...")
    df_feat = compute_features(df_raw)

    logger.info("Training model...")
    model   = TradingModel()
    reports = model.train(df_feat)

    model.save()

    # Quick sanity check on the most recent bar
    signal, prob = model.predict_latest(df_feat)
    label = {1: "BUY", -1: "SELL", 0: "HOLD"}.get(signal, "UNKNOWN")
    print(f"\nLatest signal: {label}  (confidence: {prob:.1%})")
