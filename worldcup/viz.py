"""SVG 'path to the final' bracket — the projected knockout tree drawn
top-down, 16 contenders converging to the champion at the bottom.

Pure string generation (no deps); the result is embedded as inline SVG in
the report/site. Driven by report.predicted_bracket() output.
"""

from __future__ import annotations

from html import escape

# Layout order so connector lines never cross, derived from bracket.json:
#   QF97 = W89/W90, QF98 = W93/W94, QF99 = W91/W92, QF100 = W95/W96
#   SF101 = W97/W98, SF102 = W99/W100, Final = W101/W102
R16_ORDER = [89, 90, 93, 94, 91, 92, 95, 96]
QF_ORDER = [97, 98, 99, 100]
SF_ORDER = [101, 102]

MARGIN, BOX_W, BOX_H, GAPX = 24, 140, 48, 12
ROW_Y = {"r16": 56, "qf": 196, "sf": 336, "final": 476}
CHAMP_Y = 588

SHORT = {
    "Bosnia and Herzegovina": "Bosnia", "United States": "USA",
    "South Korea": "S. Korea", "South Africa": "S. Africa",
    "Saudi Arabia": "Saudi Arabia", "Cape Verde": "Cape Verde",
    "New Zealand": "N. Zealand", "Czech Republic": "Czechia",
    "Turkey": "Türkiye",
}


def _short(name: str) -> str:
    return SHORT.get(name, name)


def _pct(x: float) -> str:
    return f"{100 * x:.0f}%"


def _centers() -> dict:
    r16 = [MARGIN + BOX_W / 2 + i * (BOX_W + GAPX) for i in range(8)]
    qf = [(r16[2 * k] + r16[2 * k + 1]) / 2 for k in range(4)]
    sf = [(qf[2 * k] + qf[2 * k + 1]) / 2 for k in range(2)]
    final = (sf[0] + sf[1]) / 2
    return {"r16": r16, "qf": qf, "sf": sf, "final": final}


def _box(cx: float, y: float, tie: dict) -> str:
    """A match box: two teams stacked, projected winner highlighted."""
    x = cx - BOX_W / 2
    home, away, winner = tie["home"], tie["away"], tie["winner"]
    p_home = tie["p_home_advance"]
    rows = [(home, p_home, winner == home), (away, 1 - p_home, winner == away)]
    parts = [
        f'<rect x="{x:.0f}" y="{y}" width="{BOX_W}" height="{BOX_H}" rx="7" '
        f'fill="#161e31" stroke="#26314f" stroke-width="1"/>'
    ]
    for r, (team, p, win) in enumerate(rows):
        ty = y + 19 + r * 21
        if win:
            parts.append(
                f'<rect x="{x:.0f}" y="{y + 2 + r * 22:.0f}" width="{BOX_W}" '
                f'height="21" rx="5" fill="#4cc38a" opacity="0.16"/>')
        fill = "#7ef0b6" if win else "#7c89a3"
        weight = "700" if win else "400"
        parts.append(
            f'<text x="{x + 9:.0f}" y="{ty}" font-size="11.5" font-weight="{weight}" '
            f'fill="{fill}">{escape(_short(team))}</text>')
        parts.append(
            f'<text x="{x + BOX_W - 9:.0f}" y="{ty}" font-size="10" '
            f'text-anchor="end" fill="{"#cfe8d8" if win else "#5d6880"}">'
            f'{_pct(p)}</text>')
    return "".join(parts)


def _conn(x1: float, y1: float, x2: float, y2: float) -> str:
    my = (y1 + y2) / 2
    return (f'<path d="M{x1:.0f},{y1:.0f} C{x1:.0f},{my:.0f} {x2:.0f},{my:.0f} '
            f'{x2:.0f},{y2:.0f}" fill="none" stroke="#33436b" stroke-width="1.6"/>')


def bracket_svg(bracket_path: dict, champion: str, champ_prob: float) -> str:
    c = _centers()
    by_match = {t["match"]: t for rnd in ("round_of_16", "quarterfinals",
                                          "semifinals", "final")
                for t in bracket_path[rnd]}
    width = MARGIN * 2 + 8 * BOX_W + 7 * GAPX
    height = CHAMP_Y + 64

    s = [f'<svg viewBox="0 0 {width} {height}" width="100%" '
         f'preserveAspectRatio="xMidYMin meet" '
         f'xmlns="http://www.w3.org/2000/svg" font-family="-apple-system,'
         'BlinkMacSystemFont,Segoe UI,Roboto,Helvetica,Arial,sans-serif">']

    # connectors first (under the boxes)
    def bottom(cx, y):
        return cx, y + BOX_H
    # R16 -> QF
    for k in range(4):
        for j in (2 * k, 2 * k + 1):
            x1, y1 = bottom(c["r16"][j], ROW_Y["r16"])
            s.append(_conn(x1, y1, c["qf"][k], ROW_Y["qf"]))
    # QF -> SF
    for k in range(2):
        for j in (2 * k, 2 * k + 1):
            x1, y1 = bottom(c["qf"][j], ROW_Y["qf"])
            s.append(_conn(x1, y1, c["sf"][k], ROW_Y["sf"]))
    # SF -> Final
    for j in range(2):
        x1, y1 = bottom(c["sf"][j], ROW_Y["sf"])
        s.append(_conn(x1, y1, c["final"], ROW_Y["final"]))
    # Final -> champion
    s.append(_conn(c["final"], ROW_Y["final"] + BOX_H, c["final"], CHAMP_Y))

    # round labels (left gutter)
    for key, label in (("r16", "ROUND OF 16"), ("qf", "QUARTER-FINALS"),
                       ("sf", "SEMI-FINALS"), ("final", "FINAL")):
        s.append(f'<text x="6" y="{ROW_Y[key] + BOX_H / 2 + 3:.0f}" font-size="9" '
                 f'font-weight="700" fill="#5d6880" '
                 f'transform="rotate(-90 6 {ROW_Y[key] + BOX_H / 2:.0f})" '
                 f'text-anchor="middle">{label}</text>')

    # boxes
    for j, mno in enumerate(R16_ORDER):
        s.append(_box(c["r16"][j], ROW_Y["r16"], by_match[mno]))
    for j, mno in enumerate(QF_ORDER):
        s.append(_box(c["qf"][j], ROW_Y["qf"], by_match[mno]))
    for j, mno in enumerate(SF_ORDER):
        s.append(_box(c["sf"][j], ROW_Y["sf"], by_match[mno]))
    s.append(_box(c["final"], ROW_Y["final"], by_match[104]))

    # champion node
    cw = 180
    cx = c["final"] - cw / 2
    s.append(
        f'<rect x="{cx:.0f}" y="{CHAMP_Y}" width="{cw}" height="44" rx="10" '
        f'fill="#f5c542"/>'
        f'<text x="{c["final"]:.0f}" y="{CHAMP_Y + 20}" font-size="12.5" '
        f'font-weight="800" fill="#1a1300" text-anchor="middle">'
        f'\U0001F3C6 {escape(_short(champion))}</text>'
        f'<text x="{c["final"]:.0f}" y="{CHAMP_Y + 36}" font-size="10" '
        f'fill="#5a4a00" text-anchor="middle">projected champion · '
        f'{_pct(champ_prob)} to win</text>')

    s.append("</svg>")
    return "".join(s)
