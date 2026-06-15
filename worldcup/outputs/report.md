# FIFA World Cup 2026 — ML Prediction Report

*Generated 2026-06-15 · data through **2026-06-14** · 50,000 Monte Carlo simulations · 11/72 group matches played*

Probabilities come from a gradient-boosted Poisson goal model (Elo strength + rolling form + venue/importance features) trained on 30,783 internationals, simulated through the official 2026 bracket and tiebreaker rules.

*Rolling validation (7,966 matches, 2018–2026): RPS 0.1687 vs Elo-baseline 0.1711; log-loss 0.8652 vs 0.8809.*

## Title favourites

| # | Team | Group | Champion | Δ vs 2026-06-14 | Final | Semi-final | Quarter-final | Rd of 16 |
|---|------|:-----:|---------:|-------:|------:|-----------:|--------------:|---------:|
| 1 | Spain | H | **19.9%** | +0.2 | 30.0% | 41.8% | 55.1% | 71.7% |
| 2 | Argentina | J | **18.2%** | +0.2 | 27.7% | 38.2% | 52.1% | 68.0% |
| 3 | England | L | **8.5%** | -0.3 | 14.7% | 25.5% | 39.4% | 67.3% |
| 4 | France | I | **7.3%** | +0.1 | 13.8% | 27.1% | 44.3% | 65.2% |
| 5 | Brazil | C | **6.2%** | -0.3 | 12.1% | 24.1% | 40.0% | 62.6% |
| 6 | Colombia | K | **4.5%** | +0.1 | 9.3% | 16.8% | 30.6% | 58.5% |
| 7 | Portugal | K | **3.9%** | -0.4 | 8.5% | 16.1% | 31.7% | 60.1% |
| 8 | Mexico | A | **3.8%** | +0.1 | 8.9% | 19.6% | 40.9% | 68.8% |
| 9 | Japan | F | **2.7%** | – | 6.2% | 14.0% | 27.3% | 46.8% |
| 10 | Belgium | G | **2.7%** | – | 7.0% | 13.6% | 31.3% | 58.4% |
| 11 | Netherlands | F | **2.6%** | +0.2 | 6.3% | 14.9% | 28.3% | 48.6% |
| 12 | Germany | E | **2.3%** | +0.5 | 5.2% | 12.9% | 26.7% | 55.3% |
| 13 | Morocco | C | **2.2%** | +0.1 | 5.2% | 12.2% | 25.6% | 46.9% |
| 14 | Norway | I | **2.1%** | +0.3 | 5.0% | 12.5% | 26.3% | 48.4% |
| 15 | United States | D | **1.7%** | +0.1 | 4.5% | 11.0% | 28.8% | 60.8% |

## Biggest movers since last run (data through 2026-06-14)

| Team | Δ Champion | Δ Rd of 16 | Champion now |
|------|----------:|-----------:|-------------:|
| Germany | +0.5 | +2.1 | 2.3% |
| Ecuador | +0.3 | -0.3 | 1.6% |
| Norway | +0.3 | +1.2 | 2.1% |
| England | -0.3 | -2.6 | 8.5% |
| Uruguay | -0.3 | -1.3 | 1.6% |
| Scotland | -0.3 | -5.9 | 0.3% |
| Brazil | -0.3 | +0.4 | 6.2% |
| Portugal | -0.4 | -0.6 | 3.9% |

*Δ values in probability points. Full run-by-run series in `outputs/history.csv`.*

## Path to the final

The model's single most likely knockout bracket — the 16 projected round-of-16 teams and every unplayed tie, each line carrying the projected winner down to the next round until they converge on the champion. Percentages are each side's chance of advancing from that tie.

<div style="overflow-x:auto; margin:1rem 0;">
<svg viewBox="0 0 1252 652" width="100%" preserveAspectRatio="xMidYMin meet" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica,Arial,sans-serif"><path d="M94,104 C94,150 170,150 170,196" fill="none" stroke="#33436b" stroke-width="1.6"/><path d="M246,104 C246,150 170,150 170,196" fill="none" stroke="#33436b" stroke-width="1.6"/><path d="M398,104 C398,150 474,150 474,196" fill="none" stroke="#33436b" stroke-width="1.6"/><path d="M550,104 C550,150 474,150 474,196" fill="none" stroke="#33436b" stroke-width="1.6"/><path d="M702,104 C702,150 778,150 778,196" fill="none" stroke="#33436b" stroke-width="1.6"/><path d="M854,104 C854,150 778,150 778,196" fill="none" stroke="#33436b" stroke-width="1.6"/><path d="M1006,104 C1006,150 1082,150 1082,196" fill="none" stroke="#33436b" stroke-width="1.6"/><path d="M1158,104 C1158,150 1082,150 1082,196" fill="none" stroke="#33436b" stroke-width="1.6"/><path d="M170,244 C170,290 322,290 322,336" fill="none" stroke="#33436b" stroke-width="1.6"/><path d="M474,244 C474,290 322,290 322,336" fill="none" stroke="#33436b" stroke-width="1.6"/><path d="M778,244 C778,290 930,290 930,336" fill="none" stroke="#33436b" stroke-width="1.6"/><path d="M1082,244 C1082,290 930,290 930,336" fill="none" stroke="#33436b" stroke-width="1.6"/><path d="M322,384 C322,430 626,430 626,476" fill="none" stroke="#33436b" stroke-width="1.6"/><path d="M930,384 C930,430 626,430 626,476" fill="none" stroke="#33436b" stroke-width="1.6"/><path d="M626,524 C626,556 626,556 626,588" fill="none" stroke="#33436b" stroke-width="1.6"/><text x="6" y="83" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 6 80)" text-anchor="middle">ROUND OF 16</text><text x="6" y="223" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 6 220)" text-anchor="middle">QUARTER-FINALS</text><text x="6" y="363" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 6 360)" text-anchor="middle">SEMI-FINALS</text><text x="6" y="503" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 6 500)" text-anchor="middle">FINAL</text><rect x="24" y="56" width="140" height="48" rx="7" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="33" y="75" font-size="11.5" font-weight="400" fill="#7c89a3">Germany</text><text x="155" y="75" font-size="10" text-anchor="end" fill="#5d6880">29%</text><rect x="24" y="80" width="140" height="21" rx="5" fill="#4cc38a" opacity="0.16"/><text x="33" y="96" font-size="11.5" font-weight="700" fill="#7ef0b6">France</text><text x="155" y="96" font-size="10" text-anchor="end" fill="#cfe8d8">71%</text><rect x="176" y="56" width="140" height="48" rx="7" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="185" y="75" font-size="11.5" font-weight="400" fill="#7c89a3">Switzerland</text><text x="307" y="75" font-size="10" text-anchor="end" fill="#5d6880">35%</text><rect x="176" y="80" width="140" height="21" rx="5" fill="#4cc38a" opacity="0.16"/><text x="185" y="96" font-size="11.5" font-weight="700" fill="#7ef0b6">Netherlands</text><text x="307" y="96" font-size="10" text-anchor="end" fill="#cfe8d8">65%</text><rect x="328" y="56" width="140" height="48" rx="7" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="337" y="75" font-size="11.5" font-weight="400" fill="#7c89a3">Colombia</text><text x="459" y="75" font-size="10" text-anchor="end" fill="#5d6880">20%</text><rect x="328" y="80" width="140" height="21" rx="5" fill="#4cc38a" opacity="0.16"/><text x="337" y="96" font-size="11.5" font-weight="700" fill="#7ef0b6">Spain</text><text x="459" y="96" font-size="10" text-anchor="end" fill="#cfe8d8">80%</text><rect x="480" y="56" width="140" height="48" rx="7" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="489" y="75" font-size="11.5" font-weight="400" fill="#7c89a3">USA</text><text x="611" y="75" font-size="10" text-anchor="end" fill="#5d6880">39%</text><rect x="480" y="80" width="140" height="21" rx="5" fill="#4cc38a" opacity="0.16"/><text x="489" y="96" font-size="11.5" font-weight="700" fill="#7ef0b6">Belgium</text><text x="611" y="96" font-size="10" text-anchor="end" fill="#cfe8d8">61%</text><rect x="632" y="56" width="140" height="48" rx="7" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="632" y="58" width="140" height="21" rx="5" fill="#4cc38a" opacity="0.16"/><text x="641" y="75" font-size="11.5" font-weight="700" fill="#7ef0b6">Brazil</text><text x="763" y="75" font-size="10" text-anchor="end" fill="#cfe8d8">55%</text><text x="641" y="96" font-size="11.5" font-weight="400" fill="#7c89a3">Norway</text><text x="763" y="96" font-size="10" text-anchor="end" fill="#5d6880">45%</text><rect x="784" y="56" width="140" height="48" rx="7" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="784" y="58" width="140" height="21" rx="5" fill="#4cc38a" opacity="0.16"/><text x="793" y="75" font-size="11.5" font-weight="700" fill="#7ef0b6">Mexico</text><text x="915" y="75" font-size="10" text-anchor="end" fill="#cfe8d8">52%</text><text x="793" y="96" font-size="11.5" font-weight="400" fill="#7c89a3">England</text><text x="915" y="96" font-size="10" text-anchor="end" fill="#5d6880">48%</text><rect x="936" y="56" width="140" height="48" rx="7" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="936" y="58" width="140" height="21" rx="5" fill="#4cc38a" opacity="0.16"/><text x="945" y="75" font-size="11.5" font-weight="700" fill="#7ef0b6">Argentina</text><text x="1067" y="75" font-size="10" text-anchor="end" fill="#cfe8d8">74%</text><text x="945" y="96" font-size="11.5" font-weight="400" fill="#7c89a3">Australia</text><text x="1067" y="96" font-size="10" text-anchor="end" fill="#5d6880">26%</text><rect x="1088" y="56" width="140" height="48" rx="7" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="1097" y="75" font-size="11.5" font-weight="400" fill="#7c89a3">Canada</text><text x="1219" y="75" font-size="10" text-anchor="end" fill="#5d6880">45%</text><rect x="1088" y="80" width="140" height="21" rx="5" fill="#4cc38a" opacity="0.16"/><text x="1097" y="96" font-size="11.5" font-weight="700" fill="#7ef0b6">Portugal</text><text x="1219" y="96" font-size="10" text-anchor="end" fill="#cfe8d8">55%</text><rect x="100" y="196" width="140" height="48" rx="7" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="100" y="198" width="140" height="21" rx="5" fill="#4cc38a" opacity="0.16"/><text x="109" y="215" font-size="11.5" font-weight="700" fill="#7ef0b6">France</text><text x="231" y="215" font-size="10" text-anchor="end" fill="#cfe8d8">51%</text><text x="109" y="236" font-size="11.5" font-weight="400" fill="#7c89a3">Netherlands</text><text x="231" y="236" font-size="10" text-anchor="end" fill="#5d6880">49%</text><rect x="404" y="196" width="140" height="48" rx="7" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="404" y="198" width="140" height="21" rx="5" fill="#4cc38a" opacity="0.16"/><text x="413" y="215" font-size="11.5" font-weight="700" fill="#7ef0b6">Spain</text><text x="535" y="215" font-size="10" text-anchor="end" fill="#cfe8d8">72%</text><text x="413" y="236" font-size="11.5" font-weight="400" fill="#7c89a3">Belgium</text><text x="535" y="236" font-size="10" text-anchor="end" fill="#5d6880">28%</text><rect x="708" y="196" width="140" height="48" rx="7" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="708" y="198" width="140" height="21" rx="5" fill="#4cc38a" opacity="0.16"/><text x="717" y="215" font-size="11.5" font-weight="700" fill="#7ef0b6">Brazil</text><text x="839" y="215" font-size="10" text-anchor="end" fill="#cfe8d8">62%</text><text x="717" y="236" font-size="11.5" font-weight="400" fill="#7c89a3">Mexico</text><text x="839" y="236" font-size="10" text-anchor="end" fill="#5d6880">38%</text><rect x="1012" y="196" width="140" height="48" rx="7" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1012" y="198" width="140" height="21" rx="5" fill="#4cc38a" opacity="0.16"/><text x="1021" y="215" font-size="11.5" font-weight="700" fill="#7ef0b6">Argentina</text><text x="1143" y="215" font-size="10" text-anchor="end" fill="#cfe8d8">68%</text><text x="1021" y="236" font-size="11.5" font-weight="400" fill="#7c89a3">Portugal</text><text x="1143" y="236" font-size="10" text-anchor="end" fill="#5d6880">32%</text><rect x="252" y="336" width="140" height="48" rx="7" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="261" y="355" font-size="11.5" font-weight="400" fill="#7c89a3">France</text><text x="383" y="355" font-size="10" text-anchor="end" fill="#5d6880">31%</text><rect x="252" y="360" width="140" height="21" rx="5" fill="#4cc38a" opacity="0.16"/><text x="261" y="376" font-size="11.5" font-weight="700" fill="#7ef0b6">Spain</text><text x="383" y="376" font-size="10" text-anchor="end" fill="#cfe8d8">69%</text><rect x="860" y="336" width="140" height="48" rx="7" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="869" y="355" font-size="11.5" font-weight="400" fill="#7c89a3">Brazil</text><text x="991" y="355" font-size="10" text-anchor="end" fill="#5d6880">30%</text><rect x="860" y="360" width="140" height="21" rx="5" fill="#4cc38a" opacity="0.16"/><text x="869" y="376" font-size="11.5" font-weight="700" fill="#7ef0b6">Argentina</text><text x="991" y="376" font-size="10" text-anchor="end" fill="#cfe8d8">70%</text><rect x="556" y="476" width="140" height="48" rx="7" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="556" y="478" width="140" height="21" rx="5" fill="#4cc38a" opacity="0.16"/><text x="565" y="495" font-size="11.5" font-weight="700" fill="#7ef0b6">Spain</text><text x="687" y="495" font-size="10" text-anchor="end" fill="#cfe8d8">57%</text><text x="565" y="516" font-size="11.5" font-weight="400" fill="#7c89a3">Argentina</text><text x="687" y="516" font-size="10" text-anchor="end" fill="#5d6880">43%</text><rect x="536" y="588" width="180" height="44" rx="10" fill="#f5c542"/><text x="626" y="608" font-size="12.5" font-weight="800" fill="#1a1300" text-anchor="middle">🏆 Spain</text><text x="626" y="624" font-size="10" fill="#5a4a00" text-anchor="middle">projected champion · 20% to win</text></svg>
</div>

## Upcoming group matches — outcome probabilities

*(next match days; full list for all 72 group games in `match_probabilities.csv`)*

| Date | Grp | Match | Home win | Draw | Away win | xG | Likely score |
|------|:---:|-------|---------:|-----:|---------:|----|:----:|
| 2026-06-14 | F | Sweden v Tunisia | **42.5%** | 28.5% | 29.0% | 1.36–1.08 | 1-1 |
| 2026-06-15 | G | Belgium v Egypt | **56.6%** | 24.9% | 18.5% | 1.72–0.88 | 1-0 |
| 2026-06-15 | G | Iran v New Zealand | **53.3%** | 26.4% | 20.3% | 1.59–0.88 | 1-0 |
| 2026-06-15 | H | Spain v Cape Verde | **91.7%** | 6.5% | 1.8% | 3.54–0.44 | 3-0 |
| 2026-06-15 | H | Saudi Arabia v Uruguay | 16.0% | 25.9% | **58.1%** | 0.73–1.62 | 0-1 |
| 2026-06-16 | J | Austria v Jordan | **52.0%** | 25.7% | 22.3% | 1.66–1.01 | 1-1 |
| 2026-06-16 | J | Argentina v Algeria | **66.0%** | 22.1% | 12.0% | 1.90–0.68 | 1-0 |
| 2026-06-16 | I | France v Senegal | **56.3%** | 24.9% | 18.8% | 1.72–0.90 | 1-0 |
| 2026-06-16 | I | Iraq v Norway | 13.2% | 23.4% | **63.4%** | 0.68–1.79 | 0-1 |
| 2026-06-17 | K | Portugal v DR Congo | **65.8%** | 21.9% | 12.2% | 1.92–0.70 | 1-0 |
| 2026-06-17 | K | Uzbekistan v Colombia | 15.1% | 25.5% | **59.4%** | 0.70–1.64 | 0-1 |
| 2026-06-17 | L | England v Croatia | **56.4%** | 25.2% | 18.3% | 1.69–0.86 | 1-0 |
| 2026-06-17 | L | Ghana v Panama | 22.5% | 26.4% | **51.1%** | 0.98–1.59 | 1-1 |

## Group projections

### Group A

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Mexico | 1 | 1-0-0 | 2-0 | **3** | 7.40 | 73.8% | 96.1% | 99.6% |
| South Korea | 1 | 1-0-0 | 2-1 | **3** | 5.74 | 23.9% | 85.1% | 94.0% |
| Czech Republic | 1 | 0-0-1 | 1-2 | **0** | 2.28 | 1.9% | 9.8% | 45.1% |
| South Africa | 1 | 0-0-1 | 0-2 | **0** | 1.67 | 0.4% | 9.1% | 21.6% |

### Group B

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Bosnia and Herzegovina | 1 | 0-1-0 | 1-1 | **1** | 3.07 | 8.3% | 26.2% | 53.5% |
| Canada | 1 | 0-1-0 | 1-1 | **1** | 4.95 | 48.5% | 80.4% | 90.0% |
| Qatar | 1 | 0-1-0 | 1-1 | **1** | 2.58 | 5.3% | 18.8% | 39.0% |
| Switzerland | 1 | 0-1-0 | 1-1 | **1** | 4.43 | 37.9% | 74.6% | 83.7% |

### Group C

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Scotland | 1 | 1-0-0 | 1-0 | **3** | 4.64 | 18.5% | 45.3% | 83.2% |
| Brazil | 1 | 0-1-0 | 1-1 | **1** | 5.63 | 49.8% | 81.8% | 95.6% |
| Morocco | 1 | 0-1-0 | 1-1 | **1** | 5.15 | 31.3% | 70.5% | 91.2% |
| Haiti | 1 | 0-0-1 | 0-1 | **0** | 0.78 | 0.5% | 2.3% | 6.0% |

### Group D

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| United States | 1 | 1-0-0 | 4-1 | **3** | 6.06 | 51.9% | 85.4% | 97.0% |
| Australia | 1 | 1-0-0 | 2-0 | **3** | 5.80 | 40.0% | 82.0% | 94.5% |
| Turkey | 1 | 0-0-1 | 0-2 | **0** | 2.72 | 5.3% | 18.8% | 46.1% |
| Paraguay | 1 | 0-0-1 | 1-4 | **0** | 2.32 | 2.9% | 13.9% | 32.7% |

### Group E

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Germany | 1 | 1-0-0 | 7-1 | **3** | 6.24 | 55.1% | 85.0% | 99.6% |
| Ivory Coast | 1 | 1-0-0 | 1-0 | **3** | 6.16 | 35.4% | 84.9% | 95.0% |
| Ecuador | 1 | 0-0-1 | 0-1 | **0** | 3.73 | 9.2% | 27.9% | 81.0% |
| Curaçao | 1 | 0-0-1 | 1-7 | **0** | 0.94 | 0.2% | 2.2% | 5.4% |

### Group F

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Japan | 1 | 0-1-0 | 2-2 | **1** | 5.15 | 38.9% | 75.2% | 90.3% |
| Netherlands | 1 | 0-1-0 | 2-2 | **1** | 5.22 | 43.6% | 76.2% | 90.9% |
| Sweden | 0 | 0-0-0 | 0-0 | **0** | 2.95 | 9.9% | 27.2% | 48.2% |
| Tunisia | 0 | 0-0-0 | 0-0 | **0** | 2.50 | 7.5% | 21.4% | 38.1% |

### Group G

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| Belgium | 5.80 | 52.3% | 78.9% | 90.4% |
| Iran | 4.49 | 26.0% | 58.3% | 76.7% |
| Egypt | 3.41 | 13.3% | 37.3% | 57.8% |
| New Zealand | 2.74 | 8.5% | 25.4% | 43.4% |

### Group H

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| Spain | 7.28 | 74.1% | 96.1% | 99.3% |
| Uruguay | 5.27 | 22.2% | 77.8% | 90.8% |
| Saudi Arabia | 2.57 | 2.9% | 18.6% | 41.4% |
| Cape Verde | 1.68 | 0.8% | 7.5% | 19.3% |

### Group I

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| France | 6.12 | 56.2% | 82.7% | 93.2% |
| Norway | 4.76 | 25.9% | 63.1% | 82.2% |
| Senegal | 3.76 | 14.4% | 41.0% | 66.2% |
| Iraq | 1.92 | 3.5% | 13.2% | 26.2% |

### Group J

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| Argentina | 6.88 | 72.0% | 91.6% | 97.3% |
| Austria | 3.85 | 13.1% | 47.2% | 68.0% |
| Algeria | 3.69 | 11.6% | 43.5% | 65.5% |
| Jordan | 2.17 | 3.3% | 17.6% | 32.2% |

### Group K

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| Portugal | 5.70 | 45.6% | 79.1% | 91.1% |
| Colombia | 5.52 | 41.7% | 76.9% | 89.7% |
| Uzbekistan | 2.77 | 7.1% | 24.0% | 44.8% |
| DR Congo | 2.50 | 5.6% | 20.0% | 38.9% |

### Group L

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| England | 6.57 | 63.1% | 88.2% | 96.4% |
| Croatia | 4.89 | 24.3% | 66.0% | 85.7% |
| Panama | 3.50 | 10.7% | 36.2% | 61.2% |
| Ghana | 1.70 | 1.9% | 9.6% | 21.5% |

*\*Advance = top two or one of the eight best third-placed teams.*

## Most likely knockout bracket

Each tie shows the most probable pairing given projected group finishes, the chance the named winner goes through **in that pairing**, and how often the exact pairing occurred across all simulations.

### Round of 32

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 73 | 2026-06-28 | SoFi Stadium, Los Angeles | South Korea v Switzerland | **Switzerland** | 62.2% | 22.3% |
| 74 | 2026-06-29 | Gillette Stadium, Boston | Germany v Scotland | **Germany** | 58.0% | 5.6% |
| 75 | 2026-06-29 | Estadio BBVA, Monterrey | Netherlands v Morocco | **Netherlands** | 52.7% | 17.2% |
| 76 | 2026-06-29 | NRG Stadium, Houston | Brazil v Japan | **Brazil** | 62.1% | 18.0% |
| 77 | 2026-06-30 | MetLife Stadium, New York/New Jersey | France v Turkey | **France** | 68.0% | 6.4% |
| 78 | 2026-06-30 | AT&T Stadium, Dallas | Ivory Coast v Norway | **Norway** | 63.3% | 18.3% |
| 79 | 2026-06-30 | Estadio Azteca, Mexico City | Mexico v Ecuador | **Mexico** | 65.7% | 17.9% |
| 80 | 2026-07-01 | Mercedes-Benz Stadium, Atlanta | England v Saudi Arabia | **England** | 84.4% | 2.3% |
| 81 | 2026-07-01 | Levi's Stadium, San Francisco Bay Area | United States v Bosnia and Herzegovina | **United States** | 83.3% | 9.8% |
| 82 | 2026-07-01 | Lumen Field, Seattle | Belgium v Czech Republic | **Belgium** | 77.5% | 16.1% |
| 83 | 2026-07-02 | BMO Field, Toronto | Colombia v Croatia | **Colombia** | 68.9% | 14.6% |
| 84 | 2026-07-02 | SoFi Stadium, Los Angeles | Spain v Austria | **Spain** | 78.2% | 25.1% |
| 85 | 2026-07-02 | BC Place, Vancouver | Canada v Senegal | **Canada** | 60.0% | 2.3% |
| 86 | 2026-07-03 | Hard Rock Stadium, Miami | Argentina v Uruguay | **Argentina** | 78.2% | 40.0% |
| 87 | 2026-07-03 | Arrowhead Stadium, Kansas City | Portugal v Panama | **Portugal** | 73.5% | 11.3% |
| 88 | 2026-07-03 | AT&T Stadium, Dallas | Australia v Iran | **Australia** | 59.6% | 13.5% |

### Round of 16

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 89 | 2026-07-04 | Lincoln Financial Field, Philadelphia | Germany v France | **France** | 70.6% | 13.1% |
| 90 | 2026-07-04 | NRG Stadium, Houston | Switzerland v Netherlands | **Netherlands** | 64.8% | 5.0% |
| 91 | 2026-07-05 | MetLife Stadium, New York/New Jersey | Brazil v Norway | **Brazil** | 54.5% | 7.5% |
| 92 | 2026-07-05 | Estadio Azteca, Mexico City | Mexico v England | **Mexico** | 52.2% | 23.2% |
| 93 | 2026-07-06 | AT&T Stadium, Dallas | Colombia v Spain | **Spain** | 79.5% | 12.9% |
| 94 | 2026-07-06 | Lumen Field, Seattle | United States v Belgium | **Belgium** | 60.7% | 12.8% |
| 95 | 2026-07-07 | Mercedes-Benz Stadium, Atlanta | Argentina v Australia | **Argentina** | 74.0% | 13.9% |
| 96 | 2026-07-07 | BC Place, Vancouver | Canada v Portugal | **Portugal** | 54.6% | 10.1% |

### Quarter-finals

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 97 | 2026-07-09 | Gillette Stadium, Boston | France v Netherlands | **France** | 51.1% | 4.3% |
| 98 | 2026-07-10 | SoFi Stadium, Los Angeles | Spain v Belgium | **Spain** | 71.6% | 9.1% |
| 99 | 2026-07-11 | Hard Rock Stadium, Miami | Brazil v Mexico | **Brazil** | 62.4% | 6.5% |
| 100 | 2026-07-11 | Arrowhead Stadium, Kansas City | Argentina v Portugal | **Argentina** | 68.2% | 8.4% |

### Semi-finals

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 101 | 2026-07-14 | AT&T Stadium, Dallas | France v Spain | **Spain** | 68.8% | 5.7% |
| 102 | 2026-07-15 | Mercedes-Benz Stadium, Atlanta | Brazil v Argentina | **Argentina** | 70.1% | 3.7% |

### Final

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 104 | 2026-07-19 | MetLife Stadium, East Rutherford | Spain v Argentina | **Spain** | 56.6% | 6.4% |

**Projected champion: Spain** (overall title probability 19.9%; the single most likely path above is itself only one of many ways the tournament can unfold).

## How to read this

- All figures are probabilities, not certainties — a 65% favourite loses about one such match in three.
- `xPts` = expected group points; `xG` = expected goals from the Poisson model.
- Predictions refresh after every match day: run `python -m worldcup.run all` to pull new results, re-rate teams, and re-simulate.
- Machine-readable outputs: `match_probabilities.csv`, `tournament_projections.csv`. Past reports in `outputs/archive/`.

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

