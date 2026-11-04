"""Generate per-tool integration hub pages from the live pair pages. Run from repo root.
   python3 hubs.py build   -> writes <tool>-integrations-cost/index.html for 16 tools, links them in
                              from the homepage, pair pages, existing hubs and the sitemap.
"""
import re, json, glob, html, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from model import compute, tiers, cost, cheapest_api, money

TODAY = "2026-11-03"
SITE = "https://stackcostmatrix.com"
EXISTING = {"hubspot": "/hubspot-integrations-cost/", "salesforce": "/salesforce-integrations-cost/"}
SHORT = {"salesforce": "Salesforce", "quickbooks": "QuickBooks", "monday": "Monday.com"}
PRICE_NOTE = {
    "activecampaign": "ActiveCampaign publishes annual-billing rates only, so these are per-month prices billed yearly. Prices re-checked Nov 3, 2026.",
    "pipedrive": "Pipedrive prices are per-seat annual-billing rates taken from an indexed copy of its pricing page, because pipedrive.com/pricing can't be read automatically.",
    "quickbooks": "QuickBooks Online prices were last verified Oct 17, 2026; Intuit's pricing pages couldn't be re-read on Nov 3.",
    "mailchimp": "Mailchimp prices are starting prices for up to 500 contacts; the price rises with your contact count, not seats.",
    "stripe": "Stripe has no monthly plan fee; it charges per transaction, so the calculators count it as $0/month.",
    "xero": "Xero prices are flat monthly prices per organisation, re-checked Nov 3, 2026.",
}
DEFAULT_NOTE = "Prices are monthly-billing list prices, re-checked on the vendor's pricing page on Nov 3, 2026; the annual-billing price is shown where the vendor publishes one."

def read(f): return open(f, encoding="utf-8").read()
def esc(s): return html.escape(s, quote=False).replace("'", "&#39;")
def attr(s): return html.escape(s, quote=True)
def m0(x): return money(x).replace(".00", "")

def about_sources():
    a = read("about/index.html")
    rows = re.findall(r'<td class="px-4 py-3 font-medium">([^<]+)</td> <td class="px-4 py-3"> <a href="([^"]+)"[^>]*>Pricing ↗</a> </td> <td class="px-4 py-3"> <a href="([^"]+)"', a)
    return {html.unescape(n): (p, d) for n, p, d in rows}

def parse_cell(cell):
    yn = re.match(r"\s*(Yes|No)", cell).group(1)
    lab = re.search(r"· ([^<]*?)\s*</span>", cell)
    return yn, html.unescape(lab.group(1).strip()) if lab else ""

def load_pairs():
    pairs = []
    for f in sorted(glob.glob("stack/*/index.html")):
        s = read(f); slug = f.split("/")[1]
        d = json.loads(re.search(r'id="calc-data">(.*?)</script>', s, re.S).group(1)); v = compute(d)
        by = html.unescape(re.search(r"<span>((?:Integration requirements|Prices checked)[^<]*)</span>", s).group(1))
        status = "pending" if "re-check pending" in by else ("partial: " + re.search(r"\(([^)]*unconfirmed)\)", by).group(1)) if "unconfirmed" in by else "verified"
        cells = {}
        for row, idx in (("API access at required tier", 0), ("Webhook support at required tier", 1)):
            m = re.search(row + r'</td> <td class="px-4 py-3">(.*?)</td> <td class="px-4 py-3">(.*?)</td> </tr>', s, re.S)
            for t, c in zip(d["tools"], m.groups()): cells.setdefault(t["slug"], [None, None])[idx] = parse_cell(c)
        sync = re.search(r'Data sync direction</td> <td class="px-4 py-3" colspan="2">(.*?)</td>', s, re.S).group(1).strip()
        mw = d["middleware"]; conn = None
        if mw: conn = {10.59: "Make Core", 29.99: "Zapier Professional", 15: "Data Mapper for Mailchimp"}.get(mw, "Middleware")
        pairs.append(dict(slug=slug, d=d, v=v, status=status, cells=cells, sync=sync, conn=conn))
    return pairs

def tool_cost(t, tier_name):
    tt = next(u for u in tiers(t) if u["tier_name"] == tier_name)
    return cost(tt, t["slug"])

def plan_price(p, min_seats_note=True):
    base, seat, ann, mins = p.get("monthly_base_usd", 0), p.get("monthly_per_seat_usd", 0), p.get("annual_billing_per_seat_usd_per_month"), p.get("min_seats", 1)
    if not base and not seat: return "Free"
    out = f"{m0(seat)}/seat/mo" if seat else f"{m0(base)}/mo"
    if ann is not None: out += f" ({m0(ann)} billed annually)"
    if mins > 1 and min_seats_note: out += f", min. {mins} seats"
    return out

BADGE = {True: '<span class="rounded-full px-2 py-0.5 text-xs font-medium ring-1 bg-emerald-100 text-emerald-800 ring-emerald-200"> Native </span>',
         False: '<span class="rounded-full px-2 py-0.5 text-xs font-medium ring-1 bg-sky-100 text-sky-800 ring-sky-200"> Middleware </span>'}
P = '<p class="mt-4 leading-relaxed text-slate-600">'
H2 = '<h2 class="mt-10 text-xl font-bold">'
TH = '<th class="px-4 py-3 font-semibold">'
TD = '<td class="px-4 py-3">'
LINK = 'class="font-medium text-indigo-600 hover:underline"'

def cnt(k, n, one, many):
    return f"{k} of the {n} {one if k == 1 else many}"

def join_names(xs):
    xs = list(xs)
    return xs[0] if len(xs) == 1 else ", ".join(xs[:-1]) + " and " + xs[-1]

def build_tool(slug, name, plans, pairs, sources, hubs):
    short = SHORT.get(slug, name)
    mine = [p for p in pairs if any(t["slug"] == slug for t in p["d"]["tools"])]
    api_plans = [dict(tier_name=k, base=v.get("monthly_base_usd", 0), perSeat=v.get("monthly_per_seat_usd", 0), minSeats=v.get("min_seats", 1)) for k, v in plans.items() if v.get("api_access")]
    floor_plan = min(api_plans, key=lambda u: cost(u, slug)); floor = cost(floor_plan, slug)
    rows = []
    for p in mine:
        me = next(t for t in p["d"]["tools"] if t["slug"] == slug); other = next(t for t in p["d"]["tools"] if t["slug"] != slug)
        forced = tool_cost(me, me["required"]) - floor
        A, B = p["d"]["tools"]
        rows.append(dict(p=p, me=me, other=other, forced=round(forced, 2), N=p["v"]["N"], label=f"{SHORT.get(A['slug'], A['name'])} + {SHORT.get(B['slug'], B['name'])}"))
    rows.sort(key=lambda r: (r["N"], r["other"]["name"]))
    n = len(rows); nat = [r for r in rows if r["p"]["v"]["native"]]; mid = [r for r in rows if not r["p"]["v"]["native"]]
    forced = sorted([r for r in rows if r["forced"] > 0.005], key=lambda r: -r["forced"])
    req_counts = {}
    for r in rows: req_counts[r["me"]["required"]] = req_counts.get(r["me"]["required"], 0) + 1
    lo, hi = rows[0], rows[-1]
    pend = [r for r in rows if r["p"]["status"] == "pending"]; part = [r for r in rows if r["p"]["status"].startswith("partial")]
    entry = next((pl for pl in plans if pl in req_counts), None)

    title = f"{short} Integration Costs (2026): Plans & Hidden Fees"
    desc_opts = [f"{short} integration costs in 2026: the minimum {short} plan, native vs middleware and 10-seat totals for {n} connections, from {m0(lo['N'])} to {m0(hi['N'])}/mo.",
                 f"{short} integration costs in 2026: minimum plans, native vs middleware and 10-seat totals for {n} connections."]
    desc = next(o for o in desc_opts if len(o) <= 155)
    url = f"{SITE}/{slug}-integrations-cost/"

    # intro
    tiers_txt = join_names(f"{k} ({c})" for k, c in sorted(req_counts.items(), key=lambda kv: -kv[1]))
    intro = (f"This page collects the {n} {esc(name)} integrations in the StackCostMatrix index: which {esc(short)} plan each one needs, "
             f"whether it's native or runs through middleware, and what the whole stack costs for a 10-person team. "
             f"{cnt(len(nat), n, 'connects', 'connect')} natively and {len(mid)} {'needs' if len(mid) == 1 else 'need'} a connector such as Make or Zapier. "
             f"By minimum {esc(short)} plan, the count is {esc(tiers_txt)}. "
             f"Ten-seat totals run from {money(lo['N'])}/mo ({esc(lo['label'])}) to {money(hi['N'])}/mo ({esc(hi['label'])}).")
    by = f"Built from the {n} pair calculators below · integration requirements checked Nov 3, 2026"
    if pend: by += f", except {len(pend)} pending re-check ({join_names(r['other']['name'] for r in pend)}), last checked Oct 17, 2026"
    if part: by += f"; {len(part)} with a plan still unconfirmed ({join_names(r['other']['name'] for r in part)})"
    by += "."

    # pairs table
    trs = []
    for r in rows:
        st = r["p"]["status"]
        chk = "Nov 3, 2026" if st == "verified" else ("Oct 17, 2026 (re-check pending)" if st == "pending" else "Nov 3, 2026 (" + st.split(": ", 1)[1] + ")")
        conn = "" if r["p"]["v"]["native"] else f'<span class="block text-xs text-slate-500">{esc(r["p"]["conn"])} {m0(r["p"]["d"]["middleware"])}/mo</span>'
        trs.append(f'<tr class="border-t border-slate-100"> <td class="px-4 py-3 font-medium">{esc(r["label"])}</td> {TD}{BADGE[r["p"]["v"]["native"]]}{conn}</td> '
                   f'{TD}{esc(r["me"]["required"])}</td> {TD}{esc(r["other"]["required"])}</td> {TD}{money(r["N"])}</td> {TD}<span class="text-xs text-slate-500">{esc(chk)}</span></td> '
                   f'{TD}<a href="/stack/{r["p"]["slug"]}/" {LINK}>Calculator →</a></td> </tr>')
    table = (f'<div class="mt-8 overflow-x-auto rounded-xl border border-slate-200 bg-white shadow-sm"> <table class="spec-matrix w-full min-w-[640px] text-sm"> <thead class="bg-slate-50"> <tr class="text-left"> '
             f'{TH}Integration</th> {TH}Type</th> {TH}Min. {esc(short)} plan</th> {TH}Other tool&#39;s plan</th> {TH}10-seat total</th> {TH}Checked</th> {TH}Details</th> </tr> </thead> <tbody> {"".join(trs)} </tbody> </table> </div>'
             f'<p class="mt-3 text-xs text-slate-500">Totals are monthly-billing prices for 10 seats on the minimum plans, including any connector fee. Open a calculator to change team size, switch to annual billing or add usage costs.</p>')

    # plans table
    facts = {}
    for r in rows:
        api, wh = r["p"]["cells"][slug]
        facts.setdefault(r["me"]["required"], (api, wh))
    ptr = []
    for pl, pd in plans.items():
        api, wh = facts.get(pl, (None, None))
        f = lambda x: (f'{x[0]} <span class="block text-xs text-slate-500">{esc(x[1])}</span>' if x else '<span class="text-xs text-slate-500">Not checked here (no pair needs this plan)</span>')
        ptr.append(f'<tr class="border-t border-slate-100"> <td class="px-4 py-3 font-medium">{esc(pl)}</td> {TD}{esc(plan_price(pd))}</td> {TD}{f(api)}</td> {TD}{f(wh)}</td> {TD}{req_counts.get(pl, 0)}</td> </tr>')
    plan_tbl = (f'{H2}{esc(short)} plans, API access and webhooks</h2> {P}API and webhook facts are listed for the plans that at least one integration below requires, with the date each was checked against {esc(short)}&#39;s documentation. {esc(PRICE_NOTE.get(slug, DEFAULT_NOTE))} <a href="/{slug}-api-access/" {LINK}>Every {esc(short)} plan&#39;s API access, limits and webhooks →</a></p> '
                f'<div class="mt-6 overflow-x-auto rounded-xl border border-slate-200 bg-white shadow-sm"> <table class="spec-matrix w-full min-w-[640px] text-sm"> <thead class="bg-slate-50"> <tr class="text-left"> '
                f'{TH}Plan</th> {TH}Price</th> {TH}API access</th> {TH}Webhooks</th> {TH}Integrations that need it</th> </tr> </thead> <tbody> {"".join(ptr)} </tbody> </table> </div>')

    # hidden cost section
    if forced:
        items = "; ".join(f"{esc(r['label'])} needs {esc(r['me']['required'])} (+{money(r['forced'])}/mo)" for r in forced)
        trap = (f'{H2}Where {esc(short)} forces an upgrade</h2> {P}{cnt(len(forced), n, 'integrations needs', 'integrations need')} a more expensive {esc(short)} plan than {esc(floor_plan['tier_name'])}, {esc(short)}&#39;s cheapest plan with API access. The extra {esc(short)} cost at 10 seats: {items}. '
                f'That gap is the hidden cost: you pay it every month even if you only wanted the integration. Each pair&#39;s "Hidden Cost Trap" box shows the full breakdown.</p>')
    else:
        trap = (f'{H2}Does {esc(short)} force an upgrade?</h2> {P}Not for any of the {n} integrations here: each one works on {esc(short)}&#39;s cheapest plan with API access, so the integration itself adds no {esc(short)} upgrade cost. '
                f'Any extra cost comes from the other tool&#39;s plan or from a connector fee, shown in the table above.</p>')
    # middleware section
    if mid:
        mtxt = "; ".join(f"{esc(r['label'])} ({esc(r['p']['conn'])}, {money(r['p']['d']['middleware'])}/mo)" for r in mid)
        mw = (f'{H2}Which {esc(short)} integrations need middleware</h2> {P}{cnt(len(mid), n, 'has', 'have')} no native connector and {'runs' if len(mid) == 1 else 'run'} through a third-party service: {mtxt}. '
              f'Connector fees are the monthly-billing price; the calculators use the lower annual-billing price (Make Core $9, Zapier Professional $19.99, Data Mapper $12.75) when you switch on annual billing. '
              f'Real usage can push Make or Zapier onto a bigger plan, so check your expected volume.</p>')
    else:
        mw = f'{H2}Which {esc(short)} integrations need middleware</h2> {P}None of the {n}: every {esc(short)} integration here has a native connector, so there&#39;s no Make or Zapier fee unless you choose one.</p>'

    # FAQ
    hi_req = [r for r in rows if entry and r["me"]["required"] != entry]
    q1 = f"Which {short} plan do I need for integrations?"
    a1 = (f"Of the {n} {short} integrations in this index, {req_counts.get(entry, 0)} work on {short}'s {entry} plan." +
          (f" The rest need a higher plan: " + "; ".join(f"{r['other']['name']} needs {short} {r['me']['required']}" for r in hi_req) + "." if hi_req else " None needs a higher plan.") +
          " Each pair's calculator shows the exact minimum plan on both sides.")
    q2 = f"Which {short} integrations need Zapier or Make?"
    a2 = (f"{cnt(len(mid), n, 'has', 'have')} no native connector: " + "; ".join(f"{r['other']['name']} ({r['p']['conn']}, {money(r['p']['d']['middleware'])}/month)" for r in mid) + "." if mid
          else f"None of the {n} integrations here; each has a native connector.")
    q3 = f"How much does a {short} integration cost for a 10-person team?"
    a3 = (f"Including both tools' minimum plans and any connector fee, the 10-seat monthly totals range from {money(lo['N'])} ({lo['label']}) "
          f"to {money(hi['N'])} ({hi['label']}), at monthly-billing prices.")
    faqs = [(q1, a1), (q2, a2), (q3, a3)]
    faq_html = (' <section class="mt-12" aria-label="Frequently asked questions"> <h2 class="text-xl font-bold">Frequently asked questions</h2> <div class="mt-4 space-y-6"> ' +
                "".join(f'<div> <h3 class="font-semibold text-slate-900">{esc(q)}</h3> <p class="mt-1 leading-relaxed text-slate-700">{esc(a)}</p> </div>' for q, a in faqs) + ' </div> </section>')

    # sources
    names = [name] + sorted({r["other"]["name"] for r in rows})
    src = []
    for nm in names:
        if nm not in sources: continue
        pu, du = sources[nm]
        src.append(f'<a href="{attr(pu)}" rel="noopener" class="rounded-xl border border-slate-200 bg-white px-4 py-3 text-sm shadow-sm transition hover:shadow-md"><span class="font-semibold text-slate-900">{esc(nm)}</span> <span class="text-slate-500">— official pricing ↗</span></a>')
        if nm == name:
            src.append(f'<a href="{attr(du)}" rel="noopener" class="rounded-xl border border-slate-200 bg-white px-4 py-3 text-sm shadow-sm transition hover:shadow-md"><span class="font-semibold text-slate-900">{esc(nm)}</span> <span class="text-slate-500">— API docs ↗</span></a>')
    sources_html = (f'{H2}Vendor sources</h2> <p class="mt-3 text-sm text-slate-500">Each pair page lists the specific help-center and developer-docs pages behind its facts.</p> <div class="mt-4 grid gap-3 sm:grid-cols-2"> {" ".join(src)} </div>'
                    f' <p class="mt-4 text-sm text-slate-500">\nFull 20-tool source index: <a href="/about/" {LINK}>About StackCostMatrix →</a> </p>')
    others = " · ".join(f'<a href="{u}" {LINK}>{esc(nm)}</a>' for s2, (nm, u) in sorted(hubs.items(), key=lambda kv: kv[1][0].lower()) if s2 != slug)
    nav = f'{H2}Integration costs by tool</h2> <p class="mt-3 leading-relaxed text-slate-600">{others}</p>'

    body = (f'<section class="mx-auto max-w-4xl"> <p class="text-sm font-semibold uppercase tracking-widest text-indigo-600">Tool guide</p> '
            f'<h1 class="mt-2 text-3xl font-bold tracking-tight sm:text-4xl">\n{esc(short)} Integration Costs (2026): Minimum Plans, API Access &amp; Hidden Fees\n</h1> '
            f'<p class="mt-3 text-sm text-slate-500">{esc(by)}</p> {P}\n{intro}\n</p> {table} {trap} {mw} {plan_tbl} {sources_html} {nav}{faq_html} </section> ')

    ld = [
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]},
        {"@context": "https://schema.org", "@type": "TechArticle", "headline": f"{short} Integration Costs (2026): Minimum Plans, API Access & Hidden Fees", "description": desc,
         "author": {"@type": "Organization", "name": "StackCostMatrix", "url": f"{SITE}/", "email": "admin@stackcostmatrix.com"}, "datePublished": TODAY, "dateModified": TODAY,
         "citation": [sources[name][0], sources[name][1]] if name in sources else [], "mainEntityOfPage": url,
         "publisher": {"@type": "Organization", "name": "StackCostMatrix", "url": f"{SITE}/", "logo": f"{SITE}/icon-512.png"}, "image": f"{SITE}/icon-512.png", "inLanguage": "en"},
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
            {"@type": "ListItem", "position": 2, "name": f"{short} integration costs", "item": url}]},
    ]
    return dict(title=title, desc=desc, url=url, body=body, ld=ld, n=n)

def render(tpl, page):
    s = tpl
    s = re.sub(r"<title>.*?</title>", lambda m: f"<title>{esc(page['title']).replace('&#39;', "'")}</title>", s, count=1)
    for pat in (r'(<meta name="description" content=")[^"]*(")', r'(<meta property="og:description" content=")[^"]*(")'):
        s = re.sub(pat, lambda m: m.group(1) + attr(page["desc"]) + m.group(2), s, count=1)
    s = re.sub(r'(<meta property="og:title" content=")[^"]*(")', lambda m: m.group(1) + attr(page["title"]) + m.group(2), s, count=1)
    s = re.sub(r'(<link rel="canonical" href=")[^"]*(")', lambda m: m.group(1) + page["url"] + m.group(2), s, count=1)
    s = re.sub(r'(<meta property="og:url" content=")[^"]*(")', lambda m: m.group(1) + page["url"] + m.group(2), s, count=1)
    head_end = s.index("</head>")
    s = re.sub(r'<script type="application/ld\+json">.*?</script>', "", s[:head_end], flags=re.S) + s[head_end:]
    head_end = s.index("</head>")
    s = s[:head_end] + "".join('<script type="application/ld+json">' + json.dumps(o, ensure_ascii=False, separators=(",", ":")) + "</script>" for o in page["ld"]) + s[head_end:]
    a = s.index('<main class="mx-auto max-w-6xl px-4 py-8 sm:px-6 sm:py-12">') + len('<main class="mx-auto max-w-6xl px-4 py-8 sm:px-6 sm:py-12">')
    b = s.index("</main>")
    return s[:a] + "  " + page["body"] + " " + s[b:]

def main():
    D = json.load(open("data/integration-pairs.json", encoding="utf-8"))
    pairs = load_pairs(); sources = about_sources()
    cnt = {sl: sum(1 for p in pairs if any(t["slug"] == sl for t in p["d"]["tools"])) for sl in D["tools"]}
    hubs = {sl: (SHORT.get(sl, t["name"]), EXISTING.get(sl, f"/{sl}-integrations-cost/")) for sl, t in D["tools"].items() if sl in EXISTING or cnt[sl] >= 3}
    tpl = read("hubspot-integrations-cost/index.html")
    built = []
    for sl, t in D["tools"].items():
        if sl in EXISTING or sum(1 for p in pairs if any(t["slug"] == sl for t in p["d"]["tools"])) < 3: continue
        page = build_tool(sl, t["name"], t["plans"], pairs, sources, hubs)
        os.makedirs(f"{sl}-integrations-cost", exist_ok=True)
        open(f"{sl}-integrations-cost/index.html", "w", encoding="utf-8").write(render(tpl, page)); built.append((sl, page))
        print(f"{sl}: {page['n']} pairs | {len(page['title'])} | {len(page['desc'])} | {page['title']}")
    json.dump({sl: dict(name=hubs[sl][0], url=hubs[sl][1]) for sl in hubs}, open(os.path.join(os.path.dirname(__file__), "hubs.json"), "w"), indent=1)

if __name__ == "__main__":
    main()
