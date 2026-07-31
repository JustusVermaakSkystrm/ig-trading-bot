# FIFA World Cup 2026 — ML Prediction Report

*Generated 2026-07-31 · data through **2026-07-19** · 50,000 Monte Carlo simulations · 72/72 group matches played*

Probabilities come from a gradient-boosted Poisson goal model (Elo strength + rolling form + venue/importance features) trained on 30,882 internationals, simulated through the official 2026 bracket and tiebreaker rules.

*Rolling validation (7,966 matches, 2018–2026): RPS 0.1687 vs Elo-baseline 0.1711; log-loss 0.8652 vs 0.8809.*

## Title favourites

| # | Team | Group | Champion | Δ vs 2026-07-19 | Final | Semi-final | Quarter-final | Rd of 16 |
|---|------|:-----:|---------:|-------:|------:|-----------:|--------------:|---------:|
| 1 | Spain ✅ | H | **60.3%** | +1.3 | 100.0% | 100.0% | 100.0% | 100.0% |
| 2 | Argentina ✅ | J | **39.7%** | -1.3 | 100.0% | 100.0% | 100.0% | 100.0% |
| 3 | France ✅ | I | **0.0%** | – | 0.0% | 100.0% | 100.0% | 100.0% |
| 4 | England ✅ | L | **0.0%** | – | 0.0% | 100.0% | 100.0% | 100.0% |
| 5 | Mexico ✅ | A | **0.0%** | – | 0.0% | 0.0% | 0.0% | 100.0% |
| 6 | South Korea | A | **0.0%** | – | 0.0% | 0.0% | 0.0% | 0.0% |
| 7 | South Africa ✅ | A | **0.0%** | – | 0.0% | 0.0% | 0.0% | 0.0% |
| 8 | Czech Republic | A | **0.0%** | – | 0.0% | 0.0% | 0.0% | 0.0% |
| 9 | Canada ✅ | B | **0.0%** | – | 0.0% | 0.0% | 0.0% | 100.0% |
| 10 | Switzerland ✅ | B | **0.0%** | – | 0.0% | 0.0% | 100.0% | 100.0% |
| 11 | Qatar | B | **0.0%** | – | 0.0% | 0.0% | 0.0% | 0.0% |
| 12 | Bosnia and Herzegovina ✅ | B | **0.0%** | – | 0.0% | 0.0% | 0.0% | 0.0% |
| 13 | Brazil ✅ | C | **0.0%** | – | 0.0% | 0.0% | 0.0% | 100.0% |
| 14 | Morocco ✅ | C | **0.0%** | – | 0.0% | 0.0% | 100.0% | 100.0% |
| 15 | Haiti | C | **0.0%** | – | 0.0% | 0.0% | 0.0% | 0.0% |

## Biggest movers since last run (data through 2026-07-19)

| Team | Δ Champion | Δ Rd of 16 | Champion now |
|------|----------:|-----------:|-------------:|
| Spain | +1.3 | – | 60.3% |
| France | – | – | 0.0% |
| England | – | – | 0.0% |
| Mexico | – | – | 0.0% |
| South Korea | – | – | 0.0% |
| South Africa | – | – | 0.0% |
| Czech Republic | – | – | 0.0% |
| Argentina | -1.3 | – | 39.7% |

*Δ values in probability points. Full run-by-run series in `outputs/history.csv`.*

## 🏆 Knockout stage — the road ahead

The group stage is all but done, so the knockout bracket is the main event now. Here is the model's projected path through the Round of 32, Round of 16, quarters, semis and final. *(Full group-by-group detail is further down the page.)*

- **Projected final four:** France, Spain, England, Argentina
- **Projected final:** Spain v Argentina
- **Projected champion:** 🏆 **Spain** — 60.3% to lift it
- **Round-of-32 ties mathematically locked:** 16/16

### Path to the final

The single most likely knockout bracket — each line carries the projected winner down to the next round until they converge on the champion. Percentages are each side's chance of advancing from that tie. **A gold-bordered box is a confirmed (mathematically locked) tie; a green-bordered box has been played.** As ties are played, the eliminated side drops off the diagram and the winner carries forward from the round it reaches — so the bracket shrinks toward the final. (30 knockout tie(s) played so far; 16/16 Round-of-32 ties locked.)

<div style="overflow-x:auto; margin:1rem 0;">
<svg viewBox="0 0 242 205" width="100%" preserveAspectRatio="xMidYMin meet" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica,Arial,sans-serif"><path d="M121.0,92.0 C121.0,111.5 121.0,111.5 121.0,131.0" fill="none" stroke="#33436b" stroke-width="1.5"/><text x="11" y="66" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 11 66)" text-anchor="middle">FINAL</text><rect x="26.0" y="40.0" width="190" height="52" rx="6" fill="#161e31" stroke="#f5c542" stroke-width="2.5"/><rect x="26.0" y="42.0" width="190" height="23.0" rx="4" fill="#4cc38a" opacity="0.16"/><text x="34.0" y="57.9" font-size="14" font-weight="700" fill="#7ef0b6">Spain</text><text x="208.0" y="57.9" font-size="11" text-anchor="end" fill="#cfe8d8">60%</text><text x="34.0" y="83.9" font-size="14" font-weight="400" fill="#7c89a3">Argentina</text><text x="208.0" y="83.9" font-size="11" text-anchor="end" fill="#5d6880">40%</text><rect x="6" y="131" width="230" height="52" rx="10" fill="#f5c542"/><text x="121" y="155" font-size="15" font-weight="800" fill="#1a1300" text-anchor="middle">🏆 Spain</text><text x="121" y="170" font-size="11" fill="#5a4a00" text-anchor="middle">projected champion · 60% to win</text></svg>
</div>

### Round-by-round projections

Every tie shows the projected pairing and **the side favoured to win that single match** (it always advances — 'Win prob' is its chance in that one game). **🔒 marks a confirmed tie** (the same two teams in every simulation), **✅ a played tie**. Note: this is the single most likely match-by-match path, so the team that emerges as champion here is the one that wins each projected game — which is usually, but not always, the same as the favourite in the title-odds table at the top of the page (that table averages over every possible draw). (16/16 Round-of-32 ties locked so far.)

#### Round of 32

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 73 | 2026-06-28 | SoFi Stadium, Los Angeles | ✅ South Africa v Canada | **Canada** | 0-1 | ✅ played |
| 74 | 2026-06-29 | Gillette Stadium, Boston | ✅ Germany v Paraguay | **Paraguay** | 1-1 (4-3 pens) | ✅ played |
| 75 | 2026-06-29 | Estadio BBVA, Monterrey | ✅ Netherlands v Morocco | **Morocco** | 1-1 (3-2 pens) | ✅ played |
| 76 | 2026-06-29 | NRG Stadium, Houston | ✅ Brazil v Japan | **Brazil** | 2-1 | ✅ played |
| 77 | 2026-06-30 | MetLife Stadium, New York/New Jersey | ✅ France v Sweden | **France** | 3-0 | ✅ played |
| 78 | 2026-06-30 | AT&T Stadium, Dallas | ✅ Ivory Coast v Norway | **Norway** | 1-2 | ✅ played |
| 79 | 2026-06-30 | Estadio Azteca, Mexico City | ✅ Mexico v Ecuador | **Mexico** | 2-0 | ✅ played |
| 80 | 2026-07-01 | Mercedes-Benz Stadium, Atlanta | ✅ England v DR Congo | **England** | 2-1 | ✅ played |
| 81 | 2026-07-01 | Levi's Stadium, San Francisco Bay Area | ✅ United States v Bosnia and Herzegovina | **United States** | 2-0 | ✅ played |
| 82 | 2026-07-01 | Lumen Field, Seattle | ✅ Belgium v Senegal | **Belgium** | 3-2 | ✅ played |
| 83 | 2026-07-02 | BMO Field, Toronto | ✅ Portugal v Croatia | **Portugal** | 2-1 | ✅ played |
| 84 | 2026-07-02 | SoFi Stadium, Los Angeles | ✅ Spain v Austria | **Spain** | 3-0 | ✅ played |
| 85 | 2026-07-02 | BC Place, Vancouver | ✅ Switzerland v Algeria | **Switzerland** | 2-0 | ✅ played |
| 86 | 2026-07-03 | Hard Rock Stadium, Miami | ✅ Argentina v Cape Verde | **Argentina** | 3-2 (aet) | ✅ played |
| 87 | 2026-07-03 | Arrowhead Stadium, Kansas City | ✅ Colombia v Ghana | **Colombia** | 1-0 | ✅ played |
| 88 | 2026-07-03 | AT&T Stadium, Dallas | ✅ Australia v Egypt | **Egypt** | 1-1 (4-2 pens) | ✅ played |

#### Round of 16

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 89 | 2026-07-04 | Lincoln Financial Field, Philadelphia | ✅ Paraguay v France | **France** | 0-1 | ✅ played |
| 90 | 2026-07-04 | NRG Stadium, Houston | ✅ Canada v Morocco | **Morocco** | 0-3 | ✅ played |
| 91 | 2026-07-05 | MetLife Stadium, New York/New Jersey | ✅ Brazil v Norway | **Norway** | 1-2 | ✅ played |
| 92 | 2026-07-05 | Estadio Azteca, Mexico City | ✅ Mexico v England | **England** | 2-3 | ✅ played |
| 93 | 2026-07-06 | AT&T Stadium, Dallas | ✅ Portugal v Spain | **Spain** | 0-1 | ✅ played |
| 94 | 2026-07-06 | Lumen Field, Seattle | ✅ United States v Belgium | **Belgium** | 1-4 | ✅ played |
| 95 | 2026-07-07 | Mercedes-Benz Stadium, Atlanta | ✅ Argentina v Egypt | **Argentina** | 3-2 | ✅ played |
| 96 | 2026-07-07 | BC Place, Vancouver | ✅ Switzerland v Colombia | **Switzerland** | 0-0 (4-3 pens) | ✅ played |

#### Quarter-finals

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 97 | 2026-07-09 | Gillette Stadium, Boston | ✅ France v Morocco | **France** | 2-0 | ✅ played |
| 98 | 2026-07-10 | SoFi Stadium, Los Angeles | ✅ Spain v Belgium | **Spain** | 2-1 | ✅ played |
| 99 | 2026-07-11 | Hard Rock Stadium, Miami | ✅ Norway v England | **England** | 1-2 (aet) | ✅ played |
| 100 | 2026-07-11 | Arrowhead Stadium, Kansas City | ✅ Argentina v Switzerland | **Argentina** | 3-1 | ✅ played |

#### Semi-finals

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 101 | 2026-07-14 | AT&T Stadium, Dallas | ✅ France v Spain | **Spain** | 0-2 | ✅ played |
| 102 | 2026-07-15 | Mercedes-Benz Stadium, Atlanta | ✅ England v Argentina | **Argentina** | 1-2 | ✅ played |

#### Final

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 104 | 2026-07-19 | MetLife Stadium, East Rutherford | 🔒 Spain v Argentina | **Spain** | 60.4% | 🔒 locked |

**Projected champion (this bracket): Spain** — the team that wins each projected match through to the final. This matches the title-odds favourite (**Spain**) at the top of the page.

## Group stage — results & projections

### Group tables & qualification

#### Group A

**✅ Into the knockouts:** Mexico, South Africa

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Mexico ✅ | 3 | 3-0-0 | 6-0 | **9** | 9.00 | 100.0% | 100.0% | 100.0% |
| South Africa ✅ | 3 | 1-1-1 | 2-3 | **4** | 4.00 | 0.0% | 100.0% | 100.0% |
| South Korea | 3 | 1-0-2 | 2-3 | **3** | 3.00 | 0.0% | 0.0% | 0.0% |
| Czech Republic | 3 | 0-1-2 | 2-6 | **1** | 1.00 | 0.0% | 0.0% | 0.0% |

#### Group B

**✅ Into the knockouts:** Canada, Switzerland, Bosnia and Herzegovina

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Switzerland ✅ | 3 | 2-1-0 | 7-3 | **7** | 7.00 | 100.0% | 100.0% | 100.0% |
| Canada ✅ | 3 | 1-1-1 | 8-3 | **4** | 4.00 | 0.0% | 100.0% | 100.0% |
| Bosnia and Herzegovina ✅ | 3 | 1-1-1 | 5-6 | **4** | 4.00 | 0.0% | 0.0% | 100.0% |
| Qatar | 3 | 0-1-2 | 2-10 | **1** | 1.00 | 0.0% | 0.0% | 0.0% |

#### Group C

**✅ Into the knockouts:** Brazil, Morocco

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Brazil ✅ | 3 | 2-1-0 | 7-1 | **7** | 7.00 | 100.0% | 100.0% | 100.0% |
| Morocco ✅ | 3 | 2-1-0 | 6-3 | **7** | 7.00 | 0.0% | 100.0% | 100.0% |
| Scotland | 3 | 1-0-2 | 1-4 | **3** | 3.00 | 0.0% | 0.0% | 0.0% |
| Haiti | 3 | 0-0-3 | 2-8 | **0** | 0.00 | 0.0% | 0.0% | 0.0% |

#### Group D

**✅ Into the knockouts:** United States, Paraguay, Australia

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| United States ✅ | 3 | 2-0-1 | 8-4 | **6** | 6.00 | 100.0% | 100.0% | 100.0% |
| Australia ✅ | 3 | 1-1-1 | 2-2 | **4** | 4.00 | 0.0% | 100.0% | 100.0% |
| Paraguay ✅ | 3 | 1-1-1 | 2-4 | **4** | 4.00 | 0.0% | 0.0% | 100.0% |
| Turkey | 3 | 1-0-2 | 3-5 | **3** | 3.00 | 0.0% | 0.0% | 0.0% |

#### Group E

**✅ Into the knockouts:** Germany, Ivory Coast, Ecuador

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Germany ✅ | 3 | 2-0-1 | 10-4 | **6** | 6.00 | 100.0% | 100.0% | 100.0% |
| Ivory Coast ✅ | 3 | 2-0-1 | 4-2 | **6** | 6.00 | 0.0% | 100.0% | 100.0% |
| Ecuador ✅ | 3 | 1-1-1 | 2-2 | **4** | 4.00 | 0.0% | 0.0% | 100.0% |
| Curaçao | 3 | 0-1-2 | 1-9 | **1** | 1.00 | 0.0% | 0.0% | 0.0% |

#### Group F

**✅ Into the knockouts:** Netherlands, Japan, Sweden

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Netherlands ✅ | 3 | 2-1-0 | 10-4 | **7** | 7.00 | 100.0% | 100.0% | 100.0% |
| Japan ✅ | 3 | 1-2-0 | 7-3 | **5** | 5.00 | 0.0% | 100.0% | 100.0% |
| Sweden ✅ | 3 | 1-1-1 | 7-7 | **4** | 4.00 | 0.0% | 0.0% | 100.0% |
| Tunisia | 3 | 0-0-3 | 2-12 | **0** | 0.00 | 0.0% | 0.0% | 0.0% |

#### Group G

**✅ Into the knockouts:** Belgium, Egypt

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Belgium ✅ | 3 | 1-2-0 | 6-2 | **5** | 5.00 | 100.0% | 100.0% | 100.0% |
| Egypt ✅ | 3 | 1-2-0 | 5-3 | **5** | 5.00 | 0.0% | 100.0% | 100.0% |
| Iran | 3 | 0-3-0 | 3-3 | **3** | 3.00 | 0.0% | 0.0% | 0.0% |
| New Zealand | 3 | 0-1-2 | 4-10 | **1** | 1.00 | 0.0% | 0.0% | 0.0% |

#### Group H

**✅ Into the knockouts:** Spain, Cape Verde

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Spain ✅ | 3 | 2-1-0 | 5-0 | **7** | 7.00 | 100.0% | 100.0% | 100.0% |
| Cape Verde ✅ | 3 | 0-3-0 | 2-2 | **3** | 3.00 | 0.0% | 100.0% | 100.0% |
| Uruguay | 3 | 0-2-1 | 3-4 | **2** | 2.00 | 0.0% | 0.0% | 0.0% |
| Saudi Arabia | 3 | 0-2-1 | 1-5 | **2** | 2.00 | 0.0% | 0.0% | 0.0% |

#### Group I

**✅ Into the knockouts:** France, Senegal, Norway

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| France ✅ | 3 | 3-0-0 | 10-2 | **9** | 9.00 | 100.0% | 100.0% | 100.0% |
| Norway ✅ | 3 | 2-0-1 | 8-7 | **6** | 6.00 | 0.0% | 100.0% | 100.0% |
| Senegal ✅ | 3 | 1-0-2 | 8-6 | **3** | 3.00 | 0.0% | 0.0% | 100.0% |
| Iraq | 3 | 0-0-3 | 1-12 | **0** | 0.00 | 0.0% | 0.0% | 0.0% |

#### Group J

**✅ Into the knockouts:** Argentina, Algeria, Austria

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Argentina ✅ | 3 | 3-0-0 | 8-1 | **9** | 9.00 | 100.0% | 100.0% | 100.0% |
| Austria ✅ | 3 | 1-1-1 | 6-6 | **4** | 4.00 | 0.0% | 100.0% | 100.0% |
| Algeria ✅ | 3 | 1-1-1 | 5-7 | **4** | 4.00 | 0.0% | 0.0% | 100.0% |
| Jordan | 3 | 0-0-3 | 3-8 | **0** | 0.00 | 0.0% | 0.0% | 0.0% |

#### Group K

**✅ Into the knockouts:** Portugal, DR Congo, Colombia

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Colombia ✅ | 3 | 2-1-0 | 4-1 | **7** | 7.00 | 100.0% | 100.0% | 100.0% |
| Portugal ✅ | 3 | 1-2-0 | 6-1 | **5** | 5.00 | 0.0% | 100.0% | 100.0% |
| DR Congo ✅ | 3 | 1-1-1 | 4-3 | **4** | 4.00 | 0.0% | 0.0% | 100.0% |
| Uzbekistan | 3 | 0-0-3 | 2-11 | **0** | 0.00 | 0.0% | 0.0% | 0.0% |

#### Group L

**✅ Into the knockouts:** England, Croatia, Ghana

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| England ✅ | 3 | 2-1-0 | 6-2 | **7** | 7.00 | 100.0% | 100.0% | 100.0% |
| Croatia ✅ | 3 | 2-0-1 | 5-5 | **6** | 6.00 | 0.0% | 100.0% | 100.0% |
| Ghana ✅ | 3 | 1-1-1 | 2-2 | **4** | 4.00 | 0.0% | 0.0% | 100.0% |
| Panama | 3 | 0-0-3 | 0-4 | **0** | 0.00 | 0.0% | 0.0% | 0.0% |

*\*Advance = top two or one of the eight best third-placed teams.*

*✅ = already reached the knockout stage — locked into the Round of 32 in every simulation. (Reaching later rounds still requires winning knockout games, so those stay below 100%.)*

## How to read this

- All figures are probabilities, not certainties — a 65% favourite loses about one such match in three.
- `xPts` = expected group points; `xG` = expected goals from the Poisson model.
- Predictions refresh after every match day: run `python -m worldcup.run all` to pull new results, re-rate teams, and re-simulate.
- Machine-readable outputs: `match_probabilities.csv`, `tournament_projections.csv`. Past reports in `outputs/archive/`.

## Model scorecard

**43 of 72 match outcomes called correctly** (the model's own probabilities expected ≈41.5 of 72) · exact scoreline predicted 6/72 · average probability placed on what actually happened: **45.9%** (33.3% = guessing).

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
| Ivory Coast v Ecuador | Ecuador win (48.2%) | 1-1 | 1-0 | ❌ | — |
| Germany v Curaçao | Germany win (84.5%) | 2-0 | 7-1 | ✅ | — |
| Sweden v Tunisia | Sweden win (42.5%) | 1-1 | 5-1 | ✅ | — |
| Netherlands v Japan | Netherlands win (36.1%) | 1-1 | 2-2 | ❌ | — |
| Belgium v Egypt | Belgium win (56.6%) | 1-1 | 1-1 | ❌ | ✅ |
| Iran v New Zealand | Iran win (54.6%) | 1-0 | 2-2 | ❌ | — |
| Spain v Cape Verde | Spain win (90.5%) | 3-0 | 0-0 | ❌ | — |
| Saudi Arabia v Uruguay | Uruguay win (62.1%) | 0-1 | 1-1 | ❌ | — |
| Iraq v Norway | Norway win (59.1%) | 0-1 | 1-4 | ✅ | — |
| France v Senegal | France win (59.1%) | 1-0 | 3-1 | ✅ | — |
| Austria v Jordan | Austria win (47.0%) | 1-1 | 3-1 | ✅ | — |
| Argentina v Algeria | Argentina win (68.0%) | 2-0 | 3-0 | ✅ | — |
| Portugal v DR Congo | Portugal win (70.6%) | 2-0 | 1-1 | ❌ | — |
| Uzbekistan v Colombia | Colombia win (53.9%) | 0-1 | 1-3 | ✅ | — |
| England v Croatia | England win (56.9%) | 1-0 | 4-2 | ✅ | — |
| Ghana v Panama | Panama win (51.9%) | 1-1 | 1-0 | ❌ | — |
| Czech Republic v South Africa | Czech Republic win (55.5%) | 1-0 | 1-1 | ❌ | — |
| Mexico v South Korea | Mexico win (51.1%) | 1-1 | 1-0 | ✅ | — |
| Switzerland v Bosnia and Herzegovina | Switzerland win (66.8%) | 2-0 | 4-1 | ✅ | — |
| Canada v Qatar | Canada win (74.0%) | 2-0 | 6-0 | ✅ | — |
| United States v Australia | Australia win (35.9%) | 1-1 | 2-0 | ❌ | — |
| Turkey v Paraguay | Paraguay win (38.4%) | 1-1 | 0-1 | ✅ | — |
| Scotland v Morocco | Morocco win (49.3%) | 1-1 | 0-1 | ✅ | — |
| Brazil v Haiti | Brazil win (81.3%) | 2-0 | 3-0 | ✅ | — |
| Germany v Ivory Coast | Germany win (50.9%) | 1-1 | 2-1 | ✅ | — |
| Ecuador v Curaçao | Ecuador win (81.9%) | 2-0 | 0-0 | ❌ | — |
| Netherlands v Sweden | Netherlands win (52.8%) | 1-1 | 5-1 | ✅ | — |
| Tunisia v Japan | Japan win (63.1%) | 0-2 | 0-4 | ✅ | — |
| Belgium v Iran | Belgium win (46.7%) | 1-1 | 0-0 | ❌ | — |
| New Zealand v Egypt | Egypt win (38.7%) | 1-1 | 1-3 | ✅ | — |
| Spain v Saudi Arabia | Spain win (78.3%) | 2-0 | 4-0 | ✅ | — |
| Uruguay v Cape Verde | Uruguay win (72.7%) | 2-0 | 2-2 | ❌ | — |
| France v Iraq | France win (76.5%) | 2-0 | 3-0 | ✅ | — |
| Norway v Senegal | Norway win (47.5%) | 1-1 | 3-2 | ✅ | — |
| Argentina v Austria | Argentina win (66.2%) | 2-0 | 2-0 | ✅ | ✅ |
| Jordan v Algeria | Algeria win (52.0%) | 1-1 | 1-2 | ✅ | — |
| Portugal v Uzbekistan | Portugal win (63.7%) | 1-0 | 5-0 | ✅ | — |
| Colombia v DR Congo | Colombia win (65.4%) | 2-0 | 1-0 | ✅ | — |
| England v Ghana | England win (75.8%) | 2-0 | 0-0 | ❌ | — |
| Panama v Croatia | Croatia win (42.4%) | 1-1 | 0-1 | ✅ | — |
| Canada v Switzerland | Canada win (37.9%) | 1-1 | 1-2 | ❌ | — |
| South Africa v South Korea | South Korea win (56.4%) | 0-1 | 1-0 | ❌ | — |
| Mexico v Czech Republic | Mexico win (78.6%) | 2-0 | 3-0 | ✅ | — |
| Bosnia and Herzegovina v Qatar | Bosnia and Herzegovina win (47.3%) | 1-1 | 3-1 | ✅ | — |
| Morocco v Haiti | Morocco win (72.8%) | 2-0 | 4-2 | ✅ | — |
| Scotland v Brazil | Brazil win (58.8%) | 0-1 | 0-3 | ✅ | — |
| United States v Turkey | United States win (50.7%) | 1-1 | 2-3 | ❌ | — |
| Paraguay v Australia | Australia win (38.1%) | 1-1 | 0-0 | ❌ | — |
| Curaçao v Ivory Coast | Ivory Coast win (57.6%) | 0-1 | 0-2 | ✅ | — |
| Ecuador v Germany | Germany win (40.9%) | 1-1 | 2-1 | ❌ | — |
| Japan v Sweden | Japan win (61.5%) | 2-0 | 1-1 | ❌ | — |
| Tunisia v Netherlands | Netherlands win (71.3%) | 0-2 | 1-3 | ✅ | — |
| Cape Verde v Saudi Arabia | Saudi Arabia win (37.8%) | 1-1 | 0-0 | ❌ | — |
| Egypt v Iran | Iran win (38.4%) | 1-1 | 1-1 | ❌ | ✅ |
| New Zealand v Belgium | Belgium win (62.3%) | 0-1 | 0-3 | ✅ | — |
| Norway v France | France win (60.9%) | 1-1 | 1-4 | ✅ | — |
| Senegal v Iraq | Senegal win (58.4%) | 1-0 | 5-0 | ✅ | — |
| Uruguay v Spain | Spain win (62.1%) | 0-1 | 0-1 | ✅ | ✅ |
| DR Congo v Uzbekistan | DR Congo win (38.9%) | 1-1 | 3-1 | ✅ | — |
| Panama v England | England win (69.4%) | 0-2 | 0-2 | ✅ | ✅ |
| Algeria v Austria | Austria win (40.3%) | 1-1 | 3-3 | ❌ | — |
| Jordan v Argentina | Argentina win (82.9%) | 0-2 | 1-3 | ✅ | — |
| Colombia v Portugal | Colombia win (43.3%) | 1-1 | 0-0 | ❌ | — |
| Croatia v Ghana | Croatia win (62.6%) | 1-0 | 2-1 | ✅ | — |

**Calibration vs benchmarks** (the 9 graded games with bookmaker prices on file) — log-loss, lower is better. This is the honest test: is the model bad, or were the games hard for everyone?

| Forecaster | Log-loss |
|------------|---------:|
| **This model** | **1.193** |
| Sky Bet (de-vigged) | 1.156 |
| Coin-flip (33/33/33) | 1.099 |

The model is **essentially level with the market** (+0.037 log-loss). Note both the model **and** the bookmaker scored worse than a coin-flip here — with this many draws and upsets, the slate was close to unforecastable for anyone, which is the real reason the hit-rate looks poor.


*Predictions are frozen at the last run before each result arrives, then graded — the scorecard never grades a model that has already seen the answer.*

