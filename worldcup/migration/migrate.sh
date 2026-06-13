#!/bin/bash
# Migrate the World Cup predictor into its own standalone GitHub repo.
# Run from the root of your local ig-trading-bot clone, on your Mac.
#
# Requires the GitHub CLI (`brew install gh` then `gh auth login`).
# Creates a NEW public repo `worldcup-predictor` with the worldcup/ package
# at its root, a single-branch (main) hourly workflow, and pushes it.

set -euo pipefail

NEW_REPO="worldcup-predictor"
SRC="$(pwd)"

if [ ! -d "$SRC/worldcup" ]; then
  echo "Run this from the root of your ig-trading-bot clone (where worldcup/ lives)."; exit 1
fi
command -v gh >/dev/null || { echo "GitHub CLI 'gh' not found: brew install gh && gh auth login"; exit 1; }

OWNER="$(gh api user --jq .login)"
WORK="$(mktemp -d)/$NEW_REPO"
mkdir -p "$WORK/.github/workflows"

# Copy the package, excluding the throwaway model pickle (regenerated on first run).
rsync -a --exclude 'data/goal_model.pkl' "$SRC/worldcup" "$WORK/"
cp "$SRC/worldcup/migration/hourly.yml" "$WORK/.github/workflows/hourly.yml"

# Top-level README + .gitignore for the new repo.
cp "$SRC/worldcup/README.md" "$WORK/README.md"
printf '__pycache__/\n*.py[cod]\nworldcup/data/goal_model.pkl\n.venv/\n' > "$WORK/.gitignore"
# Drop the now-redundant nested migration/ and old in-repo workflow copies.
rm -rf "$WORK/worldcup/migration"

cd "$WORK"
git init -q -b main
git add -A
git commit -q -m "World Cup 2026 ML prediction engine (migrated to standalone repo)"
gh repo create "$NEW_REPO" --public --source=. --remote=origin --push \
  --description "ML-based 2026 FIFA World Cup prediction engine; hourly auto-updating site."

echo
echo "Pushed to https://github.com/$OWNER/$NEW_REPO"
echo "Next:"
echo "  1. Settings -> Pages -> Source: GitHub Actions"
echo "  2. Actions tab -> run 'Hourly World Cup prediction update' once to seed the site"
echo "  3. Point the launchd trigger at the new repo:"
echo "       edit ~/Library/Scripts/worldcup-trigger.sh -> REPO=\"$OWNER/$NEW_REPO\""
echo "       and WORKFLOW=\"hourly.yml\", then: launchctl kickstart -k gui/\$(id -u)/com.worldcup.predictor.hourly"
echo "  Site will be live at https://$OWNER.github.io/$NEW_REPO/"
