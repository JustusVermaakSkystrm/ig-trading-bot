# FIFA World Cup 2026 — ML Prediction Report

*Generated 2026-06-11 · data through **2026-06-10** · 100,000 Monte Carlo simulations · 0/72 group matches played*

Probabilities come from a gradient-boosted Poisson goal model (Elo strength + rolling form + venue/importance features) trained on 30,772 internationals, simulated through the official 2026 bracket and tiebreaker rules.

*Holdout validation (2,533 matches since 2024): RPS 0.1672 vs Elo-baseline 0.1683; log-loss 0.8666 vs 0.8755.*

## Title favourites

| # | Team | Group | Champion | Final | Semi-final | Quarter-final | Rd of 16 |
|---|------|:-----:|---------:|------:|-----------:|--------------:|---------:|
| 1 | Spain | H | **20.3%** | 31.1% | 42.0% | 56.0% | 72.5% |
| 2 | Argentina | J | **16.2%** | 25.3% | 35.1% | 49.6% | 63.6% |
| 3 | England | L | **7.2%** | 12.7% | 23.0% | 36.8% | 66.2% |
| 4 | France | I | **7.0%** | 13.1% | 25.5% | 42.8% | 64.0% |
| 5 | Colombia | K | **5.5%** | 10.6% | 18.3% | 32.5% | 58.9% |
| 6 | Brazil | C | **5.1%** | 9.6% | 21.5% | 37.0% | 60.3% |
| 7 | Portugal | K | **4.2%** | 8.9% | 16.3% | 30.0% | 56.5% |
| 8 | Ecuador | E | **3.8%** | 8.1% | 17.1% | 30.4% | 57.0% |
| 9 | Mexico | A | **3.7%** | 8.6% | 19.9% | 41.0% | 68.1% |
| 10 | Belgium | G | **3.2%** | 7.6% | 14.3% | 32.1% | 58.1% |
| 11 | Netherlands | F | **2.7%** | 6.4% | 15.3% | 29.6% | 50.7% |
| 12 | Japan | F | **2.5%** | 5.9% | 13.4% | 27.2% | 48.0% |
| 13 | Uruguay | H | **2.3%** | 5.7% | 12.2% | 23.3% | 41.7% |
| 14 | Germany | E | **2.3%** | 5.4% | 13.2% | 26.4% | 52.9% |
| 15 | Norway | I | **2.2%** | 5.3% | 12.7% | 25.9% | 48.6% |

## Upcoming group matches — outcome probabilities

*(next match days; full list for all 72 group games in `match_probabilities.csv`)*

| Date | Grp | Match | Home win | Draw | Away win | xG | Likely score |
|------|:---:|-------|---------:|-----:|---------:|----|:----:|
| 2026-06-11 | A | Mexico v South Africa | **84.1%** | 12.1% | 3.8% | 2.51–0.37 | 2-0 |
| 2026-06-11 | A | South Korea v Czech Republic | **46.3%** | 26.9% | 26.8% | 1.41–1.00 | 1-1 |
| 2026-06-12 | B | Canada v Bosnia and Herzegovina | **80.4%** | 13.3% | 6.3% | 2.61–0.60 | 2-0 |
| 2026-06-12 | D | United States v Paraguay | **37.4%** | 26.6% | 36.0% | 1.30–1.27 | 1-1 |
| 2026-06-13 | B | Qatar v Switzerland | **7.4%** | 16.7% | 75.9% | 0.52–2.19 | 0-2 |
| 2026-06-13 | C | Brazil v Morocco | **46.5%** | 28.8% | 24.7% | 1.28–0.85 | 1-0 |
| 2026-06-13 | C | Haiti v Scotland | **21.9%** | 25.8% | 52.3% | 0.89–1.53 | 0-1 |
| 2026-06-13 | D | Australia v Turkey | **29.2%** | 27.4% | 43.5% | 1.05–1.34 | 1-1 |
| 2026-06-14 | F | Sweden v Tunisia | **41.8%** | 25.3% | 32.8% | 1.48–1.28 | 1-1 |
| 2026-06-14 | F | Netherlands v Japan | **38.3%** | 28.1% | 33.7% | 1.22–1.12 | 1-1 |
| 2026-06-14 | E | Germany v Curaçao | **80.5%** | 13.4% | 6.1% | 2.57–0.57 | 2-0 |
| 2026-06-14 | E | Ivory Coast v Ecuador | **21.1%** | 26.2% | 52.7% | 0.84–1.50 | 0-1 |

## Group projections

### Group A

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| Mexico | 7.12 | 74.8% | 93.5% | 98.3% |
| South Korea | 4.33 | 15.4% | 57.5% | 77.5% |
| Czech Republic | 3.43 | 7.9% | 36.6% | 61.9% |
| South Africa | 1.83 | 1.8% | 12.5% | 25.6% |

### Group B

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| Canada | 6.53 | 53.1% | 91.0% | 97.3% |
| Switzerland | 6.10 | 42.9% | 86.9% | 95.6% |
| Bosnia and Herzegovina | 2.34 | 2.5% | 13.0% | 35.7% |
| Qatar | 1.84 | 1.6% | 9.1% | 25.1% |

### Group C

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| Brazil | 6.28 | 56.7% | 85.3% | 95.1% |
| Morocco | 5.17 | 30.8% | 70.5% | 87.9% |
| Scotland | 3.39 | 10.0% | 33.1% | 60.5% |
| Haiti | 1.80 | 2.5% | 11.1% | 24.5% |

### Group D

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| Turkey | 4.60 | 32.8% | 59.6% | 76.7% |
| Paraguay | 4.13 | 24.6% | 50.6% | 69.8% |
| United States | 4.10 | 24.8% | 49.8% | 68.9% |
| Australia | 3.57 | 17.8% | 40.1% | 60.0% |

### Group E

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| Ecuador | 5.81 | 43.4% | 78.7% | 94.1% |
| Germany | 5.79 | 42.7% | 78.2% | 93.5% |
| Ivory Coast | 3.75 | 12.8% | 37.2% | 67.8% |
| Curaçao | 1.34 | 1.1% | 5.9% | 15.2% |

### Group F

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| Netherlands | 5.86 | 47.2% | 80.6% | 92.3% |
| Japan | 5.56 | 40.2% | 76.5% | 90.1% |
| Sweden | 2.94 | 8.3% | 26.5% | 50.0% |
| Tunisia | 2.28 | 4.3% | 16.4% | 35.6% |

### Group G

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| Belgium | 5.86 | 53.5% | 79.8% | 91.3% |
| Iran | 4.44 | 24.3% | 57.4% | 77.3% |
| Egypt | 3.56 | 15.1% | 40.1% | 61.0% |
| New Zealand | 2.60 | 7.1% | 22.8% | 41.3% |

### Group H

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| Spain | 7.30 | 74.6% | 95.2% | 98.8% |
| Uruguay | 5.27 | 21.2% | 78.2% | 91.3% |
| Saudi Arabia | 2.56 | 2.9% | 17.6% | 42.5% |
| Cape Verde | 1.75 | 1.3% | 9.0% | 23.3% |

### Group I

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| France | 6.05 | 55.3% | 81.3% | 92.6% |
| Norway | 4.83 | 26.1% | 63.8% | 83.6% |
| Senegal | 3.78 | 14.9% | 41.1% | 67.3% |
| Iraq | 1.97 | 3.8% | 13.7% | 27.9% |

### Group J

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| Argentina | 6.89 | 71.0% | 91.4% | 97.4% |
| Austria | 4.03 | 15.0% | 50.6% | 71.7% |
| Algeria | 3.60 | 10.8% | 41.1% | 64.3% |
| Jordan | 2.15 | 3.2% | 16.9% | 32.5% |

### Group K

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| Colombia | 5.71 | 45.0% | 79.2% | 91.3% |
| Portugal | 5.58 | 42.3% | 76.8% | 89.9% |
| Uzbekistan | 2.72 | 6.8% | 23.2% | 44.9% |
| DR Congo | 2.55 | 5.9% | 20.7% | 40.9% |

### Group L

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| England | 6.51 | 61.4% | 86.9% | 95.9% |
| Croatia | 4.77 | 23.2% | 62.4% | 84.2% |
| Panama | 3.85 | 13.5% | 41.7% | 69.6% |
| Ghana | 1.59 | 1.9% | 9.0% | 20.4% |

*\*Advance = top two or one of the eight best third-placed teams.*

## Most likely knockout bracket

Each tie shows the most probable pairing given projected group finishes, the chance the named winner goes through **in that pairing**, and how often the exact pairing occurred across all simulations.

### Round of 32

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 73 | 2026-06-28 | SoFi Stadium, Los Angeles | South Korea v Switzerland | **Switzerland** | 59.5% | 18.5% |
| 74 | 2026-06-29 | Gillette Stadium, Boston | Ecuador v Scotland | **Ecuador** | 68.6% | 4.0% |
| 75 | 2026-06-29 | Estadio BBVA, Monterrey | Netherlands v Morocco | **Netherlands** | 59.7% | 18.7% |
| 76 | 2026-06-29 | NRG Stadium, Houston | Brazil v Japan | **Brazil** | 57.8% | 20.5% |
| 77 | 2026-06-30 | MetLife Stadium, New York/New Jersey | France v Saudi Arabia | **France** | 81.6% | 4.4% |
| 78 | 2026-06-30 | AT&T Stadium, Dallas | Germany v Norway | **Germany** | 50.2% | 13.3% |
| 79 | 2026-06-30 | Estadio Azteca, Mexico City | Mexico v Ivory Coast | **Mexico** | 83.8% | 9.1% |
| 80 | 2026-07-01 | Mercedes-Benz Stadium, Atlanta | England v Senegal | **England** | 72.2% | 1.4% |
| 81 | 2026-07-01 | Levi's Stadium, San Francisco Bay Area | Turkey v Sweden | **Turkey** | 68.2% | 1.8% |
| 82 | 2026-07-01 | Lumen Field, Seattle | Belgium v Czech Republic | **Belgium** | 69.1% | 10.7% |
| 83 | 2026-07-02 | BMO Field, Toronto | Portugal v Croatia | **Portugal** | 62.9% | 13.6% |
| 84 | 2026-07-02 | SoFi Stadium, Los Angeles | Spain v Austria | **Spain** | 77.1% | 26.5% |
| 85 | 2026-07-02 | BC Place, Vancouver | Canada v Algeria | **Canada** | 66.4% | 2.3% |
| 86 | 2026-07-03 | Hard Rock Stadium, Miami | Argentina v Uruguay | **Argentina** | 69.9% | 40.5% |
| 87 | 2026-07-03 | Arrowhead Stadium, Kansas City | Colombia v Panama | **Colombia** | 71.2% | 12.7% |
| 88 | 2026-07-03 | AT&T Stadium, Dallas | Paraguay v Iran | **Paraguay** | 55.6% | 8.6% |

### Round of 16

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 89 | 2026-07-04 | Lincoln Financial Field, Philadelphia | Ecuador v France | **France** | 58.4% | 11.2% |
| 90 | 2026-07-04 | NRG Stadium, Houston | Switzerland v Netherlands | **Netherlands** | 61.8% | 7.1% |
| 91 | 2026-07-05 | MetLife Stadium, New York/New Jersey | Brazil v Germany | **Brazil** | 53.0% | 6.2% |
| 92 | 2026-07-05 | Estadio Azteca, Mexico City | Mexico v England | **Mexico** | 53.8% | 23.4% |
| 93 | 2026-07-06 | AT&T Stadium, Dallas | Portugal v Spain | **Spain** | 75.1% | 11.6% |
| 94 | 2026-07-06 | Lumen Field, Seattle | Turkey v Belgium | **Belgium** | 60.0% | 7.4% |
| 95 | 2026-07-07 | Mercedes-Benz Stadium, Atlanta | Argentina v Paraguay | **Argentina** | 80.4% | 7.5% |
| 96 | 2026-07-07 | BC Place, Vancouver | Canada v Colombia | **Colombia** | 59.4% | 10.9% |

### Quarter-finals

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 97 | 2026-07-09 | Gillette Stadium, Boston | France v Netherlands | **France** | 53.8% | 4.5% |
| 98 | 2026-07-10 | SoFi Stadium, Los Angeles | Spain v Belgium | **Spain** | 70.2% | 9.6% |
| 99 | 2026-07-11 | Hard Rock Stadium, Miami | Brazil v Mexico | **Brazil** | 52.9% | 6.6% |
| 100 | 2026-07-11 | Arrowhead Stadium, Kansas City | Argentina v Colombia | **Argentina** | 60.0% | 7.9% |

### Semi-finals

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 101 | 2026-07-14 | AT&T Stadium, Dallas | France v Spain | **Spain** | 65.1% | 5.2% |
| 102 | 2026-07-15 | Mercedes-Benz Stadium, Atlanta | Brazil v Argentina | **Argentina** | 76.4% | 3.0% |

### Final

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 104 | 2026-07-19 | MetLife Stadium, East Rutherford | Spain v Argentina | **Spain** | 56.4% | 5.9% |

**Projected champion: Spain** (overall title probability 20.3%; the single most likely path above is itself only one of many ways the tournament can unfold).

## How to read this

- All figures are probabilities, not certainties — a 65% favourite loses about one such match in three.
- `xPts` = expected group points; `xG` = expected goals from the Poisson model.
- Predictions refresh after every match day: run `python -m worldcup.run all` to pull new results, re-rate teams, and re-simulate.
- Machine-readable outputs: `match_probabilities.csv`, `tournament_projections.csv`. Past reports in `outputs/archive/`.
