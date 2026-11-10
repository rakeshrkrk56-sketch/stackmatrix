"""Build /integration-tax-2026/ from the live pair pages + open data. Run from repo root."""
import json, re, glob, html, os, sys, statistics as st
from collections import Counter
sys.path.insert(0, os.path.dirname(__file__))
from model import compute, cost, money
from hubs import render, read, esc, attr, SHORT, SITE, P, H2, TH, TD, LINK, load_pairs

# requirements flagged for a connector-by-connector re-check (see API-WEBHOOK-VERIFICATION.md)
RECHECK = set()  # Pipedrive Growth confirmed: "The Automations feature is only available on Advanced and higher plans"
SLUG = "integration-tax-2026"
URL = f"{SITE}/{SLUG}/"
BLUE, ORANGE, TRACK = "#2a78d6", "#eb6834", "#e1e0d9"
INK2, MUTED = "#52514e", "#898781"
def m0(x): return money(x).replace(".00", "")
def name(slug, D): return SHORT.get(slug, D["tools"][slug]["name"])

def floor_plan(D, slug):
    ps = [dict(tier_name=k, base=v.get("monthly_base_usd", 0), perSeat=v.get("monthly_per_seat_usd", 0), minSeats=v.get("min_seats", 1))
          for k, v in D["tools"][slug]["plans"].items() if v.get("api_access")]
    b = min(ps, key=lambda u: cost(u, slug)); return b["tier_name"], cost(b, slug)

def dataset():
    D = json.load(open("data/integration-pairs.json", encoding="utf-8"))
    pairs = {p["slug"]: p for p in load_pairs()}
    rows = []
    from pairdata13 import NEW13
    for slug, p in pairs.items():
        if slug in NEW13: continue   # report scope: the 55 pairs indexed when it was published (Nov 3, 2026)
        d, v = p["d"], p["v"]
        st_ = p["status"]; unconf = st_.split(": ", 1)[1].split(" ")[0] if st_.startswith("partial") else None
        parts = []
        for t, c in zip(d["tools"], (v["ca"], v["cb"])):
            fn, fc = floor_plan(D, t["slug"]); up = round(c - fc, 2)
            tname = name(t["slug"], D)
            confirmed = st_ == "verified" or (unconf is not None and not tname.startswith(unconf) and not t["name"].startswith(unconf))
            if (t["slug"], t["required"]) in RECHECK: confirmed = False
            parts.append(dict(slug=t["slug"], name=tname, req=t["required"], floor=fn, up=up, confirmed=confirmed and st_ != "pending"))
        up = round(sum(x["up"] for x in parts), 2); mw = d["middleware"]; tax = round(up + mw, 2)
        rows.append(dict(slug=slug, label=" + ".join(x["name"] for x in parts), native=v["native"], parts=parts, up=up, mw=mw, tax=tax,
                         total=v["N"], conn=p["conn"], status=st_, unconfirmed_up=round(sum(x["up"] for x in parts if not x["confirmed"]), 2)))
    rows.sort(key=lambda r: (-r["tax"], r["label"]))
    return D, rows

def stats(rows):
    n = len(rows); taxed = [r for r in rows if r["tax"] > 0.005]; forced = [r for r in rows if r["up"] > 0.005]
    conf_forced = [r for r in rows if r["up"] - r["unconfirmed_up"] > 0.005]
    S = dict(n=n, taxed=len(taxed), forced=len(forced), free=n - len(taxed), mid=sum(not r["native"] for r in rows),
             median_tax=st.median([r["tax"] for r in taxed]), median_up=st.median([r["up"] for r in forced]),
             share=sum(r["tax"] for r in rows) / sum(r["total"] for r in rows) * 100,
             up_share=sum(r["up"] for r in rows) / sum(r["tax"] for r in rows) * 100,
             max_tax=rows[0]["tax"], max_rows=[r for r in rows if abs(r["tax"] - rows[0]["tax"]) < 0.005],
             conf_forced=len(conf_forced), unconf_rows=[r for r in rows if r["unconfirmed_up"] > 0.005],
             top3_share=sum(r["tax"] for r in rows[:3]) / sum(r["tax"] for r in rows) * 100,
             mw_fees=sorted({r["mw"] for r in rows if r["mw"]}))
    # headline figures by group: a single median over both groups swings between them (bimodal)
    ftax = [r["tax"] for r in forced]; conn = [r["tax"] for r in rows if r["up"] <= 0.005 and r["mw"] > 0.005]
    q = st.quantiles(ftax, n=4, method="inclusive")
    S.update(forced_q1=q[0], forced_q3=q[2], forced_median=st.median(ftax), conn_n=len(conn), conn_min=min(conn), conn_max=max(conn))
    c = Counter(); amt = {}
    for r in rows:
        for x in r["parts"]:
            if x["up"] > 0.005: c[x["slug"]] += 1; amt.setdefault(x["slug"], []).append(x)
    S["by_tool"] = [(s, k, amt[s]) for s, k in c.most_common()]
    return S

def tile(label, value, sub):
    return (f'<div class="rounded-xl border border-slate-200 bg-white p-5 shadow-sm"> <p class="text-sm text-slate-500">{esc(label)}</p> '
            f'<p class="mt-1 text-3xl font-bold tracking-tight">{esc(value)}</p> <p class="mt-1 text-xs text-slate-500">{esc(sub)}</p> </div>')

def bar_rows(items, vmax, legend=True):
    """items: (label, href, [(value, color, segname)], total_text, tip). HTML bars: 14px thick, 2px gap, 4px rounded data-end."""
    out = []
    for label, href, segs, total, tip in items:
        segs = [s for s in segs if s[0] > 0.005]
        bars = ""
        for i, (val, col, nm) in enumerate(segs):
            last = i == len(segs) - 1
            bars += (f'<span style="display:block;height:14px;width:{val / vmax * 100:.3f}%;background:{col};'
                     f'border-radius:{"0 4px 4px 0" if last else "0"};{"margin-right:2px;" if not last else ""}"></span>')
        out.append(f'<div class="mt-3" role="listitem" tabindex="0" data-tip="{attr(tip)}" aria-label="{attr(tip)}" style="outline-offset:4px"> '
                   f'<div class="flex items-center justify-between gap-3 text-sm"><a href="{href}" class="font-medium text-slate-900 hover:text-indigo-700">{esc(label)}</a>'
                   f'<span class="text-slate-700" style="font-variant-numeric:tabular-nums">{esc(total)}</span></div> '
                   f'<div style="display:flex;margin-top:4px;border-left:1px solid #c3c2b7">{bars}</div> </div>')
    return "".join(out)

def legend(items):
    return '<div class="mt-4 flex flex-wrap items-center gap-4 text-xs text-slate-600">' + "".join(
        f'<span class="flex items-center gap-2"><span style="display:inline-block;width:12px;height:12px;border-radius:3px;background:{c}"></span>{esc(t)}</span>' for c, t in items) + "</div>"

def build():
    D, rows = dataset(); S = stats(rows)
    title = "The Integration Tax 2026: Hidden Costs of SaaS Integrations"
    rng = f"${round(S['forced_q1']):,}–${round(S['forced_q3']):,}"; crng = f"{m0(S['conn_min'])}–{m0(S['conn_max'])}"
    desc = next(d for d in (f"Original research: {S['taxed']} of {S['n']} SaaS integrations add a hidden monthly cost: usually {rng}/mo when a plan upgrade is forced, {crng} for a connector alone.",
                            f"Original research: {S['taxed']} of {S['n']} SaaS integrations add a hidden monthly cost, usually {rng}/mo when a plan upgrade is forced.") if len(d) <= 155)
    assert len(title) <= 60 and len(desc) <= 155, (len(title), len(desc))
    maxl = " and ".join(r["label"] for r in S["max_rows"])
    lead = (f"We priced {S['n']} of the most common B2B software integrations at the plans each one actually requires, then compared that with the cheapest plans that still include API access. "
            f"The difference, plus any connector fee for Make or Zapier, is the <strong>integration tax</strong>: what you pay every month only because two tools need to talk to each other.")
    tiles = ('<div class="mt-8 grid gap-4 sm:grid-cols-2 lg:grid-cols-4"> ' +
             tile("Integrations with a hidden cost", f"{S['taxed']} of {S['n']}", f"{S['forced']} force a plan upgrade ({S['conf_forced']} on confirmed requirements); {S['conn_n']} only need a connector") +
             tile("When a plan upgrade is forced", f"{rng}/mo", f"middle half of {S['forced']} integrations · median {money(S['forced_median'])} · 10 seats") +
             tile("When only a connector is needed", f"{crng}/mo", f"{S['conn_n']} integrations (Make, Zapier, Data Mapper)") +
             tile("Highest integration tax", f"{m0(S['max_tax'])}/mo", maxl) + ' </div>')
    # findings
    top_tool = S["by_tool"][0]
    cal = next((x for x in S["by_tool"] if x[0] == "calendly"), None)
    hs = next((x for x in S["by_tool"] if x[0] == "hubspot"), None)
    find = [
        f"<strong>Plan upgrades, not connectors, are the real cost.</strong> Forced upgrades make up {S['up_share']:.0f}% of the total integration tax, and across all {S['n']} stacks the integration tax is {S['share']:.0f}% of what they cost in total. Connector fees are small by comparison: "
        f"{', '.join(m0(x) for x in S['mw_fees'])} a month at monthly billing.",
        f"<strong>The tax is concentrated.</strong> The three most expensive integrations account for {S['top3_share']:.0f}% of all the integration tax in the index. "
        f"{maxl} each cost {m0(S['max_tax'])} a month extra because they need a HubSpot Professional subscription: Smart CRM Professional, the cheapest one, is $50 per seat a month (<a href=\"/hubspot-professional-integrations/\" class=\"font-medium text-indigo-600 hover:underline\">compare the Professional plans</a>)." if hs else "",
        (f"<strong>Calendly&#39;s webhook gate is the most common trigger.</strong> {cal[1]} integrations need Calendly Standard, because Calendly&#39;s webhooks require a paid plan; "
         f"that&#39;s {m0(cal[2][0]['up'])} a month for 10 seats.") if cal else "",
        f"<strong>{S['free']} of {S['n']} integrations cost nothing extra.</strong> They work on each tool&#39;s cheapest plan with API access and need no connector, so connecting them is free on top of the plans you already pay for.",
    ]
    findings = f'{H2}Key findings</h2> ' + "".join(f"{P}{x}</p>" for x in find if x)
    kinds = (f'{H2}Three kinds of integration cost</h2> '
             f'{P}&ldquo;What does a SaaS integration cost?&rdquo; can mean three different bills. This report measures the first two, because they&#39;re the ones a buyer of these tools actually meets.</p>'
             f'<ol class="scm-steps"> <li><strong>Plan upgrades (measured here).</strong> The integration only works on a higher plan of one of the tools. That&#39;s {S["up_share"]:.0f}% of the integration tax in this index, '
             f'typically {m0(S["forced_q1"])} to {m0(round(S["forced_q3"]))} a month for 10 seats when an upgrade is forced.</li> '
             f'<li><strong>Connector fees (measured here).</strong> There&#39;s no native app, so you pay for Make, Zapier or a similar service: {m0(S["conn_min"])} to {m0(S["conn_max"])} a month at list price, more at high volumes.</li> '
             f'<li><strong>Building it yourself (not measured here).</strong> If no native app or connector fits, someone writes and maintains a custom integration against both APIs. We don&#39;t measure that. '
             f'For scale, Albato, an integration-platform vendor and so not a neutral source, cites Chift&#39;s cost analysis for roughly $10,000 to $22,000 in the first year for one in-house API integration, development plus maintenance '
             f'(<a href="https://albato.com/blog/publications/embedded-ipaas-roi" rel="noopener" {LINK}>Albato ↗</a>, read Nov 10, 2026).</li> </ol>')
    figure = (f'<figure class="mt-6"> <img src="/og/integration-tax-2026.jpg" width="1200" height="630" loading="lazy" class="scm-fig" '
              f'alt="Bar chart: the {min(8, len(rows))} most expensive SaaS integrations by monthly integration tax for a 10-seat team, led by {esc(rows[0]["label"])} at {m0(rows[0]["tax"])} a month"> '
              f'<figcaption class="mt-2 text-xs text-slate-500">The most expensive integrations in the index, by monthly integration tax for 10 seats. Free to reuse with credit (CC BY 4.0).</figcaption> </figure>')
    # chart 1
    top = rows[:15]; vmax = max(r["tax"] for r in top)
    items = []
    for r in top:
        up_lbl = "; ".join(f"{x['name']} {x['req']} +{m0(x['up'])}" for x in r["parts"] if x["up"] > 0.005)
        tip = f"{r['label']}: integration tax {money(r['tax'])}/mo" + (f" — plan upgrades {money(r['up'])} ({up_lbl})" if r["up"] > 0.005 else "") + (f" — connector {money(r['mw'])} ({r['conn']})" if r["mw"] else "")
        items.append((r["label"], f"/stack/{r['slug']}/", [(r["up"], BLUE, "upgrade"), (r["mw"], ORANGE, "connector")], f"{money(r['tax'])}/mo", tip))
    chart1 = (f'{H2}The 15 most expensive integrations</h2> <p class="mt-3 text-sm text-slate-500">Monthly integration tax for a 10-seat team, split into forced plan upgrades and connector fees. Hover or focus a bar for the breakdown.</p>'
              + legend([(BLUE, "Forced plan upgrade"), (ORANGE, "Connector fee (Make, Zapier, Data Mapper)")]) +
              f'<div class="mt-4 rounded-xl border border-slate-200 bg-white p-5 shadow-sm" role="list" aria-label="Integration tax by integration">{bar_rows(items, vmax)}</div>')
    # chart 2
    tmax = max(k for _, k, _ in S["by_tool"]); items2 = []
    for s, k, xs in S["by_tool"]:
        med = st.median([x["up"] for x in xs]); plans = sorted({x["req"] for x in xs})
        tip = f"{name(s, D)}: forces an upgrade in {k} integration{'s' if k != 1 else ''} (to {', '.join(plans)}), median +{money(med)}/mo"
        items2.append((name(s, D), f"/{s}-integrations-cost/" if os.path.exists(f"{s}-integrations-cost") else f"/{s}-api-access/", [(k, BLUE, "count")],
                       f"{k} · median +{m0(med)}/mo" + (f" · {sum(not x['confirmed'] for x in xs)} unconfirmed" if any(not x["confirmed"] for x in xs) else ""), tip + (f"; {sum(not x['confirmed'] for x in xs)} of these rest on an unconfirmed plan requirement" if any(not x["confirmed"] for x in xs) else "")))
    chart2 = (f'{H2}Which tools force the upgrade</h2> <p class="mt-3 text-sm text-slate-500">Number of integrations in which each tool requires a plan above its cheapest plan with API access, with the median extra cost. "Unconfirmed" counts upgrades whose plan requirement is still due for a re-check.</p>'
              f'<div class="mt-4 rounded-xl border border-slate-200 bg-white p-5 shadow-sm" role="list" aria-label="Forced upgrades by tool">{bar_rows(items2, tmax)}</div>')
    # table
    trs = []
    for r in rows:
        unc = sorted({x["name"] for x in r["parts"] if not x["confirmed"] and x["up"] > 0.005})
        stx = ("Re-check pending" if r["status"] == "pending" else (f"{' and '.join(unc)} plan unconfirmed" if unc else
               ("Confirmed" if r["status"] == "verified" else r["status"].split(": ", 1)[1].capitalize())))
        trs.append(f'<tr class="border-t border-slate-100"> <td class="px-4 py-3 font-medium"><a href="/stack/{r["slug"]}/" class="text-slate-900 hover:text-indigo-700">{esc(r["label"])}</a></td> '
                   f'{TD}{"Native" if r["native"] else "Middleware"}</td> {TD}{money(r["up"])}</td> {TD}{money(r["mw"])}</td> {TD}<strong>{money(r["tax"])}</strong></td> {TD}{money(r["tax"] * 12)}</td> '
                   f'{TD}<span class="text-xs text-slate-500">{esc(stx)}</span></td> </tr>')
    table = (f'{H2}All {S["n"]} integrations</h2> <p class="mt-3 text-sm text-slate-500">Sorted by integration tax. Every row links to the calculator, where you can change team size and billing.</p>'
             f'<div class="mt-4 overflow-x-auto rounded-xl border border-slate-200 bg-white shadow-sm"> <table class="spec-matrix w-full min-w-[640px] text-sm" style="font-variant-numeric:tabular-nums"> <thead class="bg-slate-50"> <tr class="text-left"> '
             f'{TH}Integration</th> {TH}Type</th> {TH}Forced upgrade</th> {TH}Connector fee</th> {TH}Integration tax / mo</th> {TH}Per year</th> {TH}Requirements</th> </tr> </thead> <tbody> {"".join(trs)} </tbody> </table> </div>')
    # methodology
    floors = "; ".join(f"{name(s, D)} {floor_plan(D, s)[0]} ({m0(floor_plan(D, s)[1])}/mo)" for s in sorted(D["tools"], key=lambda s: name(s, D).lower()))
    unc = S["unconf_rows"]
    meth = (f'{H2}Methodology</h2> '
            f'{P}<strong>Integration tax</strong> = (each tool&#39;s minimum plan for the integration − that tool&#39;s cheapest plan with API access) + the connector fee, for a 10-seat team at monthly-billing list prices (ActiveCampaign, Pipedrive and Salesforce publish annual-billing rates only, so those rates are used). '
            f'The report covers the {S["n"]} integrations in the index when it was published on Nov 3, 2026; pairs added since then aren&#39;t included, so the figures stay comparable. Minimum plans, connector fees and prices come from those pair calculators; every figure there links to the vendor&#39;s pricing page, help center or developer docs, with the date it was checked (Nov 3 to Nov 8, 2026).</p>'
            f'{P}<strong>Baseline plans</strong> (cheapest plan with API access, 10 seats): {esc(floors)}.</p>'
            f'{P}<strong>Limitations.</strong> HubSpot Professional is modeled as Smart CRM Professional ($50 per seat a month, $45 on annual billing), the cheapest subscription that unlocks the Salesforce connector and the Asana workflow action; other Professional Hubs cost more. Make Core&#39;s $10.59 monthly price comes from third-party pricing reviews, because make.com blocks automated checks. '
            f'Salesforce&#39;s baseline includes the $25/user API add-on that Professional needs. Stripe has no plan fee, so its baseline is $0. '
            f'{len(unc)} integrations include an upgrade that rests on a plan requirement we haven&#39;t confirmed yet ({esc(", ".join(r["label"] for r in unc))}), worth {m0(sum(r["unconfirmed_up"] for r in unc))} a month in total; '
            f'counting only confirmed requirements, {S["conf_forced"]} of {S["n"]} integrations force an upgrade instead of {S["forced"]}. Usage-based charges (Zapier tasks, Make credits, API overages) aren&#39;t included.</p>'
            f'{P}<strong>Why the headline is split.</strong> Integrations that force a plan upgrade and those that only need a connector differ by an order of magnitude, so a single median across both swings between the two groups whenever one row changes. The figures are therefore reported per group: the range covers the middle half of the integrations in each group.</p>')
    cite = (f'<div class="mt-10 rounded-xl border border-indigo-200 bg-indigo-50 p-6"> <h2 class="text-lg font-bold">Use this research</h2> '
            f'<p class="mt-2 text-sm leading-relaxed text-slate-700">The data is open under <a href="https://creativecommons.org/licenses/by/4.0/" rel="noopener" {LINK}>CC BY 4.0</a>: reuse it, including commercially, with a credit and a link. '
            f'Download the full dataset: <a href="/data/integration-pairs.json" {LINK}>integration-pairs.json</a>.</p> '
            f'<p class="mt-3 text-sm text-slate-700"><strong>Suggested citation:</strong> StackCostMatrix, &ldquo;The Integration Tax 2026: Hidden Costs of SaaS Integrations,&rdquo; November 3, 2026, {URL}</p> </div>')
    # FAQ
    faqs = [
        ("What is the integration tax?", f"It's the extra monthly cost of connecting two SaaS tools: any plan upgrade an integration forces above each tool's cheapest plan with API access, plus any connector fee for a service such as Make or Zapier. Across {S['n']} popular integrations, {S['taxed']} have one."),
        ("How much does a SaaS integration cost per month?", f"It depends on whether the integration forces a plan upgrade. For a 10-person team, the {S['forced']} integrations here that force one usually add ${round(S['forced_q1']):,} to ${round(S['forced_q3']):,} a month (median {money(S['forced_median'])}), while the {S['conn_n']} that only need a connector add {money(S['conn_min'])} to {money(S['conn_max'])}. {S['free']} of {S['n']} integrations cost nothing extra, and the most expensive, {maxl}, cost {money(S['max_tax'])} a month."),
        ("Is it cheaper to use Zapier or Make than a native integration?", f"It can be. Connector fees in this index are {', '.join(m0(x) for x in S['mw_fees'])} a month, while forced plan upgrades make up {S['up_share']:.0f}% of the total integration tax, so when a native connector needs a higher plan and the middleware route works on a cheaper one, middleware usually wins. Each pair's calculator compares the native and middleware totals at your team size."),
    ]
    faq_html = (' <section class="mt-12" aria-label="Frequently asked questions"> <h2 class="text-xl font-bold">Frequently asked questions</h2> <div class="mt-4 space-y-6"> ' +
                "".join(f'<div> <h3 class="font-semibold text-slate-900">{esc(q)}</h3> <p class="mt-1 leading-relaxed text-slate-700">{esc(a)}</p> </div>' for q, a in faqs) + ' </div> </section>')
    tipjs = ('<div id="tax-tip" role="tooltip" style="position:fixed;z-index:50;display:none;max-width:320px;padding:8px 10px;border-radius:8px;background:#0b0b0b;color:#fff;font-size:12px;line-height:1.4;pointer-events:none"></div>'
             '<script>(function(){var t=document.getElementById("tax-tip");function show(e,el){t.textContent=el.getAttribute("data-tip");t.style.display="block";var r=el.getBoundingClientRect();'
             'var x=e&&e.clientX?e.clientX+12:r.left;var y=e&&e.clientY?e.clientY+14:r.bottom+6;x=Math.min(x,window.innerWidth-t.offsetWidth-8);t.style.left=x+"px";t.style.top=y+"px";}'
             'function hide(){t.style.display="none";}document.querySelectorAll("[data-tip]").forEach(function(el){el.addEventListener("mousemove",function(e){show(e,el)});'
             'el.addEventListener("mouseleave",hide);el.addEventListener("focus",function(){show(null,el)});el.addEventListener("blur",hide);});})();</script>')
    body = (f'<section class="mx-auto max-w-4xl"> <p class="text-sm font-semibold uppercase tracking-widest text-indigo-600">Research · November 2026</p> '
            f'<h1 class="mt-2 text-3xl font-bold tracking-tight sm:text-4xl">\nThe Integration Tax 2026: What Connecting SaaS Tools Really Costs\n</h1> '
            f'<p class="mt-3 text-sm text-slate-500">StackCostMatrix · Published Nov 3, 2026 · Data checked against vendor docs Nov 3, 2026 · Updated Nov 10, 2026: HubSpot Professional repriced per seat (Nov 5); ActiveCampaign + Stripe, Mailchimp + Calendly and Pipedrive + Xero corrected (Nov 8); &ldquo;Three kinds of integration cost&rdquo; added (Nov 10). See the About page changelog · Edited by <a href="/about/#editor" class="font-medium text-indigo-600 hover:underline">Rakesh Kumar</a></p> '
            f'{P}{lead}</p> {tiles} {figure} {findings} {kinds} {chart1} {chart2} {table} {meth} {cite}{faq_html} </section> {tipjs} ')
    ld = [
        {"@context": "https://schema.org", "@type": "Article", "headline": "The Integration Tax 2026: What Connecting SaaS Tools Really Costs", "description": desc,
         "author": {"@type": "Organization", "name": "StackCostMatrix", "url": f"{SITE}/"}, "publisher": {"@type": "Organization", "name": "StackCostMatrix", "url": f"{SITE}/", "logo": f"{SITE}/icon-512.png"},
         "datePublished": "2026-11-03", "dateModified": "2026-11-10", "mainEntityOfPage": URL, "image": f"{SITE}/og/integration-tax-2026.jpg", "inLanguage": "en", "isBasedOn": {"@id": f"{SITE}/#dataset"}},
        {"@context": "https://schema.org", "@type": "Dataset", "@id": f"{URL}#dataset", "isBasedOn": {"@id": f"{SITE}/#dataset"}, "isAccessibleForFree": True, "name": "StackCostMatrix Integration Tax 2026", "description": f"Monthly integration tax (forced plan upgrades plus connector fees) for {S['n']} B2B SaaS integrations at 10 seats, derived from vendor-verified plan requirements and prices checked 2026-11-03.",
         "url": URL, "license": "https://creativecommons.org/licenses/by/4.0/", "creator": {"@type": "Organization", "name": "StackCostMatrix", "url": f"{SITE}/"},
         "dateModified": "2026-11-10", "keywords": ["SaaS pricing", "integration cost", "API access", "webhooks", "Zapier", "Make"],
         "distribution": [{"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": f"{SITE}/data/integration-pairs.json"}]},
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]},
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
                                                                                         {"@type": "ListItem", "position": 2, "name": "The Integration Tax 2026", "item": URL}]},
    ]
    from site16 import fix_ld
    page = dict(title=title, desc=desc, url=URL, body=body, ld=fix_ld(ld))
    os.makedirs(SLUG, exist_ok=True)
    open(f"{SLUG}/index.html", "w", encoding="utf-8").write(render(read("hubspot-integrations-cost/index.html"), page))
    json.dump({k: (v if not isinstance(v, list) or k == "mw_fees" else len(v)) for k, v in S.items() if k != "by_tool"}, sys.stdout, default=str); print()

def update_home_card():
    """Homepage: the research card and the first FAQ answer quote the report's current figures."""
    D, rows = dataset(); S = stats(rows)
    rng = f"${round(S['forced_q1']):,}–${round(S['forced_q3']):,}"
    new = (f"Original research: {S['taxed']} of {S['n']} popular integrations add a hidden monthly cost, usually {rng} a month when a plan upgrade is forced. "
           f"It covers the {S['n']} pairs in the index when it was published; pairs added since aren&#39;t counted.")
    h = read("index.html")
    h, n = re.subn(r"Original research: \d+ of \d+ popular integrations add a hidden monthly cost[^<]*", new, h)
    assert n == 1
    faq = (f"\nHidden API tier costs are the extra subscription fees you pay because an integration only works on a higher plan of one of the tools. "
           f"In our 2026 research, {S['taxed']} of {S['n']} popular integrations add a hidden monthly cost, and forced plan upgrades make up {S['up_share']:.0f}% of it: "
           f"typically {rng} a month for a 10-person team when an upgrade is forced, against ${S['conn_min']:.2f}–${S['conn_max']:.2f} for a connector such as Make or Zapier. "
           f"The full figures are in The Integration Tax 2026 report on this site.\n")
    h, n = re.subn(r'(<summary class="cursor-pointer font-semibold text-slate-900">What are hidden API tier costs\?</summary> <p class="mt-2 text-sm leading-relaxed text-slate-600">).*?(</p>)',
                   lambda m: m.group(1) + faq + m.group(2), h, count=1, flags=re.S)
    assert n == 1
    open("index.html", "w", encoding="utf-8").write(h)

if __name__ == "__main__":
    build()
    update_home_card()
