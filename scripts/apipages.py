"""Generate /<tool>-api-access/ pages from apidata.py. Run from repo root."""
import json, os, sys, html
sys.path.insert(0, os.path.dirname(__file__))
from apidata import TOOLS, CHECKED
from site16 import fix_ld
from hubs import load_pairs, plan_price, render, read, esc, attr, SHORT, SITE, P, H2, TH, TD, LINK, join_names

QUOTE_OK = set()  # filled from the source check: (slug, index) whose quote was found on the page

def val_html(v, note):
    n = f' <span class="block text-xs text-slate-500">{esc(note)}</span>' if note else ""
    return f"{esc(v) if v else '—'}{n}"

def build(slug, tool, pairs, hubs, api_urls):
    T = TOOLS[slug]; short = SHORT.get(slug, tool["name"]); name = tool["name"]
    url = f"{SITE}/{slug}-api-access/"
    plans = [(pl, T["plans"][pl], tool["plans"].get(pl)) for pl in T["plans"]]
    need = {}
    for p in pairs:
        for t in p["d"]["tools"]:
            if t["slug"] == slug: need.setdefault(t["required"], []).append(p)
    title = T.get("title", f"{short} API & Webhook Access by Plan (2026)")
    h1 = T.get("h1", title)
    first = plans[0][0]
    desc = next(d for d in [f"Which {short} plans include API access and webhooks in 2026, with rate limits and the vendor source for each plan, checked {T.get('checked', CHECKED)}.",
                             f"Which {short} plans include API access and webhooks in 2026, with the vendor source for each plan."] if len(d) <= 155)
    rows = []
    for pl, f, pd in plans:
        price = plan_price(pd) if pd else "—"
        rows.append(f'<tr class="border-t border-slate-100"> <td class="px-4 py-3 font-medium">{esc(pl)}</td> {TD}{esc(price)}</td> {TD}{val_html(f["api"], f["api_note"])}</td> '
                    f'{TD}{esc(f["lim"]) if f["lim"] else ("<span class=\"text-xs text-slate-500\">N/A (no API access)</span>" if f["api"] == "No" else "<span class=\"text-xs text-slate-500\">Not published per plan</span>")}</td> {TD}{val_html(f["wh"], f["wh_note"])}</td> {TD}{esc(f["auto"]) if f["auto"] else "—"}</td> </tr>')
    table = (f'<div class="mt-8 overflow-x-auto rounded-xl border border-slate-200 bg-white shadow-sm"> <table class="spec-matrix w-full min-w-[640px] text-sm"> <thead class="bg-slate-50"> <tr class="text-left"> '
             f'{TH}Plan</th> {TH}Price</th> {TH}API access</th> {TH}API limit</th> {TH}Webhooks</th> {TH}Webhook automation action</th> </tr> </thead> <tbody> {"".join(rows)} </tbody> </table> </div>'
             f'<p class="mt-3 text-xs text-slate-500">' + (f'"Not stated" means {esc(short)}&#39;s documentation that we read doesn&#39;t say either way. ' if any("Not stated" in (f["api"], f["wh"], f["auto"]) for _, f, _ in plans) else "") + 'Prices are monthly-billing list prices from this site&#39;s calculators.</p>')
    kinds = (f'{H2}Two kinds of webhooks</h2> {P}Vendors use "webhooks" for two different features. <strong>Developer webhooks</strong> let an app or a tool like Make or Zapier subscribe to events, '
             f'and are usually available wherever the API is. A <strong>webhook automation action</strong> is a no-code step that sends data out from the tool&#39;s own automations, and is often limited to paid plans. '
             f'The table lists them separately so you can see which one an integration actually needs.</p>')
    note = f"{P}{esc(T['note'])}</p>" if T["note"] else ""
    # integrations by plan
    items = []
    for pl, f, pd in plans:
        ps = need.get(pl, [])
        if not ps: continue
        links = ", ".join(f'<a href="/stack/{p["slug"]}/" {LINK}>{esc(" + ".join(SHORT.get(t["slug"], t["name"]) for t in p["d"]["tools"]))}</a>' for p in ps)
        items.append(f"<strong>{esc(pl)}</strong> ({len(ps)}): {links}")
    hub = hubs.get(slug)
    integ = (f'{H2}Which {esc(short)} plan the integrations here need</h2> {P}' + "<br>".join(items) + "</p>" +
             (f' <p class="mt-3 text-sm text-slate-500">Full costs, including the other tool&#39;s plan and any connector fee: <a href="{hub["url"]}" {LINK}>{esc(short)} integration costs →</a></p>' if hub else "")) if items else ""
    src = []
    for i, (l, u, q) in enumerate(T["sources"]):
        qt = f' <span class="block text-xs text-slate-500">&ldquo;{esc(q)}&rdquo;</span>' if (slug, i) in QUOTE_OK else ""
        src.append(f'<li><a href="{attr(u)}" rel="noopener" {LINK}>{esc(l)} ↗</a>{qt}</li>')
    sources = f'{H2}Sources</h2> <p class="mt-3 text-sm text-slate-500">Checked {T.get('checked', CHECKED)}.</p> <ul class="mt-3 space-y-3 text-sm"> {" ".join(src)} </ul>'
    nav = " · ".join(f'<a href="{u}" {LINK}>{esc(n)}</a>' for s2, (n, u) in sorted(api_urls.items(), key=lambda kv: kv[1][0].lower()) if s2 != slug)
    navh = f'{H2}API access by plan for other tools</h2> <p class="mt-3 leading-relaxed text-slate-600">{nav}</p>'
    # FAQ
    fig = (f'<figure class="mt-6"> <img src="/og/{slug}-api-access.jpg" width="1200" height="630" loading="lazy" class="scm-fig" '
           f'alt="{attr(short)} API access by plan: ' + "; ".join(f"{pl} {f['api'].lower()}" for pl, f, _ in plans[:4]) + '"> '
           f'<figcaption class="mt-2 text-xs text-slate-500">{esc(short)} API access by plan at a glance. Free to reuse with credit (CC BY 4.0).</figcaption> </figure>') if os.path.exists(f"og/{slug}-api-access.jpg") else ""
    extra = ""
    for h, items in T.get("sections", []):
        extra += f"{H2}{esc(h)}</h2> "
        for it in items:
            if isinstance(it, list): extra += '<ol class="scm-steps"> ' + " ".join(f"<li>{esc(x)}</li>" for x in it) + " </ol> "
            else: extra += f"{P}{esc(it)}</p> "
    f0 = T["plans"][first]
    apiv = {"Yes": "Yes.", "No": "No.", "Add-on": "Only as a paid add-on.", "Not stated": f"{short}'s documentation doesn't say."}[f0["api"]]
    q1 = f"Does {short} {first} include API access?"
    a1 = f"{apiv} " + (f"{f0['api_note']}. " if f0["api_note"] else "") + (f"The limit is {f0['lim']}. " if f0["lim"] else "") + T["answer"]
    a1 = T.get("answer_first", a1)
    whp = [pl for pl, f, _ in plans if f["wh"] == "Yes"]
    q2 = f"Which {short} plans include webhooks?"
    a2 = (f"Webhooks are available on {join_names(whp)}" + ("." if len(whp) == len(plans) else f", but not on {join_names([pl for pl, f, _ in plans if f['wh'] == 'No'])}." if any(f["wh"] == "No" for _, f, _ in plans) else ".")
          if whp else (f"None of the {short} plans listed here include them." if any(f["wh"] == "No" for _, f, _ in plans) else f"{short}'s documentation we read doesn't state developer-webhook availability by plan."))
    autos = [f"{pl}: {f['auto']}" for pl, f, _ in plans if f["auto"]]
    if autos: a2 += " Webhook automation action by plan — " + "; ".join(autos) + "."
    a2 = T.get("wh_answer", a2)
    lims = [f"{pl}: {f['lim']}" for pl, f, _ in plans if f["lim"]]
    if lims:
        q3, a3 = f"What are {short}'s API rate limits by plan?", "; ".join(lims) + "." + (f" {T['note']}" if T["note"] else "")
    else:
        q3 = f"Which {short} plan do integrations need?"
        a3 = ("In this index: " + "; ".join(f"{pl} for {len(need[pl])} integration{'s' if len(need[pl]) != 1 else ''}" for pl, _, _ in plans if pl in need) + "." if need
              else f"None of the integrations in this index requires a specific {short} plan.")
    faqs = [(q1, a1), (q2, a2), (q3, a3)] + list(T.get("faq_extra", []))
    faq_html = (f' <section class="mt-12" aria-label="Frequently asked questions"> <h2 class="text-xl font-bold">{esc(short)} API access: frequently asked questions</h2> <div class="mt-4 space-y-6"> ' +
                "".join(f'<div> <h3 class="font-semibold text-slate-900">{esc(q)}</h3> <p class="mt-1 leading-relaxed text-slate-700">{esc(a)}</p> </div>' for q, a in faqs) + ' </div> </section>')
    body = (f'<section class="mx-auto max-w-4xl"> <p class="text-sm font-semibold uppercase tracking-widest text-indigo-600">API &amp; webhooks</p> '
            f'<h1 class="mt-2 text-3xl font-bold tracking-tight sm:text-4xl">\n{esc(h1)}\n</h1> '
            f'<p class="mt-3 text-sm text-slate-500">Checked against {esc(short)}&#39;s developer and help-center documentation · {T.get('checked', CHECKED)} · Edited by <a href="/about/#editor" class="font-medium text-indigo-600 hover:underline">Rakesh Kumar</a></p> '
            f'{P}<strong>Short answer:</strong> {esc(T["answer"])}</p> {table} {note} {fig} {extra} {kinds} {integ} {sources} {navh}{faq_html} </section> ')
    ld = [
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]},
        {"@context": "https://schema.org", "@type": "TechArticle", "headline": title, "description": desc,
         "author": {"@type": "Organization", "name": "StackCostMatrix", "url": f"{SITE}/", "email": "admin@stackcostmatrix.com"}, "datePublished": "2026-11-03", "dateModified": T.get("modified", "2026-11-03"),
         "citation": [u for _, u, _ in T["sources"]], "mainEntityOfPage": url,
         "publisher": {"@type": "Organization", "name": "StackCostMatrix", "url": f"{SITE}/", "logo": f"{SITE}/icon-512.png"}, "image": f"{SITE}/icon-512.png", "inLanguage": "en"},
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
            {"@type": "ListItem", "position": 2, "name": f"{short} API access by plan", "item": url}]},
    ]
    return dict(title=title, desc=desc, url=url, body=body, ld=fix_ld(ld))

def main():
    global QUOTE_OK
    qf = os.path.join(os.path.dirname(__file__), "quote_ok.json")
    if os.path.exists(qf): QUOTE_OK = {tuple(x) for x in json.load(open(qf))}
    D = json.load(open("data/integration-pairs.json", encoding="utf-8")); pairs = load_pairs()
    hubs = json.load(open(os.path.join(os.path.dirname(__file__), "hubs.json")))
    api_urls = {sl: (SHORT.get(sl, D["tools"][sl]["name"]), f"/{sl}-api-access/") for sl in TOOLS}
    tpl = read("hubspot-integrations-cost/index.html")
    for sl in TOOLS:
        page = build(sl, D["tools"][sl], pairs, hubs, api_urls)
        os.makedirs(f"{sl}-api-access", exist_ok=True)
        open(f"{sl}-api-access/index.html", "w", encoding="utf-8").write(render(tpl, page))
        print(sl, len(page["title"]), len(page["desc"]))
    json.dump({sl: dict(name=n, url=u) for sl, (n, u) in api_urls.items()}, open(os.path.join(os.path.dirname(__file__), "apipages.json"), "w"), indent=1)

if __name__ == "__main__":
    main()
