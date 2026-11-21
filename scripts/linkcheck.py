"""Internal-link check, run by check_all.sh. It reads the built pages and fails on the faults that went unnoticed
before links24.py existed. Usage (from the repo root): python3 scripts/linkcheck.py

  1. every page in the sitemap can be reached from the homepage in three clicks or fewer
  2. every pair page is linked from at least three other pair pages (the related cards)
  3. every pair page links to the hub of each of its tools (where the tool has one) and to both API pages
  4. the homepage links to every hub and every API page
  5. no link in a page's main content has link text that says nothing about its target ("Calculator", "Read more")
  6. the footer's list of guides is the same on every page
  7. every link to a directory or partner site in the footer carries rel="nofollow" or "sponsored" (no link exchanges)
"""
import collections, glob, html, json, os, re, sys

SITE = "https://stackcostmatrix.com"
HERE = os.path.dirname(os.path.abspath(__file__))
VAGUE = {"calculator", "true-cost calculator", "click here", "here", "read more", "learn more", "more", "details", "link", "this page", "guide"}

def read(f): return open(f, encoding="utf-8").read()
def file_of(path): return (path.strip("/") + "/index.html") if path.strip("/") else "index.html"
def text(x): return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", x))).strip()

def main():
    paths = [u.replace(SITE, "") for u in re.findall(r"<loc>([^<]+)</loc>", read("sitemap-0.xml"))]
    pages = {p: read(file_of(p)) for p in paths}
    out = collections.defaultdict(set); main_out = collections.defaultdict(set); bad = []
    for p, s in pages.items():
        a, b = s.find("<main"), s.find("</main>")
        for m in re.finditer(r'<a\b([^>]*)>(.*?)</a>', s, re.S):
            h = re.search(r'href="(/[^"#?]*)', m.group(1))
            if not h: continue
            d = h.group(1) if h.group(1).endswith("/") or "." in h.group(1).rsplit("/", 1)[-1] else h.group(1) + "/"
            if d == p or d not in pages: continue
            out[p].add(d)
            if a <= m.start() < b:
                main_out[p].add(d)
                t = text(m.group(2)).rstrip("→↗ ").lower()
                if t in VAGUE: bad.append(f"vague link text '{text(m.group(2))}' on {p} -> {d}")
    # 1. click depth
    depth = {"/": 0}; q = ["/"]
    while q:
        x = q.pop(0)
        for d in sorted(out[x]):
            if d not in depth: depth[d] = depth[x] + 1; q.append(d)
    for p in paths:
        if depth.get(p, 99) > 3: bad.append(f"{p} is {depth.get(p, 'not reachable')} clicks from the homepage")
    # 2-4. pair pages, hubs, API pages
    hubs = {k: v["url"] for k, v in json.load(open(os.path.join(HERE, "hubs.json"), encoding="utf-8")).items()}
    apis = {k: v["url"] for k, v in json.load(open(os.path.join(HERE, "apipages.json"), encoding="utf-8")).items()}
    pairs = [p for p in paths if p.startswith("/stack/")]
    inbound = collections.Counter(d for p in pairs for d in main_out[p] if d.startswith("/stack/"))
    for p in pairs:
        if inbound[p] < 3: bad.append(f"{p} is linked from only {inbound[p]} other pair pages")
        tools = [t["slug"] for t in json.loads(re.search(r'id="calc-data">(.*?)</script>', pages[p], re.S).group(1))["tools"]]
        for t in tools:
            for kind, urls in (("hub", hubs), ("API page", apis)):
                if t in urls and urls[t] not in main_out[p]: bad.append(f"{p} does not link to the {t} {kind}")
    for kind, urls in (("hub", hubs), ("API page", apis)):
        for t, u in urls.items():
            if u not in main_out["/"]: bad.append(f"the homepage does not link to the {t} {kind}")
    # 6. footer
    navs = collections.Counter()
    for f in glob.glob("*.html") + glob.glob("*/index.html") + glob.glob("stack/*/index.html"):
        m = re.search(r'<nav aria-label="Site".*?</nav>', read(f), re.S)
        if m: navs[m.group(0)] += 1
    if len(navs) != 1: bad.append(f"the footer's guide list has {len(navs)} versions: {sorted(navs.values(), reverse=True)}")
    # 7. outbound footer links (directory badges and the like) must not pass ranking credit
    for f in glob.glob("*.html") + glob.glob("*/index.html") + glob.glob("stack/*/index.html"):
        s = read(f); i = s.find("</main>")
        if i < 0: continue
        for m in re.finditer(r'<a\b([^>]*)>', s[i:]):
            h = re.search(r'href="(https?://[^"]+)"', m.group(1))
            if not h or h.group(1).startswith(SITE): continue
            rel = (re.search(r'rel="([^"]*)"', m.group(1)) or [None, ""])[1].split()
            if not {"nofollow", "sponsored"} & set(rel): bad.append(f"{f}: footer link to {h.group(1)} has no nofollow or sponsored")
    for b_ in bad[:25]: print("  ", b_)
    vals = sorted(inbound[p] for p in pairs)
    print(f"link check: {len(paths)} pages, deepest {max(depth.values())} clicks from the homepage, pair pages linked from {vals[0]} to {vals[-1]} other pair pages, {len(bad)} problems")
    sys.exit(1 if bad else 0)

if __name__ == "__main__":
    main()
