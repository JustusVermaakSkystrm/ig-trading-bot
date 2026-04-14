#!/bin/bash
# setup_deploy.sh — run once to initialise git and push to GitHub
# Usage: bash setup_deploy.sh

set -e   # stop on any error

PROJECT_DIR="/Users/justusvermaak/Documents/Claude/Projects/IG Trading"
cd "$PROJECT_DIR"

echo ""
echo "=== IG Trading Bot — Git Setup ==="
echo ""

# --- 1. Initialise git (skip if already done) ---
if [ ! -d ".git" ]; then
    echo "[1/4] Initialising git repository..."
    git init
    git branch -M main
else
    echo "[1/4] Git already initialised — skipping."
fi

# --- 2. Make sure data/ dir exists (model + CSV land here at runtime) ---
mkdir -p data

# --- 3. Stage and commit everything ---
echo "[2/4] Staging files..."
git add .
git status --short

echo ""
echo "[3/4] Creating initial commit..."
git commit -m "Initial commit: IG EURUSD automated spread betting bot" 2>/dev/null || \
    echo "       (nothing new to commit — already up to date)"

# --- 4. Print next steps ---
echo ""
echo "[4/4] Local git setup complete!"
echo ""
echo "Next: create a GitHub repo and run:"
echo ""
echo "  git remote add origin https://github.com/YOUR_USERNAME/ig-trading-bot.git"
echo "  git push -u origin main"
echo ""
echo "Then deploy on Railway — see instructions from Claude."
echo ""
