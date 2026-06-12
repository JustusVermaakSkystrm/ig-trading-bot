"""Elo ratings for international football, computed from full match history.

Implements the standard World Football Elo formulation (eloratings.net):
  - K factor scaled by match importance
  - goal-difference multiplier
  - home advantage of 100 points for non-neutral venues
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field

HOME_ADVANTAGE = 100.0
INITIAL_RATING = 1500.0

# K factors by match importance (eloratings.net convention)
K_WORLD_CUP = 60.0
K_CONTINENTAL_FINALS = 50.0
K_QUALIFIERS_MAJOR = 40.0
K_OTHER_TOURNAMENTS = 30.0
K_FRIENDLY = 20.0

CONTINENTAL_FINALS = {
    "Copa América", "African Cup of Nations", "AFC Asian Cup",
    "UEFA Euro", "CONCACAF Championship", "Gold Cup",
    "Oceania Nations Cup", "Confederations Cup",
}

QUALIFIER_KEYWORDS = ("qualification", "qualifier", "Nations League")


def k_factor(tournament: str) -> float:
    t = tournament or ""
    if t == "FIFA World Cup":
        return K_WORLD_CUP
    if t in CONTINENTAL_FINALS:
        return K_CONTINENTAL_FINALS
    tl = t.lower()
    if any(k.lower() in tl for k in QUALIFIER_KEYWORDS):
        return K_QUALIFIERS_MAJOR
    if t == "Friendly":
        return K_FRIENDLY
    return K_OTHER_TOURNAMENTS


def importance_level(tournament: str) -> int:
    """Ordinal match-importance feature for the ML model."""
    t = tournament or ""
    if t == "FIFA World Cup":
        return 4
    if t in CONTINENTAL_FINALS:
        return 3
    tl = t.lower()
    if any(k.lower() in tl for k in QUALIFIER_KEYWORDS):
        return 2
    if t == "Friendly":
        return 0
    return 1


def goal_multiplier(goal_diff: int) -> float:
    n = abs(goal_diff)
    if n <= 1:
        return 1.0
    if n == 2:
        return 1.5
    return (11.0 + n) / 8.0


def expected_score(rating_a: float, rating_b: float) -> float:
    return 1.0 / (1.0 + 10.0 ** ((rating_b - rating_a) / 400.0))


@dataclass
class EloTracker:
    """Sequential Elo state over a chronologically sorted match list."""

    ratings: dict = field(default_factory=dict)

    def get(self, team: str) -> float:
        return self.ratings.get(team, INITIAL_RATING)

    def pre_match(self, home: str, away: str, neutral: bool) -> tuple[float, float, float]:
        """Pre-match ratings and the home win expectancy (with venue bonus)."""
        rh, ra = self.get(home), self.get(away)
        bonus = 0.0 if neutral else HOME_ADVANTAGE
        return rh, ra, expected_score(rh + bonus, ra)

    def update(self, home: str, away: str, home_goals: int, away_goals: int,
               tournament: str, neutral: bool) -> None:
        rh, ra, exp_home = self.pre_match(home, away, neutral)
        if home_goals > away_goals:
            actual = 1.0
        elif home_goals == away_goals:
            actual = 0.5
        else:
            actual = 0.0
        delta = k_factor(tournament) * goal_multiplier(home_goals - away_goals) * (actual - exp_home)
        self.ratings[home] = rh + delta
        self.ratings[away] = ra - delta


# Attack/defence ratings: online Poisson regression on goals. A single Elo
# number cannot separate "wins 1-0" sides from "wins 4-2" sides, but a goal
# model needs exactly that distinction.
AD_MU = 0.20            # log of the global mean goals per team per match
AD_HOME = 0.25          # home scoring bonus in log space
AD_ETA = 0.05           # per-goal learning rate (scaled by importance)
AD_GOAL_CAP = 6         # limit the shock from historical blowouts


@dataclass
class AttackDefence:
    """Per-team attack/defence strengths in log-goal space.

    Expected goals: home ~ exp(MU + HOME + att_h - def_a),
    away ~ exp(MU + att_a - def_h). Updates follow the Poisson
    log-likelihood gradient (residual = observed - expected goals).
    """

    att: dict = field(default_factory=dict)
    dfc: dict = field(default_factory=dict)

    def get(self, team: str) -> tuple[float, float]:
        return self.att.get(team, 0.0), self.dfc.get(team, 0.0)

    def expected(self, home: str, away: str, neutral: bool) -> tuple[float, float]:
        ah, dh = self.get(home)
        aa, da = self.get(away)
        bonus = 0.0 if neutral else AD_HOME
        return (math.exp(AD_MU + bonus + ah - da),
                math.exp(AD_MU + aa - dh))

    def update(self, home: str, away: str, home_goals: int, away_goals: int,
               tournament: str, neutral: bool) -> None:
        lh, la = self.expected(home, away, neutral)
        eta = AD_ETA * (k_factor(tournament) / 40.0)
        rh = min(home_goals, AD_GOAL_CAP) - lh
        ra = min(away_goals, AD_GOAL_CAP) - la
        ah, dh = self.get(home)
        aa, da = self.get(away)
        self.att[home] = ah + eta * rh
        self.dfc[away] = da - eta * rh
        self.att[away] = aa + eta * ra
        self.dfc[home] = dh - eta * ra
