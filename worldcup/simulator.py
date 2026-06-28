"""Monte Carlo simulation of the 2026 FIFA World Cup.

Uses the goal model's Poisson rates to sample every remaining match.
Already-played matches enter with their real scores. Implements the
official 2026 group tiebreakers (head-to-head before overall goal
difference — Article 13), the ranking of third-placed teams, the official
round-of-32 bracket template (data/bracket.json) and knockout progression
to the final.
"""

from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np
import pandas as pd

from .dataset import FeatureBuilder, load_teams
from .model import MAX_GOALS, GoalModel, score_matrix
from .ratings import expected_score

DATA_DIR = Path(__file__).parent / "data"

STAGE_OF_ROUND = {"round_of_32": "R32", "round_of_16": "R16",
                  "quarterfinals": "QF", "semifinals": "SF", "final": "F"}
ET_RATE_FACTOR = 1.0 / 3.0  # extra time is a third of a match
PENALTY_ELO_EDGE = 0.1      # shootouts are nearly a coin flip


def load_bracket() -> dict:
    with open(DATA_DIR / "bracket.json") as f:
        return json.load(f)


def load_third_override() -> dict | None:
    """Official third-place slot allocation, fixed once the group stage ends.
    When present it replaces the Annex C approximation so the simulated R32
    matches the real bracket exactly."""
    p = DATA_DIR / "third_place_actual.json"
    if p.exists():
        return json.load(open(p)).get("slots")
    return None


def load_knockout_results() -> dict:
    """Actual played knockout results keyed by bracket match number (as int).
    The simulator forces the recorded winner for these ties instead of
    simulating them, and propagates the winner downstream."""
    p = DATA_DIR / "knockout_results.json"
    if not p.exists():
        return {}
    raw = json.load(open(p)).get("results", {})
    return {int(k): v for k, v in raw.items()}


class MatchPredictor:
    """Caches Poisson rates per pairing.

    Team strength features are frozen at the latest data refresh, so a
    pairing's rates are constant across simulations.
    """

    def __init__(self, model: GoalModel, state: FeatureBuilder, hosts: list[str]):
        self.model = model
        self.rho = getattr(model, "rho", 0.0)
        self.state = state
        self.hosts = set(hosts)
        self.cache: dict[tuple, tuple[float, float]] = {}
        self._cum: dict[tuple, np.ndarray] = {}

    def rates(self, home: str, away: str, venue_country: str | None) -> tuple[float, float]:
        # A side only gets home advantage when playing in its own country.
        home_adv = home in self.hosts and home == venue_country
        away_adv = away in self.hosts and away == venue_country
        key = (home, away, home_adv, away_adv)
        if key not in self.cache:
            if away_adv and not home_adv:
                feats = self.state.match_features(away, home, neutral=False,
                                                  tournament="FIFA World Cup")
                la, lh = self.model.predict_rates(pd.DataFrame([feats]))
            else:
                feats = self.state.match_features(home, away, neutral=not home_adv,
                                                  tournament="FIFA World Cup")
                lh, la = self.model.predict_rates(pd.DataFrame([feats]))
            self.cache[key] = (float(lh[0]), float(la[0]))
        return self.cache[key]

    def score_cdf(self, home: str, away: str, venue_country: str | None,
                  et: bool = False) -> np.ndarray:
        """Flattened cumulative scoreline distribution (Dixon-Coles
        adjusted) for sampling. `et` scales rates to 30 minutes."""
        key = (home, away, venue_country, et)
        if key not in self._cum:
            lh, la = self.rates(home, away, venue_country)
            if et:
                lh, la = lh * ET_RATE_FACTOR, la * ET_RATE_FACTOR
            m = score_matrix(lh, la, self.rho)
            self._cum[key] = np.cumsum(m.ravel())
        return self._cum[key]


def sample_scores(cum: np.ndarray, u: np.ndarray | float) -> tuple:
    """Map uniform draws through a flattened scoreline CDF."""
    idx = np.searchsorted(cum, u, side="right")
    idx = np.minimum(idx, len(cum) - 1)
    return idx // (MAX_GOALS + 1), idx % (MAX_GOALS + 1)


# --------------------------------------------------------------- standings

def _table(teams: list[str], results: list[tuple[str, str, int, int]],
           ) -> dict[str, tuple[int, int, int]]:
    """(points, goal difference, goals for) per team."""
    s = {t: [0, 0, 0] for t in teams}
    for h, a, hg, ag in results:
        if h in s:
            s[h][1] += hg - ag
            s[h][2] += hg
            s[h][0] += 3 if hg > ag else (1 if hg == ag else 0)
        if a in s:
            s[a][1] += ag - hg
            s[a][2] += ag
            s[a][0] += 3 if ag > hg else (1 if ag == hg else 0)
    return {t: tuple(v) for t, v in s.items()}


def fifa_group_rank(teams: list[str], results: list[tuple[str, str, int, int]],
                    strength: dict[str, float]) -> list[str]:
    """Order a group by the official 2026 tiebreakers (Article 13).

    points > head-to-head points/GD/GF among tied teams (reapplied to any
    still-tied subset) > overall GD > overall GF > FIFA ranking (proxied
    here by Elo; fair-play points are not modelled).
    """
    overall = _table(teams, results)

    def resolve(tied: list[str], allow_h2h: bool) -> list[str]:
        if len(tied) == 1:
            return tied
        if allow_h2h:
            sub = [r for r in results if r[0] in tied and r[1] in tied]
            stats = _table(tied, sub)
        else:
            stats = {t: (overall[t][1], overall[t][2], strength[t]) for t in tied}
        order = sorted(tied, key=lambda t: stats[t], reverse=True)
        out: list[str] = []
        block = [order[0]]
        for t in order[1:]:
            if stats[t] == stats[block[-1]]:
                block.append(t)
            else:
                out.extend(_settle(block, tied, allow_h2h))
                block = [t]
        out.extend(_settle(block, tied, allow_h2h))
        return out

    def _settle(block: list[str], parent: list[str], was_h2h: bool) -> list[str]:
        if len(block) == 1:
            return block
        if was_h2h and len(block) < len(parent):
            return resolve(block, allow_h2h=True)   # reapply h2h to subset
        return resolve(block, allow_h2h=False)      # fall through to overall

    ordered = sorted(teams, key=lambda t: overall[t][0], reverse=True)
    out: list[str] = []
    block = [ordered[0]]
    for t in ordered[1:]:
        if overall[t][0] == overall[block[-1]][0]:
            block.append(t)
        else:
            out.extend(resolve(block, allow_h2h=True))
            block = [t]
    out.extend(resolve(block, allow_h2h=True))
    return out


def rank_thirds(third_rows: list[tuple[str, str, tuple]], strength: dict[str, float],
                ) -> list[tuple[str, str]]:
    """Best-first ranking of third-placed teams: points, GD, GF, then FIFA
    ranking (Elo proxy)."""
    ordered = sorted(third_rows,
                     key=lambda r: (r[2][0], r[2][1], r[2][2], strength[r[1]]),
                     reverse=True)
    return [(g, t) for g, t, _ in ordered]


def allocate_thirds(qualified: list[tuple[str, str]], slots: list[dict]) -> dict[str, str]:
    """Assign the 8 best thirds to the R32 slots that accept their group.

    FIFA's Annex C fixes the assignment for each of the 495 possible group
    combinations; that table is not public in machine-readable form, so we
    approximate it: better-ranked thirds claim the first eligible slot, with
    backtracking to guarantee a complete assignment. All hard constraints
    (slot group lists; never facing your own group winner) are respected.
    """
    slot_ids = [s["slot"] for s in slots]
    allowed = {s["slot"]: set(s["groups"]) for s in slots}
    assignment: dict[str, str] = {}

    def backtrack(i: int, used: frozenset) -> bool:
        if i == len(qualified):
            return True
        group, team = qualified[i]
        for sid in slot_ids:
            if sid in used or group not in allowed[sid]:
                continue
            assignment[sid] = team
            if backtrack(i + 1, used | {sid}):
                return True
            del assignment[sid]
        return False

    if not backtrack(0, frozenset()):
        raise RuntimeError(f"No valid third-place allocation for {qualified}")
    return assignment


# -------------------------------------------------------------- simulation

class TournamentSimulator:
    def __init__(self, predictor: MatchPredictor, group_fixtures: pd.DataFrame,
                 seed: int = 42):
        """group_fixtures: the 72 group matches with columns home_team,
        away_team, home_score, away_score (NaN if unplayed), neutral,
        country (venue), group."""
        self.pred = predictor
        self.bracket = load_bracket()
        self.teams_cfg = load_teams()
        self.groups: dict[str, list[str]] = self.teams_cfg["groups"]
        self.rng = np.random.default_rng(seed)

        gf = group_fixtures.reset_index(drop=True)
        self.fixtures = gf
        self.played_mask = gf["home_score"].notna().to_numpy()
        self.cdfs = np.stack([
            predictor.score_cdf(r.home_team, r.away_team,
                                None if r.neutral else r.country)
            for r in gf.itertuples(index=False)
        ])  # (72, (MAX_GOALS+1)^2)
        self.elo = {t: predictor.state.elo.get(t)
                    for g in self.groups.values() for t in g}
        self._fix_tuples = [(r.home_team, r.away_team)
                            for r in gf.itertuples(index=False)]
        self._group_match_idx = {g: gf.index[gf["group"] == g].to_list()
                                 for g in self.groups}

    def _sample_group_scores(self, n_sims: int) -> np.ndarray:
        n_fix = len(self.fixtures)
        scores = np.empty((n_sims, n_fix, 2), dtype=np.int64)
        u = self.rng.random((n_sims, n_fix))
        for j in range(n_fix):
            hg, ag = sample_scores(self.cdfs[j], u[:, j])
            scores[:, j, 0] = hg
            scores[:, j, 1] = ag
        actual = self.fixtures[["home_score", "away_score"]].to_numpy(dtype=float)
        scores[:, self.played_mask, :] = actual[self.played_mask].astype(np.int64)
        return scores

    def _knockout_match(self, home: str, away: str, venue_country: str | None,
                        ) -> tuple[str, str]:
        """Returns (winner, loser): 90 minutes, then extra time, then pens."""
        hg, ag = sample_scores(self.pred.score_cdf(home, away, venue_country),
                               self.rng.random())
        if hg != ag:
            return (home, away) if hg > ag else (away, home)
        eh, ea = sample_scores(
            self.pred.score_cdf(home, away, venue_country, et=True),
            self.rng.random())
        if eh != ea:
            return (home, away) if eh > ea else (away, home)
        p_home = 0.5 + PENALTY_ELO_EDGE * (
            expected_score(self.elo[home], self.elo[away]) - 0.5)
        if self.rng.random() < p_home:
            return home, away
        return away, home

    def run(self, n_sims: int = 100_000) -> "SimResults":
        bracket = self.bracket
        third_override = load_third_override()
        ko_results = load_knockout_results()
        res = SimResults(self.groups, n_sims)
        all_scores = self._sample_group_scores(n_sims)

        ko_rounds = [(STAGE_OF_ROUND[r], bracket[r])
                     for r in ("round_of_32", "round_of_16",
                               "quarterfinals", "semifinals")]

        for s in range(n_sims):
            scores = all_scores[s]
            slots: dict[str, str] = {}
            thirds: list[tuple[str, str, tuple]] = []

            for g, members in self.groups.items():
                results = [(h, a, int(scores[i, 0]), int(scores[i, 1]))
                           for i in self._group_match_idx[g]
                           for h, a in (self._fix_tuples[i],)]
                order = fifa_group_rank(members, results, self.elo)
                pts = _table(members, results)
                res.record_group(g, order, pts)
                slots[f"W_{g}"] = order[0]
                slots[f"RU_{g}"] = order[1]
                thirds.append((g, order[2], pts[order[2]]))

            qualified = rank_thirds(thirds, self.elo)[:8]
            res.record_thirds(qualified)
            if third_override:
                slots.update(third_override)
            else:
                slots.update(allocate_thirds(qualified, bracket["third_place_slots"]))

            advancers: dict[str, str] = {}
            for stage, matches in ko_rounds:
                for m in matches:
                    home = slots.get(m["home"]) or advancers[m["home"]]
                    away = slots.get(m["away"]) or advancers[m["away"]]
                    forced = ko_results.get(m["match"], {}).get("winner")
                    if forced in (home, away):
                        w = forced
                    else:
                        w, _ = self._knockout_match(home, away, m.get("venue_country"))
                    advancers[f"W{m['match']}"] = w
                    res.record_ko(stage, m["match"], home, away, w)

            fm = bracket["final"]
            fh, fa = advancers[fm["home"]], advancers[fm["away"]]
            forced = ko_results.get(fm["match"], {}).get("winner")
            if forced in (fh, fa):
                champion = forced
                runner_up = fa if champion == fh else fh
            else:
                champion, runner_up = self._knockout_match(fh, fa, fm.get("venue_country"))
            res.record_ko("F", fm["match"], fh, fa, champion)
            res.record_final(champion, runner_up)
        return res


class SimResults:
    """Aggregates outcomes across simulations."""

    def __init__(self, groups: dict[str, list[str]], n_sims: int):
        self.n = n_sims
        self.groups = groups
        teams = [t for g in groups.values() for t in g]
        self.rank_counts = {t: np.zeros(4) for t in teams}
        self.points_sum = {t: 0.0 for t in teams}
        self.gd_sum = {t: 0.0 for t in teams}
        self.third_qualified = Counter()
        self.stage_counts = {t: Counter() for t in teams}
        self.match_pairings: dict[int, Counter] = defaultdict(Counter)
        self.match_wins_in_pairing: dict[int, Counter] = defaultdict(Counter)
        self.champion = Counter()
        self.final_pair = Counter()

    def record_group(self, g: str, order: list[str], pts: dict[str, tuple]):
        for pos, t in enumerate(order):
            self.rank_counts[t][pos] += 1
        for t, v in pts.items():
            self.points_sum[t] += v[0]
            self.gd_sum[t] += v[1]

    def record_thirds(self, qualified: list[tuple[str, str]]):
        for _, t in qualified:
            self.third_qualified[t] += 1

    def record_ko(self, stage: str, match_no: int, home: str, away: str, winner: str):
        self.stage_counts[home][stage] += 1
        self.stage_counts[away][stage] += 1
        pair = (home, away)
        self.match_pairings[match_no][pair] += 1
        self.match_wins_in_pairing[match_no][(pair, winner)] += 1

    def record_final(self, champion: str, runner_up: str):
        self.champion[champion] += 1
        self.final_pair[(champion, runner_up)] += 1
        self.stage_counts[champion]["W"] += 1

    # ------------------------------------------------------------- queries

    def team_table(self) -> pd.DataFrame:
        rows = []
        for g, members in self.groups.items():
            for t in members:
                rc = self.rank_counts[t] / self.n
                sc = self.stage_counts[t]
                rows.append({
                    "group": g, "team": t,
                    "exp_points": self.points_sum[t] / self.n,
                    "exp_gd": self.gd_sum[t] / self.n,
                    "p_win_group": rc[0], "p_runner_up": rc[1],
                    "p_third": rc[2], "p_fourth": rc[3],
                    "p_third_advance": self.third_qualified[t] / self.n,
                    "p_R32": sc["R32"] / self.n, "p_R16": sc["R16"] / self.n,
                    "p_QF": sc["QF"] / self.n, "p_SF": sc["SF"] / self.n,
                    "p_final": sc["F"] / self.n,
                    "p_champion": self.champion[t] / self.n,
                })
        df = pd.DataFrame(rows)
        return df.sort_values(["p_champion", "p_final", "p_SF"],
                              ascending=False).reset_index(drop=True)

    def modal_pairing(self, match_no: int) -> tuple[tuple[str, str], float, float]:
        """Most likely pairing for a knockout match.

        Returns ((home, away), P(pairing), P(home advances | pairing)).
        """
        pair, cnt = self.match_pairings[match_no].most_common(1)[0]
        home_wins = self.match_wins_in_pairing[match_no][(pair, pair[0])]
        return pair, cnt / self.n, home_wins / cnt
