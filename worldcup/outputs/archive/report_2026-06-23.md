# FIFA World Cup 2026 — ML Prediction Report

*Generated 2026-06-24 · data through **2026-06-23** · 50,000 Monte Carlo simulations · 47/72 group matches played*

Probabilities come from a gradient-boosted Poisson goal model (Elo strength + rolling form + venue/importance features) trained on 30,819 internationals, simulated through the official 2026 bracket and tiebreaker rules.

*Rolling validation (7,966 matches, 2018–2026): RPS 0.1687 vs Elo-baseline 0.1711; log-loss 0.8652 vs 0.8809.*

## Title favourites

| # | Team | Group | Champion | Δ vs 2026-06-23 | Final | Semi-final | Quarter-final | Rd of 16 |
|---|------|:-----:|---------:|-------:|------:|-----------:|--------------:|---------:|
| 1 | Argentina ✅ | J | **31.1%** | +6.0 | 43.5% | 57.0% | 74.0% | 88.1% |
| 2 | Spain ✅ | H | **15.2%** | -1.5 | 27.1% | 38.1% | 50.7% | 74.4% |
| 3 | France ✅ | I | **8.8%** | -3.0 | 19.1% | 35.3% | 57.7% | 76.7% |
| 4 | England ✅ | L | **6.7%** | +0.5 | 12.3% | 24.5% | 36.8% | 72.5% |
| 5 | Portugal ✅ | K | **4.9%** | +0.5 | 11.0% | 20.6% | 41.3% | 72.6% |
| 6 | Brazil ✅ | C | **4.8%** | +0.9 | 9.3% | 21.9% | 36.7% | 60.5% |
| 7 | Colombia | K | **4.7%** | -1.0 | 10.4% | 19.6% | 41.2% | 73.9% |
| 8 | Mexico ✅ | A | **4.1%** | +0.7 | 9.3% | 23.5% | 53.0% | 80.5% |
| 9 | United States ✅ | D | **2.8%** | +0.3 | 8.4% | 20.1% | 54.3% | 82.6% |
| 10 | Japan ✅ | F | **2.7%** | – | 6.6% | 16.0% | 30.3% | 52.0% |
| 11 | Netherlands ✅ | F | **2.6%** | -0.7 | 6.6% | 16.7% | 31.1% | 50.7% |
| 12 | Norway ✅ | I | **2.2%** | -0.2 | 5.3% | 16.9% | 35.2% | 70.3% |
| 13 | Morocco ✅ | C | **2.0%** | – | 5.3% | 12.6% | 27.1% | 46.0% |
| 14 | Switzerland ✅ | B | **1.2%** | +0.1 | 3.9% | 10.1% | 25.3% | 64.9% |
| 15 | Belgium | G | **1.1%** | +0.2 | 3.0% | 6.8% | 16.3% | 47.3% |

## Biggest movers since last run (data through 2026-06-23)

| Team | Δ Champion | Δ Rd of 16 | Champion now |
|------|----------:|-----------:|-------------:|
| Argentina | +6.0 | +0.2 | 31.1% |
| Brazil | +0.9 | +4.3 | 4.8% |
| Mexico | +0.7 | +1.7 | 4.1% |
| Netherlands | -0.7 | -4.1 | 2.6% |
| Colombia | -1.0 | -0.4 | 4.7% |
| Spain | -1.5 | -1.1 | 15.2% |
| Germany | -2.1 | -5.8 | 1.0% |
| France | -3.0 | -2.1 | 8.8% |

*Δ values in probability points. Full run-by-run series in `outputs/history.csv`.*

## Path to the final

The model's single most likely knockout bracket — all 32 projected round-of-32 teams and every unplayed tie, each line carrying the projected winner down to the next round until they converge on the champion. Percentages are each side's chance of advancing from that tie. **A gold-bordered box is a confirmed Round-of-32 tie** (the same pairing in every simulation — mathematically locked): 0/16 locked so far, the rest finalise as the group stage ends on 27 June.

<div style="overflow-x:auto; margin:1rem 0;">
<svg viewBox="0 0 1964 662" width="100%" preserveAspectRatio="xMidYMin meet" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica,Arial,sans-serif"><path d="M82,98 C82,134 142,134 142,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M202,98 C202,134 142,134 142,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M322,98 C322,134 382,134 382,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M442,98 C442,134 382,134 382,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M562,98 C562,134 622,134 622,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M682,98 C682,134 622,134 622,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M802,98 C802,134 862,134 862,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M922,98 C922,134 862,134 862,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1042,98 C1042,134 1102,134 1102,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1162,98 C1162,134 1102,134 1102,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1282,98 C1282,134 1342,134 1342,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1402,98 C1402,134 1342,134 1342,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1522,98 C1522,134 1582,134 1582,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1642,98 C1642,134 1582,134 1582,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1762,98 C1762,134 1822,134 1822,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1882,98 C1882,134 1822,134 1822,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M142,214 C142,250 262,250 262,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M382,214 C382,250 262,250 262,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M622,214 C622,250 742,250 742,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M862,214 C862,250 742,250 742,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1102,214 C1102,250 1222,250 1222,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1342,214 C1342,250 1222,250 1222,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1582,214 C1582,250 1702,250 1702,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1822,214 C1822,250 1702,250 1702,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M262,330 C262,366 502,366 502,402" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M742,330 C742,366 502,366 502,402" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1222,330 C1222,366 1462,366 1462,402" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1702,330 C1702,366 1462,366 1462,402" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M502,446 C502,482 982,482 982,518" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1462,446 C1462,482 982,482 982,518" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M982,562 C982,580 982,580 982,598" fill="none" stroke="#33436b" stroke-width="1.5"/><text x="11" y="76" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 11 76)" text-anchor="middle">ROUND OF 32</text><text x="11" y="192" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 11 192)" text-anchor="middle">ROUND OF 16</text><text x="11" y="308" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 11 308)" text-anchor="middle">QUARTER-FINALS</text><text x="11" y="424" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 11 424)" text-anchor="middle">SEMI-FINALS</text><text x="11" y="540" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 11 540)" text-anchor="middle">FINAL</text><rect x="26" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="26" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="34" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Germany</text><text x="130" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">80%</text><text x="34" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Sweden</text><text x="130" y="91" font-size="9" text-anchor="end" fill="#5d6880">20%</text><rect x="146" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="146" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="154" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">France</text><text x="250" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">77%</text><text x="154" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Paraguay</text><text x="250" y="91" font-size="9" text-anchor="end" fill="#5d6880">23%</text><rect x="266" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="274" y="71" font-size="10.5" font-weight="400" fill="#7c89a3">S. Korea</text><text x="370" y="71" font-size="9" text-anchor="end" fill="#5d6880">36%</text><rect x="266" y="77" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="274" y="91" font-size="10.5" font-weight="700" fill="#7ef0b6">Switzerland</text><text x="370" y="91" font-size="9" text-anchor="end" fill="#cfe8d8">64%</text><rect x="386" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="386" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="394" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Netherlands</text><text x="490" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">57%</text><text x="394" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Morocco</text><text x="490" y="91" font-size="9" text-anchor="end" fill="#5d6880">43%</text><rect x="506" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="506" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="514" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Portugal</text><text x="610" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">77%</text><text x="514" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Croatia</text><text x="610" y="91" font-size="9" text-anchor="end" fill="#5d6880">23%</text><rect x="626" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="626" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="634" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Spain</text><text x="730" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">77%</text><text x="634" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Austria</text><text x="730" y="91" font-size="9" text-anchor="end" fill="#5d6880">23%</text><rect x="746" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="746" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="754" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">USA</text><text x="850" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">90%</text><text x="754" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Bosnia</text><text x="850" y="91" font-size="9" text-anchor="end" fill="#5d6880">10%</text><rect x="866" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="866" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="874" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Egypt</text><text x="970" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">46%†</text><text x="874" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Senegal</text><text x="970" y="91" font-size="9" text-anchor="end" fill="#5d6880">54%</text><rect x="986" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="986" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="994" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Brazil</text><text x="1090" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">56%</text><text x="994" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Japan</text><text x="1090" y="91" font-size="9" text-anchor="end" fill="#5d6880">44%</text><rect x="1106" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="1114" y="71" font-size="10.5" font-weight="400" fill="#7c89a3">Ivory Coast</text><text x="1210" y="71" font-size="9" text-anchor="end" fill="#5d6880">31%</text><rect x="1106" y="77" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1114" y="91" font-size="10.5" font-weight="700" fill="#7ef0b6">Norway</text><text x="1210" y="91" font-size="9" text-anchor="end" fill="#cfe8d8">69%</text><rect x="1226" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1226" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1234" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Mexico</text><text x="1330" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">83%</text><text x="1234" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Scotland</text><text x="1330" y="91" font-size="9" text-anchor="end" fill="#5d6880">17%</text><rect x="1346" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1346" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1354" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">England</text><text x="1450" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">89%</text><text x="1354" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">DR Congo</text><text x="1450" y="91" font-size="9" text-anchor="end" fill="#5d6880">11%</text><rect x="1466" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1466" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1474" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Argentina</text><text x="1570" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">92%</text><text x="1474" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">C. Verde</text><text x="1570" y="91" font-size="9" text-anchor="end" fill="#5d6880">8%</text><rect x="1586" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="1594" y="71" font-size="10.5" font-weight="400" fill="#7c89a3">Australia</text><text x="1690" y="71" font-size="9" text-anchor="end" fill="#5d6880">41%</text><rect x="1586" y="77" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1594" y="91" font-size="10.5" font-weight="700" fill="#7ef0b6">Belgium</text><text x="1690" y="91" font-size="9" text-anchor="end" fill="#cfe8d8">59%</text><rect x="1706" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1706" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1714" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Canada</text><text x="1810" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">64%</text><text x="1714" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Algeria</text><text x="1810" y="91" font-size="9" text-anchor="end" fill="#5d6880">36%</text><rect x="1826" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1826" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1834" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Colombia</text><text x="1930" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">85%</text><text x="1834" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Ghana</text><text x="1930" y="91" font-size="9" text-anchor="end" fill="#5d6880">15%</text><rect x="86" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="94" y="187" font-size="10.5" font-weight="400" fill="#7c89a3">Germany</text><text x="190" y="187" font-size="9" text-anchor="end" fill="#5d6880">22%</text><rect x="86" y="193" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="94" y="207" font-size="10.5" font-weight="700" fill="#7ef0b6">France</text><text x="190" y="207" font-size="9" text-anchor="end" fill="#cfe8d8">78%</text><rect x="326" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="334" y="187" font-size="10.5" font-weight="400" fill="#7c89a3">Switzerland</text><text x="430" y="187" font-size="9" text-anchor="end" fill="#5d6880">35%</text><rect x="326" y="193" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="334" y="207" font-size="10.5" font-weight="700" fill="#7ef0b6">Netherlands</text><text x="430" y="207" font-size="9" text-anchor="end" fill="#cfe8d8">65%</text><rect x="566" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="574" y="187" font-size="10.5" font-weight="400" fill="#7c89a3">Portugal</text><text x="670" y="187" font-size="9" text-anchor="end" fill="#5d6880">40%</text><rect x="566" y="193" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="574" y="207" font-size="10.5" font-weight="700" fill="#7ef0b6">Spain</text><text x="670" y="207" font-size="9" text-anchor="end" fill="#cfe8d8">60%</text><rect x="806" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="806" y="172" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="814" y="187" font-size="10.5" font-weight="700" fill="#7ef0b6">USA</text><text x="910" y="187" font-size="9" text-anchor="end" fill="#cfe8d8">71%</text><text x="814" y="207" font-size="10.5" font-weight="400" fill="#7c89a3">Egypt</text><text x="910" y="207" font-size="9" text-anchor="end" fill="#5d6880">29%</text><rect x="1046" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1046" y="172" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1054" y="187" font-size="10.5" font-weight="700" fill="#7ef0b6">Brazil</text><text x="1150" y="187" font-size="9" text-anchor="end" fill="#cfe8d8">56%</text><text x="1054" y="207" font-size="10.5" font-weight="400" fill="#7c89a3">Norway</text><text x="1150" y="207" font-size="9" text-anchor="end" fill="#5d6880">44%</text><rect x="1286" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="1294" y="187" font-size="10.5" font-weight="400" fill="#7c89a3">Mexico</text><text x="1390" y="187" font-size="9" text-anchor="end" fill="#5d6880">55%</text><rect x="1286" y="193" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1294" y="207" font-size="10.5" font-weight="700" fill="#7ef0b6">England</text><text x="1390" y="207" font-size="9" text-anchor="end" fill="#cfe8d8">45%†</text><rect x="1526" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1526" y="172" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1534" y="187" font-size="10.5" font-weight="700" fill="#7ef0b6">Argentina</text><text x="1630" y="187" font-size="9" text-anchor="end" fill="#cfe8d8">78%</text><text x="1534" y="207" font-size="10.5" font-weight="400" fill="#7c89a3">Belgium</text><text x="1630" y="207" font-size="9" text-anchor="end" fill="#5d6880">22%</text><rect x="1766" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="1774" y="187" font-size="10.5" font-weight="400" fill="#7c89a3">Canada</text><text x="1870" y="187" font-size="9" text-anchor="end" fill="#5d6880">39%</text><rect x="1766" y="193" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1774" y="207" font-size="10.5" font-weight="700" fill="#7ef0b6">Colombia</text><text x="1870" y="207" font-size="9" text-anchor="end" fill="#cfe8d8">61%</text><rect x="206" y="286" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="206" y="288" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="214" y="303" font-size="10.5" font-weight="700" fill="#7ef0b6">France</text><text x="310" y="303" font-size="9" text-anchor="end" fill="#cfe8d8">54%</text><text x="214" y="323" font-size="10.5" font-weight="400" fill="#7c89a3">Netherlands</text><text x="310" y="323" font-size="9" text-anchor="end" fill="#5d6880">46%</text><rect x="686" y="286" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="686" y="288" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="694" y="303" font-size="10.5" font-weight="700" fill="#7ef0b6">Spain</text><text x="790" y="303" font-size="9" text-anchor="end" fill="#cfe8d8">73%</text><text x="694" y="323" font-size="10.5" font-weight="400" fill="#7c89a3">USA</text><text x="790" y="323" font-size="9" text-anchor="end" fill="#5d6880">27%</text><rect x="1166" y="286" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="1174" y="303" font-size="10.5" font-weight="400" fill="#7c89a3">Brazil</text><text x="1270" y="303" font-size="9" text-anchor="end" fill="#5d6880">43%</text><rect x="1166" y="309" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1174" y="323" font-size="10.5" font-weight="700" fill="#7ef0b6">England</text><text x="1270" y="323" font-size="9" text-anchor="end" fill="#cfe8d8">57%</text><rect x="1646" y="286" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1646" y="288" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1654" y="303" font-size="10.5" font-weight="700" fill="#7ef0b6">Argentina</text><text x="1750" y="303" font-size="9" text-anchor="end" fill="#cfe8d8">70%</text><text x="1654" y="323" font-size="10.5" font-weight="400" fill="#7c89a3">Colombia</text><text x="1750" y="323" font-size="9" text-anchor="end" fill="#5d6880">30%</text><rect x="446" y="402" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="454" y="419" font-size="10.5" font-weight="400" fill="#7c89a3">France</text><text x="550" y="419" font-size="9" text-anchor="end" fill="#5d6880">34%</text><rect x="446" y="425" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="454" y="439" font-size="10.5" font-weight="700" fill="#7ef0b6">Spain</text><text x="550" y="439" font-size="9" text-anchor="end" fill="#cfe8d8">66%</text><rect x="1406" y="402" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="1414" y="419" font-size="10.5" font-weight="400" fill="#7c89a3">England</text><text x="1510" y="419" font-size="9" text-anchor="end" fill="#5d6880">30%</text><rect x="1406" y="425" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1414" y="439" font-size="10.5" font-weight="700" fill="#7ef0b6">Argentina</text><text x="1510" y="439" font-size="9" text-anchor="end" fill="#cfe8d8">70%</text><rect x="926" y="518" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="934" y="535" font-size="10.5" font-weight="400" fill="#7c89a3">Spain</text><text x="1030" y="535" font-size="9" text-anchor="end" fill="#5d6880">44%</text><rect x="926" y="541" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="934" y="555" font-size="10.5" font-weight="700" fill="#7ef0b6">Argentina</text><text x="1030" y="555" font-size="9" text-anchor="end" fill="#cfe8d8">56%</text><rect x="888" y="598" width="188" height="46" rx="10" fill="#f5c542"/><text x="982" y="619" font-size="13" font-weight="800" fill="#1a1300" text-anchor="middle">🏆 Argentina</text><text x="982" y="635" font-size="10" fill="#5a4a00" text-anchor="middle">projected champion · 31% to win</text></svg>
</div>

## Upcoming group matches — outcome probabilities

*(next match days; full list for all 72 group games in `match_probabilities.csv`)*

| Date | Grp | Match | Home win | Draw | Away win | xG | Likely score |
|------|:---:|-------|---------:|-----:|---------:|----|:----:|
| 2026-06-23 | K | Colombia v DR Congo | **65.4%** | 21.5% | 13.1% | 1.99–0.77 | 2-0 |
| 2026-06-24 | C | Morocco v Haiti | **72.5%** | 18.8% | 8.7% | 2.13–0.60 | 2-0 |
| 2026-06-24 | B | Bosnia and Herzegovina v Qatar | **45.5%** | 29.0% | 25.5% | 1.36–0.95 | 1-1 |
| 2026-06-24 | C | Scotland v Brazil | 12.0% | 20.7% | **67.3%** | 0.74–2.05 | 0-2 |
| 2026-06-24 | A | South Africa v South Korea | 20.0% | 27.1% | **52.9%** | 0.84–1.53 | 0-1 |
| 2026-06-24 | A | Mexico v Czech Republic | **77.6%** | 16.5% | 5.9% | 2.24–0.47 | 2-0 |
| 2026-06-24 | B | Canada v Switzerland | **41.0%** | 29.7% | 29.3% | 1.26–1.02 | 1-1 |
| 2026-06-25 | D | United States v Turkey | **50.2%** | 26.0% | 23.8% | 1.62–1.04 | 1-1 |
| 2026-06-25 | D | Paraguay v Australia | **35.7%** | 29.1% | 35.2% | 1.20–1.19 | 1-1 |
| 2026-06-25 | E | Curaçao v Ivory Coast | 17.3% | 26.0% | **56.7%** | 0.78–1.61 | 0-1 |
| 2026-06-25 | E | Ecuador v Germany | 24.2% | 28.9% | **46.9%** | 0.91–1.37 | 1-1 |
| 2026-06-25 | F | Japan v Sweden | **71.3%** | 17.1% | 11.6% | 2.53–0.95 | 2-0 |
| 2026-06-25 | F | Tunisia v Netherlands | 7.1% | 18.5% | **74.4%** | 0.50–2.09 | 0-2 |
| 2026-06-26 | I | Senegal v Iraq | **62.1%** | 23.0% | 14.9% | 1.87–0.80 | 1-0 |
| 2026-06-26 | I | Norway v France | 16.4% | 21.7% | **61.9%** | 0.96–2.04 | 0-2 |
| 2026-06-26 | H | Uruguay v Spain | 13.9% | 23.4% | **62.6%** | 0.73–1.81 | 0-1 |
| 2026-06-26 | G | New Zealand v Belgium | 18.0% | 25.4% | **56.6%** | 0.83–1.67 | 0-1 |
| 2026-06-26 | G | Egypt v Iran | 33.2% | 30.0% | **36.8%** | 1.10–1.17 | 1-1 |
| 2026-06-26 | H | Cape Verde v Saudi Arabia | 32.2% | 28.9% | **39.0%** | 1.14–1.28 | 1-1 |

## Group projections

### Group A

**✅ Into the knockouts:** Mexico

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Mexico ✅ | 2 | 2-0-0 | 3-0 | **6** | 8.50 | 100.0% | 100.0% | 100.0% |
| South Korea | 2 | 1-0-1 | 2-2 | **3** | 4.85 | 0.0% | 79.7% | 95.5% |
| Czech Republic | 2 | 0-1-1 | 2-3 | **1** | 1.34 | 0.0% | 1.0% | 6.7% |
| South Africa | 2 | 0-1-1 | 1-3 | **1** | 1.88 | 0.0% | 19.3% | 20.6% |

### Group B

**✅ Into the knockouts:** Canada, Switzerland

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Canada ✅ | 2 | 1-1-0 | 7-1 | **4** | 5.53 | 70.8% | 100.0% | 100.0% |
| Switzerland ✅ | 2 | 1-1-0 | 5-2 | **4** | 5.17 | 29.2% | 100.0% | 100.0% |
| Bosnia and Herzegovina | 2 | 0-1-1 | 2-5 | **1** | 2.66 | 0.0% | 0.0% | 45.7% |
| Qatar | 2 | 0-1-1 | 1-7 | **1** | 2.05 | 0.0% | 0.0% | 25.4% |

### Group C

**✅ Into the knockouts:** Brazil, Morocco

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Brazil ✅ | 2 | 1-1-0 | 4-1 | **4** | 6.22 | 68.0% | 89.0% | 100.0% |
| Morocco ✅ | 2 | 1-1-0 | 2-1 | **4** | 6.37 | 28.7% | 99.0% | 100.0% |
| Scotland | 2 | 1-0-1 | 1-1 | **3** | 3.57 | 3.3% | 12.1% | 83.7% |
| Haiti | 2 | 0-0-2 | 0-4 | **0** | 0.45 | 0.0% | 0.0% | 0.0% |

### Group D

**✅ Into the knockouts:** United States

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| United States ✅ | 2 | 2-0-0 | 6-1 | **6** | 7.77 | 100.0% | 100.0% | 100.0% |
| Australia | 2 | 1-0-1 | 2-2 | **3** | 4.35 | 0.0% | 64.3% | 95.1% |
| Paraguay | 2 | 1-0-1 | 2-4 | **3** | 4.36 | 0.0% | 35.7% | 86.3% |
| Turkey | 2 | 0-0-2 | 0-3 | **0** | 0.97 | 0.0% | 0.0% | 0.0% |

### Group E

**✅ Into the knockouts:** Germany

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Germany ✅ | 2 | 2-0-0 | 9-2 | **6** | 7.69 | 100.0% | 100.0% | 100.0% |
| Ivory Coast | 2 | 1-0-1 | 2-2 | **3** | 4.96 | 0.0% | 82.9% | 93.8% |
| Ecuador | 2 | 0-1-1 | 0-1 | **1** | 2.02 | 0.0% | 4.1% | 25.4% |
| Curaçao | 2 | 0-1-1 | 1-7 | **1** | 1.78 | 0.0% | 13.0% | 17.1% |

### Group F

**✅ Into the knockouts:** Netherlands, Japan

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Netherlands ✅ | 2 | 1-1-0 | 7-3 | **4** | 6.42 | 53.8% | 99.8% | 100.0% |
| Japan ✅ | 2 | 1-1-0 | 6-2 | **4** | 6.31 | 43.2% | 88.5% | 100.0% |
| Sweden | 2 | 1-0-1 | 6-6 | **3** | 3.52 | 2.9% | 11.7% | 87.3% |
| Tunisia | 2 | 0-0-2 | 1-9 | **0** | 0.40 | 0.0% | 0.0% | 0.0% |

### Group G

**✅ Into the knockouts:** Egypt

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Egypt ✅ | 2 | 1-1-0 | 4-2 | **4** | 5.30 | 58.5% | 79.4% | 100.0% |
| Iran | 2 | 0-2-0 | 2-2 | **2** | 3.40 | 26.2% | 41.6% | 69.6% |
| Belgium | 2 | 0-2-0 | 1-1 | **2** | 3.95 | 15.3% | 67.5% | 82.2% |
| New Zealand | 2 | 0-1-1 | 3-5 | **1** | 1.80 | 0.0% | 11.5% | 18.2% |

### Group H

**✅ Into the knockouts:** Spain

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Spain ✅ | 2 | 1-1-0 | 4-0 | **4** | 6.11 | 85.8% | 95.6% | 100.0% |
| Uruguay | 2 | 0-2-0 | 3-3 | **2** | 2.65 | 12.4% | 20.1% | 41.9% |
| Cape Verde | 2 | 0-2-0 | 2-2 | **2** | 3.26 | 1.8% | 50.8% | 61.7% |
| Saudi Arabia | 2 | 0-1-1 | 1-5 | **1** | 2.46 | 0.0% | 33.5% | 39.1% |

### Group I

**✅ Into the knockouts:** France, Norway

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| France ✅ | 2 | 2-0-0 | 6-1 | **6** | 8.08 | 83.6% | 100.0% | 100.0% |
| Norway ✅ | 2 | 2-0-0 | 7-3 | **6** | 6.71 | 16.4% | 100.0% | 100.0% |
| Senegal | 2 | 0-0-2 | 3-6 | **0** | 2.09 | 0.0% | 0.0% | 57.4% |
| Iraq | 2 | 0-0-2 | 1-7 | **0** | 0.69 | 0.0% | 0.0% | 6.5% |

### Group J

**✅ Into the knockouts:** Argentina

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Argentina ✅ | 2 | 2-0-0 | 5-0 | **6** | 8.63 | 100.0% | 100.0% | 100.0% |
| Austria | 2 | 1-0-1 | 3-3 | **3** | 4.54 | 0.0% | 70.9% | 96.7% |
| Algeria | 2 | 1-0-1 | 2-4 | **3** | 4.17 | 0.0% | 29.1% | 82.5% |
| Jordan | 2 | 0-0-2 | 2-5 | **0** | 0.23 | 0.0% | 0.0% | 0.0% |

### Group K

**✅ Into the knockouts:** Portugal

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Portugal ✅ | 2 | 1-1-0 | 6-1 | **4** | 5.37 | 43.6% | 93.2% | 100.0% |
| Colombia | 1 | 1-0-0 | 3-1 | **3** | 6.51 | 52.6% | 87.4% | 99.6% |
| DR Congo | 1 | 0-1-0 | 1-1 | **1** | 3.11 | 3.9% | 19.4% | 55.6% |
| Uzbekistan | 2 | 0-0-2 | 1-8 | **0** | 1.20 | 0.0% | 0.0% | 8.7% |

### Group L

**✅ Into the knockouts:** England, Ghana

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| England ✅ | 2 | 1-1-0 | 4-2 | **4** | 6.06 | 66.0% | 99.7% | 100.0% |
| Ghana ✅ | 2 | 1-1-0 | 1-0 | **4** | 4.68 | 9.5% | 38.6% | 100.0% |
| Croatia | 2 | 1-0-1 | 3-4 | **3** | 5.09 | 24.5% | 61.7% | 97.7% |
| Panama | 2 | 0-0-2 | 0-2 | **0** | 0.71 | 0.0% | 0.0% | 0.0% |

*\*Advance = top two or one of the eight best third-placed teams.*

*✅ = already reached the knockout stage — locked into the Round of 32 in every simulation. (Reaching later rounds still requires winning knockout games, so those stay below 100%.)*

## Most likely knockout bracket

Each tie shows the projected pairing and the side that advances — the team **more likely to win the tournament** of the two, so the bracket crowns the overall favourite. 'Win prob' is that team's chance in that single match (a **†** flags a near-even tie where the title favourite is a slight underdog in the one-off game). **🔒 marks a confirmed tie** — the same two teams in every simulation, mathematically locked. (0/16 Round-of-32 ties locked so far; the rest finalise as the group stage completes on 27 June.)

### Round of 32

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 73 | 2026-06-28 | SoFi Stadium, Los Angeles | South Korea v Switzerland | **Switzerland** | 64.2% | 56.4% |
| 74 | 2026-06-29 | Gillette Stadium, Boston | Germany v Sweden | **Germany** | 80.2% | 13.4% |
| 75 | 2026-06-29 | Estadio BBVA, Monterrey | Netherlands v Morocco | **Netherlands** | 56.5% | 37.9% |
| 76 | 2026-06-29 | NRG Stadium, Houston | Brazil v Japan | **Brazil** | 55.6% | 30.7% |
| 77 | 2026-06-30 | MetLife Stadium, New York/New Jersey | France v Paraguay | **France** | 77.1% | 27.6% |
| 78 | 2026-06-30 | AT&T Stadium, Dallas | Ivory Coast v Norway | **Norway** | 69.3% | 69.4% |
| 79 | 2026-06-30 | Estadio Azteca, Mexico City | Mexico v Scotland | **Mexico** | 82.7% | 49.5% |
| 80 | 2026-07-01 | Mercedes-Benz Stadium, Atlanta | England v DR Congo | **England** | 88.5% | 23.8% |
| 81 | 2026-07-01 | Levi's Stadium, San Francisco Bay Area | United States v Bosnia and Herzegovina | **United States** | 90.1% | 29.6% |
| 82 | 2026-07-01 | Lumen Field, Seattle | Egypt v Senegal | **Egypt** | 46.0%† | 11.6% |
| 83 | 2026-07-02 | BMO Field, Toronto | Portugal v Croatia | **Portugal** | 76.9% | 18.6% |
| 84 | 2026-07-02 | SoFi Stadium, Los Angeles | Spain v Austria | **Spain** | 77.0% | 60.8% |
| 85 | 2026-07-02 | BC Place, Vancouver | Canada v Algeria | **Canada** | 63.6% | 6.2% |
| 86 | 2026-07-03 | Hard Rock Stadium, Miami | Argentina v Cape Verde | **Argentina** | 91.6% | 49.0% |
| 87 | 2026-07-03 | Arrowhead Stadium, Kansas City | Colombia v Ghana | **Colombia** | 85.2% | 32.5% |
| 88 | 2026-07-03 | AT&T Stadium, Dallas | Australia v Belgium | **Belgium** | 58.9% | 33.6% |

### Round of 16

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 89 | 2026-07-04 | Lincoln Financial Field, Philadelphia | Germany v France | **France** | 78.4% | 42.1% |
| 90 | 2026-07-04 | NRG Stadium, Houston | Switzerland v Netherlands | **Netherlands** | 64.9% | 13.4% |
| 91 | 2026-07-05 | MetLife Stadium, New York/New Jersey | Brazil v Norway | **Brazil** | 56.3% | 23.8% |
| 92 | 2026-07-05 | Estadio Azteca, Mexico City | Mexico v England | **England** | 45.1%† | 42.0% |
| 93 | 2026-07-06 | AT&T Stadium, Dallas | Portugal v Spain | **Spain** | 60.3% | 22.2% |
| 94 | 2026-07-06 | Lumen Field, Seattle | United States v Egypt | **United States** | 70.7% | 23.4% |
| 95 | 2026-07-07 | Mercedes-Benz Stadium, Atlanta | Argentina v Belgium | **Argentina** | 78.0% | 26.6% |
| 96 | 2026-07-07 | BC Place, Vancouver | Canada v Colombia | **Colombia** | 60.5% | 20.5% |

### Quarter-finals

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 97 | 2026-07-09 | Gillette Stadium, Boston | France v Netherlands | **France** | 54.0% | 9.2% |
| 98 | 2026-07-10 | SoFi Stadium, Los Angeles | Spain v United States | **Spain** | 73.0% | 24.2% |
| 99 | 2026-07-11 | Hard Rock Stadium, Miami | Brazil v England | **England** | 57.0% | 6.2% |
| 100 | 2026-07-11 | Arrowhead Stadium, Kansas City | Argentina v Colombia | **Argentina** | 69.6% | 20.4% |

### Semi-finals

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 101 | 2026-07-14 | AT&T Stadium, Dallas | France v Spain | **Spain** | 65.8% | 10.5% |
| 102 | 2026-07-15 | Mercedes-Benz Stadium, Atlanta | England v Argentina | **Argentina** | 69.7% | 9.6% |

### Final

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 104 | 2026-07-19 | MetLife Stadium, East Rutherford | Spain v Argentina | **Argentina** | 55.7% | 11.2% |

**Projected champion: Argentina** (overall title probability 31.1%). The bracket advances the team more likely to go all the way in each tie, so the champion here matches the title favourite at the top of the page.

*† The title favourite reaches this tie via an easier path, so it wins the tournament most often even though this specific one-off match is a near coin-flip the other side shades.*

## How to read this

- All figures are probabilities, not certainties — a 65% favourite loses about one such match in three.
- `xPts` = expected group points; `xG` = expected goals from the Poisson model.
- Predictions refresh after every match day: run `python -m worldcup.run all` to pull new results, re-rate teams, and re-simulate.
- Machine-readable outputs: `match_probabilities.csv`, `tournament_projections.csv`. Past reports in `outputs/archive/`.

## Model scorecard

**28 of 47 match outcomes called correctly** (the model's own probabilities expected ≈27.6 of 47) · exact scoreline predicted 3/47 · average probability placed on what actually happened: **44.3%** (33.3% = guessing).

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
| Austria v Jordan | Austria win (47.0%) | 1-1 | 3-1 | ✅ | — |
| Argentina v Algeria | Argentina win (68.0%) | 2-0 | 3-0 | ✅ | — |
| France v Senegal | France win (59.1%) | 1-0 | 3-1 | ✅ | — |
| England v Croatia | England win (56.9%) | 1-0 | 4-2 | ✅ | — |
| Ghana v Panama | Panama win (51.9%) | 1-1 | 1-0 | ❌ | — |
| Portugal v DR Congo | Portugal win (70.6%) | 2-0 | 1-1 | ❌ | — |
| Uzbekistan v Colombia | Colombia win (53.9%) | 0-1 | 1-3 | ✅ | — |
| Czech Republic v South Africa | Czech Republic win (55.5%) | 1-0 | 1-1 | ❌ | — |
| Mexico v South Korea | Mexico win (51.1%) | 1-1 | 1-0 | ✅ | — |
| Switzerland v Bosnia and Herzegovina | Switzerland win (66.8%) | 2-0 | 4-1 | ✅ | — |
| Canada v Qatar | Canada win (74.0%) | 2-0 | 6-0 | ✅ | — |
| Turkey v Paraguay | Paraguay win (38.4%) | 1-1 | 0-1 | ✅ | — |
| Scotland v Morocco | Morocco win (49.3%) | 1-1 | 0-1 | ✅ | — |
| Brazil v Haiti | Brazil win (81.3%) | 2-0 | 3-0 | ✅ | — |
| United States v Australia | Australia win (35.9%) | 1-1 | 2-0 | ❌ | — |
| Ecuador v Curaçao | Ecuador win (81.9%) | 2-0 | 0-0 | ❌ | — |
| Germany v Ivory Coast | Germany win (50.9%) | 1-1 | 2-1 | ✅ | — |
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
| England v Ghana | England win (75.8%) | 2-0 | 0-0 | ❌ | — |
| Portugal v Uzbekistan | Portugal win (63.7%) | 1-0 | 5-0 | ✅ | — |
| Panama v Croatia | Croatia win (42.4%) | 1-1 | 0-1 | ✅ | — |

**Calibration vs benchmarks** (the 9 graded games with bookmaker prices on file) — log-loss, lower is better. This is the honest test: is the model bad, or were the games hard for everyone?

| Forecaster | Log-loss |
|------------|---------:|
| **This model** | **1.193** |
| Sky Bet (de-vigged) | 1.156 |
| Coin-flip (33/33/33) | 1.099 |

The model is **essentially level with the market** (+0.037 log-loss). Note both the model **and** the bookmaker scored worse than a coin-flip here — with this many draws and upsets, the slate was close to unforecastable for anyone, which is the real reason the hit-rate looks poor.


*Predictions are frozen at the last run before each result arrives, then graded — the scorecard never grades a model that has already seen the answer.*

