"""ML goal model: gradient-boosted Poisson regression for match scorelines.

Two-step design (mirroring the approach in The Conversation's World Cup
study): team strengths are estimated first (Elo + rolling form, see
dataset.py), then a machine-learning model learns how to combine those
strength estimates with match context (venue, importance) into expected
goal rates for both sides. The pair of Poisson rates is the "loaded dice"
from which full scoreline distributions follow.
"""

from __future__ import annotations

import pickle
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import poisson
from sklearn.ensemble import HistGradientBoostingRegressor

from .dataset import FEATURES

MODEL_PATH = Path(__file__).parent / "data" / "goal_model.pkl"
MAX_GOALS = 12          # score-matrix truncation
WEIGHT_HALF_LIFE_YEARS = 10.0


def _recency_weights(dates: pd.Series) -> np.ndarray:
    age_years = (dates.max() - dates).dt.days / 365.25
    return np.power(0.5, age_years / WEIGHT_HALF_LIFE_YEARS)


def _make_regressor() -> HistGradientBoostingRegressor:
    return HistGradientBoostingRegressor(
        loss="poisson", max_iter=400, learning_rate=0.05,
        max_leaf_nodes=31, min_samples_leaf=50,
        l2_regularization=1.0, random_state=7,
    )


class GoalModel:
    def __init__(self):
        self.model_home = _make_regressor()
        self.model_away = _make_regressor()

    def fit(self, table: pd.DataFrame) -> "GoalModel":
        X = table[FEATURES]
        w = _recency_weights(table["date"])
        self.model_home.fit(X, table["home_goals"], sample_weight=w)
        self.model_away.fit(X, table["away_goals"], sample_weight=w)
        return self

    def predict_rates(self, X: pd.DataFrame) -> tuple[np.ndarray, np.ndarray]:
        lam_h = np.clip(self.model_home.predict(X[FEATURES]), 0.05, 6.0)
        lam_a = np.clip(self.model_away.predict(X[FEATURES]), 0.05, 6.0)
        return lam_h, lam_a

    def save(self, path: Path = MODEL_PATH) -> None:
        with open(path, "wb") as f:
            pickle.dump(self, f)

    @staticmethod
    def load(path: Path = MODEL_PATH) -> "GoalModel":
        with open(path, "rb") as f:
            return pickle.load(f)


def score_matrix(lam_h: float, lam_a: float, max_goals: int = MAX_GOALS) -> np.ndarray:
    """P(home scores i, away scores j) under independent Poisson rates."""
    gh = poisson.pmf(np.arange(max_goals + 1), lam_h)
    ga = poisson.pmf(np.arange(max_goals + 1), lam_a)
    m = np.outer(gh, ga)
    return m / m.sum()


def outcome_probs(lam_h: float, lam_a: float) -> tuple[float, float, float]:
    """(P(home win), P(draw), P(away win)) in 90 minutes."""
    m = score_matrix(lam_h, lam_a)
    home = float(np.tril(m, -1).sum())
    draw = float(np.trace(m))
    away = float(np.triu(m, 1).sum())
    return home, draw, away


def most_likely_score(lam_h: float, lam_a: float) -> tuple[int, int]:
    m = score_matrix(lam_h, lam_a)
    i, j = np.unravel_index(int(m.argmax()), m.shape)
    return int(i), int(j)


# ---------------------------------------------------------------- validation

def _rps(probs: np.ndarray, outcome_idx: np.ndarray) -> float:
    """Mean ranked probability score over (home, draw, away) forecasts."""
    cum = np.cumsum(probs, axis=1)
    obs = np.zeros_like(probs)
    obs[np.arange(len(outcome_idx)), outcome_idx] = 1.0
    cum_obs = np.cumsum(obs, axis=1)
    return float(np.mean(np.sum((cum - cum_obs) ** 2, axis=1) / (probs.shape[1] - 1)))


def evaluate_holdout(table: pd.DataFrame, holdout_from: str = "2024-01-01") -> dict:
    """Time-split validation: train before `holdout_from`, test after.

    Compares the ML model with an Elo-only baseline (win expectancy from the
    Elo difference, draw rate fixed at the empirical frequency).
    """
    train = table[table["date"] < holdout_from]
    test = table[table["date"] >= holdout_from]
    model = GoalModel().fit(train)
    lam_h, lam_a = model.predict_rates(test)
    probs = np.array([outcome_probs(h, a) for h, a in zip(lam_h, lam_a)])

    outcome = np.where(test["home_goals"] > test["away_goals"], 0,
                       np.where(test["home_goals"] == test["away_goals"], 1, 2))

    # Elo baseline: split Elo win expectancy into W/D/L with a draw share
    # that peaks for evenly matched sides.
    exp_home = 1.0 / (1.0 + 10.0 ** (-test["elo_diff_adj"] / 400.0))
    base_draw = 0.29 - 0.20 * np.abs(exp_home - 0.5)
    base = np.column_stack([exp_home * (1 - base_draw), base_draw,
                            (1 - exp_home) * (1 - base_draw)])

    eps = 1e-12
    return {
        "n_test": len(test),
        "model_rps": _rps(probs, outcome),
        "elo_rps": _rps(base, outcome),
        "model_logloss": float(-np.mean(np.log(probs[np.arange(len(outcome)), outcome] + eps))),
        "elo_logloss": float(-np.mean(np.log(base[np.arange(len(outcome)), outcome] + eps))),
        "goal_mae_home": float(np.mean(np.abs(lam_h - test["home_goals"]))),
        "goal_mae_away": float(np.mean(np.abs(lam_a - test["away_goals"]))),
    }
