#!/usr/bin/env bash
# Starts the Google Search Console MCP server for a session (see CLAUDE.md, "Search Console access").
#
# The Google service-account key comes from the GSC_SERVICE_ACCOUNT_JSON environment variable, which the owner sets
# in the cloud environment's settings as:   GSC_SERVICE_ACCOUNT_JSON='<the whole key file>'
# The single quotes matter: without them the settings keep only the first line of the file.
# The key is never stored in the repository and this script never prints any part of it.
set -eu
if [ -z "${GSC_SERVICE_ACCOUNT_JSON:-}" ]; then
  echo "Search Console is not connected: GSC_SERVICE_ACCOUNT_JSON is not set in the environment (see CLAUDE.md)." >&2
  exit 1
fi
umask 077
key="$(mktemp -d)/gsc-service-account.json"
python3 - "$key" <<'PY' || exit 1
import base64, json, os, re, sys

PEM = re.compile(r"-----BEGIN PRIVATE KEY-----(.+?)-----END PRIVATE KEY-----", re.S)
FIX = ("In the cloud environment's settings write it as GSC_SERVICE_ACCOUNT_JSON='...' with the whole downloaded "
       "key file between two straight single quotes.")

raw = os.environ["GSC_SERVICE_ACCOUNT_JSON"].strip()
if len(raw) > 1 and raw[0] == raw[-1] and raw[0] in "'\"":      # saved with the quotes still round it
    raw = raw[1:-1].strip()


def read(text):
    """The key file as a dict, or None. strict=False also takes a key whose \\n marks became real line breaks."""
    try:
        d = json.loads(text, strict=False)
    except ValueError:
        return None
    return d if isinstance(d, dict) and d.get("private_key") and d.get("client_email") else None


d = read(raw)
if d is None:                                                    # the file's text as base64
    try:
        d = read(base64.b64decode(raw, validate=True).decode("utf-8"))
    except ValueError:
        d = None
if d is None:                                                    # damaged JSON: the key and the email are what matter
    mail = re.search(r"[\w.+-]+@[\w.-]+\.gserviceaccount\.com", raw)
    if PEM.search(raw) and mail:
        d = {"private_key": PEM.search(raw).group(0), "client_email": mail.group(0)}
if d is None:
    if len(raw) < 200:
        sys.exit(f"GSC_SERVICE_ACCOUNT_JSON is only {len(raw)} characters long, so the key was cut off when it was "
                 f"saved, most likely at the first line break. {FIX}")
    sys.exit(f"GSC_SERVICE_ACCOUNT_JSON is set ({len(raw)} characters) but no service-account key could be read "
             f"from it. {FIX}")

# Write the private key as one clean PEM block, whatever shape it arrived in.
m = PEM.search(str(d["private_key"]))
body = re.sub(r"\\n|\s", "", m.group(1)) if m else ""
try:
    der = base64.b64decode(body, validate=True)
except ValueError:
    der = b""
if len(der) < 500:
    sys.exit("GSC_SERVICE_ACCOUNT_JSON was read, but the private key inside it is incomplete. Save the whole key "
             "file again; if that fails too, create a new JSON key for the service account and save that one.")
lines = "\n".join(body[i:i + 64] for i in range(0, len(body), 64))
d["private_key"] = f"-----BEGIN PRIVATE KEY-----\n{lines}\n-----END PRIVATE KEY-----\n"
d.setdefault("type", "service_account")
d.setdefault("token_uri", "https://oauth2.googleapis.com/token")
with open(sys.argv[1], "w", encoding="utf-8") as f:
    json.dump(d, f)
PY
export GSC_CREDENTIALS_PATH="$key" GSC_SKIP_OAUTH=true GSC_DATA_STATE=all
unset GSC_SERVICE_ACCOUNT_JSON
exec uvx mcp-search-console==0.4.2
