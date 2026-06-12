"""Official result confirmation via ESPN's public World Cup scoreboard.

The quarantine ledger's stability rule (three unchanged sightings) is a
heuristic; this module provides ground truth. ESPN's scoreboard API
reports a per-match completed flag and final score, so a result can be
accepted the moment the match is officially over — and rejected while in
progress regardless of what any snapshot claims.

Note: this endpoint is reachable from GitHub Actions runners (where the
hourly job runs) but not from restricted sandboxes; every failure path
degrades gracefully to the stability rule.
"""

from __future__ import annotations

import json
import urllib.request
from datetime import date, timedelta

SCOREBOARD_URL = ("https://site.api.espn.com/apis/site/v2/sports/soccer/"
                  "fifa.world/scoreboard?dates={d}")

# ESPN display names -> names used by our dataset.
ALIASES = {
    "usa": "United States", "united states": "United States",
    "czechia": "Czech Republic", "czech republic": "Czech Republic",
    "türkiye": "Turkey", "turkiye": "Turkey", "turkey": "Turkey",
    "côte d'ivoire": "Ivory Coast", "cote d'ivoire": "Ivory Coast",
    "ivory coast": "Ivory Coast",
    "cabo verde": "Cape Verde", "cape verde islands": "Cape Verde",
    "cape verde": "Cape Verde",
    "bosnia-herzegovina": "Bosnia and Herzegovina",
    "bosnia and herzegovina": "Bosnia and Herzegovina",
    "democratic republic of the congo": "DR Congo", "dr congo": "DR Congo",
    "congo dr": "DR Congo",
    "south korea": "South Korea", "korea republic": "South Korea",
    "iran": "Iran", "ir iran": "Iran",
    "curacao": "Curaçao", "curaçao": "Curaçao",
}


def _canon(name: str, known: set[str]) -> str | None:
    n = name.strip()
    if n in known:
        return n
    return ALIASES.get(n.lower())


def parse_scoreboard(payload: dict, known_teams: set[str]) -> list[dict]:
    """Extract completed matches as
    {home, away, home_score, away_score, date} in our team names."""
    out = []
    for ev in payload.get("events", []):
        try:
            status = ev["status"]["type"]
            if not (status.get("completed") or status.get("state") == "post"):
                continue
            comp = ev["competitions"][0]
            sides = {}
            for c in comp["competitors"]:
                team = _canon(c["team"]["displayName"], known_teams)
                if team is None:
                    raise KeyError(f"unmapped team {c['team']['displayName']}")
                sides[c["homeAway"]] = (team, int(c["score"]))
            out.append({
                "home": sides["home"][0], "home_score": sides["home"][1],
                "away": sides["away"][0], "away_score": sides["away"][1],
                "event_date": ev.get("date", ""),
            })
        except (KeyError, IndexError, ValueError) as e:
            print(f"  official: skipping event ({e})")
    return out


def fetch_official_results(days_back: int = 3, known_teams: set[str] | None = None,
                           ) -> list[dict]:
    """Completed World Cup matches over the recent window, [] on any failure."""
    known_teams = known_teams or set()
    results, seen = [], set()
    for delta in range(days_back, -1, -1):
        d = (date.today() - timedelta(days=delta)).strftime("%Y%m%d")
        try:
            req = urllib.request.Request(SCOREBOARD_URL.format(d=d),
                                         headers={"User-Agent": "worldcup-predictor"})
            with urllib.request.urlopen(req, timeout=20) as resp:
                payload = json.loads(resp.read())
        except Exception as e:  # network blocked / API down -> fallback rule
            print(f"  official: scoreboard fetch failed for {d}: {e}")
            continue
        for m in parse_scoreboard(payload, known_teams):
            key = frozenset((m["home"], m["away"]))
            if key not in seen:
                seen.add(key)
                results.append(m)
    return results
