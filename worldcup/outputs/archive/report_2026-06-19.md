# FIFA World Cup 2026 — ML Prediction Report

*Generated 2026-06-20 · data through **2026-06-19** · 50,000 Monte Carlo simulations · 32/72 group matches played*

Probabilities come from a gradient-boosted Poisson goal model (Elo strength + rolling form + venue/importance features) trained on 30,804 internationals, simulated through the official 2026 bracket and tiebreaker rules.

*Rolling validation (7,966 matches, 2018–2026): RPS 0.1687 vs Elo-baseline 0.1711; log-loss 0.8652 vs 0.8809.*

## Title favourites

| # | Team | Group | Champion | Δ vs 2026-06-19 | Final | Semi-final | Quarter-final | Rd of 16 |
|---|------|:-----:|---------:|-------:|------:|-----------:|--------------:|---------:|
| 1 | Argentina | J | **20.1%** | – | 30.1% | 43.7% | 60.0% | 74.1% |
| 2 | Spain | H | **14.0%** | – | 22.5% | 33.1% | 46.1% | 62.0% |
| 3 | France | I | **9.7%** | – | 17.7% | 31.5% | 50.3% | 72.5% |
| 4 | England | L | **7.7%** | – | 13.5% | 25.1% | 39.3% | 71.6% |
| 5 | Colombia | K | **6.4%** | – | 12.0% | 21.4% | 42.0% | 72.2% |
| 6 | Brazil ✅ | C | **4.9%** | – | 9.5% | 20.5% | 37.1% | 63.5% |
| 7 | Mexico ✅ | A | **3.8%** | – | 8.6% | 19.0% | 42.5% | 73.7% |
| 8 | United States ✅ | D | **3.8%** | – | 9.8% | 21.5% | 48.3% | 78.7% |
| 9 | Portugal | K | **3.6%** | – | 7.8% | 14.9% | 27.7% | 54.1% |
| 10 | Morocco ✅ | C | **2.9%** | – | 6.9% | 15.1% | 31.4% | 55.3% |
| 11 | Japan | F | **2.5%** | – | 5.8% | 12.3% | 24.2% | 43.3% |
| 12 | Germany | E | **2.5%** | – | 5.8% | 12.6% | 25.6% | 54.9% |
| 13 | Netherlands | F | **2.5%** | – | 5.7% | 12.5% | 24.7% | 45.5% |
| 14 | Norway | I | **2.4%** | – | 5.6% | 13.9% | 31.9% | 58.0% |
| 15 | Belgium | G | **2.0%** | – | 5.1% | 10.2% | 23.2% | 49.3% |

## Biggest movers since last run (data through 2026-06-19)

| Team | Δ Champion | Δ Rd of 16 | Champion now |
|------|----------:|-----------:|-------------:|
| Netherlands | – | – | 2.5% |
| Egypt | – | – | 0.2% |
| Croatia | – | – | 0.5% |
| South Korea | – | – | 0.6% |
| Austria | – | – | 1.1% |
| Ecuador | – | – | 1.5% |
| Paraguay | – | – | 0.5% |
| Canada | – | – | 1.0% |

*Δ values in probability points. Full run-by-run series in `outputs/history.csv`.*

## Path to the final

The model's single most likely knockout bracket — all 32 projected round-of-32 teams and every unplayed tie, each line carrying the projected winner down to the next round until they converge on the champion. Percentages are each side's chance of advancing from that tie. **A gold-bordered box is a confirmed Round-of-32 tie** (the same pairing in every simulation — mathematically locked): 0/16 locked so far, the rest finalise as the group stage ends on 27 June.

<div style="overflow-x:auto; margin:1rem 0;">
<svg viewBox="0 0 1964 662" width="100%" preserveAspectRatio="xMidYMin meet" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica,Arial,sans-serif"><path d="M82,98 C82,134 142,134 142,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M202,98 C202,134 142,134 142,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M322,98 C322,134 382,134 382,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M442,98 C442,134 382,134 382,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M562,98 C562,134 622,134 622,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M682,98 C682,134 622,134 622,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M802,98 C802,134 862,134 862,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M922,98 C922,134 862,134 862,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1042,98 C1042,134 1102,134 1102,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1162,98 C1162,134 1102,134 1102,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1282,98 C1282,134 1342,134 1342,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1402,98 C1402,134 1342,134 1342,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1522,98 C1522,134 1582,134 1582,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1642,98 C1642,134 1582,134 1582,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1762,98 C1762,134 1822,134 1822,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1882,98 C1882,134 1822,134 1822,170" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M142,214 C142,250 262,250 262,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M382,214 C382,250 262,250 262,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M622,214 C622,250 742,250 742,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M862,214 C862,250 742,250 742,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1102,214 C1102,250 1222,250 1222,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1342,214 C1342,250 1222,250 1222,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1582,214 C1582,250 1702,250 1702,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1822,214 C1822,250 1702,250 1702,286" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M262,330 C262,366 502,366 502,402" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M742,330 C742,366 502,366 502,402" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1222,330 C1222,366 1462,366 1462,402" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1702,330 C1702,366 1462,366 1462,402" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M502,446 C502,482 982,482 982,518" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M1462,446 C1462,482 982,482 982,518" fill="none" stroke="#33436b" stroke-width="1.5"/><path d="M982,562 C982,580 982,580 982,598" fill="none" stroke="#33436b" stroke-width="1.5"/><text x="11" y="76" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 11 76)" text-anchor="middle">ROUND OF 32</text><text x="11" y="192" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 11 192)" text-anchor="middle">ROUND OF 16</text><text x="11" y="308" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 11 308)" text-anchor="middle">QUARTER-FINALS</text><text x="11" y="424" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 11 424)" text-anchor="middle">SEMI-FINALS</text><text x="11" y="540" font-size="9" font-weight="700" fill="#5d6880" transform="rotate(-90 11 540)" text-anchor="middle">FINAL</text><rect x="26" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="26" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="34" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Germany</text><text x="130" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">61%</text><text x="34" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Scotland</text><text x="130" y="91" font-size="9" text-anchor="end" fill="#5d6880">39%</text><rect x="146" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="146" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="154" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">France</text><text x="250" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">74%</text><text x="154" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Paraguay</text><text x="250" y="91" font-size="9" text-anchor="end" fill="#5d6880">26%</text><rect x="266" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="274" y="71" font-size="10.5" font-weight="400" fill="#7c89a3">S. Korea</text><text x="370" y="71" font-size="9" text-anchor="end" fill="#5d6880">42%</text><rect x="266" y="77" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="274" y="91" font-size="10.5" font-weight="700" fill="#7ef0b6">Switzerland</text><text x="370" y="91" font-size="9" text-anchor="end" fill="#cfe8d8">58%</text><rect x="386" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="394" y="71" font-size="10.5" font-weight="400" fill="#7c89a3">Netherlands</text><text x="490" y="71" font-size="9" text-anchor="end" fill="#5d6880">50%</text><rect x="386" y="77" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="394" y="91" font-size="10.5" font-weight="700" fill="#7ef0b6">Morocco</text><text x="490" y="91" font-size="9" text-anchor="end" fill="#cfe8d8">50%</text><rect x="506" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="506" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="514" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Portugal</text><text x="610" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">64%</text><text x="514" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Croatia</text><text x="610" y="91" font-size="9" text-anchor="end" fill="#5d6880">36%</text><rect x="626" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="626" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="634" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Spain</text><text x="730" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">75%</text><text x="634" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Austria</text><text x="730" y="91" font-size="9" text-anchor="end" fill="#5d6880">25%</text><rect x="746" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="746" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="754" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">USA</text><text x="850" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">91%</text><text x="754" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Bosnia</text><text x="850" y="91" font-size="9" text-anchor="end" fill="#5d6880">9%</text><rect x="866" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="866" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="874" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Belgium</text><text x="970" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">66%</text><text x="874" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Algeria</text><text x="970" y="91" font-size="9" text-anchor="end" fill="#5d6880">34%</text><rect x="986" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="986" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="994" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Brazil</text><text x="1090" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">60%</text><text x="994" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Japan</text><text x="1090" y="91" font-size="9" text-anchor="end" fill="#5d6880">40%</text><rect x="1106" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="1114" y="71" font-size="10.5" font-weight="400" fill="#7c89a3">Ivory Coast</text><text x="1210" y="71" font-size="9" text-anchor="end" fill="#5d6880">36%</text><rect x="1106" y="77" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1114" y="91" font-size="10.5" font-weight="700" fill="#7ef0b6">Norway</text><text x="1210" y="91" font-size="9" text-anchor="end" fill="#cfe8d8">64%</text><rect x="1226" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1226" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1234" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Mexico</text><text x="1330" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">66%</text><text x="1234" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Ecuador</text><text x="1330" y="91" font-size="9" text-anchor="end" fill="#5d6880">34%</text><rect x="1346" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1346" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1354" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">England</text><text x="1450" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">74%</text><text x="1354" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Senegal</text><text x="1450" y="91" font-size="9" text-anchor="end" fill="#5d6880">26%</text><rect x="1466" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1466" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1474" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Argentina</text><text x="1570" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">78%</text><text x="1474" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Uruguay</text><text x="1570" y="91" font-size="9" text-anchor="end" fill="#5d6880">22%</text><rect x="1586" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1586" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1594" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Australia</text><text x="1690" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">56%</text><text x="1594" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Iran</text><text x="1690" y="91" font-size="9" text-anchor="end" fill="#5d6880">44%</text><rect x="1706" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1706" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1714" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Canada</text><text x="1810" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">70%</text><text x="1714" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Sweden</text><text x="1810" y="91" font-size="9" text-anchor="end" fill="#5d6880">30%</text><rect x="1826" y="54" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1826" y="56" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1834" y="71" font-size="10.5" font-weight="700" fill="#7ef0b6">Colombia</text><text x="1930" y="71" font-size="9" text-anchor="end" fill="#cfe8d8">87%</text><text x="1834" y="91" font-size="10.5" font-weight="400" fill="#7c89a3">Ghana</text><text x="1930" y="91" font-size="9" text-anchor="end" fill="#5d6880">13%</text><rect x="86" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="94" y="187" font-size="10.5" font-weight="400" fill="#7c89a3">Germany</text><text x="190" y="187" font-size="9" text-anchor="end" fill="#5d6880">33%</text><rect x="86" y="193" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="94" y="207" font-size="10.5" font-weight="700" fill="#7ef0b6">France</text><text x="190" y="207" font-size="9" text-anchor="end" fill="#cfe8d8">67%</text><rect x="326" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="334" y="187" font-size="10.5" font-weight="400" fill="#7c89a3">Switzerland</text><text x="430" y="187" font-size="9" text-anchor="end" fill="#5d6880">46%</text><rect x="326" y="193" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="334" y="207" font-size="10.5" font-weight="700" fill="#7ef0b6">Morocco</text><text x="430" y="207" font-size="9" text-anchor="end" fill="#cfe8d8">54%</text><rect x="566" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="574" y="187" font-size="10.5" font-weight="400" fill="#7c89a3">Portugal</text><text x="670" y="187" font-size="9" text-anchor="end" fill="#5d6880">36%</text><rect x="566" y="193" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="574" y="207" font-size="10.5" font-weight="700" fill="#7ef0b6">Spain</text><text x="670" y="207" font-size="9" text-anchor="end" fill="#cfe8d8">64%</text><rect x="806" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="806" y="172" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="814" y="187" font-size="10.5" font-weight="700" fill="#7ef0b6">USA</text><text x="910" y="187" font-size="9" text-anchor="end" fill="#cfe8d8">51%</text><text x="814" y="207" font-size="10.5" font-weight="400" fill="#7c89a3">Belgium</text><text x="910" y="207" font-size="9" text-anchor="end" fill="#5d6880">49%</text><rect x="1046" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1046" y="172" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1054" y="187" font-size="10.5" font-weight="700" fill="#7ef0b6">Brazil</text><text x="1150" y="187" font-size="9" text-anchor="end" fill="#cfe8d8">53%</text><text x="1054" y="207" font-size="10.5" font-weight="400" fill="#7c89a3">Norway</text><text x="1150" y="207" font-size="9" text-anchor="end" fill="#5d6880">47%</text><rect x="1286" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="1294" y="187" font-size="10.5" font-weight="400" fill="#7c89a3">Mexico</text><text x="1390" y="187" font-size="9" text-anchor="end" fill="#5d6880">50%</text><rect x="1286" y="193" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1294" y="207" font-size="10.5" font-weight="700" fill="#7ef0b6">England</text><text x="1390" y="207" font-size="9" text-anchor="end" fill="#cfe8d8">50%</text><rect x="1526" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1526" y="172" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1534" y="187" font-size="10.5" font-weight="700" fill="#7ef0b6">Argentina</text><text x="1630" y="187" font-size="9" text-anchor="end" fill="#cfe8d8">82%</text><text x="1534" y="207" font-size="10.5" font-weight="400" fill="#7c89a3">Australia</text><text x="1630" y="207" font-size="9" text-anchor="end" fill="#5d6880">18%</text><rect x="1766" y="170" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="1774" y="187" font-size="10.5" font-weight="400" fill="#7c89a3">Canada</text><text x="1870" y="187" font-size="9" text-anchor="end" fill="#5d6880">43%</text><rect x="1766" y="193" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1774" y="207" font-size="10.5" font-weight="700" fill="#7ef0b6">Colombia</text><text x="1870" y="207" font-size="9" text-anchor="end" fill="#cfe8d8">57%</text><rect x="206" y="286" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="206" y="288" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="214" y="303" font-size="10.5" font-weight="700" fill="#7ef0b6">France</text><text x="310" y="303" font-size="9" text-anchor="end" fill="#cfe8d8">64%</text><text x="214" y="323" font-size="10.5" font-weight="400" fill="#7c89a3">Morocco</text><text x="310" y="323" font-size="9" text-anchor="end" fill="#5d6880">36%</text><rect x="686" y="286" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="686" y="288" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="694" y="303" font-size="10.5" font-weight="700" fill="#7ef0b6">Spain</text><text x="790" y="303" font-size="9" text-anchor="end" fill="#cfe8d8">68%</text><text x="694" y="323" font-size="10.5" font-weight="400" fill="#7c89a3">USA</text><text x="790" y="323" font-size="9" text-anchor="end" fill="#5d6880">32%</text><rect x="1166" y="286" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="1174" y="303" font-size="10.5" font-weight="400" fill="#7c89a3">Brazil</text><text x="1270" y="303" font-size="9" text-anchor="end" fill="#5d6880">39%</text><rect x="1166" y="309" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1174" y="323" font-size="10.5" font-weight="700" fill="#7ef0b6">England</text><text x="1270" y="323" font-size="9" text-anchor="end" fill="#cfe8d8">61%</text><rect x="1646" y="286" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="1646" y="288" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1654" y="303" font-size="10.5" font-weight="700" fill="#7ef0b6">Argentina</text><text x="1750" y="303" font-size="9" text-anchor="end" fill="#cfe8d8">63%</text><text x="1654" y="323" font-size="10.5" font-weight="400" fill="#7c89a3">Colombia</text><text x="1750" y="323" font-size="9" text-anchor="end" fill="#5d6880">37%</text><rect x="446" y="402" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="454" y="419" font-size="10.5" font-weight="400" fill="#7c89a3">France</text><text x="550" y="419" font-size="9" text-anchor="end" fill="#5d6880">41%</text><rect x="446" y="425" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="454" y="439" font-size="10.5" font-weight="700" fill="#7ef0b6">Spain</text><text x="550" y="439" font-size="9" text-anchor="end" fill="#cfe8d8">59%</text><rect x="1406" y="402" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><text x="1414" y="419" font-size="10.5" font-weight="400" fill="#7c89a3">England</text><text x="1510" y="419" font-size="9" text-anchor="end" fill="#5d6880">38%</text><rect x="1406" y="425" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="1414" y="439" font-size="10.5" font-weight="700" fill="#7ef0b6">Argentina</text><text x="1510" y="439" font-size="9" text-anchor="end" fill="#cfe8d8">62%</text><rect x="926" y="518" width="112" height="44" rx="6" fill="#161e31" stroke="#26314f" stroke-width="1"/><rect x="926" y="520" width="112" height="20" rx="4" fill="#4cc38a" opacity="0.16"/><text x="934" y="535" font-size="10.5" font-weight="700" fill="#7ef0b6">Spain</text><text x="1030" y="535" font-size="9" text-anchor="end" fill="#cfe8d8">53%</text><text x="934" y="555" font-size="10.5" font-weight="400" fill="#7c89a3">Argentina</text><text x="1030" y="555" font-size="9" text-anchor="end" fill="#5d6880">47%</text><rect x="888" y="598" width="188" height="46" rx="10" fill="#f5c542"/><text x="982" y="619" font-size="13" font-weight="800" fill="#1a1300" text-anchor="middle">🏆 Spain</text><text x="982" y="635" font-size="10" fill="#5a4a00" text-anchor="middle">projected champion · 14% to win</text></svg>
</div>

## Upcoming group matches — outcome probabilities

*(next match days; full list for all 72 group games in `match_probabilities.csv`)*

| Date | Grp | Match | Home win | Draw | Away win | xG | Likely score |
|------|:---:|-------|---------:|-----:|---------:|----|:----:|
| 2026-06-20 | F | Netherlands v Sweden | **52.8%** | 22.7% | 24.6% | 2.00–1.32 | 1-1 |
| 2026-06-20 | F | Tunisia v Japan | 13.1% | 21.4% | **65.5%** | 0.78–2.00 | 0-2 |
| 2026-06-20 | E | Germany v Ivory Coast | **49.2%** | 27.2% | 23.5% | 1.51–0.97 | 1-1 |
| 2026-06-20 | E | Ecuador v Curaçao | **82.9%** | 12.1% | 5.0% | 2.83–0.60 | 2-0 |
| 2026-06-21 | G | Belgium v Iran | **46.0%** | 26.4% | 27.6% | 1.56–1.16 | 1-1 |
| 2026-06-21 | G | New Zealand v Egypt | 27.1% | 28.1% | **44.8%** | 1.04–1.41 | 1-1 |
| 2026-06-21 | H | Spain v Saudi Arabia | **77.3%** | 16.5% | 6.2% | 2.26–0.50 | 2-0 |
| 2026-06-21 | H | Uruguay v Cape Verde | **66.8%** | 21.2% | 12.0% | 1.99–0.72 | 2-0 |
| 2026-06-22 | I | France v Iraq | **77.3%** | 15.5% | 7.2% | 2.48–0.64 | 2-0 |
| 2026-06-22 | I | Norway v Senegal | **47.3%** | 25.7% | 27.1% | 1.64–1.19 | 1-1 |
| 2026-06-22 | J | Argentina v Austria | **63.3%** | 22.4% | 14.4% | 1.92–0.80 | 2-0 |
| 2026-06-22 | J | Jordan v Algeria | 22.9% | 25.0% | **52.1%** | 1.07–1.72 | 1-1 |
| 2026-06-23 | K | Portugal v Uzbekistan | **62.7%** | 22.8% | 14.5% | 1.88–0.79 | 1-0 |
| 2026-06-23 | K | Colombia v DR Congo | **64.7%** | 22.2% | 13.1% | 1.91–0.73 | 1-0 |
| 2026-06-23 | L | England v Ghana | **75.2%** | 17.7% | 7.1% | 2.17–0.52 | 2-0 |
| 2026-06-23 | L | Panama v Croatia | 23.7% | 26.3% | **50.0%** | 1.02–1.59 | 1-1 |

## Group projections

### Group A

**✅ Into the knockouts:** Mexico

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Mexico ✅ | 2 | 2-0-0 | 3-0 | **6** | 8.50 | 100.0% | 100.0% | 100.0% |
| South Korea | 2 | 1-0-1 | 2-2 | **3** | 4.99 | 0.0% | 83.6% | 94.7% |
| Czech Republic | 2 | 0-1-1 | 2-3 | **1** | 1.34 | 0.0% | 1.0% | 6.9% |
| South Africa | 2 | 0-1-1 | 1-3 | **1** | 1.75 | 0.0% | 15.4% | 16.5% |

### Group B

**✅ Into the knockouts:** Canada, Switzerland

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Canada ✅ | 2 | 1-1-0 | 7-1 | **4** | 5.55 | 71.0% | 100.0% | 100.0% |
| Switzerland ✅ | 2 | 1-1-0 | 5-2 | **4** | 5.16 | 29.0% | 100.0% | 100.0% |
| Bosnia and Herzegovina | 2 | 0-1-1 | 2-5 | **1** | 2.66 | 0.0% | 0.0% | 45.9% |
| Qatar | 2 | 0-1-1 | 1-7 | **1** | 2.06 | 0.0% | 0.0% | 25.7% |

### Group C

**✅ Into the knockouts:** Brazil, Morocco

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Brazil ✅ | 2 | 1-1-0 | 4-1 | **4** | 6.12 | 64.5% | 87.0% | 100.0% |
| Morocco ✅ | 2 | 1-1-0 | 2-1 | **4** | 6.37 | 31.6% | 98.8% | 100.0% |
| Scotland | 2 | 1-0-1 | 1-1 | **3** | 3.65 | 3.9% | 14.2% | 79.1% |
| Haiti | 2 | 0-0-2 | 0-4 | **0** | 0.45 | 0.0% | 0.0% | 0.0% |

### Group D

**✅ Into the knockouts:** United States

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| United States ✅ | 2 | 2-0-0 | 6-1 | **6** | 7.83 | 100.0% | 100.0% | 100.0% |
| Australia | 2 | 1-0-1 | 2-2 | **3** | 4.40 | 0.0% | 66.4% | 92.6% |
| Paraguay | 2 | 1-0-1 | 2-4 | **3** | 4.30 | 0.0% | 33.6% | 80.4% |
| Turkey | 2 | 0-0-2 | 0-3 | **0** | 0.92 | 0.0% | 0.0% | 0.0% |

### Group E

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Germany | 1 | 1-0-0 | 7-1 | **3** | 6.31 | 56.4% | 85.4% | 99.7% |
| Ivory Coast | 1 | 1-0-0 | 1-0 | **3** | 6.14 | 33.9% | 84.8% | 95.3% |
| Ecuador | 1 | 0-0-1 | 0-1 | **0** | 3.76 | 9.5% | 28.1% | 83.9% |
| Curaçao | 1 | 0-0-1 | 1-7 | **0** | 0.89 | 0.2% | 1.7% | 5.2% |

### Group F

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Sweden | 1 | 1-0-0 | 5-1 | **3** | 4.94 | 29.7% | 55.4% | 96.4% |
| Japan | 1 | 0-1-0 | 2-2 | **1** | 4.96 | 32.9% | 69.0% | 88.7% |
| Netherlands | 1 | 0-1-0 | 2-2 | **1** | 5.00 | 36.4% | 70.3% | 89.1% |
| Tunisia | 1 | 0-0-1 | 1-5 | **0** | 1.20 | 1.0% | 5.3% | 10.3% |

### Group G

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Iran | 1 | 0-1-0 | 2-2 | **1** | 3.49 | 22.6% | 51.3% | 62.6% |
| New Zealand | 1 | 0-1-0 | 2-2 | **1** | 2.70 | 9.6% | 28.9% | 42.3% |
| Belgium | 1 | 0-1-0 | 1-1 | **1** | 4.84 | 46.8% | 72.3% | 86.7% |
| Egypt | 1 | 0-1-0 | 1-1 | **1** | 3.92 | 20.9% | 47.5% | 70.7% |

### Group H

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Saudi Arabia | 1 | 0-1-0 | 1-1 | **1** | 2.85 | 7.0% | 26.0% | 48.8% |
| Uruguay | 1 | 0-1-0 | 1-1 | **1** | 4.08 | 27.6% | 67.4% | 79.5% |
| Cape Verde | 1 | 0-1-0 | 0-0 | **1** | 2.77 | 5.3% | 20.1% | 44.5% |
| Spain | 1 | 0-1-0 | 0-0 | **1** | 5.35 | 60.1% | 86.4% | 93.6% |

### Group I

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Norway | 1 | 1-0-0 | 4-1 | **3** | 5.42 | 23.9% | 77.9% | 97.4% |
| France | 1 | 1-0-0 | 3-1 | **3** | 7.50 | 73.9% | 97.5% | 99.5% |
| Senegal | 1 | 0-0-1 | 1-3 | **0** | 3.07 | 1.7% | 22.6% | 59.7% |
| Iraq | 1 | 0-0-1 | 1-4 | **0** | 1.13 | 0.5% | 2.0% | 11.1% |

### Group J

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Argentina | 1 | 1-0-0 | 3-0 | **3** | 7.74 | 83.2% | 98.8% | 99.8% |
| Austria | 1 | 1-0-0 | 3-1 | **3** | 5.19 | 15.3% | 75.5% | 95.2% |
| Jordan | 1 | 0-0-1 | 1-3 | **0** | 1.18 | 0.4% | 2.1% | 14.4% |
| Algeria | 1 | 0-0-1 | 0-3 | **0** | 2.99 | 1.1% | 23.6% | 52.2% |

### Group K

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| Colombia | 1 | 1-0-0 | 3-1 | **3** | 6.69 | 69.6% | 90.1% | 99.0% |
| DR Congo | 1 | 0-1-0 | 1-1 | **1** | 3.04 | 6.4% | 29.0% | 53.1% |
| Portugal | 1 | 0-1-0 | 1-1 | **1** | 4.30 | 22.9% | 66.7% | 81.7% |
| Uzbekistan | 1 | 0-0-1 | 1-3 | **0** | 1.94 | 1.1% | 14.1% | 30.7% |

### Group L

| Team | P | W-D-L | GF-GA | Pts | xPts | Win grp | Top 2 | Advance* |
|------|--:|:----:|:----:|----:|-----:|--------:|------:|--------:|
| England | 1 | 1-0-0 | 4-2 | **3** | 7.59 | 88.0% | 98.0% | 99.5% |
| Ghana | 1 | 1-0-0 | 1-0 | **3** | 4.05 | 6.4% | 35.3% | 70.1% |
| Panama | 1 | 0-0-1 | 0-1 | **0** | 1.58 | 2.4% | 9.7% | 23.3% |
| Croatia | 1 | 0-0-1 | 2-4 | **0** | 3.87 | 3.3% | 57.1% | 74.2% |

*\*Advance = top two or one of the eight best third-placed teams.*

*✅ = already reached the knockout stage — locked into the Round of 32 in every simulation. (Reaching later rounds still requires winning knockout games, so those stay below 100%.)*

## Most likely knockout bracket

Each tie shows the most probable pairing given projected group finishes, the chance the named winner goes through **in that pairing**, and how often the exact pairing occurred across all simulations. **🔒 marks a confirmed tie** — the same two teams in every simulation, i.e. mathematically locked. (0/16 Round-of-32 ties locked so far; the rest finalise as the group stage completes on 27 June.)

### Round of 32

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 73 | 2026-06-28 | SoFi Stadium, Los Angeles | South Korea v Switzerland | **Switzerland** | 57.8% | 59.4% |
| 74 | 2026-06-29 | Gillette Stadium, Boston | Germany v Scotland | **Germany** | 61.4% | 10.0% |
| 75 | 2026-06-29 | Estadio BBVA, Monterrey | Netherlands v Morocco | **Morocco** | 50.2% | 24.5% |
| 76 | 2026-06-29 | NRG Stadium, Houston | Brazil v Japan | **Brazil** | 59.7% | 23.4% |
| 77 | 2026-06-30 | MetLife Stadium, New York/New Jersey | France v Paraguay | **France** | 74.5% | 15.6% |
| 78 | 2026-06-30 | AT&T Stadium, Dallas | Ivory Coast v Norway | **Norway** | 64.5% | 27.3% |
| 79 | 2026-06-30 | Estadio Azteca, Mexico City | Mexico v Ecuador | **Mexico** | 66.1% | 22.4% |
| 80 | 2026-07-01 | Mercedes-Benz Stadium, Atlanta | England v Senegal | **England** | 74.0% | 3.3% |
| 81 | 2026-07-01 | Levi's Stadium, San Francisco Bay Area | United States v Bosnia and Herzegovina | **United States** | 90.7% | 33.7% |
| 82 | 2026-07-01 | Lumen Field, Seattle | Belgium v Algeria | **Belgium** | 65.9% | 4.6% |
| 83 | 2026-07-02 | BMO Field, Toronto | Portugal v Croatia | **Portugal** | 63.5% | 23.5% |
| 84 | 2026-07-02 | SoFi Stadium, Los Angeles | Spain v Austria | **Spain** | 75.3% | 36.1% |
| 85 | 2026-07-02 | BC Place, Vancouver | Canada v Sweden | **Canada** | 70.0% | 9.0% |
| 86 | 2026-07-03 | Hard Rock Stadium, Miami | Argentina v Uruguay | **Argentina** | 78.4% | 33.1% |
| 87 | 2026-07-03 | Arrowhead Stadium, Kansas City | Colombia v Ghana | **Colombia** | 87.3% | 24.8% |
| 88 | 2026-07-03 | AT&T Stadium, Dallas | Australia v Iran | **Australia** | 56.4% | 19.0% |

### Round of 16

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 89 | 2026-07-04 | Lincoln Financial Field, Philadelphia | Germany v France | **France** | 66.9% | 19.1% |
| 90 | 2026-07-04 | NRG Stadium, Houston | Switzerland v Morocco | **Morocco** | 53.7% | 16.1% |
| 91 | 2026-07-05 | MetLife Stadium, New York/New Jersey | Brazil v Norway | **Brazil** | 53.4% | 13.3% |
| 92 | 2026-07-05 | Estadio Azteca, Mexico City | Mexico v England | **England** | 50.2% | 47.2% |
| 93 | 2026-07-06 | AT&T Stadium, Dallas | Portugal v Spain | **Spain** | 63.6% | 13.4% |
| 94 | 2026-07-06 | Lumen Field, Seattle | United States v Belgium | **United States** | 50.7% | 22.0% |
| 95 | 2026-07-07 | Mercedes-Benz Stadium, Atlanta | Argentina v Australia | **Argentina** | 81.6% | 23.8% |
| 96 | 2026-07-07 | BC Place, Vancouver | Canada v Colombia | **Colombia** | 56.8% | 25.1% |

### Quarter-finals

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 97 | 2026-07-09 | Gillette Stadium, Boston | France v Morocco | **France** | 64.3% | 8.5% |
| 98 | 2026-07-10 | SoFi Stadium, Los Angeles | Spain v United States | **Spain** | 68.0% | 15.5% |
| 99 | 2026-07-11 | Hard Rock Stadium, Miami | Brazil v England | **England** | 61.2% | 7.9% |
| 100 | 2026-07-11 | Arrowhead Stadium, Kansas City | Argentina v Colombia | **Argentina** | 62.7% | 17.3% |

### Semi-finals

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 101 | 2026-07-14 | AT&T Stadium, Dallas | France v Spain | **Spain** | 59.5% | 6.2% |
| 102 | 2026-07-15 | Mercedes-Benz Stadium, Atlanta | England v Argentina | **Argentina** | 62.2% | 8.5% |

### Final

| Match | Date | Venue | Tie | Projected winner | Win prob | Pairing freq |
|:-----:|------|-------|-----|------------------|---------:|-------------:|
| 104 | 2026-07-19 | MetLife Stadium, East Rutherford | Spain v Argentina | **Spain** | 52.6% | 5.2% |

**Projected champion: Spain** (overall title probability 14.0%; the single most likely path above is itself only one of many ways the tournament can unfold).

## How to read this

- All figures are probabilities, not certainties — a 65% favourite loses about one such match in three.
- `xPts` = expected group points; `xG` = expected goals from the Poisson model.
- Predictions refresh after every match day: run `python -m worldcup.run all` to pull new results, re-rate teams, and re-simulate.
- Machine-readable outputs: `match_probabilities.csv`, `tournament_projections.csv`. Past reports in `outputs/archive/`.

## Model scorecard

**17 of 32 match outcomes called correctly** (the model's own probabilities expected ≈18.5 of 32) · exact scoreline predicted 2/32 · average probability placed on what actually happened: **42.8%** (33.3% = guessing).

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
| Spain v Cape Verde | Spain win (90.5%) | 3-0 | 0-0 | ❌ | — |
| Saudi Arabia v Uruguay | Uruguay win (62.1%) | 0-1 | 1-1 | ❌ | — |
| Belgium v Egypt | Belgium win (56.6%) | 1-1 | 1-1 | ❌ | ✅ |
| Iran v New Zealand | Iran win (54.6%) | 1-0 | 2-2 | ❌ | — |
| Austria v Jordan | Austria win (47.0%) | 1-1 | 3-1 | ✅ | — |
| Argentina v Algeria | Argentina win (68.0%) | 2-0 | 3-0 | ✅ | — |
| France v Senegal | France win (59.1%) | 1-0 | 3-1 | ✅ | — |
| Iraq v Norway | Norway win (59.1%) | 0-1 | 1-4 | ✅ | — |
| Ghana v Panama | Panama win (51.9%) | 1-1 | 1-0 | ❌ | — |
| England v Croatia | England win (56.9%) | 1-0 | 4-2 | ✅ | — |
| Portugal v DR Congo | Portugal win (70.6%) | 2-0 | 1-1 | ❌ | — |
| Uzbekistan v Colombia | Colombia win (53.9%) | 0-1 | 1-3 | ✅ | — |
| Czech Republic v South Africa | Czech Republic win (55.5%) | 1-0 | 1-1 | ❌ | — |
| Mexico v South Korea | Mexico win (51.1%) | 1-1 | 1-0 | ✅ | — |
| Switzerland v Bosnia and Herzegovina | Switzerland win (66.8%) | 2-0 | 4-1 | ✅ | — |
| Canada v Qatar | Canada win (74.0%) | 2-0 | 6-0 | ✅ | — |
| Brazil v Haiti | Brazil win (81.3%) | 2-0 | 3-0 | ✅ | — |
| Turkey v Paraguay | Paraguay win (38.4%) | 1-1 | 0-1 | ✅ | — |
| Scotland v Morocco | Morocco win (49.3%) | 1-1 | 0-1 | ✅ | — |
| United States v Australia | Australia win (35.9%) | 1-1 | 2-0 | ❌ | — |

**Calibration vs benchmarks** (the 9 graded games with bookmaker prices on file) — log-loss, lower is better. This is the honest test: is the model bad, or were the games hard for everyone?

| Forecaster | Log-loss |
|------------|---------:|
| **This model** | **1.193** |
| Sky Bet (de-vigged) | 1.156 |
| Coin-flip (33/33/33) | 1.099 |

The model is **essentially level with the market** (+0.037 log-loss). Note both the model **and** the bookmaker scored worse than a coin-flip here — with this many draws and upsets, the slate was close to unforecastable for anyone, which is the real reason the hit-rate looks poor.


*Predictions are frozen at the last run before each result arrives, then graded — the scorecard never grades a model that has already seen the answer.*

