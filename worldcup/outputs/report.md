# FIFA World Cup 2026 — ML Prediction Report

*Generated 2026-06-12 · data through **2026-06-11** · 100,000 Monte Carlo simulations · 2/72 group matches played*

Probabilities come from a gradient-boosted Poisson goal model (Elo strength + rolling form + venue/importance features) trained on 30,774 internationals, simulated through the official 2026 bracket and tiebreaker rules.

*Rolling validation (7,966 matches, 2018–2026): RPS 0.1687 vs Elo-baseline 0.1711; log-loss 0.8652 vs 0.8809.*

## Model scorecard

**2 of 2 match outcomes called correctly** (the model's own probabilities expected ≈1.3 of 2) · exact scoreline predicted 1/2 · average probability placed on what actually happened: **65.2%** (33.3% = guessing).

| Match | Model said | Likely score | Actual | Outcome | Score |
|-------|-----------|:---:|:---:|:---:|:---:|
| Mexico v South Africa | Mexico win (84.1%) | 2-0 | 2-0 | ✅ | ✅ |
| South Korea v Czech Republic | South Korea win (46.3%) | 1-1 | 2-1 | ✅ | — |

*Predictions are frozen at the last run before each result arrives, then graded — the scorecard never grades a model that has already seen the answer.*

## Title favourites

| # | Team | Group | Champion | Δ vs 2026-06-11 | Final | Semi-final | Quarter-final | Rd of 16 |
|---|------|:-----:|---------:|-------:|------:|-----------:|--------------:|---------:|
| 1 | Spain | H | **19.8%** | – | 30.2% | 41.7% | 55.5% | 71.9% |
| 2 | Argentina | J | **18.1%** | – | 27.8% | 38.8% | 53.6% | 68.5% |
| 3 | England | L | **8.0%** | – | 14.0% | 24.5% | 39.2% | 67.8% |
| 4 | France | I | **6.7%** | – | 12.6% | 25.1% | 42.2% | 64.8% |
| 5 | Brazil | C | **5.7%** | – | 11.0% | 23.1% | 38.5% | 62.2% |
| 6 | Colombia | K | **4.4%** | – | 9.1% | 16.7% | 30.6% | 58.7% |
| 7 | Mexico | A | **3.8%** | – | 9.0% | 19.3% | 42.2% | 70.1% |
| 8 | Portugal | K | **3.8%** | – | 8.3% | 16.1% | 31.3% | 60.5% |
| 9 | Ecuador | E | **3.6%** | – | 7.9% | 16.3% | 29.8% | 56.8% |
| 10 | Belgium | G | **2.8%** | – | 7.3% | 14.3% | 33.0% | 60.1% |
| 11 | Netherlands | F | **2.8%** | – | 6.6% | 15.0% | 28.7% | 48.9% |
| 12 | Japan | F | **2.7%** | – | 6.2% | 13.7% | 27.1% | 47.4% |
| 13 | Morocco | C | **2.3%** | – | 5.4% | 11.8% | 24.5% | 44.8% |
| 14 | Germany | E | **2.2%** | – | 5.1% | 13.0% | 26.8% | 54.0% |
| 15 | Switzerland | B | **2.1%** | – | 5.3% | 12.2% | 26.2% | 59.1% |

## Biggest movers since last run (data through 2026-06-11)

| Team | Δ Champion | Δ Rd of 16 | Champion now |
|------|----------:|-----------:|-------------:|
| Spain | – | – | 19.8% |
| Argentina | – | – | 18.1% |
| Haiti | – | – | 0.0% |
| South Korea | – | – | 0.6% |
| Ivory Coast | – | – | 0.1% |
| Austria | – | – | 0.5% |
| Morocco | – | – | 2.3% |
| Scotland | – | – | 0.2% |

*Δ values in probability points. Full run-by-run series in `outputs/history.csv`.*

## Upcoming group matches — outcome probabilities

*(next match days; full list for all 72 group games in `match_probabilities.csv`)*

| Date | Grp | Match | Home win | Draw | Away win | xG | Likely score |
|------|:---:|-------|---------:|-----:|---------:|----|:----:|
| 2026-06-12 | B | Canada v Bosnia and Herzegovina | **75.0%** | 17.2% | 7.8% | 2.28–0.61 | 2-0 |
| 2026-06-12 | D | United States v Paraguay | 33.1% | 27.9% | **39.0%** | 1.22–1.35 | 1-1 |
| 2026-06-13 | B | Qatar v Switzerland | 6.3% | 13.9% | **79.8%** | 0.65–2.66 | 0-2 |
| 2026-06-13 | C | Brazil v Morocco | **48.2%** | 28.6% | 23.2% | 1.40–0.89 | 1-0 |
| 2026-06-13 | C | Haiti v Scotland | 25.4% | 27.1% | **47.5%** | 1.04–1.51 | 1-1 |
| 2026-06-13 | D | Australia v Turkey | 29.5% | 28.5% | **42.0%** | 1.09–1.35 | 1-1 |
| 2026-06-14 | F | Sweden v Tunisia | **42.5%** | 28.5% | 29.0% | 1.36–1.08 | 1-1 |
| 2026-06-14 | F | Netherlands v Japan | 32.7% | 29.7% | **37.6%** | 1.11–1.21 | 1-1 |
| 2026-06-14 | E | Germany v Curaçao | **82.5%** | 12.8% | 4.7% | 2.67–0.52 | 2-0 |
| 2026-06-14 | E | Ivory Coast v Ecuador | 18.7% | 25.0% | **56.3%** | 0.88–1.71 | 0-1 |
| 2026-06-15 | G | Belgium v Egypt | **56.6%** | 24.9% | 18.5% | 1.72–0.88 | 1-0 |
| 2026-06-15 | G | Iran v New Zealand | **53.3%** | 26.4% | 20.3% | 1.59–0.88 | 1-0 |
| 2026-06-15 | H | Spain v Cape Verde | **91.7%** | 6.5% | 1.8% | 3.54–0.44 | 3-0 |
| 2026-06-15 | H | Saudi Arabia v Uruguay | 16.0% | 25.9% | **58.1%** | 0.73–1.62 | 0-1 |

## Group projections

### Group A

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Mexico | 1 | 1-0-0 | 2-0 | **3** | 7.39 | 73.7% | 96.1% | 99.7% |
| South Korea | 1 | 1-0-0 | 2-1 | **3** | 5.74 | 24.0% | 85.2% | 94.6% |
| Czech Republic | 1 | 0-0-1 | 1-2 | **0** | 2.28 | 1.9% | 9.8% | 47.9% |
| South Africa | 1 | 0-0-1 | 0-2 | **0** | 1.67 | 0.4% | 9.0% | 22.9% |

### Group B

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| Canada | 6.57 | 53.8% | 91.2% | 97.5% |
| Switzerland | 6.10 | 42.2% | 87.3% | 96.0% |
| Bosnia and Herzegovina | 2.44 | 2.8% | 14.2% | 39.2% |
| Qatar | 1.69 | 1.1% | 7.3% | 21.9% |

### Group C

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| Brazil | 6.34 | 57.6% | 85.9% | 95.7% |
| Morocco | 5.25 | 30.9% | 72.8% | 89.2% |
| Scotland | 3.23 | 9.4% | 30.6% | 57.0% |
| Haiti | 1.82 | 2.1% | 10.7% | 25.5% |

### Group D

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| Turkey | 4.77 | 36.2% | 62.7% | 79.4% |
| Paraguay | 4.02 | 23.8% | 49.3% | 68.5% |
| Australia | 3.78 | 20.3% | 44.4% | 64.1% |
| United States | 3.73 | 19.8% | 43.6% | 63.5% |

### Group E

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| Germany | 5.89 | 45.4% | 80.6% | 94.7% |
| Ecuador | 5.76 | 42.4% | 78.9% | 93.3% |
| Ivory Coast | 3.52 | 10.9% | 34.0% | 63.3% |
| Curaçao | 1.45 | 1.3% | 6.5% | 17.2% |

### Group F

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| Japan | 5.56 | 43.1% | 76.3% | 89.6% |
| Netherlands | 5.52 | 42.3% | 76.3% | 89.7% |
| Sweden | 2.91 | 8.2% | 26.3% | 49.5% |
| Tunisia | 2.52 | 6.3% | 21.0% | 40.2% |

### Group G

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| Belgium | 5.80 | 52.5% | 79.0% | 90.8% |
| Iran | 4.48 | 25.8% | 58.2% | 77.3% |
| Egypt | 3.41 | 13.3% | 37.3% | 58.7% |
| New Zealand | 2.74 | 8.4% | 25.5% | 44.7% |

### Group H

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| Spain | 7.28 | 74.0% | 96.0% | 99.3% |
| Uruguay | 5.27 | 22.3% | 77.9% | 91.4% |
| Saudi Arabia | 2.57 | 2.9% | 18.8% | 43.2% |
| Cape Verde | 1.67 | 0.8% | 7.4% | 20.7% |

### Group I

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| France | 6.11 | 56.1% | 82.6% | 93.5% |
| Norway | 4.76 | 26.0% | 63.2% | 82.8% |
| Senegal | 3.75 | 14.5% | 40.9% | 67.6% |
| Iraq | 1.93 | 3.4% | 13.3% | 27.2% |

### Group J

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| Argentina | 6.89 | 72.1% | 91.6% | 97.4% |
| Austria | 3.85 | 13.1% | 47.3% | 69.1% |
| Algeria | 3.68 | 11.5% | 43.5% | 66.6% |
| Jordan | 2.17 | 3.3% | 17.6% | 33.4% |

### Group K

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| Portugal | 5.71 | 45.7% | 79.1% | 91.4% |
| Colombia | 5.51 | 41.5% | 76.7% | 90.0% |
| Uzbekistan | 2.77 | 7.1% | 24.2% | 46.2% |
| DR Congo | 2.50 | 5.6% | 20.0% | 40.2% |

### Group L

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| England | 6.58 | 63.1% | 88.3% | 96.5% |
| Croatia | 4.89 | 24.3% | 66.0% | 86.4% |
| Panama | 3.50 | 10.7% | 36.0% | 62.6% |
| Ghana | 1.70 | 1.9% | 9.7% | 22.9% |

*\*Advance = top two or one of the eight best third-placed teams.*

## Most likely knockout bracket

Each tie shows the most probable pairing given projected group finishes, the chance the named winner goes through **in that pairing**, and how often the exact pairing occurred across all simulations.

### Round of 32

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 73 | 2026-06-28 | SoFi Stadium, Los Angeles | South Korea v Switzerland | **Switzerland** | 61.7% | 27.6% |
| 74 | 2026-06-29 | Gillette Stadium, Boston | Germany v Czech Republic | **Germany** | 78.5% | 2.7% |
| 75 | 2026-06-29 | Estadio BBVA, Monterrey | Japan v Morocco | **Japan** | 57.6% | 18.1% |
| 76 | 2026-06-29 | NRG Stadium, Houston | Brazil v Netherlands | **Brazil** | 54.7% | 19.6% |
| 77 | 2026-06-30 | MetLife Stadium, New York/New Jersey | France v Scotland | **France** | 74.6% | 4.2% |
| 78 | 2026-06-30 | AT&T Stadium, Dallas | Ecuador v Norway | **Ecuador** | 58.0% | 13.6% |
| 79 | 2026-06-30 | Estadio Azteca, Mexico City | Mexico v Ivory Coast | **Mexico** | 81.9% | 8.5% |
| 80 | 2026-07-01 | Mercedes-Benz Stadium, Atlanta | England v Senegal | **England** | 75.3% | 1.5% |
| 81 | 2026-07-01 | Levi's Stadium, San Francisco Bay Area | Turkey v Bosnia and Herzegovina | **Turkey** | 84.6% | 6.7% |
| 82 | 2026-07-01 | Lumen Field, Seattle | Belgium v Saudi Arabia | **Belgium** | 80.2% | 4.2% |
| 83 | 2026-07-02 | BMO Field, Toronto | Colombia v Croatia | **Colombia** | 68.9% | 14.7% |
| 84 | 2026-07-02 | SoFi Stadium, Los Angeles | Spain v Austria | **Spain** | 78.2% | 25.3% |
| 85 | 2026-07-02 | BC Place, Vancouver | Canada v Sweden | **Canada** | 72.9% | 4.1% |
| 86 | 2026-07-03 | Hard Rock Stadium, Miami | Argentina v Uruguay | **Argentina** | 78.2% | 40.1% |
| 87 | 2026-07-03 | Arrowhead Stadium, Kansas City | Portugal v Panama | **Portugal** | 73.5% | 12.1% |
| 88 | 2026-07-03 | AT&T Stadium, Dallas | Paraguay v Iran | **Paraguay** | 50.6% | 8.2% |

### Round of 16

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 89 | 2026-07-04 | Lincoln Financial Field, Philadelphia | Germany v France | **France** | 70.6% | 11.6% |
| 90 | 2026-07-04 | NRG Stadium, Houston | Switzerland v Japan | **Japan** | 60.9% | 6.7% |
| 91 | 2026-07-05 | MetLife Stadium, New York/New Jersey | Brazil v Ecuador | **Brazil** | 67.0% | 7.9% |
| 92 | 2026-07-05 | Estadio Azteca, Mexico City | Mexico v England | **Mexico** | 52.2% | 24.6% |
| 93 | 2026-07-06 | AT&T Stadium, Dallas | Colombia v Spain | **Spain** | 79.5% | 12.7% |
| 94 | 2026-07-06 | Lumen Field, Seattle | Turkey v Belgium | **Belgium** | 63.2% | 9.0% |
| 95 | 2026-07-07 | Mercedes-Benz Stadium, Atlanta | Argentina v Paraguay | **Argentina** | 81.7% | 7.5% |
| 96 | 2026-07-07 | BC Place, Vancouver | Canada v Portugal | **Portugal** | 54.0% | 11.5% |

### Quarter-finals

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 97 | 2026-07-09 | Gillette Stadium, Boston | France v Japan | **France** | 57.9% | 4.2% |
| 98 | 2026-07-10 | SoFi Stadium, Los Angeles | Spain v Belgium | **Spain** | 71.6% | 10.2% |
| 99 | 2026-07-11 | Hard Rock Stadium, Miami | Brazil v Mexico | **Brazil** | 61.9% | 7.5% |
| 100 | 2026-07-11 | Arrowhead Stadium, Kansas City | Argentina v Portugal | **Argentina** | 68.2% | 8.5% |

### Semi-finals

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 101 | 2026-07-14 | AT&T Stadium, Dallas | France v Spain | **Spain** | 68.8% | 5.3% |
| 102 | 2026-07-15 | Mercedes-Benz Stadium, Atlanta | Brazil v Argentina | **Argentina** | 74.1% | 4.3% |

### Final

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 104 | 2026-07-19 | MetLife Stadium, East Rutherford | Spain v Argentina | **Spain** | 56.6% | 6.5% |

**Projected champion: Spain** (overall title probability 19.8%; the single most likely path above is itself only one of many ways the tournament can unfold).

## How to read this

- All figures are probabilities, not certainties — a 65% favourite loses about one such match in three.
- `xPts` = expected group points; `xG` = expected goals from the Poisson model.
- Predictions refresh after every match day: run `python -m worldcup.run all` to pull new results, re-rate teams, and re-simulate.
- Machine-readable outputs: `match_probabilities.csv`, `tournament_projections.csv`. Past reports in `outputs/archive/`.
