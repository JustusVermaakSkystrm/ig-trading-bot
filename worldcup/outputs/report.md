# FIFA World Cup 2026 — ML Prediction Report

*Generated 2026-06-25 · data through **2026-06-24** · 50,000 Monte Carlo simulations · 54/72 group matches played*

Probabilities come from a gradient-boosted Poisson goal model (Elo strength + rolling form + venue/importance features) trained on 30,826 internationals, simulated through the official 2026 bracket and tiebreaker rules.

*Rolling validation (7,966 matches, 2018–2026): RPS 0.1687 vs Elo-baseline 0.1711; log-loss 0.8652 vs 0.8809.*

## Title favourites

| # | Team | Group | Champion | Δ vs 2026-06-24 | Final | Semi-final | Quarter-final | Rd of 16 |
|---|------|:-----:|---------:|-------:|------:|-----------:|--------------:|---------:|
| 1 | Argentina ✅ | J | **23.8%** | +2.1 | 36.4% | 51.1% | 71.2% | 89.2% |
| 2 | Spain ✅ | H | **16.8%** | +2.7 | 27.6% | 40.2% | 53.0% | 75.7% |
| 3 | France ✅ | I | **10.3%** | -0.8 | 19.6% | 35.4% | 53.3% | 78.1% |
| 4 | Mexico ✅ | A | **5.8%** | +1.3 | 13.1% | 28.0% | 57.9% | 82.3% |
| 5 | England ✅ | L | **5.7%** | -1.2 | 10.4% | 21.4% | 32.9% | 73.5% |
| 6 | Colombia ✅ | K | **5.6%** | -0.2 | 11.4% | 20.9% | 45.5% | 76.9% |
| 7 | Portugal ✅ | K | **4.2%** | -1.1 | 9.5% | 18.2% | 33.1% | 67.2% |
| 8 | Brazil ✅ | C | **4.0%** | -0.6 | 7.6% | 18.2% | 31.8% | 54.8% |
| 9 | Morocco ✅ | C | **3.2%** | +1.3 | 8.0% | 17.6% | 37.1% | 53.2% |
| 10 | United States ✅ | D | **3.1%** | – | 8.5% | 19.2% | 51.3% | 80.4% |
| 11 | Switzerland ✅ | B | **2.7%** | -0.1 | 5.8% | 11.5% | 30.5% | 66.6% |
| 12 | Netherlands ✅ | F | **2.7%** | -2.1 | 6.3% | 15.3% | 29.8% | 49.4% |
| 13 | Germany ✅ | E | **2.5%** | +0.5 | 7.1% | 16.4% | 31.5% | 78.4% |
| 14 | Japan ✅ | F | **2.5%** | -0.7 | 6.1% | 14.3% | 27.9% | 46.9% |
| 15 | Norway ✅ | I | **1.9%** | -0.8 | 4.6% | 15.7% | 35.2% | 67.9% |

## Biggest movers since last run (data through 2026-06-24)

| Team | Δ Champion | Δ Rd of 16 | Champion now |
|------|----------:|-----------:|-------------:|
| Spain | +2.7 | +3.3 | 16.8% |
| Argentina | +2.1 | +1.0 | 23.8% |
| Mexico | +1.3 | +1.9 | 5.8% |
| Morocco | +1.3 | +11.3 | 3.2% |
| France | -0.8 | +1.6 | 10.3% |
| Portugal | -1.1 | -3.6 | 4.2% |
| England | -1.2 | -1.6 | 5.7% |
| Netherlands | -2.1 | -9.1 | 2.7% |

*Δ values in probability points. Full run-by-run series in `outputs/history.csv`.*

## Path to the final

The model's single most likely knockout bracket — all 32 projected round-of-32 teams and every unplayed tie, each line carrying the projected winner down to the next round until they converge on the champion. Percentages are each side's chance of advancing from that tie. **A gold-bordered box is a confirmed Round-of-32 tie** (the same pairing in every simulation — mathematically locked): 1/16 locked so far, the rest finalise as the group stage ends on 27 June.

<div style="overflow-x:auto; margin:1rem 0;">
<svg viewBox="0 0 1964 662" width="100%" preserveAspectRatio="xMidYMin meet" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica,Arial,sans-serif"><path d="M82,98 C82,134 142,134 142,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M202,98 C202,134 142,134 142,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M322,98 C322,134 382,134 382,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M442,98 C442,134 382,134 382,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M562,98 C562,134 622,134 622,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M682,98 C682,134 622,134 622,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M802,98 C802,134 862,134 862,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M922,98 C922,134 862,134 862,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1042,98 C1042,134 1102,134 1102,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1162,98 C1162,134 1102,134 1102,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1282,98 C1282,134 1342,134 1342,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1402,98 C1402,134 1342,134 1342,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1522,98 C1522,134 1582,134 1582,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1642,98 C1642,134 1582,134 1582,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1762,98 C1762,134 1822,134 1822,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1882,98 C1882,134 1822,134 1822,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M142,214 C142,250 262,250 262,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M382,214 C382,250 262,250 262,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M622,214 C622,250 742,250 742,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M862,214 C862,250 742,250 742,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1102,214 C1102,250 1222,250 1222,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1342,214 C1342,250 1222,250 1222,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1582,214 C1582,250 1702,250 1702,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1822,214 C1822,250 1702,250 1702,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M262,330 C262,366 502,366 502,402" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M742,330 C742,366 502,366 502,402" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1222,330 C1222,366 1462,366 1462,402" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1702,330 C1702,366 1462,366 1462,402" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M502,446 C502,482 982,482 982,518" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1462,446 C1462,482 982,482 982,518" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M982,562 C982,580 982,580 982,598" fill="none" stroke="#33436b" stroke-width="1.5"/><text x="11" y="76" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 11 76)" text-anchor="middle">ROUND OF 32</text><text x="11" y="192" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 11 192)" text-anchor="middle">ROUND OF 16</text><text x="11" y="308" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 11 308)" text-anchor="middle">QUARTER-FINALS</text><text x="11" y="424" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 11 424)" text-anchor="middle">SEMI-FINALS</text><text x="11" y="540" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 11 540)" text-anchor="middle">FINAL</text><rect x="26" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="26" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="34" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Germany</text><text x="130" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">92%</text><text x="34" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Bosnia</text><text x="130" y="91" font-size="9" text-anchor="end" fill="#5d6880">8%</text><rect x="146" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="146" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="154" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">France</text><text x="250" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">79%</text><text x="154" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Paraguay</text><text x="250" y="91" font-size="9" text-anchor="end" fill="#5d6880">21%</text><rect x="266" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#f5c542" stroke-width="2.5"/><text x="274" y="71" font-size="10.5" font-weight="400" fill="#7c89a3">S. Africa</text><text x="370" y="71" font-size="9" text-anchor="end" fill="#5d6880">33%</text><rect x="266" y="77" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="274" y="91" font-size="10.5" font-weight="700" fill="#7ef0b6">Canada</text><text x="370" y="91" font-size="9" text-anchor="end" fill="#cfe8d8">67%</text><rect x="386" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="394" y="71" font-size="10.5" font-weight="400" fill="#7c89a3">Netherlands</text><text x="490" y="71" font-size="9" text-anchor="end" fill="#5d6880">49%</text><rect x="386" y="77" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="394" y="91" font-size="10.5" font-weight="700" fill="#7ef0b6">Morocco</text><text x="490" y="91" font-size="9" text-anchor="end" fill="#cfe8d8">51%</text><rect x="506" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="506" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="514" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Portugal</text><text x="610" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">63%</text><text x="514" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Croatia</text><text x="610" y="91" font-size="9" text-anchor="end" fill="#5d6880">37%</text><rect x="626" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="626" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="634" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Spain</text><text x="730" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">79%</text><text x="634" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Austria</text><text x="730" y="91" font-size="9" text-anchor="end" fill="#5d6880">21%</text><rect x="746" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="746" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="754" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">USA</text><text x="850" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">68%</text><text x="754" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Senegal</text><text x="850" y="91" font-size="9" text-anchor="end" fill="#5d6880">32%</text><rect x="866" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="874" y="71" font-size="10.5" font-weight="400" fill="#7c89a3">Egypt</text><text x="970" y="71" font-size="9" text-anchor="end" fill="#5d6880">47%</text><rect x="866" y="77" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="874" y="91" font-size="10.5" font-weight="700" fill="#7ef0b6">S. Korea</text><text x="970" y="91" font-size="9" text-anchor="end" fill="#cfe8d8">53%</text><rect x="986" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="986" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="994" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Brazil</text><text x="1090" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">54%</text><text x="994" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Japan</text><text x="1090" y="91" font-size="9" text-anchor="end" fill="#5d6880">46%</text><rect x="1106" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="1114" y="71" font-size="10.5" font-weight="400" fill="#7c89a3">Ivory Coast</text><text x="1210" y="71" font-size="9" text-anchor="end" fill="#5d6880">32%</text><rect x="1106" y="77" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1114" y="91" font-size="10.5" font-weight="700" fill="#7ef0b6">Norway</text><text x="1210" y="91" font-size="9" text-anchor="end" fill="#cfe8d8">68%</text><rect x="1226" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1226" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1234" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Mexico</text><text x="1330" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">88%</text><text x="1234" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Sweden</text><text x="1330" y="91" font-size="9" text-anchor="end" fill="#5d6880">12%</text><rect x="1346" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1346" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1354" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">England</text><text x="1450" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">85%</text><text x="1354" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">DR Congo</text><text x="1450" y="91" font-size="9" text-anchor="end" fill="#5d6880">15%</text><rect x="1466" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1466" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1474" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Argentina</text><text x="1570" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">92%</text><text x="1474" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">C. Verde</text><text x="1570" y="91" font-size="9" text-anchor="end" fill="#5d6880">8%</text><rect x="1586" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="1594" y="71" font-size="10.5" font-weight="400" fill="#7c89a3">Australia</text><text x="1690" y="71" font-size="9" text-anchor="end" fill="#5d6880">48%</text><rect x="1586" y="77" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1594" y="91" font-size="10.5" font-weight="700" fill="#7ef0b6">Belgium</text><text x="1690" y="91" font-size="9" text-anchor="end" fill="#cfe8d8">52%</text><rect x="1706" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1706" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1714" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Switzerland</text><text x="1810" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">63%</text><text x="1714" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Algeria</text><text x="1810" y="91" font-size="9" text-anchor="end" fill="#5d6880">37%</text><rect x="1826" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1826" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1834" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Colombia</text><text x="1930" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">87%</text><text x="1834" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Ghana</text><text x="1930" y="91" font-size="9" text-anchor="end" fill="#5d6880">13%</text><rect x="86" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="94" y="187" font-size="10.5" font-weight="400" fill="#7c89a3">Germany</text><text x="190" y="187" font-size="9" text-anchor="end" fill="#5d6880">33%</text><rect x="86" y="193" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="94" y="207" font-size="10.5" font-weight="700" fill="#7ef0b6">France</text><text x="190" y="207" font-size="9" text-anchor="end" fill="#cfe8d8">67%</text><rect x="326" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="334" y="187" font-size="10.5" font-weight="400" fill="#7c89a3">Canada</text><text x="430" y="187" font-size="9" text-anchor="end" fill="#5d6880">36%</text><rect x="326" y="193" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="334" y="207" font-size="10.5" font-weight="700" fill="#7ef0b6">Morocco</text><text x="430" y="207" font-size="9" text-anchor="end" fill="#cfe8d8">64%</text><rect x="566" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="574" y="187" font-size="10.5" font-weight="400" fill="#7c89a3">Portugal</text><text x="670" y="187" font-size="9" text-anchor="end" fill="#5d6880">34%</text><rect x="566" y="193" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="574" y="207" font-size="10.5" font-weight="700" fill="#7ef0b6">Spain</text><text x="670" y="207" font-size="9" text-anchor="end" fill="#cfe8d8">66%</text><rect x="806" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="806" y="172" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="814" y="187" font-size="10.5" font-weight="700" fill="#7ef0b6">USA</text><text x="910" y="187" font-size="9" text-anchor="end" fill="#cfe8d8">65%</text><text x="814" y="207" font-size="10.5" font-weight="400" fill="#7c89a3">S. Korea</text><text x="910" y="207" font-size="9" text-anchor="end" fill="#5d6880">35%</text><rect x="1046" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1046" y="172" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1054" y="187" font-size="10.5" font-weight="700" fill="#7ef0b6">Brazil</text><text x="1150" y="187" font-size="9" text-anchor="end" fill="#cfe8d8">52%</text><text x="1054" y="207" font-size="10.5" font-weight="400" fill="#7c89a3">Norway</text><text x="1150" y="207" font-size="9" text-anchor="end" fill="#5d6880">48%</text><rect x="1286" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1286" y="172" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1294" y="187" font-size="10.5" font-weight="700" fill="#7ef0b6">Mexico</text><text x="1390" y="187" font-size="9" text-anchor="end" fill="#cfe8d8">62%</text><text x="1294" y="207" font-size="10.5" font-weight="400" fill="#7c89a3">England</text><text x="1390" y="207" font-size="9" text-anchor="end" fill="#5d6880">38%</text><rect x="1526" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1526" y="172" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1534" y="187" font-size="10.5" font-weight="700" fill="#7ef0b6">Argentina</text><text x="1630" y="187" font-size="9" text-anchor="end" fill="#cfe8d8">73%</text><text x="1534" y="207" font-size="10.5" font-weight="400" fill="#7c89a3">Belgium</text><text x="1630" y="207" font-size="9" text-anchor="end" fill="#5d6880">27%</text><rect x="1766" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="1774" y="187" font-size="10.5" font-weight="400" fill="#7c89a3">Switzerland</text><text x="1870" y="187" font-size="9" text-anchor="end" fill="#5d6880">38%</text><rect x="1766" y="193" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1774" y="207" font-size="10.5" font-weight="700" fill="#7ef0b6">Colombia</text><text x="1870" y="207" font-size="9" text-anchor="end" fill="#cfe8d8">62%</text><rect x="206" y="286" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="206" y="288" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="214" y="303" font-size="10.5" font-weight="700" fill="#7ef0b6">France</text><text x="310" y="303" font-size="9" text-anchor="end" fill="#cfe8d8">64%</text><text x="214" y="323" font-size="10.5" font-weight="400" fill="#7c89a3">Morocco</text><text x="310" y="323" font-size="9" text-anchor="end" fill="#5d6880">36%</text><rect x="686" y="286" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="686" y="288" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="694" y="303" font-size="10.5" font-weight="700" fill="#7ef0b6">Spain</text><text x="790" y="303" font-size="9" text-anchor="end" fill="#cfe8d8">70%</text><text x="694" y="323" font-size="10.5" font-weight="400" fill="#7c89a3">USA</text><text x="790" y="323" font-size="9" text-anchor="end" fill="#5d6880">30%</text><rect x="1166" y="286" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="1174" y="303" font-size="10.5" font-weight="400" fill="#7c89a3">Brazil</text><text x="1270" y="303" font-size="9" text-anchor="end" fill="#5d6880">59%</text><rect x="1166" y="309" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1174" y="323" font-size="10.5" font-weight="700" fill="#7ef0b6">Mexico</text><text x="1270" y="323" font-size="9" text-anchor="end" fill="#cfe8d8">41%†</text><rect x="1646" y="286" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1646" y="288" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1654" y="303" font-size="10.5" font-weight="700" fill="#7ef0b6">Argentina</text><text x="1750" y="303" font-size="9" text-anchor="end" fill="#cfe8d8">69%</text><text x="1654" y="323" font-size="10.5" font-weight="400" fill="#7c89a3">Colombia</text><text x="1750" y="323" font-size="9" text-anchor="end" fill="#5d6880">31%</text><rect x="446" y="402" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="454" y="419" font-size="10.5" font-weight="400" fill="#7c89a3">France</text><text x="550" y="419" font-size="9" text-anchor="end" fill="#5d6880">40%</text><rect x="446" y="425" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="454" y="439" font-size="10.5" font-weight="700" fill="#7ef0b6">Spain</text><text x="550" y="439" font-size="9" text-anchor="end" fill="#cfe8d8">60%</text><rect x="1406" y="402" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="1414" y="419" font-size="10.5" font-weight="400" fill="#7c89a3">Mexico</text><text x="1510" y="419" font-size="9" text-anchor="end" fill="#5d6880">36%</text><rect x="1406" y="425" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1414" y="439" font-size="10.5" font-weight="700" fill="#7ef0b6">Argentina</text><text x="1510" y="439" font-size="9" text-anchor="end" fill="#cfe8d8">64%</text><rect x="926" y="518" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="934" y="535" font-size="10.5" font-weight="400" fill="#7c89a3">Spain</text><text x="1030" y="535" font-size="9" text-anchor="end" fill="#5d6880">53%</text><rect x="926" y="541" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="934" y="555" font-size="10.5" font-weight="700" fill="#7ef0b6">Argentina</text><text x="1030" y="555" font-size="9" text-anchor="end" fill="#cfe8d8">47%†</text><rect x="888" y="598" width="188" height="46" rx="10" fill="#f5c542"/><text x="982" y="619" font-size="13" font-weight="800" fill="#1a1300" text-anchor="middle">🏆 Argentina</text><text x="982" y="635" font-size="10" fill="#5a4a00" text-anchor="middle">projected champion · 24% to win</text></svg>
</div>

## Upcoming group matches — outcome probabilities

*(next match days; full list for all 72 group games in `match_probabilities.csv`)*

| Date | Grp | Match | Home win | Draw | Away win | xG | Likely score |
|------|:---:|-------|---------:|-----:|---------:|----|:----:|
| 2026-06-25 | D | United States v Turkey | **50.2%** | 25.5% | 24.3% | 1.67–1.09 | 1-1 |
| 2026-06-25 | D | Paraguay v Australia | **37.3%** | 29.0% | 33.7% | 1.24–1.17 | 1-1 |
| 2026-06-25 | E | Curaçao v Ivory Coast | 16.8% | 25.6% | **57.6%** | 0.78–1.65 | 0-1 |
| 2026-06-25 | E | Ecuador v Germany | 29.5% | 29.6% | **40.9%** | 1.03–1.26 | 1-1 |
| 2026-06-25 | F | Japan v Sweden | **68.1%** | 18.7% | 13.2% | 2.36–0.96 | 2-0 |
| 2026-06-25 | F | Tunisia v Netherlands | 11.7% | 22.2% | **66.2%** | 0.65–1.88 | 0-1 |
| 2026-06-26 | I | Senegal v Iraq | **62.4%** | 22.9% | 14.6% | 1.87–0.79 | 1-0 |
| 2026-06-26 | I | Norway v France | 15.5% | 20.8% | **63.7%** | 0.96–2.14 | 0-2 |
| 2026-06-26 | H | Uruguay v Spain | 11.6% | 20.9% | **67.6%** | 0.71–2.02 | 0-2 |
| 2026-06-26 | G | New Zealand v Belgium | 19.2% | 25.2% | **55.6%** | 0.90–1.70 | 0-1 |
| 2026-06-26 | G | Egypt v Iran | 33.3% | 29.5% | **37.2%** | 1.13–1.21 | 1-1 |
| 2026-06-26 | H | Cape Verde v Saudi Arabia | 33.8% | 30.2% | **36.0%** | 1.10–1.15 | 1-1 |
| 2026-06-27 | L | Panama v England | 11.7% | 20.2% | **68.1%** | 0.75–2.09 | 0-2 |
| 2026-06-27 | J | Algeria v Austria | 31.5% | 28.1% | **40.4%** | 1.17–1.35 | 1-1 |
| 2026-06-27 | J | Jordan v Argentina | 3.6% | 12.1% | **84.3%** | 0.41–2.63 | 0-2 |
| 2026-06-27 | K | Colombia v Portugal | **42.2%** | 28.7% | 29.1% | 1.34–1.07 | 1-1 |
| 2026-06-27 | K | DR Congo v Uzbekistan | **37.7%** | 30.7% | 31.6% | 1.15–1.03 | 1-1 |
| 2026-06-27 | L | Croatia v Ghana | **60.9%** | 24.4% | 14.7% | 1.74–0.73 | 1-0 |

## Group projections

### Group A

**✅ Into the knockouts:** Mexico, South Africa

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Mexico ✅ | 3 | 3-0-0 | 6-0 | **9** | 9.00 | 100.0% | 100.0% | 100.0% |
| South Africa ✅ | 3 | 1-1-1 | 2-3 | **4** | 4.00 | 0.0% | 100.0% | 100.0% |
| South Korea | 3 | 1-0-2 | 2-3 | **3** | 3.00 | 0.0% | 0.0% | 92.4% |
| Czech Republic | 3 | 0-1-2 | 2-6 | **1** | 1.00 | 0.0% | 0.0% | 0.0% |

### Group B

**✅ Into the knockouts:** Canada, Switzerland, Bosnia and Herzegovina

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Switzerland ✅ | 3 | 2-1-0 | 8-3 | **7** | 7.00 | 100.0% | 100.0% | 100.0% |
| Canada ✅ | 3 | 1-1-1 | 8-4 | **4** | 4.00 | 0.0% | 100.0% | 100.0% |
| Bosnia and Herzegovina ✅ | 3 | 1-1-1 | 5-6 | **4** | 4.00 | 0.0% | 0.0% | 100.0% |
| Qatar | 3 | 0-1-2 | 2-10 | **1** | 1.00 | 0.0% | 0.0% | 0.0% |

### Group C

**✅ Into the knockouts:** Brazil, Morocco

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Brazil ✅ | 3 | 2-1-0 | 7-1 | **7** | 7.00 | 100.0% | 100.0% | 100.0% |
| Morocco ✅ | 3 | 2-1-0 | 6-3 | **7** | 7.00 | 0.0% | 100.0% | 100.0% |
| Scotland | 3 | 1-0-2 | 1-4 | **3** | 3.00 | 0.0% | 0.0% | 35.4% |
| Haiti | 3 | 0-0-3 | 2-8 | **0** | 0.00 | 0.0% | 0.0% | 0.0% |

### Group D

**✅ Into the knockouts:** United States

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| United States ✅ | 2 | 2-0-0 | 6-1 | **6** | 7.76 | 100.0% | 100.0% | 100.0% |
| Australia | 2 | 1-0-1 | 2-2 | **3** | 4.30 | 0.0% | 62.6% | 94.4% |
| Paraguay | 2 | 1-0-1 | 2-4 | **3** | 4.41 | 0.0% | 37.4% | 82.5% |
| Turkey | 2 | 0-0-2 | 0-3 | **0** | 0.98 | 0.0% | 0.0% | 0.0% |

### Group E

**✅ Into the knockouts:** Germany

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Germany ✅ | 2 | 2-0-0 | 9-2 | **6** | 7.51 | 100.0% | 100.0% | 100.0% |
| Ivory Coast | 2 | 1-0-1 | 2-2 | **3** | 4.99 | 0.0% | 83.4% | 93.5% |
| Ecuador | 2 | 0-1-1 | 0-1 | **1** | 2.19 | 0.0% | 5.0% | 29.7% |
| Curaçao | 2 | 0-1-1 | 1-7 | **1** | 1.76 | 0.0% | 11.6% | 16.6% |

### Group F

**✅ Into the knockouts:** Netherlands, Japan

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Netherlands ✅ | 2 | 1-1-0 | 7-3 | **4** | 6.21 | 49.7% | 99.6% | 100.0% |
| Japan ✅ | 2 | 1-1-0 | 6-2 | **4** | 6.23 | 45.8% | 87.1% | 100.0% |
| Sweden | 2 | 1-0-1 | 6-6 | **3** | 3.59 | 4.5% | 13.3% | 85.3% |
| Tunisia | 2 | 0-0-2 | 1-9 | **0** | 0.57 | 0.0% | 0.0% | 0.0% |

### Group G

**✅ Into the knockouts:** Egypt

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Egypt ✅ | 2 | 1-1-0 | 4-2 | **4** | 5.30 | 58.4% | 79.6% | 100.0% |
| Iran | 2 | 0-2-0 | 2-2 | **2** | 3.40 | 26.6% | 41.7% | 66.8% |
| Belgium | 2 | 0-2-0 | 1-1 | **2** | 3.92 | 15.1% | 66.6% | 80.9% |
| New Zealand | 2 | 0-1-1 | 3-5 | **1** | 1.83 | 0.0% | 12.0% | 19.1% |

### Group H

**✅ Into the knockouts:** Spain

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Spain ✅ | 2 | 1-1-0 | 4-0 | **4** | 6.23 | 88.1% | 96.0% | 100.0% |
| Uruguay | 2 | 0-2-0 | 3-3 | **2** | 2.56 | 10.3% | 17.6% | 32.8% |
| Cape Verde | 2 | 0-2-0 | 2-2 | **2** | 3.32 | 1.6% | 54.6% | 64.0% |
| Saudi Arabia | 2 | 0-1-1 | 1-5 | **1** | 2.38 | 0.0% | 31.7% | 36.0% |

### Group I

**✅ Into the knockouts:** France, Norway

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| France ✅ | 2 | 2-0-0 | 6-1 | **6** | 8.12 | 84.6% | 100.0% | 100.0% |
| Norway ✅ | 2 | 2-0-0 | 7-3 | **6** | 6.67 | 15.4% | 100.0% | 100.0% |
| Senegal | 2 | 0-0-2 | 3-6 | **0** | 2.10 | 0.0% | 0.0% | 57.3% |
| Iraq | 2 | 0-0-2 | 1-7 | **0** | 0.68 | 0.0% | 0.0% | 2.3% |

### Group J

**✅ Into the knockouts:** Argentina

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Argentina ✅ | 2 | 2-0-0 | 5-0 | **6** | 8.65 | 100.0% | 100.0% | 100.0% |
| Austria | 2 | 1-0-1 | 3-3 | **3** | 4.49 | 0.0% | 68.3% | 95.9% |
| Algeria | 2 | 1-0-1 | 2-4 | **3** | 4.23 | 0.0% | 31.7% | 77.3% |
| Jordan | 2 | 0-0-2 | 2-5 | **0** | 0.23 | 0.0% | 0.0% | 0.0% |

### Group K

**✅ Into the knockouts:** Portugal, Colombia

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Colombia ✅ | 2 | 2-0-0 | 4-1 | **6** | 7.56 | 71.1% | 100.0% | 100.0% |
| Portugal ✅ | 2 | 1-1-0 | 6-1 | **4** | 5.16 | 28.9% | 99.7% | 100.0% |
| DR Congo | 2 | 0-1-1 | 1-2 | **1** | 2.44 | 0.0% | 0.3% | 38.2% |
| Uzbekistan | 2 | 0-0-2 | 1-8 | **0** | 1.25 | 0.0% | 0.0% | 2.3% |

### Group L

**✅ Into the knockouts:** England, Ghana

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| England ✅ | 2 | 1-1-0 | 4-2 | **4** | 6.23 | 72.4% | 99.8% | 100.0% |
| Ghana ✅ | 2 | 1-1-0 | 1-0 | **4** | 4.68 | 7.7% | 39.3% | 100.0% |
| Croatia | 2 | 1-0-1 | 3-4 | **3** | 5.07 | 19.9% | 60.9% | 97.2% |
| Panama | 2 | 0-0-2 | 0-2 | **0** | 0.56 | 0.0% | 0.0% | 0.0% |

*\*Advance = top two or one of the eight best third-placed teams.*

*✅ = already reached the knockout stage — locked into the Round of 32 in every simulation. (Reaching later rounds still requires winning knockout games, so those stay below 100%.)*

## Most likely knockout bracket

Each tie shows the projected pairing and the side that advances — the team **more likely to win the tournament** of the two, so the bracket crowns the overall favourite. 'Win prob' is that team's chance in that single match (a **†** flags a near-even tie where the title favourite is a slight underdog in the one-off game). **🔒 marks a confirmed tie** — the same two teams in every simulation, mathematically locked. (1/16 Round-of-32 ties locked so far; the rest finalise as the group stage completes on 27 June.)

### Round of 32

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 73 | 2026-06-28 | SoFi Stadium, Los Angeles | 🔒 South Africa v Canada | **Canada** | 67.1% | 🔒 locked |
| 74 | 2026-06-29 | Gillette Stadium, Boston | Germany v Bosnia and Herzegovina | **Germany** | 92.1% | 53.9% |
| 75 | 2026-06-29 | Estadio BBVA, Monterrey | Netherlands v Morocco | **Morocco** | 50.8% | 49.7% |
| 76 | 2026-06-29 | NRG Stadium, Houston | Brazil v Japan | **Brazil** | 54.1% | 41.3% |
| 77 | 2026-06-30 | MetLife Stadium, New York/New Jersey | France v Paraguay | **France** | 79.3% | 29.4% |
| 78 | 2026-06-30 | AT&T Stadium, Dallas | Ivory Coast v Norway | **Norway** | 67.7% | 70.6% |
| 79 | 2026-06-30 | Estadio Azteca, Mexico City | Mexico v Sweden | **Mexico** | 88.4% | 9.6% |
| 80 | 2026-07-01 | Mercedes-Benz Stadium, Atlanta | England v DR Congo | **England** | 85.0% | 27.4% |
| 81 | 2026-07-01 | Levi's Stadium, San Francisco Bay Area | United States v Senegal | **United States** | 68.1% | 9.4% |
| 82 | 2026-07-01 | Lumen Field, Seattle | Egypt v South Korea | **South Korea** | 53.5% | 55.1% |
| 83 | 2026-07-02 | BMO Field, Toronto | Portugal v Croatia | **Portugal** | 63.2% | 29.1% |
| 84 | 2026-07-02 | SoFi Stadium, Los Angeles | Spain v Austria | **Spain** | 79.4% | 60.3% |
| 85 | 2026-07-02 | BC Place, Vancouver | Switzerland v Algeria | **Switzerland** | 62.7% | 13.2% |
| 86 | 2026-07-03 | Hard Rock Stadium, Miami | Argentina v Cape Verde | **Argentina** | 92.0% | 53.1% |
| 87 | 2026-07-03 | Arrowhead Stadium, Kansas City | Colombia v Ghana | **Colombia** | 86.5% | 43.3% |
| 88 | 2026-07-03 | AT&T Stadium, Dallas | Australia v Belgium | **Belgium** | 51.8% | 32.3% |

### Round of 16

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 89 | 2026-07-04 | Lincoln Financial Field, Philadelphia | Germany v France | **France** | 66.9% | 51.4% |
| 90 | 2026-07-04 | NRG Stadium, Houston | Canada v Morocco | **Morocco** | 63.7% | 35.7% |
| 91 | 2026-07-05 | MetLife Stadium, New York/New Jersey | Brazil v Norway | **Brazil** | 51.8% | 32.0% |
| 92 | 2026-07-05 | Estadio Azteca, Mexico City | Mexico v England | **Mexico** | 61.5% | 47.0% |
| 93 | 2026-07-06 | AT&T Stadium, Dallas | Portugal v Spain | **Spain** | 66.3% | 31.4% |
| 94 | 2026-07-06 | Lumen Field, Seattle | United States v South Korea | **United States** | 65.1% | 37.1% |
| 95 | 2026-07-07 | Mercedes-Benz Stadium, Atlanta | Argentina v Belgium | **Argentina** | 73.4% | 23.9% |
| 96 | 2026-07-07 | BC Place, Vancouver | Switzerland v Colombia | **Colombia** | 61.9% | 38.1% |

### Quarter-finals

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 97 | 2026-07-09 | Gillette Stadium, Boston | France v Morocco | **France** | 64.5% | 16.7% |
| 98 | 2026-07-10 | SoFi Stadium, Los Angeles | Spain v United States | **Spain** | 69.6% | 24.9% |
| 99 | 2026-07-11 | Hard Rock Stadium, Miami | Brazil v Mexico | **Mexico** | 41.1%† | 18.5% |
| 100 | 2026-07-11 | Arrowhead Stadium, Kansas City | Argentina v Colombia | **Argentina** | 69.0% | 26.1% |

### Semi-finals

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 101 | 2026-07-14 | AT&T Stadium, Dallas | France v Spain | **Spain** | 60.0% | 11.6% |
| 102 | 2026-07-15 | Mercedes-Benz Stadium, Atlanta | Mexico v Argentina | **Argentina** | 63.7% | 14.3% |

### Final

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 104 | 2026-07-19 | MetLife Stadium, East Rutherford | Spain v Argentina | **Argentina** | 46.9%† | 9.9% |

**Projected champion: Argentina** (overall title probability 23.8%). The bracket advances the team more likely to go all the way in each tie, so the champion here matches the title favourite at the top of the page.

*† The title favourite reaches this tie via an easier path, so it wins the tournament most often even though this specific one-off match is a near coin-flip the other side shades.*

## How to read this

- All figures are probabilities, not certainties — a 65% favourite loses about one such match in three.
- `xPts` = expected group points; `xG` = expected goals from the Poisson model.
- Predictions refresh after every match day: run `python -m worldcup.run all` to pull new results, re-rate teams, and re-simulate.
- Machine-readable outputs: `match_probabilities.csv`, `tournament_projections.csv`. Past reports in `outputs/archive/`.

## Model scorecard

**33 of 54 match outcomes called correctly** (the model's own probabilities expected ≈31.7 of 54) · exact scoreline predicted 3/54 · average probability placed on what actually happened: **45.4%** (33.3% = guessing).

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
| Sweden v Tunisia | Sweden win (42.5%) | 1-1 | 5-1 | ✅ | — |
| Netherlands v Japan | Netherlands win (36.1%) | 1-1 | 2-2 | ❌ | — |
| Germany v Curaçao | Germany win (84.5%) | 2-0 | 7-1 | ✅ | — |
| Ivory Coast v Ecuador | Ecuador win (48.2%) | 1-1 | 1-0 | ❌ | — |
| Saudi Arabia v Uruguay | Uruguay win (62.1%) | 0-1 | 1-1 | ❌ | — |
| Spain v Cape Verde | Spain win (90.5%) | 3-0 | 0-0 | ❌ | — |
| Belgium v Egypt | Belgium win (56.6%) | 1-1 | 1-1 | ❌ | ✅ |
| Iran v New Zealand | Iran win (54.6%) | 1-0 | 2-2 | ❌ | — |
| Austria v Jordan | Austria win (47.0%) | 1-1 | 3-1 | ✅ | — |
| Argentina v Algeria | Argentina win (68.0%) | 2-0 | 3-0 | ✅ | — |
| France v Senegal | France win (59.1%) | 1-0 | 3-1 | ✅ | — |
| Iraq v Norway | Norway win (59.1%) | 0-1 | 1-4 | ✅ | — |
| Ghana v Panama | Panama win (51.9%) | 1-1 | 1-0 | ❌ | — |
| Portugal v DR Congo | Portugal win (70.6%) | 2-0 | 1-1 | ❌ | — |
| Uzbekistan v Colombia | Colombia win (53.9%) | 0-1 | 1-3 | ✅ | — |
| England v Croatia | England win (56.9%) | 1-0 | 4-2 | ✅ | — |
| Canada v Qatar | Canada win (74.0%) | 2-0 | 6-0 | ✅ | — |
| Switzerland v Bosnia and Herzegovina | Switzerland win (66.8%) | 2-0 | 4-1 | ✅ | — |
| Czech Republic v South Africa | Czech Republic win (55.5%) | 1-0 | 1-1 | ❌ | — |
| Mexico v South Korea | Mexico win (51.1%) | 1-1 | 1-0 | ✅ | — |
| Turkey v Paraguay | Paraguay win (38.4%) | 1-1 | 0-1 | ✅ | — |
| Scotland v Morocco | Morocco win (49.3%) | 1-1 | 0-1 | ✅ | — |
| Brazil v Haiti | Brazil win (81.3%) | 2-0 | 3-0 | ✅ | — |
| United States v Australia | Australia win (35.9%) | 1-1 | 2-0 | ❌ | — |
| Netherlands v Sweden | Netherlands win (52.8%) | 1-1 | 5-1 | ✅ | — |
| Tunisia v Japan | Japan win (63.1%) | 0-2 | 0-4 | ✅ | — |
| Germany v Ivory Coast | Germany win (50.9%) | 1-1 | 2-1 | ✅ | — |
| Ecuador v Curaçao | Ecuador win (81.9%) | 2-0 | 0-0 | ❌ | — |
| Uruguay v Cape Verde | Uruguay win (72.7%) | 2-0 | 2-2 | ❌ | — |
| Spain v Saudi Arabia | Spain win (78.3%) | 2-0 | 4-0 | ✅ | — |
| New Zealand v Egypt | Egypt win (38.7%) | 1-1 | 1-3 | ✅ | — |
| Belgium v Iran | Belgium win (46.7%) | 1-1 | 0-0 | ❌ | — |
| France v Iraq | France win (76.5%) | 2-0 | 3-0 | ✅ | — |
| Norway v Senegal | Norway win (47.5%) | 1-1 | 3-2 | ✅ | — |
| Argentina v Austria | Argentina win (66.2%) | 2-0 | 2-0 | ✅ | ✅ |
| Jordan v Algeria | Algeria win (52.0%) | 1-1 | 1-2 | ✅ | — |
| Portugal v Uzbekistan | Portugal win (63.7%) | 1-0 | 5-0 | ✅ | — |
| Colombia v DR Congo | Colombia win (65.4%) | 2-0 | 1-0 | ✅ | — |
| England v Ghana | England win (75.8%) | 2-0 | 0-0 | ❌ | — |
| Panama v Croatia | Croatia win (42.4%) | 1-1 | 0-1 | ✅ | — |
| South Africa v South Korea | South Korea win (56.4%) | 0-1 | 1-0 | ❌ | — |
| Scotland v Brazil | Brazil win (58.8%) | 0-1 | 0-3 | ✅ | — |
| Mexico v Czech Republic | Mexico win (78.6%) | 2-0 | 3-0 | ✅ | — |
| Morocco v Haiti | Morocco win (72.8%) | 2-0 | 4-2 | ✅ | — |
| Bosnia and Herzegovina v Qatar | Bosnia and Herzegovina win (47.3%) | 1-1 | 3-1 | ✅ | — |
| Canada v Switzerland | Canada win (37.9%) | 1-1 | 1-2 | ❌ | — |

**Calibration vs benchmarks** (the 9 graded games with bookmaker prices on file) — log-loss, lower is better. This is the honest test: is the model bad, or were the games hard for everyone?

| Forecaster | Log-loss |
|------------|---------:|
| **This model** | **1.193** |
| Sky Bet (de-vigged) | 1.156 |
| Coin-flip (33/33/33) | 1.099 |

The model is **essentially level with the market** (+0.037 log-loss). Note both the model **and** the bookmaker scored worse than a coin-flip here — with this many draws and upsets, the slate was close to unforecastable for anyone, which is the real reason the hit-rate looks poor.


*Predictions are frozen at the last run before each result arrives, then graded — the scorecard never grades a model that has already seen the answer.*

