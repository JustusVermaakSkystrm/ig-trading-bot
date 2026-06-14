# FIFA World Cup 2026 — ML Prediction Report

*Generated 2026-06-14 · data through **2026-06-13** · 50,000 Monte Carlo simulations · 6/72 group matches played*

Probabilities come from a gradient-boosted Poisson goal model (Elo strength + rolling form + venue/importance features) trained on 30,778 internationals, simulated through the official 2026 bracket and tiebreaker rules.

*Rolling validation (7,966 matches, 2018–2026): RPS 0.1687 vs Elo-baseline 0.1711; log-loss 0.8652 vs 0.8809.*

## Model scorecard

**2 of 6 match outcomes called correctly** (the model's own probabilities expected ≈3.6 of 6) · exact scoreline predicted 1/6 · average probability placed on what actually happened: **38.2%** (33.3% = guessing).

| Match | Model said | Likely score | Actual | Outcome | Score |
|-------|-----------|:---:|:---:|:---:|:---:|
| Mexico v South Africa | Mexico win (84.1%) | 2-0 | 2-0 | ✅ | ✅ |
| South Korea v Czech Republic | South Korea win (46.3%) | 1-1 | 2-1 | ✅ | — |
| Canada v Bosnia and Herzegovina | Canada win (75.0%) | 2-0 | 1-1 | ❌ | — |
| United States v Paraguay | Paraguay win (36.6%) | 1-1 | 4-1 | ❌ | — |
| Qatar v Switzerland | Switzerland win (73.8%) | 0-2 | 1-1 | ❌ | — |
| Brazil v Morocco | Brazil win (44.6%) | 1-0 | 1-1 | ❌ | — |

*Predictions are frozen at the last run before each result arrives, then graded — the scorecard never grades a model that has already seen the answer.*

## Title favourites

| # | Team | Group | Champion | Δ vs 2026-06-13 | Final | Semi-final | Quarter-final | Rd of 16 |
|---|------|:-----:|---------:|-------:|------:|-----------:|--------------:|---------:|
| 1 | Spain | H | **16.7%** | -0.3 | 25.8% | 37.7% | 51.2% | 70.4% |
| 2 | Argentina | J | **16.3%** | +1.4 | 24.9% | 36.0% | 49.8% | 66.0% |
| 3 | England | L | **8.8%** | +1.3 | 15.4% | 26.7% | 42.0% | 68.1% |
| 4 | France | I | **8.0%** | +1.1 | 14.6% | 27.7% | 44.7% | 67.4% |
| 5 | Colombia | K | **5.6%** | +0.1 | 11.3% | 19.7% | 34.8% | 61.3% |
| 6 | Brazil | C | **5.4%** | -0.5 | 10.6% | 22.0% | 37.9% | 60.8% |
| 7 | Portugal | K | **4.8%** | +0.2 | 9.9% | 18.6% | 34.4% | 62.2% |
| 8 | Netherlands | F | **3.5%** | -0.2 | 7.5% | 15.6% | 29.6% | 49.8% |
| 9 | Belgium | G | **3.3%** | +0.1 | 7.8% | 14.6% | 32.5% | 59.1% |
| 10 | Mexico | A | **3.3%** | -0.3 | 7.9% | 18.3% | 36.8% | 67.8% |
| 11 | Ecuador | E | **3.1%** | -0.8 | 6.9% | 14.4% | 27.3% | 53.6% |
| 12 | Germany | E | **2.4%** | -0.7 | 5.5% | 13.2% | 27.2% | 54.6% |
| 13 | Japan | F | **2.4%** | -0.2 | 5.5% | 12.1% | 25.4% | 44.7% |
| 14 | Morocco | C | **2.3%** | +0.2 | 5.5% | 11.7% | 25.2% | 46.6% |
| 15 | Norway | I | **2.2%** | – | 5.1% | 12.0% | 26.5% | 49.3% |

## Biggest movers since last run (data through 2026-06-13)

| Team | Δ Champion | Δ Rd of 16 | Champion now |
|------|----------:|-----------:|-------------:|
| Argentina | +1.4 | +2.1 | 16.3% |
| England | +1.3 | +1.2 | 8.8% |
| France | +1.1 | +3.2 | 8.0% |
| Spain | -0.3 | -2.0 | 16.7% |
| Brazil | -0.5 | -0.7 | 5.4% |
| Germany | -0.7 | -1.3 | 2.4% |
| United States | -0.8 | -1.7 | 1.5% |
| Ecuador | -0.8 | -2.6 | 3.1% |

*Δ values in probability points. Full run-by-run series in `outputs/history.csv`.*

## Upcoming group matches — outcome probabilities

*(next match days; full list for all 72 group games in `match_probabilities.csv`)*

| Date | Grp | Match | Home win | Draw | Away win | xG | Likely score |
|------|:---:|-------|---------:|-----:|---------:|----|:----:|
| 2026-06-13 | C | Haiti v Scotland | 26.8% | 26.6% | **46.6%** | 1.12–1.55 | 1-1 |
| 2026-06-13 | D | Australia v Turkey | 25.6% | 28.6% | **45.8%** | 0.97–1.38 | 1-1 |
| 2026-06-14 | F | Sweden v Tunisia | **42.9%** | 27.2% | 29.8% | 1.46–1.18 | 1-1 |
| 2026-06-14 | F | Netherlands v Japan | **37.1%** | 28.9% | 34.0% | 1.24–1.17 | 1-1 |
| 2026-06-14 | E | Germany v Curaçao | **87.5%** | 9.4% | 3.0% | 3.06–0.47 | 3-0 |
| 2026-06-14 | E | Ivory Coast v Ecuador | 21.0% | 26.3% | **52.7%** | 0.92–1.60 | 1-1 |
| 2026-06-15 | G | Belgium v Egypt | **54.8%** | 25.2% | 20.0% | 1.70–0.93 | 1-1 |
| 2026-06-15 | G | Iran v New Zealand | **52.7%** | 26.5% | 20.7% | 1.58–0.90 | 1-0 |
| 2026-06-15 | H | Spain v Cape Verde | **84.6%** | 11.2% | 4.2% | 2.91–0.56 | 2-0 |
| 2026-06-15 | H | Saudi Arabia v Uruguay | 13.0% | 24.0% | **63.0%** | 0.65–1.74 | 0-1 |
| 2026-06-16 | J | Austria v Jordan | **53.0%** | 25.8% | 21.2% | 1.65–0.96 | 1-1 |
| 2026-06-16 | J | Argentina v Algeria | **63.8%** | 22.8% | 13.4% | 1.86–0.73 | 1-0 |
| 2026-06-16 | I | France v Senegal | **59.4%** | 24.2% | 16.4% | 1.77–0.82 | 1-0 |
| 2026-06-16 | I | Iraq v Norway | 11.9% | 21.1% | **66.9%** | 0.72–1.99 | 0-2 |

## Group projections

### Group A

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Mexico | 1 | 1-0-0 | 2-0 | **3** | 7.05 | 63.1% | 93.8% | 99.4% |
| South Korea | 1 | 1-0-0 | 2-1 | **3** | 6.21 | 34.6% | 90.2% | 96.8% |
| Czech Republic | 1 | 0-0-1 | 1-2 | **0** | 2.44 | 1.9% | 10.5% | 51.1% |
| South Africa | 1 | 0-0-1 | 0-2 | **0** | 1.41 | 0.4% | 5.4% | 16.9% |

### Group B

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Bosnia and Herzegovina | 1 | 0-1-0 | 1-1 | **1** | 3.06 | 7.3% | 24.7% | 53.8% |
| Canada | 1 | 0-1-0 | 1-1 | **1** | 5.04 | 50.3% | 82.3% | 91.6% |
| Qatar | 1 | 0-1-0 | 1-1 | **1** | 2.47 | 4.1% | 16.2% | 36.2% |
| Switzerland | 1 | 0-1-0 | 1-1 | **1** | 4.49 | 38.3% | 76.8% | 85.3% |

### Group C

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Brazil | 1 | 0-1-0 | 1-1 | **1** | 5.49 | 50.2% | 80.6% | 94.5% |
| Morocco | 1 | 0-1-0 | 1-1 | **1** | 5.03 | 32.1% | 70.5% | 90.2% |
| Haiti | 0 | 0-0-0 | 0-0 | **0** | 1.89 | 3.5% | 11.9% | 25.9% |
| Scotland | 0 | 0-0-0 | 0-0 | **0** | 3.48 | 14.2% | 37.0% | 59.7% |

### Group D

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| United States | 1 | 1-0-0 | 4-1 | **3** | 5.87 | 50.6% | 82.1% | 96.3% |
| Australia | 0 | 0-0-0 | 0-0 | **0** | 3.60 | 15.1% | 39.4% | 61.8% |
| Turkey | 0 | 0-0-0 | 0-0 | **0** | 4.77 | 30.9% | 62.3% | 79.3% |
| Paraguay | 1 | 0-0-1 | 1-4 | **0** | 2.36 | 3.3% | 16.2% | 34.8% |

### Group E

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| Germany | 6.05 | 47.6% | 82.5% | 96.1% |
| Ecuador | 5.70 | 40.2% | 77.4% | 92.8% |
| Ivory Coast | 3.62 | 11.3% | 35.1% | 64.8% |
| Curaçao | 1.32 | 0.8% | 5.0% | 14.2% |

### Group F

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| Netherlands | 5.66 | 45.9% | 77.9% | 90.3% |
| Japan | 5.34 | 38.5% | 72.8% | 87.5% |
| Sweden | 2.96 | 8.8% | 27.2% | 49.6% |
| Tunisia | 2.58 | 6.9% | 22.1% | 40.7% |

### Group G

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| Belgium | 5.70 | 50.4% | 77.6% | 89.7% |
| Iran | 4.46 | 26.1% | 57.5% | 76.4% |
| Egypt | 3.53 | 14.8% | 39.2% | 60.3% |
| New Zealand | 2.75 | 8.7% | 25.8% | 44.1% |

### Group H

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| Spain | 7.18 | 72.7% | 94.6% | 98.6% |
| Uruguay | 5.31 | 22.9% | 78.7% | 91.3% |
| Saudi Arabia | 2.57 | 3.1% | 17.9% | 42.5% |
| Cape Verde | 1.74 | 1.3% | 8.9% | 22.7% |

### Group I

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| France | 6.24 | 57.8% | 84.1% | 94.3% |
| Norway | 4.81 | 26.1% | 63.9% | 83.4% |
| Senegal | 3.72 | 13.3% | 40.1% | 66.5% |
| Iraq | 1.82 | 2.8% | 11.9% | 24.7% |

### Group J

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| Argentina | 6.68 | 68.5% | 89.6% | 96.6% |
| Austria | 4.00 | 15.9% | 50.0% | 70.6% |
| Algeria | 3.64 | 12.2% | 42.3% | 64.6% |
| Jordan | 2.22 | 3.5% | 18.1% | 33.9% |

### Group K

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| Portugal | 5.83 | 45.4% | 81.7% | 92.8% |
| Colombia | 5.76 | 44.7% | 80.7% | 92.1% |
| Uzbekistan | 2.61 | 5.5% | 20.4% | 42.3% |
| DR Congo | 2.34 | 4.4% | 17.1% | 36.3% |

### Group L

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| England | 6.64 | 64.5% | 88.8% | 96.8% |
| Croatia | 4.84 | 22.9% | 65.7% | 85.9% |
| Panama | 3.49 | 10.9% | 36.0% | 61.5% |
| Ghana | 1.72 | 1.8% | 9.6% | 22.8% |

*\*Advance = top two or one of the eight best third-placed teams.*

## Most likely knockout bracket

Each tie shows the most probable pairing given projected group finishes, the chance the named winner goes through **in that pairing**, and how often the exact pairing occurred across all simulations.

### Round of 32

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 73 | 2026-06-28 | SoFi Stadium, Los Angeles | South Korea v Switzerland | **Switzerland** | 68.6% | 21.5% |
| 74 | 2026-06-29 | Gillette Stadium, Boston | Germany v Czech Republic | **Germany** | 78.5% | 2.6% |
| 75 | 2026-06-29 | Estadio BBVA, Monterrey | Netherlands v Morocco | **Netherlands** | 54.0% | 17.6% |
| 76 | 2026-06-29 | NRG Stadium, Houston | Brazil v Japan | **Brazil** | 58.8% | 17.2% |
| 77 | 2026-06-30 | MetLife Stadium, New York/New Jersey | France v Australia | **France** | 77.5% | 5.4% |
| 78 | 2026-06-30 | AT&T Stadium, Dallas | Ecuador v Norway | **Ecuador** | 53.8% | 14.1% |
| 79 | 2026-06-30 | Estadio Azteca, Mexico City | Mexico v Scotland | **Mexico** | 74.3% | 5.3% |
| 80 | 2026-07-01 | Mercedes-Benz Stadium, Atlanta | England v Ivory Coast | **England** | 78.9% | 1.7% |
| 81 | 2026-07-01 | Levi's Stadium, San Francisco Bay Area | United States v Bosnia and Herzegovina | **United States** | 85.4% | 10.0% |
| 82 | 2026-07-01 | Lumen Field, Seattle | Belgium v Saudi Arabia | **Belgium** | 82.4% | 4.0% |
| 83 | 2026-07-02 | BMO Field, Toronto | Colombia v Croatia | **Colombia** | 65.9% | 15.4% |
| 84 | 2026-07-02 | SoFi Stadium, Los Angeles | Spain v Austria | **Spain** | 75.7% | 24.9% |
| 85 | 2026-07-02 | BC Place, Vancouver | Canada v Senegal | **Canada** | 61.6% | 2.2% |
| 86 | 2026-07-03 | Hard Rock Stadium, Miami | Argentina v Uruguay | **Argentina** | 76.1% | 38.2% |
| 87 | 2026-07-03 | Arrowhead Stadium, Kansas City | Portugal v Panama | **Portugal** | 76.4% | 11.8% |
| 88 | 2026-07-03 | AT&T Stadium, Dallas | Turkey v Iran | **Turkey** | 58.6% | 9.8% |

### Round of 16

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 89 | 2026-07-04 | Lincoln Financial Field, Philadelphia | Germany v France | **France** | 69.0% | 12.9% |
| 90 | 2026-07-04 | NRG Stadium, Houston | Switzerland v Netherlands | **Netherlands** | 69.3% | 5.9% |
| 91 | 2026-07-05 | MetLife Stadium, New York/New Jersey | Brazil v Ecuador | **Brazil** | 62.1% | 6.3% |
| 92 | 2026-07-05 | Estadio Azteca, Mexico City | Mexico v England | **England** | 55.0% | 21.0% |
| 93 | 2026-07-06 | AT&T Stadium, Dallas | Colombia v Spain | **Spain** | 73.4% | 12.6% |
| 94 | 2026-07-06 | Lumen Field, Seattle | United States v Belgium | **Belgium** | 60.6% | 12.3% |
| 95 | 2026-07-07 | Mercedes-Benz Stadium, Atlanta | Argentina v Turkey | **Argentina** | 69.5% | 9.2% |
| 96 | 2026-07-07 | BC Place, Vancouver | Canada v Portugal | **Portugal** | 56.6% | 11.1% |

### Quarter-finals

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 97 | 2026-07-09 | Gillette Stadium, Boston | France v Netherlands | **France** | 52.3% | 4.7% |
| 98 | 2026-07-10 | SoFi Stadium, Los Angeles | Spain v Belgium | **Spain** | 66.4% | 8.3% |
| 99 | 2026-07-11 | Hard Rock Stadium, Miami | Brazil v England | **England** | 64.0% | 5.5% |
| 100 | 2026-07-11 | Arrowhead Stadium, Kansas City | Argentina v Portugal | **Argentina** | 71.7% | 8.0% |

### Semi-finals

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 101 | 2026-07-14 | AT&T Stadium, Dallas | France v Spain | **Spain** | 65.1% | 5.2% |
| 102 | 2026-07-15 | Mercedes-Benz Stadium, Atlanta | England v Argentina | **Argentina** | 62.3% | 5.5% |

### Final

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 104 | 2026-07-19 | MetLife Stadium, East Rutherford | Spain v Argentina | **Spain** | 54.2% | 4.8% |

**Projected champion: Spain** (overall title probability 16.7%; the single most likely path above is itself only one of many ways the tournament can unfold).

## How to read this

- All figures are probabilities, not certainties — a 65% favourite loses about one such match in three.
- `xPts` = expected group points; `xG` = expected goals from the Poisson model.
- Predictions refresh after every match day: run `python -m worldcup.run all` to pull new results, re-rate teams, and re-simulate.
- Machine-readable outputs: `match_probabilities.csv`, `tournament_projections.csv`. Past reports in `outputs/archive/`.
