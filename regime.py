"""
regime.py
---------
Hidden Markov Model (HMM) based market regime detection.

Detects two hidden regimes from (5-bar log-returns, 14-bar realised volatility):
  State 0 — Trending   : higher absolute returns, directional momentum
  State 1 — Ranging    : lower absolute returns, mean-reverting noise

The detector is designed to be fully causal: at inference time it only
uses data up to and including the current bar.

Typical usage (inside walk-forward loop):
    from regime import RegimeDetector
    detector = RegimeDetector(n_states=2)
    detector.fit(train_df)                         # fit on training window only
    regimes = detector.predict(full_df)            # causal prediction
    df["regime"] = regimes
    # Gate signals: only trade when regime == detector.trending_state
"""

import logging

import numpy as np
import pandas as pd

logger = logging.getLogger(__name__)

# How many bars of realized vol to use for each component
_RV_SHORT = 14
_RV_LONG  = 60
_RET_BARS = 5


def _build_hmm_features(df: pd.DataFrame) -> np.ndarray:
    """
    Build the 2D observation matrix fed to the HMM:
      col 0 — 5-bar log return (directional signal)
      col 1 — 14-bar realised volatility (regime signal)
    """
    close    = df["close"]
    ret5     = np.log(close / close.shift(_RET_BARS)).fillna(0).values
    rv14     = close.pct_change().rolling(_RV_SHORT).std().fillna(0).values
    return np.column_stack([ret5, rv14])


class RegimeDetector:
    """
    2-state Gaussian HMM for market regime classification.

    Parameters
    ----------
    n_states : int
        Number of hidden states (2 = trending / ranging).
    n_iter : int
        EM iterations for HMM fitting.
    """

    def __init__(self, n_states: int = 2, n_iter: int = 200):
        self.n_states      = n_states
        self.n_iter        = n_iter
        self.model         = None
        self.trending_state: int = 0   # will be resolved after fit

    # ------------------------------------------------------------------
    def fit(self, df: pd.DataFrame) -> "RegimeDetector":
        """
        Fit the HMM on df (training window only — never include test data).
        Identifies which state corresponds to the trending/volatile regime.
        Uses VOLATILITY level (not mean return) as the discriminator, which is
        more stable out-of-sample than mean-return discrimination.
        """
        try:
            from hmmlearn.hmm import GaussianHMM
        except ImportError:
            raise ImportError("hmmlearn is required: pip install hmmlearn")

        X = _build_hmm_features(df)

        self.model = GaussianHMM(
            n_components=self.n_states,
            covariance_type="diag",
            n_iter=self.n_iter,
            random_state=42,
        )
        self.model.fit(X)

        # Identify trending state as the one with HIGHER realized volatility
        # (column 1 = rv14).  High-vol states tend to be more directional.
        rv_means = self.model.means_[:, 1]
        self.trending_state = int(np.argmax(rv_means))

        logger.info(
            "HMM fitted: trending_state=%d  (rv_mean=%.5f vs %.5f)",
            self.trending_state,
            rv_means[self.trending_state],
            rv_means[1 - self.trending_state],
        )
        return self

    # ------------------------------------------------------------------
    def predict(self, df: pd.DataFrame) -> pd.Series:
        """
        Predict regime label for every bar in df using the fitted HMM.
        Returns a Series aligned with df.index.
        """
        if self.model is None:
            raise RuntimeError("Call fit() before predict().")
        X      = _build_hmm_features(df)
        states = self.model.predict(X)
        return pd.Series(states, index=df.index, name="regime")

    # ------------------------------------------------------------------
    def is_trending(self, df: pd.DataFrame) -> pd.Series:
        """
        Boolean Series — True where the bar is in the trending regime.
        """
        regimes = self.predict(df)
        return (regimes == self.trending_state).rename("is_trending")

    # ------------------------------------------------------------------
    def add_regime_feature(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Add 'regime' and 'is_trending' columns to df (in-place copy).
        """
        df = df.copy()
        df["regime"]     = self.predict(df)
        df["is_trending"] = (df["regime"] == self.trending_state).astype(int)
        return df
