"""Build the four new pair pages from structurally similar existing pages. Run from repo root.
Templates are copied, every tool-specific name/slug/URL is swapped, then the page is re-rendered with pairfix's
render_page and the parts render_page doesn't manage (title, H1, byline, dates, setup-time FAQ, related cards)
are rewritten here."""
import html, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pairfix
from pairfix import render_page, build_facts, money, read
from pairdata13 import NEW13, TIER_SOURCE, CHECKED
from hubs import about_sources, SHORT

D = json.load(open("data/integration-pairs.json", encoding="utf-8"))
SRC = about_sources()                        # display name -> (pricing url, api url)
NAME = {sl: t["name"] for sl, t in D["tools"].items()}
FAQ4 = {1: "Setup typically takes under 1 hour — an estimate based on a setup-difficulty rating of 1 out of 5, not a vendor-quoted time.",
        2: "Setup typically takes about 1–3 hours — an estimate based on a setup-difficulty rating of 2 out of 5, not a vendor-quoted time.",
        3: "Setup typically takes about half a day — an estimate based on a setup-difficulty rating of 3 out of 5, not a vendor-quoted time."}
MAKE_EX = "Make fee: $9 annual price Oct 17, 2026; $10.59 monthly price from third-party pricing reviews, Nov 3, 2026, as make.com blocks automated checks"
PRICE_EX = {"salesforce": "Salesforce prices: Oct 17, 2026", "quickbooks": "QuickBooks prices: Nov 4, 2026", "pipedrive": "Pipedrive prices: from an indexed copy of its pricing page"}
CARD = ('<a href="/stack/{slug}/" class="rounded-xl border border-slate-200 bg-white p-5 shadow-sm transition hover:-translate-y-0.5 hover:shadow-md"> '
        '<h3 class="font-semibold text-slate-900 hover:text-indigo-700"> {label} </h3> <p class="mt-1 text-xs font-medium text-slate-500"> {kind} </p> </a>')
LINK = 'class="font-medium text-indigo-600 hover:underline"'

def calc_tools(pair_cfg):
    out = []
    for slug in (pair_cfg["A"], pair_cfg["B"]):
        d = json.loads(re.search(r'id="calc-data">(.*?)</script>', read(f"stack/{TIER_SOURCE[slug]}/index.html"), re.S).group(1))
        t = next(x for x in d["tools"] if x["slug"] == slug)
        out.append(dict(name=NAME[slug], slug=slug, tiers=t["tiers"], required=pair_cfg["req"][slug]))
    return out

def all_pairs_with_new():
    pairs = {p["pair"]: p["connection_type"] for p in D["pairs"]}
    for p, c in NEW13.items(): pairs[p] = "native" if c["native"] else "middleware"
    return pairs

def label(pair):
    a, b = pair.split("-and-")
    return f"{SHORT.get(a, NAME[a])} + {SHORT.get(b, NAME[b])}" if a in NAME and b in NAME else pair

def build(pair, c, facts):
    tpl = c["template"]; old, new = c["swap"]
    s = read(f"stack/{tpl}/index.html")
    s = s.replace(tpl, pair)
    # URLs: old tool's pricing / API docs -> new tool's
    for i in (0, 1):
        s = s.replace(SRC[NAME[old]][i], SRC[NAME[new]][i])
    for pat in ('/go/{}"', 'data-tool="{}"', '/{}-integrations-cost/', '/{}-api-access/'):
        s = s.replace(pat.format(old), pat.format(new))
    s = s.replace(NAME[old], NAME[new])
    d = dict(tools=calc_tools(c), middleware=(c["mw"][0] if c["mw"] else 0), middlewareLabel=("Middleware" if c["mw"] else "No middleware required"))
    if c["mw"]: d["middlewareAnnual"] = c["mw"][1]
    s = re.sub(r'(<script type="application/json" id="calc-data">).*?(</script>)', lambda m: m.group(1) + json.dumps(d, separators=(",", ":"), ensure_ascii=False) + m.group(2), s, count=1, flags=re.S)
    s, v = render_page(s, pair, d, c["summary"], c["sync"], facts, date_modified="2026-11-04", copy=pairfix.COPY[pair], cta=True)
    A, B = NAME[c["A"]], NAME[c["B"]]; sA, sB = SHORT.get(c["A"], A), SHORT.get(c["B"], B)
    # title / H1 / og / WebPage name / breadcrumb
    title = next(o for o in (f"{sA} + {sB} Integration: How It Works & Cost (2026)", f"{sA} + {sB} Integration: Setup & Cost (2026)") if len(o) <= 60)
    h1 = f"{A} + {B} Integration (2026): How It Works, Setup & True Cost"
    s = re.sub(r"<title>.*?</title>", f"<title>{html.escape(title, quote=False)}</title>", s, count=1)
    s = re.sub(r'(<meta property="og:title" content=")[^"]*(")', lambda m: m.group(1) + html.escape(title, quote=True) + m.group(2), s, count=1)
    s = re.sub(r'(<h1 class="text-3xl font-bold tracking-tight sm:text-4xl">).*?(</h1>)', lambda m: m.group(1) + html.escape(h1, quote=False) + m.group(2), s, count=1, flags=re.S)
    s = re.sub(r'(<span class="text-slate-700">)[^<]*(</span> </nav>)', lambda m: m.group(1) + html.escape(f"{A} + {B}", quote=False) + m.group(2), s, count=1)
    def ld(m):
        o = json.loads(m.group(1))
        if o.get("@type") == "WebPage":
            o["name"] = h1; o["lastReviewed"] = "2026-11-04"; o["dateModified"] = "2026-11-04"
        if o.get("@type") == "BreadcrumbList": o["itemListElement"][-1]["name"] = f"{A} + {B}"
        if o.get("@type") == "FAQPage" and len(o["mainEntity"]) > 3: o["mainEntity"][3]["acceptedAnswer"]["text"] = FAQ4[c["difficulty"]]
        return '<script type="application/ld+json">' + json.dumps(o, ensure_ascii=False, separators=(",", ":")) + "</script>"
    s = re.sub(r'<script type="application/ld\+json">(.*?)</script>', ld, s, flags=re.S)
    # visible setup-time FAQ answer
    s = re.sub(r'(How long does it take to set up the [^<]* integration\?</h3> <p class="mt-1 leading-relaxed text-slate-700">)[^<]*(</p>)', lambda m: m.group(1) + html.escape(FAQ4[c["difficulty"]], quote=False) + m.group(2), s, count=1)
    # byline, last-checked lines, connection-type date
    ex = [PRICE_EX[t] for t in (c["A"], c["B"]) if t in PRICE_EX] + ([MAKE_EX] if c["mw"] else [])
    exs = f" ({'; '.join(ex)})" if ex else ""
    s = re.sub(r"<span>(?:Integration requirements|Prices checked)[^<]*</span>", f"<span>Integration requirements checked against official vendor docs · {CHECKED} · Prices checked · Nov 3, 2026{html.escape(exs, quote=False)}</span>", s, count=1)
    s = re.sub(r"(?:Prices last checked|Last checked): [^<·]*?(?= · Sources linked below\.|\s*</p>)", f"Last checked: {CHECKED}" + (" (exceptions listed at the top)" if ex else ""), s)
    s = re.sub(r'(Connection type</td> <td class="px-4 py-3" colspan="2">.*? · Verified )[A-Z][a-z]{2} \d+, 2026( </span>)', lambda m: m.group(1) + CHECKED + m.group(2), s, count=1, flags=re.S)
    # related integrations: hub + API links, then pairs that share a tool
    pairs = all_pairs_with_new()
    rel = sorted([p for p in pairs if p != pair and (set(p.split("-and-")) & {c["A"], c["B"]})], key=lambda p: (not (set(p.split("-and-")) & {c["A"]}), label(p)))[:6]
    hubs = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "hubs.json")))
    links = [f'<a href="{hubs[t]["url"]}" {LINK}>All {html.escape(hubs[t]["name"])} integrations →</a>' for t in (c["A"], c["B"]) if t in hubs]
    links += [f'<a href="/{t}-api-access/" {LINK}>{html.escape(SHORT.get(t, NAME[t]))} API access by plan →</a>' for t in (c["A"], c["B"])]
    cards = "".join(CARD.format(slug=p, label=html.escape(label(p)), kind="Native" if pairs[p] == "native" else "Middleware") for p in rel)
    sec = (f'<section class="mt-12" aria-label="Related integrations"> <h2 class="text-xl font-bold">Related integrations</h2> <p class="mt-2 text-sm text-slate-600">{" · ".join(links)}</p> '
           f'<p class="mt-2 text-sm text-slate-600">Part of our <a href="/crm-integration-pricing-guide/" {LINK}>CRM integration hidden-costs guide</a>.</p> '
           f'<div class="mt-4 grid gap-4 sm:grid-cols-2 lg:grid-cols-3"> {cards} </div> </section>')
    s = re.sub(r'<section class="mt-12" aria-label="Related integrations">.*?</section>', lambda m: sec, s, count=1, flags=re.S)
    return s, v

def cell_of(slug, tier, row):
    """The spec cell for (slug, tier) on an existing page, for facts render_page/cells8 don't rewrite."""
    import glob
    for f in sorted(glob.glob("stack/*/index.html")):
        if any(f"stack/{p}/" in f for p in NEW13): continue
        s = read(f); d = json.loads(re.search(r'id="calc-data">(.*?)</script>', s, re.S).group(1))
        m = re.search(row + r'</td> <td class="px-4 py-3">(.*?)</td> <td class="px-4 py-3">(.*?)</td> </tr>', s, re.S)
        for i, t in enumerate(d["tools"]):
            if t["slug"] == slug and t["required"] == tier: return m.group(i + 1)
    return None

def fix_cells(s, c):
    for i, slug in enumerate((c["A"], c["B"])):
        if slug != "salesforce": continue
        for row in ("API access at required tier", "Webhook support at required tier"):
            ref = cell_of(slug, c["req"][slug], row); assert ref, (slug, row)
            m = re.search(row + r'</td> <td class="px-4 py-3">(.*?)</td> <td class="px-4 py-3">(.*?)</td> </tr>', s, re.S)
            s = s[:m.start(i + 1)] + ref + s[m.end(i + 1):]
    return s

def main():
    facts = build_facts()
    for pair, c in NEW13.items():
        s, v = build(pair, c, facts)
        s = fix_cells(s, c)
        old = NAME[c["swap"][0]]
        body = re.sub(r'<section class="mt-12" aria-label="Related integrations">.*?</section>', "", s, flags=re.S)
        left = [m.start() for m in re.finditer(re.escape(c["swap"][0]), body, re.I)] + [m.start() for m in re.finditer(re.escape(old), body)]
        s_print = body
        os.makedirs(f"stack/{pair}", exist_ok=True)
        open(f"stack/{pair}/index.html", "w", encoding="utf-8").write(s)
        print(pair, money(v["N"]), "| leftovers of", c["swap"][0], len(left))
        for i in left[:6]: print("   …", re.sub(r"\s+", " ", s_print[max(0, i - 80):i + 60]))

if __name__ == "__main__":
    main()
