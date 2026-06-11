"""Data loading and point-in-time feature construction.

Builds, in a single chronological pass with no lookahead leakage:
  - per-match training rows (features + goal targets) for completed matches
  - a current-state snapshot per team (Elo, rolling form) used to build
    feature rows for matches that have not been played yet
"""

from __future__ import annotations

import json
from collections import deque
from pathlib import Path

import numpy as np
import pandas as pd

from .ratings import EloTracker, HOME_ADVANTAGE, importance_level

DATA_DIR = Path(__file__).parent / "data"
RESULTS_URL = "https://raw.githubusercontent.com/martj42/international_results/master/results.csv"
SHOOTOUTS_URL = "https://raw.githubusercontent.com/martj42/international_results/master/shootouts.csv"

FORM_WINDOW = 10

FEATURES = [
    "elo_home", "elo_away", "elo_diff_adj",
    "form_gf_home", "form_ga_home", "form_ppg_home",
    "form_gf_away", "form_ga_away", "form_ppg_away",
    "matches_home", "matches_away",
    "neutral", "importance",
]


def load_teams() -> dict:
    with open(DATA_DIR / "teams.json") as f:
        return json.load(f)


def load_results() -> pd.DataFrame:
    df = pd.read_csv(DATA_DIR / "results.csv")
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date", kind="stable").reset_index(drop=True)
    df["neutral"] = df["neutral"].astype(bool)
    return df


def load_manual_results() -> pd.DataFrame:
    """Optional manual result entry (worldcup/data/manual_results.csv).

    Same columns as results.csv. Rows here override/augment the snapshot —
    useful for entering a final score minutes after a match ends, before the
    upstream dataset catches up.
    """
    path = DATA_DIR / "manual_results.csv"
    if not path.exists():
        return pd.DataFrame()
    df = pd.read_csv(path)
    if df.empty:
        return df
    df["date"] = pd.to_datetime(df["date"])
    df["neutral"] = df["neutral"].astype(bool)
    return df


def merged_results() -> pd.DataFrame:
    """Upstream snapshot with manual overrides applied (manual rows win)."""
    base = load_results()
    manual = load_manual_results()
    if manual.empty:
        return base
    key = ["date", "home_team", "away_team"]
    base = base.merge(manual[key + ["home_score", "away_score"]],
                      on=key, how="left", suffixes=("", "_manual"))
    override = base["home_score_manual"].notna()
    base.loc[override, "home_score"] = base.loc[override, "home_score_manual"]
    base.loc[override, "away_score"] = base.loc[override, "away_score_manual"]
    base = base.drop(columns=["home_score_manual", "away_score_manual"])
    extra = manual.merge(base[key], on=key, how="left", indicator=True)
    extra = extra[extra["_merge"] == "left_only"].drop(columns="_merge")
    if not extra.empty:
        base = pd.concat([base, extra], ignore_index=True).sort_values(
            "date", kind="stable").reset_index(drop=True)
    return base


class _TeamForm:
    __slots__ = ("gf", "ga", "pts", "n")

    def __init__(self):
        self.gf = deque(maxlen=FORM_WINDOW)
        self.ga = deque(maxlen=FORM_WINDOW)
        self.pts = deque(maxlen=FORM_WINDOW)
        self.n = 0

    def features(self) -> tuple[float, float, float]:
        if not self.gf:
            return 1.3, 1.3, 1.3  # rough global averages as priors
        return (float(np.mean(self.gf)), float(np.mean(self.ga)),
                float(np.mean(self.pts)))

    def record(self, scored: int, conceded: int) -> None:
        self.gf.append(scored)
        self.ga.append(conceded)
        self.pts.append(3 if scored > conceded else (1 if scored == conceded else 0))
        self.n += 1


class FeatureBuilder:
    """One chronological pass over history; emits leak-free feature rows."""

    def __init__(self):
        self.elo = EloTracker()
        self.form: dict[str, _TeamForm] = {}

    def _form(self, team: str) -> _TeamForm:
        if team not in self.form:
            self.form[team] = _TeamForm()
        return self.form[team]

    def match_features(self, home: str, away: str, neutral: bool,
                       tournament: str) -> dict:
        rh, ra = self.elo.get(home), self.elo.get(away)
        bonus = 0.0 if neutral else HOME_ADVANTAGE
        fh, fa = self._form(home), self._form(away)
        gf_h, ga_h, ppg_h = fh.features()
        gf_a, ga_a, ppg_a = fa.features()
        return {
            "elo_home": rh, "elo_away": ra,
            "elo_diff_adj": (rh + bonus) - ra,
            "form_gf_home": gf_h, "form_ga_home": ga_h, "form_ppg_home": ppg_h,
            "form_gf_away": gf_a, "form_ga_away": ga_a, "form_ppg_away": ppg_a,
            "matches_home": fh.n, "matches_away": fa.n,
            "neutral": int(neutral), "importance": importance_level(tournament),
        }

    def advance(self, home: str, away: str, hg: int, ag: int,
                tournament: str, neutral: bool) -> None:
        self.elo.update(home, away, hg, ag, tournament, neutral)
        self._form(home).record(hg, ag)
        self._form(away).record(ag, hg)


def build_training_table(results: pd.DataFrame,
                         min_date: str = "1990-01-01",
                         min_matches: int = 20) -> tuple[pd.DataFrame, FeatureBuilder]:
    """Returns (training table, end-of-history state for future predictions).

    The full history feeds Elo/form state; only matches after `min_date`
    where both teams have at least `min_matches` prior games become
    training rows.
    """
    fb = FeatureBuilder()
    rows = []
    min_ts = pd.Timestamp(min_date)
    played = results.dropna(subset=["home_score", "away_score"])
    for r in played.itertuples(index=False):
        feats = fb.match_features(r.home_team, r.away_team, r.neutral, r.tournament)
        if r.date >= min_ts and feats["matches_home"] >= min_matches \
                and feats["matches_away"] >= min_matches:
            feats.update({
                "date": r.date,
                "home_team": r.home_team, "away_team": r.away_team,
                "home_goals": int(r.home_score), "away_goals": int(r.away_score),
            })
            rows.append(feats)
        fb.advance(r.home_team, r.away_team, int(r.home_score),
                   int(r.away_score), r.tournament, r.neutral)
    return pd.DataFrame(rows), fb
