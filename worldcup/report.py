"""Readable outputs: markdown report + CSVs in worldcup/outputs/."""

from __future__ import annotations

from datetime import date
from pathlib import Path

import pandas as pd

from .model import most_likely_score, outcome_probs
from .ratings import expected_score
from .simulator import (ET_RATE_FACTOR, PENALTY_ELO_EDGE, MatchPredictor,
                        SimResults, allocate_thirds, load_bracket)

OUT_DIR = Path(__file__).parent / "outputs"

ROUND_TITLES = [("round_of_32", "Round of 32"), ("round_of_16", "Round of 16"),
                ("quarterfinals", "Quarter-finals"), ("semifinals", "Semi-finals")]


def _pct(x: float) -> str:
    return f"{100 * x:.1f}%"


def _advance_prob(pred: MatchPredictor, elo: dict, home: str, away: str,
                  venue_country: str | None) -> float:
    """Analytic P(home advances) through 90', extra time and penalties."""
    lh, la = pred.rates(home, away, venue_country)
    pw, pd_, _ = outcome_probs(lh, la, pred.rho)
    pw_et, pd_et, _ = outcome_probs(lh * ET_RATE_FACTOR, la * ET_RATE_FACTOR,
                                    pred.rho)
    p_pens = 0.5 + PENALTY_ELO_EDGE * (expected_score(elo[home], elo[away]) - 0.5)
    return pw + pd_ * (pw_et + pd_et * p_pens)


def match_probability_table(pred: MatchPredictor, fixtures: pd.DataFrame) -> pd.DataFrame:
    """Win/draw/loss probabilities for all group matches (played ones keep
    their real score for reference)."""
    rows = []
    for r in fixtures.itertuples(index=False):
        lh, la = pred.rates(r.home_team, r.away_team,
                            None if r.neutral else r.country)
        ph, pdr, pa = outcome_probs(lh, la, pred.rho)
        ms = most_likely_score(lh, la, pred.rho)
        played = not (pd.isna(r.home_score) or pd.isna(r.away_score))
        rows.append({
            "date": r.date.date() if hasattr(r.date, "date") else r.date,
            "group": r.group, "home": r.home_team, "away": r.away_team,
            "status": "played" if played else "upcoming",
            "score": f"{int(r.home_score)}-{int(r.away_score)}" if played else "",
            "p_home_win": round(ph, 4), "p_draw": round(pdr, 4),
            "p_away_win": round(pa, 4),
            "xg_home": f"{lh:.2f}", "xg_away": f"{la:.2f}",
            "most_likely_score": f"{ms[0]}-{ms[1]}",
        })
    return pd.DataFrame(rows)


def predicted_bracket(pred: MatchPredictor, res: SimResults, elo: dict) -> dict:
    """A single self-consistent most-likely tournament path.

    Group positions come from simulation frequencies; each knockout tie is
    then decided by the analytic advance probability of the projected
    pairing.
    """
    bracket = load_bracket()
    tt = res.team_table().set_index("team")
    slots: dict[str, str] = {}
    modal_thirds: list[tuple[str, str, tuple]] = []

    for g, members in res.groups.items():
        remaining = list(members)
        order = []
        for col in ("p_win_group", "p_runner_up", "p_third"):
            pick = max(remaining, key=lambda t: tt.loc[t, col])
            order.append(pick)
            remaining.remove(pick)
        order.append(remaining[0])
        slots[f"W_{g}"] = order[0]
        slots[f"RU_{g}"] = order[1]
        modal_thirds.append((g, order[2], ()))

    thirds_sorted = sorted(modal_thirds,
                           key=lambda r: tt.loc[r[1], "p_third_advance"],
                           reverse=True)[:8]
    slots.update(allocate_thirds([(g, t) for g, t, _ in thirds_sorted],
                                 bracket["third_place_slots"]))

    path = {}
    advancers: dict[str, str] = {}
    for key, _title in ROUND_TITLES:
        ties = []
        for m in bracket[key]:
            home = slots.get(m["home"]) or advancers[m["home"]]
            away = slots.get(m["away"]) or advancers[m["away"]]
            p_home = _advance_prob(pred, elo, home, away, m.get("venue_country"))
            winner = home if p_home >= 0.5 else away
            advancers[f"W{m['match']}"] = winner
            pair_freq = res.match_pairings[m["match"]][(home, away)] / res.n
            ties.append({"match": m["match"], "date": m["date"], "venue": m["venue"],
                         "home": home, "away": away, "p_home_advance": p_home,
                         "winner": winner, "pairing_freq": pair_freq})
        path[key] = ties

    fm = bracket["final"]
    fh, fa = advancers[fm["home"]], advancers[fm["away"]]
    p_home = _advance_prob(pred, elo, fh, fa, fm.get("venue_country"))
    path["final"] = [{"match": fm["match"], "date": fm["date"], "venue": fm["venue"],
                      "home": fh, "away": fa, "p_home_advance": p_home,
                      "winner": fh if p_home >= 0.5 else fa,
                      "pairing_freq": res.match_pairings[fm["match"]][(fh, fa)] / res.n}]
    return path


def current_group_tables(fixtures: pd.DataFrame, groups: dict) -> dict[str, pd.DataFrame]:
    """Actual standings from played matches only (display order: pts, GD, GF)."""
    tables = {}
    played = fixtures.dropna(subset=["home_score", "away_score"])
    for g, members in groups.items():
        s = {t: {"P": 0, "W": 0, "D": 0, "L": 0, "GF": 0, "GA": 0, "Pts": 0}
             for t in members}
        for r in played[played["group"] == g].itertuples(index=False):
            hg, ag = int(r.home_score), int(r.away_score)
            for team, gf, ga in ((r.home_team, hg, ag), (r.away_team, ag, hg)):
                s[team]["P"] += 1
                s[team]["GF"] += gf
                s[team]["GA"] += ga
                s[team]["W"] += gf > ga
                s[team]["D"] += gf == ga
                s[team]["L"] += gf < ga
                s[team]["Pts"] += 3 if gf > ga else (1 if gf == ga else 0)
        df = pd.DataFrame([{"team": t, **v, "GD": v["GF"] - v["GA"]}
                           for t, v in s.items()])
        tables[g] = df.sort_values(["Pts", "GD", "GF", "team"],
                                   ascending=[False, False, False, True]
                                   ).reset_index(drop=True)
    return tables


# ----------------------------------------------------------------- writing

def write_outputs(pred: MatchPredictor, res: SimResults, fixtures: pd.DataFrame,
                  meta: dict) -> None:
    OUT_DIR.mkdir(exist_ok=True)
    elo = {t: pred.state.elo.get(t) for g in res.groups.values() for t in g}

    matches = match_probability_table(pred, fixtures)
    matches.to_csv(OUT_DIR / "match_probabilities.csv", index=False)

    from .scorecard import summary, update_log
    meta["scorecard"] = summary(update_log(matches))

    tt = res.team_table()
    prev = _load_previous_projections()
    deltas = _compute_deltas(tt, prev)

    proj = tt.copy()
    proj.insert(0, "data_through", meta["data_through"])
    proj.insert(1, "n_sims", meta["n_sims"])
    proj.round(4).to_csv(OUT_DIR / "tournament_projections.csv", index=False)
    _append_history(proj)

    bracket_path = predicted_bracket(pred, res, elo)
    md = _render_markdown(pred, res, fixtures, tt, bracket_path, elo, meta, deltas)
    (OUT_DIR / "report.md").write_text(md)

    archive = OUT_DIR / "archive"
    archive.mkdir(exist_ok=True)
    (archive / f"report_{meta['data_through']}.md").write_text(md)

    try:
        from .site import build_site
        build_site()
    except ImportError:  # markdown package not installed; site is optional
        pass


def _load_previous_projections() -> pd.DataFrame | None:
    path = OUT_DIR / "tournament_projections.csv"
    if not path.exists():
        return None
    return pd.read_csv(path)


def _append_history(proj: pd.DataFrame) -> None:
    """One row per team per run, for tracking prediction drift over time."""
    path = OUT_DIR / "history.csv"
    proj = proj.copy()
    proj.insert(0, "run_at", pd.Timestamp.now().isoformat(timespec="seconds"))
    proj.round(4).to_csv(path, mode="a", header=not path.exists(), index=False)


DELTA_COLS = ["p_champion", "p_final", "p_SF", "p_QF", "p_R16", "p_R32",
              "p_win_group", "exp_points"]


def _compute_deltas(tt: pd.DataFrame, prev: pd.DataFrame | None) -> dict | None:
    """Per-team change vs the previous run, in probability points."""
    if prev is None or "team" not in prev.columns:
        return None
    merged = tt.merge(prev[["team"] + [c for c in DELTA_COLS if c in prev.columns]],
                      on="team", how="left", suffixes=("", "_prev"))
    delta = {}
    for c in DELTA_COLS:
        if f"{c}_prev" in merged.columns:
            delta[c] = dict(zip(merged["team"], merged[c] - merged[f"{c}_prev"]))
    label = str(prev["data_through"].iloc[0]) if "data_through" in prev.columns \
        else "previous run"
    return {"deltas": delta, "prev_label": label}


def _fmt_delta(x: float, threshold: float = 0.0005) -> str:
    if x != x:  # NaN: team absent from previous run
        return "new"
    if abs(x) < threshold:
        return "–"
    return f"{100 * x:+.1f}"


def _render_markdown(pred, res: SimResults, fixtures, tt, bracket_path, elo,
                     meta, deltas: dict | None = None) -> str:
    L = []
    add = L.append
    n_played = int(fixtures["home_score"].notna().sum())
    add("# FIFA World Cup 2026 — ML Prediction Report\n")
    add(f"*Generated {date.today().isoformat()} · data through "
        f"**{meta['data_through']}** · {meta['n_sims']:,} Monte Carlo simulations · "
        f"{n_played}/72 group matches played*\n")
    add("Probabilities come from a gradient-boosted Poisson goal model "
        "(Elo strength + rolling form + venue/importance features) trained on "
        f"{meta['n_train']:,} internationals, simulated through the official "
        "2026 bracket and tiebreaker rules.\n")
    if meta.get("validation"):
        v = meta["validation"]
        add(f"*Rolling validation ({v['n_test']:,} matches, 2018–2026): "
            f"RPS {v['model_rps']:.4f} vs Elo-baseline {v['elo_rps']:.4f}; "
            f"log-loss {v['model_logloss']:.4f} vs {v['elo_logloss']:.4f}.*\n")

    # ---- model scorecard
    sc = meta.get("scorecard")
    if sc:
        add("## Model scorecard\n")
        add(f"**{sc['hits']} of {sc['n']} match outcomes called correctly** "
            f"(the model's own probabilities expected ≈{sc['expected_hits']:.1f} "
            f"of {sc['n']}) · exact scoreline predicted {sc['score_hits']}/{sc['n']} "
            f"· average probability placed on what actually happened: "
            f"**{_pct(sc['mean_p_actual'])}** (33.3% = guessing).\n")
        add("| Match | Model said | Likely score | Actual | Outcome | Score |")
        add("|-------|-----------|:---:|:---:|:---:|:---:|")
        for r in sc["rows"].itertuples(index=False):
            probs = {f"{r.home} win": float(r.p_home), "Draw": float(r.p_draw),
                     f"{r.away} win": float(r.p_away)}
            pick = max(probs, key=probs.get)
            add(f"| {r.home} v {r.away} | {pick} ({_pct(probs[pick])}) | "
                f"{r.pred_score} | {int(r.home_score)}-{int(r.away_score)} | "
                f"{'✅' if r.hit else '❌'} | {'✅' if r.score_hit else '—'} |")
        add("\n*Predictions are frozen at the last run before each result "
            "arrives, then graded — the scorecard never grades a model that "
            "has already seen the answer.*\n")

    # ---- title favourites
    add("## Title favourites\n")
    dch = deltas["deltas"].get("p_champion", {}) if deltas else {}
    dcol = f" Δ vs {deltas['prev_label']} |" if deltas else ""
    add(f"| # | Team | Group | Champion |{dcol} Final | Semi-final | "
        "Quarter-final | Rd of 16 |")
    add("|---|------|:-----:|---------:|" + ("-------:|" if deltas else "")
        + "------:|-----------:|--------------:|---------:|")
    for i, r in tt.head(15).iterrows():
        dcell = f" {_fmt_delta(dch.get(r['team'], float('nan')))} |" if deltas else ""
        add(f"| {i + 1} | {r['team']} | {r['group']} | **{_pct(r['p_champion'])}** |"
            f"{dcell} {_pct(r['p_final'])} | {_pct(r['p_SF'])} | {_pct(r['p_QF'])} | "
            f"{_pct(r['p_R16'])} |")
    add("")

    # ---- movers since last run
    if deltas and deltas["deltas"].get("p_champion"):
        add(f"## Biggest movers since last run (data through {deltas['prev_label']})\n")
        ch = pd.Series(deltas["deltas"]["p_champion"]).dropna()
        r16 = pd.Series(deltas["deltas"].get("p_R16", {})).dropna()
        movers = (ch.abs().sort_values(ascending=False).head(8)).index
        add("| Team | Δ Champion | Δ Rd of 16 | Champion now |")
        add("|------|----------:|-----------:|-------------:|")
        tt_idx_ = tt.set_index("team")
        for t in sorted(movers, key=lambda t: ch[t], reverse=True):
            add(f"| {t} | {_fmt_delta(ch[t])} | "
                f"{_fmt_delta(r16.get(t, float('nan')))} | "
                f"{_pct(tt_idx_.loc[t, 'p_champion'])} |")
        add("\n*Δ values in probability points. Full run-by-run series in "
            "`outputs/history.csv`.*\n")

    # ---- upcoming matches
    add("## Upcoming group matches — outcome probabilities\n")
    matches = match_probability_table(pred, fixtures)
    upcoming = matches[matches["status"] == "upcoming"]
    horizon = upcoming["date"].sort_values().unique()[:4]
    add("*(next match days; full list for all 72 group games in "
        "`match_probabilities.csv`)*\n")
    add("| Date | Grp | Match | Home win | Draw | Away win | xG | Likely score |")
    add("|------|:---:|-------|---------:|-----:|---------:|----|:----:|")
    for r in upcoming[upcoming["date"].isin(horizon)].itertuples(index=False):
        probs = [r.p_home_win, r.p_draw, r.p_away_win]
        cells = [_pct(p) for p in probs]
        best = probs.index(max(probs))
        cells[best] = f"**{cells[best]}**"   # highlight the likeliest outcome
        add(f"| {r.date} | {r.group} | {r.home} v {r.away} | "
            f"{cells[0]} | {cells[1]} | {cells[2]} | "
            f"{r.xg_home}–{r.xg_away} | {r.most_likely_score} |")
    add("")

    # ---- groups
    add("## Group projections\n")
    from .dataset import load_teams
    groups_cfg = load_teams()["groups"]
    cur = current_group_tables(fixtures, groups_cfg)
    tt_idx = tt.set_index("team")
    for g, members in groups_cfg.items():
        add(f"### Group {g}\n")
        table = cur[g]
        if table["P"].sum() > 0:
            add("| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |")
            add("|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|")
            for r in table.itertuples(index=False):
                p = tt_idx.loc[r.team]
                adv = p["p_win_group"] + p["p_runner_up"] + p["p_third_advance"]
                add(f"| {r.team} | {r.P} | {r.W}-{r.D}-{r.L} | {r.GF}-{r.GA} | "
                    f"**{r.Pts}** | {p['exp_points']:.2f} | {_pct(p['p_win_group'])} | "
                    f"{_pct(p['p_win_group'] + p['p_runner_up'])} | {_pct(adv)} |")
        else:
            add("| Team | xPts | Win grp | Top 2 | Advance* |")
            add("|------|-----:|--------:|------:|--------:|")
            order = sorted(members, key=lambda t: tt_idx.loc[t, "exp_points"],
                           reverse=True)
            for t in order:
                p = tt_idx.loc[t]
                adv = p["p_win_group"] + p["p_runner_up"] + p["p_third_advance"]
                add(f"| {t} | {p['exp_points']:.2f} | {_pct(p['p_win_group'])} | "
                    f"{_pct(p['p_win_group'] + p['p_runner_up'])} | {_pct(adv)} |")
        add("")
    add("*\\*Advance = top two or one of the eight best third-placed teams.*\n")

    # ---- predicted bracket
    add("## Most likely knockout bracket\n")
    add("Each tie shows the most probable pairing given projected group "
        "finishes, the chance the named winner goes through **in that "
        "pairing**, and how often the exact pairing occurred across all "
        "simulations.\n")
    for key, title in ROUND_TITLES + [("final", "Final")]:
        add(f"### {title}\n")
        add("| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |")
        add("|:-----:|------|-------|-----|------------------|---------:|-------------:|")
        for t in bracket_path[key]:
            p = t["p_home_advance"] if t["winner"] == t["home"] else 1 - t["p_home_advance"]
            add(f"| {t['match']} | {t['date']} | {t['venue']} | "
                f"{t['home']} v {t['away']} | **{t['winner']}** | {_pct(p)} | "
                f"{_pct(t['pairing_freq'])} |")
        add("")
    champ = bracket_path["final"][0]["winner"]
    add(f"**Projected champion: {champ}** "
        f"(overall title probability {_pct(tt.set_index('team').loc[champ, 'p_champion'])}; "
        "the single most likely path above is itself only one of many ways "
        "the tournament can unfold).\n")

    add("## How to read this\n")
    add("- All figures are probabilities, not certainties — a 65% favourite "
        "loses about one such match in three.")
    add("- `xPts` = expected group points; `xG` = expected goals from the "
        "Poisson model.")
    add("- Predictions refresh after every match day: run "
        "`python -m worldcup.run all` to pull new results, re-rate teams, "
        "and re-simulate.")
    add("- Machine-readable outputs: `match_probabilities.csv`, "
        "`tournament_projections.csv`. Past reports in `outputs/archive/`.")
    return "\n".join(L) + "\n"
