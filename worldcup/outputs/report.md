# FIFA World Cup 2026 — ML Prediction Report

*Generated 2026-06-15 · data through **2026-06-14** · 50,000 Monte Carlo simulations · 12/72 group matches played*

Probabilities come from a gradient-boosted Poisson goal model (Elo strength + rolling form + venue/importance features) trained on 30,784 internationals, simulated through the official 2026 bracket and tiebreaker rules.

*Rolling validation (7,966 matches, 2018–2026): RPS 0.1687 vs Elo-baseline 0.1711; log-loss 0.8652 vs 0.8809.*

## Title favourites

| # | Team | Group | Champion | Δ vs 2026-06-14 | Final | Semi-final | Quarter-final | Rd of 16 |
|---|------|:-----:|---------:|-------:|------:|-----------:|--------------:|---------:|
| 1 | Spain | H | **18.4%** | -1.5 | 28.0% | 40.1% | 53.6% | 71.7% |
| 2 | Argentina | J | **17.2%** | -1.0 | 26.3% | 37.5% | 50.9% | 66.6% |
| 3 | England | L | **8.4%** | -0.1 | 15.0% | 25.7% | 40.3% | 68.8% |
| 4 | France | I | **8.3%** | +1.0 | 15.1% | 28.4% | 46.6% | 67.2% |
| 5 | Brazil | C | **6.1%** | – | 12.0% | 23.7% | 39.5% | 60.9% |
| 6 | Colombia | K | **4.9%** | +0.4 | 9.9% | 17.7% | 32.6% | 59.2% |
| 7 | Portugal | K | **4.4%** | +0.5 | 9.3% | 17.2% | 32.8% | 60.3% |
| 8 | Netherlands | F | **3.1%** | +0.5 | 7.0% | 15.5% | 29.1% | 48.7% |
| 9 | Mexico | A | **3.0%** | -0.8 | 7.4% | 17.7% | 36.7% | 66.4% |
| 10 | Belgium | G | **2.9%** | +0.2 | 7.0% | 13.3% | 30.4% | 56.7% |
| 11 | Japan | F | **2.8%** | +0.1 | 6.2% | 13.5% | 25.8% | 45.6% |
| 12 | Uruguay | H | **2.1%** | +0.5 | 5.3% | 11.1% | 21.1% | 39.5% |
| 13 | Morocco | C | **2.1%** | – | 5.3% | 12.2% | 25.3% | 45.7% |
| 14 | Norway | I | **2.1%** | -0.1 | 4.9% | 12.1% | 25.2% | 46.5% |
| 15 | Germany | E | **2.0%** | -0.3 | 4.8% | 11.9% | 25.1% | 55.1% |

## Biggest movers since last run (data through 2026-06-14)

| Team | Δ Champion | Δ Rd of 16 | Champion now |
|------|----------:|-----------:|-------------:|
| France | +1.0 | +2.0 | 8.3% |
| Uruguay | +0.5 | +2.3 | 2.1% |
| Portugal | +0.5 | +0.3 | 4.4% |
| Netherlands | +0.5 | – | 3.1% |
| Colombia | +0.4 | +0.7 | 4.9% |
| Mexico | -0.8 | -2.5 | 3.0% |
| Argentina | -1.0 | -1.5 | 17.2% |
| Spain | -1.5 | – | 18.4% |

*Δ values in probability points. Full run-by-run series in `outputs/history.csv`.*

## Path to the final

The model's single most likely knockout bracket — all 32 projected round-of-32 teams and every unplayed tie, each line carrying the projected winner down to the next round until they converge on the champion. Percentages are each side's chance of advancing from that tie.

<div style="overflow-x:auto; margin:1rem 0;">
<svg viewBox="0 0 1964 662" width="100%" preserveAspectRatio="xMidYMin meet" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica,Arial,sans-serif"><path d="M82,98 C82,134 142,134 142,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M202,98 C202,134 142,134 142,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M322,98 C322,134 382,134 382,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M442,98 C442,134 382,134 382,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M562,98 C562,134 622,134 622,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M682,98 C682,134 622,134 622,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M802,98 C802,134 862,134 862,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M922,98 C922,134 862,134 862,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1042,98 C1042,134 1102,134 1102,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1162,98 C1162,134 1102,134 1102,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1282,98 C1282,134 1342,134 1342,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1402,98 C1402,134 1342,134 1342,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1522,98 C1522,134 1582,134 1582,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1642,98 C1642,134 1582,134 1582,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1762,98 C1762,134 1822,134 1822,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1882,98 C1882,134 1822,134 1822,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M142,214 C142,250 262,250 262,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M382,214 C382,250 262,250 262,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M622,214 C622,250 742,250 742,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M862,214 C862,250 742,250 742,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1102,214 C1102,250 1222,250 1222,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1342,214 C1342,250 1222,250 1222,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1582,214 C1582,250 1702,250 1702,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1822,214 C1822,250 1702,250 1702,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M262,330 C262,366 502,366 502,402" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M742,330 C742,366 502,366 502,402" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1222,330 C1222,366 1462,366 1462,402" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1702,330 C1702,366 1462,366 1462,402" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M502,446 C502,482 982,482 982,518" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1462,446 C1462,482 982,482 982,518" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M982,562 C982,580 982,580 982,598" fill="none" stroke="#33436b" stroke-width="1.5"/><text x="11" y="76" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 11 76)" text-anchor="middle">ROUND OF 32</text><text x="11" y="192" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 11 192)" text-anchor="middle">ROUND OF 16</text><text x="11" y="308" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 11 308)" text-anchor="middle">QUARTER-FINALS</text><text x="11" y="424" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 11 424)" text-anchor="middle">SEMI-FINALS</text><text x="11" y="540" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 11 540)" text-anchor="middle">FINAL</text><rect x="26" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="26" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="34" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Germany</text><text x="130" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">58%</text><text x="34" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Scotland</text><text x="130" y="91" font-size="9" text-anchor="end" fill="#5d6880">42%</text><rect x="146" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="146" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="154" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">France</text><text x="250" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">73%</text><text x="154" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Türkiye</text><text x="250" y="91" font-size="9" text-anchor="end" fill="#5d6880">27%</text><rect x="266" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="274" y="71" font-size="10.5" font-weight="400" fill="#7c89a3">S. Korea</text><text x="370" y="71" font-size="9" text-anchor="end" fill="#5d6880">37%</text><rect x="266" y="77" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="274" y="91" font-size="10.5" font-weight="700" fill="#7ef0b6">Switzerland</text><text x="370" y="91" font-size="9" text-anchor="end" fill="#cfe8d8">63%</text><rect x="386" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="386" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="394" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Netherlands</text><text x="490" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">58%</text><text x="394" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Morocco</text><text x="490" y="91" font-size="9" text-anchor="end" fill="#5d6880">42%</text><rect x="506" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="506" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="514" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Colombia</text><text x="610" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">65%</text><text x="514" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Croatia</text><text x="610" y="91" font-size="9" text-anchor="end" fill="#5d6880">35%</text><rect x="626" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="626" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="634" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Spain</text><text x="730" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">78%</text><text x="634" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Austria</text><text x="730" y="91" font-size="9" text-anchor="end" fill="#5d6880">22%</text><rect x="746" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="746" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="754" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">USA</text><text x="850" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">83%</text><text x="754" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Bosnia</text><text x="850" y="91" font-size="9" text-anchor="end" fill="#5d6880">17%</text><rect x="866" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="866" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="874" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Belgium</text><text x="970" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">73%</text><text x="874" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Czechia</text><text x="970" y="91" font-size="9" text-anchor="end" fill="#5d6880">27%</text><rect x="986" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="986" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="994" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Brazil</text><text x="1090" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">60%</text><text x="994" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Japan</text><text x="1090" y="91" font-size="9" text-anchor="end" fill="#5d6880">40%</text><rect x="1106" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="1114" y="71" font-size="10.5" font-weight="400" fill="#7c89a3">Ivory Coast</text><text x="1210" y="71" font-size="9" text-anchor="end" fill="#5d6880">36%</text><rect x="1106" y="77" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1114" y="91" font-size="10.5" font-weight="700" fill="#7ef0b6">Norway</text><text x="1210" y="91" font-size="9" text-anchor="end" fill="#cfe8d8">64%</text><rect x="1226" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1226" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1234" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Mexico</text><text x="1330" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">65%</text><text x="1234" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Ecuador</text><text x="1330" y="91" font-size="9" text-anchor="end" fill="#5d6880">35%</text><rect x="1346" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1346" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1354" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">England</text><text x="1450" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">73%</text><text x="1354" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Senegal</text><text x="1450" y="91" font-size="9" text-anchor="end" fill="#5d6880">27%</text><rect x="1466" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1466" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1474" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Argentina</text><text x="1570" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">78%</text><text x="1474" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Uruguay</text><text x="1570" y="91" font-size="9" text-anchor="end" fill="#5d6880">22%</text><rect x="1586" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1586" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1594" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Australia</text><text x="1690" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">61%</text><text x="1594" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Iran</text><text x="1690" y="91" font-size="9" text-anchor="end" fill="#5d6880">39%</text><rect x="1706" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1706" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1714" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Canada</text><text x="1810" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">60%</text><text x="1714" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Sweden</text><text x="1810" y="91" font-size="9" text-anchor="end" fill="#5d6880">40%</text><rect x="1826" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1826" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1834" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Portugal</text><text x="1930" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">77%</text><text x="1834" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Panama</text><text x="1930" y="91" font-size="9" text-anchor="end" fill="#5d6880">23%</text><rect x="86" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="94" y="187" font-size="10.5" font-weight="400" fill="#7c89a3">Germany</text><text x="190" y="187" font-size="9" text-anchor="end" fill="#5d6880">24%</text><rect x="86" y="193" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="94" y="207" font-size="10.5" font-weight="700" fill="#7ef0b6">France</text><text x="190" y="207" font-size="9" text-anchor="end" fill="#cfe8d8">76%</text><rect x="326" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="334" y="187" font-size="10.5" font-weight="400" fill="#7c89a3">Switzerland</text><text x="430" y="187" font-size="9" text-anchor="end" fill="#5d6880">33%</text><rect x="326" y="193" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="334" y="207" font-size="10.5" font-weight="700" fill="#7ef0b6">Netherlands</text><text x="430" y="207" font-size="9" text-anchor="end" fill="#cfe8d8">67%</text><rect x="566" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="574" y="187" font-size="10.5" font-weight="400" fill="#7c89a3">Colombia</text><text x="670" y="187" font-size="9" text-anchor="end" fill="#5d6880">27%</text><rect x="566" y="193" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="574" y="207" font-size="10.5" font-weight="700" fill="#7ef0b6">Spain</text><text x="670" y="207" font-size="9" text-anchor="end" fill="#cfe8d8">73%</text><rect x="806" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="814" y="187" font-size="10.5" font-weight="400" fill="#7c89a3">USA</text><text x="910" y="187" font-size="9" text-anchor="end" fill="#5d6880">39%</text><rect x="806" y="193" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="814" y="207" font-size="10.5" font-weight="700" fill="#7ef0b6">Belgium</text><text x="910" y="207" font-size="9" text-anchor="end" fill="#cfe8d8">61%</text><rect x="1046" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1046" y="172" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1054" y="187" font-size="10.5" font-weight="700" fill="#7ef0b6">Brazil</text><text x="1150" y="187" font-size="9" text-anchor="end" fill="#cfe8d8">57%</text><text x="1054" y="207" font-size="10.5" font-weight="400" fill="#7c89a3">Norway</text><text x="1150" y="207" font-size="9" text-anchor="end" fill="#5d6880">43%</text><rect x="1286" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1286" y="172" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1294" y="187" font-size="10.5" font-weight="700" fill="#7ef0b6">Mexico</text><text x="1390" y="187" font-size="9" text-anchor="end" fill="#cfe8d8">51%</text><text x="1294" y="207" font-size="10.5" font-weight="400" fill="#7c89a3">England</text><text x="1390" y="207" font-size="9" text-anchor="end" fill="#5d6880">49%</text><rect x="1526" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1526" y="172" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1534" y="187" font-size="10.5" font-weight="700" fill="#7ef0b6">Argentina</text><text x="1630" y="187" font-size="9" text-anchor="end" fill="#cfe8d8">75%</text><text x="1534" y="207" font-size="10.5" font-weight="400" fill="#7c89a3">Australia</text><text x="1630" y="207" font-size="9" text-anchor="end" fill="#5d6880">25%</text><rect x="1766" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="1774" y="187" font-size="10.5" font-weight="400" fill="#7c89a3">Canada</text><text x="1870" y="187" font-size="9" text-anchor="end" fill="#5d6880">44%</text><rect x="1766" y="193" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1774" y="207" font-size="10.5" font-weight="700" fill="#7ef0b6">Portugal</text><text x="1870" y="207" font-size="9" text-anchor="end" fill="#cfe8d8">56%</text><rect x="206" y="286" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="206" y="288" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="214" y="303" font-size="10.5" font-weight="700" fill="#7ef0b6">France</text><text x="310" y="303" font-size="9" text-anchor="end" fill="#cfe8d8">50%</text><text x="214" y="323" font-size="10.5" font-weight="400" fill="#7c89a3">Netherlands</text><text x="310" y="323" font-size="9" text-anchor="end" fill="#5d6880">50%</text><rect x="686" y="286" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="686" y="288" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="694" y="303" font-size="10.5" font-weight="700" fill="#7ef0b6">Spain</text><text x="790" y="303" font-size="9" text-anchor="end" fill="#cfe8d8">69%</text><text x="694" y="323" font-size="10.5" font-weight="400" fill="#7c89a3">Belgium</text><text x="790" y="323" font-size="9" text-anchor="end" fill="#5d6880">31%</text><rect x="1166" y="286" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1166" y="288" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1174" y="303" font-size="10.5" font-weight="700" fill="#7ef0b6">Brazil</text><text x="1270" y="303" font-size="9" text-anchor="end" fill="#cfe8d8">67%</text><text x="1174" y="323" font-size="10.5" font-weight="400" fill="#7c89a3">Mexico</text><text x="1270" y="323" font-size="9" text-anchor="end" fill="#5d6880">33%</text><rect x="1646" y="286" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1646" y="288" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1654" y="303" font-size="10.5" font-weight="700" fill="#7ef0b6">Argentina</text><text x="1750" y="303" font-size="9" text-anchor="end" fill="#cfe8d8">68%</text><text x="1654" y="323" font-size="10.5" font-weight="400" fill="#7c89a3">Portugal</text><text x="1750" y="323" font-size="9" text-anchor="end" fill="#5d6880">32%</text><rect x="446" y="402" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="454" y="419" font-size="10.5" font-weight="400" fill="#7c89a3">France</text><text x="550" y="419" font-size="9" text-anchor="end" fill="#5d6880">36%</text><rect x="446" y="425" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="454" y="439" font-size="10.5" font-weight="700" fill="#7ef0b6">Spain</text><text x="550" y="439" font-size="9" text-anchor="end" fill="#cfe8d8">64%</text><rect x="1406" y="402" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="1414" y="419" font-size="10.5" font-weight="400" fill="#7c89a3">Brazil</text><text x="1510" y="419" font-size="9" text-anchor="end" fill="#5d6880">33%</text><rect x="1406" y="425" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1414" y="439" font-size="10.5" font-weight="700" fill="#7ef0b6">Argentina</text><text x="1510" y="439" font-size="9" text-anchor="end" fill="#cfe8d8">67%</text><rect x="926" y="518" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="926" y="520" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="934" y="535" font-size="10.5" font-weight="700" fill="#7ef0b6">Spain</text><text x="1030" y="535" font-size="9" text-anchor="end" fill="#cfe8d8">54%</text><text x="934" y="555" font-size="10.5" font-weight="400" fill="#7c89a3">Argentina</text><text x="1030" y="555" font-size="9" text-anchor="end" fill="#5d6880">46%</text><rect x="888" y="598" width="188" height="46" rx="10" fill="#f5c542"/><text x="982" y="619" font-size="13" font-weight="800" fill="#1a1300" text-anchor="middle">🏆 Spain</text><text x="982" y="635" font-size="10" fill="#5a4a00" text-anchor="middle">projected champion · 18% to win</text></svg>
</div>

## Upcoming group matches — outcome probabilities

*(next match days; full list for all 72 group games in `match_probabilities.csv`)*

| Date | Grp | Match | Home win | Draw | Away win | xG | Likely score |
|------|:---:|-------|---------:|-----:|---------:|----|:----:|
| 2026-06-15 | G | Belgium v Egypt | **57.8%** | 24.0% | 18.1% | 1.81–0.91 | 1-1 |
| 2026-06-15 | G | Iran v New Zealand | **55.2%** | 26.0% | 18.8% | 1.62–0.84 | 1-0 |
| 2026-06-15 | H | Spain v Cape Verde | **90.5%** | 7.0% | 2.4% | 3.59–0.55 | 3-0 |
| 2026-06-15 | H | Saudi Arabia v Uruguay | 13.8% | 24.8% | **61.4%** | 0.66–1.68 | 0-1 |
| 2026-06-16 | J | Austria v Jordan | **51.6%** | 25.4% | 22.9% | 1.68–1.04 | 1-1 |
| 2026-06-16 | J | Argentina v Algeria | **63.5%** | 23.5% | 12.9% | 1.78–0.67 | 1-0 |
| 2026-06-16 | I | France v Senegal | **57.8%** | 24.7% | 17.5% | 1.73–0.84 | 1-0 |
| 2026-06-16 | I | Iraq v Norway | 15.5% | 26.0% | **58.5%** | 0.70–1.60 | 0-1 |
| 2026-06-17 | K | Portugal v DR Congo | **68.0%** | 20.2% | 11.8% | 2.09–0.75 | 2-0 |
| 2026-06-17 | K | Uzbekistan v Colombia | 14.2% | 25.1% | **60.7%** | 0.67–1.66 | 0-1 |
| 2026-06-17 | L | England v Croatia | **58.8%** | 23.5% | 17.7% | 1.86–0.92 | 1-1 |
| 2026-06-17 | L | Ghana v Panama | 23.0% | 25.5% | **51.4%** | 1.04–1.67 | 1-1 |
| 2026-06-18 | A | Czech Republic v South Africa | **53.8%** | 26.0% | 20.2% | 1.62–0.90 | 1-0 |
| 2026-06-18 | A | Mexico v South Korea | **51.2%** | 25.4% | 23.4% | 1.69–1.07 | 1-1 |
| 2026-06-18 | B | Switzerland v Bosnia and Herzegovina | **69.5%** | 19.4% | 11.2% | 2.18–0.76 | 2-0 |
| 2026-06-18 | B | Canada v Qatar | **74.1%** | 17.9% | 8.0% | 2.20–0.58 | 2-0 |

## Group projections

### Group A

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Mexico | 1 | 1-0-0 | 2-0 | **3** | 7.18 | 67.6% | 94.8% | 99.4% |
| South Korea | 1 | 1-0-0 | 2-1 | **3** | 6.02 | 30.0% | 88.1% | 95.5% |
| Czech Republic | 1 | 0-0-1 | 1-2 | **0** | 2.32 | 1.9% | 9.9% | 44.5% |
| South Africa | 1 | 0-0-1 | 0-2 | **0** | 1.55 | 0.4% | 7.1% | 18.9% |

### Group B

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Bosnia and Herzegovina | 1 | 0-1-0 | 1-1 | **1** | 3.13 | 8.7% | 27.5% | 55.1% |
| Canada | 1 | 0-1-0 | 1-1 | **1** | 4.86 | 45.9% | 79.0% | 89.1% |
| Qatar | 1 | 0-1-0 | 1-1 | **1** | 2.51 | 4.6% | 17.3% | 36.4% |
| Switzerland | 1 | 0-1-0 | 1-1 | **1** | 4.53 | 40.8% | 76.2% | 84.3% |

### Group C

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Scotland | 1 | 1-0-0 | 1-0 | **3** | 4.73 | 19.8% | 47.2% | 84.3% |
| Brazil | 1 | 0-1-0 | 1-1 | **1** | 5.59 | 49.1% | 80.9% | 95.4% |
| Morocco | 1 | 0-1-0 | 1-1 | **1** | 5.10 | 30.7% | 69.8% | 90.9% |
| Haiti | 1 | 0-0-1 | 0-1 | **0** | 0.75 | 0.4% | 2.1% | 5.7% |

### Group D

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| United States | 1 | 1-0-0 | 4-1 | **3** | 5.95 | 49.9% | 84.5% | 96.4% |
| Australia | 1 | 1-0-0 | 2-0 | **3** | 5.85 | 41.6% | 82.5% | 94.7% |
| Turkey | 1 | 0-0-1 | 0-2 | **0** | 2.69 | 5.1% | 18.6% | 44.2% |
| Paraguay | 1 | 0-0-1 | 1-4 | **0** | 2.40 | 3.3% | 14.4% | 34.0% |

### Group E

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Germany | 1 | 1-0-0 | 7-1 | **3** | 6.31 | 56.7% | 85.4% | 99.6% |
| Ivory Coast | 1 | 1-0-0 | 1-0 | **3** | 6.22 | 34.3% | 85.9% | 95.8% |
| Ecuador | 1 | 0-0-1 | 0-1 | **0** | 3.69 | 8.8% | 26.7% | 80.0% |
| Curaçao | 1 | 0-0-1 | 1-7 | **0** | 0.86 | 0.2% | 1.9% | 4.8% |

### Group F

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Sweden | 1 | 1-0-0 | 5-1 | **3** | 5.10 | 33.0% | 59.4% | 96.2% |
| Japan | 1 | 0-1-0 | 2-2 | **1** | 4.74 | 28.3% | 63.8% | 85.9% |
| Netherlands | 1 | 0-1-0 | 2-2 | **1** | 5.01 | 37.7% | 71.3% | 88.8% |
| Tunisia | 1 | 0-0-1 | 1-5 | **0** | 1.22 | 0.9% | 5.4% | 10.0% |

### Group G

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| Belgium | 5.68 | 50.3% | 77.1% | 89.1% |
| Iran | 4.48 | 26.5% | 58.2% | 76.1% |
| Egypt | 3.36 | 13.3% | 36.6% | 55.9% |
| New Zealand | 2.91 | 9.9% | 28.1% | 46.3% |

### Group H

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| Spain | 7.21 | 72.6% | 95.5% | 99.0% |
| Uruguay | 5.37 | 23.9% | 79.3% | 91.1% |
| Saudi Arabia | 2.55 | 2.7% | 17.6% | 40.3% |
| Cape Verde | 1.67 | 0.8% | 7.6% | 18.9% |

### Group I

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| France | 6.33 | 60.3% | 85.4% | 94.5% |
| Norway | 4.52 | 22.3% | 59.1% | 78.2% |
| Senegal | 3.79 | 14.0% | 42.1% | 66.6% |
| Iraq | 1.93 | 3.3% | 13.3% | 25.8% |

### Group J

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| Argentina | 6.69 | 69.0% | 89.8% | 96.5% |
| Austria | 3.93 | 15.2% | 48.9% | 68.7% |
| Algeria | 3.60 | 11.7% | 41.7% | 62.7% |
| Jordan | 2.31 | 4.2% | 19.6% | 34.7% |

### Group K

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| Portugal | 5.74 | 45.5% | 79.9% | 91.5% |
| Colombia | 5.56 | 42.3% | 77.5% | 89.7% |
| Uzbekistan | 2.74 | 6.8% | 23.1% | 43.8% |
| DR Congo | 2.46 | 5.4% | 19.5% | 37.3% |

### Group L

| Team | xPts | Win grp | Top 2 | Advance* |
|------|-----:|--------:|------:|--------:|
| England | 6.72 | 64.9% | 89.6% | 97.2% |
| Croatia | 4.90 | 23.0% | 65.7% | 86.2% |
| Panama | 3.57 | 10.8% | 37.0% | 61.9% |
| Ghana | 1.55 | 1.3% | 7.7% | 18.1% |

*\*Advance = top two or one of the eight best third-placed teams.*

## Most likely knockout bracket

Each tie shows the most probable pairing given projected group finishes, the chance the named winner goes through **in that pairing**, and how often the exact pairing occurred across all simulations.

### Round of 32

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 73 | 2026-06-28 | SoFi Stadium, Los Angeles | South Korea v Switzerland | **Switzerland** | 62.9% | 20.7% |
| 74 | 2026-06-29 | Gillette Stadium, Boston | Germany v Scotland | **Germany** | 58.2% | 5.4% |
| 75 | 2026-06-29 | Estadio BBVA, Monterrey | Netherlands v Morocco | **Netherlands** | 58.2% | 14.7% |
| 76 | 2026-06-29 | NRG Stadium, Houston | Brazil v Japan | **Brazil** | 60.3% | 17.3% |
| 77 | 2026-06-30 | MetLife Stadium, New York/New Jersey | France v Turkey | **France** | 72.8% | 6.7% |
| 78 | 2026-06-30 | AT&T Stadium, Dallas | Ivory Coast v Norway | **Norway** | 64.5% | 18.9% |
| 79 | 2026-06-30 | Estadio Azteca, Mexico City | Mexico v Ecuador | **Mexico** | 64.9% | 15.4% |
| 80 | 2026-07-01 | Mercedes-Benz Stadium, Atlanta | England v Senegal | **England** | 73.0% | 1.9% |
| 81 | 2026-07-01 | Levi's Stadium, San Francisco Bay Area | United States v Bosnia and Herzegovina | **United States** | 83.2% | 10.4% |
| 82 | 2026-07-01 | Lumen Field, Seattle | Belgium v Czech Republic | **Belgium** | 73.3% | 15.6% |
| 83 | 2026-07-02 | BMO Field, Toronto | Colombia v Croatia | **Colombia** | 65.0% | 14.9% |
| 84 | 2026-07-02 | SoFi Stadium, Los Angeles | Spain v Austria | **Spain** | 78.2% | 24.4% |
| 85 | 2026-07-02 | BC Place, Vancouver | Canada v Sweden | **Canada** | 59.7% | 4.1% |
| 86 | 2026-07-03 | Hard Rock Stadium, Miami | Argentina v Uruguay | **Argentina** | 78.2% | 38.2% |
| 87 | 2026-07-03 | Arrowhead Stadium, Kansas City | Portugal v Panama | **Portugal** | 76.8% | 11.2% |
| 88 | 2026-07-03 | AT&T Stadium, Dallas | Australia v Iran | **Australia** | 60.8% | 13.0% |

### Round of 16

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 89 | 2026-07-04 | Lincoln Financial Field, Philadelphia | Germany v France | **France** | 75.7% | 14.4% |
| 90 | 2026-07-04 | NRG Stadium, Houston | Switzerland v Netherlands | **Netherlands** | 67.1% | 4.4% |
| 91 | 2026-07-05 | MetLife Stadium, New York/New Jersey | Brazil v Norway | **Brazil** | 57.2% | 6.8% |
| 92 | 2026-07-05 | Estadio Azteca, Mexico City | Mexico v England | **Mexico** | 50.7% | 22.1% |
| 93 | 2026-07-06 | AT&T Stadium, Dallas | Colombia v Spain | **Spain** | 73.3% | 12.3% |
| 94 | 2026-07-06 | Lumen Field, Seattle | United States v Belgium | **Belgium** | 61.5% | 11.3% |
| 95 | 2026-07-07 | Mercedes-Benz Stadium, Atlanta | Argentina v Australia | **Argentina** | 74.8% | 12.6% |
| 96 | 2026-07-07 | BC Place, Vancouver | Canada v Portugal | **Portugal** | 55.8% | 8.9% |

### Quarter-finals

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 97 | 2026-07-09 | Gillette Stadium, Boston | France v Netherlands | **France** | 50.4% | 4.2% |
| 98 | 2026-07-10 | SoFi Stadium, Los Angeles | Spain v Belgium | **Spain** | 68.9% | 8.1% |
| 99 | 2026-07-11 | Hard Rock Stadium, Miami | Brazil v Mexico | **Brazil** | 66.9% | 5.0% |
| 100 | 2026-07-11 | Arrowhead Stadium, Kansas City | Argentina v Portugal | **Argentina** | 68.1% | 8.0% |

### Semi-finals

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 101 | 2026-07-14 | AT&T Stadium, Dallas | France v Spain | **Spain** | 63.5% | 5.9% |
| 102 | 2026-07-15 | Mercedes-Benz Stadium, Atlanta | Brazil v Argentina | **Argentina** | 66.7% | 3.3% |

### Final

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 104 | 2026-07-19 | MetLife Stadium, East Rutherford | Spain v Argentina | **Spain** | 54.1% | 5.6% |

**Projected champion: Spain** (overall title probability 18.4%; the single most likely path above is itself only one of many ways the tournament can unfold).

## How to read this

- All figures are probabilities, not certainties — a 65% favourite loses about one such match in three.
- `xPts` = expected group points; `xG` = expected goals from the Poisson model.
- Predictions refresh after every match day: run `python -m worldcup.run all` to pull new results, re-rate teams, and re-simulate.
- Machine-readable outputs: `match_probabilities.csv`, `tournament_projections.csv`. Past reports in `outputs/archive/`.

## Model scorecard

**5 of 12 match outcomes called correctly** (the model's own probabilities expected ≈6.6 of 12) · exact scoreline predicted 1/12 · average probability placed on what actually happened: **40.1%** (33.3% = guessing).

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

*Predictions are frozen at the last run before each result arrives, then graded — the scorecard never grades a model that has already seen the answer.*

