# FIFA World Cup 2026 — ML Prediction Report

*Generated 2026-06-14 · data through **2026-06-14** · 50,000 Monte Carlo simulations · 10/72 group matches played*

Probabilities come from a gradient-boosted Poisson goal model (Elo strength + rolling form + venue/importance features) trained on 30,782 internationals, simulated through the official 2026 bracket and tiebreaker rules.

*Rolling validation (7,966 matches, 2018–2026): RPS 0.1687 vs Elo-baseline 0.1711; log-loss 0.8652 vs 0.8809.*

## Model scorecard

**4 of 10 match outcomes called correctly** (the model's own probabilities expected ≈5.7 of 10) · exact scoreline predicted 1/10 · average probability placed on what actually happened: **41.5%** (33.3% = guessing).

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

*Predictions are frozen at the last run before each result arrives, then graded — the scorecard never grades a model that has already seen the answer.*

## Title favourites

| # | Team | Group | Champion | Δ vs 2026-06-14 | Final | Semi-final | Quarter-final | Rd of 16 |
|---|------|:-----:|---------:|-------:|------:|-----------:|--------------:|---------:|
| 1 | Spain | H | **21.2%** | +0.7 | 31.9% | 44.2% | 57.7% | 74.8% |
| 2 | Argentina | J | **15.8%** | -4.6 | 25.5% | 37.2% | 51.4% | 67.0% |
| 3 | England | L | **7.5%** | -2.3 | 13.3% | 23.4% | 37.5% | 66.5% |
| 4 | France | I | **6.8%** | -0.3 | 12.9% | 25.9% | 44.8% | 65.5% |
| 5 | Brazil | C | **5.4%** | -0.7 | 10.2% | 21.6% | 36.6% | 59.6% |
| 6 | Colombia | K | **5.0%** | +1.0 | 10.1% | 18.0% | 31.7% | 58.2% |
| 7 | Portugal | K | **4.5%** | +1.1 | 9.2% | 16.6% | 31.0% | 58.1% |
| 8 | Mexico | A | **4.0%** | +1.4 | 9.2% | 20.4% | 39.7% | 68.8% |
| 9 | Ecuador | E | **2.9%** | -0.1 | 6.1% | 13.5% | 27.0% | 52.0% |
| 10 | Japan | F | **2.8%** | +0.8 | 6.3% | 14.1% | 27.3% | 47.6% |
| 11 | Belgium | G | **2.6%** | +0.1 | 6.5% | 12.3% | 29.7% | 56.9% |
| 12 | Netherlands | F | **2.6%** | -0.5 | 6.2% | 14.8% | 27.6% | 48.7% |
| 13 | Germany | E | **2.3%** | +1.0 | 5.2% | 12.9% | 26.8% | 55.1% |
| 14 | Morocco | C | **2.1%** | +0.1 | 5.3% | 12.0% | 25.2% | 46.7% |
| 15 | Australia | D | **2.0%** | – | 5.1% | 11.4% | 27.9% | 58.6% |

## Biggest movers since last run (data through 2026-06-14)

| Team | Δ Champion | Δ Rd of 16 | Champion now |
|------|----------:|-----------:|-------------:|
| Mexico | +1.4 | +1.7 | 4.0% |
| Portugal | +1.1 | -0.6 | 4.5% |
| Germany | +1.0 | +5.2 | 2.3% |
| Colombia | +1.0 | +1.3 | 5.0% |
| Japan | +0.8 | +4.5 | 2.8% |
| Brazil | -0.7 | -4.1 | 5.4% |
| England | -2.3 | -5.6 | 7.5% |
| Argentina | -4.6 | -3.9 | 15.8% |

*Δ values in probability points. Full run-by-run series in `outputs/history.csv`.*

## Upcoming group matches — outcome probabilities

*(next match days; full list for all 72 group games in `match_probabilities.csv`)*

| Date | Grp | Match | Home win | Draw | Away win | xG | Likely score |
|------|:---:|-------|---------:|-----:|---------:|----|:----:|
| 2026-06-14 | F | Sweden v Tunisia | **42.1%** | 27.2% | 30.7% | 1.45–1.20 | 1-1 |
| 2026-06-14 | E | Ivory Coast v Ecuador | 24.1% | 27.8% | **48.2%** | 0.96–1.46 | 1-1 |
| 2026-06-15 | G | Belgium v Egypt | **56.5%** | 25.5% | 18.1% | 1.66–0.83 | 1-0 |
| 2026-06-15 | G | Iran v New Zealand | **48.9%** | 27.3% | 23.8% | 1.51–0.97 | 1-1 |
| 2026-06-15 | H | Spain v Cape Verde | **91.6%** | 6.5% | 1.8% | 3.51–0.43 | 3-0 |
| 2026-06-15 | H | Saudi Arabia v Uruguay | 13.8% | 23.8% | **62.4%** | 0.70–1.77 | 0-1 |
| 2026-06-16 | J | Austria v Jordan | **50.0%** | 26.6% | 23.4% | 1.57–0.99 | 1-1 |
| 2026-06-16 | J | Argentina v Algeria | **68.5%** | 21.0% | 10.5% | 1.97–0.63 | 2-0 |
| 2026-06-16 | I | France v Senegal | **54.4%** | 25.3% | 20.3% | 1.69–0.94 | 1-1 |
| 2026-06-16 | I | Iraq v Norway | 13.7% | 23.9% | **62.4%** | 0.69–1.76 | 0-1 |
| 2026-06-17 | K | Portugal v DR Congo | **66.6%** | 22.1% | 11.3% | 1.88–0.64 | 1-0 |
| 2026-06-17 | K | Uzbekistan v Colombia | 16.4% | 25.3% | **58.3%** | 0.77–1.67 | 0-1 |
| 2026-06-17 | L | England v Croatia | **53.2%** | 26.7% | 20.1% | 1.56–0.86 | 1-0 |
| 2026-06-17 | L | Ghana v Panama | 22.9% | 25.7% | **51.4%** | 1.03–1.65 | 1-1 |

## Group projections

### Group A

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Mexico | 1 | 1-0-0 | 2-0 | **3** | 7.35 | 70.1% | 96.2% | 99.7% |
| South Korea | 1 | 1-0-0 | 2-1 | **3** | 6.06 | 28.1% | 89.7% | 96.5% |
| Czech Republic | 1 | 0-0-1 | 1-2 | **0** | 2.23 | 1.4% | 7.7% | 44.6% |
| South Africa | 1 | 0-0-1 | 0-2 | **0** | 1.47 | 0.3% | 6.4% | 18.4% |

### Group B

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Bosnia and Herzegovina | 1 | 0-1-0 | 1-1 | **1** | 3.02 | 7.6% | 24.6% | 52.2% |
| Canada | 1 | 0-1-0 | 1-1 | **1** | 4.85 | 45.4% | 80.0% | 89.8% |
| Qatar | 1 | 0-1-0 | 1-1 | **1** | 2.56 | 4.8% | 17.3% | 38.7% |
| Switzerland | 1 | 0-1-0 | 1-1 | **1** | 4.62 | 42.2% | 78.0% | 86.3% |

### Group C

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Scotland | 1 | 1-0-0 | 1-0 | **3** | 4.74 | 20.7% | 47.8% | 86.6% |
| Brazil | 1 | 0-1-0 | 1-1 | **1** | 5.48 | 47.1% | 79.8% | 94.4% |
| Morocco | 1 | 0-1-0 | 1-1 | **1** | 5.07 | 31.6% | 69.6% | 90.5% |
| Haiti | 1 | 0-0-1 | 0-1 | **0** | 0.85 | 0.6% | 2.8% | 7.3% |

### Group D

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| United States | 1 | 1-0-0 | 4-1 | **3** | 5.93 | 49.1% | 83.7% | 96.4% |
| Australia | 1 | 1-0-0 | 2-0 | **3** | 5.92 | 42.7% | 83.0% | 95.2% |
| Turkey | 1 | 0-0-1 | 0-2 | **0** | 2.67 | 5.0% | 19.1% | 44.8% |
| Paraguay | 1 | 0-0-1 | 1-4 | **0** | 2.39 | 3.2% | 14.2% | 35.4% |

### Group E

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Germany | 1 | 1-0-0 | 7-1 | **3** | 6.34 | 55.2% | 86.4% | 99.7% |
| Ecuador | 0 | 0-0-0 | 0-0 | **0** | 5.59 | 33.0% | 74.0% | 93.0% |
| Ivory Coast | 0 | 0-0-0 | 0-0 | **0** | 3.85 | 11.7% | 37.4% | 69.4% |
| Curaçao | 1 | 0-0-1 | 1-7 | **0** | 1.02 | 0.2% | 2.2% | 6.5% |

### Group F

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Japan | 1 | 0-1-0 | 2-2 | **1** | 5.10 | 37.7% | 74.1% | 89.8% |
| Netherlands | 1 | 0-1-0 | 2-2 | **1** | 5.22 | 44.1% | 76.3% | 90.8% |
| Sweden | 0 | 0-0-0 | 0-0 | **0** | 2.93 | 10.2% | 27.2% | 48.4% |
| Tunisia | 0 | 0-0-0 | 0-0 | **0** | 2.58 | 8.0% | 22.4% | 40.1% |

### Group G

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| Belgium | 5.63 | 49.4% | 76.6% | 89.0% |
| Iran | 4.34 | 25.3% | 55.3% | 74.1% |
| Egypt | 3.55 | 15.2% | 39.6% | 60.8% |
| New Zealand | 2.88 | 10.2% | 28.5% | 46.7% |

### Group H

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| Spain | 7.49 | 77.4% | 97.0% | 99.5% |
| Uruguay | 5.30 | 19.8% | 79.5% | 91.5% |
| Saudi Arabia | 2.50 | 2.1% | 16.6% | 40.4% |
| Cape Verde | 1.59 | 0.6% | 7.0% | 18.5% |

### Group I

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| France | 6.27 | 59.5% | 84.5% | 94.2% |
| Norway | 4.47 | 21.0% | 57.5% | 78.5% |
| Senegal | 3.92 | 16.2% | 44.8% | 69.4% |
| Iraq | 1.92 | 3.3% | 13.2% | 26.5% |

### Group J

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| Argentina | 6.89 | 72.7% | 91.6% | 97.3% |
| Austria | 3.74 | 12.6% | 45.5% | 66.2% |
| Algeria | 3.64 | 10.7% | 43.2% | 64.9% |
| Jordan | 2.29 | 4.0% | 19.6% | 35.2% |

### Group K

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| Portugal | 5.66 | 44.8% | 78.7% | 90.9% |
| Colombia | 5.53 | 42.2% | 76.8% | 89.8% |
| Uzbekistan | 2.90 | 8.0% | 26.1% | 48.2% |
| DR Congo | 2.39 | 5.0% | 18.4% | 37.1% |

### Group L

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| England | 6.45 | 60.4% | 86.7% | 96.0% |
| Croatia | 5.00 | 26.2% | 67.8% | 86.8% |
| Panama | 3.53 | 11.5% | 36.0% | 61.9% |
| Ghana | 1.69 | 1.9% | 9.5% | 21.8% |

*\*Advance = top two or one of the eight best third-placed teams.*

## Most likely knockout bracket

Each tie shows the most probable pairing given projected group finishes, the chance the named winner goes through **in that pairing**, and how often the exact pairing occurred across all simulations.

### Round of 32

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 73 | 2026-06-28 | SoFi Stadium, Los Angeles | South Korea v Switzerland | **Switzerland** | 60.1% | 22.1% |
| 74 | 2026-06-29 | Gillette Stadium, Boston | Germany v Scotland | **Germany** | 58.8% | 5.8% |
| 75 | 2026-06-29 | Estadio BBVA, Monterrey | Netherlands v Morocco | **Netherlands** | 52.2% | 16.8% |
| 76 | 2026-06-29 | NRG Stadium, Houston | Brazil v Japan | **Brazil** | 53.5% | 17.1% |
| 77 | 2026-06-30 | MetLife Stadium, New York/New Jersey | France v Turkey | **France** | 67.7% | 6.6% |
| 78 | 2026-06-30 | AT&T Stadium, Dallas | Ecuador v Norway | **Ecuador** | 53.1% | 15.0% |
| 79 | 2026-06-30 | Estadio Azteca, Mexico City | Mexico v Ivory Coast | **Mexico** | 82.9% | 9.4% |
| 80 | 2026-07-01 | Mercedes-Benz Stadium, Atlanta | England v Saudi Arabia | **England** | 88.5% | 2.3% |
| 81 | 2026-07-01 | Levi's Stadium, San Francisco Bay Area | United States v Bosnia and Herzegovina | **United States** | 84.7% | 9.5% |
| 82 | 2026-07-01 | Lumen Field, Seattle | Belgium v Czech Republic | **Belgium** | 74.1% | 16.1% |
| 83 | 2026-07-02 | BMO Field, Toronto | Colombia v Croatia | **Colombia** | 63.0% | 14.4% |
| 84 | 2026-07-02 | SoFi Stadium, Los Angeles | Spain v Austria | **Spain** | 80.2% | 25.4% |
| 85 | 2026-07-02 | BC Place, Vancouver | Canada v Senegal | **Canada** | 57.6% | 1.9% |
| 86 | 2026-07-03 | Hard Rock Stadium, Miami | Argentina v Uruguay | **Argentina** | 76.3% | 43.3% |
| 87 | 2026-07-03 | Arrowhead Stadium, Kansas City | Portugal v Panama | **Portugal** | 70.9% | 11.7% |
| 88 | 2026-07-03 | AT&T Stadium, Dallas | Australia v Iran | **Australia** | 57.1% | 12.1% |

### Round of 16

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 89 | 2026-07-04 | Lincoln Financial Field, Philadelphia | Germany v France | **France** | 73.1% | 13.8% |
| 90 | 2026-07-04 | NRG Stadium, Houston | Switzerland v Netherlands | **Netherlands** | 70.3% | 4.6% |
| 91 | 2026-07-05 | MetLife Stadium, New York/New Jersey | Brazil v Ecuador | **Brazil** | 57.3% | 6.2% |
| 92 | 2026-07-05 | Estadio Azteca, Mexico City | Mexico v England | **Mexico** | 52.3% | 21.8% |
| 93 | 2026-07-06 | AT&T Stadium, Dallas | Colombia v Spain | **Spain** | 75.1% | 13.1% |
| 94 | 2026-07-06 | Lumen Field, Seattle | United States v Belgium | **Belgium** | 58.9% | 11.3% |
| 95 | 2026-07-07 | Mercedes-Benz Stadium, Atlanta | Argentina v Australia | **Argentina** | 74.6% | 13.1% |
| 96 | 2026-07-07 | BC Place, Vancouver | Canada v Portugal | **Portugal** | 56.6% | 9.1% |

### Quarter-finals

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 97 | 2026-07-09 | Gillette Stadium, Boston | France v Netherlands | **Netherlands** | 54.9% | 4.1% |
| 98 | 2026-07-10 | SoFi Stadium, Los Angeles | Spain v Belgium | **Spain** | 73.8% | 9.2% |
| 99 | 2026-07-11 | Hard Rock Stadium, Miami | Brazil v Mexico | **Brazil** | 55.8% | 4.8% |
| 100 | 2026-07-11 | Arrowhead Stadium, Kansas City | Argentina v Portugal | **Argentina** | 65.8% | 8.3% |

### Semi-finals

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 101 | 2026-07-14 | AT&T Stadium, Dallas | Netherlands v Spain | **Spain** | 74.0% | 3.5% |
| 102 | 2026-07-15 | Mercedes-Benz Stadium, Atlanta | Brazil v Argentina | **Argentina** | 65.1% | 2.8% |

### Final

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 104 | 2026-07-19 | MetLife Stadium, East Rutherford | Spain v Argentina | **Spain** | 56.3% | 6.6% |

**Projected champion: Spain** (overall title probability 21.2%; the single most likely path above is itself only one of many ways the tournament can unfold).

## How to read this

- All figures are probabilities, not certainties — a 65% favourite loses about one such match in three.
- `xPts` = expected group points; `xG` = expected goals from the Poisson model.
- Predictions refresh after every match day: run `python -m worldcup.run all` to pull new results, re-rate teams, and re-simulate.
- Machine-readable outputs: `match_probabilities.csv`, `tournament_projections.csv`. Past reports in `outputs/archive/`.
