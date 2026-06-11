# World Cup 2026 — ML Prediction Engine

A machine-learning prediction engine for the 2026 FIFA World Cup (USA /
Canada / Mexico, 48 teams). Inspired by the two-step methodology described in
[The Conversation's "We ran 100,000 computer simulations of the World
Cup"](https://theconversation.com/we-ran-100-000-computer-simulations-of-the-world-cup-and-the-winner-will-be-284629):
first estimate team strengths, then let a machine-learning model turn those
strengths into goal-scoring rates ("a pair of loaded dice"), and Monte Carlo
simulate the entire tournament.

## What it produces (`outputs/`)

| File | Contents |
|------|----------|
| `report.md` | The main readable report: title favourites, outcome probabilities for upcoming matches, projected group standings, and the most likely bracket from the round of 32 through the final. |
| `match_probabilities.csv` | Win/draw/loss probabilities, expected goals and most likely score for all 72 group matches. |
| `tournament_projections.csv` | Per team: expected points, P(win group / runner-up / best-third), and P(reaching R32, R16, QF, SF, final, title). |
| `archive/report_YYYY-MM-DD.md` | Snapshot of each report by data date, so prediction drift is auditable. |

## How it works

1. **Data** — 49k+ international results since 1872
   ([martj42/international_results](https://github.com/martj42/international_results)),
   which is updated upstream as 2026 World Cup matches finish.
2. **Strength estimation** — World-Football-Elo ratings (importance-scaled K,
   goal-difference multiplier, home advantage) plus 10-match rolling form,
   computed in a single chronological pass with no lookahead leakage
   (`ratings.py`, `dataset.py`).
3. **ML goal model** — two gradient-boosted regressors with Poisson loss
   (scikit-learn `HistGradientBoostingRegressor`) predict home/away goal
   rates from Elo, form, venue and match-importance features, with a 10-year
   recency half-life on training weights (`model.py`). Validated on a
   2024–2026 time-split holdout against an Elo-only baseline (the model wins
   on both ranked probability score and log-loss).
4. **Tournament simulation** — 100,000 Monte Carlo tournaments (`simulator.py`):
   played matches use real scores; remaining matches are sampled from the
   Poisson scoreline distribution. Implements the official 2026 rules:
   - group tiebreakers per Article 13 (points → head-to-head points/GD/goals
     among tied teams, reapplied to sub-ties → overall GD → goals → FIFA
     ranking, proxied by Elo; fair-play points are not modelled),
   - ranking of third-placed teams and their allocation to the official
     round-of-32 slots (FIFA's Annex C table is approximated by rank-priority
     assignment under the official slot constraints),
   - the official bracket (matches 73–104, `data/bracket.json`), venues and
     host home advantage (hosts only get the home bump in their own country),
   - knockouts: 90 minutes → extra time (⅓ scoring rate) → penalties
     (near coin-flip with a small Elo edge).

## Usage

```bash
pip install -r worldcup/requirements.txt   # pandas, numpy, scikit-learn, scipy

python -m worldcup.run all          # update data + retrain + 100k sims + reports
python -m worldcup.run update       # just pull the latest results
python -m worldcup.run train        # retrain + print holdout validation
python -m worldcup.run simulate --sims 100000 --seed 42
```

Run from the repository root (the directory containing `worldcup/`).

### Updating after each match day

`python -m worldcup.run all` re-downloads the results dataset, re-rates every
team, retrains the model and re-simulates the tournament — so probabilities
condition on everything that has actually happened (real group scores enter
the simulation as fixed results). If the upstream dataset lags, drop a row
into `data/manual_results.csv` (same columns as `results.csv`); manual rows
override the snapshot.

## Caveats

- Probabilities, not certainties: the favourite typically carries < 25%
  title probability.
- Team strength is frozen at the latest refresh; within one simulated
  tournament, ratings don't update from simulated results.
- Fair-play tiebreakers and squad-level information (injuries, transfers
  market values) are not modelled.
- The third-place allocation approximates FIFA's Annex C lookup table while
  respecting all of its hard constraints; in rare combinations the slot
  assignment (not qualification) may differ from FIFA's table.
