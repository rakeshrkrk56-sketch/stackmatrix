"""Rebuild sitemap-0.xml from the pages on disk, with <lastmod> for each URL.
lastmod = the page's JSON-LD dateModified when it has one, otherwise the date of the file's last git commit
(or today for a file not committed yet). Run from the repo root after page changes: python3 scripts/sitemap16.py"""
import datetime, glob, json, os, re, subprocess

SITE = "https://stackcostmatrix.com"
SKIP = ("site/", "scripts/", "agent_scripts/", "go/", "data/", "_astro/")
HEAD = ('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
        'xmlns:news="http://www.google.com/schemas/sitemap-news/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml" '
        'xmlns:image="http://www.google.com/schemas/sitemap-image/1.1" xmlns:video="http://www.google.com/schemas/sitemap-video/1.1">')

def lastmod(f):
    s = open(f, encoding="utf-8").read()
    dates = [m for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)
             for m in re.findall(r'"dateModified":\s*"(\d{4}-\d{2}-\d{2})', b)]
    if dates: return max(dates)
    out = subprocess.run(["git", "log", "-1", "--format=%cs", "--", f], capture_output=True, text=True).stdout.strip()
    if out and not subprocess.run(["git", "diff", "--quiet", "HEAD", "--", f]).returncode: return out
    return datetime.date.today().isoformat()

def main():
    files = sorted(f for f in glob.glob("index.html") + glob.glob("*/index.html") + glob.glob("stack/*/index.html") if not f.startswith(SKIP))
    urls = []
    for f in files:
        s = open(f, encoding="utf-8").read()
        if 'name="robots" content="noindex' in s: continue
        path = "" if f == "index.html" else f[:-len("index.html")]
        key = f.split("/")[-2] if "/" in f else ""
        img = f"{SITE}/og/{key}.jpg" if key and os.path.exists(f"og/{key}.jpg") else ""
        urls.append((f"{SITE}/{path}", lastmod(f), img))
    urls.sort()
    xml = HEAD + "".join(f"<url><loc>{u}</loc><lastmod>{d}</lastmod>" + (f"<image:image><image:loc>{i}</image:loc></image:image>" if i else "") + "</url>" for u, d, i in urls) + "</urlset>"
    open("sitemap-0.xml", "w", encoding="utf-8").write(xml)
    print(f"sitemap-0.xml: {len(urls)} URLs with lastmod, {sum(1 for u in urls if u[2])} with an image")

if __name__ == "__main__":
    main()
