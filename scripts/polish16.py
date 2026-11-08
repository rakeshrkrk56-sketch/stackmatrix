"""2026-11-08 accuracy and clarity round (from the claude-seo plugin audit). One-time, idempotent edits to text the
generators don't manage. Run from the repo root: python3 scripts/polish16.py   (then pairfix apply, homefaq, security)."""
import glob, json, re, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from model import compute

def edit(f, pairs, required=True):
    s = open(f, encoding="utf-8").read(); s0 = s
    for a, b, n in pairs:
        if a not in s and (not b or b in s): continue         # already applied
        c = s.count(a)
        if required: assert c == n, (f, a[:70], c, n)
        s = s.replace(a, b)
    if s != s0: open(f, "w", encoding="utf-8").write(s)
    return s != s0

changed = []

# --- every pair page: calculator state messages (hidden until JS shows them) read as conditions, so they never
#     contradict the visible totals when read out of context; dated heading; H1 on pages with no extra cost
CALC = [
 ('<p class="font-bold text-emerald-900">✓ No upgrade needed — $0 incremental cost</p>',
  '<p class="font-bold text-emerald-900">✓ With these settings: no upgrade needed, $0 extra</p>', 1),
 ('On the required tiers shown above, this integration needs no tier upgrade and no middleware fee. (This assumes you already pay for the plans shown — it is not a claim that the integration is free for non-subscribers.)',
  'Shown when the plans you already pay for need no upgrade and no middleware fee for this integration. It isn&#39;t a claim that the integration is free for non-subscribers.', 1),
 ('Price unavailable: one or more plan prices could not be found in our data, so the totals below are partial. Do not treat them as a complete cost.',
  'If a plan price is missing from our data, the totals below are partial and shouldn&#39;t be treated as a complete cost.', 1),
 ('Showing the cheapest tiers with API access — but the native integration is unavailable on these tiers. Use the middleware path for the real middleware cost.',
  'With the required plans switched off, this shows the cheapest plans with API access, where the native integration isn&#39;t available; use the middleware path for the real cost.', 1),
 ('Verified sources <span class="font-normal normal-case">(Oct 2026)</span>', 'Verified sources', 1),
]
for f in sorted(glob.glob("stack/*/index.html")):
    s = open(f, encoding="utf-8").read()
    v = compute(json.loads(re.search(r'id="calc-data">(.*?)</script>', s, re.S).group(1)))
    pairs = list(CALC)
    if v["native"] and v["UP"] <= 0.004:   # nothing hidden to pay: don't promise "Hidden API Fees"
        pairs.append(("True Price, Minimum Plan &amp; Hidden API Fees", "Plans, Setup &amp; True Price", None))
    else:                                  # there is an extra cost (e.g. after a correction): keep/restore the original H1
        pairs.append(("Plans, Setup &amp; True Price", "True Price, Minimum Plan &amp; Hidden API Fees", None))
    s0 = s
    for a, b, n in pairs:
        if b in s and a not in s: continue
        if n is not None: assert s.count(a) == n, (f, a[:60], s.count(a))
        s = s.replace(a, b)
    if s != s0: open(f, "w", encoding="utf-8").write(s); changed.append(f)

# --- HubSpot hub
changed += ["hubspot-integrations-cost"] * edit("hubspot-integrations-cost/index.html", [
 ("HubSpot's $20/seat Starter plan looks affordable — until an integration\n      demands a higher tier for API access or webhooks. This matrix compares the",
  "Most HubSpot integrations work on the free CRM, but a few need a paid Professional\n      subscription. This matrix compares the", 1),
 ("The most common HubSpot hidden cost is the <strong>API access gate</strong>:\n      workflows that sync deals, timelines, or custom objects often require\n      Professional-tier features.",
  "The most common HubSpot hidden cost is a <strong>Professional subscription</strong>:\n      the Salesforce connector and the Asana workflow action need one, and webhook actions in\n      workflows need Data Hub Professional specifically.", 1),
 ("modeled at about $9–$20 a month", "modeled at $10.59 (Make Core) to $29.99 (Zapier Professional) a month", 2),
 ('Verified pricing &amp; API documentation sources <span class="text-sm font-normal text-slate-500">(Oct 2026)</span>', "Verified pricing &amp; API documentation sources", 1),
])
# --- Salesforce hub
sf = open("salesforce-integrations-cost/index.html", encoding="utf-8").read()
n_sf = len(set(re.findall(r'href="/stack/([^"/]*salesforce[^"/]*)/"', sf)))
changed += ["salesforce-integrations-cost"] * edit("salesforce-integrations-cost/index.html", [
 ("That single add-on is the biggest\n      hidden cost in B2B integrations, and it applies to most connections\n      below. This matrix shows the true cost of 5 Salesforce\n      integrations.",
  f"That add-on is the most common\n      hidden cost in Salesforce integrations, and it applies to most connections\n      below. This matrix shows the true cost of {n_sf} Salesforce\n      integrations.", 1),
 ('<span class="text-sm font-normal text-slate-500">(Oct 2026)</span>', "", None),
], required=False)
# --- CRM guide
crm = open("crm-integration-pricing-guide/index.html", encoding="utf-8").read()
n_crm = len(set(re.findall(r'href="/stack/([^"/]+)/"', crm)))
changed += ["crm-integration-pricing-guide"] * edit("crm-integration-pricing-guide/index.html", [
 ("This guide compares 21 \nintegrations", f"This guide compares {n_crm} \nintegrations", 1),
 ("Native requires a 3–5x tier jump", "Native forces a big plan upgrade (typically $120–$251/mo at 10 seats in our research)", 1),
 ('<span class="text-sm font-normal text-slate-500">(Oct 2026)</span>', "", None),
], required=False)
# --- homepage: unsourced "3-5x", defensive line, changelog brought up to date
changed += ["index"] * edit("index.html", [
 ("can force a\n          3–5x price jump once you actually connect your tools.",
  "can cost a lot more\n          once you actually connect your tools: in our research, a forced upgrade typically adds $120–$251 a month for a 10-person team.", 1),
 ("\nThis index is maintained by humans, not scraped and forgotten. Recent verification activity:\n", "\nRecent verification activity:\n", 1),
 ('<ul class="mt-5 space-y-3 text-sm leading-relaxed text-slate-600"> <li><strong class="text-slate-800">Nov 3, 2026</strong>',
  '<ul class="mt-5 space-y-3 text-sm leading-relaxed text-slate-600"> '
  '<li><strong class="text-slate-800">Nov 8, 2026</strong> — Three integrations corrected after re-reading vendor pages: ActiveCampaign + Stripe needs ActiveCampaign Plus ($49/mo), Mailchimp + Calendly works on Mailchimp&#39;s free plan ($120/mo), and Pipedrive + Xero now runs through Make because Pipedrive&#39;s own Xero app is gone ($177.59/mo). The Integration Tax report now counts 31 of 55 integrations with a hidden cost. Also: stale counts on the guides fixed, each cost box states its own extra cost, and every page names its editor.</li> '
  '<li><strong class="text-slate-800">Nov 5, 2026</strong> — HubSpot Professional repriced at HubSpot&#39;s per-seat price (Smart CRM Professional, $50/seat): HubSpot + Salesforce now $1,750/mo and HubSpot + Asana $634.90/mo at 10 seats.</li> '
  '<li><strong class="text-slate-800">Nov 4, 2026</strong> — QuickBooks Online prices updated ($38 / $75 / $115), Pipedrive + Mailchimp re-checked, and four QuickBooks and Pipedrive integrations added.</li> '
  '<li><strong class="text-slate-800">Nov 3, 2026</strong>', 1),
 (' <li><strong class="text-slate-800">Oct 17, 2026</strong> — Pricing re-audit: HubSpot Starter $20/seat · Salesforce Professional $100/user + $25/user/mo API add-on · Pipedrive Enterprise $99 — all confirmed.</li>', "", 1),
])
# --- About: say where prices don't come from the vendor page; drop the defensive line
changed += ["about"] * edit("about/index.html", [
 ("No third-party price aggregators, no estimates.",
  "Two exceptions are flagged wherever they apply: Pipedrive&#39;s prices come from an indexed copy of its pricing page and Make&#39;s monthly price from third-party reviews, because both sites block automated checks. ActiveCampaign, Pipedrive and Salesforce publish annual-billing rates only, so those are the rates used.", 1),
 ("date — evidence of active human maintenance, not a static snapshot.", "date.", None),
], required=False)

print("files changed:", len(changed))
