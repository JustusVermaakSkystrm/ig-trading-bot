# FIFA World Cup 2026 — ML Prediction Report

*Generated 2026-06-15 · data through **2026-06-14** · 50,000 Monte Carlo simulations · 11/72 group matches played*

Probabilities come from a gradient-boosted Poisson goal model (Elo strength + rolling form + venue/importance features) trained on 30,783 internationals, simulated through the official 2026 bracket and tiebreaker rules.

*Rolling validation (7,966 matches, 2018–2026): RPS 0.1687 vs Elo-baseline 0.1711; log-loss 0.8652 vs 0.8809.*

## Title favourites

| # | Team | Group | Champion | Δ vs 2026-06-14 | Final | Semi-final | Quarter-final | Rd of 16 |
|---|------|:-----:|---------:|-------:|------:|-----------:|--------------:|---------:|
| 1 | Spain | H | **19.9%** | – | 30.0% | 41.8% | 55.1% | 71.7% |
| 2 | Argentina | J | **18.2%** | – | 27.7% | 38.2% | 52.1% | 68.0% |
| 3 | England | L | **8.5%** | – | 14.7% | 25.5% | 39.4% | 67.3% |
| 4 | France | I | **7.3%** | – | 13.8% | 27.1% | 44.3% | 65.2% |
| 5 | Brazil | C | **6.2%** | – | 12.1% | 24.1% | 40.0% | 62.6% |
| 6 | Colombia | K | **4.5%** | – | 9.3% | 16.8% | 30.6% | 58.5% |
| 7 | Portugal | K | **3.9%** | – | 8.5% | 16.1% | 31.7% | 60.1% |
| 8 | Mexico | A | **3.8%** | – | 8.9% | 19.6% | 40.9% | 68.8% |
| 9 | Japan | F | **2.7%** | – | 6.2% | 14.0% | 27.3% | 46.8% |
| 10 | Belgium | G | **2.7%** | – | 7.0% | 13.6% | 31.3% | 58.4% |
| 11 | Netherlands | F | **2.6%** | – | 6.3% | 14.9% | 28.3% | 48.6% |
| 12 | Germany | E | **2.3%** | – | 5.2% | 12.9% | 26.7% | 55.3% |
| 13 | Morocco | C | **2.2%** | – | 5.2% | 12.2% | 25.6% | 46.9% |
| 14 | Norway | I | **2.1%** | – | 5.0% | 12.5% | 26.3% | 48.4% |
| 15 | United States | D | **1.7%** | – | 4.5% | 11.0% | 28.8% | 60.8% |

## Biggest movers since last run (data through 2026-06-14)

| Team | Δ Champion | Δ Rd of 16 | Champion now |
|------|----------:|-----------:|-------------:|
| Spain | – | – | 19.9% |
| Algeria | – | – | 0.3% |
| South Korea | – | – | 0.7% |
| Senegal | – | – | 0.5% |
| Iran | – | – | 0.6% |
| Austria | – | – | 0.6% |
| Uruguay | – | – | 1.6% |
| Morocco | – | – | 2.2% |

*Δ values in probability points. Full run-by-run series in `outputs/history.csv`.*

## Path to the final

The model's single most likely knockout bracket — all 32 projected round-of-32 teams and every unplayed tie, each line carrying the projected winner down to the next round until they converge on the champion. Percentages are each side's chance of advancing from that tie.

<div style="overflow-x:auto; margin:1rem 0;">
<svg viewBox="0 0 1964 662" width="100%" preserveAspectRatio="xMidYMin meet" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica,Arial,sans-serif"><path d="M82,98 C82,134 142,134 142,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M202,98 C202,134 142,134 142,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M322,98 C322,134 382,134 382,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M442,98 C442,134 382,134 382,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M562,98 C562,134 622,134 622,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M682,98 C682,134 622,134 622,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M802,98 C802,134 862,134 862,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M922,98 C922,134 862,134 862,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1042,98 C1042,134 1102,134 1102,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1162,98 C1162,134 1102,134 1102,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1282,98 C1282,134 1342,134 1342,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1402,98 C1402,134 1342,134 1342,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1522,98 C1522,134 1582,134 1582,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1642,98 C1642,134 1582,134 1582,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1762,98 C1762,134 1822,134 1822,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1882,98 C1882,134 1822,134 1822,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M142,214 C142,250 262,250 262,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M382,214 C382,250 262,250 262,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M622,214 C622,250 742,250 742,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M862,214 C862,250 742,250 742,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1102,214 C1102,250 1222,250 1222,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1342,214 C1342,250 1222,250 1222,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1582,214 C1582,250 1702,250 1702,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1822,214 C1822,250 1702,250 1702,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M262,330 C262,366 502,366 502,402" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M742,330 C742,366 502,366 502,402" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1222,330 C1222,366 1462,366 1462,402" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1702,330 C1702,366 1462,366 1462,402" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M502,446 C502,482 982,482 982,518" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1462,446 C1462,482 982,482 982,518" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M982,562 C982,580 982,580 982,598" fill="none" stroke="#33436b" stroke-width="1.5"/><text x="11" y="76" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 11 76)" text-anchor="middle">ROUND OF 32</text><text x="11" y="192" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 11 192)" text-anchor="middle">ROUND OF 16</text><text x="11" y="308" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 11 308)" text-anchor="middle">QUARTER-FINALS</text><text x="11" y="424" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 11 424)" text-anchor="middle">SEMI-FINALS</text><text x="11" y="540" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 11 540)" text-anchor="middle">FINAL</text><rect x="26" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="26" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="34" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Germany</text><text x="130" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">58%</text><text x="34" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Scotland</text><text x="130" y="91" font-size="9" text-anchor="end" fill="#5d6880">42%</text><rect x="146" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="146" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="154" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">France</text><text x="250" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">68%</text><text x="154" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Türkiye</text><text x="250" y="91" font-size="9" text-anchor="end" fill="#5d6880">32%</text><rect x="266" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="274" y="71" font-size="10.5" font-weight="400" fill="#7c89a3">S. Korea</text><text x="370" y="71" font-size="9" text-anchor="end" fill="#5d6880">38%</text><rect x="266" y="77" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="274" y="91" font-size="10.5" font-weight="700" fill="#7ef0b6">Switzerland</text><text x="370" y="91" font-size="9" text-anchor="end" fill="#cfe8d8">62%</text><rect x="386" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="386" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="394" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Netherlands</text><text x="490" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">53%</text><text x="394" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Morocco</text><text x="490" y="91" font-size="9" text-anchor="end" fill="#5d6880">47%</text><rect x="506" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="506" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="514" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Colombia</text><text x="610" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">69%</text><text x="514" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Croatia</text><text x="610" y="91" font-size="9" text-anchor="end" fill="#5d6880">31%</text><rect x="626" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="626" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="634" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Spain</text><text x="730" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">78%</text><text x="634" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Austria</text><text x="730" y="91" font-size="9" text-anchor="end" fill="#5d6880">22%</text><rect x="746" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="746" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="754" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">USA</text><text x="850" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">83%</text><text x="754" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Bosnia</text><text x="850" y="91" font-size="9" text-anchor="end" fill="#5d6880">17%</text><rect x="866" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="866" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="874" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Belgium</text><text x="970" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">77%</text><text x="874" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Czechia</text><text x="970" y="91" font-size="9" text-anchor="end" fill="#5d6880">23%</text><rect x="986" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="986" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="994" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Brazil</text><text x="1090" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">62%</text><text x="994" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Japan</text><text x="1090" y="91" font-size="9" text-anchor="end" fill="#5d6880">38%</text><rect x="1106" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="1114" y="71" font-size="10.5" font-weight="400" fill="#7c89a3">Ivory Coast</text><text x="1210" y="71" font-size="9" text-anchor="end" fill="#5d6880">37%</text><rect x="1106" y="77" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1114" y="91" font-size="10.5" font-weight="700" fill="#7ef0b6">Norway</text><text x="1210" y="91" font-size="9" text-anchor="end" fill="#cfe8d8">63%</text><rect x="1226" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1226" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1234" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Mexico</text><text x="1330" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">66%</text><text x="1234" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Ecuador</text><text x="1330" y="91" font-size="9" text-anchor="end" fill="#5d6880">34%</text><rect x="1346" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1346" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1354" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">England</text><text x="1450" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">84%</text><text x="1354" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Saudi</text><text x="1450" y="91" font-size="9" text-anchor="end" fill="#5d6880">16%</text><rect x="1466" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1466" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1474" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Argentina</text><text x="1570" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">78%</text><text x="1474" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Uruguay</text><text x="1570" y="91" font-size="9" text-anchor="end" fill="#5d6880">22%</text><rect x="1586" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1586" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1594" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Australia</text><text x="1690" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">60%</text><text x="1594" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Iran</text><text x="1690" y="91" font-size="9" text-anchor="end" fill="#5d6880">40%</text><rect x="1706" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1706" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1714" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Canada</text><text x="1810" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">60%</text><text x="1714" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Senegal</text><text x="1810" y="91" font-size="9" text-anchor="end" fill="#5d6880">40%</text><rect x="1826" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1826" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1834" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Portugal</text><text x="1930" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">73%</text><text x="1834" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Panama</text><text x="1930" y="91" font-size="9" text-anchor="end" fill="#5d6880">27%</text><rect x="86" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="94" y="187" font-size="10.5" font-weight="400" fill="#7c89a3">Germany</text><text x="190" y="187" font-size="9" text-anchor="end" fill="#5d6880">29%</text><rect x="86" y="193" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="94" y="207" font-size="10.5" font-weight="700" fill="#7ef0b6">France</text><text x="190" y="207" font-size="9" text-anchor="end" fill="#cfe8d8">71%</text><rect x="326" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="334" y="187" font-size="10.5" font-weight="400" fill="#7c89a3">Switzerland</text><text x="430" y="187" font-size="9" text-anchor="end" fill="#5d6880">35%</text><rect x="326" y="193" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="334" y="207" font-size="10.5" font-weight="700" fill="#7ef0b6">Netherlands</text><text x="430" y="207" font-size="9" text-anchor="end" fill="#cfe8d8">65%</text><rect x="566" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="574" y="187" font-size="10.5" font-weight="400" fill="#7c89a3">Colombia</text><text x="670" y="187" font-size="9" text-anchor="end" fill="#5d6880">20%</text><rect x="566" y="193" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="574" y="207" font-size="10.5" font-weight="700" fill="#7ef0b6">Spain</text><text x="670" y="207" font-size="9" text-anchor="end" fill="#cfe8d8">80%</text><rect x="806" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="814" y="187" font-size="10.5" font-weight="400" fill="#7c89a3">USA</text><text x="910" y="187" font-size="9" text-anchor="end" fill="#5d6880">39%</text><rect x="806" y="193" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="814" y="207" font-size="10.5" font-weight="700" fill="#7ef0b6">Belgium</text><text x="910" y="207" font-size="9" text-anchor="end" fill="#cfe8d8">61%</text><rect x="1046" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1046" y="172" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1054" y="187" font-size="10.5" font-weight="700" fill="#7ef0b6">Brazil</text><text x="1150" y="187" font-size="9" text-anchor="end" fill="#cfe8d8">55%</text><text x="1054" y="207" font-size="10.5" font-weight="400" fill="#7c89a3">Norway</text><text x="1150" y="207" font-size="9" text-anchor="end" fill="#5d6880">45%</text><rect x="1286" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1286" y="172" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1294" y="187" font-size="10.5" font-weight="700" fill="#7ef0b6">Mexico</text><text x="1390" y="187" font-size="9" text-anchor="end" fill="#cfe8d8">52%</text><text x="1294" y="207" font-size="10.5" font-weight="400" fill="#7c89a3">England</text><text x="1390" y="207" font-size="9" text-anchor="end" fill="#5d6880">48%</text><rect x="1526" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1526" y="172" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1534" y="187" font-size="10.5" font-weight="700" fill="#7ef0b6">Argentina</text><text x="1630" y="187" font-size="9" text-anchor="end" fill="#cfe8d8">74%</text><text x="1534" y="207" font-size="10.5" font-weight="400" fill="#7c89a3">Australia</text><text x="1630" y="207" font-size="9" text-anchor="end" fill="#5d6880">26%</text><rect x="1766" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="1774" y="187" font-size="10.5" font-weight="400" fill="#7c89a3">Canada</text><text x="1870" y="187" font-size="9" text-anchor="end" fill="#5d6880">45%</text><rect x="1766" y="193" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1774" y="207" font-size="10.5" font-weight="700" fill="#7ef0b6">Portugal</text><text x="1870" y="207" font-size="9" text-anchor="end" fill="#cfe8d8">55%</text><rect x="206" y="286" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="206" y="288" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="214" y="303" font-size="10.5" font-weight="700" fill="#7ef0b6">France</text><text x="310" y="303" font-size="9" text-anchor="end" fill="#cfe8d8">51%</text><text x="214" y="323" font-size="10.5" font-weight="400" fill="#7c89a3">Netherlands</text><text x="310" y="323" font-size="9" text-anchor="end" fill="#5d6880">49%</text><rect x="686" y="286" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="686" y="288" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="694" y="303" font-size="10.5" font-weight="700" fill="#7ef0b6">Spain</text><text x="790" y="303" font-size="9" text-anchor="end" fill="#cfe8d8">72%</text><text x="694" y="323" font-size="10.5" font-weight="400" fill="#7c89a3">Belgium</text><text x="790" y="323" font-size="9" text-anchor="end" fill="#5d6880">28%</text><rect x="1166" y="286" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1166" y="288" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1174" y="303" font-size="10.5" font-weight="700" fill="#7ef0b6">Brazil</text><text x="1270" y="303" font-size="9" text-anchor="end" fill="#cfe8d8">62%</text><text x="1174" y="323" font-size="10.5" font-weight="400" fill="#7c89a3">Mexico</text><text x="1270" y="323" font-size="9" text-anchor="end" fill="#5d6880">38%</text><rect x="1646" y="286" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1646" y="288" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1654" y="303" font-size="10.5" font-weight="700" fill="#7ef0b6">Argentina</text><text x="1750" y="303" font-size="9" text-anchor="end" fill="#cfe8d8">68%</text><text x="1654" y="323" font-size="10.5" font-weight="400" fill="#7c89a3">Portugal</text><text x="1750" y="323" font-size="9" text-anchor="end" fill="#5d6880">32%</text><rect x="446" y="402" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="454" y="419" font-size="10.5" font-weight="400" fill="#7c89a3">France</text><text x="550" y="419" font-size="9" text-anchor="end" fill="#5d6880">31%</text><rect x="446" y="425" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="454" y="439" font-size="10.5" font-weight="700" fill="#7ef0b6">Spain</text><text x="550" y="439" font-size="9" text-anchor="end" fill="#cfe8d8">69%</text><rect x="1406" y="402" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="1414" y="419" font-size="10.5" font-weight="400" fill="#7c89a3">Brazil</text><text x="1510" y="419" font-size="9" text-anchor="end" fill="#5d6880">30%</text><rect x="1406" y="425" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1414" y="439" font-size="10.5" font-weight="700" fill="#7ef0b6">Argentina</text><text x="1510" y="439" font-size="9" text-anchor="end" fill="#cfe8d8">70%</text><rect x="926" y="518" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="926" y="520" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="934" y="535" font-size="10.5" font-weight="700" fill="#7ef0b6">Spain</text><text x="1030" y="535" font-size="9" text-anchor="end" fill="#cfe8d8">57%</text><text x="934" y="555" font-size="10.5" font-weight="400" fill="#7c89a3">Argentina</text><text x="1030" y="555" font-size="9" text-anchor="end" fill="#5d6880">43%</text><rect x="888" y="598" width="188" height="46" rx="10" fill="#f5c542"/><text x="982" y="619" font-size="13" font-weight="800" fill="#1a1300" text-anchor="middle">🏆 Spain</text><text x="982" y="635" font-size="10" fill="#5a4a00" text-anchor="middle">projected champion · 20% to win</text></svg>
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

