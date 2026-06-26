"""Live re-pricing of tracked personal accumulators (data/tracked_bets.json).

For each bet it runs one shared Monte-Carlo pass over the remaining
tournament and counts the fraction of simulated tournaments in which EVERY
leg lands together — so nested rungs (Argentina to the final implies the
R16/QF/SF rungs) and teams that can knock each other out are handled exactly,
not by multiplying marginals.

It also reports, per leg, the standalone chance and flags the weakest link,
computes expected value against the price actually taken, and surfaces the
upcoming group games most likely to make-or-break a bet.

    python -m worldcup.bets               # re-price with 50k sims
    python -m worldcup.bets --sims 100000
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import pandas as pd

from .dataset import build_training_table, load_teams, merged_results
from .model import GoalModel, MODEL_PATH
from .simulator import (STAGE_OF_ROUND, MatchPredictor, TournamentSimulator,
                        _table, allocate_thirds, fifa_group_rank, rank_thirds)
from .run import world_cup_fixtures

DATA_DIR = Path(__file__).parent / "data"
OUT_DIR = Path(__file__).parent / "outputs"
BETS_PATH = DATA_DIR / "tracked_bets.json"

# Stage ordering: reaching a deeper stage implies every shallower one.
RANK = {"R32": 1, "R16": 2, "QF": 3, "SF": 4, "F": 5}
STAGE_LABEL = {"R32": "Round of 32", "R16": "Round of 16", "QF": "Quarter-finals",
               "SF": "Semi-finals", "F": "the Final"}
DISPLAY = {"United States": "USA"}


def _disp(team: str) -> str:
    return DISPLAY.get(team, team)


def _leg_ok(reached_val: int, lg: dict) -> bool:
    """A leg lands when a team reaches a stage ("reach", default) or is
    eliminated exactly at it ("out" — reached that round but no further)."""
    r = RANK[lg["stage"]]
    if lg.get("type") == "out":
        return reached_val == r
    return reached_val >= r


def _leg_desc(lg: dict) -> str:
    if lg.get("type") == "out":
        return f"out in {STAGE_LABEL[lg['stage']]}"
    return f"reach {STAGE_LABEL[lg['stage']]}"


def load_bets() -> list[dict]:
    return json.loads(BETS_PATH.read_text())["bets"]


def _build_sim(seed: int):
    results = merged_results()
    if not MODEL_PATH.exists():
        raise SystemExit("No trained model — run `python -m worldcup.run train` first.")
    model = GoalModel.load()
    _, state = build_training_table(results)
    teams = load_teams()
    pred = MatchPredictor(model, state, teams["hosts"])
    fixtures = world_cup_fixtures(results)
    return TournamentSimulator(pred, fixtures, seed=seed), fixtures, pred


def simulate_reached_stats(sim, bets: list[dict], n_sims: int,
                           watch: list[dict] | None = None) -> dict:
    """One shared pass over n_sims tournaments.

    Returns joint hit counts and per-leg hit counts, plus — for each watched
    upcoming fixture — bet-success counts split by that game's sampled result.
    That gives an EXACT conditional swing P(bet | home win / draw / away win)
    in a single pass, no per-scenario re-simulation.
    """
    watch = watch or []
    all_scores = sim._sample_group_scores(n_sims)
    bracket = sim.bracket
    ko_rounds = [(STAGE_OF_ROUND[r], bracket[r]) for r in
                 ("round_of_32", "round_of_16", "quarterfinals", "semifinals")]
    joint = {b["id"]: 0 for b in bets}
    leg = {b["id"]: [0] * len(b["legs"]) for b in bets}
    # watch[k] -> {outcome -> total, (bet_id,outcome) -> hits}
    w_total = [{"H": 0, "D": 0, "A": 0} for _ in watch]
    w_hit = [{b["id"]: {"H": 0, "D": 0, "A": 0} for b in bets} for _ in watch]

    for s in range(n_sims):
        scores = all_scores[s]
        slots: dict[str, str] = {}
        thirds = []
        for g, members in sim.groups.items():
            rs = [(h, a, int(scores[i, 0]), int(scores[i, 1]))
                  for i in sim._group_match_idx[g]
                  for h, a in (sim._fix_tuples[i],)]
            order = fifa_group_rank(members, rs, sim.elo)
            pts = _table(members, rs)
            slots[f"W_{g}"], slots[f"RU_{g}"] = order[0], order[1]
            thirds.append((g, order[2], pts[order[2]]))
        qualified = rank_thirds(thirds, sim.elo)[:8]
        slots.update(allocate_thirds(qualified, bracket["third_place_slots"]))

        reached: dict[str, int] = {}
        advancers: dict[str, str] = {}
        for stage, matches in ko_rounds:
            for m in matches:
                home = slots.get(m["home"]) or advancers[m["home"]]
                away = slots.get(m["away"]) or advancers[m["away"]]
                reached[home] = max(reached.get(home, 0), RANK[stage])
                reached[away] = max(reached.get(away, 0), RANK[stage])
                w, _ = sim._knockout_match(home, away, m.get("venue_country"))
                advancers[f"W{m['match']}"] = w
        fm = bracket["final"]
        fh, fa = advancers[fm["home"]], advancers[fm["away"]]
        reached[fh] = max(reached.get(fh, 0), RANK["F"])
        reached[fa] = max(reached.get(fa, 0), RANK["F"])

        bet_ok = {}
        for b in bets:
            ok = True
            for i, lg in enumerate(b["legs"]):
                if _leg_ok(reached.get(lg["team"], 0), lg):
                    leg[b["id"]][i] += 1
                else:
                    ok = False
            bet_ok[b["id"]] = ok
            if ok:
                joint[b["id"]] += 1

        for k, wf in enumerate(watch):
            j = wf["idx"]
            hg, ag = scores[j, 0], scores[j, 1]
            o = "H" if hg > ag else ("A" if ag > hg else "D")
            w_total[k][o] += 1
            for b in bets:
                if bet_ok[b["id"]]:
                    w_hit[k][b["id"]][o] += 1
    return {"n": n_sims, "joint": joint, "leg": leg,
            "w_total": w_total, "w_hit": w_hit}


def _projections() -> pd.DataFrame:
    path = OUT_DIR / "tournament_projections.csv"
    return pd.read_csv(path) if path.exists() else pd.DataFrame()


def watch_fixtures(bets: list[dict], fixtures: pd.DataFrame) -> list[dict]:
    """Unplayed group games involving at least one bet team (by row index,
    which matches the score-array axis)."""
    teams_in_bets: dict[str, set] = {}
    for b in bets:
        for lg in b["legs"]:
            teams_in_bets.setdefault(lg["team"], set()).add(b["id"])
    gf = fixtures.reset_index(drop=True)
    out = []
    for j, r in enumerate(gf.itertuples(index=False)):
        if pd.notna(r.home_score):
            continue
        involved = [t for t in (r.home_team, r.away_team) if t in teams_in_bets]
        if not involved:
            continue
        out.append({"idx": j, "date": str(r.date)[:10],
                    "home": r.home_team, "away": r.away_team,
                    "involved": involved,
                    "bets": sorted(set().union(*(teams_in_bets[t] for t in involved)))})
    return out


def criticality(watch: list[dict], stats: dict, base: dict) -> list[dict]:
    """For each watched game, the biggest swing it causes to any bet it
    touches: P(bet | best result for our team) vs P(bet | worst result)."""
    n = stats["n"]
    out = []
    for k, wf in enumerate(watch):
        tot = stats["w_total"][k]
        rows = []
        for bid in wf["bets"]:
            hit = stats["w_hit"][k][bid]
            # outcome conditional bet probs
            cond = {o: (hit[o] / tot[o] if tot[o] else 0.0) for o in ("H", "D", "A")}
            # is our team home or away? best = our team wins
            team_home = wf["home"] in wf["involved"]
            win_o, lose_o = ("H", "A") if team_home else ("A", "H")
            p_if_win = cond[win_o]
            p_if_not = (hit[lose_o] + hit["D"]) / (tot[lose_o] + tot["D"]) \
                if (tot[lose_o] + tot["D"]) else 0.0
            rows.append({"bet": bid, "base": base[bid], "if_win": p_if_win,
                         "if_not": p_if_not, "swing": p_if_win - p_if_not})
        rows.sort(key=lambda d: -abs(d["swing"]))
        top = rows[0]
        out.append({**wf, "rows": rows, "max_swing": abs(top["swing"]),
                    "p_home": tot["H"] / n, "p_draw": tot["D"] / n,
                    "p_away": tot["A"] / n})
    out.sort(key=lambda d: (-d["max_swing"], d["date"]))
    return out


def compute(n_sims: int = 50_000, seed: int = 19) -> dict:
    """Structured re-pricing of every tracked bet plus the conditional-swing
    ranking of upcoming games. Shared by the text report and the web page."""
    bets = load_bets()
    sim, fixtures, pred = _build_sim(seed)
    played = int(fixtures["home_score"].notna().sum())
    watch = watch_fixtures(bets, fixtures)
    stats = simulate_reached_stats(sim, bets, n_sims, watch=watch)
    n = stats["n"]
    base = {b["id"]: stats["joint"][b["id"]] / n for b in bets}

    out_bets = []
    for b in bets:
        p = base[b["id"]]
        dec = b["returns"] / b["stake"]
        order = sorted(range(len(b["legs"])),
                       key=lambda i: stats["leg"][b["id"]][i] / n)
        legs = []
        for rank, i in enumerate(order):
            lg = b["legs"][i]
            ph = stats["leg"][b["id"]][i] / n
            legs.append({"team": _disp(lg["team"]), "desc": _leg_desc(lg),
                         "stage": STAGE_LABEL[lg["stage"]],
                         "prob": ph, "weakest": rank == 0,
                         "status": "✅" if ph >= 0.99995 else ("❌" if ph <= 0.00005 else "")})
        out_bets.append({
            "id": b["id"], "name": b["name"], "stake": b["stake"],
            "returns": b["returns"], "dec": dec, "prob": p,
            "implied": 1.0 / dec, "ev": p * dec - 1.0,
            "exp_return": b["stake"] * p * dec, "legs": legs})

    crit = criticality(watch, stats, base)
    return {"played": played, "n_sims": n, "bets": out_bets, "criticality": crit}


def report(n_sims: int = 50_000, seed: int = 19) -> str:
    bets = load_bets()
    sim, fixtures, pred = _build_sim(seed)
    played = int(fixtures["home_score"].notna().sum())
    watch = watch_fixtures(bets, fixtures)
    stats = simulate_reached_stats(sim, bets, n_sims, watch=watch)
    n = stats["n"]
    base = {b["id"]: stats["joint"][b["id"]] / n for b in bets}

    lines = [f"BET TRACKER  ({played}/72 group games in, {n_sims:,} sims)\n"]
    for b in bets:
        p = base[b["id"]]
        dec = b["returns"] / b["stake"]
        implied = 1.0 / dec
        ev = p * dec - 1.0
        odds = f"1 in {1/p:,.0f}" if p > 0 else "—"
        lines.append(f"### {b['name']}  (£{b['stake']:.0f} -> £{b['returns']:,.2f}, {dec:.0f}x)")
        lines.append(f"   Model now: {100*p:.2f}%  ({odds})   "
                     f"Bookie implied: {100*implied:.2f}%   "
                     f"EV: {ev*100:+.0f}%   "
                     f"E[return]: £{b['stake']*p*dec:,.2f}")
        legs = sorted(range(len(b["legs"])),
                      key=lambda i: stats["leg"][b["id"]][i] / n)
        for i in legs:
            lg = b["legs"][i]
            ph = stats["leg"][b["id"]][i] / n
            mark = "  <- weakest link" if i == legs[0] else ""
            lines.append(f"      {_disp(lg['team']):<14} {_leg_desc(lg):<20} "
                         f"{100*ph:5.1f}%{mark}")
        lines.append("")

    crit = criticality(watch, stats, base)
    if crit:
        lines.append("### Upcoming games, ranked by how much they swing a bet")
        for c in crit:
            who = " & ".join(_disp(t) for t in c["involved"])
            tag = "🔴" if c["max_swing"] >= 0.02 else ("🟠" if c["max_swing"] >= 0.005 else "⚪")
            lines.append(
                f"   {tag} {c['date']}  {c['home']} v {c['away']}  "
                f"({100*c['p_home']:.0f}/{100*c['p_draw']:.0f}/{100*c['p_away']:.0f})  — {who}")
            for r in c["rows"]:
                if abs(r["swing"]) < 0.002:
                    continue
                lines.append(
                    f"        {r['bet']}: {100*r['base']:.2f}% now -> "
                    f"{100*r['if_win']:.2f}% if {_disp(c['involved'][0])} win, "
                    f"{100*r['if_not']:.2f}% if not "
                    f"({r['swing']*100:+.2f} pts)")
    return "\n".join(lines)


def main(argv=None) -> None:
    ap = argparse.ArgumentParser(prog="worldcup.bets")
    ap.add_argument("--sims", type=int, default=50_000)
    ap.add_argument("--seed", type=int, default=19)
    args = ap.parse_args(argv)
    print(report(args.sims, args.seed))


if __name__ == "__main__":
    main()
