"""2026-11-12, one-time: build the batch 1 pair pages (pairdata22.NEW22) from structurally similar existing pages.

Same method as newpairs.py: copy a template page that shares one tool with the new pair, swap every name, slug and
URL of the other tool, re-render it with pairfix.render_page, then rewrite the parts render_page doesn't manage:
title, H1, byline and dates, the spec cells of the swapped-in tool, the setup-time row and the related cards.

Run from the repo root, then wire22.py, then build_all.sh:  python3 scripts/newpairs22.py [--rebuild]
Without --rebuild it refuses to overwrite a page that already exists."""
import collections, copy, glob, html, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pairfix
from pairfix import render_page, build_facts, money, read, calc_data
from pairdata22 import NEW22, COPY22, CHECKED22, DATE22
from hubs import about_sources, SHORT
from apidata import TOOLS

D = json.load(open("data/integration-pairs.json", encoding="utf-8"))
NAME = {sl: t["name"] for sl, t in D["tools"].items()}
SRC = about_sources()                                   # display name -> (pricing url, api docs url)
OLD_PAGES = sorted(f for f in glob.glob("stack/*/index.html") if f.split("/")[1] not in NEW22)
SETUP_TIME = {1: "Under 1 hour", 2: "1–3 hours", 3: "Half a day"}   # the site's own estimate from its difficulty rating
PRICE_EX = {"salesforce": "Salesforce prices: Oct 17, 2026", "quickbooks": "QuickBooks prices: Nov 4, 2026",
            "pipedrive": "Pipedrive prices: from an indexed copy of its pricing page"}
MAKE_EX = "Make fee: $9 annual price Oct 17, 2026; $10.59 monthly price from third-party pricing reviews, Nov 3, 2026, as make.com blocks automated checks"
TIER_SOURCE = {"salesforce": "salesforce-and-stripe", "stripe": "stripe-and-slack", "mailchimp": "hubspot-and-mailchimp"}   # tiers kept only in pages
FREE = {"tier_name": "Free", "base": 0, "perSeat": 0, "minSeats": 1, "api": True}
ROWS = ("API available (distinct from native app)", "API access at required tier", "Webhook support at required tier")
CRM = {"hubspot", "salesforce", "pipedrive"}
LINK = 'class="font-medium text-indigo-600 hover:underline"'
CARD = ('<a href="/stack/{slug}/" class="rounded-xl border border-slate-200 bg-white p-5 shadow-sm transition hover:-translate-y-0.5 hover:shadow-md"> '
        '<h3 class="font-semibold text-slate-900 hover:text-indigo-700"> {label} </h3> <p class="mt-1 text-xs font-medium text-slate-500"> {kind} </p> </a>')


def row_re(row):
    return re.compile(r'(' + re.escape(row) + r'</td> <td class="px-4 py-3">)(.*?)(</td> <td class="px-4 py-3">)(.*?)(</td> </tr>)', re.S)


# what existing pages say, per tool: homepage URL (schema "about") and spec cells per tier
HOME, CELLS, HAS_FREE = {}, collections.defaultdict(collections.Counter), collections.defaultdict(set)
for f in OLD_PAGES:
    s = read(f); d = calc_data(s)
    for t in d["tools"]: HAS_FREE[t["slug"]].add(any(x["tier_name"] == "Free" for x in t["tiers"]))
    for blk in re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
        o = json.loads(blk)
        if o.get("@type") == "WebPage":
            for a in o.get("about", []): HOME.setdefault(a["name"], a["url"])
    for row in ROWS:
        m = row_re(row).search(s)
        for t, cell in zip(d["tools"], (m.group(2), m.group(4))):
            CELLS[(row, t["slug"], None if row == ROWS[0] else t["required"])][cell] += 1


def cell_for(row, slug, tier):
    """The cell an existing page shows for this tool (and tier); for a tier no page uses yet, the cell of another tier
    whose facts in apidata.py are identical, with the tier label changed."""
    key = (row, slug, None if row == ROWS[0] else tier)
    if CELLS.get(key): return CELLS[key].most_common(1)[0][0], "copied"
    keys = ("api", "api_note", "lim") if row == ROWS[1] else ("wh", "wh_note")
    plans = TOOLS[slug]["plans"]; want = plans[tier]
    for (r, sl, tr), cnt in sorted(CELLS.items(), key=lambda kv: str(kv[0])):
        if cnt and r == row and sl == slug and tr in plans and all(plans[tr].get(k) == want.get(k) for k in keys):
            cell = cnt.most_common(1)[0][0]
            new = cell.replace(f"('{tr}')", f"('{tier}')", 1)
            assert new != cell, key
            return new, f"from the '{tr}' cell (same facts in apidata)"
    # same Yes/No but a different note (e.g. Airtable's API-call limit): swap the note the way cells8.py writes it
    def note(p): return (p.get("api_note") or p.get("lim") or "") if row == ROWS[1] else (p.get("wh_note") or "")
    for (r, sl, tr), cnt in sorted(CELLS.items(), key=lambda kv: str(kv[0])):
        if cnt and r == row and sl == slug and tr in plans and plans[tr].get(keys[0]) == want.get(keys[0]) and note(plans[tr]):
            cell = cnt.most_common(1)[0][0]
            old_n = f'<span class="block text-xs text-slate-500">{html.escape(note(plans[tr]))}</span>'
            if old_n not in cell: continue
            new_n = f'<span class="block text-xs text-slate-500">{html.escape(note(want))}</span>' if note(want) else ""
            new = cell.replace(old_n, new_n, 1).replace(f"('{tr}')", f"('{tier}')", 1)
            return new, f"from the '{tr}' cell, note changed to {note(want)!r}"
    raise SystemExit(f"no cell for {key}")


def tiers_for(slug, req):
    if slug in pairfix.TOOL_TIERS: tiers = copy.deepcopy(pairfix.TOOL_TIERS[slug])
    else:
        d = calc_data(read(f"stack/{TIER_SOURCE[slug]}/index.html"))
        tiers = copy.deepcopy(next(t for t in d["tools"] if t["slug"] == slug)["tiers"])
    for x in tiers:
        if x.get("api") is None: x["api"] = True   # as pairfix does when a page has no flag for that tier
    always_free = HAS_FREE[slug] == {True}   # every existing page of this tool lists its Free tier (Airtable, HubSpot, Slack...)
    if req != "Free" and not always_free: tiers = [x for x in tiers if x["tier_name"] != "Free"]   # Calendly, Mailchimp: only when required
    if (req == "Free" or always_free) and not any(x["tier_name"] == "Free" for x in tiers): tiers.insert(0, dict(FREE))
    assert any(x["tier_name"] == req for x in tiers), (slug, req, [x["tier_name"] for x in tiers])
    return tiers


def label(pair, kinds):
    a, b = pair.split("-and-")
    return f"{SHORT.get(a, NAME[a])} + {SHORT.get(b, NAME[b])}"


def related(pair, c, kinds):
    A, B = NAME[c["A"]], NAME[c["B"]]
    rel = sorted([p for p in kinds if p != pair and set(p.split("-and-")) & {c["A"], c["B"]}],
                 key=lambda p: (not (set(p.split("-and-")) & {c["A"]}), label(p, kinds)))[:6]
    hubs = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "hubs.json")))
    links = [f'<a href="{hubs[t]["url"]}" {LINK}>All {html.escape(hubs[t]["name"])} integrations →</a>' for t in (c["A"], c["B"]) if t in hubs]
    links += [f'<a href="/{t}-api-access/" {LINK}>{html.escape(SHORT.get(t, NAME[t]))} API access by plan →</a>' for t in (c["A"], c["B"])]
    crm = (f' <p class="mt-2 text-sm text-slate-600">Part of our <a href="/crm-integration-pricing-guide/" {LINK}>CRM integration hidden-costs guide</a>.</p>'
           if {c["A"], c["B"]} & CRM else "")
    cards = "".join(CARD.format(slug=p, label=html.escape(label(p, kinds)), kind=kinds[p]) for p in rel)
    return (f'<section class="mt-12" aria-label="Related integrations"> <h2 class="text-xl font-bold">Integrations related to {html.escape(A)} + {html.escape(B)}</h2> '
            f'<p class="mt-2 text-sm text-slate-600">{" · ".join(links)}</p>{crm} '
            f'<div class="mt-4 grid gap-4 sm:grid-cols-2 lg:grid-cols-3"> {cards} </div> </section>')


def build(pair, c, facts, kinds, cells):
    tpl = c["template"]; old, new = c["swap"]
    s = read(f"stack/{tpl}/index.html").replace(tpl, pair)
    for i in (0, 1): s = s.replace(SRC[NAME[old]][i], SRC[NAME[new]][i])
    for pat in ('/go/{}"', 'data-tool="{}"', '/{}-integrations-cost/', '/{}-api-access/'):
        s = s.replace(pat.format(old), pat.format(new))
    a_old, a_new = f'"url":"{HOME[NAME[old]]}"', f'"url":"{HOME[NAME[new]]}"'
    assert s.count(a_old) == 1, (pair, a_old); s = s.replace(a_old, a_new)
    s = s.replace(NAME[old], NAME[new])
    d = dict(tools=[dict(name=NAME[t], slug=t, tiers=tiers_for(t, c["req"][t]), required=c["req"][t]) for t in (c["A"], c["B"])],
             middleware=(c["mw"][0] if c["mw"] else 0), middlewareLabel=("Middleware" if c["mw"] else "No middleware required"))
    if c["mw"]: d["middlewareAnnual"] = c["mw"][1]
    s, v = render_page(s, pair, d, c["summary"], c["sync"], facts, date_modified=DATE22, copy=COPY22[pair], cta=True)
    A, B = NAME[c["A"]], NAME[c["B"]]; sA, sB = SHORT.get(c["A"], A), SHORT.get(c["B"], B)
    title = next(o for o in (f"{sA} + {sB} Integration: How It Works & Cost (2026)", f"{sA} + {sB} Integration: Setup & Cost (2026)",
                             f"{sA} + {sB} Integration (2026)") if len(o) <= 60)
    h1 = f"{A} + {B} Integration (2026): How It Works, Setup & True Cost"
    s = re.sub(r"<title>.*?</title>", f"<title>{html.escape(title, quote=False)}</title>", s, count=1)
    s = re.sub(r'(<meta property="og:title" content=")[^"]*(")', lambda m: m.group(1) + html.escape(title, quote=True) + m.group(2), s, count=1)
    s = re.sub(r'(<h1 class="text-3xl font-bold tracking-tight sm:text-4xl">).*?(</h1>)', lambda m: m.group(1) + html.escape(h1, quote=False) + m.group(2), s, count=1, flags=re.S)
    s = re.sub(r'(<span class="text-slate-700">)[^<]*(</span> </nav>)', lambda m: m.group(1) + html.escape(f"{A} + {B}", quote=False) + m.group(2), s, count=1)
    def ld(m):
        o = json.loads(m.group(1))
        if o.get("@type") == "WebPage": o["name"] = h1; o["lastReviewed"] = DATE22; o["dateModified"] = DATE22
        if o.get("@type") == "BreadcrumbList": o["itemListElement"][-1]["name"] = f"{A} + {B}"
        return '<script type="application/ld+json">' + json.dumps(o, ensure_ascii=False, separators=(",", ":")) + "</script>"
    s = re.sub(r'<script type="application/ld\+json">(.*?)</script>', ld, s, flags=re.S)
    # byline, the "verified facts" date line, the connection-type date
    ex = [PRICE_EX[t] for t in (c["A"], c["B"]) if t in PRICE_EX] + ([MAKE_EX] if c["mw"] else [])
    exs = f" ({'; '.join(ex)})" if ex else ""
    by = f"<span>Integration requirements checked against official vendor docs · {CHECKED22} · Prices checked · Nov 3, 2026{html.escape(exs, quote=False)}</span>"
    s, n = re.subn(r"<span>(?:Integration requirements|Prices checked)[^<]*</span>", lambda m: by, s, count=1); assert n == 1, pair
    s, n = re.subn(r"(?:Prices last checked|Last checked|Requirements checked): [^<·]*?(?= · Sources linked below\.|\s*</p>)",
                   f"Requirements checked: {CHECKED22}; prices: Nov 3, 2026" + (" (exceptions listed at the top)" if ex else ""), s); assert n == 2, (pair, n)
    s, n = re.subn(r'(Connection type</td> <td class="px-4 py-3" colspan="2">.*? · Verified )[A-Z][a-z]{2} \d+, 2026( </span>)',
                   lambda m: m.group(1) + CHECKED22 + m.group(2), s, count=1, flags=re.S); assert n == 1, pair
    st = f' {SETUP_TIME[c["difficulty"]]} <span class="text-slate-500">(difficulty {c["difficulty"]}/5)</span> '
    s, n = re.subn(r'(Setup time</td> <td class="px-4 py-3" colspan="2">).*?(</td>)', lambda m: m.group(1) + st + m.group(2), s, count=1, flags=re.S)
    assert n == 1, pair
    # spec cells: both tools, the cells their own pages show for these tiers
    for row in ROWS:
        def fix(m):
            return m.group(1) + cells[(row, c["A"])] + m.group(3) + cells[(row, c["B"])] + m.group(5)
        s, n = row_re(row).subn(fix, s, count=1); assert n == 1, (pair, row)
    s, n = re.subn(r'<section class="mt-12" aria-label="Related integrations">.*?</section>', lambda m: related(pair, c, kinds), s, count=1, flags=re.S)
    assert n == 1, pair
    return s, v


def main():
    rebuild = "--rebuild" in sys.argv
    kinds = {p["pair"]: ("Native" if p["connection_type"] == "native" else "Middleware") for p in D["pairs"]}
    kinds.update({p: ("Native" if c["native"] else "Middleware") for p, c in NEW22.items()})
    facts = build_facts()
    plan = {}
    for pair, c in NEW22.items():
        cells = {}
        for t in (c["A"], c["B"]):
            for row in ROWS:
                cell, how = cell_for(row, t, c["req"][t]); cells[(row, t)] = cell
                if how != "copied": print(f"  {pair}: {t} '{c['req'][t]}' {row}: {how}")
            yn = [re.match(r"\s*(Yes|No)", cells[(r, t)]).group(1) for r in ROWS[1:]]
            facts.setdefault((t, c["req"][t]), tuple(yn))
            assert facts[(t, c["req"][t])] == tuple(yn), (pair, t)
        plan[pair] = cells
    for pair, c in NEW22.items():
        out = f"stack/{pair}/index.html"
        if os.path.exists(out) and not rebuild: raise SystemExit(f"{out} exists; pass --rebuild to overwrite")
        s, v = build(pair, c, facts, kinds, plan[pair])
        old = c["swap"][0]
        body = re.sub(r'<section class="mt-12" aria-label="Related integrations">.*?</section>', "", s, flags=re.S)
        body = re.sub(r'<script type="application/json" id="calc-data">.*?</script>', "", body, flags=re.S)
        names = {old, NAME[old], SHORT.get(old, NAME[old])}
        left = sorted({m.start() for n in names for m in re.finditer(r"\b" + re.escape(n) + r"\b", body, re.I)})
        os.makedirs(f"stack/{pair}", exist_ok=True)
        open(out, "w", encoding="utf-8").write(s)
        print(f"{pair}: {money(v['N'])}/mo for 10 seats | {'native' if v['native'] else 'middleware'} | upgrade {money(v['UP'])} | leftovers of {old}: {len(left)}")
        for i in left[:5]: print("     …", re.sub(r"\s+", " ", body[max(0, i - 90):i + 60]))


if __name__ == "__main__":
    main()
