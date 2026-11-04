"""Wire the four new pairs into the rest of the site (data, homepage, counts, guides, sitemap, README). Idempotent."""
import glob, html, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from model import compute
from pairfix import excerpt
from pairdata13 import NEW13
from hubs import SHORT

NEW = list(NEW13)
OLD_N, NEW_N = 55, 55 + len(NEW)
def rd(f): return open(f, encoding="utf-8").read()
def wr(f, s): open(f, "w", encoding="utf-8").write(s)
def one(s, a, b, f=""):
    if b in s and a not in s: return s
    assert s.count(a) == 1, (f, a[:70], s.count(a)); return s.replace(a, b)

D = json.load(open("data/integration-pairs.json", encoding="utf-8"))
NAME = {sl: t["name"] for sl, t in D["tools"].items()}

# 1. open data
have = {p["pair"] for p in D["pairs"]}
for pair in NEW:
    s = rd(f"stack/{pair}/index.html"); d = json.loads(re.search(r'id="calc-data">(.*?)</script>', s, re.S).group(1)); v = compute(d)
    m = re.search(r'Sources \(checked [^)]*\): (.*?)</p>', s, re.S)
    e = {"pair": pair, "url": f"https://stackcostmatrix.com/stack/{pair}/", "tools": [t["name"] for t in d["tools"]],
         "connection_type": "native" if v["native"] else "middleware", "minimum_plans": {t["name"]: t["required"] for t in d["tools"]},
         "middleware_monthly_usd": d["middleware"]}
    if d.get("middlewareAnnual") is not None: e["middleware_annual_billing_usd_per_month"] = d["middlewareAnnual"]
    e.update({"sync_direction": re.search(r'Data sync direction</td> <td class="px-4 py-3" colspan="2">(.*?)</td>', s, re.S).group(1).strip(),
              "ten_seat_monthly_cost_usd": round(v["N"], 2),
              "verification": html.unescape(re.search(r"<span>((?:Integration requirements|Prices checked)[^<]*)</span>", s).group(1)),
              "last_reviewed": "2026-11-04", "date_modified": "2026-11-04",
              "sources": [{"title": html.unescape(t), "url": html.unescape(u)} for u, t in re.findall(r'<a href="([^"]+)"[^>]*>(.*?) ↗</a>', m.group(1))]})
    D["pairs"] = [p for p in D["pairs"] if p["pair"] != pair] + [e]
D["pairs"].sort(key=lambda p: p["pair"])
wr("data/integration-pairs.json", json.dumps(D, indent=1, ensure_ascii=False))
assert len(D["pairs"]) == NEW_N, len(D["pairs"])

# 2. homepage cards (after the last card of the same first tool), counts
h = rd("index.html")
for pair, c in NEW13.items():
    if f'href="/stack/{pair}/"' in h: continue
    A, B = NAME[c["A"]], NAME[c["B"]]
    kind = "native" if c["native"] else "middleware"
    badge = ('<span class="shrink-0 rounded-full px-2.5 py-0.5 text-xs font-medium ring-1 bg-emerald-100 text-emerald-800 ring-emerald-200"> Native </span>' if c["native"]
             else '<span class="shrink-0 rounded-full px-2.5 py-0.5 text-xs font-medium ring-1 bg-sky-100 text-sky-800 ring-sky-200"> Middleware </span>')
    card = (f'<a href="/stack/{pair}/" data-search="{html.escape((A + " " + B).lower())} {pair} {c["cats"].replace("|", " ").lower()} {kind}" data-cats="{c["cats"]}" '
            'class="group flex flex-col rounded-xl border border-slate-200 bg-white p-5 shadow-sm transition hover:-translate-y-0.5 hover:shadow-md"> '
            f'<div class="flex items-center justify-between gap-2"> <h3 class="font-semibold text-slate-900 group-hover:text-indigo-700"> {html.escape(A)} + {html.escape(B)} </h3> {badge} </div> '
            f'<p class="mt-2 flex-1 text-sm leading-relaxed text-slate-600"> {html.escape(excerpt(c["summary"], 90), quote=False).replace(chr(39), "&#39;")} </p> '
            '<p class="mt-3 text-sm font-medium text-indigo-600">\nSee true cost &amp; setup guide →\n</p> </a>')
    starts = [m for m in re.finditer(r'<a href="/stack/(' + c["A"] + r'-and-[^/]+)/" data-search=', h)]
    anchor = starts[-1] if starts else list(re.finditer(r'<a href="/stack/[^/]+/" data-search=', h))[-1]
    end = h.index("</a>", anchor.start()) + 4
    h = h[:end] + card + h[end:]
h = one(h, '<p class="text-3xl font-bold">55</p>', f'<p class="text-3xl font-bold">{NEW_N}</p>', "home stat")
h = h.replace("Showing 55 of 55 integrations", f"Showing {NEW_N} of {NEW_N} integrations")
h = re.sub(r"middleware fees behind 55(\s)", rf"middleware fees behind {NEW_N}\1", h)
h = h.replace("Compare the true cost of 55 B2B software integrations", f"Compare the true cost of {NEW_N} B2B software integrations")
h = h.replace("true integration costs for 55 B2B software pairs", f"true integration costs for {NEW_N} B2B software pairs")
wr("index.html", h)

# 3. footer count + other count mentions on every page
for f in glob.glob("*.html") + glob.glob("*/index.html") + glob.glob("stack/*/index.html"):
    s = rd(f); s0 = s
    s = s.replace(">All 55 integration pairs</a>", f">All {NEW_N} integration pairs</a>")
    s = s.replace("Browse all 55 B2B integration cost calculators", f"Browse all {NEW_N} B2B integration cost calculators")
    if s != s0: wr(f, s)
a = rd("about/index.html"); a = a.replace("53 pricing plans, 55 integration pairs", f"53 pricing plans, {NEW_N} integration pairs"); wr("about/index.html", a)

# 4. guide tables
NATIVE = '<span class="rounded-full px-2 py-0.5 text-xs font-medium ring-1 bg-emerald-100 text-emerald-800 ring-emerald-200"> Native </span>'
MIDDLE = '<span class="rounded-full px-2 py-0.5 text-xs font-medium ring-1 bg-sky-100 text-sky-800 ring-sky-200"> Middleware </span>'
def row(pair, cells):
    c = NEW13[pair]; lab = f"{NAME[c['A']]} + {NAME[c['B']]}"
    mid = "".join(f'<td class="px-4 py-3">{x}</td> ' for x in cells)
    return (f'<tr class="border-t border-slate-100"> <td class="px-4 py-3 font-medium">{html.escape(lab)}</td> <td class="px-4 py-3"> {NATIVE if c["native"] else MIDDLE} </td> {mid}'
            f'<td class="px-4 py-3"> <a href="/stack/{pair}/" class="font-medium text-indigo-600 hover:underline">True-cost calculator →</a> </td> </tr>')
def add_rows(f, rows):
    s = rd(f)
    for pair, cells in rows:
        if f'href="/stack/{pair}/"' in s: continue
        i = s.index("</tbody>"); s = s[:i] + row(pair, cells) + " " + s[i:]
    wr(f, s)
add_rows("hubspot-integrations-cost/index.html", [("hubspot-and-quickbooks", ["Free"])])
s = rd("hubspot-integrations-cost/index.html")
s = s.replace("native vs middleware totals across 10 popular connections", "native vs middleware totals across 13 popular connections")
s = s.replace("of 12 popular HubSpot\n      integrations", "of 13 popular HubSpot\n      integrations")
wr("hubspot-integrations-cost/index.html", s)
add_rows("salesforce-integrations-cost/index.html", [("salesforce-and-quickbooks", ["Yes — +$25/user/mo on Professional"]), ("pipedrive-and-salesforce", ["Yes — +$25/user/mo on Professional"])])
add_rows("crm-integration-pricing-guide/index.html", [(p, []) for p in NEW])

# 5. sitemap
s = rd("sitemap-0.xml"); locs = re.findall(r"<url><loc>([^<]*)</loc></url>", s)
allu = sorted(set(locs) | {f"https://stackcostmatrix.com/stack/{p}/" for p in NEW})
s = re.sub(r"(<urlset[^>]*>).*(</urlset>)", lambda m: m.group(1) + "".join(f"<url><loc>{u}</loc></url>" for u in allu) + m.group(2), s, flags=re.S); wr("sitemap-0.xml", s)

# 6. README files
r = rd("README.md")
r = r.replace("**55 B2B software integration pairs**", f"**{NEW_N} B2B software integration pairs**").replace("**55 integration calculators**", f"**{NEW_N} integration calculators**")
r = r.replace("all 55 integration pairs, exported", f"all {NEW_N} integration pairs, exported").replace("### All 55 integration cost calculators", f"### All {NEW_N} integration cost calculators")
m = re.search(r"### All \d+ integration cost calculators\n(.*?)(\n\n|\Z)", r, re.S)
if m:
    lines = m.group(1).rstrip("\n").split("\n")
    sample = next(l for l in lines if "/stack/" in l)
    for pair, c in NEW13.items():
        if f"/stack/{pair}/" in r: continue
        a_, b_ = pair.split("-and-")
        lines.append(f"- [{a_.title()} + {b_.title()}](https://stackcostmatrix.com/stack/{pair}/)")
    lines = sorted(set(lines), key=lambda l: re.search(r"/stack/([^/]+)/", l).group(1) if "/stack/" in l else l)
    head = r[:m.start(1)]; tail = r[m.end(1):]
    r = head + "\n".join(lines) + tail
wr("README.md", r)
dr = rd("data/README.md").replace("all 55 integration pairs", f"all {NEW_N} integration pairs"); wr("data/README.md", dr)
print("wired", NEW, "pairs:", len(D["pairs"]), "sitemap:", len(allu))
