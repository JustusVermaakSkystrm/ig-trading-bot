#!/bin/sh
# docker-entrypoint.sh
# Writes credentials.json from the IG_CREDENTIALS environment variable,
# then starts the trading bot.
#
# Set this env var in Railway / Render / any cloud host:
#   IG_CREDENTIALS = <contents of your credentials.json, as a single-line JSON string>

set -e

if [ -n "$IG_CREDENTIALS" ]; then
    echo "$IG_CREDENTIALS" > /app/credentials.json
    echo "[entrypoint] credentials.json written from IG_CREDENTIALS env var"
elif [ ! -f /app/credentials.json ]; then
    echo "[entrypoint] ERROR: no credentials.json and IG_CREDENTIALS not set"
    exit 1
fi

exec "$@"
