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
        # Project the two qualifiers as the teams most likely to finish in
        # the top two (P(win) + P(runner-up)); the more win-skewed of the
        # pair is the projected winner. A purely greedy "winner then highest
        # runner-up-prob" pick can wrongly drop a strong, win-skewed team to
        # 3rd (its runner-up-specific prob is deflated by its win prob).
        top2 = sorted(members,
                      key=lambda t: tt.loc[t, "p_win_group"] + tt.loc[t, "p_runner_up"],
                      reverse=True)[:2]
        winner = max(top2, key=lambda t: tt.loc[t, "p_win_group"])
        runner = next(t for t in top2 if t != winner)
        rest = [t for t in members if t not in (winner, runner)]
        third = max(rest, key=lambda t: tt.loc[t, "p_third"])
        fourth = next(t for t in rest if t != third)
        order = [winner, runner, third, fourth]
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
    # Advance the side more likely to win the tournament (its title
    # probability), so the projected bracket is consistent with the headline
    # "most likely champion". This matches the single-match favourite in
    # almost every tie; the two differ only in a near-even tie between teams
    # whose paths have differed (e.g. a coin-flip final), which is flagged.
    champ_p = res.team_table().set_index("team")["p_champion"]

    def resolve(home, away, p_home):
        winner = home if champ_p.get(home, 0) >= champ_p.get(away, 0) else away
        h2h = p_home if winner == home else 1 - p_home
        return winner, h2h

    for key, _title in ROUND_TITLES:
        ties = []
        for m in bracket[key]:
            home = slots.get(m["home"]) or advancers[m["home"]]
            away = slots.get(m["away"]) or advancers[m["away"]]
            p_home = _advance_prob(pred, elo, home, away, m.get("venue_country"))
            winner, h2h = resolve(home, away, p_home)
            advancers[f"W{m['match']}"] = winner
            pair_freq = res.match_pairings[m["match"]][(home, away)] / res.n
            ties.append({"match": m["match"], "date": m["date"], "venue": m["venue"],
                         "home": home, "away": away, "p_home_advance": p_home,
                         "winner": winner, "win_prob": h2h, "pairing_freq": pair_freq,
                         "confirmed": pair_freq > 0.9999, "h2h_underdog": h2h < 0.5})
        path[key] = ties

    fm = bracket["final"]
    fh, fa = advancers[fm["home"]], advancers[fm["away"]]
    p_home = _advance_prob(pred, elo, fh, fa, fm.get("venue_country"))
    winner, h2h = resolve(fh, fa, p_home)
    path["final"] = [{"match": fm["match"], "date": fm["date"], "venue": fm["venue"],
                      "home": fh, "away": fa, "p_home_advance": p_home,
                      "winner": winner, "win_prob": h2h,
                      "pairing_freq": res.match_pairings[fm["match"]][(fh, fa)] / res.n,
                      "confirmed": False, "h2h_underdog": h2h < 0.5}]
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
        name = f"{r['team']} ✅" if r['p_R32'] >= 0.9999 else r['team']
        add(f"| {i + 1} | {name} | {r['group']} | **{_pct(r['p_champion'])}** |"
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

    # ---- path to the final (SVG bracket)
    from .viz import bracket_svg
    champ = bracket_path["final"][0]["winner"]
    champ_prob = float(tt.set_index("team").loc[champ, "p_champion"])
    add("## Path to the final\n")
    n_locked = sum(t["confirmed"] for t in bracket_path["round_of_32"])
    add("The model's single most likely knockout bracket — all 32 projected "
        "round-of-32 teams and every unplayed tie, each line carrying the "
        "projected winner down to the next round until they converge on the "
        "champion. Percentages are each side's chance of advancing from that "
        "tie. **A gold-bordered box is a confirmed Round-of-32 tie** (the same "
        f"pairing in every simulation — mathematically locked): {n_locked}/16 "
        "locked so far, the rest finalise as the group stage ends on 27 June.\n")
    add('<div style="overflow-x:auto; margin:1rem 0;">')
    add(bracket_svg(bracket_path, champ, champ_prob))
    add('</div>\n')

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
    QUALIFIED = 0.9999   # reaches the knockouts in (effectively) every simulation

    def _label(team):
        return f"{team} ✅" if tt_idx.loc[team, "p_R32"] >= QUALIFIED else team

    any_qualified = (tt_idx["p_R32"] >= QUALIFIED).any()
    for g, members in groups_cfg.items():
        through = [t for t in members if tt_idx.loc[t, "p_R32"] >= QUALIFIED]
        add(f"### Group {g}\n")
        if through:
            add(f"**✅ Into the knockouts:** {', '.join(through)}\n")
        table = cur[g]
        if table["P"].sum() > 0:
            add("| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |")
            add("|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|")
            for r in table.itertuples(index=False):
                p = tt_idx.loc[r.team]
                adv = p["p_win_group"] + p["p_runner_up"] + p["p_third_advance"]
                add(f"| {_label(r.team)} | {r.P} | {r.W}-{r.D}-{r.L} | {r.GF}-{r.GA} | "
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
                add(f"| {_label(t)} | {p['exp_points']:.2f} | {_pct(p['p_win_group'])} | "
                    f"{_pct(p['p_win_group'] + p['p_runner_up'])} | {_pct(adv)} |")
        add("")
    note = "*\\*Advance = top two or one of the eight best third-placed teams.*"
    if any_qualified:
        note += ("\n\n*✅ = already reached the knockout stage — locked into the "
                 "Round of 32 in every simulation. (Reaching later rounds still "
                 "requires winning knockout games, so those stay below 100%.)*")
    add(note + "\n")

    # ---- predicted bracket
    add("## Most likely knockout bracket\n")
    n_locked = sum(t["confirmed"] for t in bracket_path["round_of_32"])
    add(f"Each tie shows the projected pairing and the side that advances — "
        "the team **more likely to win the tournament** of the two, so the "
        "bracket crowns the overall favourite. 'Win prob' is that team's chance "
        "in that single match (a **†** flags a near-even tie where the title "
        "favourite is a slight underdog in the one-off game). **🔒 marks a "
        "confirmed tie** — the same two teams in every simulation, "
        f"mathematically locked. ({n_locked}/16 Round-of-32 ties locked so far; "
        "the rest finalise as the group stage completes on 27 June.)\n")
    for key, title in ROUND_TITLES + [("final", "Final")]:
        add(f"### {title}\n")
        add("| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |")
        add("|:-----:|------|-------|-----|------------------|---------:|-------------:|")
        for t in bracket_path[key]:
            tie = f"{t['home']} v {t['away']}"
            freq = "🔒 locked" if t["confirmed"] else _pct(t["pairing_freq"])
            if t["confirmed"]:
                tie = f"🔒 {tie}"
            wp = _pct(t["win_prob"]) + ("†" if t["h2h_underdog"] else "")
            add(f"| {t['match']} | {t['date']} | {t['venue']} | "
                f"{tie} | **{t['winner']}** | {wp} | {freq} |")
        add("")
    champ = bracket_path["final"][0]["winner"]
    add(f"**Projected champion: {champ}** "
        f"(overall title probability {_pct(tt.set_index('team').loc[champ, 'p_champion'])}). "
        "The bracket advances the team more likely to go all the way in each "
        "tie, so the champion here matches the title favourite at the top of "
        "the page.\n")
    if any(t["h2h_underdog"] for k in (*[r[0] for r in ROUND_TITLES], "final")
           for t in bracket_path[k]):
        add("*† The title favourite reaches this tie via an easier path, so it "
            "wins the tournament most often even though this specific one-off "
            "match is a near coin-flip the other side shades.*\n")

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

    # ---- model scorecard (kept at the bottom: a running accuracy record)
    sc = meta.get("scorecard")
    if sc:
        add("\n## Model scorecard\n")
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
        bm = sc.get("benchmark")
        if bm:
            gap = bm["model_logloss"] - bm["market_logloss"]
            if abs(gap) < 0.05:
                vs_mkt = "essentially level with the market"
            elif gap < 0:
                vs_mkt = "ahead of the market"
            else:
                vs_mkt = "behind the market"
            add(f"\n**Calibration vs benchmarks** (the {bm['n']} graded games "
                "with bookmaker prices on file) — log-loss, lower is better. "
                "This is the honest test: is the model bad, or were the games "
                "hard for everyone?\n")
            add("| Forecaster | Log-loss |")
            add("|------------|---------:|")
            add(f"| **This model** | **{bm['model_logloss']:.3f}** |")
            add(f"| Sky Bet (de-vigged) | {bm['market_logloss']:.3f} |")
            add(f"| Coin-flip (33/33/33) | {bm['uniform_logloss']:.3f} |")
            both_lost = (bm["model_logloss"] > bm["uniform_logloss"]
                         and bm["market_logloss"] > bm["uniform_logloss"])
            msg = f"The model is **{vs_mkt}** ({gap:+.3f} log-loss)."
            if both_lost:
                msg += (" Note both the model **and** the bookmaker scored worse "
                        "than a coin-flip here — with this many draws and upsets, "
                        "the slate was close to unforecastable for anyone, which "
                        "is the real reason the hit-rate looks poor.")
            add("\n" + msg + "\n")
        add("\n*Predictions are frozen at the last run before each result "
            "arrives, then graded — the scorecard never grades a model that "
            "has already seen the answer.*\n")
    return "\n".join(L) + "\n"
