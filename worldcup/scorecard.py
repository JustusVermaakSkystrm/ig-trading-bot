"""Model accuracy tracking: freeze pre-match predictions, grade them later.

Every run upserts the current outcome probabilities for each *unplayed*
match into outputs/prediction_log.csv. Once a match's result is validated,
its row is locked with whatever the model said on the last run before the
result arrived — so the scorecard always grades genuine pre-match
predictions, never a model that has already trained on the outcome.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

LOG_PATH = Path(__file__).parent / "outputs" / "prediction_log.csv"
KEY = ["date", "home", "away"]
COLS = KEY + ["p_home", "p_draw", "p_away", "pred_score", "locked",
              "home_score", "away_score", "actual_outcome", "hit",
              "score_hit", "p_actual"]


def _load() -> pd.DataFrame:
    if LOG_PATH.exists():
        df = pd.read_csv(LOG_PATH, dtype={"date": str, "pred_score": str})
    else:
        df = pd.DataFrame(columns=COLS)
    df["locked"] = df["locked"].map(lambda x: bool(x) and str(x) != "False") \
        if len(df) else df.get("locked", pd.Series(dtype=bool))
    # Mixed-type columns must be object dtype or row-wise grading
    # assignments fail on all-NaN float64 columns.
    for c in ("pred_score", "actual_outcome", "hit", "score_hit", "locked"):
        df[c] = df[c].astype(object)
    return df


def update_log(match_table: pd.DataFrame) -> pd.DataFrame:
    """match_table: output of report.match_probability_table (validated
    scores only). Refreshes pre-match rows and locks newly finished ones."""
    log = _load().set_index(KEY)
    for r in match_table.itertuples(index=False):
        key = (str(r.date), r.home, r.away)
        if r.status == "upcoming":
            if key in log.index and bool(log.loc[key, "locked"]):
                continue   # already graded; never overwrite
            log.loc[key, ["p_home", "p_draw", "p_away", "pred_score", "locked"]] = \
                [r.p_home_win, r.p_draw, r.p_away_win, r.most_likely_score, False]
        else:
            hs, as_ = (int(x) for x in r.score.split("-"))
            outcome = "home" if hs > as_ else ("away" if hs < as_ else "draw")
            if key not in log.index:
                # No pre-match prediction stored (model may have seen the
                # result in training) — record but flag as retrospective.
                log.loc[key, ["p_home", "p_draw", "p_away", "pred_score"]] = \
                    [r.p_home_win, r.p_draw, r.p_away_win,
                     r.most_likely_score + " (retro)"]
            if bool(log.loc[key, "locked"]):
                continue
            probs = {"home": float(log.loc[key, "p_home"]),
                     "draw": float(log.loc[key, "p_draw"]),
                     "away": float(log.loc[key, "p_away"])}
            picked = max(probs, key=probs.get)
            log.loc[key, ["locked", "home_score", "away_score",
                          "actual_outcome", "hit", "score_hit", "p_actual"]] = \
                [True, hs, as_, outcome, picked == outcome,
                 str(log.loc[key, "pred_score"]) == f"{hs}-{as_}",
                 probs[outcome]]
    out = log.reset_index()
    out.to_csv(LOG_PATH, index=False)
    return out


def summary(log: pd.DataFrame) -> dict | None:
    graded = log[log["locked"] == True]  # noqa: E712
    if graded.empty:
        return None
    probs = graded[["p_home", "p_draw", "p_away"]].astype(float)
    return {
        "n": len(graded),
        "hits": int(graded["hit"].astype(bool).sum()),
        "expected_hits": float(probs.max(axis=1).sum()),
        "mean_p_actual": float(graded["p_actual"].astype(float).mean()),
        "score_hits": int(graded["score_hit"].astype(bool).sum()),
        "rows": graded.sort_values("date"),
    }
