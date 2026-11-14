#!/usr/bin/env bash
# Rebuild every generated page, in the one order that works. Usage (from the repo root): bash scripts/build_all.sh
# It runs the whole pipeline twice and fails if the second run changes anything, because every script must be
# repeatable (a script that edits its own earlier output differently each time has corrupted dates before).
# After it prints BUILD OK, run: bash scripts/check_all.sh
set -u
cd "$(dirname "$0")/.."
STEPS=("pairfix.py apply" hubs.py apipages.py hspro.py research.py ui13.py homefaq.py polish18.py polish19.py polish20.py polish21.py polish22.py og17.py ux18.py site16.py agent17.py sitemap16.py security.py)
run() {
  for c in "${STEPS[@]}"; do
    out=$(python3 scripts/$c 2>&1) || { echo "FAILED: $c"; echo "$out" | tail -15; return 1; }
  done
}
run || exit 1
a=$(git diff | sha256sum)
run || exit 1
b=$(git diff | sha256sum)
if [ "$a" = "$b" ]; then echo "BUILD OK (repeatable). Files changed since the last commit: $(git status --short | wc -l)"
else echo "BUILD NOT REPEATABLE: the second run changed files. Find the script that isn't idempotent before committing."; exit 1; fi
