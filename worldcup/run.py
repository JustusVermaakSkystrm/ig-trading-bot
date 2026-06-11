"""CLI for the World Cup 2026 prediction engine.

    python -m worldcup.run update              # pull latest results
    python -m worldcup.run train               # validate + fit goal model
    python -m worldcup.run simulate [--sims N] # Monte Carlo + reports
    python -m worldcup.run all [--sims N]      # update + train + simulate
"""

from __future__ import annotations

import argparse
import sys
import urllib.request
from pathlib import Path

import pandas as pd

from .dataset import (DATA_DIR, RESULTS_URL, SHOOTOUTS_URL,
                      build_training_table, load_teams, merged_results)
from .model import MODEL_PATH, GoalModel, evaluate_holdout
from .report import write_outputs
from .simulator import MatchPredictor, TournamentSimulator

META_PATH = DATA_DIR / "last_validation.json"


def cmd_update() -> None:
    """Refresh data/results.csv (+ shootouts) from the upstream dataset."""
    for url, name in ((RESULTS_URL, "results.csv"), (SHOOTOUTS_URL, "shootouts.csv")):
        target = DATA_DIR / name
        before = None
        if name == "results.csv" and target.exists():
            old = pd.read_csv(target)
            before = old["home_score"].notna().sum()
        print(f"Downloading {url} ...")
        with urllib.request.urlopen(url, timeout=120) as resp:
            data = resp.read()
        if len(data) < 1_000_000 and name == "results.csv":
            print(f"  ! Download looks truncated ({len(data)} bytes), keeping old file.")
            continue
        target.write_bytes(data)
        if before is not None:
            new = pd.read_csv(target)
            print(f"  {name}: {new['home_score'].notna().sum() - before:+d} "
                  f"newly recorded results, latest date "
                  f"{new.dropna(subset=['home_score'])['date'].max()}")
    wc = world_cup_fixtures(merged_results())
    print(f"World Cup 2026: {wc['home_score'].notna().sum()}/72 group matches "
          "have results.")


def cmd_train() -> dict:
    results = merged_results()
    table, _ = build_training_table(results)
    print(f"Training table: {len(table):,} matches "
          f"({table['date'].min().date()} – {table['date'].max().date()})")
    print("Time-split validation (holdout from 2024-01-01)...")
    metrics = evaluate_holdout(table)
    print(f"  test matches : {metrics['n_test']:,}")
    print(f"  RPS          : model {metrics['model_rps']:.4f} | "
          f"Elo baseline {metrics['elo_rps']:.4f}")
    print(f"  log-loss     : model {metrics['model_logloss']:.4f} | "
          f"Elo baseline {metrics['elo_logloss']:.4f}")
    print("Fitting final model on all data ...")
    GoalModel().fit(table).save()
    import json
    META_PATH.write_text(json.dumps({"n_train": len(table), "validation": metrics}))
    print(f"Saved {MODEL_PATH}")
    return metrics


def world_cup_fixtures(results: pd.DataFrame) -> pd.DataFrame:
    """The 72 group-stage matches with a `group` column attached."""
    teams = load_teams()
    group_of = {t: g for g, members in teams["groups"].items() for t in members}
    wc = results[(results["tournament"] == "FIFA World Cup")
                 & (results["date"] >= "2026-06-01")
                 & (results["date"] <= "2026-06-30")].copy()
    wc = wc[wc["home_team"].isin(group_of)]
    wc["group"] = wc["home_team"].map(group_of)
    if len(wc) != 72:
        raise RuntimeError(f"Expected 72 group fixtures, found {len(wc)}")
    return wc.sort_values("date").reset_index(drop=True)


def cmd_simulate(n_sims: int, seed: int) -> None:
    import json
    results = merged_results()
    if not MODEL_PATH.exists():
        print("No saved model found — training first.")
        cmd_train()
    model = GoalModel.load()
    # Rebuild ratings/form state over everything played so far (fast pass).
    _, state = build_training_table(results)
    teams = load_teams()
    pred = MatchPredictor(model, state, teams["hosts"])
    fixtures = world_cup_fixtures(results)
    played = int(fixtures["home_score"].notna().sum())
    print(f"{played}/72 group matches played; simulating the rest "
          f"({n_sims:,} tournaments, seed {seed}) ...")
    sim = TournamentSimulator(pred, fixtures, seed=seed)
    res = sim.run(n_sims)

    meta = {"n_sims": n_sims,
            "data_through": str(results.dropna(subset=["home_score"])["date"].max().date()),
            "n_train": 0, "validation": None}
    if META_PATH.exists():
        saved = json.loads(META_PATH.read_text())
        meta["n_train"] = saved.get("n_train", 0)
        meta["validation"] = saved.get("validation")
    write_outputs(pred, res, fixtures, meta)
    out = Path(__file__).parent / "outputs"
    print(f"Wrote {out / 'report.md'}")
    print(f"      {out / 'match_probabilities.csv'}")
    print(f"      {out / 'tournament_projections.csv'}")
    top = res.team_table().head(5)
    print("\nTitle favourites:")
    for _, r in top.iterrows():
        print(f"  {r['team']:<15} {100 * r['p_champion']:5.1f}%")


def main(argv=None) -> None:
    ap = argparse.ArgumentParser(prog="worldcup")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("update")
    sub.add_parser("train")
    for name in ("simulate", "all"):
        p = sub.add_parser(name)
        p.add_argument("--sims", type=int, default=100_000)
        p.add_argument("--seed", type=int, default=42)
    args = ap.parse_args(argv)

    if args.cmd == "update":
        cmd_update()
    elif args.cmd == "train":
        cmd_train()
    elif args.cmd == "simulate":
        cmd_simulate(args.sims, args.seed)
    elif args.cmd == "all":
        cmd_update()
        cmd_train()
        cmd_simulate(args.sims, args.seed)


if __name__ == "__main__":
    main()
