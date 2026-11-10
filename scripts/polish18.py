"""2026-11-10 round 3 (plugin re-audit). One-time, idempotent edits to text the generators don't manage.
Run from the repo root: python3 scripts/polish18.py   (then the usual pipeline; see scripts/README.md)."""
import glob, re

n = 0
MODEL_BOX = re.compile(r' <div class="rounded-2xl border border-slate-200 bg-slate-50 p-6"> <h2 class="font-bold text-slate-800">◐ Model Estimates .*?</div>(?= </section>)', re.S)
RECHECKED = {"activecampaign-and-stripe", "mailchimp-and-calendly", "pipedrive-and-xero"}   # requirements re-read Nov 8 (pairdata16)
for f in sorted(glob.glob("stack/*/index.html")):
    p = f.split("/")[1]
    s = open(f, encoding="utf-8").read(); s0 = s
    # the "Model Estimates" box repeated what the calculator's own labels say, on every page
    s = MODEL_BOX.sub("", s, count=1)
    s = s.replace('<section class="mt-8 grid gap-4 sm:grid-cols-2" aria-label="Verified facts versus estimates">', '<section class="mt-8" aria-label="Verified facts versus estimates">')
    # decorative "!" badge: keep it out of the heading's accessible name
    s = s.replace('<span class="grid h-8 w-8 place-items-center rounded-full bg-amber-400 text-lg font-black text-amber-950">!</span>',
                  '<span class="grid h-8 w-8 place-items-center rounded-full bg-amber-400 text-lg font-black text-amber-950" aria-hidden="true">!</span>')
    names = re.search(r'<nav class="mb-6 text-sm text-slate-500" aria-label="Breadcrumb">.*?<span class="text-slate-700">(.*?)</span>', s, re.S).group(1)
    s = s.replace('<h2 class="text-xl font-bold">Frequently asked questions</h2>', f'<h2 class="text-xl font-bold">{names} integration: frequently asked questions</h2>')
    s = s.replace('<h2 class="text-xl font-bold">Related integrations</h2>', f'<h2 class="text-xl font-bold">Integrations related to {names}</h2>')
    if p in RECHECKED:   # the connection type was what got re-read on Nov 8
        s = re.sub(r'(Connection type</td> <td class="px-4 py-3" colspan="2"> <span[^>]*>[^<]*</span> <span class="ml-2 text-xs text-slate-500">.*?· Verified )Nov 3, 2026', r"\g<1>Nov 8, 2026", s, count=1, flags=re.S)
    if p == "stripe-and-slack":
        s = s.replace("<span>Integration requirements and prices checked against official vendor docs · Nov 3, 2026</span>",
                      "<span>Integration requirements and prices checked against official vendor docs · Nov 3, 2026 (setup steps: Nov 10, 2026)</span>")
    if p in RECHECKED:
        s = re.sub(r"Last checked: Nov 3, 2026( \(exceptions listed at the top\))? · Sources linked below\.",
                   lambda m: "Requirements checked: Nov 8, 2026; prices: Nov 3, 2026" + (m.group(1) or "") + " · Sources linked below.", s)
    if s != s0: open(f, "w", encoding="utf-8").write(s); n += 1

# hand-written guides: say what the FAQ is about
for d, label in (("hubspot-integrations-cost", "HubSpot integration costs"), ("salesforce-integrations-cost", "Salesforce integration costs"), ("crm-integration-pricing-guide", "CRM integration costs")):
    f = f"{d}/index.html"; s = open(f, encoding="utf-8").read()
    s2 = re.sub(r"(<h2[^>]*>)\s*Frequently asked questions\s*(</h2>)", lambda m: m.group(1) + label + ": frequently asked questions" + m.group(2), s)
    if s2 != s: open(f, "w", encoding="utf-8").write(s2); n += 1

# About: one editor, not a "research team"; price-check dates
f = "about/index.html"; s = open(f, encoding="utf-8").read(); s0 = s
s = re.sub(r"(<h2[^>]*>)Publisher &amp; research team(</h2>)", r"\1Publisher &amp; editor\2", s)
s = s.replace("Every cost figure on StackCostMatrix traces to one of these official sources.",
              "Every cost figure on StackCostMatrix links to one of these sources. The &ldquo;Last audited&rdquo; column says where a price doesn&#39;t come straight from the vendor&#39;s own page.")
s = s.replace("Pricing pages for 17 of the 20 tools below were re-checked on <strong>Nov 3, 2026</strong>;",
              "Pricing pages for 17 of the 20 tools below were re-checked between <strong>Nov 3 and Nov 5, 2026</strong>;")
ENTRY = ('<li><strong class="text-slate-800">Nov 10, 2026 — Setup guides, clearer Salesforce requirements, share images.</strong> '
         'Every integration page now opens with how the integration works and a link to the vendor&#39;s setup guide, and compares the native route with Make and Zapier in one table. '
         'Stripe + Slack gained step-by-step setup from Stripe&#39;s documentation. The Salesforce API page now explains how Professional gets API access and that some AppExchange apps work without the add-on, '
         'from Salesforce&#39;s developer docs; the HubSpot Professional guide covers the Salesforce side and HubSpot&#39;s one-time onboarding fees. '
         'The Integration Tax report adds a section on the three kinds of integration cost and a chart image. No prices or plan requirements changed.</li> ')
if "Nov 10, 2026 — Setup guides" not in s:
    a = '<ul class="mt-4 space-y-3 text-sm leading-relaxed text-slate-600"> <li><strong class="text-slate-800">Nov 8, 2026'
    assert s.count(a) == 1
    s = s.replace(a, '<ul class="mt-4 space-y-3 text-sm leading-relaxed text-slate-600"> ' + ENTRY + '<li><strong class="text-slate-800">Nov 8, 2026', 1)
if s != s0: open(f, "w", encoding="utf-8").write(s); n += 1

# homepage changelog
f = "index.html"; s = open(f, encoding="utf-8").read(); s0 = s
if "Nov 10, 2026</strong>" not in s:
    a = '<ul class="mt-5 space-y-3 text-sm leading-relaxed text-slate-600"> <li><strong class="text-slate-800">Nov 8, 2026</strong>'
    assert s.count(a) == 1
    s = s.replace(a, '<ul class="mt-5 space-y-3 text-sm leading-relaxed text-slate-600"> <li><strong class="text-slate-800">Nov 10, 2026</strong> — '
                  'Every integration page now starts with how it works and the vendor&#39;s setup guide, and compares the native route with Make and Zapier. '
                  'New: how Salesforce Professional gets API access, and a chart of the most expensive integrations. No prices changed.</li> '
                  '<li><strong class="text-slate-800">Nov 8, 2026</strong>', 1)
if s != s0: open(f, "w", encoding="utf-8").write(s); n += 1
print("pages changed:", n)
