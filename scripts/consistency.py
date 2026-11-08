import re, json, glob, html, sys, os
sys.path.insert(0, os.path.dirname(__file__)); from model import compute
from pairfix import trap_text as _trap_text
U = lambda x: re.sub(r"\s+", " ", html.unescape(x)).strip()
def txt(fragment): return U(re.sub(r"<[^>]+>", " ", fragment))
home = open("index.html", encoding="utf-8").read()
guides = {g: open(f"{g}/index.html", encoding="utf-8").read() for g in ("hubspot-integrations-cost", "salesforce-integrations-cost", "crm-integration-pricing-guide")}
allpages = {f.split("/")[1]: open(f, encoding="utf-8").read() for f in sorted(glob.glob("stack/*/index.html"))}
issues = []; info = {}
def add(p, sev, where, msg): issues.append((p, sev, where, msg))
money = lambda x: "${:,.2f}".format(x)
for p, s in allpages.items():
    d = json.loads(re.search(r'id="calc-data">(.*?)</script>', s, re.S).group(1)); v = compute(d)
    A, B = d["tools"]; native = d["middleware"] == 0; typ = "Native" if native else "Middleware"
    req = {t["name"]: t["required"] for t in d["tools"]}
    summ = U(re.search(r'<p class="mt-4 max-w-3xl text-lg leading-relaxed text-slate-700">(.*?)</p>', s, re.S).group(1))
    trap_sum = U(re.search(r'<p class="mt-4 text-sm leading-relaxed text-amber-900">(.*?)</p>', s, re.S).group(1))
    sync = re.search(r'Data sync direction</td> <td class="px-4 py-3" colspan="2">(.*?)</td>', s).group(1).strip()
    badge = re.search(r'Connection type</td> <td class="px-4 py-3" colspan="2"> <span[^>]*>\s*(\w+)', s).group(1)
    nrow = txt(re.search(r'Native integration supported</td> <td class="px-4 py-3" colspan="2">(.*?)</td>', s).group(1))
    blocks = [json.loads(b) for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)]
    faq = next(b for b in blocks if b["@type"] == "FAQPage"); wp = next(b for b in blocks if b["@type"] == "WebPage")
    fa = [q["acceptedAnswer"]["text"] for q in faq["mainEntity"]]
    meta = U(re.search(r'<meta name="description" content="([^"]*)"', s).group(1)); og = U(re.search(r'<meta property="og:description" content="([^"]*)"', s).group(1))
    how = re.search(r'aria-label="How the integration works">(.*?)</section>', s, re.S)
    info[p] = dict(type=typ, req=req, cost=v["N"], sync=sync, how=bool(how), summary=summ, lastReviewed=wp.get("lastReviewed"), dateModified=wp.get("dateModified"))
    # type consistency
    if badge != typ: add(p, "High", "spec matrix", f"badge '{badge}' vs calculator type {typ}")
    if native != nrow.startswith("Yes"): add(p, "High", "spec matrix", f"'Native integration supported' = '{nrow}' vs type {typ}")
    if native != ("connection is native" in fa[2]): add(p, "High", "FAQ Q3", f"FAQ type answer disagrees with {typ}")
    # since 2026-11-08 the trap box states the pair's own extra cost (pairfix.trap_text) instead of repeating the lede
    if trap_sum != U(_trap_text(v, d)): add(p, "Medium", "hidden cost trap", "trap text differs from the computed extra cost")
    if native and re.search(r"Route it through|No native (link|connector)|runs through middleware|iPaaS only", summ): add(p, "High", "summary", f"native page but summary implies middleware: '{summ[:90]}…'")
    if not native and re.search(r"native integration\b(?! exists)|connection is native", summ) and "no native" not in summ.lower() and "not natively" not in summ.lower() and not summ.lower().startswith("neither"): add(p, "Medium", "summary", f"middleware page but summary says native: '{summ[:90]}…'")
    # tiers mentioned in summary vs calculator
    for name, tier in re.findall(r"Requires ([A-Z][\w .+]*?) on the '([^']+)' plan", summ):
        if name in req and req[name] != tier: add(p, "High", "summary", f"summary says {name} '{tier}' but calculator requires '{req[name]}'")
    # sync phrases
    if "full 2-way sync" in summ and sync != "2-way": add(p, "Medium", "summary vs spec", f"summary says 'full 2-way sync' but spec sync = '{sync}'")
    if "1-way" in summ and sync == "2-way": add(p, "Medium", "summary vs spec", "summary says 1-way but spec says 2-way")
    nvm = txt(re.search(r'aria-label="Native versus middleware">(.*?)</section>', s, re.S).group(1))
    if "with 2-way sync" in nvm and sync != "2-way": add(p, "Medium", "native vs middleware", f"says 'with 2-way sync' but spec sync = '{sync}'")
    # FAQ answers mention required tiers & cost
    for name, tier in req.items():
        if f"{name} must be on the '{tier}' plan" not in fa[0]: add(p, "High", "FAQ Q1", f"FAQ tier for {name} doesn't match '{tier}'")
    if money(v["N"]) not in fa[1]: add(p, "High", "FAQ Q2", f"FAQ cost doesn't match {money(v['N'])}")
    # meta / og / webpage
    if meta != og: add(p, "Low", "og:description", "og:description differs from meta description")
    if wp.get("description") != meta: add(p, "Low", "JSON-LD WebPage", "WebPage description differs from meta")
    cost_s = money(v["N"]).replace(".00", "")
    if cost_s not in meta: add(p, "Medium", "meta description", f"meta cost doesn't match {cost_s}: '{meta}'")
    # verified facts box & trap dd
    rt = re.search(r"<li><strong>Required tiers:</strong> '([^']+)' / '([^']+)'", s).groups()
    if rt != (A["required"], B["required"]): add(p, "High", "verified facts", f"Required tiers {rt} vs calculator")
    for t in d["tools"]:
        dd = re.search(r'<dt class="text-sm text-amber-800">' + re.escape(t["name"]) + r' minimum tier</dt> <dd class="text-lg font-bold text-amber-950">\'([^\']+)\'', s)
        if not dd or dd.group(1) != t["required"]: add(p, "High", "hidden cost trap", f"{t['name']} minimum tier box mismatch")
    for row in ("API access at required tier", "Webhook support at required tier"):
        m = re.search(row + r'</td> <td class="px-4 py-3">(.*?)</td> <td class="px-4 py-3">(.*?)</td> </tr>', s, re.S)
        for t, cell in zip(d["tools"], m.groups()):
            tt = re.search(r"\('([^']+)'\)", cell).group(1)
            if tt != t["required"]: add(p, "High", "spec matrix", f"{row} for {t['name']} shows '{tt}' vs required '{t['required']}'")
    avail = re.search(r"<li><strong>Native app availability:</strong>(.*?)</li>", s).group(1)
    if native != ("Native app available" in avail): add(p, "High", "verified facts", f"availability '{avail.strip()}' vs {typ}")
    # homepage card
    i = home.find(f'href="/stack/{p}/"'); card = home[i:home.find("</a>", i)]
    hb = re.search(r'<span class="shrink-0 rounded-full[^>]*>\s*(\w+)', card).group(1)
    if hb != typ: add(p, "High", "homepage card", f"homepage badge '{hb}' vs {typ}")
    ds = re.search(r'data-search="[^"]* (native|middleware)"', card).group(1)
    if ds != typ.lower(): add(p, "Low", "homepage card", f"search keyword '{ds}' vs {typ}")
    ex = U(re.search(r'<p class="mt-2 flex-1 text-sm leading-relaxed text-slate-600">(.*?)</p>', card, re.S).group(1)).rstrip("…")
    if not summ.startswith(ex): add(p, "Medium", "homepage card", "excerpt doesn't match current summary")
    # guide rows
    for g, gs in guides.items():
        j = gs.find(f'href="/stack/{p}/"')
        if j < 0: continue
        row = gs[gs.rfind("<tr", 0, j):gs.find("</tr>", j)]
        gb = re.search(r'<span class="rounded-full[^>]*>\s*(\w+)', row)
        if gb and gb.group(1) != typ: add(p, "High", f"guide {g}", f"guide badge '{gb.group(1)}' vs {typ}")
        if g == "hubspot-integrations-cost" and "HubSpot" in req:
            tiercell = re.search(r'</span> </td> <td class="px-4 py-3">([^<]*)</td>', row)
            if tiercell and tiercell.group(1).strip() != req["HubSpot"]: add(p, "High", f"guide {g}", f"guide HubSpot tier '{tiercell.group(1)}' vs '{req['HubSpot']}'")
# related labels
for p, s in allpages.items():
    for q, lab in re.findall(r'<a href="/stack/([^/"]+)/" class="rounded-xl[^>]*> <h3[^>]*> [^<]+ </h3> <p class="mt-1 text-xs font-medium text-slate-500"> (\w+) </p>', s):
        if lab != info[q]["type"]: add(p, "Medium", "related card", f"card for {q} labelled {lab}, page is {info[q]['type']}")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".out"); os.makedirs(OUT, exist_ok=True)
json.dump(info, open(os.path.join(OUT, "audit-info.json"), "w"), indent=1)
json.dump(issues, open(os.path.join(OUT, "audit-issues-consistency.json"), "w"), indent=1)
from collections import Counter
print("pages checked:", len(allpages), "| issues:", len(issues), Counter((i[1], i[2]) for i in issues))
for i in issues: print(" ", i)
