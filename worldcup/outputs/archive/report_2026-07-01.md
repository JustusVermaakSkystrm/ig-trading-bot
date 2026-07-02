# FIFA World Cup 2026 — ML Prediction Report

*Generated 2026-07-02 · data through **2026-07-01** · 50,000 Monte Carlo simulations · 72/72 group matches played*

Probabilities come from a gradient-boosted Poisson goal model (Elo strength + rolling form + venue/importance features) trained on 30,854 internationals, simulated through the official 2026 bracket and tiebreaker rules.

*Rolling validation (7,966 matches, 2018–2026): RPS 0.1687 vs Elo-baseline 0.1711; log-loss 0.8652 vs 0.8809.*

## Title favourites

| # | Team | Group | Champion | Δ vs 2026-07-01 | Final | Semi-final | Quarter-final | Rd of 16 |
|---|------|:-----:|---------:|-------:|------:|-----------:|--------------:|---------:|
| 1 | Argentina ✅ | J | **23.1%** | -1.0 | 39.0% | 57.7% | 79.0% | 94.2% |
| 2 | France ✅ | I | **18.9%** | -0.4 | 32.8% | 54.0% | 72.4% | 100.0% |
| 3 | Spain ✅ | H | **16.6%** | +4.0 | 27.5% | 47.0% | 68.0% | 100.0% |
| 4 | Brazil ✅ | C | **6.8%** | – | 14.2% | 32.1% | 63.1% | 100.0% |
| 5 | Mexico ✅ | A | **6.2%** | -0.4 | 13.8% | 31.3% | 60.7% | 100.0% |
| 6 | England ✅ | L | **6.0%** | -0.1 | 11.7% | 24.6% | 39.4% | 100.0% |
| 7 | Colombia ✅ | K | **5.2%** | +0.1 | 11.5% | 23.7% | 61.8% | 89.5% |
| 8 | Morocco ✅ | C | **3.7%** | -0.3 | 9.7% | 22.0% | 58.5% | 100.0% |
| 9 | Belgium ✅ | G | **2.6%** | -0.4 | 8.4% | 21.5% | 58.1% | 100.0% |
| 10 | Portugal ✅ | K | **2.6%** | -0.6 | 6.5% | 14.4% | 25.6% | 71.0% |
| 11 | United States ✅ | D | **2.2%** | -0.3 | 6.3% | 14.6% | 41.9% | 100.0% |
| 12 | Paraguay ✅ | D | **1.4%** | – | 4.5% | 13.8% | 27.6% | 100.0% |
| 13 | Switzerland ✅ | B | **1.4%** | – | 3.5% | 7.3% | 21.8% | 57.4% |
| 14 | Norway ✅ | I | **1.2%** | -0.1 | 3.4% | 12.0% | 36.9% | 100.0% |
| 15 | Canada ✅ | B | **1.0%** | -0.2 | 3.4% | 10.2% | 41.5% | 100.0% |

## Biggest movers since last run (data through 2026-07-01)

| Team | Δ Champion | Δ Rd of 16 | Champion now |
|------|----------:|-----------:|-------------:|
| Spain | +4.0 | +25.3 | 16.6% |
| Morocco | -0.3 | – | 3.7% |
| Austria | -0.3 | -25.3 | 0.0% |
| Mexico | -0.4 | – | 6.2% |
| Belgium | -0.4 | – | 2.6% |
| France | -0.4 | – | 18.9% |
| Portugal | -0.6 | +0.1 | 2.6% |
| Argentina | -1.0 | -0.1 | 23.1% |

*Δ values in probability points. Full run-by-run series in `outputs/history.csv`.*

## 🏆 Knockout stage — the road ahead

The group stage is all but done, so the knockout bracket is the main event now. Here is the model's projected path through the Round of 32, Round of 16, quarters, semis and final. *(Full group-by-group detail is further down the page.)*

- **Projected final four:** France, Spain, Brazil, Argentina
- **Projected final:** Spain v Argentina
- **Projected champion:** 🏆 **Spain** — 16.6% to lift it
- **Round-of-32 ties mathematically locked:** 16/16

### Path to the final

The single most likely knockout bracket — each line carries the projected winner down to the next round until they converge on the champion. Percentages are each side's chance of advancing from that tie. **A gold-bordered box is a confirmed (mathematically locked) tie; a green-bordered box has been played.** As ties are played, the eliminated side drops off the diagram and the winner carries forward from the round it reaches — so the bracket shrinks toward the final. (11 knockout tie(s) played so far; 16/16 Round-of-32 ties locked.)

<div style="overflow-x:auto; margin:1rem 0;">
<svg viewBox="0 0 1964 662" width="100%" preserveAspectRatio="xMidYMin meet" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica,Arial,sans-serif"><path d="M562,98 C562,134 622,134 622,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1522,98 C1522,134 1582,134 1582,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1642,98 C1642,134 1582,134 1582,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1762,98 C1762,134 1822,134 1822,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1882,98 C1882,134 1822,134 1822,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M142,214 C142,250 262,250 262,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M382,214 C382,250 262,250 262,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M622,214 C622,250 742,250 742,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M862,214 C862,250 742,250 742,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1102,214 C1102,250 1222,250 1222,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1342,214 C1342,250 1222,250 1222,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1582,214 C1582,250 1702,250 1702,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1822,214 C1822,250 1702,250 1702,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M262,330 C262,366 502,366 502,402" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M742,330 C742,366 502,366 502,402" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1222,330 C1222,366 1462,366 1462,402" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1702,330 C1702,366 1462,366 1462,402" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M502,446 C502,482 982,482 982,518" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1462,446 C1462,482 982,482 982,518" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M982,562 C982,580 982,580 982,598" fill="none" stroke="#33436b" stroke-width="1.5"/><text x="11" y="76" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 11 76)" text-anchor="middle">ROUND OF 32</text><text x="11" y="192" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 11 192)" text-anchor="middle">ROUND OF 16</text><text x="11" y="308" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 11 308)" text-anchor="middle">QUARTER-FINALS</text><text x="11" y="424" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 11 424)" text-anchor="middle">SEMI-FINALS</text><text x="11" y="540" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 11 540)" text-anchor="middle">FINAL</text><rect x="506" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#f5c542" stroke-width="2.5"/><rect x="506" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="514" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Portugal</text><text x="610" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">71%</text><text x="514" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Croatia</text><text x="610" y="91" font-size="9" text-anchor="end" fill="#5d6880">29%</text><rect x="1466" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#f5c542" stroke-width="2.5"/><rect x="1466" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1474" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Argentina</text><text x="1570" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">94%</text><text x="1474" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">C. Verde</text><text x="1570" y="91" font-size="9" text-anchor="end" fill="#5d6880">6%</text><rect x="1586" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#f5c542" stroke-width="2.5"/><rect x="1586" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1594" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Australia</text><text x="1690" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">57%</text><text x="1594" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Egypt</text><text x="1690" y="91" font-size="9" text-anchor="end" fill="#5d6880">43%</text><rect x="1706" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#f5c542" stroke-width="2.5"/><rect x="1706" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1714" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Switzerland</text><text x="1810" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">58%</text><text x="1714" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Algeria</text><text x="1810" y="91" font-size="9" text-anchor="end" fill="#5d6880">42%</text><rect x="1826" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#f5c542" stroke-width="2.5"/><rect x="1826" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1834" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Colombia</text><text x="1930" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">89%</text><text x="1834" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Ghana</text><text x="1930" y="91" font-size="9" text-anchor="end" fill="#5d6880">11%</text><rect x="86" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#f5c542" stroke-width="2.5"/><text x="94" y="187" font-size="10.5" font-weight="400" fill="#7c89a3">Paraguay</text><text x="190" y="187" font-size="9" text-anchor="end" fill="#5d6880">28%</text><rect x="86" y="193" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="94" y="207" font-size="10.5" font-weight="700" fill="#7ef0b6">France</text><text x="190" y="207" font-size="9" text-anchor="end" fill="#cfe8d8">72%</text><rect x="326" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#f5c542" stroke-width="2.5"/><text x="334" y="187" font-size="10.5" font-weight="400" fill="#7c89a3">Canada</text><text x="430" y="187" font-size="9" text-anchor="end" fill="#5d6880">42%</text><rect x="326" y="193" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="334" y="207" font-size="10.5" font-weight="700" fill="#7ef0b6">Morocco</text><text x="430" y="207" font-size="9" text-anchor="end" fill="#cfe8d8">58%</text><rect x="566" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="574" y="187" font-size="10.5" font-weight="400" fill="#7c89a3">Portugal</text><text x="670" y="187" font-size="9" text-anchor="end" fill="#5d6880">36%</text><rect x="566" y="193" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="574" y="207" font-size="10.5" font-weight="700" fill="#7ef0b6">Spain</text><text x="670" y="207" font-size="9" text-anchor="end" fill="#cfe8d8">64%</text><rect x="806" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#f5c542" stroke-width="2.5"/><text x="814" y="187" font-size="10.5" font-weight="400" fill="#7c89a3">USA</text><text x="910" y="187" font-size="9" text-anchor="end" fill="#5d6880">41%</text><rect x="806" y="193" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="814" y="207" font-size="10.5" font-weight="700" fill="#7ef0b6">Belgium</text><text x="910" y="207" font-size="9" text-anchor="end" fill="#cfe8d8">59%</text><rect x="1046" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#f5c542" stroke-width="2.5"/><rect x="1046" y="172" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1054" y="187" font-size="10.5" font-weight="700" fill="#7ef0b6">Brazil</text><text x="1150" y="187" font-size="9" text-anchor="end" fill="#cfe8d8">63%</text><text x="1054" y="207" font-size="10.5" font-weight="400" fill="#7c89a3">Norway</text><text x="1150" y="207" font-size="9" text-anchor="end" fill="#5d6880">37%</text><rect x="1286" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#f5c542" stroke-width="2.5"/><rect x="1286" y="172" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1294" y="187" font-size="10.5" font-weight="700" fill="#7ef0b6">Mexico</text><text x="1390" y="187" font-size="9" text-anchor="end" fill="#cfe8d8">61%</text><text x="1294" y="207" font-size="10.5" font-weight="400" fill="#7c89a3">England</text><text x="1390" y="207" font-size="9" text-anchor="end" fill="#5d6880">39%</text><rect x="1526" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1526" y="172" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1534" y="187" font-size="10.5" font-weight="700" fill="#7ef0b6">Argentina</text><text x="1630" y="187" font-size="9" text-anchor="end" fill="#cfe8d8">82%</text><text x="1534" y="207" font-size="10.5" font-weight="400" fill="#7c89a3">Australia</text><text x="1630" y="207" font-size="9" text-anchor="end" fill="#5d6880">18%</text><rect x="1766" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="1774" y="187" font-size="10.5" font-weight="400" fill="#7c89a3">Switzerland</text><text x="1870" y="187" font-size="9" text-anchor="end" fill="#5d6880">32%</text><rect x="1766" y="193" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1774" y="207" font-size="10.5" font-weight="700" fill="#7ef0b6">Colombia</text><text x="1870" y="207" font-size="9" text-anchor="end" fill="#cfe8d8">68%</text><rect x="206" y="286" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="206" y="288" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="214" y="303" font-size="10.5" font-weight="700" fill="#7ef0b6">France</text><text x="310" y="303" font-size="9" text-anchor="end" fill="#cfe8d8">70%</text><text x="214" y="323" font-size="10.5" font-weight="400" fill="#7c89a3">Morocco</text><text x="310" y="323" font-size="9" text-anchor="end" fill="#5d6880">30%</text><rect x="686" y="286" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="686" y="288" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="694" y="303" font-size="10.5" font-weight="700" fill="#7ef0b6">Spain</text><text x="790" y="303" font-size="9" text-anchor="end" fill="#cfe8d8">70%</text><text x="694" y="323" font-size="10.5" font-weight="400" fill="#7c89a3">Belgium</text><text x="790" y="323" font-size="9" text-anchor="end" fill="#5d6880">30%</text><rect x="1166" y="286" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1166" y="288" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1174" y="303" font-size="10.5" font-weight="700" fill="#7ef0b6">Brazil</text><text x="1270" y="303" font-size="9" text-anchor="end" fill="#cfe8d8">56%</text><text x="1174" y="323" font-size="10.5" font-weight="400" fill="#7c89a3">Mexico</text><text x="1270" y="323" font-size="9" text-anchor="end" fill="#5d6880">44%</text><rect x="1646" y="286" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1646" y="288" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1654" y="303" font-size="10.5" font-weight="700" fill="#7ef0b6">Argentina</text><text x="1750" y="303" font-size="9" text-anchor="end" fill="#cfe8d8">70%</text><text x="1654" y="323" font-size="10.5" font-weight="400" fill="#7c89a3">Colombia</text><text x="1750" y="323" font-size="9" text-anchor="end" fill="#5d6880">30%</text><rect x="446" y="402" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="454" y="419" font-size="10.5" font-weight="400" fill="#7c89a3">France</text><text x="550" y="419" font-size="9" text-anchor="end" fill="#5d6880">50%</text><rect x="446" y="425" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="454" y="439" font-size="10.5" font-weight="700" fill="#7ef0b6">Spain</text><text x="550" y="439" font-size="9" text-anchor="end" fill="#cfe8d8">50%</text><rect x="1406" y="402" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="1414" y="419" font-size="10.5" font-weight="400" fill="#7c89a3">Brazil</text><text x="1510" y="419" font-size="9" text-anchor="end" fill="#5d6880">31%</text><rect x="1406" y="425" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1414" y="439" font-size="10.5" font-weight="700" fill="#7ef0b6">Argentina</text><text x="1510" y="439" font-size="9" text-anchor="end" fill="#cfe8d8">69%</text><rect x="926" y="518" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="926" y="520" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="934" y="535" font-size="10.5" font-weight="700" fill="#7ef0b6">Spain</text><text x="1030" y="535" font-size="9" text-anchor="end" fill="#cfe8d8">53%</text><text x="934" y="555" font-size="10.5" font-weight="400" fill="#7c89a3">Argentina</text><text x="1030" y="555" font-size="9" text-anchor="end" fill="#5d6880">47%</text><rect x="888" y="598" width="188" height="46" rx="10" fill="#f5c542"/><text x="982" y="619" font-size="13" font-weight="800" fill="#1a1300" text-anchor="middle">🏆 Spain</text><text x="982" y="635" font-size="10" fill="#5a4a00" text-anchor="middle">projected champion · 17% to win</text></svg>
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
| 83 | 2026-07-02 | BMO Field, Toronto | 🔒 Portugal v Croatia | **Portugal** | 70.8% | 🔒 locked |
| 84 | 2026-07-02 | SoFi Stadium, Los Angeles | ✅ Spain v Austria | **Spain** | 3-0 | ✅ played |
| 85 | 2026-07-02 | BC Place, Vancouver | 🔒 Switzerland v Algeria | **Switzerland** | 57.7% | 🔒 locked |
| 86 | 2026-07-03 | Hard Rock Stadium, Miami | 🔒 Argentina v Cape Verde | **Argentina** | 94.2% | 🔒 locked |
| 87 | 2026-07-03 | Arrowhead Stadium, Kansas City | 🔒 Colombia v Ghana | **Colombia** | 89.4% | 🔒 locked |
| 88 | 2026-07-03 | AT&T Stadium, Dallas | 🔒 Australia v Egypt | **Australia** | 56.6% | 🔒 locked |

#### Round of 16

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 89 | 2026-07-04 | Lincoln Financial Field, Philadelphia | 🔒 Paraguay v France | **France** | 72.3% | 🔒 locked |
| 90 | 2026-07-04 | NRG Stadium, Houston | 🔒 Canada v Morocco | **Morocco** | 58.4% | 🔒 locked |
| 91 | 2026-07-05 | MetLife Stadium, New York/New Jersey | 🔒 Brazil v Norway | **Brazil** | 63.1% | 🔒 locked |
| 92 | 2026-07-05 | Estadio Azteca, Mexico City | 🔒 Mexico v England | **Mexico** | 60.7% | 🔒 locked |
| 93 | 2026-07-06 | AT&T Stadium, Dallas | Portugal v Spain | **Spain** | 63.8% | 71.0% |
| 94 | 2026-07-06 | Lumen Field, Seattle | 🔒 United States v Belgium | **Belgium** | 58.6% | 🔒 locked |
| 95 | 2026-07-07 | Mercedes-Benz Stadium, Atlanta | Argentina v Australia | **Argentina** | 82.3% | 53.2% |
| 96 | 2026-07-07 | BC Place, Vancouver | Switzerland v Colombia | **Colombia** | 67.8% | 51.3% |

#### Quarter-finals

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 97 | 2026-07-09 | Gillette Stadium, Boston | France v Morocco | **France** | 70.0% | 42.4% |
| 98 | 2026-07-10 | SoFi Stadium, Los Angeles | Spain v Belgium | **Spain** | 69.8% | 39.8% |
| 99 | 2026-07-11 | Hard Rock Stadium, Miami | Brazil v Mexico | **Brazil** | 55.9% | 38.2% |
| 100 | 2026-07-11 | Arrowhead Stadium, Kansas City | Argentina v Colombia | **Argentina** | 69.7% | 48.9% |

#### Semi-finals

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 101 | 2026-07-14 | AT&T Stadium, Dallas | France v Spain | **Spain** | 50.4% | 25.3% |
| 102 | 2026-07-15 | Mercedes-Benz Stadium, Atlanta | Brazil v Argentina | **Argentina** | 68.9% | 18.7% |

#### Final

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 104 | 2026-07-19 | MetLife Stadium, East Rutherford | Spain v Argentina | **Spain** | 52.9% | 10.8% |

**Projected champion (this bracket): Spain** — the team that wins each projected match through to the final. The title-odds table above makes **Argentina** the overall favourite; it can differ from this bracket because a team can have the best title odds across all possible draws while still being an underdog in one specific projected tie here.

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

