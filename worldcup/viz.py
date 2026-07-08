"""SVG 'path to the final' bracket — the projected knockout tree drawn
top-down, converging to the champion at the bottom.

Pure string generation (no deps); embedded as inline SVG in the report and
site. Driven by report.predicted_bracket() output.

The layout is dynamic: it roots the drawing at the round that still has the
most live (unplayed) ties and sizes boxes/fonts to that width. Early on that is
the 16-wide Round of 32; deep in the tournament it collapses to a compact
quarter-final → final tree, so the bracket fills the page instead of scaling
down to an unreadable sliver. Played ties are dropped (winner carries forward).
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

MARGIN = 26

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


def _box(cx: float, y: float, tie: dict, S: dict) -> str:
    """Draw a tie box. S holds the dynamic sizing for this render."""
    bw, bh = S["bw"], S["bh"]
    fs_team, fs_pct = S["fs_team"], S["fs_pct"]
    x = cx - bw / 2
    home, away, winner = tie["home"], tie["away"], tie["winner"]
    p_home = tie["p_home_advance"]
    confirmed = tie.get("confirmed", False)
    played = tie.get("played", False)
    rows = [(home, p_home, winner == home), (away, 1 - p_home, winner == away)]
    # Played ties get a solid green border; confirmed-but-unplayed ties gold.
    stroke, sw = (("#4cc38a", 2.5) if played
                  else ("#f5c542", 2.5) if confirmed else ("#26314f", 1))
    row_h = bh / 2
    parts = [
        f'<rect x="{x:.1f}" y="{y:.1f}" width="{bw}" height="{bh}" rx="6" '
        f'fill="#161e31" stroke="{stroke}" stroke-width="{sw}"/>'
    ]
    for r, (team, p, win) in enumerate(rows):
        ty = y + row_h * r + row_h / 2 + fs_team * 0.35
        if win:
            parts.append(
                f'<rect x="{x:.1f}" y="{y + r * row_h + 2:.1f}" width="{bw}" '
                f'height="{row_h - 3:.1f}" rx="4" fill="#4cc38a" opacity="0.16"/>')
        fill = "#7ef0b6" if win else "#7c89a3"
        weight = "700" if win else "400"
        parts.append(
            f'<text x="{x + 8:.1f}" y="{ty:.1f}" font-size="{fs_team}" '
            f'font-weight="{weight}" fill="{fill}">{escape(_short(team))}</text>')
        pct = "✓" if (played and win) else ("" if played else _pct(p))
        parts.append(
            f'<text x="{x + bw - 8:.1f}" y="{ty:.1f}" font-size="{fs_pct}" '
            f'text-anchor="end" fill="{"#cfe8d8" if win else "#5d6880"}">'
            f'{pct}</text>')
    return "".join(parts)


def _conn(x1: float, y1: float, x2: float, y2: float) -> str:
    my = (y1 + y2) / 2
    return (f'<path d="M{x1:.1f},{y1:.1f} C{x1:.1f},{my:.1f} {x2:.1f},{my:.1f} '
            f'{x2:.1f},{y2:.1f}" fill="none" stroke="#33436b" stroke-width="1.5"/>')


def bracket_svg(bracket_path: dict, champion: str, champ_prob: float) -> str:
    by_match = {t["match"]: t for key, _, _ in LEVELS for t in bracket_path[key]}

    def is_played(m):
        return by_match[m].get("played", False)

    # Root at the first round that still has an unplayed tie. Only *fully
    # completed* leading rounds are dropped — a round is never removed while it
    # still has a game left to play, so unplayed ties always stay on the chart.
    root = 0
    for li, (_, order, _) in enumerate(LEVELS):
        if all(is_played(m) for m in order):
            root = li + 1
        else:
            break
    root = min(root, len(LEVELS) - 1)
    live = LEVELS[root:]
    top_n = len(live[0][1])

    # Dynamic sizing: fewer columns -> wider boxes + larger type, and a
    # narrower viewBox so the whole thing renders larger on a phone.
    bw = min(190, max(120, int(760 / top_n)))
    gapx = max(8, bw // 12)
    bh = 52 if top_n <= 8 else 46
    row_gap = bh + 78
    top_y = 40
    fs_team = 14 if top_n <= 4 else 12 if top_n <= 8 else 10.5
    fs_pct = 11 if top_n <= 4 else 10 if top_n <= 8 else 9
    S = {"bw": bw, "bh": bh, "fs_team": fs_team, "fs_pct": fs_pct}

    # centres cascade from the top level down
    top = [MARGIN + bw / 2 + i * (bw + gapx) for i in range(top_n)]
    centres = {live[0][0]: top}
    prev = top
    for key, _, _ in live[1:]:
        cur = [(prev[2 * k] + prev[2 * k + 1]) / 2 for k in range(len(prev) // 2)]
        centres[key] = cur
        prev = cur

    width = round(MARGIN * 2 + top_n * bw + (top_n - 1) * gapx)

    def row_y(i):
        return top_y + i * row_gap

    n = len(live)
    champ_y = row_y(n) - (row_gap - bh) // 2
    height = round(champ_y + bh + 22)

    s = [f'<svg viewBox="0 0 {width} {height}" width="100%" '
         f'preserveAspectRatio="xMidYMin meet" '
         f'xmlns="http://www.w3.org/2000/svg" font-family="-apple-system,'
         'BlinkMacSystemFont,Segoe UI,Roboto,Helvetica,Arial,sans-serif">']

    # connectors: each live level feeds the one below (skip played feeders)
    keys = [k for k, _, _ in live]
    for li in range(len(keys) - 1):
        upper, lower = centres[keys[li]], centres[keys[li + 1]]
        up_order = live[li][1]
        y_from, y_to = row_y(li) + bh, row_y(li + 1)
        for k in range(len(lower)):
            for j in (2 * k, 2 * k + 1):
                if is_played(up_order[j]):
                    continue
                s.append(_conn(upper[j], y_from, lower[k], y_to))
    # final -> champion
    if keys[-1] == "final" and not is_played(live[-1][1][0]):
        s.append(_conn(centres["final"][0], row_y(n - 1) + bh,
                       centres["final"][0], champ_y))

    # gutter labels
    for li, (_, _, label) in enumerate(live):
        ly = row_y(li) + bh / 2
        s.append(f'<text x="11" y="{ly:.0f}" font-size="9" font-weight="700" '
                 f'fill="#5d6880" transform="rotate(-90 11 {ly:.0f})" '
                 f'text-anchor="middle">{label}</text>')

    # boxes (played ties are removed — winner shows in the next round)
    for li, (key, order, _) in enumerate(live):
        for j, mno in enumerate(order):
            if is_played(mno):
                continue
            s.append(_box(centres[key][j], row_y(li), by_match[mno], S))

    # champion node
    cw, cx = min(230, int(bw * 1.7)), centres["final"][0]
    s.append(
        f'<rect x="{cx - cw / 2:.0f}" y="{champ_y}" width="{cw}" height="{bh}" '
        f'rx="10" fill="#f5c542"/>'
        f'<text x="{cx:.0f}" y="{champ_y + bh / 2 - 2:.0f}" font-size="{fs_team + 1}" '
        f'font-weight="800" fill="#1a1300" text-anchor="middle">\U0001F3C6 '
        f'{escape(_short(champion))}</text>'
        f'<text x="{cx:.0f}" y="{champ_y + bh / 2 + 13:.0f}" font-size="{fs_pct}" '
        f'fill="#5a4a00" text-anchor="middle">projected champion · '
        f'{_pct(champ_prob)} to win</text>')

    s.append("</svg>")
    return "".join(s)
