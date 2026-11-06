"""Build /hubspot-professional-integrations/: which integrations need HubSpot Professional, and the cheapest way to get it.
Run from the repo root: python3 scripts/hspro.py   (then python3 scripts/security.py)
Prices come from HubSpot's pricing pages and product catalog, read on CHECKED with the billing toggles clicked.
Integration requirements come from the pair pages' calculator data, so they stay in step with the rest of the site."""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from hubs import load_pairs, render, read, esc, attr, m0, SITE, P, H2, TH, TD, LINK, SHORT
from pairdata15 import HS_CHECKED

CHECKED, CHECKED_TXT = HS_CHECKED, "Nov 5, 2026"
SLUG = "hubspot-professional-integrations"
URL = f"{SITE}/{SLUG}/"
TITLE = "Which Integrations Need HubSpot Professional? (2026)"
DESC = ("Only 2 of 13 common HubSpot integrations need Professional: Salesforce and Asana. The cheapest Professional plan "
        "is $50/seat, about $500/mo for 10 people.")

# Professional subscriptions, read on each Hub's pricing page (monthly billing / annual commitment).
# seats_incl: Core Seats included in the flat price (None = sold per seat); extra: monthly price of each extra seat.
# sf / asana: listed in HubSpot's knowledge-base article for that integration.
PRO = [
    dict(name="Smart CRM Professional", monthly=50, annual=45, per_seat=True, seats_incl=None, extra=None, onboarding=None, sf=True, asana=True,
         url="https://www.hubspot.com/pricing/smart-crm"),
    dict(name="Content Hub Professional", monthly=500, annual=450, per_seat=False, seats_incl=3, extra=50, onboarding=None, sf=True, asana=False,
         url="https://www.hubspot.com/pricing/content/enterprise"),
    dict(name="Sales Hub Professional", monthly=100, annual=90, per_seat=True, seats_incl=None, extra=None, onboarding=1500, sf=True, asana=True,
         url="https://www.hubspot.com/pricing/sales/enterprise"),
    dict(name="Service Hub Professional", monthly=100, annual=90, per_seat=True, seats_incl=None, extra=None, onboarding=1500, sf=True, asana=True,
         url="https://www.hubspot.com/pricing/service/enterprise"),
    dict(name="Marketing Hub Professional", monthly=890, annual=800, per_seat=False, seats_incl=3, extra=50, onboarding=3000, sf=True, asana=True,
         url="https://www.hubspot.com/pricing/marketing/enterprise"),
    dict(name="Data Hub Professional", monthly=800, annual=720, per_seat=False, seats_incl=1, extra=50, onboarding=None, sf=True, asana=True,
         url="https://www.hubspot.com/pricing/operations/enterprise"),
]
SEATS = 10
def ten(p):
    return p["monthly"] * SEATS if p["per_seat"] else p["monthly"] + max(0, SEATS - p["seats_incl"]) * p["extra"]
PRO.sort(key=ten)

SOURCES = [
    ("HubSpot KB: Connect HubSpot and Salesforce", "https://knowledge.hubspot.com/salesforce/install-the-hubspot-salesforce-integration",
     "Available with any of the following subscriptions, except where noted: Marketing Hub, Sales Hub, Service Hub, Data Hub, Content Hub, Smart CRM: Professional, Enterprise"),
    ("HubSpot KB: Create Asana tasks with workflows", "https://knowledge.hubspot.com/workflows/create-asana-tasks-with-workflows",
     "Available with any of the following subscriptions, except where noted: Marketing Hub, Sales Hub, Service Hub, Data Hub, Smart CRM, Revenue Hub: Professional, Enterprise"),
    ("HubSpot KB: Use webhooks with HubSpot workflows", "https://knowledge.hubspot.com/workflows/how-do-i-use-webhooks-with-hubspot-workflows",
     "Available with any of the following subscriptions, except where noted: Data Hub Professional, Enterprise"),
    ("HubSpot pricing: Smart CRM", "https://www.hubspot.com/pricing/smart-crm", "Professional · Starts at $45/mo/seat (annual commitment) · $50/mo/seat (pay monthly)"),
    ("HubSpot pricing: Sales Hub", "https://www.hubspot.com/pricing/sales/enterprise",
     "Professional · $90/mo/seat (annual commitment) · $100/mo/seat (pay monthly) · one-time Professional Onboarding for a fee of $1,500"),
    ("HubSpot pricing: Marketing Hub", "https://www.hubspot.com/pricing/marketing/enterprise",
     "Professional · $800/mo (annual commitment) · $890/mo (pay monthly) · Includes 3 Core Seats · one-time Professional Onboarding for a fee of $3,000"),
    ("HubSpot pricing: Service Hub", "https://www.hubspot.com/pricing/service/enterprise", "Professional · $90/mo/seat · $100/mo/seat · one-time Professional Onboarding for a fee of $1,500"),
    ("HubSpot pricing: Content Hub", "https://www.hubspot.com/pricing/content/enterprise", "Professional · $450/mo · $500/mo · Includes 3 Core Seats"),
    ("HubSpot pricing: Data Hub", "https://www.hubspot.com/pricing/operations/enterprise", "Professional · $720/mo · $800/mo · Includes 1 Core Seat"),
    ("HubSpot Product and Services Catalog", "https://legal.hubspot.com/hubspot-product-and-services-catalog",
     "Core Seat … Professional subscriptions $50/month per seat · View-Only Seat … Available at no additional cost"),
]

def name_of(p):
    return " + ".join(SHORT.get(t["slug"], t["name"]) for t in p["d"]["tools"])

def build():
    pairs = [p for p in load_pairs() if any(t["slug"] == "hubspot" for t in p["d"]["tools"])]
    def hs_req(p): return next(t["required"] for t in p["d"]["tools"] if t["slug"] == "hubspot")
    pro = sorted([p for p in pairs if hs_req(p) == "Professional"], key=lambda p: -p["v"]["N"])
    free = sorted([p for p in pairs if hs_req(p) == "Free"], key=name_of)
    other = [p for p in pairs if hs_req(p) not in ("Professional", "Free")]
    assert not other, [p["slug"] for p in other]
    n, npro, nfree = len(pairs), len(pro), len(free)
    cheapest = PRO[0]; c10 = ten(cheapest)
    pro_names = " and ".join(name_of(p) for p in pro)

    # 1. integrations table
    rows = []
    for p in pro + free:
        hs = hs_req(p); other_t = next(t for t in p["d"]["tools"] if t["slug"] != "hubspot")
        badge = ('<span class="rounded-full px-2 py-0.5 text-xs font-medium ring-1 bg-amber-50 text-amber-800 ring-amber-200"> Professional </span>' if hs == "Professional"
                 else '<span class="rounded-full px-2 py-0.5 text-xs font-medium ring-1 bg-emerald-100 text-emerald-800 ring-emerald-200"> Free CRM </span>')
        conn = "Native" if p["d"]["middleware"] == 0 else (p["conn"] or "Middleware")
        rows.append(f'<tr class="border-t border-slate-100"> <td class="px-4 py-3 font-medium"><a href="/stack/{p["slug"]}/" {LINK}>{esc(name_of(p))}</a></td> '
                    f'{TD}{badge}</td> {TD}{esc(SHORT.get(other_t["slug"], other_t["name"]))} {esc(other_t["required"])}</td> {TD}{esc(conn)}</td> {TD}{m0(p["v"]["N"])}/mo</td> </tr>')
    t1 = (f'<div class="mt-6 overflow-x-auto rounded-xl border border-slate-200 bg-white shadow-sm"> <table class="spec-matrix w-full min-w-[640px] text-sm"> <thead class="bg-slate-50"> <tr class="text-left"> '
          f'{TH}Integration</th> {TH}HubSpot plan needed</th> {TH}Other tool&#39;s plan</th> {TH}Connection</th> {TH}10-person total</th> </tr> </thead> <tbody> {"".join(rows)} </tbody> </table> </div>'
          f'<p class="mt-3 text-xs text-slate-500">Totals are both tools&#39; required plans plus any connector fee, for 10 seats at monthly billing, from each integration&#39;s calculator. HubSpot Professional is priced as {esc(cheapest["name"])}, the cheapest Professional subscription.</p>')

    # 2. Professional options table
    def price(p, k): return f'{m0(p[k])}/seat' if p["per_seat"] else f'{m0(p[k])}/mo'
    def seats(p): return "Sold per seat" if p["per_seat"] else f'{p["seats_incl"]} included, then from {m0(p["extra"])}/seat'
    yes, no = "Yes", '<span class="text-slate-500">Not listed</span>'
    r2 = []
    for p in PRO:
        r2.append(f'<tr class="border-t border-slate-100"> <td class="px-4 py-3 font-medium"><a href="{attr(p["url"])}" rel="noopener" {LINK}>{esc(p["name"])} ↗</a></td> '
                  f'{TD}{price(p, "monthly")}</td> {TD}{price(p, "annual")}</td> {TD}{esc(seats(p))}</td> {TD}<strong>{m0(ten(p))}/mo</strong></td> '
                  f'{TD}{m0(p["onboarding"]) + " one-time" if p["onboarding"] else "None shown"}</td> {TD}{yes if p["sf"] else no}</td> {TD}{yes if p["asana"] else no}</td> </tr>')
    t2 = (f'<div class="mt-6 overflow-x-auto rounded-xl border border-slate-200 bg-white shadow-sm"> <table class="spec-matrix w-full min-w-[640px] text-sm"> <thead class="bg-slate-50"> <tr class="text-left"> '
          f'{TH}Professional subscription</th> {TH}Pay monthly</th> {TH}Annual commitment</th> {TH}Seats</th> {TH}10 people, monthly</th> {TH}Onboarding fee</th> {TH}Salesforce connector</th> {TH}Asana action</th> </tr> </thead> <tbody> {"".join(r2)} </tbody> </table> </div>'
          f'<p class="mt-3 text-xs text-slate-500">Prices from HubSpot&#39;s pricing pages, checked {CHECKED_TXT}. Annual-commitment prices are per month. Extra Core Seats are listed as &ldquo;start at&rdquo; prices, so these are minimums. '
          f'&ldquo;Not listed&rdquo; means that Hub isn&#39;t in HubSpot&#39;s help article for the integration. Revenue Hub Professional also unlocks the Asana action.</p>')

    sf = next(p for p in pro if p["slug"] == "hubspot-and-salesforce")
    mkt = next(x for x in PRO if x["name"].startswith("Marketing"))
    sec_cheap = (f'{H2}The cheapest way to get HubSpot Professional</h2> '
                 f'{P}Both integrations work with <em>any</em> Professional subscription HubSpot lists for them, so you don&#39;t need Marketing Hub. '
                 f'<strong>{esc(cheapest["name"])}</strong> is the cheapest: {m0(cheapest["monthly"])} per seat a month, or {m0(cheapest["annual"])} with an annual commitment, '
                 f'with no onboarding fee shown. For 10 people that&#39;s {m0(c10)} a month. Marketing Hub Professional, the plan most people think of, costs {m0(ten(mkt))} a month for the same team, plus a {m0(mkt["onboarding"])} onboarding fee.</p>'
                 f'{t2}'
                 f'{P}<strong>You may not need 10 paid seats.</strong> HubSpot charges per Core Seat, and its product catalog says View-Only Seats are &ldquo;available at no additional cost&rdquo;. '
                 f'People who only look at records don&#39;t need a paid seat, so a team where a few people do the editing pays less than the 10-seat figure.</p>')
    sec_alt = (f'{H2}Is there a cheaper route than upgrading?</h2> '
               f'{P}Sometimes. HubSpot&#39;s API works on every plan, including the free CRM, so a connector like Make can link HubSpot to Salesforce or Asana without Professional. '
               + "".join(f'For <a href="/stack/{p["slug"]}/" {LINK}>{esc(name_of(p))}</a>, the native route costs {m0(p["v"]["N"])} a month for 10 people and the connector route about {money2(p["v"]["MP"])}. ' for p in pro)
               + 'The trade-off is that you build and maintain the sync yourself, and the native Salesforce connector does more (two-way sync of contacts, companies, deals and activities) than a simple automation.</p>')
    sec_other = (f'{H2}What else needs Professional</h2> '
                 f'{P}<strong>Webhooks in workflows</strong> need <em>Data Hub</em> Professional or Enterprise specifically; HubSpot&#39;s knowledge base lists no other Hub for them. '
                 f'Developer webhooks, which apps and tools like Make use, are a separate feature. See <a href="/hubspot-api-access/" {LINK}>HubSpot API &amp; webhook access by plan</a>.</p>')

    src = " ".join(f'<li><a href="{attr(u)}" rel="noopener" {LINK}>{esc(l)} ↗</a> <span class="block text-xs text-slate-500">&ldquo;{esc(q)}&rdquo;</span></li>' for l, u, q in SOURCES)
    sources = f'{H2}Sources</h2> <p class="mt-3 text-sm text-slate-500">Checked {CHECKED_TXT}. Help-article quotes are copied from each article, with the plan lists condensed; pricing lines show the figures each page displays.</p> <ul class="mt-3 space-y-3 text-sm"> {src} </ul>'
    more = (f'{H2}More on HubSpot</h2> <p class="mt-3 leading-relaxed text-slate-600"><a href="/hubspot-integrations-cost/" {LINK}>All HubSpot integration costs</a> · '
            f'<a href="/hubspot-api-access/" {LINK}>HubSpot API access by plan</a> · <a href="/integration-tax-2026/" {LINK}>The Integration Tax 2026 report</a></p>')

    free_names = ", ".join(name_of(p).replace("HubSpot + ", "").replace(" + HubSpot", "") for p in free)
    faqs = [
        ("Which HubSpot integrations need Professional?",
         f"Of the {n} HubSpot integrations on this site, {npro} need a Professional subscription: {pro_names}. The other {nfree} ({free_names}) work on HubSpot's free CRM."),
        ("What is the cheapest HubSpot Professional plan?",
         f"{cheapest['name']}, at ${cheapest['monthly']} per seat a month on monthly billing or ${cheapest['annual']} with an annual commitment, with no onboarding fee shown on HubSpot's pricing page. "
         f"HubSpot's help articles list it among the subscriptions that unlock both the Salesforce connector and the Asana workflow action."),
        ("Does the HubSpot Salesforce integration work on the free CRM?",
         "No. HubSpot's knowledge base says the Salesforce integration is available with Marketing Hub, Sales Hub, Service Hub, Data Hub, Content Hub or Smart CRM on Professional or Enterprise. "
         f"For 10 people, HubSpot + Salesforce costs {m0(sf['v']['N'])} a month on the plans it needs."),
        ("Do webhooks in HubSpot workflows need Professional?",
         "They need Data Hub Professional or Enterprise specifically. Developer webhooks for apps are a separate feature and aren't tied to that requirement."),
    ]
    faq_html = (' <section class="mt-12" aria-label="Frequently asked questions"> <h2 class="text-xl font-bold">Frequently asked questions</h2> <div class="mt-4 space-y-6"> ' +
                "".join(f'<div> <h3 class="font-semibold text-slate-900">{esc(q)}</h3> <p class="mt-1 leading-relaxed text-slate-700">{esc(a)}</p> </div>' for q, a in faqs) + ' </div> </section>')
    answer = (f"Only {npro} of the {n} HubSpot integrations we track need Professional: {pro_names}. Any Professional subscription HubSpot lists for them works, "
              f"and the cheapest is {cheapest['name']} at ${cheapest['monthly']} per seat a month (${cheapest['annual']} on an annual commitment), about {m0(c10)} a month for 10 people. "
              f"The other {nfree} work on HubSpot's free CRM.")
    body = (f'<section class="mx-auto max-w-4xl"> <p class="text-sm font-semibold uppercase tracking-widest text-indigo-600">HubSpot plans</p> '
            f'<h1 class="mt-2 text-3xl font-bold tracking-tight sm:text-4xl">\n{esc(TITLE)}\n</h1> '
            f'<p class="mt-3 text-sm text-slate-500">Checked against HubSpot&#39;s pricing pages and knowledge base · {CHECKED_TXT}</p> '
            f'{P}<strong>Short answer:</strong> {esc(answer)}</p> '
            f'{H2}Which HubSpot plan each integration needs</h2> {t1} {sec_cheap} {sec_alt} {sec_other} {sources} {more}{faq_html} </section> ')
    ld = [
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]},
        {"@context": "https://schema.org", "@type": "Article", "headline": TITLE, "description": DESC,
         "author": {"@type": "Organization", "name": "StackCostMatrix", "url": f"{SITE}/", "email": "admin@stackcostmatrix.com"}, "datePublished": CHECKED, "dateModified": CHECKED,
         "citation": [u for _, u, _ in SOURCES], "mainEntityOfPage": URL,
         "publisher": {"@type": "Organization", "name": "StackCostMatrix", "url": f"{SITE}/", "logo": f"{SITE}/icon-512.png"}, "image": f"{SITE}/icon-512.png", "inLanguage": "en"},
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
            {"@type": "ListItem", "position": 2, "name": "HubSpot integrations", "item": f"{SITE}/hubspot-integrations-cost/"},
            {"@type": "ListItem", "position": 3, "name": "Integrations that need HubSpot Professional", "item": URL}]},
    ]
    return dict(title=TITLE, desc=DESC, url=URL, body=body, ld=ld)

def money2(x):
    return f"${x:,.2f}"

if __name__ == "__main__":
    page = build()
    assert len(page["title"]) <= 60 and len(page["desc"]) <= 160, (len(page["title"]), len(page["desc"]))
    os.makedirs(SLUG, exist_ok=True)
    open(f"{SLUG}/index.html", "w", encoding="utf-8").write(render(read("hubspot-integrations-cost/index.html"), page))
    print(f"wrote {SLUG}/index.html | title {len(page['title'])} | desc {len(page['desc'])}")
