"""ML goal model: gradient-boosted Poisson regression for match scorelines.

Two-step design (mirroring the approach in The Conversation's World Cup
study): team strengths are estimated first (Elo + attack/defence ratings +
rolling form, see dataset.py), then a machine-learning model learns how to
combine those strength estimates with match context (venue, importance)
into expected goal rates for both sides. Scoreline distributions follow
from the rates with a Dixon-Coles low-score correction, which fixes the
independent-Poisson tendency to underestimate 0-0 and 1-1 draws.
"""

from __future__ import annotations

import pickle
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.optimize import minimize_scalar
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


def _dc_tau(hg: np.ndarray, ag: np.ndarray, lam_h: np.ndarray,
            lam_a: np.ndarray, rho: float) -> np.ndarray:
    """Dixon-Coles low-score adjustment factor for observed scores."""
    tau = np.ones_like(lam_h, dtype=float)
    tau = np.where((hg == 0) & (ag == 0), 1.0 - lam_h * lam_a * rho, tau)
    tau = np.where((hg == 0) & (ag == 1), 1.0 + lam_h * rho, tau)
    tau = np.where((hg == 1) & (ag == 0), 1.0 + lam_a * rho, tau)
    tau = np.where((hg == 1) & (ag == 1), 1.0 - rho, tau)
    return tau


def fit_rho(lam_h: np.ndarray, lam_a: np.ndarray, hg: np.ndarray,
            ag: np.ndarray, weights: np.ndarray | None = None) -> float:
    """MLE for the Dixon-Coles rho given predicted rates and observed
    scores. Only matches with both scores <= 1 inform rho."""
    mask = (hg <= 1) & (ag <= 1)
    if mask.sum() < 100:
        return 0.0
    lh, la = lam_h[mask], lam_a[mask]
    h, a = hg[mask], ag[mask]
    w = np.ones(mask.sum()) if weights is None else weights[mask]

    def nll(rho: float) -> float:
        tau = _dc_tau(h, a, lh, la, rho)
        return -float(np.sum(w * np.log(np.clip(tau, 1e-9, None))))

    res = minimize_scalar(nll, bounds=(-0.3, 0.15), method="bounded")
    return float(res.x)


class GoalModel:
    def __init__(self, features: list[str] | None = None, use_dc: bool = True):
        self.features = features or FEATURES
        self.use_dc = use_dc
        self.rho = 0.0
        self.model_home = _make_regressor()
        self.model_away = _make_regressor()

    def fit(self, table: pd.DataFrame) -> "GoalModel":
        X = table[self.features]
        w = _recency_weights(table["date"])
        self.model_home.fit(X, table["home_goals"], sample_weight=w)
        self.model_away.fit(X, table["away_goals"], sample_weight=w)
        if self.use_dc:
            lam_h, lam_a = self.predict_rates(table)
            self.rho = fit_rho(lam_h, lam_a,
                               table["home_goals"].to_numpy(),
                               table["away_goals"].to_numpy(),
                               w.to_numpy() if hasattr(w, "to_numpy") else w)
        return self

    def predict_rates(self, X: pd.DataFrame) -> tuple[np.ndarray, np.ndarray]:
        lam_h = np.clip(self.model_home.predict(X[self.features]), 0.05, 6.0)
        lam_a = np.clip(self.model_away.predict(X[self.features]), 0.05, 6.0)
        return lam_h, lam_a

    def save(self, path: Path = MODEL_PATH) -> None:
        with open(path, "wb") as f:
            pickle.dump(self, f)

    @staticmethod
    def load(path: Path = MODEL_PATH) -> "GoalModel":
        with open(path, "rb") as f:
            model = pickle.load(f)
        if not hasattr(model, "rho"):  # pre-Dixon-Coles pickle
            model.rho = 0.0
            model.features = FEATURES
        return model


def score_matrix(lam_h: float, lam_a: float, rho: float = 0.0,
                 max_goals: int = MAX_GOALS) -> np.ndarray:
    """P(home scores i, away scores j): independent Poisson with the
    Dixon-Coles adjustment applied to the 0/1-goal cells."""
    gh = poisson.pmf(np.arange(max_goals + 1), lam_h)
    ga = poisson.pmf(np.arange(max_goals + 1), lam_a)
    m = np.outer(gh, ga)
    if rho:
        m[0, 0] *= max(1.0 - lam_h * lam_a * rho, 1e-9)
        m[0, 1] *= max(1.0 + lam_h * rho, 1e-9)
        m[1, 0] *= max(1.0 + lam_a * rho, 1e-9)
        m[1, 1] *= max(1.0 - rho, 1e-9)
    return m / m.sum()


def outcome_probs(lam_h: float, lam_a: float, rho: float = 0.0,
                  ) -> tuple[float, float, float]:
    """(P(home win), P(draw), P(away win)) in 90 minutes."""
    m = score_matrix(lam_h, lam_a, rho)
    home = float(np.tril(m, -1).sum())
    draw = float(np.trace(m))
    away = float(np.triu(m, 1).sum())
    return home, draw, away


def most_likely_score(lam_h: float, lam_a: float, rho: float = 0.0,
                      ) -> tuple[int, int]:
    m = score_matrix(lam_h, lam_a, rho)
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


def _logloss(probs: np.ndarray, outcome_idx: np.ndarray) -> float:
    return float(-np.mean(np.log(probs[np.arange(len(outcome_idx)),
                                       outcome_idx] + 1e-12)))


def _outcome_index(test: pd.DataFrame) -> np.ndarray:
    return np.where(test["home_goals"] > test["away_goals"], 0,
                    np.where(test["home_goals"] == test["away_goals"], 1, 2)
                    ).astype(int)


def _elo_baseline_probs(test: pd.DataFrame) -> np.ndarray:
    """Elo win expectancy split into W/D/L with a draw share that peaks
    for evenly matched sides."""
    exp_home = 1.0 / (1.0 + 10.0 ** (-test["elo_diff_adj"] / 400.0))
    draw = 0.29 - 0.20 * np.abs(exp_home - 0.5)
    return np.column_stack([exp_home * (1 - draw), draw,
                            (1 - exp_home) * (1 - draw)])


ROLLING_WINDOWS = [("2018-01-01", "2020-01-01"), ("2020-01-01", "2022-01-01"),
                   ("2022-01-01", "2024-01-01"), ("2024-01-01", "2027-01-01")]

VARIANTS = {
    "elo_baseline": None,
    "v1_poisson": {"features": "v1", "use_dc": False},
    "v2_ad_dc": {"features": "all", "use_dc": True},
}


def evaluate_rolling(table: pd.DataFrame,
                     windows: list[tuple[str, str]] = ROLLING_WINDOWS,
                     ) -> pd.DataFrame:
    """Rolling-origin validation: for each window, train on everything
    before it and score the window. Compares the Elo baseline, the original
    model (v1: no attack/defence features, plain Poisson) and the current
    model (v2: attack/defence + Dixon-Coles)."""
    from .dataset import FEATURES_V1
    rows = []
    for start, end in windows:
        train = table[table["date"] < start]
        test = table[(table["date"] >= start) & (table["date"] < end)]
        if len(test) == 0:
            continue
        outcome = _outcome_index(test)
        probs = {"elo_baseline": _elo_baseline_probs(test)}

        for name, cfg in VARIANTS.items():
            if cfg is None:
                continue
            feats = FEATURES_V1 if cfg["features"] == "v1" else None
            model = GoalModel(features=feats, use_dc=cfg["use_dc"]).fit(train)
            lam_h, lam_a = model.predict_rates(test)
            probs[name] = np.array([
                outcome_probs(h, a, model.rho)
                for h, a in zip(lam_h, lam_a)])

        for name, p in probs.items():
            rows.append({"window": f"{start[:4]}-{int(end[:4]) - 1}",
                         "n_test": len(test), "model": name,
                         "rps": _rps(p, outcome),
                         "logloss": _logloss(p, outcome)})
    df = pd.DataFrame(rows)
    overall = (df.groupby("model")
               .apply(lambda g: pd.Series({
                   "rps": np.average(g["rps"], weights=g["n_test"]),
                   "logloss": np.average(g["logloss"], weights=g["n_test"]),
                   "n_test": g["n_test"].sum()}), include_groups=False)
               .reset_index())
    overall["window"] = "ALL"
    return pd.concat([df, overall], ignore_index=True)
