"""Static website generation: renders the markdown report as a styled
single-page site in outputs/site/ (deployable to any static host).

    python -m worldcup.site        # rebuild outputs/site/index.html
"""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

import markdown

OUT_DIR = Path(__file__).parent / "outputs"
SITE_DIR = OUT_DIR / "site"

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>World Cup 2026 — ML Predictions</title>
<style>
  :root {{
    --bg: #0e1320; --card: #161e31; --text: #e8ecf5; --muted: #93a0b8;
    --accent: #4cc38a; --accent2: #f5c542; --line: #26314f;
  }}
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0; background: var(--bg); color: var(--text);
    font: 16px/1.55 -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
      Helvetica, Arial, sans-serif;
  }}
  header.hero {{
    background: linear-gradient(135deg, #14532d 0%, #1d4ed8 100%);
    padding: 2.2rem 1rem 1.8rem; text-align: center;
  }}
  header.hero h1 {{ margin: 0 0 .4rem; font-size: 1.7rem; }}
  header.hero p {{ margin: .2rem 0; color: #dbeafe; font-size: .95rem; }}
  main {{ max-width: 960px; margin: 0 auto; padding: 1rem; }}
  h2 {{
    margin-top: 2.2rem; padding-bottom: .35rem; font-size: 1.25rem;
    border-bottom: 2px solid var(--line); color: var(--accent2);
  }}
  h3 {{ margin-top: 1.4rem; font-size: 1.05rem; color: var(--accent); }}
  p, li {{ color: var(--text); }}
  em {{ color: var(--muted); }}
  a {{ color: #7cb8ff; }}
  table {{
    border-collapse: collapse; width: 100%; margin: .8rem 0 1.2rem;
    font-size: .88rem; background: var(--card); border-radius: 8px;
    overflow: hidden; display: block; overflow-x: auto; white-space: nowrap;
  }}
  thead th {{
    background: #1f2a44; color: #cdd7ea; text-align: left;
    padding: .5rem .65rem; position: sticky; top: 0;
  }}
  td {{ padding: .42rem .65rem; border-top: 1px solid var(--line); }}
  tbody tr:nth-child(odd) {{ background: rgba(255,255,255,.02); }}
  tbody tr:hover {{ background: rgba(76,195,138,.08); }}
  strong {{ color: var(--accent); }}
  footer {{
    margin: 3rem 0 1rem; text-align: center; color: var(--muted);
    font-size: .8rem; padding: 0 1rem;
  }}
</style>
</head>
<body>
<header class="hero">
  <h1>&#9917; World Cup 2026 — ML Predictions</h1>
  <p>Machine-learned probabilities for every match, group and the road to the final</p>
  <p>Last updated {updated} UTC</p>
</header>
<main>
{body}
</main>
<footer>
  Gradient-boosted Poisson goal model + 100,000 Monte Carlo tournament
  simulations. Probabilities, not promises — refreshed after each match day.
</footer>
</body>
</html>
"""


def build_site() -> Path:
    md_text = (OUT_DIR / "report.md").read_text()
    # The H1 and generation line are replaced by the page hero.
    lines = md_text.splitlines()
    if lines and lines[0].startswith("# "):
        lines = lines[1:]
    body = markdown.markdown("\n".join(lines), extensions=["tables"])
    SITE_DIR.mkdir(parents=True, exist_ok=True)
    html = TEMPLATE.format(
        updated=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M"),
        body=body)
    out = SITE_DIR / "index.html"
    out.write_text(html)
    # Ship the machine-readable artifacts alongside the page.
    for csv in ("match_probabilities.csv", "tournament_projections.csv",
                "history.csv", "value_bets.csv"):
        src = OUT_DIR / csv
        if src.exists():
            (SITE_DIR / csv).write_bytes(src.read_bytes())
    return out


if __name__ == "__main__":
    print(f"Wrote {build_site()}")
