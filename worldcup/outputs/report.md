# FIFA World Cup 2026 — ML Prediction Report

*Generated 2026-06-26 · data through **2026-06-25** · 50,000 Monte Carlo simulations · 58/72 group matches played*

Probabilities come from a gradient-boosted Poisson goal model (Elo strength + rolling form + venue/importance features) trained on 30,830 internationals, simulated through the official 2026 bracket and tiebreaker rules.

*Rolling validation (7,966 matches, 2018–2026): RPS 0.1687 vs Elo-baseline 0.1711; log-loss 0.8652 vs 0.8809.*

## Title favourites

| # | Team | Group | Champion | Δ vs 2026-06-25 | Final | Semi-final | Quarter-final | Rd of 16 |
|---|------|:-----:|---------:|-------:|------:|-----------:|--------------:|---------:|
| 1 | Argentina ✅ | J | **20.7%** | -4.3 | 32.5% | 46.3% | 68.7% | 87.9% |
| 2 | Spain ✅ | H | **16.1%** | -0.1 | 26.0% | 38.1% | 50.6% | 74.1% |
| 3 | France ✅ | I | **11.0%** | – | 20.9% | 37.4% | 58.5% | 77.2% |
| 4 | Colombia ✅ | K | **7.3%** | +0.8 | 14.2% | 24.8% | 48.9% | 78.1% |
| 5 | England ✅ | L | **6.0%** | -0.5 | 11.5% | 22.7% | 36.5% | 70.4% |
| 6 | Portugal ✅ | K | **5.0%** | +0.1 | 11.0% | 20.8% | 36.9% | 71.4% |
| 7 | Brazil ✅ | C | **4.8%** | +0.5 | 8.6% | 19.6% | 33.7% | 57.6% |
| 8 | Netherlands ✅ | F | **3.9%** | +1.0 | 9.8% | 20.5% | 36.8% | 50.8% |
| 9 | Mexico ✅ | A | **3.8%** | +0.3 | 8.2% | 20.6% | 43.4% | 67.1% |
| 10 | United States ✅ | D | **3.5%** | +0.8 | 9.3% | 21.3% | 56.3% | 88.9% |
| 11 | Morocco ✅ | C | **3.2%** | +0.6 | 7.5% | 17.0% | 34.6% | 49.2% |
| 12 | Norway ✅ | I | **2.6%** | +0.6 | 5.8% | 16.7% | 35.0% | 67.7% |
| 13 | Switzerland ✅ | B | **2.5%** | -0.7 | 5.5% | 10.7% | 26.0% | 62.0% |
| 14 | Japan ✅ | F | **2.0%** | -1.0 | 4.5% | 11.3% | 21.6% | 42.4% |
| 15 | Germany ✅ | E | **1.4%** | +0.6 | 4.4% | 11.1% | 23.3% | 70.7% |

## Biggest movers since last run (data through 2026-06-25)

| Team | Δ Champion | Δ Rd of 16 | Champion now |
|------|----------:|-----------:|-------------:|
| Netherlands | +1.0 | -1.9 | 3.9% |
| Colombia | +0.8 | +0.5 | 7.3% |
| United States | +0.8 | +8.7 | 3.5% |
| Germany | +0.6 | +0.5 | 1.4% |
| Morocco | +0.6 | +0.4 | 3.2% |
| Switzerland | -0.7 | -5.0 | 2.5% |
| Japan | -1.0 | -10.0 | 2.0% |
| Argentina | -4.3 | -1.5 | 20.7% |

*Δ values in probability points. Full run-by-run series in `outputs/history.csv`.*

## Path to the final

The model's single most likely knockout bracket — all 32 projected round-of-32 teams and every unplayed tie, each line carrying the projected winner down to the next round until they converge on the champion. Percentages are each side's chance of advancing from that tie. **A gold-bordered box is a confirmed Round-of-32 tie** (the same pairing in every simulation — mathematically locked): 3/16 locked so far, the rest finalise as the group stage ends on 27 June.

<div style="overflow-x:auto; margin:1rem 0;">
<svg viewBox="0 0 1964 662" width="100%" preserveAspectRatio="xMidYMin meet" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica,Arial,sans-serif"><path d="M82,98 C82,134 142,134 142,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M202,98 C202,134 142,134 142,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M322,98 C322,134 382,134 382,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M442,98 C442,134 382,134 382,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M562,98 C562,134 622,134 622,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M682,98 C682,134 622,134 622,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M802,98 C802,134 862,134 862,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M922,98 C922,134 862,134 862,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1042,98 C1042,134 1102,134 1102,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1162,98 C1162,134 1102,134 1102,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1282,98 C1282,134 1342,134 1342,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1402,98 C1402,134 1342,134 1342,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1522,98 C1522,134 1582,134 1582,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1642,98 C1642,134 1582,134 1582,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1762,98 C1762,134 1822,134 1822,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1882,98 C1882,134 1822,134 1822,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M142,214 C142,250 262,250 262,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M382,214 C382,250 262,250 262,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M622,214 C622,250 742,250 742,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M862,214 C862,250 742,250 742,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1102,214 C1102,250 1222,250 1222,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1342,214 C1342,250 1222,250 1222,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1582,214 C1582,250 1702,250 1702,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1822,214 C1822,250 1702,250 1702,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M262,330 C262,366 502,366 502,402" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M742,330 C742,366 502,366 502,402" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1222,330 C1222,366 1462,366 1462,402" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1702,330 C1702,366 1462,366 1462,402" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M502,446 C502,482 982,482 982,518" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1462,446 C1462,482 982,482 982,518" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M982,562 C982,580 982,580 982,598" fill="none" stroke="#33436b" stroke-width="1.5"/><text x="11" y="76" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 11 76)" text-anchor="middle">ROUND OF 32</text><text x="11" y="192" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 11 192)" text-anchor="middle">ROUND OF 16</text><text x="11" y="308" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 11 308)" text-anchor="middle">QUARTER-FINALS</text><text x="11" y="424" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 11 424)" text-anchor="middle">SEMI-FINALS</text><text x="11" y="540" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 11 540)" text-anchor="middle">FINAL</text><rect x="26" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="26" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="34" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Germany</text><text x="130" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">92%</text><text x="34" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Bosnia</text><text x="130" y="91" font-size="9" text-anchor="end" fill="#5d6880">8%</text><rect x="146" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="146" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="154" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">France</text><text x="250" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">81%</text><text x="154" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Sweden</text><text x="250" y="91" font-size="9" text-anchor="end" fill="#5d6880">19%</text><rect x="266" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#f5c542" stroke-width="2.5"/><text x="274" y="71" font-size="10.5" font-weight="400" fill="#7c89a3">S. Africa</text><text x="370" y="71" font-size="9" text-anchor="end" fill="#5d6880">36%</text><rect x="266" y="77" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="274" y="91" font-size="10.5" font-weight="700" fill="#7ef0b6">Canada</text><text x="370" y="91" font-size="9" text-anchor="end" fill="#cfe8d8">64%</text><rect x="386" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#f5c542" stroke-width="2.5"/><rect x="386" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="394" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Netherlands</text><text x="490" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">51%</text><text x="394" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Morocco</text><text x="490" y="91" font-size="9" text-anchor="end" fill="#5d6880">49%</text><rect x="506" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="506" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="514" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Portugal</text><text x="610" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">75%</text><text x="514" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Croatia</text><text x="610" y="91" font-size="9" text-anchor="end" fill="#5d6880">25%</text><rect x="626" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="626" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="634" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Spain</text><text x="730" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">77%</text><text x="634" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Austria</text><text x="730" y="91" font-size="9" text-anchor="end" fill="#5d6880">23%</text><rect x="746" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="746" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="754" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">USA</text><text x="850" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">72%</text><text x="754" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Senegal</text><text x="850" y="91" font-size="9" text-anchor="end" fill="#5d6880">28%</text><rect x="866" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="866" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="874" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Egypt</text><text x="970" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">48%†</text><text x="874" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">S. Korea</text><text x="970" y="91" font-size="9" text-anchor="end" fill="#5d6880">52%</text><rect x="986" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#f5c542" stroke-width="2.5"/><rect x="986" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="994" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Brazil</text><text x="1090" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">58%</text><text x="994" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Japan</text><text x="1090" y="91" font-size="9" text-anchor="end" fill="#5d6880">42%</text><rect x="1106" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="1114" y="71" font-size="10.5" font-weight="400" fill="#7c89a3">Ivory Coast</text><text x="1210" y="71" font-size="9" text-anchor="end" fill="#5d6880">32%</text><rect x="1106" y="77" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1114" y="91" font-size="10.5" font-weight="700" fill="#7ef0b6">Norway</text><text x="1210" y="91" font-size="9" text-anchor="end" fill="#cfe8d8">68%</text><rect x="1226" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1226" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1234" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Mexico</text><text x="1330" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">64%</text><text x="1234" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Ecuador</text><text x="1330" y="91" font-size="9" text-anchor="end" fill="#5d6880">36%</text><rect x="1346" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1346" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1354" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">England</text><text x="1450" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">86%</text><text x="1354" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">DR Congo</text><text x="1450" y="91" font-size="9" text-anchor="end" fill="#5d6880">14%</text><rect x="1466" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1466" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1474" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Argentina</text><text x="1570" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">93%</text><text x="1474" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">C. Verde</text><text x="1570" y="91" font-size="9" text-anchor="end" fill="#5d6880">7%</text><rect x="1586" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="1594" y="71" font-size="10.5" font-weight="400" fill="#7c89a3">Australia</text><text x="1690" y="71" font-size="9" text-anchor="end" fill="#5d6880">47%</text><rect x="1586" y="77" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1594" y="91" font-size="10.5" font-weight="700" fill="#7ef0b6">Belgium</text><text x="1690" y="91" font-size="9" text-anchor="end" fill="#cfe8d8">53%</text><rect x="1706" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1706" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1714" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Switzerland</text><text x="1810" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">61%</text><text x="1714" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Algeria</text><text x="1810" y="91" font-size="9" text-anchor="end" fill="#5d6880">39%</text><rect x="1826" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1826" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1834" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Colombia</text><text x="1930" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">87%</text><text x="1834" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Ghana</text><text x="1930" y="91" font-size="9" text-anchor="end" fill="#5d6880">13%</text><rect x="86" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="94" y="187" font-size="10.5" font-weight="400" fill="#7c89a3">Germany</text><text x="190" y="187" font-size="9" text-anchor="end" fill="#5d6880">23%</text><rect x="86" y="193" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="94" y="207" font-size="10.5" font-weight="700" fill="#7ef0b6">France</text><text x="190" y="207" font-size="9" text-anchor="end" fill="#cfe8d8">77%</text><rect x="326" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="334" y="187" font-size="10.5" font-weight="400" fill="#7c89a3">Canada</text><text x="430" y="187" font-size="9" text-anchor="end" fill="#5d6880">32%</text><rect x="326" y="193" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="334" y="207" font-size="10.5" font-weight="700" fill="#7ef0b6">Netherlands</text><text x="430" y="207" font-size="9" text-anchor="end" fill="#cfe8d8">68%</text><rect x="566" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="574" y="187" font-size="10.5" font-weight="400" fill="#7c89a3">Portugal</text><text x="670" y="187" font-size="9" text-anchor="end" fill="#5d6880">35%</text><rect x="566" y="193" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="574" y="207" font-size="10.5" font-weight="700" fill="#7ef0b6">Spain</text><text x="670" y="207" font-size="9" text-anchor="end" fill="#cfe8d8">65%</text><rect x="806" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="806" y="172" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="814" y="187" font-size="10.5" font-weight="700" fill="#7ef0b6">USA</text><text x="910" y="187" font-size="9" text-anchor="end" fill="#cfe8d8">66%</text><text x="814" y="207" font-size="10.5" font-weight="400" fill="#7c89a3">Egypt</text><text x="910" y="207" font-size="9" text-anchor="end" fill="#5d6880">34%</text><rect x="1046" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1046" y="172" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1054" y="187" font-size="10.5" font-weight="700" fill="#7ef0b6">Brazil</text><text x="1150" y="187" font-size="9" text-anchor="end" fill="#cfe8d8">53%</text><text x="1054" y="207" font-size="10.5" font-weight="400" fill="#7c89a3">Norway</text><text x="1150" y="207" font-size="9" text-anchor="end" fill="#5d6880">47%</text><rect x="1286" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="1294" y="187" font-size="10.5" font-weight="400" fill="#7c89a3">Mexico</text><text x="1390" y="187" font-size="9" text-anchor="end" fill="#5d6880">52%</text><rect x="1286" y="193" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1294" y="207" font-size="10.5" font-weight="700" fill="#7ef0b6">England</text><text x="1390" y="207" font-size="9" text-anchor="end" fill="#cfe8d8">48%†</text><rect x="1526" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1526" y="172" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1534" y="187" font-size="10.5" font-weight="700" fill="#7ef0b6">Argentina</text><text x="1630" y="187" font-size="9" text-anchor="end" fill="#cfe8d8">69%</text><text x="1534" y="207" font-size="10.5" font-weight="400" fill="#7c89a3">Belgium</text><text x="1630" y="207" font-size="9" text-anchor="end" fill="#5d6880">31%</text><rect x="1766" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="1774" y="187" font-size="10.5" font-weight="400" fill="#7c89a3">Switzerland</text><text x="1870" y="187" font-size="9" text-anchor="end" fill="#5d6880">33%</text><rect x="1766" y="193" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1774" y="207" font-size="10.5" font-weight="700" fill="#7ef0b6">Colombia</text><text x="1870" y="207" font-size="9" text-anchor="end" fill="#cfe8d8">67%</text><rect x="206" y="286" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="206" y="288" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="214" y="303" font-size="10.5" font-weight="700" fill="#7ef0b6">France</text><text x="310" y="303" font-size="9" text-anchor="end" fill="#cfe8d8">53%</text><text x="214" y="323" font-size="10.5" font-weight="400" fill="#7c89a3">Netherlands</text><text x="310" y="323" font-size="9" text-anchor="end" fill="#5d6880">47%</text><rect x="686" y="286" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="686" y="288" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="694" y="303" font-size="10.5" font-weight="700" fill="#7ef0b6">Spain</text><text x="790" y="303" font-size="9" text-anchor="end" fill="#cfe8d8">72%</text><text x="694" y="323" font-size="10.5" font-weight="400" fill="#7c89a3">USA</text><text x="790" y="323" font-size="9" text-anchor="end" fill="#5d6880">28%</text><rect x="1166" y="286" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="1174" y="303" font-size="10.5" font-weight="400" fill="#7c89a3">Brazil</text><text x="1270" y="303" font-size="9" text-anchor="end" fill="#5d6880">44%</text><rect x="1166" y="309" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1174" y="323" font-size="10.5" font-weight="700" fill="#7ef0b6">England</text><text x="1270" y="323" font-size="9" text-anchor="end" fill="#cfe8d8">56%</text><rect x="1646" y="286" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1646" y="288" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1654" y="303" font-size="10.5" font-weight="700" fill="#7ef0b6">Argentina</text><text x="1750" y="303" font-size="9" text-anchor="end" fill="#cfe8d8">62%</text><text x="1654" y="323" font-size="10.5" font-weight="400" fill="#7c89a3">Colombia</text><text x="1750" y="323" font-size="9" text-anchor="end" fill="#5d6880">38%</text><rect x="446" y="402" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="454" y="419" font-size="10.5" font-weight="400" fill="#7c89a3">France</text><text x="550" y="419" font-size="9" text-anchor="end" fill="#5d6880">39%</text><rect x="446" y="425" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="454" y="439" font-size="10.5" font-weight="700" fill="#7ef0b6">Spain</text><text x="550" y="439" font-size="9" text-anchor="end" fill="#cfe8d8">61%</text><rect x="1406" y="402" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="1414" y="419" font-size="10.5" font-weight="400" fill="#7c89a3">England</text><text x="1510" y="419" font-size="9" text-anchor="end" fill="#5d6880">38%</text><rect x="1406" y="425" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1414" y="439" font-size="10.5" font-weight="700" fill="#7ef0b6">Argentina</text><text x="1510" y="439" font-size="9" text-anchor="end" fill="#cfe8d8">62%</text><rect x="926" y="518" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="934" y="535" font-size="10.5" font-weight="400" fill="#7c89a3">Spain</text><text x="1030" y="535" font-size="9" text-anchor="end" fill="#5d6880">55%</text><rect x="926" y="541" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="934" y="555" font-size="10.5" font-weight="700" fill="#7ef0b6">Argentina</text><text x="1030" y="555" font-size="9" text-anchor="end" fill="#cfe8d8">45%†</text><rect x="888" y="598" width="188" height="46" rx="10" fill="#f5c542"/><text x="982" y="619" font-size="13" font-weight="800" fill="#1a1300" text-anchor="middle">🏆 Argentina</text><text x="982" y="635" font-size="10" fill="#5a4a00" text-anchor="middle">projected champion · 21% to win</text></svg>
</div>

## Upcoming group matches — outcome probabilities

*(next match days; full list for all 72 group games in `match_probabilities.csv`)*

| Date | Grp | Match | Home win | Draw | Away win | xG | Likely score |
|------|:---:|-------|---------:|-----:|---------:|----|:----:|
| 2026-06-25 | D | United States v Turkey | **50.7%** | 25.7% | 23.5% | 1.65–1.05 | 1-1 |
| 2026-06-25 | D | Paraguay v Australia | **37.0%** | 28.8% | 34.2% | 1.25–1.19 | 1-1 |
| 2026-06-26 | I | Senegal v Iraq | **62.7%** | 22.4% | 14.9% | 1.93–0.83 | 2-0 |
| 2026-06-26 | I | Norway v France | 17.8% | 22.8% | **59.4%** | 0.96–1.93 | 1-1 |
| 2026-06-26 | H | Uruguay v Spain | 14.8% | 23.7% | **61.5%** | 0.76–1.79 | 0-1 |
| 2026-06-26 | G | New Zealand v Belgium | 19.3% | 25.8% | **54.9%** | 0.87–1.64 | 0-1 |
| 2026-06-26 | G | Egypt v Iran | 31.4% | 28.8% | **39.8%** | 1.12–1.29 | 1-1 |
| 2026-06-26 | H | Cape Verde v Saudi Arabia | 33.0% | 29.0% | **38.1%** | 1.15–1.25 | 1-1 |
| 2026-06-27 | L | Panama v England | 15.1% | 23.2% | **61.6%** | 0.80–1.85 | 0-1 |
| 2026-06-27 | J | Algeria v Austria | 31.8% | 29.2% | **39.0%** | 1.10–1.25 | 1-1 |
| 2026-06-27 | J | Jordan v Argentina | 4.2% | 13.3% | **82.5%** | 0.43–2.52 | 0-2 |
| 2026-06-27 | K | Colombia v Portugal | **42.6%** | 29.6% | 27.8% | 1.28–0.98 | 1-1 |
| 2026-06-27 | K | DR Congo v Uzbekistan | **37.8%** | 30.6% | 31.7% | 1.15–1.03 | 1-1 |
| 2026-06-27 | L | Croatia v Ghana | **61.5%** | 23.7% | 14.8% | 1.80–0.76 | 1-0 |

## Group projections

### Group A

**✅ Into the knockouts:** Mexico, South Africa

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Mexico ✅ | 3 | 3-0-0 | 6-0 | **9** | 9.00 | 100.0% | 100.0% | 100.0% |
| South Africa ✅ | 3 | 1-1-1 | 2-3 | **4** | 4.00 | 0.0% | 100.0% | 100.0% |
| South Korea | 3 | 1-0-2 | 2-3 | **3** | 3.00 | 0.0% | 0.0% | 75.1% |
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
| Scotland | 3 | 1-0-2 | 1-4 | **3** | 3.00 | 0.0% | 0.0% | 12.8% |
| Haiti | 3 | 0-0-3 | 2-8 | **0** | 0.00 | 0.0% | 0.0% | 0.0% |

### Group D

**✅ Into the knockouts:** United States

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| United States ✅ | 2 | 2-0-0 | 6-1 | **6** | 7.78 | 100.0% | 100.0% | 100.0% |
| Australia | 2 | 1-0-1 | 2-2 | **3** | 4.31 | 0.0% | 62.9% | 88.3% |
| Paraguay | 2 | 1-0-1 | 2-4 | **3** | 4.40 | 0.0% | 37.1% | 74.5% |
| Turkey | 2 | 0-0-2 | 0-3 | **0** | 0.96 | 0.0% | 0.0% | 0.0% |

### Group E

**✅ Into the knockouts:** Germany, Ivory Coast, Ecuador

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Germany ✅ | 3 | 2-0-1 | 10-4 | **6** | 6.00 | 100.0% | 100.0% | 100.0% |
| Ivory Coast ✅ | 3 | 2-0-1 | 4-2 | **6** | 6.00 | 0.0% | 100.0% | 100.0% |
| Ecuador ✅ | 3 | 1-1-1 | 2-2 | **4** | 4.00 | 0.0% | 0.0% | 100.0% |
| Curaçao | 3 | 0-1-2 | 1-9 | **1** | 1.00 | 0.0% | 0.0% | 0.0% |

### Group F

**✅ Into the knockouts:** Netherlands, Japan, Sweden

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Netherlands ✅ | 3 | 2-1-0 | 10-4 | **7** | 7.00 | 100.0% | 100.0% | 100.0% |
| Japan ✅ | 3 | 1-2-0 | 7-3 | **5** | 5.00 | 0.0% | 100.0% | 100.0% |
| Sweden ✅ | 3 | 1-1-1 | 7-7 | **4** | 4.00 | 0.0% | 0.0% | 100.0% |
| Tunisia | 3 | 0-0-3 | 2-12 | **0** | 0.00 | 0.0% | 0.0% | 0.0% |

### Group G

**✅ Into the knockouts:** Egypt

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Egypt ✅ | 2 | 1-1-0 | 4-2 | **4** | 5.24 | 56.1% | 78.5% | 100.0% |
| Iran | 2 | 0-2-0 | 2-2 | **2** | 3.47 | 29.3% | 44.5% | 67.8% |
| Belgium | 2 | 0-2-0 | 1-1 | **2** | 3.90 | 14.7% | 65.4% | 80.3% |
| New Zealand | 2 | 0-1-1 | 3-5 | **1** | 1.84 | 0.0% | 11.6% | 19.3% |

### Group H

**✅ Into the knockouts:** Spain

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Spain ✅ | 2 | 1-1-0 | 4-0 | **4** | 6.08 | 85.0% | 95.2% | 100.0% |
| Uruguay | 2 | 0-2-0 | 3-3 | **2** | 2.68 | 13.1% | 21.0% | 38.0% |
| Cape Verde | 2 | 0-2-0 | 2-2 | **2** | 3.28 | 1.9% | 51.3% | 61.5% |
| Saudi Arabia | 2 | 0-1-1 | 1-5 | **1** | 2.43 | 0.0% | 32.5% | 38.1% |

### Group I

**✅ Into the knockouts:** France, Norway

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| France ✅ | 2 | 2-0-0 | 6-1 | **6** | 8.02 | 82.4% | 100.0% | 100.0% |
| Norway ✅ | 2 | 2-0-0 | 7-3 | **6** | 6.76 | 17.6% | 100.0% | 100.0% |
| Senegal | 2 | 0-0-2 | 3-6 | **0** | 2.10 | 0.0% | 0.0% | 50.3% |
| Iraq | 2 | 0-0-2 | 1-7 | **0** | 0.67 | 0.0% | 0.0% | 0.7% |

### Group J

**✅ Into the knockouts:** Argentina

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Argentina ✅ | 2 | 2-0-0 | 5-0 | **6** | 8.61 | 100.0% | 100.0% | 100.0% |
| Austria | 2 | 1-0-1 | 3-3 | **3** | 4.46 | 0.0% | 68.2% | 91.0% |
| Algeria | 2 | 1-0-1 | 2-4 | **3** | 4.25 | 0.0% | 31.8% | 69.7% |
| Jordan | 2 | 0-0-2 | 2-5 | **0** | 0.26 | 0.0% | 0.0% | 0.0% |

### Group K

**✅ Into the knockouts:** Portugal, Colombia

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Colombia ✅ | 2 | 2-0-0 | 4-1 | **6** | 7.58 | 72.4% | 100.0% | 100.0% |
| Portugal ✅ | 2 | 1-1-0 | 6-1 | **4** | 5.12 | 27.6% | 99.7% | 100.0% |
| DR Congo | 2 | 0-1-1 | 1-2 | **1** | 2.45 | 0.0% | 0.3% | 38.1% |
| Uzbekistan | 2 | 0-0-2 | 1-8 | **0** | 1.25 | 0.0% | 0.0% | 0.5% |

### Group L

**✅ Into the knockouts:** England

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| England ✅ | 2 | 1-1-0 | 4-2 | **4** | 6.07 | 66.6% | 99.7% | 100.0% |
| Ghana | 2 | 1-1-0 | 1-0 | **4** | 4.69 | 9.6% | 38.9% | 100.0% |
| Croatia | 2 | 1-0-1 | 3-4 | **3** | 5.08 | 23.9% | 61.4% | 93.9% |
| Panama | 2 | 0-0-2 | 0-2 | **0** | 0.69 | 0.0% | 0.0% | 0.0% |

*\*Advance = top two or one of the eight best third-placed teams.*

*✅ = already reached the knockout stage — locked into the Round of 32 in every simulation. (Reaching later rounds still requires winning knockout games, so those stay below 100%.)*

## Most likely knockout bracket

Each tie shows the projected pairing and the side that advances — the team **more likely to win the tournament** of the two, so the bracket crowns the overall favourite. 'Win prob' is that team's chance in that single match (a **†** flags a near-even tie where the title favourite is a slight underdog in the one-off game). **🔒 marks a confirmed tie** — the same two teams in every simulation, mathematically locked. (3/16 Round-of-32 ties locked so far; the rest finalise as the group stage completes on 27 June.)

### Round of 32

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 73 | 2026-06-28 | SoFi Stadium, Los Angeles | 🔒 South Africa v Canada | **Canada** | 63.7% | 🔒 locked |
| 74 | 2026-06-29 | Gillette Stadium, Boston | Germany v Bosnia and Herzegovina | **Germany** | 91.9% | 1.7% |
| 75 | 2026-06-29 | Estadio BBVA, Monterrey | 🔒 Netherlands v Morocco | **Netherlands** | 50.8% | 🔒 locked |
| 76 | 2026-06-29 | NRG Stadium, Houston | 🔒 Brazil v Japan | **Brazil** | 57.6% | 🔒 locked |
| 77 | 2026-06-30 | MetLife Stadium, New York/New Jersey | France v Sweden | **France** | 80.9% | 1.5% |
| 78 | 2026-06-30 | AT&T Stadium, Dallas | Ivory Coast v Norway | **Norway** | 68.2% | 82.4% |
| 79 | 2026-06-30 | Estadio Azteca, Mexico City | Mexico v Ecuador | **Mexico** | 64.3% | 81.9% |
| 80 | 2026-07-01 | Mercedes-Benz Stadium, Atlanta | England v DR Congo | **England** | 85.9% | 25.2% |
| 81 | 2026-07-01 | Levi's Stadium, San Francisco Bay Area | United States v Senegal | **United States** | 72.1% | 0.7% |
| 82 | 2026-07-01 | Lumen Field, Seattle | Egypt v South Korea | **Egypt** | 48.0%† | 45.3% |
| 83 | 2026-07-02 | BMO Field, Toronto | Portugal v Croatia | **Portugal** | 74.9% | 27.1% |
| 84 | 2026-07-02 | SoFi Stadium, Los Angeles | Spain v Austria | **Spain** | 76.5% | 58.2% |
| 85 | 2026-07-02 | BC Place, Vancouver | Switzerland v Algeria | **Switzerland** | 61.4% | 15.9% |
| 86 | 2026-07-03 | Hard Rock Stadium, Miami | Argentina v Cape Verde | **Argentina** | 93.1% | 49.3% |
| 87 | 2026-07-03 | Arrowhead Stadium, Kansas City | Colombia v Ghana | **Colombia** | 87.1% | 44.3% |
| 88 | 2026-07-03 | AT&T Stadium, Dallas | Australia v Belgium | **Belgium** | 52.6% | 31.9% |

### Round of 16

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 89 | 2026-07-04 | Lincoln Financial Field, Philadelphia | Germany v France | **France** | 76.6% | 44.8% |
| 90 | 2026-07-04 | NRG Stadium, Houston | Canada v Netherlands | **Netherlands** | 68.1% | 32.2% |
| 91 | 2026-07-05 | MetLife Stadium, New York/New Jersey | Brazil v Norway | **Brazil** | 53.3% | 32.6% |
| 92 | 2026-07-05 | Estadio Azteca, Mexico City | Mexico v England | **England** | 47.6%† | 34.6% |
| 93 | 2026-07-06 | AT&T Stadium, Dallas | Portugal v Spain | **Spain** | 64.7% | 32.2% |
| 94 | 2026-07-06 | Lumen Field, Seattle | United States v Egypt | **United States** | 66.4% | 23.9% |
| 95 | 2026-07-07 | Mercedes-Benz Stadium, Atlanta | Argentina v Belgium | **Argentina** | 68.7% | 24.0% |
| 96 | 2026-07-07 | BC Place, Vancouver | Switzerland v Colombia | **Colombia** | 67.1% | 36.7% |

### Quarter-finals

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 97 | 2026-07-09 | Gillette Stadium, Boston | France v Netherlands | **France** | 53.0% | 18.1% |
| 98 | 2026-07-10 | SoFi Stadium, Los Angeles | Spain v United States | **Spain** | 72.3% | 24.7% |
| 99 | 2026-07-11 | Hard Rock Stadium, Miami | Brazil v England | **England** | 55.9% | 9.3% |
| 100 | 2026-07-11 | Arrowhead Stadium, Kansas City | Argentina v Colombia | **Argentina** | 61.6% | 27.4% |

### Semi-finals

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 101 | 2026-07-14 | AT&T Stadium, Dallas | France v Spain | **Spain** | 60.8% | 10.9% |
| 102 | 2026-07-15 | Mercedes-Benz Stadium, Atlanta | England v Argentina | **Argentina** | 62.2% | 7.6% |

### Final

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 104 | 2026-07-19 | MetLife Stadium, East Rutherford | Spain v Argentina | **Argentina** | 44.8%† | 8.3% |

**Projected champion: Argentina** (overall title probability 20.7%). The bracket advances the team more likely to go all the way in each tie, so the champion here matches the title favourite at the top of the page.

*† The title favourite reaches this tie via an easier path, so it wins the tournament most often even though this specific one-off match is a near coin-flip the other side shades.*

## How to read this

- All figures are probabilities, not certainties — a 65% favourite loses about one such match in three.
- `xPts` = expected group points; `xG` = expected goals from the Poisson model.
- Predictions refresh after every match day: run `python -m worldcup.run all` to pull new results, re-rate teams, and re-simulate.
- Machine-readable outputs: `match_probabilities.csv`, `tournament_projections.csv`. Past reports in `outputs/archive/`.

## Model scorecard

**35 of 58 match outcomes called correctly** (the model's own probabilities expected ≈34.0 of 58) · exact scoreline predicted 3/58 · average probability placed on what actually happened: **45.4%** (33.3% = guessing).

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
| Belgium v Iran | Belgium win (46.7%) | 1-1 | 0-0 | ❌ | — |
| New Zealand v Egypt | Egypt win (38.7%) | 1-1 | 1-3 | ✅ | — |
| Spain v Saudi Arabia | Spain win (78.3%) | 2-0 | 4-0 | ✅ | — |
| Uruguay v Cape Verde | Uruguay win (72.7%) | 2-0 | 2-2 | ❌ | — |
| Argentina v Austria | Argentina win (66.2%) | 2-0 | 2-0 | ✅ | ✅ |
| France v Iraq | France win (76.5%) | 2-0 | 3-0 | ✅ | — |
| Norway v Senegal | Norway win (47.5%) | 1-1 | 3-2 | ✅ | — |
| Jordan v Algeria | Algeria win (52.0%) | 1-1 | 1-2 | ✅ | — |
| Panama v Croatia | Croatia win (42.4%) | 1-1 | 0-1 | ✅ | — |
| England v Ghana | England win (75.8%) | 2-0 | 0-0 | ❌ | — |
| Portugal v Uzbekistan | Portugal win (63.7%) | 1-0 | 5-0 | ✅ | — |
| Colombia v DR Congo | Colombia win (65.4%) | 2-0 | 1-0 | ✅ | — |
| Canada v Switzerland | Canada win (37.9%) | 1-1 | 1-2 | ❌ | — |
| Morocco v Haiti | Morocco win (72.8%) | 2-0 | 4-2 | ✅ | — |
| Bosnia and Herzegovina v Qatar | Bosnia and Herzegovina win (47.3%) | 1-1 | 3-1 | ✅ | — |
| Scotland v Brazil | Brazil win (58.8%) | 0-1 | 0-3 | ✅ | — |
| South Africa v South Korea | South Korea win (56.4%) | 0-1 | 1-0 | ❌ | — |
| Mexico v Czech Republic | Mexico win (78.6%) | 2-0 | 3-0 | ✅ | — |
| Ecuador v Germany | Germany win (40.9%) | 1-1 | 2-1 | ❌ | — |
| Japan v Sweden | Japan win (61.5%) | 2-0 | 1-1 | ❌ | — |
| Curaçao v Ivory Coast | Ivory Coast win (57.6%) | 0-1 | 0-2 | ✅ | — |
| Tunisia v Netherlands | Netherlands win (71.3%) | 0-2 | 1-3 | ✅ | — |

**Calibration vs benchmarks** (the 9 graded games with bookmaker prices on file) — log-loss, lower is better. This is the honest test: is the model bad, or were the games hard for everyone?

| Forecaster | Log-loss |
|------------|---------:|
| **This model** | **1.193** |
| Sky Bet (de-vigged) | 1.156 |
| Coin-flip (33/33/33) | 1.099 |

The model is **essentially level with the market** (+0.037 log-loss). Note both the model **and** the bookmaker scored worse than a coin-flip here — with this many draws and upsets, the slate was close to unforecastable for anyone, which is the real reason the hit-rate looks poor.


*Predictions are frozen at the last run before each result arrives, then graded — the scorecard never grades a model that has already seen the answer.*

