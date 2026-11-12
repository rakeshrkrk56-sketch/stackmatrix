#!/usr/bin/env bash
# Starts the Google Search Console MCP server for Claude Code cloud sessions (see .mcp.json).
# Server: github.com/AminForou/mcp-gsc, PyPI package mcp-search-console. The version is pinned to the one whose
# code was read before adding it (0.4.2); read the new code before raising the pin.
#
# The Google service-account key is never stored in this repository. The site owner pastes the key file's JSON
# into an environment variable named GSC_SERVICE_ACCOUNT_JSON in the cloud environment's settings. This script
# writes it to a private temp file for the server and starts it in service-account mode. Add, delete-site and
# delete-sitemap tools stay off (GSC_ALLOW_DESTRUCTIVE is not set).
set -eu
if [ -z "${GSC_SERVICE_ACCOUNT_JSON:-}" ]; then
  echo "Search Console is not connected: GSC_SERVICE_ACCOUNT_JSON is not set in the environment (see CLAUDE.md)." >&2
  exit 1
fi
umask 077
key="$(mktemp -d)/gsc-service-account.json"
printf '%s' "$GSC_SERVICE_ACCOUNT_JSON" > "$key"
if ! python3 -c 'import json,sys; d=json.load(open(sys.argv[1])); assert d.get("type")=="service_account" and d.get("private_key")' "$key" 2>/dev/null; then
  echo "GSC_SERVICE_ACCOUNT_JSON is set but is not a service-account key file's JSON. Paste the whole downloaded file." >&2
  exit 1
fi
export GSC_CREDENTIALS_PATH="$key" GSC_SKIP_OAUTH=true GSC_DATA_STATE=all
exec uvx mcp-search-console==0.4.2
