# FIFA World Cup 2026 — ML Prediction Report

*Generated 2026-06-22 · data through **2026-06-21** · 50,000 Monte Carlo simulations · 40/72 group matches played*

Probabilities come from a gradient-boosted Poisson goal model (Elo strength + rolling form + venue/importance features) trained on 30,812 internationals, simulated through the official 2026 bracket and tiebreaker rules.

*Rolling validation (7,966 matches, 2018–2026): RPS 0.1687 vs Elo-baseline 0.1711; log-loss 0.8652 vs 0.8809.*

## Title favourites

| # | Team | Group | Champion | Δ vs 2026-06-21 | Final | Semi-final | Quarter-final | Rd of 16 |
|---|------|:-----:|---------:|-------:|------:|-----------:|--------------:|---------:|
| 1 | Argentina | J | **22.1%** | – | 34.6% | 49.7% | 66.7% | 82.3% |
| 2 | Spain ✅ | H | **17.9%** | – | 28.1% | 40.3% | 55.0% | 73.0% |
| 3 | France | I | **8.6%** | – | 16.2% | 30.2% | 49.5% | 72.6% |
| 4 | England | L | **8.4%** | – | 15.1% | 28.5% | 43.3% | 73.1% |
| 5 | Colombia | K | **5.7%** | – | 11.2% | 20.6% | 42.1% | 73.2% |
| 6 | Brazil ✅ | C | **4.3%** | – | 8.7% | 19.0% | 34.5% | 57.9% |
| 7 | United States ✅ | D | **4.1%** | – | 10.1% | 22.6% | 52.8% | 81.8% |
| 8 | Netherlands ✅ | F | **4.0%** | – | 8.6% | 18.8% | 35.5% | 55.9% |
| 9 | Germany ✅ | E | **3.0%** | – | 7.6% | 15.9% | 31.0% | 68.1% |
| 10 | Japan ✅ | F | **3.0%** | – | 6.8% | 14.5% | 29.7% | 50.0% |
| 11 | Mexico ✅ | A | **3.0%** | – | 7.6% | 18.2% | 39.8% | 75.2% |
| 12 | Portugal | K | **2.6%** | – | 6.3% | 13.4% | 25.6% | 54.4% |
| 13 | Morocco ✅ | C | **2.2%** | – | 5.5% | 12.5% | 27.3% | 45.4% |
| 14 | Norway | I | **2.1%** | – | 5.3% | 13.6% | 31.4% | 62.4% |
| 15 | Switzerland ✅ | B | **1.4%** | – | 3.9% | 9.9% | 24.0% | 63.9% |

## Biggest movers since last run (data through 2026-06-21)

| Team | Δ Champion | Δ Rd of 16 | Champion now |
|------|----------:|-----------:|-------------:|
| Morocco | – | – | 2.2% |
| Senegal | – | – | 0.3% |
| South Korea | – | – | 0.5% |
| Egypt | – | – | 0.4% |
| Austria | – | – | 1.0% |
| Switzerland | – | – | 1.4% |
| Uruguay | – | – | 0.5% |
| Spain | – | – | 17.9% |

*Δ values in probability points. Full run-by-run series in `outputs/history.csv`.*

## Path to the final

The model's single most likely knockout bracket — all 32 projected round-of-32 teams and every unplayed tie, each line carrying the projected winner down to the next round until they converge on the champion. Percentages are each side's chance of advancing from that tie. **A gold-bordered box is a confirmed Round-of-32 tie** (the same pairing in every simulation — mathematically locked): 0/16 locked so far, the rest finalise as the group stage ends on 27 June.

<div style="overflow-x:auto; margin:1rem 0;">
<svg viewBox="0 0 1964 662" width="100%" preserveAspectRatio="xMidYMin meet" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica,Arial,sans-serif"><path d="M82,98 C82,134 142,134 142,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M202,98 C202,134 142,134 142,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M322,98 C322,134 382,134 382,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M442,98 C442,134 382,134 382,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M562,98 C562,134 622,134 622,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M682,98 C682,134 622,134 622,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M802,98 C802,134 862,134 862,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M922,98 C922,134 862,134 862,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1042,98 C1042,134 1102,134 1102,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1162,98 C1162,134 1102,134 1102,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1282,98 C1282,134 1342,134 1342,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1402,98 C1402,134 1342,134 1342,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1522,98 C1522,134 1582,134 1582,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1642,98 C1642,134 1582,134 1582,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1762,98 C1762,134 1822,134 1822,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1882,98 C1882,134 1822,134 1822,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M142,214 C142,250 262,250 262,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M382,214 C382,250 262,250 262,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M622,214 C622,250 742,250 742,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M862,214 C862,250 742,250 742,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1102,214 C1102,250 1222,250 1222,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1342,214 C1342,250 1222,250 1222,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1582,214 C1582,250 1702,250 1702,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1822,214 C1822,250 1702,250 1702,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M262,330 C262,366 502,366 502,402" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M742,330 C742,366 502,366 502,402" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1222,330 C1222,366 1462,366 1462,402" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1702,330 C1702,366 1462,366 1462,402" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M502,446 C502,482 982,482 982,518" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1462,446 C1462,482 982,482 982,518" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M982,562 C982,580 982,580 982,598" fill="none" stroke="#33436b" stroke-width="1.5"/><text x="11" y="76" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 11 76)" text-anchor="middle">ROUND OF 32</text><text x="11" y="192" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 11 192)" text-anchor="middle">ROUND OF 16</text><text x="11" y="308" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 11 308)" text-anchor="middle">QUARTER-FINALS</text><text x="11" y="424" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 11 424)" text-anchor="middle">SEMI-FINALS</text><text x="11" y="540" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 11 540)" text-anchor="middle">FINAL</text><rect x="26" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="26" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="34" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Germany</text><text x="130" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">80%</text><text x="34" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Sweden</text><text x="130" y="91" font-size="9" text-anchor="end" fill="#5d6880">20%</text><rect x="146" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="146" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="154" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">France</text><text x="250" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">71%</text><text x="154" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Paraguay</text><text x="250" y="91" font-size="9" text-anchor="end" fill="#5d6880">29%</text><rect x="266" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="274" y="71" font-size="10.5" font-weight="400" fill="#7c89a3">S. Korea</text><text x="370" y="71" font-size="9" text-anchor="end" fill="#5d6880">37%</text><rect x="266" y="77" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="274" y="91" font-size="10.5" font-weight="700" fill="#7ef0b6">Switzerland</text><text x="370" y="91" font-size="9" text-anchor="end" fill="#cfe8d8">63%</text><rect x="386" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="386" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="394" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Netherlands</text><text x="490" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">61%</text><text x="394" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Morocco</text><text x="490" y="91" font-size="9" text-anchor="end" fill="#5d6880">39%</text><rect x="506" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="506" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="514" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Portugal</text><text x="610" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">64%</text><text x="514" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Croatia</text><text x="610" y="91" font-size="9" text-anchor="end" fill="#5d6880">36%</text><rect x="626" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="626" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="634" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Spain</text><text x="730" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">79%</text><text x="634" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Austria</text><text x="730" y="91" font-size="9" text-anchor="end" fill="#5d6880">21%</text><rect x="746" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="746" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="754" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">USA</text><text x="850" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">89%</text><text x="754" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Bosnia</text><text x="850" y="91" font-size="9" text-anchor="end" fill="#5d6880">11%</text><rect x="866" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="874" y="71" font-size="10.5" font-weight="400" fill="#7c89a3">Egypt</text><text x="970" y="71" font-size="9" text-anchor="end" fill="#5d6880">50%</text><rect x="866" y="77" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="874" y="91" font-size="10.5" font-weight="700" fill="#7ef0b6">Algeria</text><text x="970" y="91" font-size="9" text-anchor="end" fill="#cfe8d8">50%</text><rect x="986" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="986" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="994" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Brazil</text><text x="1090" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">55%</text><text x="994" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Japan</text><text x="1090" y="91" font-size="9" text-anchor="end" fill="#5d6880">45%</text><rect x="1106" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="1114" y="71" font-size="10.5" font-weight="400" fill="#7c89a3">Ivory Coast</text><text x="1210" y="71" font-size="9" text-anchor="end" fill="#5d6880">32%</text><rect x="1106" y="77" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1114" y="91" font-size="10.5" font-weight="700" fill="#7ef0b6">Norway</text><text x="1210" y="91" font-size="9" text-anchor="end" fill="#cfe8d8">68%</text><rect x="1226" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1226" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1234" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Mexico</text><text x="1330" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">80%</text><text x="1234" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Scotland</text><text x="1330" y="91" font-size="9" text-anchor="end" fill="#5d6880">20%</text><rect x="1346" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1346" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1354" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">England</text><text x="1450" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">75%</text><text x="1354" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Senegal</text><text x="1450" y="91" font-size="9" text-anchor="end" fill="#5d6880">25%</text><rect x="1466" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1466" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1474" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Argentina</text><text x="1570" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">94%</text><text x="1474" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">C. Verde</text><text x="1570" y="91" font-size="9" text-anchor="end" fill="#5d6880">6%</text><rect x="1586" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="1594" y="71" font-size="10.5" font-weight="400" fill="#7c89a3">Australia</text><text x="1690" y="71" font-size="9" text-anchor="end" fill="#5d6880">44%</text><rect x="1586" y="77" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1594" y="91" font-size="10.5" font-weight="700" fill="#7ef0b6">Belgium</text><text x="1690" y="91" font-size="9" text-anchor="end" fill="#cfe8d8">56%</text><rect x="1706" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1706" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1714" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Canada</text><text x="1810" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">60%</text><text x="1714" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Iran</text><text x="1810" y="91" font-size="9" text-anchor="end" fill="#5d6880">40%</text><rect x="1826" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1826" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1834" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Colombia</text><text x="1930" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">86%</text><text x="1834" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Ghana</text><text x="1930" y="91" font-size="9" text-anchor="end" fill="#5d6880">14%</text><rect x="86" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="94" y="187" font-size="10.5" font-weight="400" fill="#7c89a3">Germany</text><text x="190" y="187" font-size="9" text-anchor="end" fill="#5d6880">32%</text><rect x="86" y="193" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="94" y="207" font-size="10.5" font-weight="700" fill="#7ef0b6">France</text><text x="190" y="207" font-size="9" text-anchor="end" fill="#cfe8d8">68%</text><rect x="326" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="334" y="187" font-size="10.5" font-weight="400" fill="#7c89a3">Switzerland</text><text x="430" y="187" font-size="9" text-anchor="end" fill="#5d6880">31%</text><rect x="326" y="193" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="334" y="207" font-size="10.5" font-weight="700" fill="#7ef0b6">Netherlands</text><text x="430" y="207" font-size="9" text-anchor="end" fill="#cfe8d8">69%</text><rect x="566" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="574" y="187" font-size="10.5" font-weight="400" fill="#7c89a3">Portugal</text><text x="670" y="187" font-size="9" text-anchor="end" fill="#5d6880">32%</text><rect x="566" y="193" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="574" y="207" font-size="10.5" font-weight="700" fill="#7ef0b6">Spain</text><text x="670" y="207" font-size="9" text-anchor="end" fill="#cfe8d8">68%</text><rect x="806" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="806" y="172" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="814" y="187" font-size="10.5" font-weight="700" fill="#7ef0b6">USA</text><text x="910" y="187" font-size="9" text-anchor="end" fill="#cfe8d8">66%</text><text x="814" y="207" font-size="10.5" font-weight="400" fill="#7c89a3">Algeria</text><text x="910" y="207" font-size="9" text-anchor="end" fill="#5d6880">34%</text><rect x="1046" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1046" y="172" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1054" y="187" font-size="10.5" font-weight="700" fill="#7ef0b6">Brazil</text><text x="1150" y="187" font-size="9" text-anchor="end" fill="#cfe8d8">52%</text><text x="1054" y="207" font-size="10.5" font-weight="400" fill="#7c89a3">Norway</text><text x="1150" y="207" font-size="9" text-anchor="end" fill="#5d6880">48%</text><rect x="1286" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="1294" y="187" font-size="10.5" font-weight="400" fill="#7c89a3">Mexico</text><text x="1390" y="187" font-size="9" text-anchor="end" fill="#5d6880">43%</text><rect x="1286" y="193" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1294" y="207" font-size="10.5" font-weight="700" fill="#7ef0b6">England</text><text x="1390" y="207" font-size="9" text-anchor="end" fill="#cfe8d8">57%</text><rect x="1526" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1526" y="172" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1534" y="187" font-size="10.5" font-weight="700" fill="#7ef0b6">Argentina</text><text x="1630" y="187" font-size="9" text-anchor="end" fill="#cfe8d8">77%</text><text x="1534" y="207" font-size="10.5" font-weight="400" fill="#7c89a3">Belgium</text><text x="1630" y="207" font-size="9" text-anchor="end" fill="#5d6880">23%</text><rect x="1766" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="1774" y="187" font-size="10.5" font-weight="400" fill="#7c89a3">Canada</text><text x="1870" y="187" font-size="9" text-anchor="end" fill="#5d6880">42%</text><rect x="1766" y="193" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1774" y="207" font-size="10.5" font-weight="700" fill="#7ef0b6">Colombia</text><text x="1870" y="207" font-size="9" text-anchor="end" fill="#cfe8d8">58%</text><rect x="206" y="286" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="206" y="288" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="214" y="303" font-size="10.5" font-weight="700" fill="#7ef0b6">France</text><text x="310" y="303" font-size="9" text-anchor="end" fill="#cfe8d8">51%</text><text x="214" y="323" font-size="10.5" font-weight="400" fill="#7c89a3">Netherlands</text><text x="310" y="323" font-size="9" text-anchor="end" fill="#5d6880">49%</text><rect x="686" y="286" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="686" y="288" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="694" y="303" font-size="10.5" font-weight="700" fill="#7ef0b6">Spain</text><text x="790" y="303" font-size="9" text-anchor="end" fill="#cfe8d8">67%</text><text x="694" y="323" font-size="10.5" font-weight="400" fill="#7c89a3">USA</text><text x="790" y="323" font-size="9" text-anchor="end" fill="#5d6880">33%</text><rect x="1166" y="286" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="1174" y="303" font-size="10.5" font-weight="400" fill="#7c89a3">Brazil</text><text x="1270" y="303" font-size="9" text-anchor="end" fill="#5d6880">35%</text><rect x="1166" y="309" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1174" y="323" font-size="10.5" font-weight="700" fill="#7ef0b6">England</text><text x="1270" y="323" font-size="9" text-anchor="end" fill="#cfe8d8">65%</text><rect x="1646" y="286" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1646" y="288" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1654" y="303" font-size="10.5" font-weight="700" fill="#7ef0b6">Argentina</text><text x="1750" y="303" font-size="9" text-anchor="end" fill="#cfe8d8">64%</text><text x="1654" y="323" font-size="10.5" font-weight="400" fill="#7c89a3">Colombia</text><text x="1750" y="323" font-size="9" text-anchor="end" fill="#5d6880">36%</text><rect x="446" y="402" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="454" y="419" font-size="10.5" font-weight="400" fill="#7c89a3">France</text><text x="550" y="419" font-size="9" text-anchor="end" fill="#5d6880">36%</text><rect x="446" y="425" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="454" y="439" font-size="10.5" font-weight="700" fill="#7ef0b6">Spain</text><text x="550" y="439" font-size="9" text-anchor="end" fill="#cfe8d8">64%</text><rect x="1406" y="402" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="1414" y="419" font-size="10.5" font-weight="400" fill="#7c89a3">England</text><text x="1510" y="419" font-size="9" text-anchor="end" fill="#5d6880">35%</text><rect x="1406" y="425" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1414" y="439" font-size="10.5" font-weight="700" fill="#7ef0b6">Argentina</text><text x="1510" y="439" font-size="9" text-anchor="end" fill="#cfe8d8">65%</text><rect x="926" y="518" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="926" y="520" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="934" y="535" font-size="10.5" font-weight="700" fill="#7ef0b6">Spain</text><text x="1030" y="535" font-size="9" text-anchor="end" fill="#cfe8d8">54%</text><text x="934" y="555" font-size="10.5" font-weight="400" fill="#7c89a3">Argentina</text><text x="1030" y="555" font-size="9" text-anchor="end" fill="#5d6880">46%</text><rect x="888" y="598" width="188" height="46" rx="10" fill="#f5c542"/><text x="982" y="619" font-size="13" font-weight="800" fill="#1a1300" text-anchor="middle">🏆 Spain</text><text x="982" y="635" font-size="10" fill="#5a4a00" text-anchor="middle">projected champion · 18% to win</text></svg>
</div>

## Upcoming group matches — outcome probabilities

*(next match days; full list for all 72 group games in `match_probabilities.csv`)*

| Date | Grp | Match | Home win | Draw | Away win | xG | Likely score |
|------|:---:|-------|---------:|-----:|---------:|----|:----:|
| 2026-06-22 | I | France v Iraq | **74.9%** | 16.9% | 8.3% | 2.36–0.66 | 2-0 |
| 2026-06-22 | I | Norway v Senegal | **46.5%** | 25.9% | 27.6% | 1.61–1.19 | 1-1 |
| 2026-06-22 | J | Argentina v Austria | **66.2%** | 20.9% | 12.9% | 2.05–0.79 | 2-0 |
| 2026-06-22 | J | Jordan v Algeria | 23.6% | 26.7% | **49.6%** | 1.00–1.56 | 1-1 |
| 2026-06-23 | K | Portugal v Uzbekistan | **63.6%** | 22.6% | 13.8% | 1.89–0.76 | 1-0 |
| 2026-06-23 | K | Colombia v DR Congo | **65.2%** | 21.3% | 13.5% | 2.02–0.81 | 2-0 |
| 2026-06-23 | L | England v Ghana | **76.3%** | 17.2% | 6.5% | 2.19–0.49 | 2-0 |
| 2026-06-23 | L | Panama v Croatia | 27.0% | 26.6% | **46.5%** | 1.13–1.55 | 1-1 |
| 2026-06-24 | C | Morocco v Haiti | **73.3%** | 18.5% | 8.2% | 2.14–0.58 | 2-0 |
| 2026-06-24 | B | Bosnia and Herzegovina v Qatar | **47.9%** | 27.5% | 24.6% | 1.48–0.99 | 1-1 |
| 2026-06-24 | C | Scotland v Brazil | 17.7% | 25.0% | **57.3%** | 0.84–1.71 | 0-1 |
| 2026-06-24 | A | South Africa v South Korea | 21.0% | 27.1% | **51.8%** | 0.88–1.53 | 0-1 |
| 2026-06-24 | A | Mexico v Czech Republic | **76.8%** | 16.2% | 7.0% | 2.36–0.58 | 2-0 |
| 2026-06-24 | B | Canada v Switzerland | **41.9%** | 28.8% | 29.4% | 1.33–1.07 | 1-1 |
| 2026-06-25 | D | United States v Turkey | **49.8%** | 25.9% | 24.2% | 1.63–1.07 | 1-1 |
| 2026-06-25 | D | Paraguay v Australia | 34.2% | 30.2% | **35.5%** | 1.11–1.13 | 1-1 |
| 2026-06-25 | E | Curaçao v Ivory Coast | 17.7% | 26.4% | **55.9%** | 0.78–1.58 | 0-1 |
| 2026-06-25 | E | Ecuador v Germany | 26.3% | 29.9% | **43.7%** | 0.93–1.27 | 1-1 |
| 2026-06-25 | F | Japan v Sweden | **65.4%** | 19.7% | 14.9% | 2.27–1.00 | 2-1 |
| 2026-06-25 | F | Tunisia v Netherlands | 12.0% | 20.8% | **67.2%** | 0.74–2.03 | 0-2 |

## Group projections

### Group A

**✅ Into the knockouts:** Mexico

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Mexico ✅ | 2 | 2-0-0 | 3-0 | **6** | 8.47 | 100.0% | 100.0% | 100.0% |
| South Korea | 2 | 1-0-1 | 2-2 | **3** | 4.82 | 0.0% | 78.6% | 95.3% |
| Czech Republic | 2 | 0-1-1 | 2-3 | **1** | 1.37 | 0.0% | 1.3% | 8.5% |
| South Africa | 2 | 0-1-1 | 1-3 | **1** | 1.91 | 0.0% | 20.1% | 21.7% |

### Group B

**✅ Into the knockouts:** Canada, Switzerland

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Canada ✅ | 2 | 1-1-0 | 7-1 | **4** | 5.55 | 70.8% | 100.0% | 100.0% |
| Switzerland ✅ | 2 | 1-1-0 | 5-2 | **4** | 5.17 | 29.2% | 100.0% | 100.0% |
| Bosnia and Herzegovina | 2 | 0-1-1 | 2-5 | **1** | 2.72 | 0.0% | 0.0% | 48.5% |
| Qatar | 2 | 0-1-1 | 1-7 | **1** | 2.00 | 0.0% | 0.0% | 24.3% |

### Group C

**✅ Into the knockouts:** Brazil, Morocco

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Brazil ✅ | 2 | 1-1-0 | 4-1 | **4** | 5.96 | 59.0% | 83.7% | 100.0% |
| Morocco ✅ | 2 | 1-1-0 | 2-1 | **4** | 6.38 | 36.3% | 98.5% | 100.0% |
| Scotland | 2 | 1-0-1 | 1-1 | **3** | 3.79 | 4.7% | 17.9% | 88.6% |
| Haiti | 2 | 0-0-2 | 0-4 | **0** | 0.43 | 0.0% | 0.0% | 0.0% |

### Group D

**✅ Into the knockouts:** United States

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| United States ✅ | 2 | 2-0-0 | 6-1 | **6** | 7.76 | 100.0% | 100.0% | 100.0% |
| Australia | 2 | 1-0-1 | 2-2 | **3** | 4.37 | 0.0% | 65.7% | 95.6% |
| Paraguay | 2 | 1-0-1 | 2-4 | **3** | 4.33 | 0.0% | 34.3% | 86.0% |
| Turkey | 2 | 0-0-2 | 0-3 | **0** | 0.98 | 0.0% | 0.0% | 0.0% |

### Group E

**✅ Into the knockouts:** Germany

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Germany ✅ | 2 | 2-0-0 | 9-2 | **6** | 7.61 | 100.0% | 100.0% | 100.0% |
| Ivory Coast | 2 | 1-0-1 | 2-2 | **3** | 4.94 | 0.0% | 82.4% | 93.4% |
| Ecuador | 2 | 0-1-1 | 0-1 | **1** | 2.09 | 0.0% | 4.6% | 28.3% |
| Curaçao | 2 | 0-1-1 | 1-7 | **1** | 1.79 | 0.0% | 13.0% | 17.6% |

### Group F

**✅ Into the knockouts:** Netherlands, Japan

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Netherlands ✅ | 2 | 1-1-0 | 7-3 | **4** | 6.23 | 53.0% | 99.5% | 100.0% |
| Japan ✅ | 2 | 1-1-0 | 6-2 | **4** | 6.15 | 42.2% | 85.2% | 100.0% |
| Sweden | 2 | 1-0-1 | 6-6 | **3** | 3.65 | 4.8% | 15.2% | 90.0% |
| Tunisia | 2 | 0-0-2 | 1-9 | **0** | 0.57 | 0.0% | 0.0% | 0.0% |

### Group G

**✅ Into the knockouts:** Egypt

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Egypt ✅ | 2 | 1-1-0 | 4-2 | **4** | 5.27 | 57.6% | 79.5% | 100.0% |
| Iran | 2 | 0-2-0 | 2-2 | **2** | 3.43 | 27.8% | 42.9% | 71.3% |
| Belgium | 2 | 0-2-0 | 1-1 | **2** | 3.89 | 14.5% | 65.4% | 80.6% |
| New Zealand | 2 | 0-1-1 | 3-5 | **1** | 1.85 | 0.0% | 12.2% | 19.9% |

### Group H

**✅ Into the knockouts:** Spain

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Spain ✅ | 2 | 1-1-0 | 4-0 | **4** | 6.01 | 83.1% | 94.2% | 100.0% |
| Uruguay | 2 | 0-2-0 | 3-3 | **2** | 2.75 | 14.8% | 23.9% | 47.7% |
| Cape Verde | 2 | 0-2-0 | 2-2 | **2** | 3.36 | 2.0% | 53.4% | 66.7% |
| Saudi Arabia | 2 | 0-1-1 | 1-5 | **1** | 2.33 | 0.0% | 28.5% | 34.2% |

### Group I

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Norway | 1 | 1-0-0 | 4-1 | **3** | 5.41 | 24.6% | 77.2% | 98.2% |
| France | 1 | 1-0-0 | 3-1 | **3** | 7.42 | 72.8% | 97.1% | 99.4% |
| Senegal | 1 | 0-0-1 | 1-3 | **0** | 3.17 | 2.1% | 23.6% | 65.2% |
| Iraq | 1 | 0-0-1 | 1-4 | **0** | 1.11 | 0.5% | 2.1% | 12.1% |

### Group J

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Argentina | 1 | 1-0-0 | 3-0 | **3** | 7.82 | 84.6% | 99.0% | 99.8% |
| Austria | 1 | 1-0-0 | 3-1 | **3** | 5.15 | 14.0% | 76.0% | 96.2% |
| Jordan | 1 | 0-0-1 | 1-3 | **0** | 1.23 | 0.5% | 2.2% | 16.8% |
| Algeria | 1 | 0-0-1 | 0-3 | **0** | 2.90 | 0.8% | 22.8% | 52.4% |

### Group K

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Colombia | 1 | 1-0-0 | 3-1 | **3** | 6.74 | 70.2% | 90.4% | 99.2% |
| DR Congo | 1 | 0-1-0 | 1-1 | **1** | 3.05 | 6.6% | 29.2% | 54.2% |
| Portugal | 1 | 0-1-0 | 1-1 | **1** | 4.29 | 22.3% | 66.8% | 82.8% |
| Uzbekistan | 1 | 0-0-1 | 1-3 | **0** | 1.90 | 0.9% | 13.5% | 31.8% |

### Group L

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| England | 1 | 1-0-0 | 4-2 | **3** | 7.62 | 88.1% | 98.2% | 99.5% |
| Ghana | 1 | 1-0-0 | 1-0 | **3** | 3.98 | 5.7% | 33.7% | 72.7% |
| Panama | 1 | 0-0-1 | 0-1 | **0** | 1.69 | 3.1% | 11.1% | 27.3% |
| Croatia | 1 | 0-0-1 | 2-4 | **0** | 3.84 | 3.1% | 57.0% | 74.5% |

*\*Advance = top two or one of the eight best third-placed teams.*

*✅ = already reached the knockout stage — locked into the Round of 32 in every simulation. (Reaching later rounds still requires winning knockout games, so those stay below 100%.)*

## Most likely knockout bracket

Each tie shows the most probable pairing given projected group finishes, the chance the named winner goes through **in that pairing**, and how often the exact pairing occurred across all simulations. **🔒 marks a confirmed tie** — the same two teams in every simulation, i.e. mathematically locked. (0/16 Round-of-32 ties locked so far; the rest finalise as the group stage completes on 27 June.)

### Round of 32

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 73 | 2026-06-28 | SoFi Stadium, Los Angeles | South Korea v Switzerland | **Switzerland** | 62.7% | 55.6% |
| 74 | 2026-06-29 | Gillette Stadium, Boston | Germany v Sweden | **Germany** | 79.5% | 13.5% |
| 75 | 2026-06-29 | Estadio BBVA, Monterrey | Netherlands v Morocco | **Netherlands** | 60.6% | 33.0% |
| 76 | 2026-06-29 | NRG Stadium, Houston | Brazil v Japan | **Brazil** | 55.0% | 25.5% |
| 77 | 2026-06-30 | MetLife Stadium, New York/New Jersey | France v Paraguay | **France** | 70.9% | 21.4% |
| 78 | 2026-06-30 | AT&T Stadium, Dallas | Ivory Coast v Norway | **Norway** | 67.5% | 43.5% |
| 79 | 2026-06-30 | Estadio Azteca, Mexico City | Mexico v Scotland | **Mexico** | 80.2% | 39.0% |
| 80 | 2026-07-01 | Mercedes-Benz Stadium, Atlanta | England v Senegal | **England** | 74.7% | 4.4% |
| 81 | 2026-07-01 | Levi's Stadium, San Francisco Bay Area | United States v Bosnia and Herzegovina | **United States** | 88.9% | 33.4% |
| 82 | 2026-07-01 | Lumen Field, Seattle | Egypt v Algeria | **Algeria** | 50.4% | 6.4% |
| 83 | 2026-07-02 | BMO Field, Toronto | Portugal v Croatia | **Portugal** | 63.7% | 24.2% |
| 84 | 2026-07-02 | SoFi Stadium, Los Angeles | Spain v Austria | **Spain** | 78.9% | 51.5% |
| 85 | 2026-07-02 | BC Place, Vancouver | Canada v Iran | **Canada** | 60.3% | 16.7% |
| 86 | 2026-07-03 | Hard Rock Stadium, Miami | Argentina v Cape Verde | **Argentina** | 93.9% | 43.5% |
| 87 | 2026-07-03 | Arrowhead Stadium, Kansas City | Colombia v Ghana | **Colombia** | 86.5% | 27.7% |
| 88 | 2026-07-03 | AT&T Stadium, Dallas | Australia v Belgium | **Belgium** | 55.8% | 33.4% |

### Round of 16

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 89 | 2026-07-04 | Lincoln Financial Field, Philadelphia | Germany v France | **France** | 67.7% | 35.1% |
| 90 | 2026-07-04 | NRG Stadium, Houston | Switzerland v Netherlands | **Netherlands** | 69.4% | 14.2% |
| 91 | 2026-07-05 | MetLife Stadium, New York/New Jersey | Brazil v Norway | **Brazil** | 52.2% | 12.1% |
| 92 | 2026-07-05 | Estadio Azteca, Mexico City | Mexico v England | **England** | 56.7% | 49.4% |
| 93 | 2026-07-06 | AT&T Stadium, Dallas | Portugal v Spain | **Spain** | 68.4% | 19.1% |
| 94 | 2026-07-06 | Lumen Field, Seattle | United States v Algeria | **United States** | 66.4% | 4.5% |
| 95 | 2026-07-07 | Mercedes-Benz Stadium, Atlanta | Argentina v Belgium | **Argentina** | 77.2% | 20.9% |
| 96 | 2026-07-07 | BC Place, Vancouver | Canada v Colombia | **Colombia** | 58.2% | 26.5% |

### Quarter-finals

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 97 | 2026-07-09 | Gillette Stadium, Boston | France v Netherlands | **France** | 50.9% | 7.5% |
| 98 | 2026-07-10 | SoFi Stadium, Los Angeles | Spain v United States | **Spain** | 67.4% | 24.9% |
| 99 | 2026-07-11 | Hard Rock Stadium, Miami | Brazil v England | **England** | 64.8% | 7.4% |
| 100 | 2026-07-11 | Arrowhead Stadium, Kansas City | Argentina v Colombia | **Argentina** | 63.7% | 20.8% |

### Semi-finals

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 101 | 2026-07-14 | AT&T Stadium, Dallas | France v Spain | **Spain** | 63.8% | 7.9% |
| 102 | 2026-07-15 | Mercedes-Benz Stadium, Atlanta | England v Argentina | **Argentina** | 64.9% | 11.8% |

### Final

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 104 | 2026-07-19 | MetLife Stadium, East Rutherford | Spain v Argentina | **Spain** | 53.6% | 8.9% |

**Projected champion: Spain** (overall title probability 17.9%; the single most likely path above is itself only one of many ways the tournament can unfold).

## How to read this

- All figures are probabilities, not certainties — a 65% favourite loses about one such match in three.
- `xPts` = expected group points; `xG` = expected goals from the Poisson model.
- Predictions refresh after every match day: run `python -m worldcup.run all` to pull new results, re-rate teams, and re-simulate.
- Machine-readable outputs: `match_probabilities.csv`, `tournament_projections.csv`. Past reports in `outputs/archive/`.

## Model scorecard

**22 of 40 match outcomes called correctly** (the model's own probabilities expected ≈23.3 of 40) · exact scoreline predicted 2/40 · average probability placed on what actually happened: **42.8%** (33.3% = guessing).

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
| Saudi Arabia v Uruguay | Uruguay win (62.1%) | 0-1 | 1-1 | ❌ | — |
| Belgium v Egypt | Belgium win (56.6%) | 1-1 | 1-1 | ❌ | ✅ |
| Iran v New Zealand | Iran win (54.6%) | 1-0 | 2-2 | ❌ | — |
| Spain v Cape Verde | Spain win (90.5%) | 3-0 | 0-0 | ❌ | — |
| France v Senegal | France win (59.1%) | 1-0 | 3-1 | ✅ | — |
| Iraq v Norway | Norway win (59.1%) | 0-1 | 1-4 | ✅ | — |
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
| Brazil v Haiti | Brazil win (81.3%) | 2-0 | 3-0 | ✅ | — |
| Turkey v Paraguay | Paraguay win (38.4%) | 1-1 | 0-1 | ✅ | — |
| Scotland v Morocco | Morocco win (49.3%) | 1-1 | 0-1 | ✅ | — |
| Netherlands v Sweden | Netherlands win (52.8%) | 1-1 | 5-1 | ✅ | — |
| Tunisia v Japan | Japan win (63.1%) | 0-2 | 0-4 | ✅ | — |
| Germany v Ivory Coast | Germany win (50.9%) | 1-1 | 2-1 | ✅ | — |
| Ecuador v Curaçao | Ecuador win (81.9%) | 2-0 | 0-0 | ❌ | — |
| Spain v Saudi Arabia | Spain win (78.3%) | 2-0 | 4-0 | ✅ | — |
| Belgium v Iran | Belgium win (46.7%) | 1-1 | 0-0 | ❌ | — |
| New Zealand v Egypt | Egypt win (38.7%) | 1-1 | 1-3 | ✅ | — |
| Uruguay v Cape Verde | Uruguay win (72.7%) | 2-0 | 2-2 | ❌ | — |

**Calibration vs benchmarks** (the 9 graded games with bookmaker prices on file) — log-loss, lower is better. This is the honest test: is the model bad, or were the games hard for everyone?

| Forecaster | Log-loss |
|------------|---------:|
| **This model** | **1.193** |
| Sky Bet (de-vigged) | 1.156 |
| Coin-flip (33/33/33) | 1.099 |

The model is **essentially level with the market** (+0.037 log-loss). Note both the model **and** the bookmaker scored worse than a coin-flip here — with this many draws and upsets, the slate was close to unforecastable for anyone, which is the real reason the hit-rate looks poor.


*Predictions are frozen at the last run before each result arrives, then graded — the scorecard never grades a model that has already seen the answer.*

