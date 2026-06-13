# FIFA World Cup 2026 — ML Prediction Report

*Generated 2026-06-13 · data through **2026-06-12** · 50,000 Monte Carlo simulations · 4/72 group matches played*

Probabilities come from a gradient-boosted Poisson goal model (Elo strength + rolling form + venue/importance features) trained on 30,776 internationals, simulated through the official 2026 bracket and tiebreaker rules.

*Rolling validation (7,966 matches, 2018–2026): RPS 0.1687 vs Elo-baseline 0.1711; log-loss 0.8652 vs 0.8809.*

## Model scorecard

**2 of 4 match outcomes called correctly** (the model's own probabilities expected ≈2.4 of 4) · exact scoreline predicted 1/4 · average probability placed on what actually happened: **45.4%** (33.3% = guessing).

| Match | Model said | Likely score | Actual | Outcome | Score |
|-------|-----------|:---:|:---:|:---:|:---:|
| Mexico v South Africa | Mexico win (84.1%) | 2-0 | 2-0 | ✅ | ✅ |
| South Korea v Czech Republic | South Korea win (46.3%) | 1-1 | 2-1 | ✅ | — |
| Canada v Bosnia and Herzegovina | Canada win (75.0%) | 2-0 | 1-1 | ❌ | — |
| United States v Paraguay | Paraguay win (36.6%) | 1-1 | 4-1 | ❌ | — |

*Predictions are frozen at the last run before each result arrives, then graded — the scorecard never grades a model that has already seen the answer.*

## Title favourites

| # | Team | Group | Champion | Δ vs 2026-06-12 | Final | Semi-final | Quarter-final | Rd of 16 |
|---|------|:-----:|---------:|-------:|------:|-----------:|--------------:|---------:|
| 1 | Spain | H | **17.4%** | – | 26.6% | 38.0% | 52.7% | 71.2% |
| 2 | Argentina | J | **14.8%** | – | 23.2% | 33.6% | 48.7% | 66.7% |
| 3 | France | I | **8.0%** | – | 14.2% | 26.3% | 43.5% | 65.2% |
| 4 | England | L | **7.0%** | – | 12.8% | 22.7% | 37.9% | 66.4% |
| 5 | Brazil | C | **6.2%** | – | 11.5% | 23.4% | 38.5% | 61.6% |
| 6 | Colombia | K | **4.9%** | – | 9.7% | 17.9% | 32.4% | 59.4% |
| 7 | Portugal | K | **4.8%** | – | 9.7% | 18.2% | 32.8% | 59.2% |
| 8 | Netherlands | F | **3.8%** | – | 8.2% | 16.8% | 30.8% | 51.4% |
| 9 | Mexico | A | **3.6%** | – | 8.5% | 19.7% | 40.6% | 69.0% |
| 10 | Ecuador | E | **3.2%** | – | 7.2% | 15.1% | 28.7% | 55.1% |
| 11 | Belgium | G | **2.8%** | – | 7.2% | 14.5% | 32.0% | 57.9% |
| 12 | Switzerland | B | **2.7%** | – | 6.3% | 13.6% | 27.9% | 59.4% |
| 13 | Germany | E | **2.7%** | – | 6.0% | 13.6% | 27.2% | 54.1% |
| 14 | Japan | F | **2.6%** | – | 6.1% | 13.1% | 26.5% | 45.9% |
| 15 | Norway | I | **2.2%** | – | 5.0% | 11.9% | 24.9% | 46.8% |

## Biggest movers since last run (data through 2026-06-12)

| Team | Δ Champion | Δ Rd of 16 | Champion now |
|------|----------:|-----------:|-------------:|
| Spain | – | – | 17.4% |
| Argentina | – | – | 14.8% |
| Turkey | – | – | 1.6% |
| Paraguay | – | – | 0.2% |
| Senegal | – | – | 0.5% |
| Ivory Coast | – | – | 0.2% |
| South Korea | – | – | 0.9% |
| Croatia | – | – | 0.9% |

*Δ values in probability points. Full run-by-run series in `outputs/history.csv`.*

## Upcoming group matches — outcome probabilities

*(next match days; full list for all 72 group games in `match_probabilities.csv`)*

| Date | Grp | Match | Home win | Draw | Away win | xG | Likely score |
|------|:---:|-------|---------:|-----:|---------:|----|:----:|
| 2026-06-13 | B | Qatar v Switzerland | 8.6% | 17.6% | **73.8%** | 0.65–2.27 | 0-2 |
| 2026-06-13 | C | Brazil v Morocco | **53.0%** | 26.8% | 20.2% | 1.55–0.86 | 1-0 |
| 2026-06-13 | C | Haiti v Scotland | 24.3% | 26.5% | **49.2%** | 1.04–1.57 | 1-1 |
| 2026-06-13 | D | Australia v Turkey | 26.1% | 28.7% | **45.2%** | 0.98–1.37 | 1-1 |
| 2026-06-14 | F | Sweden v Tunisia | **42.8%** | 28.7% | 28.5% | 1.34–1.05 | 1-1 |
| 2026-06-14 | F | Netherlands v Japan | **37.7%** | 29.7% | 32.6% | 1.20–1.10 | 1-1 |
| 2026-06-14 | E | Germany v Curaçao | **81.8%** | 12.7% | 5.6% | 2.80–0.64 | 2-0 |
| 2026-06-14 | E | Ivory Coast v Ecuador | 22.9% | 27.0% | **50.1%** | 0.96–1.53 | 1-1 |
| 2026-06-15 | G | Belgium v Egypt | **55.8%** | 24.3% | 19.9% | 1.79–0.98 | 1-1 |
| 2026-06-15 | G | Iran v New Zealand | **51.3%** | 27.5% | 21.2% | 1.50–0.87 | 1-0 |
| 2026-06-15 | H | Spain v Cape Verde | **85.4%** | 10.7% | 4.0% | 2.97–0.55 | 2-0 |
| 2026-06-15 | H | Saudi Arabia v Uruguay | 15.7% | 25.1% | **59.3%** | 0.74–1.68 | 0-1 |
| 2026-06-16 | J | Austria v Jordan | **50.3%** | 26.4% | 23.4% | 1.59–1.01 | 1-1 |
| 2026-06-16 | J | Argentina v Algeria | **63.7%** | 22.3% | 14.0% | 1.92–0.78 | 2-0 |
| 2026-06-16 | I | France v Senegal | **56.3%** | 25.5% | 18.2% | 1.66–0.84 | 1-0 |
| 2026-06-16 | I | Iraq v Norway | 14.1% | 23.3% | **62.5%** | 0.74–1.82 | 0-1 |

## Group projections

### Group A

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Mexico | 1 | 1-0-0 | 2-0 | **3** | 7.19 | 66.9% | 94.7% | 99.6% |
| South Korea | 1 | 1-0-0 | 2-1 | **3** | 6.13 | 31.0% | 89.8% | 96.5% |
| Czech Republic | 1 | 0-0-1 | 1-2 | **0** | 2.41 | 1.8% | 9.9% | 49.9% |
| South Africa | 1 | 0-0-1 | 0-2 | **0** | 1.38 | 0.3% | 5.6% | 16.9% |

### Group B

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Bosnia and Herzegovina | 1 | 0-1-0 | 1-1 | **1** | 3.21 | 6.8% | 26.5% | 58.0% |
| Canada | 1 | 0-1-0 | 1-1 | **1** | 4.87 | 34.9% | 79.7% | 92.1% |
| Qatar | 0 | 0-0-0 | 0-0 | **0** | 1.74 | 2.8% | 10.0% | 22.4% |
| Switzerland | 0 | 0-0-0 | 0-0 | **0** | 6.07 | 55.5% | 83.8% | 94.1% |

### Group C

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| Brazil | 6.34 | 59.7% | 85.4% | 95.1% |
| Morocco | 4.92 | 26.1% | 66.8% | 84.7% |
| Scotland | 3.41 | 11.2% | 34.9% | 59.8% |
| Haiti | 1.94 | 2.9% | 12.9% | 27.4% |

### Group D

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| United States | 1 | 1-0-0 | 4-1 | **3** | 6.02 | 53.7% | 84.2% | 97.0% |
| Australia | 0 | 0-0-0 | 0-0 | **0** | 3.52 | 13.9% | 37.9% | 60.3% |
| Turkey | 0 | 0-0-0 | 0-0 | **0** | 4.73 | 29.3% | 61.6% | 79.0% |
| Paraguay | 1 | 0-0-1 | 1-4 | **0** | 2.34 | 3.1% | 16.3% | 34.3% |

### Group E

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| Germany | 5.82 | 44.7% | 79.0% | 93.8% |
| Ecuador | 5.64 | 40.8% | 76.3% | 92.6% |
| Ivory Coast | 3.75 | 13.3% | 38.5% | 66.9% |
| Curaçao | 1.41 | 1.2% | 6.2% | 15.9% |

### Group F

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| Netherlands | 5.51 | 43.9% | 75.1% | 88.9% |
| Japan | 5.25 | 38.0% | 71.6% | 86.8% |
| Sweden | 3.28 | 12.0% | 33.3% | 55.6% |
| Tunisia | 2.43 | 6.1% | 20.0% | 37.5% |

### Group G

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| Belgium | 5.67 | 50.4% | 77.1% | 89.5% |
| Iran | 4.38 | 25.3% | 56.0% | 75.0% |
| Egypt | 3.56 | 15.1% | 40.0% | 60.6% |
| New Zealand | 2.80 | 9.2% | 26.9% | 45.2% |

### Group H

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| Spain | 7.11 | 71.5% | 94.3% | 98.6% |
| Uruguay | 5.20 | 23.4% | 75.5% | 89.5% |
| Saudi Arabia | 2.73 | 3.8% | 20.9% | 46.4% |
| Cape Verde | 1.73 | 1.4% | 9.3% | 22.7% |

### Group I

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| France | 6.06 | 55.6% | 82.0% | 92.7% |
| Norway | 4.68 | 25.4% | 61.5% | 81.0% |
| Senegal | 3.77 | 14.8% | 41.6% | 66.8% |
| Iraq | 2.04 | 4.1% | 14.8% | 28.9% |

### Group J

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| Argentina | 6.78 | 69.9% | 90.3% | 97.0% |
| Austria | 3.83 | 13.9% | 46.6% | 67.6% |
| Algeria | 3.80 | 12.9% | 45.6% | 67.7% |
| Jordan | 2.18 | 3.3% | 17.5% | 32.7% |

### Group K

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| Portugal | 5.65 | 44.8% | 78.1% | 90.7% |
| Colombia | 5.49 | 41.7% | 76.2% | 89.3% |
| Uzbekistan | 2.83 | 7.6% | 25.1% | 46.8% |
| DR Congo | 2.51 | 6.0% | 20.5% | 39.5% |

### Group L

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| England | 6.59 | 62.9% | 88.2% | 96.4% |
| Croatia | 4.95 | 24.6% | 67.0% | 86.7% |
| Panama | 3.51 | 10.8% | 35.8% | 62.2% |
| Ghana | 1.66 | 1.7% | 9.1% | 21.3% |

*\*Advance = top two or one of the eight best third-placed teams.*

## Most likely knockout bracket

Each tie shows the most probable pairing given projected group finishes, the chance the named winner goes through **in that pairing**, and how often the exact pairing occurred across all simulations.

### Round of 32

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 73 | 2026-06-28 | SoFi Stadium, Los Angeles | South Korea v Canada | **South Korea** | 60.1% | 26.5% |
| 74 | 2026-06-29 | Gillette Stadium, Boston | Germany v Czech Republic | **Germany** | 77.1% | 2.8% |
| 75 | 2026-06-29 | Estadio BBVA, Monterrey | Netherlands v Morocco | **Netherlands** | 61.6% | 17.8% |
| 76 | 2026-06-29 | NRG Stadium, Houston | Brazil v Japan | **Brazil** | 63.1% | 20.0% |
| 77 | 2026-06-30 | MetLife Stadium, New York/New Jersey | France v Australia | **France** | 71.4% | 5.0% |
| 78 | 2026-06-30 | AT&T Stadium, Dallas | Ecuador v Norway | **Ecuador** | 53.6% | 12.7% |
| 79 | 2026-06-30 | Estadio Azteca, Mexico City | Mexico v Scotland | **Mexico** | 79.2% | 6.4% |
| 80 | 2026-07-01 | Mercedes-Benz Stadium, Atlanta | England v Ivory Coast | **England** | 80.4% | 1.6% |
| 81 | 2026-07-01 | Levi's Stadium, San Francisco Bay Area | United States v Bosnia and Herzegovina | **United States** | 85.0% | 10.8% |
| 82 | 2026-07-01 | Lumen Field, Seattle | Belgium v Saudi Arabia | **Belgium** | 79.7% | 4.2% |
| 83 | 2026-07-02 | BMO Field, Toronto | Colombia v Croatia | **Colombia** | 67.3% | 14.6% |
| 84 | 2026-07-02 | SoFi Stadium, Los Angeles | Spain v Austria | **Spain** | 77.2% | 23.3% |
| 85 | 2026-07-02 | BC Place, Vancouver | Switzerland v Senegal | **Switzerland** | 60.6% | 2.3% |
| 86 | 2026-07-03 | Hard Rock Stadium, Miami | Argentina v Uruguay | **Argentina** | 76.8% | 36.3% |
| 87 | 2026-07-03 | Arrowhead Stadium, Kansas City | Portugal v Panama | **Portugal** | 72.8% | 11.8% |
| 88 | 2026-07-03 | AT&T Stadium, Dallas | Turkey v Iran | **Turkey** | 58.4% | 9.9% |

### Round of 16

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 89 | 2026-07-04 | Lincoln Financial Field, Philadelphia | Germany v France | **France** | 68.3% | 11.6% |
| 90 | 2026-07-04 | NRG Stadium, Houston | South Korea v Netherlands | **Netherlands** | 72.3% | 9.1% |
| 91 | 2026-07-05 | MetLife Stadium, New York/New Jersey | Brazil v Ecuador | **Brazil** | 62.3% | 7.6% |
| 92 | 2026-07-05 | Estadio Azteca, Mexico City | Mexico v England | **Mexico** | 54.1% | 21.6% |
| 93 | 2026-07-06 | AT&T Stadium, Dallas | Colombia v Spain | **Spain** | 73.0% | 12.1% |
| 94 | 2026-07-06 | Lumen Field, Seattle | United States v Belgium | **Belgium** | 62.8% | 12.6% |
| 95 | 2026-07-07 | Mercedes-Benz Stadium, Atlanta | Argentina v Turkey | **Argentina** | 62.6% | 9.6% |
| 96 | 2026-07-07 | BC Place, Vancouver | Switzerland v Portugal | **Portugal** | 64.4% | 11.4% |

### Quarter-finals

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 97 | 2026-07-09 | Gillette Stadium, Boston | France v Netherlands | **France** | 50.9% | 4.8% |
| 98 | 2026-07-10 | SoFi Stadium, Los Angeles | Spain v Belgium | **Spain** | 66.4% | 8.5% |
| 99 | 2026-07-11 | Hard Rock Stadium, Miami | Brazil v Mexico | **Brazil** | 61.2% | 6.9% |
| 100 | 2026-07-11 | Arrowhead Stadium, Kansas City | Argentina v Portugal | **Argentina** | 63.7% | 7.6% |

### Semi-finals

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 101 | 2026-07-14 | AT&T Stadium, Dallas | France v Spain | **Spain** | 64.1% | 4.9% |
| 102 | 2026-07-15 | Mercedes-Benz Stadium, Atlanta | Brazil v Argentina | **Argentina** | 71.4% | 3.7% |

### Final

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 104 | 2026-07-19 | MetLife Stadium, East Rutherford | Spain v Argentina | **Spain** | 58.1% | 4.5% |

**Projected champion: Spain** (overall title probability 17.4%; the single most likely path above is itself only one of many ways the tournament can unfold).

## How to read this

- All figures are probabilities, not certainties — a 65% favourite loses about one such match in three.
- `xPts` = expected group points; `xG` = expected goals from the Poisson model.
- Predictions refresh after every match day: run `python -m worldcup.run all` to pull new results, re-rate teams, and re-simulate.
- Machine-readable outputs: `match_probabilities.csv`, `tournament_projections.csv`. Past reports in `outputs/archive/`.
