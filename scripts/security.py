"""Browser security headers for every page, written as <meta> tags (GitHub Pages can't send custom headers).

What it adds to each page, right after <meta charset>:
  - a Content-Security-Policy that only lets the page run its own scripts: the files in /_astro/ and the
    exact inline scripts on that page (by SHA-256 hash). Anything injected later, or loaded from another
    site, is blocked by the browser. Images may come only from this site and the three badge sites.
  - a Referrer-Policy, so other sites see only "stackcostmatrix.com", never the full page URL.
It also adds rel="noopener noreferrer" to links that open in a new tab.

Run from the repo root after any script that edits page scripts (pairfix, ui13, research, hubs, apipages...):
    python3 scripts/security.py          # write/update the tags
    python3 scripts/security.py check    # exit 1 if any page's policy is missing or out of date
check_all.sh runs the check.
"""
import base64, glob, hashlib, re, sys

IMG_HOSTS = ["https://startupfa.me", "https://fazier.com", "https://cdn-b.saashub.com"]  # footer badges
SKIP = {"googlefec91e27bb84e108.html"}  # Search Console verification file: leave byte-for-byte

def pages():
    fs = glob.glob("*.html") + glob.glob("*/index.html") + glob.glob("*/*/index.html") + glob.glob("go/*.html")
    return sorted(f for f in set(fs) if f not in SKIP and not f.startswith(("site/", "scripts/", "agent_scripts/")))

def inline_hashes(s):
    out = []
    for attrs, body in re.findall(r"<script([^>]*)>(.*?)</script>", s, re.S):
        if "src=" in attrs or re.search(r'type="application/(ld\+)?json"', attrs):
            continue  # external files are covered by 'self'; JSON blocks never run
        h = "'sha256-" + base64.b64encode(hashlib.sha256(body.encode("utf-8")).digest()).decode() + "'"
        if h not in out:
            out.append(h)
    return out

def policy(s):
    script = " ".join(["'self'"] + inline_hashes(s))
    return ("default-src 'self'; "
            f"script-src {script}; "
            "style-src 'self' 'unsafe-inline'; "
            f"img-src 'self' data: {' '.join(IMG_HOSTS)}; "
            "font-src 'self'; connect-src 'self'; object-src 'none'; base-uri 'self'; "
            "form-action 'self'; upgrade-insecure-requests")

CSP_RE = re.compile(r'<meta http-equiv="Content-Security-Policy" content="[^"]*">\n?')
REF_RE = re.compile(r'<meta name="referrer" content="[^"]*">\n?')
CHARSET_RE = re.compile(r"(<meta charset=\"?utf-8\"?>\n?)", re.I)

def secure(s):
    s = CSP_RE.sub("", s)
    s = REF_RE.sub("", s)
    nl = "\n" if re.search(r'<meta charset="?utf-8"?>\n', s, re.I) else ""
    tags = (f'<meta http-equiv="Content-Security-Policy" content="{policy(s)}">{nl}'
            f'<meta name="referrer" content="strict-origin-when-cross-origin">{nl}')
    s, n = CHARSET_RE.subn(lambda m: m.group(1) + tags, s, count=1)
    assert n == 1, "no <meta charset> found"
    def rel(m):
        a = m.group(0)
        if "noopener" in a:
            return a
        if 'rel="' in a:
            return a.replace('rel="', 'rel="noopener noreferrer ', 1)
        return a[:-1] + ' rel="noopener noreferrer">'
    return re.sub(r'<a [^>]*target="_blank"[^>]*>', rel, s)

def main():
    check = sys.argv[1:] == ["check"]
    bad = changed = 0
    for f in pages():
        s = open(f, encoding="utf-8").read()
        new = secure(s)
        if new != s:
            if check:
                print("security tags missing or out of date:", f); bad += 1
            else:
                open(f, "w", encoding="utf-8").write(new); changed += 1
    if check:
        print(f"security check: {len(pages())} pages, {bad} out of date" + (" (run: python3 scripts/security.py)" if bad else ""))
        sys.exit(1 if bad else 0)
    print(f"security tags: {changed} pages updated, {len(pages())} total")

if __name__ == "__main__":
    main()
