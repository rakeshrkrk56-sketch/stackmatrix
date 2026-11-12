"""2026-11-12, one-time and idempotent: wire the batch 1 pairs (pairdata22) into the rest of the site.
Open data, homepage cards and counts, the footer count on every page, the CRM guide and the HubSpot and Salesforce
hubs, the About and homepage changelogs, and the READMEs. Run after newpairs22.py and before build_all.sh; the build
then re-renders everything (chart, hubs, sitemap, llms.txt, share images)."""
import glob, html, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from model import compute
from pairfix import excerpt, read
from pairdata22 import NEW22, DATE22

def wr(f, s): open(f, "w", encoding="utf-8").write(s)
def one(s, a, b, f=""):
    if b in s and a not in s: return s
    assert s.count(a) == 1, (f, a[:80], s.count(a)); return s.replace(a, b)

D = json.load(open("data/integration-pairs.json", encoding="utf-8"))
NAME = {sl: t["name"] for sl, t in D["tools"].items()}
NEW = list(NEW22)
OLD_N = len([p for p in D["pairs"] if p["pair"] not in NEW22])
NEW_N = OLD_N + len(NEW)
assert OLD_N == 59 and NEW_N == 76, (OLD_N, NEW_N)

# 1. open data, in the format wire13.py used
for pair in NEW:
    s = read(f"stack/{pair}/index.html"); d = json.loads(re.search(r'id="calc-data">(.*?)</script>', s, re.S).group(1)); v = compute(d)
    m = re.search(r'Sources \(checked [^)]*\): (.*?)</p>', s, re.S)
    e = {"pair": pair, "url": f"https://stackcostmatrix.com/stack/{pair}/", "tools": [t["name"] for t in d["tools"]],
         "connection_type": "native" if v["native"] else "middleware", "minimum_plans": {t["name"]: t["required"] for t in d["tools"]},
         "middleware_monthly_usd": d["middleware"]}
    if d.get("middlewareAnnual") is not None: e["middleware_annual_billing_usd_per_month"] = d["middlewareAnnual"]
    e.update({"sync_direction": html.unescape(re.search(r'Data sync direction</td> <td class="px-4 py-3" colspan="2">(.*?)</td>', s, re.S).group(1).strip()),
              "ten_seat_monthly_cost_usd": round(v["N"], 2),
              "verification": html.unescape(re.search(r"<span>((?:Integration requirements|Prices checked)[^<]*)</span>", s).group(1)),
              "last_reviewed": DATE22, "date_modified": DATE22,
              "sources": [{"title": html.unescape(t), "url": html.unescape(u)} for u, t in re.findall(r'<a href="([^"]+)"[^>]*>(.*?) ↗</a>', m.group(1))]})
    D["pairs"] = [p for p in D["pairs"] if p["pair"] != pair] + [e]
D["pairs"].sort(key=lambda p: p["pair"])
wr("data/integration-pairs.json", json.dumps(D, indent=1, ensure_ascii=False))
assert len(D["pairs"]) == NEW_N, len(D["pairs"])

# 2. homepage cards, after the last card whose pair starts with the same tool
h = read("index.html")
for pair, c in NEW22.items():
    if f'href="/stack/{pair}/" data-search=' in h: continue
    A, B = NAME[c["A"]], NAME[c["B"]]; kind = "native" if c["native"] else "middleware"
    badge = ('<span class="shrink-0 rounded-full px-2.5 py-0.5 text-xs font-medium ring-1 bg-emerald-100 text-emerald-800 ring-emerald-200"> Native </span>' if c["native"]
             else '<span class="shrink-0 rounded-full px-2.5 py-0.5 text-xs font-medium ring-1 bg-sky-100 text-sky-800 ring-sky-200"> Middleware </span>')
    card = (f'<a href="/stack/{pair}/" data-search="{html.escape((A + " " + B).lower())} {pair} {c["cats"].replace("|", " ").lower()} {kind}" data-cats="{c["cats"]}" '
            'class="group flex flex-col rounded-xl border border-slate-200 bg-white p-5 shadow-sm transition hover:-translate-y-0.5 hover:shadow-md"> '
            f'<div class="flex items-center justify-between gap-2"> <h3 class="font-semibold text-slate-900 group-hover:text-indigo-700"> {html.escape(A)} + {html.escape(B)} </h3> {badge} </div> '
            f'<p class="mt-2 flex-1 text-sm leading-relaxed text-slate-600"> {html.escape(excerpt(c["summary"], 90), quote=False).replace(chr(39), "&#39;")} </p> '
            '<p class="mt-3 text-sm font-medium text-indigo-600">\nSee true cost &amp; setup guide →\n</p> </a>')
    starts = list(re.finditer(r'<a href="/stack/(' + c["A"] + r'-and-[^/]+)/" data-search=', h))
    anchor = starts[-1] if starts else list(re.finditer(r'<a href="/stack/[^/]+/" data-search=', h))[-1]
    end = h.index("</a>", anchor.start()) + 4
    h = h[:end] + card + h[end:]
h = h.replace(f"for {OLD_N} pairs checked against vendor docs", f"for {NEW_N} pairs checked against vendor docs")
h = h.replace(f"Showing {OLD_N} of {OLD_N} integrations", f"Showing {NEW_N} of {NEW_N} integrations")
HOME_LOG = (f'<li><strong class="text-slate-800">Nov 12, 2026</strong> — {len(NEW)} new integrations, each checked on the vendors&#39; own pages: '
            'Calendly with Salesforce, Stripe and Intercom; HubSpot with Xero, Airtable and Notion; Intercom with Salesforce and Mailchimp; and nine more. '
            f'The index now covers {NEW_N} pairs. No prices changed.</li> ')
if "Nov 12, 2026</strong>" not in h:
    a = '<ul class="mt-5 space-y-3 text-sm leading-relaxed text-slate-600"> <li><strong class="text-slate-800">Nov 11, 2026</strong>'
    h = one(h, a, '<ul class="mt-5 space-y-3 text-sm leading-relaxed text-slate-600"> ' + HOME_LOG + '<li><strong class="text-slate-800">Nov 11, 2026</strong>', "home log")
wr("index.html", h)

# 3. footer count and other count mentions on every page
for f in glob.glob("*.html") + glob.glob("*/index.html") + glob.glob("stack/*/index.html"):
    s = read(f); s0 = s
    s = s.replace(f">All {OLD_N} integration pairs</a>", f">All {NEW_N} integration pairs</a>")
    s = s.replace(f"Browse all {OLD_N} B2B integration cost calculators", f"Browse all {NEW_N} B2B integration cost calculators")
    if s != s0: wr(f, s)

# 4. About: the current-count sentence and a dated changelog entry
a = read("about/index.html")
a = a.replace(f"53 pricing plans, {OLD_N} integration pairs", f"53 pricing plans, {NEW_N} integration pairs")
LOG = (f'<li><strong class="text-slate-800">Nov 12, 2026 — {len(NEW)} new integration pairs.</strong> '
       'Calendly + Salesforce, Calendly + Stripe, Calendly + Intercom, HubSpot + Xero, HubSpot + Airtable, HubSpot + Notion, Intercom + Salesforce, '
       'Intercom + Mailchimp, Asana + Salesforce, Zendesk + Asana, Salesforce + Airtable, Pipedrive + Intercom, Pipedrive + Zendesk, Pipedrive + Asana, '
       'Mailchimp + Slack, Salesforce + Xero (through Make) and Xero + Slack (through Make). Each one&#39;s plan requirements, how it works, limits and setup steps '
       'were read on the vendors&#39; own help pages and app listings that day. Where a vendor names no plan, the page says so and uses each tool&#39;s cheapest '
       'plan with API access. Three more candidates were left out because a fact they needed couldn&#39;t be read. '
       f'The index now covers {NEW_N} pairs; the Integration Tax report still covers the 55 pairs it was published with. No prices changed.</li> ')
if "Nov 12, 2026 — " not in a:
    a = one(a, '<ul class="mt-4 space-y-3 text-sm leading-relaxed text-slate-600"> <li><strong class="text-slate-800">Nov 11, 2026',
            '<ul class="mt-4 space-y-3 text-sm leading-relaxed text-slate-600"> ' + LOG + '<li><strong class="text-slate-800">Nov 11, 2026', "about log")
wr("about/index.html", a)

# 5. guide tables: the CRM guide lists every pair with a CRM, the two hand-written hubs every pair with their tool
NATIVE = '<span class="rounded-full px-2 py-0.5 text-xs font-medium ring-1 bg-emerald-100 text-emerald-800 ring-emerald-200"> Native </span>'
MIDDLE = '<span class="rounded-full px-2 py-0.5 text-xs font-medium ring-1 bg-sky-100 text-sky-800 ring-sky-200"> Middleware </span>'
def row(pair, cells):
    c = NEW22[pair]; lab = f"{NAME[c['A']]} + {NAME[c['B']]}"
    mid = "".join(f'<td class="px-4 py-3">{x}</td> ' for x in cells)
    return (f'<tr class="border-t border-slate-100"> <td class="px-4 py-3 font-medium">{html.escape(lab)}</td> <td class="px-4 py-3"> {NATIVE if c["native"] else MIDDLE} </td> {mid}'
            f'<td class="px-4 py-3"> <a href="/stack/{pair}/" class="font-medium text-indigo-600 hover:underline">True-cost calculator →</a> </td> </tr>')
def add_rows(f, rows):
    s = read(f)
    for pair, cells in rows:
        if f'href="/stack/{pair}/"' in s: continue
        i = s.index("</tbody>"); s = s[:i] + row(pair, cells) + " " + s[i:]
    wr(f, s)
crm = [p for p, c in NEW22.items() if {c["A"], c["B"]} & {"hubspot", "salesforce", "pipedrive"}]
add_rows("crm-integration-pricing-guide/index.html", [(p, []) for p in crm])
hs = [p for p, c in NEW22.items() if "hubspot" in (c["A"], c["B"])]
add_rows("hubspot-integrations-cost/index.html", [(p, [NEW22[p]["req"]["hubspot"]]) for p in hs])
s = read("hubspot-integrations-cost/index.html"); n_hs = len(re.findall(r'<tr class="border-t border-slate-100">(?:(?!</tr>).)*?href="/stack/', s, re.S))
n_old = n_hs - len(hs)
s = s.replace(f"native vs middleware totals across {n_old} popular connections", f"native vs middleware totals across {n_hs} popular connections")
s = s.replace(f"of {n_old} popular HubSpot\n      integrations", f"of {n_hs} popular HubSpot\n      integrations")
wr("hubspot-integrations-cost/index.html", s)
SF_COL = {"Professional": "Yes — +$25/user/mo on Professional", "Enterprise": "No — needs Enterprise (API included)"}
sf = [p for p, c in NEW22.items() if "salesforce" in (c["A"], c["B"])]
add_rows("salesforce-integrations-cost/index.html", [(p, [SF_COL[NEW22[p]["req"]["salesforce"]]]) for p in sf])

# 6. READMEs
r = read("README.md")
r = r.replace(f"**{OLD_N} B2B software integration pairs**", f"**{NEW_N} B2B software integration pairs**").replace(f"**{OLD_N} integration calculators**", f"**{NEW_N} integration calculators**")
r = r.replace(f"all {OLD_N} integration pairs, exported", f"all {NEW_N} integration pairs, exported").replace(f"### All {OLD_N} integration cost calculators", f"### All {NEW_N} integration cost calculators")
m = re.search(r"### All \d+ integration cost calculators\n(.*?)(\n\n|\Z)", r, re.S)
lines = m.group(1).rstrip("\n").split("\n")
for pair in NEW:
    if f"/stack/{pair}/" in r: continue
    a_, b_ = pair.split("-and-")
    lines.append(f"- [{a_.title()} + {b_.title()}](https://stackcostmatrix.com/stack/{pair}/)")
lines = sorted(set(lines), key=lambda l: re.search(r"/stack/([^/]+)/", l).group(1))
r = r[:m.start(1)] + "\n".join(lines) + r[m.end(1):]
wr("README.md", r)
dr = read("data/README.md").replace(f"all {OLD_N} integration pairs", f"all {NEW_N} integration pairs"); wr("data/README.md", dr)
print("wired", len(NEW), "pairs | open data:", len(D["pairs"]), "| CRM guide +", len(crm), "| HubSpot hub +", len(hs), f"({n_hs} rows) | Salesforce hub +", len(sf))
