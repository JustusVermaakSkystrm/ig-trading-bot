"""Compare model probabilities with bookmaker odds to find value bets.

Reads outputs/tournament_projections.csv (model) and data/skybet_odds.csv
(manually mined bookmaker prices) and ranks outright-winner bets by
expected value and Kelly fraction.

    python -m worldcup.value_bets
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

BASE = Path(__file__).parent
ODDS_PATH = BASE / "data" / "skybet_odds.csv"
PROJ_PATH = BASE / "outputs" / "tournament_projections.csv"


def value_table() -> pd.DataFrame:
    odds = pd.read_csv(ODDS_PATH)
    proj = pd.read_csv(PROJ_PATH)[["team", "p_champion"]]
    df = odds.merge(proj, on="team", how="left")
    d = df["decimal_odds"]
    p = df["p_champion"]
    df["implied_prob"] = 1.0 / d
    df["model_edge"] = p - df["implied_prob"]
    df["ev_per_unit"] = p * d - 1.0
    # Kelly fraction for a binary bet at decimal odds d: (d*p - 1) / (d - 1)
    df["kelly"] = ((d * p - 1.0) / (d - 1.0)).clip(lower=0.0)
    return df.sort_values("kelly", ascending=False).reset_index(drop=True)


def main() -> None:
    df = value_table()
    out = df.copy()
    for col in ("p_champion", "implied_prob", "model_edge", "ev_per_unit", "kelly"):
        out[col] = (100 * out[col]).round(2)
    cols = ["team", "fractional_odds", "p_champion", "implied_prob",
            "model_edge", "ev_per_unit", "kelly", "confirmed_skybet"]
    print(out[cols].rename(columns={
        "p_champion": "model_%", "implied_prob": "implied_%",
        "model_edge": "edge_pp", "ev_per_unit": "EV_%", "kelly": "kelly_%",
    }).to_string(index=False))
    out_path = BASE / "outputs" / "value_bets.csv"
    df.round(4).to_csv(out_path, index=False)
    print(f"\nWrote {out_path}")


if __name__ == "__main__":
    main()
