# FIFA World Cup 2026 — ML Prediction Report

*Generated 2026-06-14 · data through **2026-06-13** · 50,000 Monte Carlo simulations · 8/72 group matches played*

Probabilities come from a gradient-boosted Poisson goal model (Elo strength + rolling form + venue/importance features) trained on 30,780 internationals, simulated through the official 2026 bracket and tiebreaker rules.

*Rolling validation (7,966 matches, 2018–2026): RPS 0.1687 vs Elo-baseline 0.1711; log-loss 0.8652 vs 0.8809.*

## Model scorecard

**3 of 8 match outcomes called correctly** (the model's own probabilities expected ≈4.5 of 8) · exact scoreline predicted 1/8 · average probability placed on what actually happened: **37.7%** (33.3% = guessing).

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

*Predictions are frozen at the last run before each result arrives, then graded — the scorecard never grades a model that has already seen the answer.*

## Title favourites

| # | Team | Group | Champion | Δ vs 2026-06-13 | Final | Semi-final | Quarter-final | Rd of 16 |
|---|------|:-----:|---------:|-------:|------:|-----------:|--------------:|---------:|
| 1 | Spain | H | **19.7%** | +2.9 | 29.5% | 41.7% | 55.2% | 73.2% |
| 2 | Argentina | J | **17.0%** | +0.7 | 26.7% | 38.0% | 51.2% | 66.9% |
| 3 | England | L | **8.3%** | -0.5 | 14.9% | 25.3% | 39.8% | 70.1% |
| 4 | France | I | **8.1%** | +0.1 | 14.5% | 28.0% | 45.7% | 67.1% |
| 5 | Brazil | C | **6.0%** | +0.5 | 11.4% | 23.4% | 39.6% | 63.1% |
| 6 | Portugal | K | **4.3%** | -0.5 | 9.0% | 17.0% | 32.9% | 60.3% |
| 7 | Mexico | A | **3.8%** | +0.5 | 9.1% | 20.7% | 42.3% | 70.7% |
| 8 | Colombia | K | **3.6%** | -2.0 | 7.8% | 14.4% | 27.3% | 53.8% |
| 9 | Ecuador | E | **3.0%** | -0.1 | 6.9% | 14.5% | 27.7% | 53.8% |
| 10 | Netherlands | F | **2.8%** | -0.7 | 6.3% | 14.1% | 27.4% | 46.1% |
| 11 | Germany | E | **2.7%** | +0.3 | 5.8% | 13.5% | 27.1% | 54.6% |
| 12 | Belgium | G | **2.6%** | -0.7 | 6.8% | 14.0% | 31.2% | 58.6% |
| 13 | Japan | F | **2.3%** | – | 5.5% | 12.1% | 25.0% | 43.6% |
| 14 | Morocco | C | **2.0%** | -0.3 | 5.0% | 11.8% | 24.8% | 46.5% |
| 15 | Australia | D | **1.9%** | +1.5 | 5.2% | 12.3% | 28.9% | 59.4% |

## Biggest movers since last run (data through 2026-06-13)

| Team | Δ Champion | Δ Rd of 16 | Champion now |
|------|----------:|-----------:|-------------:|
| Spain | +2.9 | +2.8 | 19.7% |
| Australia | +1.5 | +30.5 | 1.9% |
| Argentina | +0.7 | +0.9 | 17.0% |
| Brazil | +0.5 | +2.3 | 6.0% |
| Belgium | -0.7 | -0.5 | 2.6% |
| Netherlands | -0.7 | -3.7 | 2.8% |
| Turkey | -1.3 | -28.5 | 0.3% |
| Colombia | -2.0 | -7.5 | 3.6% |

*Δ values in probability points. Full run-by-run series in `outputs/history.csv`.*

## Upcoming group matches — outcome probabilities

*(next match days; full list for all 72 group games in `match_probabilities.csv`)*

| Date | Grp | Match | Home win | Draw | Away win | xG | Likely score |
|------|:---:|-------|---------:|-----:|---------:|----|:----:|
| 2026-06-14 | F | Sweden v Tunisia | **43.3%** | 27.8% | 28.9% | 1.41–1.11 | 1-1 |
| 2026-06-14 | F | Netherlands v Japan | **35.6%** | 29.5% | 34.9% | 1.18–1.16 | 1-1 |
| 2026-06-14 | E | Germany v Curaçao | **84.5%** | 11.6% | 4.0% | 2.79–0.49 | 2-0 |
| 2026-06-14 | E | Ivory Coast v Ecuador | 21.3% | 28.5% | **50.2%** | 0.83–1.41 | 0-1 |
| 2026-06-15 | G | Belgium v Egypt | **55.0%** | 26.4% | 18.6% | 1.58–0.81 | 1-0 |
| 2026-06-15 | G | Iran v New Zealand | **51.8%** | 27.1% | 21.1% | 1.53–0.88 | 1-0 |
| 2026-06-15 | H | Spain v Cape Verde | **84.5%** | 11.6% | 3.9% | 2.77–0.48 | 2-0 |
| 2026-06-15 | H | Saudi Arabia v Uruguay | 14.8% | 25.0% | **60.2%** | 0.71–1.68 | 0-1 |
| 2026-06-16 | J | Austria v Jordan | **51.3%** | 26.3% | 22.4% | 1.60–0.98 | 1-1 |
| 2026-06-16 | J | Argentina v Algeria | **64.5%** | 23.3% | 12.1% | 1.78–0.63 | 1-0 |
| 2026-06-16 | I | France v Senegal | **57.4%** | 24.8% | 17.8% | 1.72–0.86 | 1-0 |
| 2026-06-16 | I | Iraq v Norway | 14.1% | 23.1% | **62.8%** | 0.75–1.85 | 0-1 |
| 2026-06-17 | K | Portugal v DR Congo | **68.5%** | 20.8% | 10.7% | 1.99–0.66 | 2-0 |
| 2026-06-17 | K | Uzbekistan v Colombia | 17.4% | 26.7% | **55.8%** | 0.75–1.55 | 0-1 |
| 2026-06-17 | L | England v Croatia | **56.5%** | 25.3% | 18.2% | 1.68–0.85 | 1-0 |
| 2026-06-17 | L | Ghana v Panama | 19.2% | 26.4% | **54.4%** | 0.84–1.59 | 0-1 |

## Group projections

### Group A

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Mexico | 1 | 1-0-0 | 2-0 | **3** | 7.27 | 68.0% | 95.9% | 99.5% |
| South Korea | 1 | 1-0-0 | 2-1 | **3** | 6.02 | 30.2% | 88.2% | 95.8% |
| Czech Republic | 1 | 0-0-1 | 1-2 | **0** | 2.22 | 1.4% | 8.4% | 44.2% |
| South Africa | 1 | 0-0-1 | 0-2 | **0** | 1.59 | 0.4% | 7.5% | 20.3% |

### Group B

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Bosnia and Herzegovina | 1 | 0-1-0 | 1-1 | **1** | 3.16 | 8.6% | 26.9% | 56.0% |
| Canada | 1 | 0-1-0 | 1-1 | **1** | 4.99 | 49.0% | 81.4% | 91.3% |
| Qatar | 1 | 0-1-0 | 1-1 | **1** | 2.43 | 3.9% | 15.6% | 34.9% |
| Switzerland | 1 | 0-1-0 | 1-1 | **1** | 4.48 | 38.5% | 76.0% | 84.3% |

### Group C

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Scotland | 1 | 1-0-0 | 1-0 | **3** | 4.78 | 21.2% | 48.9% | 86.4% |
| Brazil | 1 | 0-1-0 | 1-1 | **1** | 5.53 | 47.8% | 80.1% | 95.0% |
| Morocco | 1 | 0-1-0 | 1-1 | **1** | 5.04 | 30.5% | 68.5% | 90.3% |
| Haiti | 1 | 0-0-1 | 0-1 | **0** | 0.81 | 0.5% | 2.5% | 6.8% |

### Group D

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| United States | 1 | 1-0-0 | 4-1 | **3** | 5.84 | 48.0% | 83.6% | 96.0% |
| Australia | 1 | 1-0-0 | 2-0 | **3** | 5.96 | 43.4% | 83.5% | 95.8% |
| Turkey | 1 | 0-0-1 | 0-2 | **0** | 2.61 | 4.6% | 18.0% | 42.6% |
| Paraguay | 1 | 0-0-1 | 1-4 | **0** | 2.48 | 4.0% | 14.9% | 37.4% |

### Group E

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| Germany | 6.01 | 48.3% | 81.6% | 95.2% |
| Ecuador | 5.57 | 38.5% | 75.9% | 92.1% |
| Ivory Coast | 3.70 | 12.2% | 36.9% | 66.4% |
| Curaçao | 1.34 | 1.0% | 5.6% | 14.5% |

### Group F

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| Netherlands | 5.46 | 42.9% | 74.9% | 88.4% |
| Japan | 5.31 | 39.5% | 72.3% | 86.9% |
| Sweden | 3.08 | 10.1% | 29.7% | 51.6% |
| Tunisia | 2.64 | 7.5% | 23.1% | 41.5% |

### Group G

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| Belgium | 5.79 | 52.2% | 78.8% | 90.5% |
| Iran | 4.45 | 25.3% | 57.9% | 76.4% |
| Egypt | 3.45 | 13.9% | 37.6% | 58.8% |
| New Zealand | 2.73 | 8.6% | 25.8% | 43.5% |

### Group H

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| Spain | 7.21 | 73.1% | 95.1% | 98.7% |
| Uruguay | 5.21 | 22.9% | 76.7% | 89.8% |
| Saudi Arabia | 2.54 | 2.7% | 18.1% | 41.1% |
| Cape Verde | 1.82 | 1.4% | 10.1% | 24.4% |

### Group I

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| France | 6.32 | 60.4% | 85.1% | 94.4% |
| Norway | 4.49 | 21.4% | 58.3% | 78.6% |
| Senegal | 3.84 | 14.9% | 43.2% | 68.3% |
| Iraq | 1.93 | 3.3% | 13.5% | 26.7% |

### Group J

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| Argentina | 6.78 | 71.0% | 90.7% | 96.8% |
| Austria | 3.74 | 12.7% | 45.1% | 66.3% |
| Algeria | 3.67 | 11.8% | 43.6% | 65.0% |
| Jordan | 2.36 | 4.4% | 20.6% | 36.6% |

### Group K

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| Portugal | 5.88 | 49.4% | 81.4% | 92.4% |
| Colombia | 5.37 | 38.1% | 74.7% | 88.4% |
| Uzbekistan | 2.86 | 7.6% | 25.6% | 47.3% |
| DR Congo | 2.38 | 4.9% | 18.2% | 36.7% |

### Group L

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| England | 6.60 | 63.2% | 88.3% | 96.5% |
| Croatia | 4.90 | 24.2% | 65.9% | 86.2% |
| Panama | 3.59 | 10.9% | 37.1% | 63.6% |
| Ghana | 1.59 | 1.7% | 8.7% | 19.7% |

*\*Advance = top two or one of the eight best third-placed teams.*

## Most likely knockout bracket

Each tie shows the most probable pairing given projected group finishes, the chance the named winner goes through **in that pairing**, and how often the exact pairing occurred across all simulations.

### Round of 32

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 73 | 2026-06-28 | SoFi Stadium, Los Angeles | South Korea v Switzerland | **Switzerland** | 60.6% | 21.6% |
| 74 | 2026-06-29 | Gillette Stadium, Boston | Germany v Scotland | **Germany** | 57.7% | 5.0% |
| 75 | 2026-06-29 | Estadio BBVA, Monterrey | Netherlands v Morocco | **Netherlands** | 52.6% | 16.2% |
| 76 | 2026-06-29 | NRG Stadium, Houston | Brazil v Japan | **Brazil** | 60.8% | 15.5% |
| 77 | 2026-06-30 | MetLife Stadium, New York/New Jersey | France v Turkey | **France** | 70.1% | 6.2% |
| 78 | 2026-06-30 | AT&T Stadium, Dallas | Ecuador v Norway | **Ecuador** | 54.3% | 13.9% |
| 79 | 2026-06-30 | Estadio Azteca, Mexico City | Mexico v Ivory Coast | **Mexico** | 80.3% | 8.1% |
| 80 | 2026-07-01 | Mercedes-Benz Stadium, Atlanta | England v Saudi Arabia | **England** | 88.7% | 2.2% |
| 81 | 2026-07-01 | Levi's Stadium, San Francisco Bay Area | United States v Bosnia and Herzegovina | **United States** | 80.8% | 9.6% |
| 82 | 2026-07-01 | Lumen Field, Seattle | Belgium v Czech Republic | **Belgium** | 74.4% | 16.5% |
| 83 | 2026-07-02 | BMO Field, Toronto | Colombia v Croatia | **Colombia** | 62.8% | 15.3% |
| 84 | 2026-07-02 | SoFi Stadium, Los Angeles | Spain v Austria | **Spain** | 81.1% | 23.8% |
| 85 | 2026-07-02 | BC Place, Vancouver | Canada v Senegal | **Canada** | 59.0% | 2.0% |
| 86 | 2026-07-03 | Hard Rock Stadium, Miami | Argentina v Uruguay | **Argentina** | 76.3% | 38.2% |
| 87 | 2026-07-03 | Arrowhead Stadium, Kansas City | Portugal v Panama | **Portugal** | 74.1% | 13.1% |
| 88 | 2026-07-03 | AT&T Stadium, Dallas | Australia v Iran | **Australia** | 61.4% | 13.0% |

### Round of 16

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 89 | 2026-07-04 | Lincoln Financial Field, Philadelphia | Germany v France | **France** | 70.4% | 13.4% |
| 90 | 2026-07-04 | NRG Stadium, Houston | Switzerland v Netherlands | **Netherlands** | 66.6% | 4.8% |
| 91 | 2026-07-05 | MetLife Stadium, New York/New Jersey | Brazil v Ecuador | **Brazil** | 62.1% | 6.6% |
| 92 | 2026-07-05 | Estadio Azteca, Mexico City | Mexico v England | **Mexico** | 56.2% | 23.4% |
| 93 | 2026-07-06 | AT&T Stadium, Dallas | Colombia v Spain | **Spain** | 77.3% | 12.3% |
| 94 | 2026-07-06 | Lumen Field, Seattle | United States v Belgium | **Belgium** | 58.8% | 11.7% |
| 95 | 2026-07-07 | Mercedes-Benz Stadium, Atlanta | Argentina v Australia | **Argentina** | 71.4% | 12.8% |
| 96 | 2026-07-07 | BC Place, Vancouver | Canada v Portugal | **Portugal** | 55.5% | 10.8% |

### Quarter-finals

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 97 | 2026-07-09 | Gillette Stadium, Boston | France v Netherlands | **France** | 54.5% | 4.4% |
| 98 | 2026-07-10 | SoFi Stadium, Los Angeles | Spain v Belgium | **Spain** | 67.2% | 8.9% |
| 99 | 2026-07-11 | Hard Rock Stadium, Miami | Brazil v Mexico | **Brazil** | 61.8% | 6.0% |
| 100 | 2026-07-11 | Arrowhead Stadium, Kansas City | Argentina v Portugal | **Argentina** | 69.7% | 8.8% |

### Semi-finals

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 101 | 2026-07-14 | AT&T Stadium, Dallas | France v Spain | **Spain** | 66.0% | 6.0% |
| 102 | 2026-07-15 | Mercedes-Benz Stadium, Atlanta | Brazil v Argentina | **Argentina** | 67.4% | 3.4% |

### Final

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 104 | 2026-07-19 | MetLife Stadium, East Rutherford | Spain v Argentina | **Spain** | 58.8% | 6.2% |

**Projected champion: Spain** (overall title probability 19.7%; the single most likely path above is itself only one of many ways the tournament can unfold).

## How to read this

- All figures are probabilities, not certainties — a 65% favourite loses about one such match in three.
- `xPts` = expected group points; `xG` = expected goals from the Poisson model.
- Predictions refresh after every match day: run `python -m worldcup.run all` to pull new results, re-rate teams, and re-simulate.
- Machine-readable outputs: `match_probabilities.csv`, `tournament_projections.csv`. Past reports in `outputs/archive/`.
