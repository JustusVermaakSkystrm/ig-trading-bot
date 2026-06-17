# FIFA World Cup 2026 — ML Prediction Report

*Generated 2026-06-17 · data through **2026-06-17** · 50,000 Monte Carlo simulations · 22/72 group matches played*

Probabilities come from a gradient-boosted Poisson goal model (Elo strength + rolling form + venue/importance features) trained on 30,794 internationals, simulated through the official 2026 bracket and tiebreaker rules.

*Rolling validation (7,966 matches, 2018–2026): RPS 0.1687 vs Elo-baseline 0.1711; log-loss 0.8652 vs 0.8809.*

## Title favourites

| # | Team | Group | Champion | Δ vs 2026-06-17 | Final | Semi-final | Quarter-final | Rd of 16 |
|---|------|:-----:|---------:|-------:|------:|-----------:|--------------:|---------:|
| 1 | Argentina | J | **20.5%** | -0.5 | 29.7% | 41.4% | 55.5% | 72.3% |
| 2 | Spain | H | **13.3%** | -1.3 | 21.5% | 31.8% | 43.7% | 60.5% |
| 3 | England | L | **10.2%** | +1.4 | 16.7% | 31.9% | 47.0% | 71.8% |
| 4 | France | I | **10.0%** | – | 18.3% | 31.6% | 50.3% | 71.4% |
| 5 | Colombia | K | **5.5%** | +1.0 | 10.7% | 19.6% | 37.3% | 61.9% |
| 6 | Brazil | C | **5.4%** | -0.3 | 10.7% | 20.4% | 36.9% | 59.3% |
| 7 | Mexico | A | **3.4%** | -0.3 | 7.7% | 17.9% | 34.6% | 69.5% |
| 8 | Portugal | K | **3.1%** | +0.3 | 7.2% | 14.2% | 26.9% | 51.7% |
| 9 | Japan | F | **2.8%** | – | 6.3% | 13.2% | 26.6% | 46.3% |
| 10 | Norway | I | **2.6%** | – | 6.0% | 14.4% | 34.2% | 59.6% |
| 11 | Netherlands | F | **2.3%** | -0.7 | 5.5% | 12.1% | 25.1% | 45.6% |
| 12 | United States | D | **2.2%** | +0.9 | 6.0% | 14.4% | 31.8% | 62.7% |
| 13 | Belgium | G | **2.1%** | +0.1 | 5.8% | 11.9% | 25.6% | 52.0% |
| 14 | Morocco | C | **2.1%** | +0.1 | 5.2% | 11.4% | 25.0% | 46.1% |
| 15 | Germany | E | **2.0%** | -1.0 | 4.8% | 10.9% | 23.3% | 53.1% |

## Biggest movers since last run (data through 2026-06-17)

| Team | Δ Champion | Δ Rd of 16 | Champion now |
|------|----------:|-----------:|-------------:|
| England | +1.4 | +3.1 | 10.2% |
| Colombia | +1.0 | +4.3 | 5.5% |
| United States | +0.9 | +3.6 | 2.2% |
| Ecuador | -0.3 | -2.9 | 1.3% |
| Argentina | -0.5 | -2.6 | 20.5% |
| Netherlands | -0.7 | -3.0 | 2.3% |
| Germany | -1.0 | -4.5 | 2.0% |
| Spain | -1.3 | -1.0 | 13.3% |

*Δ values in probability points. Full run-by-run series in `outputs/history.csv`.*

## Path to the final

The model's single most likely knockout bracket — all 32 projected round-of-32 teams and every unplayed tie, each line carrying the projected winner down to the next round until they converge on the champion. Percentages are each side's chance of advancing from that tie.

<div style="overflow-x:auto; margin:1rem 0;">
<svg viewBox="0 0 1964 662" width="100%" preserveAspectRatio="xMidYMin meet" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica,Arial,sans-serif"><path d="M82,98 C82,134 142,134 142,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M202,98 C202,134 142,134 142,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M322,98 C322,134 382,134 382,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M442,98 C442,134 382,134 382,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M562,98 C562,134 622,134 622,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M682,98 C682,134 622,134 622,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M802,98 C802,134 862,134 862,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M922,98 C922,134 862,134 862,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1042,98 C1042,134 1102,134 1102,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1162,98 C1162,134 1102,134 1102,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1282,98 C1282,134 1342,134 1342,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1402,98 C1402,134 1342,134 1342,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1522,98 C1522,134 1582,134 1582,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1642,98 C1642,134 1582,134 1582,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1762,98 C1762,134 1822,134 1822,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1882,98 C1882,134 1822,134 1822,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M142,214 C142,250 262,250 262,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M382,214 C382,250 262,250 262,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M622,214 C622,250 742,250 742,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M862,214 C862,250 742,250 742,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1102,214 C1102,250 1222,250 1222,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1342,214 C1342,250 1222,250 1222,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1582,214 C1582,250 1702,250 1702,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1822,214 C1822,250 1702,250 1702,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M262,330 C262,366 502,366 502,402" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M742,330 C742,366 502,366 502,402" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1222,330 C1222,366 1462,366 1462,402" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1702,330 C1702,366 1462,366 1462,402" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M502,446 C502,482 982,482 982,518" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1462,446 C1462,482 982,482 982,518" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M982,562 C982,580 982,580 982,598" fill="none" stroke="#33436b" stroke-width="1.5"/><text x="11" y="76" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 11 76)" text-anchor="middle">ROUND OF 32</text><text x="11" y="192" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 11 192)" text-anchor="middle">ROUND OF 16</text><text x="11" y="308" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 11 308)" text-anchor="middle">QUARTER-FINALS</text><text x="11" y="424" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 11 424)" text-anchor="middle">SEMI-FINALS</text><text x="11" y="540" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 11 540)" text-anchor="middle">FINAL</text><rect x="26" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="26" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="34" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Germany</text><text x="130" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">57%</text><text x="34" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Scotland</text><text x="130" y="91" font-size="9" text-anchor="end" fill="#5d6880">43%</text><rect x="146" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="146" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="154" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">France</text><text x="250" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">81%</text><text x="154" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Saudi</text><text x="250" y="91" font-size="9" text-anchor="end" fill="#5d6880">19%</text><rect x="266" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="274" y="71" font-size="10.5" font-weight="400" fill="#7c89a3">S. Korea</text><text x="370" y="71" font-size="9" text-anchor="end" fill="#5d6880">36%</text><rect x="266" y="77" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="274" y="91" font-size="10.5" font-weight="700" fill="#7ef0b6">Switzerland</text><text x="370" y="91" font-size="9" text-anchor="end" fill="#cfe8d8">64%</text><rect x="386" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="394" y="71" font-size="10.5" font-weight="400" fill="#7c89a3">Sweden</text><text x="490" y="71" font-size="9" text-anchor="end" fill="#5d6880">31%</text><rect x="386" y="77" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="394" y="91" font-size="10.5" font-weight="700" fill="#7ef0b6">Morocco</text><text x="490" y="91" font-size="9" text-anchor="end" fill="#cfe8d8">69%</text><rect x="506" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="506" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="514" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Portugal</text><text x="610" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">64%</text><text x="514" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Croatia</text><text x="610" y="91" font-size="9" text-anchor="end" fill="#5d6880">36%</text><rect x="626" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="626" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="634" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Spain</text><text x="730" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">74%</text><text x="634" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Austria</text><text x="730" y="91" font-size="9" text-anchor="end" fill="#5d6880">26%</text><rect x="746" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="746" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="754" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">USA</text><text x="850" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">84%</text><text x="754" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Bosnia</text><text x="850" y="91" font-size="9" text-anchor="end" fill="#5d6880">16%</text><rect x="866" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="866" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="874" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Belgium</text><text x="970" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">75%</text><text x="874" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Czechia</text><text x="970" y="91" font-size="9" text-anchor="end" fill="#5d6880">25%</text><rect x="986" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="986" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="994" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Brazil</text><text x="1090" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">57%</text><text x="994" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Japan</text><text x="1090" y="91" font-size="9" text-anchor="end" fill="#5d6880">43%</text><rect x="1106" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="1114" y="71" font-size="10.5" font-weight="400" fill="#7c89a3">Ivory Coast</text><text x="1210" y="71" font-size="9" text-anchor="end" fill="#5d6880">34%</text><rect x="1106" y="77" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1114" y="91" font-size="10.5" font-weight="700" fill="#7ef0b6">Norway</text><text x="1210" y="91" font-size="9" text-anchor="end" fill="#cfe8d8">66%</text><rect x="1226" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1226" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1234" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Mexico</text><text x="1330" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">72%</text><text x="1234" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Ecuador</text><text x="1330" y="91" font-size="9" text-anchor="end" fill="#5d6880">28%</text><rect x="1346" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1346" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1354" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">England</text><text x="1450" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">73%</text><text x="1354" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Senegal</text><text x="1450" y="91" font-size="9" text-anchor="end" fill="#5d6880">27%</text><rect x="1466" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1466" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1474" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Argentina</text><text x="1570" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">78%</text><text x="1474" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Uruguay</text><text x="1570" y="91" font-size="9" text-anchor="end" fill="#5d6880">22%</text><rect x="1586" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1586" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1594" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Australia</text><text x="1690" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">62%</text><text x="1594" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Iran</text><text x="1690" y="91" font-size="9" text-anchor="end" fill="#5d6880">38%</text><rect x="1706" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1706" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1714" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Canada</text><text x="1810" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">65%</text><text x="1714" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Algeria</text><text x="1810" y="91" font-size="9" text-anchor="end" fill="#5d6880">35%</text><rect x="1826" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1826" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1834" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Colombia</text><text x="1930" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">70%</text><text x="1834" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Türkiye</text><text x="1930" y="91" font-size="9" text-anchor="end" fill="#5d6880">30%</text><rect x="86" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="94" y="187" font-size="10.5" font-weight="400" fill="#7c89a3">Germany</text><text x="190" y="187" font-size="9" text-anchor="end" fill="#5d6880">26%</text><rect x="86" y="193" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="94" y="207" font-size="10.5" font-weight="700" fill="#7ef0b6">France</text><text x="190" y="207" font-size="9" text-anchor="end" fill="#cfe8d8">74%</text><rect x="326" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="334" y="187" font-size="10.5" font-weight="400" fill="#7c89a3">Switzerland</text><text x="430" y="187" font-size="9" text-anchor="end" fill="#5d6880">43%</text><rect x="326" y="193" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="334" y="207" font-size="10.5" font-weight="700" fill="#7ef0b6">Morocco</text><text x="430" y="207" font-size="9" text-anchor="end" fill="#cfe8d8">57%</text><rect x="566" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="574" y="187" font-size="10.5" font-weight="400" fill="#7c89a3">Portugal</text><text x="670" y="187" font-size="9" text-anchor="end" fill="#5d6880">32%</text><rect x="566" y="193" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="574" y="207" font-size="10.5" font-weight="700" fill="#7ef0b6">Spain</text><text x="670" y="207" font-size="9" text-anchor="end" fill="#cfe8d8">68%</text><rect x="806" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="806" y="172" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="814" y="187" font-size="10.5" font-weight="700" fill="#7ef0b6">USA</text><text x="910" y="187" font-size="9" text-anchor="end" fill="#cfe8d8">50%</text><text x="814" y="207" font-size="10.5" font-weight="400" fill="#7c89a3">Belgium</text><text x="910" y="207" font-size="9" text-anchor="end" fill="#5d6880">50%</text><rect x="1046" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1046" y="172" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1054" y="187" font-size="10.5" font-weight="700" fill="#7ef0b6">Brazil</text><text x="1150" y="187" font-size="9" text-anchor="end" fill="#cfe8d8">53%</text><text x="1054" y="207" font-size="10.5" font-weight="400" fill="#7c89a3">Norway</text><text x="1150" y="207" font-size="9" text-anchor="end" fill="#5d6880">47%</text><rect x="1286" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="1294" y="187" font-size="10.5" font-weight="400" fill="#7c89a3">Mexico</text><text x="1390" y="187" font-size="9" text-anchor="end" fill="#5d6880">40%</text><rect x="1286" y="193" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1294" y="207" font-size="10.5" font-weight="700" fill="#7ef0b6">England</text><text x="1390" y="207" font-size="9" text-anchor="end" fill="#cfe8d8">60%</text><rect x="1526" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1526" y="172" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1534" y="187" font-size="10.5" font-weight="700" fill="#7ef0b6">Argentina</text><text x="1630" y="187" font-size="9" text-anchor="end" fill="#cfe8d8">74%</text><text x="1534" y="207" font-size="10.5" font-weight="400" fill="#7c89a3">Australia</text><text x="1630" y="207" font-size="9" text-anchor="end" fill="#5d6880">26%</text><rect x="1766" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="1774" y="187" font-size="10.5" font-weight="400" fill="#7c89a3">Canada</text><text x="1870" y="187" font-size="9" text-anchor="end" fill="#5d6880">43%</text><rect x="1766" y="193" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1774" y="207" font-size="10.5" font-weight="700" fill="#7ef0b6">Colombia</text><text x="1870" y="207" font-size="9" text-anchor="end" fill="#cfe8d8">57%</text><rect x="206" y="286" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="206" y="288" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="214" y="303" font-size="10.5" font-weight="700" fill="#7ef0b6">France</text><text x="310" y="303" font-size="9" text-anchor="end" fill="#cfe8d8">69%</text><text x="214" y="323" font-size="10.5" font-weight="400" fill="#7c89a3">Morocco</text><text x="310" y="323" font-size="9" text-anchor="end" fill="#5d6880">31%</text><rect x="686" y="286" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="686" y="288" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="694" y="303" font-size="10.5" font-weight="700" fill="#7ef0b6">Spain</text><text x="790" y="303" font-size="9" text-anchor="end" fill="#cfe8d8">72%</text><text x="694" y="323" font-size="10.5" font-weight="400" fill="#7c89a3">USA</text><text x="790" y="323" font-size="9" text-anchor="end" fill="#5d6880">28%</text><rect x="1166" y="286" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="1174" y="303" font-size="10.5" font-weight="400" fill="#7c89a3">Brazil</text><text x="1270" y="303" font-size="9" text-anchor="end" fill="#5d6880">38%</text><rect x="1166" y="309" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1174" y="323" font-size="10.5" font-weight="700" fill="#7ef0b6">England</text><text x="1270" y="323" font-size="9" text-anchor="end" fill="#cfe8d8">62%</text><rect x="1646" y="286" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1646" y="288" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1654" y="303" font-size="10.5" font-weight="700" fill="#7ef0b6">Argentina</text><text x="1750" y="303" font-size="9" text-anchor="end" fill="#cfe8d8">66%</text><text x="1654" y="323" font-size="10.5" font-weight="400" fill="#7c89a3">Colombia</text><text x="1750" y="323" font-size="9" text-anchor="end" fill="#5d6880">34%</text><rect x="446" y="402" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="454" y="419" font-size="10.5" font-weight="400" fill="#7c89a3">France</text><text x="550" y="419" font-size="9" text-anchor="end" fill="#5d6880">38%</text><rect x="446" y="425" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="454" y="439" font-size="10.5" font-weight="700" fill="#7ef0b6">Spain</text><text x="550" y="439" font-size="9" text-anchor="end" fill="#cfe8d8">62%</text><rect x="1406" y="402" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="1414" y="419" font-size="10.5" font-weight="400" fill="#7c89a3">England</text><text x="1510" y="419" font-size="9" text-anchor="end" fill="#5d6880">33%</text><rect x="1406" y="425" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1414" y="439" font-size="10.5" font-weight="700" fill="#7ef0b6">Argentina</text><text x="1510" y="439" font-size="9" text-anchor="end" fill="#cfe8d8">67%</text><rect x="926" y="518" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="934" y="535" font-size="10.5" font-weight="400" fill="#7c89a3">Spain</text><text x="1030" y="535" font-size="9" text-anchor="end" fill="#5d6880">47%</text><rect x="926" y="541" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="934" y="555" font-size="10.5" font-weight="700" fill="#7ef0b6">Argentina</text><text x="1030" y="555" font-size="9" text-anchor="end" fill="#cfe8d8">53%</text><rect x="888" y="598" width="188" height="46" rx="10" fill="#f5c542"/><text x="982" y="619" font-size="13" font-weight="800" fill="#1a1300" text-anchor="middle">🏆 Argentina</text><text x="982" y="635" font-size="10" fill="#5a4a00" text-anchor="middle">projected champion · 21% to win</text></svg>
</div>

## Upcoming group matches — outcome probabilities

*(next match days; full list for all 72 group games in `match_probabilities.csv`)*

| Date | Grp | Match | Home win | Draw | Away win | xG | Likely score |
|------|:---:|-------|---------:|-----:|---------:|----|:----:|
| 2026-06-17 | K | Uzbekistan v Colombia | 15.0% | 25.4% | **59.7%** | 0.70–1.65 | 0-1 |
| 2026-06-17 | L | Ghana v Panama | 22.1% | 26.0% | **51.9%** | 0.98–1.63 | 1-1 |
| 2026-06-18 | A | Czech Republic v South Africa | **53.8%** | 26.4% | 19.8% | 1.60–0.87 | 1-0 |
| 2026-06-18 | A | Mexico v South Korea | **55.9%** | 24.2% | 19.9% | 1.81–0.99 | 1-1 |
| 2026-06-18 | B | Switzerland v Bosnia and Herzegovina | **70.2%** | 19.4% | 10.4% | 2.14–0.70 | 2-0 |
| 2026-06-18 | B | Canada v Qatar | **75.1%** | 17.7% | 7.2% | 2.18–0.53 | 2-0 |
| 2026-06-19 | D | Turkey v Paraguay | **40.8%** | 27.2% | 31.9% | 1.43–1.23 | 1-1 |
| 2026-06-19 | C | Scotland v Morocco | 23.1% | 26.4% | **50.5%** | 1.00–1.59 | 1-1 |
| 2026-06-19 | C | Brazil v Haiti | **78.5%** | 14.4% | 7.2% | 2.66–0.71 | 2-0 |
| 2026-06-19 | D | United States v Australia | **41.4%** | 28.2% | 30.4% | 1.36–1.13 | 1-1 |
| 2026-06-20 | F | Netherlands v Sweden | **50.2%** | 23.2% | 26.6% | 1.94–1.37 | 1-1 |
| 2026-06-20 | F | Tunisia v Japan | 15.8% | 24.3% | **59.9%** | 0.79–1.76 | 0-1 |
| 2026-06-20 | E | Germany v Ivory Coast | **52.2%** | 24.7% | 23.1% | 1.76–1.10 | 1-1 |
| 2026-06-20 | E | Ecuador v Curaçao | **83.3%** | 12.2% | 4.5% | 2.75–0.53 | 2-0 |

## Group projections

### Group A

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Mexico | 1 | 1-0-0 | 2-0 | **3** | 7.37 | 72.5% | 96.0% | 99.6% |
| South Korea | 1 | 1-0-0 | 2-1 | **3** | 5.83 | 25.2% | 86.8% | 94.8% |
| Czech Republic | 1 | 0-0-1 | 1-2 | **0** | 2.27 | 1.9% | 9.1% | 43.5% |
| South Africa | 1 | 0-0-1 | 0-2 | **0** | 1.60 | 0.4% | 8.1% | 20.1% |

### Group B

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Bosnia and Herzegovina | 1 | 0-1-0 | 1-1 | **1** | 3.09 | 8.1% | 26.3% | 54.1% |
| Canada | 1 | 0-1-0 | 1-1 | **1** | 4.90 | 47.1% | 80.0% | 90.0% |
| Qatar | 1 | 0-1-0 | 1-1 | **1** | 2.50 | 4.4% | 17.1% | 36.7% |
| Switzerland | 1 | 0-1-0 | 1-1 | **1** | 4.54 | 40.5% | 76.6% | 85.0% |

### Group C

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Scotland | 1 | 1-0-0 | 1-0 | **3** | 4.66 | 19.4% | 46.8% | 83.6% |
| Brazil | 1 | 0-1-0 | 1-1 | **1** | 5.58 | 51.1% | 81.5% | 94.9% |
| Morocco | 1 | 0-1-0 | 1-1 | **1** | 5.00 | 28.8% | 68.6% | 89.0% |
| Haiti | 1 | 0-0-1 | 0-1 | **0** | 0.92 | 0.7% | 3.1% | 7.8% |

### Group D

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| United States | 1 | 1-0-0 | 4-1 | **3** | 6.23 | 55.5% | 87.7% | 97.4% |
| Australia | 1 | 1-0-0 | 2-0 | **3** | 5.76 | 37.2% | 82.1% | 94.6% |
| Turkey | 1 | 0-0-1 | 0-2 | **0** | 2.54 | 4.6% | 16.0% | 41.2% |
| Paraguay | 1 | 0-0-1 | 1-4 | **0** | 2.38 | 2.7% | 14.2% | 34.3% |

### Group E

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Germany | 1 | 1-0-0 | 7-1 | **3** | 6.36 | 57.4% | 85.8% | 99.7% |
| Ivory Coast | 1 | 1-0-0 | 1-0 | **3** | 6.07 | 32.4% | 83.4% | 94.5% |
| Ecuador | 1 | 0-0-1 | 0-1 | **0** | 3.78 | 10.1% | 29.0% | 82.4% |
| Curaçao | 1 | 0-0-1 | 1-7 | **0** | 0.90 | 0.2% | 1.8% | 5.1% |

### Group F

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Sweden | 1 | 1-0-0 | 5-1 | **3** | 5.08 | 34.8% | 60.2% | 95.4% |
| Japan | 1 | 0-1-0 | 2-2 | **1** | 4.73 | 30.1% | 65.3% | 85.4% |
| Netherlands | 1 | 0-1-0 | 2-2 | **1** | 4.78 | 33.7% | 67.1% | 86.0% |
| Tunisia | 1 | 0-0-1 | 1-5 | **0** | 1.44 | 1.4% | 7.5% | 13.4% |

### Group G

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Iran | 1 | 0-1-0 | 2-2 | **1** | 3.50 | 22.7% | 50.9% | 62.5% |
| New Zealand | 1 | 0-1-0 | 2-2 | **1** | 2.80 | 11.2% | 31.3% | 44.7% |
| Belgium | 1 | 0-1-0 | 1-1 | **1** | 4.75 | 44.9% | 70.7% | 85.1% |
| Egypt | 1 | 0-1-0 | 1-1 | **1** | 3.89 | 21.2% | 47.1% | 69.8% |

### Group H

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Saudi Arabia | 1 | 0-1-0 | 1-1 | **1** | 2.89 | 6.3% | 24.3% | 49.9% |
| Uruguay | 1 | 0-1-0 | 1-1 | **1** | 4.35 | 33.9% | 73.1% | 84.0% |
| Cape Verde | 1 | 0-1-0 | 0-0 | **1** | 2.60 | 4.0% | 16.8% | 39.7% |
| Spain | 1 | 0-1-0 | 0-0 | **1** | 5.23 | 55.8% | 85.8% | 92.8% |

### Group I

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Norway | 1 | 1-0-0 | 4-1 | **3** | 5.47 | 25.1% | 79.1% | 96.9% |
| France | 1 | 1-0-0 | 3-1 | **3** | 7.39 | 72.4% | 97.0% | 99.3% |
| Senegal | 1 | 0-0-1 | 1-3 | **0** | 3.06 | 1.9% | 21.6% | 57.4% |
| Iraq | 1 | 0-0-1 | 1-4 | **0** | 1.17 | 0.6% | 2.4% | 10.8% |

### Group J

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Argentina | 1 | 1-0-0 | 3-0 | **3** | 7.73 | 82.2% | 99.0% | 99.8% |
| Austria | 1 | 1-0-0 | 3-1 | **3** | 5.31 | 16.4% | 76.4% | 94.6% |
| Jordan | 1 | 0-0-1 | 1-3 | **0** | 1.05 | 0.3% | 1.6% | 11.0% |
| Algeria | 1 | 0-0-1 | 0-3 | **0** | 3.05 | 1.0% | 23.0% | 51.7% |

### Group K

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| DR Congo | 1 | 0-1-0 | 1-1 | **1** | 2.99 | 8.0% | 28.8% | 50.7% |
| Portugal | 1 | 0-1-0 | 1-1 | **1** | 4.28 | 26.8% | 66.4% | 80.9% |
| Colombia | 0 | 0-0-0 | 0-0 | **0** | 5.78 | 56.2% | 79.9% | 90.5% |
| Uzbekistan | 0 | 0-0-0 | 0-0 | **0** | 2.67 | 9.0% | 24.9% | 42.6% |

### Group L

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| England | 1 | 1-0-0 | 4-2 | **3** | 7.99 | 91.6% | 99.0% | 99.8% |
| Ghana | 0 | 0-0-0 | 0-0 | **0** | 1.80 | 1.2% | 12.5% | 24.6% |
| Panama | 0 | 0-0-0 | 0-0 | **0** | 3.27 | 5.4% | 34.1% | 57.5% |
| Croatia | 1 | 0-0-1 | 2-4 | **0** | 3.89 | 1.8% | 54.4% | 74.8% |

*\*Advance = top two or one of the eight best third-placed teams.*

## Most likely knockout bracket

Each tie shows the most probable pairing given projected group finishes, the chance the named winner goes through **in that pairing**, and how often the exact pairing occurred across all simulations.

### Round of 32

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 73 | 2026-06-28 | SoFi Stadium, Los Angeles | South Korea v Switzerland | **Switzerland** | 63.6% | 22.2% |
| 74 | 2026-06-29 | Gillette Stadium, Boston | Germany v Scotland | **Germany** | 57.0% | 5.9% |
| 75 | 2026-06-29 | Estadio BBVA, Monterrey | Sweden v Morocco | **Morocco** | 68.5% | 13.8% |
| 76 | 2026-06-29 | NRG Stadium, Houston | Brazil v Japan | **Brazil** | 56.9% | 18.0% |
| 77 | 2026-06-30 | MetLife Stadium, New York/New Jersey | France v Saudi Arabia | **France** | 81.0% | 6.7% |
| 78 | 2026-06-30 | AT&T Stadium, Dallas | Ivory Coast v Norway | **Norway** | 66.1% | 27.6% |
| 79 | 2026-06-30 | Estadio Azteca, Mexico City | Mexico v Ecuador | **Mexico** | 71.7% | 16.3% |
| 80 | 2026-07-01 | Mercedes-Benz Stadium, Atlanta | England v Senegal | **England** | 73.2% | 3.5% |
| 81 | 2026-07-01 | Levi's Stadium, San Francisco Bay Area | United States v Bosnia and Herzegovina | **United States** | 83.8% | 11.6% |
| 82 | 2026-07-01 | Lumen Field, Seattle | Belgium v Czech Republic | **Belgium** | 75.5% | 13.8% |
| 83 | 2026-07-02 | BMO Field, Toronto | Portugal v Croatia | **Portugal** | 63.8% | 20.9% |
| 84 | 2026-07-02 | SoFi Stadium, Los Angeles | Spain v Austria | **Spain** | 74.4% | 33.4% |
| 85 | 2026-07-02 | BC Place, Vancouver | Canada v Algeria | **Canada** | 64.6% | 3.5% |
| 86 | 2026-07-03 | Hard Rock Stadium, Miami | Argentina v Uruguay | **Argentina** | 78.4% | 32.2% |
| 87 | 2026-07-03 | Arrowhead Stadium, Kansas City | Colombia v Turkey | **Colombia** | 70.4% | 5.0% |
| 88 | 2026-07-03 | AT&T Stadium, Dallas | Australia v Iran | **Australia** | 61.6% | 12.5% |

### Round of 16

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 89 | 2026-07-04 | Lincoln Financial Field, Philadelphia | Germany v France | **France** | 73.6% | 17.7% |
| 90 | 2026-07-04 | NRG Stadium, Houston | Switzerland v Morocco | **Morocco** | 57.2% | 4.9% |
| 91 | 2026-07-05 | MetLife Stadium, New York/New Jersey | Brazil v Norway | **Brazil** | 53.0% | 10.4% |
| 92 | 2026-07-05 | Estadio Azteca, Mexico City | Mexico v England | **England** | 60.3% | 34.2% |
| 93 | 2026-07-06 | AT&T Stadium, Dallas | Portugal v Spain | **Spain** | 67.8% | 10.4% |
| 94 | 2026-07-06 | Lumen Field, Seattle | United States v Belgium | **United States** | 50.3% | 11.6% |
| 95 | 2026-07-07 | Mercedes-Benz Stadium, Atlanta | Argentina v Australia | **Argentina** | 73.5% | 17.0% |
| 96 | 2026-07-07 | BC Place, Vancouver | Canada v Colombia | **Colombia** | 57.2% | 11.8% |

### Quarter-finals

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 97 | 2026-07-09 | Gillette Stadium, Boston | France v Morocco | **France** | 68.6% | 5.1% |
| 98 | 2026-07-10 | SoFi Stadium, Los Angeles | Spain v United States | **Spain** | 72.3% | 6.7% |
| 99 | 2026-07-11 | Hard Rock Stadium, Miami | Brazil v England | **England** | 62.0% | 7.9% |
| 100 | 2026-07-11 | Arrowhead Stadium, Kansas City | Argentina v Colombia | **Argentina** | 65.8% | 12.3% |

### Semi-finals

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 101 | 2026-07-14 | AT&T Stadium, Dallas | France v Spain | **Spain** | 61.5% | 5.4% |
| 102 | 2026-07-15 | Mercedes-Benz Stadium, Atlanta | England v Argentina | **Argentina** | 67.3% | 10.5% |

### Final

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 104 | 2026-07-19 | MetLife Stadium, East Rutherford | Spain v Argentina | **Argentina** | 53.2% | 4.6% |

**Projected champion: Argentina** (overall title probability 20.5%; the single most likely path above is itself only one of many ways the tournament can unfold).

## How to read this

- All figures are probabilities, not certainties — a 65% favourite loses about one such match in three.
- `xPts` = expected group points; `xG` = expected goals from the Poisson model.
- Predictions refresh after every match day: run `python -m worldcup.run all` to pull new results, re-rate teams, and re-simulate.
- Machine-readable outputs: `match_probabilities.csv`, `tournament_projections.csv`. Past reports in `outputs/archive/`.

## Model scorecard

**10 of 22 match outcomes called correctly** (the model's own probabilities expected ≈12.9 of 22) · exact scoreline predicted 2/22 · average probability placed on what actually happened: **39.7%** (33.3% = guessing).

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
| Austria v Jordan | Austria win (47.0%) | 1-1 | 3-1 | ✅ | — |
| Argentina v Algeria | Argentina win (68.0%) | 2-0 | 3-0 | ✅ | — |
| France v Senegal | France win (59.1%) | 1-0 | 3-1 | ✅ | — |
| Iraq v Norway | Norway win (59.1%) | 0-1 | 1-4 | ✅ | — |
| Portugal v DR Congo | Portugal win (70.6%) | 2-0 | 1-1 | ❌ | — |
| England v Croatia | England win (56.9%) | 1-0 | 4-2 | ✅ | — |

**Calibration vs benchmarks** (the 9 graded games with bookmaker prices on file) — log-loss, lower is better. This is the honest test: is the model bad, or were the games hard for everyone?

| Forecaster | Log-loss |
|------------|---------:|
| **This model** | **1.193** |
| Sky Bet (de-vigged) | 1.156 |
| Coin-flip (33/33/33) | 1.099 |

The model is **essentially level with the market** (+0.037 log-loss). Note both the model **and** the bookmaker scored worse than a coin-flip here — with this many draws and upsets, the slate was close to unforecastable for anyone, which is the real reason the hit-rate looks poor.


*Predictions are frozen at the last run before each result arrives, then graded — the scorecard never grades a model that has already seen the answer.*

