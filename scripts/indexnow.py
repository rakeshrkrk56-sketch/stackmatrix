"""Tell IndexNow which pages changed, so Bing (and the engines that share its feed) re-read them without waiting.

NOT part of the build, and never run automatically: it sends a request to an outside service. Run it only when the
owner says so, and only after the change is live on stackcostmatrix.com.

    python3 scripts/indexnow.py --since 2026-11-15          # dry run: lists the URLs it would send
    python3 scripts/indexnow.py --since 2026-11-15 --send   # sends them
    python3 scripts/indexnow.py --all --send                # every URL in the sitemap

What is sent: the site's host name, the IndexNow key, and the list of URLs. Nothing else, and nothing personal.
The key is the 32-character file name of <key>.txt in the site root. It is public by design: a search engine reads
that file to confirm the sender controls the site. Format checked against indexnow.org/documentation on Nov 15, 2026:
POST /indexnow with JSON {host, key, keyLocation, urlList}; 200 or 202 means accepted; one engine shares with the rest.
"""
import glob, json, os, re, sys, urllib.request

SITE = "https://stackcostmatrix.com"
ENDPOINT = "https://www.bing.com/indexnow"
UA = "Mozilla/5.0 (compatible; sitemap-notifier)"   # generic on purpose: no name or contact details in requests

def key():
    for f in glob.glob("*.txt"):
        k = os.path.basename(f)[:-4]
        if re.fullmatch(r"[0-9a-f]{32}", k) and open(f, encoding="utf-8").read().strip() == k: return k
    sys.exit("no IndexNow key file (<32 hex characters>.txt holding the same characters) in the site root")

def urls(since):
    xml = open("sitemap-0.xml", encoding="utf-8").read()
    return [u for u, d in re.findall(r"<loc>([^<]+)</loc><lastmod>(\d{4}-\d{2}-\d{2})</lastmod>", xml) if since is None or d >= since]

def get(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=30) as r: return r.status, r.read().decode("utf-8", "replace")

def main():
    a = sys.argv[1:]
    if "--all" in a: since = None
    elif "--since" in a and re.fullmatch(r"\d{4}-\d{2}-\d{2}", a[a.index("--since") + 1]): since = a[a.index("--since") + 1]
    else: sys.exit(__doc__)
    k = key(); us = urls(since)
    print(f"{len(us)} URLs" + (f" changed on or after {since}" if since else " (all)") + f"; key file {SITE}/{k}.txt")
    for u in us[:5]: print("  ", u)
    if len(us) > 5: print(f"   ... and {len(us) - 5} more")
    if "--send" not in a: print("Dry run. Add --send to submit them (ask the owner first)."); return
    if not us: return
    st, body = get(f"{SITE}/{k}.txt")
    if st != 200 or body.strip() != k: sys.exit(f"the key file is not live at {SITE}/{k}.txt (HTTP {st}); nothing sent")
    data = json.dumps({"host": SITE.split("//")[1], "key": k, "keyLocation": f"{SITE}/{k}.txt", "urlList": us}).encode("utf-8")
    req = urllib.request.Request(ENDPOINT, data=data, method="POST", headers={"Content-Type": "application/json; charset=utf-8", "User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=60) as r: st = r.status
    except urllib.error.HTTPError as e: st = e.code
    meaning = {200: "accepted", 202: "received; key check pending", 400: "bad request", 403: "key not valid", 422: "a URL is not on this host", 429: "too many requests"}
    print(f"IndexNow answered HTTP {st}: {meaning.get(st, 'unexpected')}")
    sys.exit(0 if st in (200, 202) else 1)

if __name__ == "__main__":
    main()
