"""SVG 'path to the final' bracket — the projected knockout tree drawn
top-down, from the Round of 32 converging to the champion at the bottom.

Pure string generation (no deps); embedded as inline SVG in the report and
site. Driven by report.predicted_bracket() output.
"""

from __future__ import annotations

from html import escape

# Left-to-right orders at each level so connector lines never cross,
# derived from bracket.json:
#   R16 89=W74/W77 90=W73/W75 91=W76/W78 92=W79/W80
#       93=W83/W84 94=W81/W82 95=W86/W88 96=W85/W87
#   QF 97=W89/W90 98=W93/W94 99=W91/W92 100=W95/W96
#   SF 101=W97/W98 102=W99/W100 ; Final 104=W101/W102
R32_ORDER = [74, 77, 73, 75, 83, 84, 81, 82, 76, 78, 79, 80, 86, 88, 85, 87]
R16_ORDER = [89, 90, 93, 94, 91, 92, 95, 96]
QF_ORDER = [97, 98, 99, 100]
SF_ORDER = [101, 102]

# (path-key, match-order, gutter label)
LEVELS = [
    ("round_of_32", R32_ORDER, "ROUND OF 32"),
    ("round_of_16", R16_ORDER, "ROUND OF 16"),
    ("quarterfinals", QF_ORDER, "QUARTER-FINALS"),
    ("semifinals", SF_ORDER, "SEMI-FINALS"),
    ("final", [104], "FINAL"),
]

MARGIN, BOX_W, BOX_H, GAPX, ROW_GAP = 26, 112, 44, 8, 116
TOP_Y = 54

SHORT = {
    "Bosnia and Herzegovina": "Bosnia", "United States": "USA",
    "South Korea": "S. Korea", "South Africa": "S. Africa",
    "Saudi Arabia": "Saudi", "Cape Verde": "C. Verde",
    "New Zealand": "N. Zealand", "Czech Republic": "Czechia",
    "Turkey": "Türkiye", "DR Congo": "DR Congo",
}


def _short(name: str) -> str:
    return SHORT.get(name, name)


def _pct(x: float) -> str:
    return f"{100 * x:.0f}%"


def _centers() -> dict:
    """Cascade centres from the 16-wide Round of 32 down to the final."""
    r32 = [MARGIN + BOX_W / 2 + i * (BOX_W + GAPX) for i in range(16)]
    levels = {"round_of_32": r32}
    prev = r32
    for key in ("round_of_16", "quarterfinals", "semifinals"):
        cur = [(prev[2 * k] + prev[2 * k + 1]) / 2 for k in range(len(prev) // 2)]
        levels[key] = cur
        prev = cur
    levels["final"] = [(prev[0] + prev[1]) / 2]
    return levels


def _row_y(level_idx: int) -> int:
    return TOP_Y + level_idx * ROW_GAP


def _box(cx: float, y: int, tie: dict) -> str:
    x = cx - BOX_W / 2
    home, away, winner = tie["home"], tie["away"], tie["winner"]
    p_home = tie["p_home_advance"]
    confirmed = tie.get("confirmed", False)
    underdog = tie.get("h2h_underdog", False)
    played = tie.get("played", False)
    rows = [(home, p_home, winner == home), (away, 1 - p_home, winner == away)]
    # Played ties get a solid green border; confirmed-but-unplayed ties gold.
    stroke, sw = (("#4cc38a", 2.5) if played
                  else ("#f5c542", 2.5) if confirmed else ("#26314f", 1))
    parts = [
        f'<rect x="{x:.0f}" y="{y}" width="{BOX_W}" height="{BOX_H}" rx="6" '
        f'fill="#161e31" stroke="{stroke}" stroke-width="{sw}"/>'
    ]
    for r, (team, p, win) in enumerate(rows):
        ty = y + 17 + r * 20
        if win:
            parts.append(
                f'<rect x="{x:.0f}" y="{y + 2 + r * 21:.0f}" width="{BOX_W}" '
                f'height="20" rx="4" fill="#4cc38a" opacity="0.16"/>')
        fill = "#7ef0b6" if win else "#7c89a3"
        weight = "700" if win else "400"
        parts.append(
            f'<text x="{x + 8:.0f}" y="{ty}" font-size="10.5" font-weight="{weight}" '
            f'fill="{fill}">{escape(_short(team))}</text>')
        if played:
            pct = "✓" if win else ""
        else:
            pct = _pct(p) + ("†" if win and underdog else "")
        parts.append(
            f'<text x="{x + BOX_W - 8:.0f}" y="{ty}" font-size="9" '
            f'text-anchor="end" fill="{"#cfe8d8" if win else "#5d6880"}">'
            f'{pct}</text>')
    return "".join(parts)


def _conn(x1: float, y1: float, x2: float, y2: float) -> str:
    my = (y1 + y2) / 2
    return (f'<path d="M{x1:.0f},{y1:.0f} C{x1:.0f},{my:.0f} {x2:.0f},{my:.0f} '
            f'{x2:.0f},{y2:.0f}" fill="none" stroke="#33436b" stroke-width="1.5"/>')


def bracket_svg(bracket_path: dict, champion: str, champ_prob: float) -> str:
    c = _centers()
    by_match = {t["match"]: t for key, _, _ in LEVELS for t in bracket_path[key]}
    width = MARGIN * 2 + 16 * BOX_W + 15 * GAPX
    champ_y = _row_y(len(LEVELS)) - (ROW_GAP - BOX_H) // 2
    height = champ_y + 64

    s = [f'<svg viewBox="0 0 {width} {height}" width="100%" '
         f'preserveAspectRatio="xMidYMin meet" '
         f'xmlns="http://www.w3.org/2000/svg" font-family="-apple-system,'
         'BlinkMacSystemFont,Segoe UI,Roboto,Helvetica,Arial,sans-serif">']

    # connectors (under boxes): each level feeds the one below it
    keys = [k for k, _, _ in LEVELS]
    for li in range(len(keys) - 1):
        upper, lower = c[keys[li]], c[keys[li + 1]]
        y_from, y_to = _row_y(li) + BOX_H, _row_y(li + 1)
        for k in range(len(lower)):
            for j in (2 * k, 2 * k + 1):
                s.append(_conn(upper[j], y_from, lower[k], y_to))
    # final -> champion
    s.append(_conn(c["final"][0], _row_y(len(LEVELS) - 1) + BOX_H,
                   c["final"][0], champ_y))

    # gutter labels
    for li, (_, _, label) in enumerate(LEVELS):
        ly = _row_y(li) + BOX_H / 2
        s.append(f'<text x="11" y="{ly:.0f}" font-size="9" font-weight="700" '
                 f'fill="#5d6880" transform="rotate(-90 11 {ly:.0f})" '
                 f'text-anchor="middle">{label}</text>')

    # boxes
    for li, (key, order, _) in enumerate(LEVELS):
        for j, mno in enumerate(order):
            s.append(_box(c[key][j], _row_y(li), by_match[mno]))

    # champion node
    cw, cx = 188, c["final"][0]
    s.append(
        f'<rect x="{cx - cw / 2:.0f}" y="{champ_y}" width="{cw}" height="46" '
        f'rx="10" fill="#f5c542"/>'
        f'<text x="{cx:.0f}" y="{champ_y + 21}" font-size="13" font-weight="800" '
        f'fill="#1a1300" text-anchor="middle">\U0001F3C6 '
        f'{escape(_short(champion))}</text>'
        f'<text x="{cx:.0f}" y="{champ_y + 37}" font-size="10" fill="#5a4a00" '
        f'text-anchor="middle">projected champion · {_pct(champ_prob)} to win</text>')

    s.append("</svg>")
    return "".join(s)
