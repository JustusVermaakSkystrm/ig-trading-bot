# FIFA World Cup 2026 — ML Prediction Report

*Generated 2026-06-21 · data through **2026-06-21** · 50,000 Monte Carlo simulations · 38/72 group matches played*

Probabilities come from a gradient-boosted Poisson goal model (Elo strength + rolling form + venue/importance features) trained on 30,810 internationals, simulated through the official 2026 bracket and tiebreaker rules.

*Rolling validation (7,966 matches, 2018–2026): RPS 0.1687 vs Elo-baseline 0.1711; log-loss 0.8652 vs 0.8809.*

## Title favourites

| # | Team | Group | Champion | Δ vs 2026-06-21 | Final | Semi-final | Quarter-final | Rd of 16 |
|---|------|:-----:|---------:|-------:|------:|-----------:|--------------:|---------:|
| 1 | Argentina | J | **20.0%** | +0.4 | 30.7% | 46.1% | 61.0% | 73.2% |
| 2 | Spain ✅ | H | **17.3%** | -1.4 | 26.9% | 39.4% | 52.7% | 69.8% |
| 3 | France | I | **9.5%** | +0.7 | 17.7% | 32.2% | 52.9% | 76.5% |
| 4 | England | L | **8.0%** | -0.5 | 14.2% | 25.8% | 40.0% | 76.2% |
| 5 | Colombia | K | **5.8%** | -0.4 | 11.4% | 21.0% | 42.9% | 73.1% |
| 6 | Brazil ✅ | C | **4.8%** | +0.3 | 9.5% | 19.8% | 35.4% | 58.0% |
| 7 | Mexico ✅ | A | **4.4%** | +1.0 | 10.3% | 22.0% | 48.9% | 81.1% |
| 8 | Netherlands ✅ | F | **3.9%** | +0.4 | 8.4% | 18.1% | 34.3% | 55.1% |
| 9 | Japan ✅ | F | **3.3%** | – | 7.4% | 15.5% | 30.6% | 52.5% |
| 10 | United States ✅ | D | **3.2%** | -0.3 | 8.6% | 20.3% | 50.9% | 79.5% |
| 11 | Norway | I | **2.7%** | +0.4 | 6.3% | 15.2% | 33.2% | 64.9% |
| 12 | Portugal | K | **2.6%** | -0.1 | 6.3% | 13.0% | 24.6% | 51.7% |
| 13 | Germany ✅ | E | **2.3%** | -0.6 | 5.9% | 13.0% | 26.6% | 63.0% |
| 14 | Morocco ✅ | C | **2.3%** | +0.4 | 5.7% | 12.0% | 26.0% | 44.2% |
| 15 | Switzerland ✅ | B | **1.6%** | – | 4.6% | 11.9% | 26.3% | 64.9% |

## Biggest movers since last run (data through 2026-06-21)

| Team | Δ Champion | Δ Rd of 16 | Champion now |
|------|----------:|-----------:|-------------:|
| Mexico | +1.0 | +4.5 | 4.4% |
| France | +0.7 | +0.4 | 9.5% |
| Argentina | +0.4 | – | 20.0% |
| Netherlands | +0.4 | +1.6 | 3.9% |
| England | -0.5 | +2.8 | 8.0% |
| Belgium | -0.5 | -6.3 | 1.4% |
| Germany | -0.6 | -4.4 | 2.3% |
| Spain | -1.4 | -1.0 | 17.3% |

*Δ values in probability points. Full run-by-run series in `outputs/history.csv`.*

## Path to the final

The model's single most likely knockout bracket — all 32 projected round-of-32 teams and every unplayed tie, each line carrying the projected winner down to the next round until they converge on the champion. Percentages are each side's chance of advancing from that tie. **A gold-bordered box is a confirmed Round-of-32 tie** (the same pairing in every simulation — mathematically locked): 0/16 locked so far, the rest finalise as the group stage ends on 27 June.

<div style="overflow-x:auto; margin:1rem 0;">
<svg viewBox="0 0 1964 662" width="100%" preserveAspectRatio="xMidYMin meet" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica,Arial,sans-serif"><path d="M82,98 C82,134 142,134 142,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M202,98 C202,134 142,134 142,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M322,98 C322,134 382,134 382,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M442,98 C442,134 382,134 382,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M562,98 C562,134 622,134 622,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M682,98 C682,134 622,134 622,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M802,98 C802,134 862,134 862,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M922,98 C922,134 862,134 862,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1042,98 C1042,134 1102,134 1102,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1162,98 C1162,134 1102,134 1102,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1282,98 C1282,134 1342,134 1342,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1402,98 C1402,134 1342,134 1342,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1522,98 C1522,134 1582,134 1582,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1642,98 C1642,134 1582,134 1582,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1762,98 C1762,134 1822,134 1822,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1882,98 C1882,134 1822,134 1822,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M142,214 C142,250 262,250 262,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M382,214 C382,250 262,250 262,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M622,214 C622,250 742,250 742,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M862,214 C862,250 742,250 742,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1102,214 C1102,250 1222,250 1222,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1342,214 C1342,250 1222,250 1222,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1582,214 C1582,250 1702,250 1702,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1822,214 C1822,250 1702,250 1702,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M262,330 C262,366 502,366 502,402" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M742,330 C742,366 502,366 502,402" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1222,330 C1222,366 1462,366 1462,402" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1702,330 C1702,366 1462,366 1462,402" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M502,446 C502,482 982,482 982,518" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1462,446 C1462,482 982,482 982,518" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M982,562 C982,580 982,580 982,598" fill="none" stroke="#33436b" stroke-width="1.5"/><text x="11" y="76" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 11 76)" text-anchor="middle">ROUND OF 32</text><text x="11" y="192" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 11 192)" text-anchor="middle">ROUND OF 16</text><text x="11" y="308" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 11 308)" text-anchor="middle">QUARTER-FINALS</text><text x="11" y="424" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 11 424)" text-anchor="middle">SEMI-FINALS</text><text x="11" y="540" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 11 540)" text-anchor="middle">FINAL</text><rect x="26" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="26" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="34" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Germany</text><text x="130" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">76%</text><text x="34" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Sweden</text><text x="130" y="91" font-size="9" text-anchor="end" fill="#5d6880">24%</text><rect x="146" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="146" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="154" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">France</text><text x="250" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">74%</text><text x="154" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Paraguay</text><text x="250" y="91" font-size="9" text-anchor="end" fill="#5d6880">26%</text><rect x="266" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="274" y="71" font-size="10.5" font-weight="400" fill="#7c89a3">S. Korea</text><text x="370" y="71" font-size="9" text-anchor="end" fill="#5d6880">35%</text><rect x="266" y="77" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="274" y="91" font-size="10.5" font-weight="700" fill="#7ef0b6">Switzerland</text><text x="370" y="91" font-size="9" text-anchor="end" fill="#cfe8d8">65%</text><rect x="386" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="386" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="394" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Netherlands</text><text x="490" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">59%</text><text x="394" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Morocco</text><text x="490" y="91" font-size="9" text-anchor="end" fill="#5d6880">41%</text><rect x="506" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="506" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="514" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Portugal</text><text x="610" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">60%</text><text x="514" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Croatia</text><text x="610" y="91" font-size="9" text-anchor="end" fill="#5d6880">40%</text><rect x="626" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="626" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="634" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Spain</text><text x="730" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">77%</text><text x="634" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Austria</text><text x="730" y="91" font-size="9" text-anchor="end" fill="#5d6880">23%</text><rect x="746" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="746" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="754" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">USA</text><text x="850" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">90%</text><text x="754" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Bosnia</text><text x="850" y="91" font-size="9" text-anchor="end" fill="#5d6880">10%</text><rect x="866" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="866" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="874" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Belgium</text><text x="970" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">81%</text><text x="874" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">C. Verde</text><text x="970" y="91" font-size="9" text-anchor="end" fill="#5d6880">19%</text><rect x="986" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="986" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="994" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Brazil</text><text x="1090" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">55%</text><text x="994" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Japan</text><text x="1090" y="91" font-size="9" text-anchor="end" fill="#5d6880">45%</text><rect x="1106" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="1114" y="71" font-size="10.5" font-weight="400" fill="#7c89a3">Ivory Coast</text><text x="1210" y="71" font-size="9" text-anchor="end" fill="#5d6880">30%</text><rect x="1106" y="77" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1114" y="91" font-size="10.5" font-weight="700" fill="#7ef0b6">Norway</text><text x="1210" y="91" font-size="9" text-anchor="end" fill="#cfe8d8">70%</text><rect x="1226" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1226" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1234" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Mexico</text><text x="1330" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">86%</text><text x="1234" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Scotland</text><text x="1330" y="91" font-size="9" text-anchor="end" fill="#5d6880">14%</text><rect x="1346" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1346" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1354" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">England</text><text x="1450" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">79%</text><text x="1354" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Senegal</text><text x="1450" y="91" font-size="9" text-anchor="end" fill="#5d6880">21%</text><rect x="1466" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1466" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1474" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Argentina</text><text x="1570" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">77%</text><text x="1474" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Uruguay</text><text x="1570" y="91" font-size="9" text-anchor="end" fill="#5d6880">23%</text><rect x="1586" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1586" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1594" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Australia</text><text x="1690" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">59%</text><text x="1594" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Egypt</text><text x="1690" y="91" font-size="9" text-anchor="end" fill="#5d6880">41%</text><rect x="1706" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1706" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1714" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Canada</text><text x="1810" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">65%</text><text x="1714" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Algeria</text><text x="1810" y="91" font-size="9" text-anchor="end" fill="#5d6880">35%</text><rect x="1826" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1826" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1834" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Colombia</text><text x="1930" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">85%</text><text x="1834" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Ghana</text><text x="1930" y="91" font-size="9" text-anchor="end" fill="#5d6880">15%</text><rect x="86" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="94" y="187" font-size="10.5" font-weight="400" fill="#7c89a3">Germany</text><text x="190" y="187" font-size="9" text-anchor="end" fill="#5d6880">30%</text><rect x="86" y="193" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="94" y="207" font-size="10.5" font-weight="700" fill="#7ef0b6">France</text><text x="190" y="207" font-size="9" text-anchor="end" fill="#cfe8d8">70%</text><rect x="326" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="334" y="187" font-size="10.5" font-weight="400" fill="#7c89a3">Switzerland</text><text x="430" y="187" font-size="9" text-anchor="end" fill="#5d6880">36%</text><rect x="326" y="193" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="334" y="207" font-size="10.5" font-weight="700" fill="#7ef0b6">Netherlands</text><text x="430" y="207" font-size="9" text-anchor="end" fill="#cfe8d8">64%</text><rect x="566" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="574" y="187" font-size="10.5" font-weight="400" fill="#7c89a3">Portugal</text><text x="670" y="187" font-size="9" text-anchor="end" fill="#5d6880">34%</text><rect x="566" y="193" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="574" y="207" font-size="10.5" font-weight="700" fill="#7ef0b6">Spain</text><text x="670" y="207" font-size="9" text-anchor="end" fill="#cfe8d8">66%</text><rect x="806" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="806" y="172" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="814" y="187" font-size="10.5" font-weight="700" fill="#7ef0b6">USA</text><text x="910" y="187" font-size="9" text-anchor="end" fill="#cfe8d8">52%</text><text x="814" y="207" font-size="10.5" font-weight="400" fill="#7c89a3">Belgium</text><text x="910" y="207" font-size="9" text-anchor="end" fill="#5d6880">48%</text><rect x="1046" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1046" y="172" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1054" y="187" font-size="10.5" font-weight="700" fill="#7ef0b6">Brazil</text><text x="1150" y="187" font-size="9" text-anchor="end" fill="#cfe8d8">56%</text><text x="1054" y="207" font-size="10.5" font-weight="400" fill="#7c89a3">Norway</text><text x="1150" y="207" font-size="9" text-anchor="end" fill="#5d6880">44%</text><rect x="1286" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1286" y="172" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1294" y="187" font-size="10.5" font-weight="700" fill="#7ef0b6">Mexico</text><text x="1390" y="187" font-size="9" text-anchor="end" fill="#cfe8d8">52%</text><text x="1294" y="207" font-size="10.5" font-weight="400" fill="#7c89a3">England</text><text x="1390" y="207" font-size="9" text-anchor="end" fill="#5d6880">48%</text><rect x="1526" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1526" y="172" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1534" y="187" font-size="10.5" font-weight="700" fill="#7ef0b6">Argentina</text><text x="1630" y="187" font-size="9" text-anchor="end" fill="#cfe8d8">84%</text><text x="1534" y="207" font-size="10.5" font-weight="400" fill="#7c89a3">Australia</text><text x="1630" y="207" font-size="9" text-anchor="end" fill="#5d6880">16%</text><rect x="1766" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="1774" y="187" font-size="10.5" font-weight="400" fill="#7c89a3">Canada</text><text x="1870" y="187" font-size="9" text-anchor="end" fill="#5d6880">42%</text><rect x="1766" y="193" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1774" y="207" font-size="10.5" font-weight="700" fill="#7ef0b6">Colombia</text><text x="1870" y="207" font-size="9" text-anchor="end" fill="#cfe8d8">58%</text><rect x="206" y="286" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="206" y="288" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="214" y="303" font-size="10.5" font-weight="700" fill="#7ef0b6">France</text><text x="310" y="303" font-size="9" text-anchor="end" fill="#cfe8d8">55%</text><text x="214" y="323" font-size="10.5" font-weight="400" fill="#7c89a3">Netherlands</text><text x="310" y="323" font-size="9" text-anchor="end" fill="#5d6880">45%</text><rect x="686" y="286" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="686" y="288" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="694" y="303" font-size="10.5" font-weight="700" fill="#7ef0b6">Spain</text><text x="790" y="303" font-size="9" text-anchor="end" fill="#cfe8d8">73%</text><text x="694" y="323" font-size="10.5" font-weight="400" fill="#7c89a3">USA</text><text x="790" y="323" font-size="9" text-anchor="end" fill="#5d6880">27%</text><rect x="1166" y="286" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1166" y="288" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1174" y="303" font-size="10.5" font-weight="700" fill="#7ef0b6">Brazil</text><text x="1270" y="303" font-size="9" text-anchor="end" fill="#cfe8d8">63%</text><text x="1174" y="323" font-size="10.5" font-weight="400" fill="#7c89a3">Mexico</text><text x="1270" y="323" font-size="9" text-anchor="end" fill="#5d6880">37%</text><rect x="1646" y="286" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1646" y="288" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1654" y="303" font-size="10.5" font-weight="700" fill="#7ef0b6">Argentina</text><text x="1750" y="303" font-size="9" text-anchor="end" fill="#cfe8d8">66%</text><text x="1654" y="323" font-size="10.5" font-weight="400" fill="#7c89a3">Colombia</text><text x="1750" y="323" font-size="9" text-anchor="end" fill="#5d6880">34%</text><rect x="446" y="402" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="454" y="419" font-size="10.5" font-weight="400" fill="#7c89a3">France</text><text x="550" y="419" font-size="9" text-anchor="end" fill="#5d6880">37%</text><rect x="446" y="425" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="454" y="439" font-size="10.5" font-weight="700" fill="#7ef0b6">Spain</text><text x="550" y="439" font-size="9" text-anchor="end" fill="#cfe8d8">63%</text><rect x="1406" y="402" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="1414" y="419" font-size="10.5" font-weight="400" fill="#7c89a3">Brazil</text><text x="1510" y="419" font-size="9" text-anchor="end" fill="#5d6880">30%</text><rect x="1406" y="425" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1414" y="439" font-size="10.5" font-weight="700" fill="#7ef0b6">Argentina</text><text x="1510" y="439" font-size="9" text-anchor="end" fill="#cfe8d8">70%</text><rect x="926" y="518" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="926" y="520" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="934" y="535" font-size="10.5" font-weight="700" fill="#7ef0b6">Spain</text><text x="1030" y="535" font-size="9" text-anchor="end" fill="#cfe8d8">53%</text><text x="934" y="555" font-size="10.5" font-weight="400" fill="#7c89a3">Argentina</text><text x="1030" y="555" font-size="9" text-anchor="end" fill="#5d6880">47%</text><rect x="888" y="598" width="188" height="46" rx="10" fill="#f5c542"/><text x="982" y="619" font-size="13" font-weight="800" fill="#1a1300" text-anchor="middle">🏆 Spain</text><text x="982" y="635" font-size="10" fill="#5a4a00" text-anchor="middle">projected champion · 17% to win</text></svg>
</div>

## Upcoming group matches — outcome probabilities

*(next match days; full list for all 72 group games in `match_probabilities.csv`)*

| Date | Grp | Match | Home win | Draw | Away win | xG | Likely score |
|------|:---:|-------|---------:|-----:|---------:|----|:----:|
| 2026-06-21 | G | New Zealand v Egypt | 29.3% | 27.3% | **43.4%** | 1.15–1.45 | 1-1 |
| 2026-06-21 | H | Uruguay v Cape Verde | **72.7%** | 18.2% | 9.1% | 2.22–0.66 | 2-0 |
| 2026-06-22 | I | France v Iraq | **75.0%** | 16.8% | 8.2% | 2.36–0.66 | 2-0 |
| 2026-06-22 | I | Norway v Senegal | **46.4%** | 26.9% | 26.6% | 1.52–1.09 | 1-1 |
| 2026-06-22 | J | Argentina v Austria | **67.8%** | 20.2% | 11.9% | 2.10–0.76 | 2-0 |
| 2026-06-22 | J | Jordan v Algeria | 25.8% | 26.9% | **47.3%** | 1.06–1.52 | 1-1 |
| 2026-06-23 | K | Portugal v Uzbekistan | **61.7%** | 23.7% | 14.6% | 1.79–0.75 | 1-0 |
| 2026-06-23 | K | Colombia v DR Congo | **64.2%** | 22.8% | 12.9% | 1.84–0.70 | 1-0 |
| 2026-06-23 | L | England v Ghana | **75.5%** | 17.9% | 6.6% | 2.12–0.48 | 2-0 |
| 2026-06-23 | L | Panama v Croatia | 28.7% | 27.2% | **44.0%** | 1.14–1.47 | 1-1 |
| 2026-06-24 | C | Morocco v Haiti | **72.7%** | 18.7% | 8.6% | 2.14–0.60 | 2-0 |
| 2026-06-24 | B | Bosnia and Herzegovina v Qatar | **44.7%** | 29.7% | 25.5% | 1.30–0.91 | 1-1 |
| 2026-06-24 | C | Scotland v Brazil | 16.5% | 23.5% | **59.9%** | 0.86–1.84 | 0-1 |
| 2026-06-24 | A | South Africa v South Korea | 20.6% | 27.2% | **52.2%** | 0.86–1.52 | 0-1 |
| 2026-06-24 | A | Mexico v Czech Republic | **81.6%** | 13.8% | 4.5% | 2.47–0.44 | 2-0 |
| 2026-06-24 | B | Canada v Switzerland | **41.3%** | 29.5% | 29.1% | 1.27–1.02 | 1-1 |

## Group projections

### Group A

**✅ Into the knockouts:** Mexico

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Mexico ✅ | 2 | 2-0-0 | 3-0 | **6** | 8.59 | 100.0% | 100.0% | 100.0% |
| South Korea | 2 | 1-0-1 | 2-2 | **3** | 4.83 | 0.0% | 79.0% | 95.3% |
| Czech Republic | 2 | 0-1-1 | 2-3 | **1** | 1.27 | 0.0% | 0.9% | 5.7% |
| South Africa | 2 | 0-1-1 | 1-3 | **1** | 1.90 | 0.0% | 20.2% | 21.4% |

### Group B

**✅ Into the knockouts:** Canada, Switzerland

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Canada ✅ | 2 | 1-1-0 | 7-1 | **4** | 5.54 | 71.0% | 100.0% | 100.0% |
| Switzerland ✅ | 2 | 1-1-0 | 5-2 | **4** | 5.17 | 29.0% | 100.0% | 100.0% |
| Bosnia and Herzegovina | 2 | 0-1-1 | 2-5 | **1** | 2.64 | 0.0% | 0.0% | 45.1% |
| Qatar | 2 | 0-1-1 | 1-7 | **1** | 2.06 | 0.0% | 0.0% | 25.2% |

### Group C

**✅ Into the knockouts:** Brazil, Morocco

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Brazil ✅ | 2 | 1-1-0 | 4-1 | **4** | 6.03 | 61.5% | 84.9% | 100.0% |
| Morocco ✅ | 2 | 1-1-0 | 2-1 | **4** | 6.37 | 34.0% | 98.5% | 100.0% |
| Scotland | 2 | 1-0-1 | 1-1 | **3** | 3.74 | 4.5% | 16.6% | 86.0% |
| Haiti | 2 | 0-0-2 | 0-4 | **0** | 0.45 | 0.0% | 0.0% | 0.0% |

### Group D

**✅ Into the knockouts:** United States

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| United States ✅ | 2 | 2-0-0 | 6-1 | **6** | 7.68 | 100.0% | 100.0% | 100.0% |
| Australia | 2 | 1-0-1 | 2-2 | **3** | 4.36 | 0.0% | 65.3% | 95.0% |
| Paraguay | 2 | 1-0-1 | 2-4 | **3** | 4.34 | 0.0% | 34.7% | 84.6% |
| Turkey | 2 | 0-0-2 | 0-3 | **0** | 1.06 | 0.0% | 0.0% | 0.0% |

### Group E

**✅ Into the knockouts:** Germany

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Germany ✅ | 2 | 2-0-0 | 9-2 | **6** | 7.68 | 100.0% | 100.0% | 100.0% |
| Ivory Coast | 2 | 1-0-1 | 2-2 | **3** | 4.94 | 0.0% | 82.6% | 93.6% |
| Ecuador | 2 | 0-1-1 | 0-1 | **1** | 2.03 | 0.0% | 4.3% | 26.9% |
| Curaçao | 2 | 0-1-1 | 1-7 | **1** | 1.79 | 0.0% | 13.0% | 17.3% |

### Group F

**✅ Into the knockouts:** Netherlands, Japan

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Netherlands ✅ | 2 | 1-1-0 | 7-3 | **4** | 6.22 | 53.1% | 99.5% | 100.0% |
| Japan ✅ | 2 | 1-1-0 | 6-2 | **4** | 6.10 | 41.4% | 83.9% | 100.0% |
| Sweden | 2 | 1-0-1 | 6-6 | **3** | 3.70 | 5.5% | 16.6% | 89.7% |
| Tunisia | 2 | 0-0-2 | 1-9 | **0** | 0.57 | 0.0% | 0.0% | 0.0% |

### Group G

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Iran | 2 | 0-2-0 | 2-2 | **2** | 3.43 | 23.7% | 49.1% | 69.3% |
| Belgium | 2 | 0-2-0 | 1-1 | **2** | 3.81 | 28.9% | 57.9% | 77.9% |
| New Zealand | 1 | 0-1-0 | 2-2 | **1** | 3.09 | 18.4% | 42.6% | 53.8% |
| Egypt | 1 | 0-1-0 | 1-1 | **1** | 3.84 | 28.9% | 50.4% | 70.1% |

### Group H

**✅ Into the knockouts:** Spain

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Spain ✅ | 2 | 1-1-0 | 4-0 | **4** | 5.95 | 78.6% | 98.0% | 100.0% |
| Uruguay | 1 | 0-1-0 | 1-1 | **1** | 4.17 | 19.3% | 77.7% | 83.8% |
| Cape Verde | 1 | 0-1-0 | 0-0 | **1** | 2.68 | 2.1% | 14.5% | 44.0% |
| Saudi Arabia | 2 | 0-1-1 | 1-5 | **1** | 2.47 | 0.0% | 9.8% | 38.6% |

### Group I

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Norway | 1 | 1-0-0 | 4-1 | **3** | 5.55 | 28.8% | 79.8% | 98.4% |
| France | 1 | 1-0-0 | 3-1 | **3** | 7.27 | 68.5% | 96.8% | 99.3% |
| Senegal | 1 | 0-0-1 | 1-3 | **0** | 3.07 | 2.0% | 21.0% | 62.1% |
| Iraq | 1 | 0-0-1 | 1-4 | **0** | 1.16 | 0.6% | 2.3% | 12.6% |

### Group J

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Argentina | 1 | 1-0-0 | 3-0 | **3** | 7.81 | 85.0% | 98.8% | 99.7% |
| Austria | 1 | 1-0-0 | 3-1 | **3** | 5.13 | 13.5% | 75.8% | 95.5% |
| Jordan | 1 | 0-0-1 | 1-3 | **0** | 1.33 | 0.6% | 2.7% | 18.3% |
| Algeria | 1 | 0-0-1 | 0-3 | **0** | 2.84 | 0.8% | 22.7% | 50.1% |

### Group K

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Colombia | 1 | 1-0-0 | 3-1 | **3** | 6.76 | 71.8% | 90.8% | 99.3% |
| DR Congo | 1 | 0-1-0 | 1-1 | **1** | 3.04 | 6.4% | 29.5% | 54.5% |
| Portugal | 1 | 0-1-0 | 1-1 | **1** | 4.19 | 20.8% | 65.3% | 81.2% |
| Uzbekistan | 1 | 0-0-1 | 1-3 | **0** | 1.95 | 1.0% | 14.5% | 32.7% |

### Group L

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| England | 1 | 1-0-0 | 4-2 | **3** | 7.60 | 87.9% | 98.1% | 99.5% |
| Ghana | 1 | 1-0-0 | 1-0 | **3** | 4.02 | 6.1% | 35.7% | 72.2% |
| Panama | 1 | 0-0-1 | 0-1 | **0** | 1.74 | 3.1% | 11.9% | 29.0% |
| Croatia | 1 | 0-0-1 | 2-4 | **0** | 3.73 | 2.9% | 54.4% | 72.1% |

*\*Advance = top two or one of the eight best third-placed teams.*

*✅ = already reached the knockout stage — locked into the Round of 32 in every simulation. (Reaching later rounds still requires winning knockout games, so those stay below 100%.)*

## Most likely knockout bracket

Each tie shows the most probable pairing given projected group finishes, the chance the named winner goes through **in that pairing**, and how often the exact pairing occurred across all simulations. **🔒 marks a confirmed tie** — the same two teams in every simulation, i.e. mathematically locked. (0/16 Round-of-32 ties locked so far; the rest finalise as the group stage completes on 27 June.)

### Round of 32

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 73 | 2026-06-28 | SoFi Stadium, Los Angeles | South Korea v Switzerland | **Switzerland** | 65.3% | 56.1% |
| 74 | 2026-06-29 | Gillette Stadium, Boston | Germany v Sweden | **Germany** | 75.5% | 14.9% |
| 75 | 2026-06-29 | Estadio BBVA, Monterrey | Netherlands v Morocco | **Netherlands** | 59.3% | 34.4% |
| 76 | 2026-06-29 | NRG Stadium, Houston | Brazil v Japan | **Brazil** | 55.2% | 26.3% |
| 77 | 2026-06-30 | MetLife Stadium, New York/New Jersey | France v Paraguay | **France** | 74.4% | 18.8% |
| 78 | 2026-06-30 | AT&T Stadium, Dallas | Ivory Coast v Norway | **Norway** | 70.1% | 42.2% |
| 79 | 2026-06-30 | Estadio Azteca, Mexico City | Mexico v Scotland | **Mexico** | 85.7% | 38.5% |
| 80 | 2026-07-01 | Mercedes-Benz Stadium, Atlanta | England v Senegal | **England** | 78.8% | 3.9% |
| 81 | 2026-07-01 | Levi's Stadium, San Francisco Bay Area | United States v Bosnia and Herzegovina | **United States** | 89.7% | 31.2% |
| 82 | 2026-07-01 | Lumen Field, Seattle | Belgium v Cape Verde | **Belgium** | 81.3% | 3.0% |
| 83 | 2026-07-02 | BMO Field, Toronto | Portugal v Croatia | **Portugal** | 59.7% | 23.0% |
| 84 | 2026-07-02 | SoFi Stadium, Los Angeles | Spain v Austria | **Spain** | 76.8% | 49.1% |
| 85 | 2026-07-02 | BC Place, Vancouver | Canada v Algeria | **Canada** | 65.0% | 3.4% |
| 86 | 2026-07-03 | Hard Rock Stadium, Miami | Argentina v Uruguay | **Argentina** | 77.2% | 49.8% |
| 87 | 2026-07-03 | Arrowhead Stadium, Kansas City | Colombia v Ghana | **Colombia** | 84.5% | 26.8% |
| 88 | 2026-07-03 | AT&T Stadium, Dallas | Australia v Egypt | **Australia** | 58.6% | 14.0% |

### Round of 16

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 89 | 2026-07-04 | Lincoln Financial Field, Philadelphia | Germany v France | **France** | 70.1% | 33.0% |
| 90 | 2026-07-04 | NRG Stadium, Houston | Switzerland v Netherlands | **Netherlands** | 64.2% | 14.6% |
| 91 | 2026-07-05 | MetLife Stadium, New York/New Jersey | Brazil v Norway | **Brazil** | 56.0% | 12.7% |
| 92 | 2026-07-05 | Estadio Azteca, Mexico City | Mexico v England | **Mexico** | 52.1% | 55.3% |
| 93 | 2026-07-06 | AT&T Stadium, Dallas | Portugal v Spain | **Spain** | 65.6% | 17.4% |
| 94 | 2026-07-06 | Lumen Field, Seattle | United States v Belgium | **United States** | 51.8% | 15.1% |
| 95 | 2026-07-07 | Mercedes-Benz Stadium, Atlanta | Argentina v Australia | **Argentina** | 84.2% | 23.2% |
| 96 | 2026-07-07 | BC Place, Vancouver | Canada v Colombia | **Colombia** | 58.2% | 26.8% |

### Quarter-finals

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 97 | 2026-07-09 | Gillette Stadium, Boston | France v Netherlands | **France** | 55.5% | 7.5% |
| 98 | 2026-07-10 | SoFi Stadium, Los Angeles | Spain v United States | **Spain** | 72.8% | 22.4% |
| 99 | 2026-07-11 | Hard Rock Stadium, Miami | Brazil v Mexico | **Brazil** | 62.8% | 10.1% |
| 100 | 2026-07-11 | Arrowhead Stadium, Kansas City | Argentina v Colombia | **Argentina** | 66.4% | 19.3% |

### Semi-finals

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 101 | 2026-07-14 | AT&T Stadium, Dallas | France v Spain | **Spain** | 62.7% | 7.7% |
| 102 | 2026-07-15 | Mercedes-Benz Stadium, Atlanta | Brazil v Argentina | **Argentina** | 70.2% | 4.8% |

### Final

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 104 | 2026-07-19 | MetLife Stadium, East Rutherford | Spain v Argentina | **Spain** | 53.3% | 7.2% |

**Projected champion: Spain** (overall title probability 17.3%; the single most likely path above is itself only one of many ways the tournament can unfold).

## How to read this

- All figures are probabilities, not certainties — a 65% favourite loses about one such match in three.
- `xPts` = expected group points; `xG` = expected goals from the Poisson model.
- Predictions refresh after every match day: run `python -m worldcup.run all` to pull new results, re-rate teams, and re-simulate.
- Machine-readable outputs: `match_probabilities.csv`, `tournament_projections.csv`. Past reports in `outputs/archive/`.

## Model scorecard

**21 of 38 match outcomes called correctly** (the model's own probabilities expected ≈22.2 of 38) · exact scoreline predicted 2/38 · average probability placed on what actually happened: **43.6%** (33.3% = guessing).

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
| Iraq v Norway | Norway win (59.1%) | 0-1 | 1-4 | ✅ | — |
| France v Senegal | France win (59.1%) | 1-0 | 3-1 | ✅ | — |
| Austria v Jordan | Austria win (47.0%) | 1-1 | 3-1 | ✅ | — |
| Argentina v Algeria | Argentina win (68.0%) | 2-0 | 3-0 | ✅ | — |
| Portugal v DR Congo | Portugal win (70.6%) | 2-0 | 1-1 | ❌ | — |
| Uzbekistan v Colombia | Colombia win (53.9%) | 0-1 | 1-3 | ✅ | — |
| England v Croatia | England win (56.9%) | 1-0 | 4-2 | ✅ | — |
| Ghana v Panama | Panama win (51.9%) | 1-1 | 1-0 | ❌ | — |
| Canada v Qatar | Canada win (74.0%) | 2-0 | 6-0 | ✅ | — |
| Switzerland v Bosnia and Herzegovina | Switzerland win (66.8%) | 2-0 | 4-1 | ✅ | — |
| Czech Republic v South Africa | Czech Republic win (55.5%) | 1-0 | 1-1 | ❌ | — |
| Mexico v South Korea | Mexico win (51.1%) | 1-1 | 1-0 | ✅ | — |
| Turkey v Paraguay | Paraguay win (38.4%) | 1-1 | 0-1 | ✅ | — |
| Scotland v Morocco | Morocco win (49.3%) | 1-1 | 0-1 | ✅ | — |
| Brazil v Haiti | Brazil win (81.3%) | 2-0 | 3-0 | ✅ | — |
| United States v Australia | Australia win (35.9%) | 1-1 | 2-0 | ❌ | — |
| Germany v Ivory Coast | Germany win (50.9%) | 1-1 | 2-1 | ✅ | — |
| Netherlands v Sweden | Netherlands win (52.8%) | 1-1 | 5-1 | ✅ | — |
| Tunisia v Japan | Japan win (63.1%) | 0-2 | 0-4 | ✅ | — |
| Ecuador v Curaçao | Ecuador win (81.9%) | 2-0 | 0-0 | ❌ | — |
| Belgium v Iran | Belgium win (46.7%) | 1-1 | 0-0 | ❌ | — |
| Spain v Saudi Arabia | Spain win (78.3%) | 2-0 | 4-0 | ✅ | — |

**Calibration vs benchmarks** (the 9 graded games with bookmaker prices on file) — log-loss, lower is better. This is the honest test: is the model bad, or were the games hard for everyone?

| Forecaster | Log-loss |
|------------|---------:|
| **This model** | **1.193** |
| Sky Bet (de-vigged) | 1.156 |
| Coin-flip (33/33/33) | 1.099 |

The model is **essentially level with the market** (+0.037 log-loss). Note both the model **and** the bookmaker scored worse than a coin-flip here — with this many draws and upsets, the slate was close to unforecastable for anyone, which is the real reason the hit-rate looks poor.


*Predictions are frozen at the last run before each result arrives, then graded — the scorecard never grades a model that has already seen the answer.*

