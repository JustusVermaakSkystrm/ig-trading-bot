# FIFA World Cup 2026 — ML Prediction Report

*Generated 2026-06-15 · data through **2026-06-14** · 50,000 Monte Carlo simulations · 11/72 group matches played*

Probabilities come from a gradient-boosted Poisson goal model (Elo strength + rolling form + venue/importance features) trained on 30,783 internationals, simulated through the official 2026 bracket and tiebreaker rules.

*Rolling validation (7,966 matches, 2018–2026): RPS 0.1687 vs Elo-baseline 0.1711; log-loss 0.8652 vs 0.8809.*

## Model scorecard

**4 of 11 match outcomes called correctly** (the model's own probabilities expected ≈6.2 of 11) · exact scoreline predicted 1/11 · average probability placed on what actually happened: **39.9%** (33.3% = guessing).

| Match | Model said | Likely score | Actual | Outcome | Score |
|-------|-----------|:---:|:---:|:---:|:---:|
| Mexico v South Africa | Mexico win (84.1%) | 2-0 | 2-0 | ✅ | ✅ |
| South Korea v Czech Republic | South Korea win (46.3%) | 1-1 | 2-1 | ✅ | — |
| Canada v Bosnia and Herzegovina | Canada win (75.0%) | 2-0 | 1-1 | ❌ | — |
| United States v Paraguay | Paraguay win (36.6%) | 1-1 | 4-1 | ❌ | — |
| Qatar v Switzerland | Switzerland win (73.8%) | 0-2 | 1-1 | ❌ | — |
| Brazil v Morocco | Brazil win (44.6%) | 1-0 | 1-1 | ❌ | — |
| Haiti v Scotland | Scotland win (46.6%) | 1-1 | 0-1 | ✅ | — |
| Australia v Turkey | Turkey win (45.8%) | 1-1 | 2-0 | ❌ | — |
| Netherlands v Japan | Netherlands win (36.1%) | 1-1 | 2-2 | ❌ | — |
| Germany v Curaçao | Germany win (84.5%) | 2-0 | 7-1 | ✅ | — |
| Ivory Coast v Ecuador | Ecuador win (48.2%) | 1-1 | 1-0 | ❌ | — |

*Predictions are frozen at the last run before each result arrives, then graded — the scorecard never grades a model that has already seen the answer.*

## Title favourites

| # | Team | Group | Champion | Δ vs 2026-06-14 | Final | Semi-final | Quarter-final | Rd of 16 |
|---|------|:-----:|---------:|-------:|------:|-----------:|--------------:|---------:|
| 1 | Spain | H | **19.7%** | -1.5 | 29.5% | 41.2% | 53.7% | 72.3% |
| 2 | Argentina | J | **18.0%** | +2.1 | 27.9% | 39.5% | 52.3% | 67.1% |
| 3 | England | L | **8.8%** | +1.3 | 15.3% | 26.4% | 40.9% | 69.9% |
| 4 | France | I | **7.2%** | +0.4 | 13.4% | 26.8% | 45.5% | 66.0% |
| 5 | Brazil | C | **6.5%** | +1.1 | 12.5% | 24.5% | 40.2% | 62.2% |
| 6 | Colombia | K | **4.3%** | -0.7 | 9.1% | 16.5% | 30.9% | 57.5% |
| 7 | Portugal | K | **4.2%** | -0.3 | 9.1% | 16.8% | 32.7% | 60.7% |
| 8 | Mexico | A | **3.7%** | -0.3 | 8.7% | 20.5% | 38.7% | 67.4% |
| 9 | Japan | F | **2.7%** | -0.1 | 6.4% | 14.2% | 27.5% | 46.8% |
| 10 | Belgium | G | **2.7%** | +0.1 | 6.9% | 13.1% | 29.6% | 56.1% |
| 11 | Netherlands | F | **2.4%** | -0.2 | 5.8% | 14.1% | 26.9% | 46.6% |
| 12 | Morocco | C | **2.0%** | – | 5.1% | 11.8% | 25.1% | 46.4% |
| 13 | Uruguay | H | **1.9%** | +0.2 | 4.9% | 9.9% | 20.3% | 38.5% |
| 14 | Norway | I | **1.8%** | – | 4.4% | 10.9% | 25.8% | 47.3% |
| 15 | Germany | E | **1.8%** | -0.5 | 4.4% | 11.1% | 25.1% | 53.2% |

## Biggest movers since last run (data through 2026-06-14)

| Team | Δ Champion | Δ Rd of 16 | Champion now |
|------|----------:|-----------:|-------------:|
| Argentina | +2.1 | +0.1 | 18.0% |
| England | +1.3 | +3.4 | 8.8% |
| Brazil | +1.1 | +2.6 | 6.5% |
| France | +0.4 | +0.5 | 7.2% |
| Germany | -0.5 | -1.9 | 1.8% |
| Colombia | -0.7 | -0.7 | 4.3% |
| Spain | -1.5 | -2.5 | 19.7% |
| Ecuador | -1.6 | -11.7 | 1.2% |

*Δ values in probability points. Full run-by-run series in `outputs/history.csv`.*

## Upcoming group matches — outcome probabilities

*(next match days; full list for all 72 group games in `match_probabilities.csv`)*

| Date | Grp | Match | Home win | Draw | Away win | xG | Likely score |
|------|:---:|-------|---------:|-----:|---------:|----|:----:|
| 2026-06-14 | F | Sweden v Tunisia | **44.3%** | 27.4% | 28.2% | 1.46–1.11 | 1-1 |
| 2026-06-15 | G | Belgium v Egypt | **57.9%** | 24.3% | 17.8% | 1.78–0.89 | 1-0 |
| 2026-06-15 | G | Iran v New Zealand | **49.7%** | 27.3% | 23.0% | 1.51–0.94 | 1-1 |
| 2026-06-15 | H | Spain v Cape Verde | **91.1%** | 6.7% | 2.2% | 3.60–0.52 | 3-0 |
| 2026-06-15 | H | Saudi Arabia v Uruguay | 12.9% | 23.5% | **63.6%** | 0.67–1.78 | 0-1 |
| 2026-06-16 | J | Austria v Jordan | **50.0%** | 27.0% | 23.0% | 1.54–0.96 | 1-1 |
| 2026-06-16 | J | Argentina v Algeria | **67.8%** | 21.5% | 10.7% | 1.92–0.62 | 1-0 |
| 2026-06-16 | I | France v Senegal | **55.3%** | 26.0% | 18.7% | 1.62–0.84 | 1-0 |
| 2026-06-16 | I | Iraq v Norway | 13.4% | 24.1% | **62.5%** | 0.67–1.74 | 0-1 |
| 2026-06-17 | K | Portugal v DR Congo | **67.9%** | 20.9% | 11.2% | 2.00–0.68 | 2-0 |
| 2026-06-17 | K | Uzbekistan v Colombia | 17.9% | 26.3% | **55.8%** | 0.79–1.59 | 0-1 |
| 2026-06-17 | L | England v Croatia | **58.8%** | 24.2% | 17.0% | 1.78–0.85 | 1-0 |
| 2026-06-17 | L | Ghana v Panama | 20.3% | 25.1% | **54.6%** | 0.95–1.71 | 1-1 |

## Group projections

### Group A

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Mexico | 1 | 1-0-0 | 2-0 | **3** | 7.32 | 68.5% | 95.9% | 99.6% |
| South Korea | 1 | 1-0-0 | 2-1 | **3** | 6.09 | 29.9% | 89.6% | 96.0% |
| Czech Republic | 1 | 0-0-1 | 1-2 | **0** | 2.31 | 1.4% | 8.4% | 45.9% |
| South Africa | 1 | 0-0-1 | 0-2 | **0** | 1.43 | 0.3% | 6.1% | 16.9% |

### Group B

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Bosnia and Herzegovina | 1 | 0-1-0 | 1-1 | **1** | 3.11 | 8.4% | 26.5% | 54.5% |
| Canada | 1 | 0-1-0 | 1-1 | **1** | 4.97 | 49.1% | 80.9% | 90.6% |
| Qatar | 1 | 0-1-0 | 1-1 | **1** | 2.50 | 4.5% | 17.2% | 36.9% |
| Switzerland | 1 | 0-1-0 | 1-1 | **1** | 4.46 | 38.1% | 75.4% | 84.0% |

### Group C

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Scotland | 1 | 1-0-0 | 1-0 | **3** | 4.86 | 22.3% | 50.4% | 87.2% |
| Brazil | 1 | 0-1-0 | 1-1 | **1** | 5.52 | 48.4% | 80.2% | 95.4% |
| Morocco | 1 | 0-1-0 | 1-1 | **1** | 4.98 | 28.9% | 67.3% | 89.5% |
| Haiti | 1 | 0-0-1 | 0-1 | **0** | 0.78 | 0.4% | 2.1% | 6.3% |

### Group D

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| United States | 1 | 1-0-0 | 4-1 | **3** | 6.02 | 51.6% | 85.5% | 96.6% |
| Australia | 1 | 1-0-0 | 2-0 | **3** | 5.89 | 40.8% | 83.1% | 95.3% |
| Turkey | 1 | 0-0-1 | 0-2 | **0** | 2.56 | 4.5% | 17.1% | 41.3% |
| Paraguay | 1 | 0-0-1 | 1-4 | **0** | 2.44 | 3.1% | 14.4% | 36.0% |

### Group E

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Germany | 1 | 1-0-0 | 7-1 | **3** | 6.24 | 54.0% | 85.1% | 99.6% |
| Ivory Coast | 1 | 1-0-0 | 1-0 | **3** | 6.23 | 37.3% | 86.1% | 95.5% |
| Ecuador | 1 | 0-0-1 | 0-1 | **0** | 3.73 | 8.5% | 27.1% | 83.1% |
| Curaçao | 1 | 0-0-1 | 1-7 | **0** | 0.89 | 0.2% | 1.7% | 4.6% |

### Group F

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Japan | 1 | 0-1-0 | 2-2 | **1** | 5.00 | 37.3% | 72.1% | 88.3% |
| Netherlands | 1 | 0-1-0 | 2-2 | **1** | 5.05 | 41.3% | 73.1% | 88.8% |
| Sweden | 0 | 0-0-0 | 0-0 | **0** | 3.20 | 13.3% | 32.6% | 52.9% |
| Tunisia | 0 | 0-0-0 | 0-0 | **0** | 2.55 | 8.1% | 22.2% | 38.8% |

### Group G

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| Belgium | 5.54 | 48.0% | 75.3% | 88.0% |
| Iran | 4.47 | 27.3% | 57.5% | 75.4% |
| Egypt | 3.50 | 14.5% | 38.8% | 59.3% |
| New Zealand | 2.88 | 10.3% | 28.5% | 46.0% |

### Group H

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| Spain | 7.32 | 74.5% | 95.8% | 99.2% |
| Uruguay | 5.36 | 22.0% | 79.4% | 91.5% |
| Saudi Arabia | 2.58 | 2.8% | 17.5% | 41.6% |
| Cape Verde | 1.60 | 0.7% | 7.2% | 18.3% |

### Group I

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| France | 6.22 | 58.0% | 83.9% | 94.0% |
| Norway | 4.62 | 23.8% | 60.2% | 80.2% |
| Senegal | 3.87 | 15.3% | 43.7% | 68.1% |
| Iraq | 1.85 | 3.0% | 12.2% | 24.5% |

### Group J

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| Argentina | 6.83 | 71.8% | 91.2% | 97.1% |
| Austria | 3.85 | 13.8% | 47.8% | 67.5% |
| Algeria | 3.54 | 10.5% | 41.3% | 62.5% |
| Jordan | 2.31 | 3.9% | 19.7% | 35.0% |

### Group K

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| Portugal | 5.76 | 46.6% | 80.0% | 91.6% |
| Colombia | 5.43 | 40.4% | 75.3% | 88.5% |
| Uzbekistan | 2.91 | 7.9% | 26.3% | 47.8% |
| DR Congo | 2.38 | 5.1% | 18.3% | 35.8% |

### Group L

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| England | 6.72 | 65.6% | 89.4% | 97.1% |
| Croatia | 4.78 | 21.6% | 63.7% | 84.4% |
| Panama | 3.66 | 11.3% | 38.7% | 64.4% |
| Ghana | 1.56 | 1.4% | 8.2% | 18.8% |

*\*Advance = top two or one of the eight best third-placed teams.*

## Most likely knockout bracket

Each tie shows the most probable pairing given projected group finishes, the chance the named winner goes through **in that pairing**, and how often the exact pairing occurred across all simulations.

### Round of 32

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 73 | 2026-06-28 | SoFi Stadium, Los Angeles | South Korea v Switzerland | **Switzerland** | 62.9% | 22.2% |
| 74 | 2026-06-29 | Gillette Stadium, Boston | Germany v Scotland | **Germany** | 51.6% | 6.0% |
| 75 | 2026-06-29 | Estadio BBVA, Monterrey | Netherlands v Morocco | **Netherlands** | 54.8% | 16.0% |
| 76 | 2026-06-29 | NRG Stadium, Houston | Brazil v Japan | **Brazil** | 56.8% | 17.0% |
| 77 | 2026-06-30 | MetLife Stadium, New York/New Jersey | France v Turkey | **France** | 69.2% | 5.9% |
| 78 | 2026-06-30 | AT&T Stadium, Dallas | Ivory Coast v Norway | **Norway** | 64.3% | 17.9% |
| 79 | 2026-06-30 | Estadio Azteca, Mexico City | Mexico v Ecuador | **Mexico** | 64.9% | 17.2% |
| 80 | 2026-07-01 | Mercedes-Benz Stadium, Atlanta | England v Saudi Arabia | **England** | 86.9% | 2.7% |
| 81 | 2026-07-01 | Levi's Stadium, San Francisco Bay Area | United States v Bosnia and Herzegovina | **United States** | 86.1% | 10.2% |
| 82 | 2026-07-01 | Lumen Field, Seattle | Belgium v Czech Republic | **Belgium** | 75.9% | 15.9% |
| 83 | 2026-07-02 | BMO Field, Toronto | Colombia v Croatia | **Colombia** | 67.3% | 14.7% |
| 84 | 2026-07-02 | SoFi Stadium, Los Angeles | Spain v Austria | **Spain** | 78.6% | 25.4% |
| 85 | 2026-07-02 | BC Place, Vancouver | Canada v Senegal | **Canada** | 57.7% | 2.1% |
| 86 | 2026-07-03 | Hard Rock Stadium, Miami | Argentina v Uruguay | **Argentina** | 75.9% | 41.4% |
| 87 | 2026-07-03 | Arrowhead Stadium, Kansas City | Portugal v Panama | **Portugal** | 72.1% | 12.0% |
| 88 | 2026-07-03 | AT&T Stadium, Dallas | Australia v Iran | **Australia** | 57.0% | 12.8% |

### Round of 16

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 89 | 2026-07-04 | Lincoln Financial Field, Philadelphia | Germany v France | **France** | 74.4% | 12.5% |
| 90 | 2026-07-04 | NRG Stadium, Houston | Switzerland v Netherlands | **Netherlands** | 68.2% | 4.4% |
| 91 | 2026-07-05 | MetLife Stadium, New York/New Jersey | Brazil v Norway | **Brazil** | 57.2% | 6.8% |
| 92 | 2026-07-05 | Estadio Azteca, Mexico City | Mexico v England | **Mexico** | 53.2% | 23.4% |
| 93 | 2026-07-06 | AT&T Stadium, Dallas | Colombia v Spain | **Spain** | 70.8% | 13.0% |
| 94 | 2026-07-06 | Lumen Field, Seattle | United States v Belgium | **Belgium** | 59.0% | 11.6% |
| 95 | 2026-07-07 | Mercedes-Benz Stadium, Atlanta | Argentina v Australia | **Argentina** | 78.5% | 13.3% |
| 96 | 2026-07-07 | BC Place, Vancouver | Canada v Portugal | **Portugal** | 57.9% | 10.2% |

### Quarter-finals

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 97 | 2026-07-09 | Gillette Stadium, Boston | France v Netherlands | **Netherlands** | 50.6% | 4.0% |
| 98 | 2026-07-10 | SoFi Stadium, Los Angeles | Spain v Belgium | **Spain** | 69.4% | 8.2% |
| 99 | 2026-07-11 | Hard Rock Stadium, Miami | Brazil v Mexico | **Brazil** | 60.5% | 5.3% |
| 100 | 2026-07-11 | Arrowhead Stadium, Kansas City | Argentina v Portugal | **Argentina** | 71.5% | 8.9% |

### Semi-finals

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 101 | 2026-07-14 | AT&T Stadium, Dallas | Netherlands v Spain | **Spain** | 74.0% | 3.0% |
| 102 | 2026-07-15 | Mercedes-Benz Stadium, Atlanta | Brazil v Argentina | **Argentina** | 66.7% | 3.7% |

### Final

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 104 | 2026-07-19 | MetLife Stadium, East Rutherford | Spain v Argentina | **Spain** | 58.3% | 6.4% |

**Projected champion: Spain** (overall title probability 19.7%; the single most likely path above is itself only one of many ways the tournament can unfold).

## How to read this

- All figures are probabilities, not certainties — a 65% favourite loses about one such match in three.
- `xPts` = expected group points; `xG` = expected goals from the Poisson model.
- Predictions refresh after every match day: run `python -m worldcup.run all` to pull new results, re-rate teams, and re-simulate.
- Machine-readable outputs: `match_probabilities.csv`, `tournament_projections.csv`. Past reports in `outputs/archive/`.
