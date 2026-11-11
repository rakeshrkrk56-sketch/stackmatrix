"""2026-11-11, with the new theme. One-time, idempotent edits to the three hand-written guides:
the small "Pillar guide" label above the heading goes (the generated pages lost theirs in their generators).
Also adds the new design to the Nov 11 changelog entries on the About page and the homepage."""
import re
n = 0
for d in ("hubspot-integrations-cost", "salesforce-integrations-cost", "crm-integration-pricing-guide"):
    f = f"{d}/index.html"; s = open(f, encoding="utf-8").read()
    s2 = re.sub(r'\s*<p class="text-sm font-semibold uppercase tracking-widest text-indigo-600">\s*Pillar guide\s*</p>', " ", s, count=1)
    if s2 != s: open(f, "w", encoding="utf-8").write(s2); n += 1
print("guides changed:", n)

# changelog: the new design, added to the Nov 11 entries
f = "about/index.html"; s = open(f, encoding="utf-8").read()
NOTE = (" The site also has a new design: the homepage opens with a chart of every integration&#39;s cost, the typeface is Barlow, "
        "and yellow is used only to mark costs a pricing page doesn&#39;t show up front.")
if NOTE not in s:
    a = "so 52 of the 59 integration pages now have steps."
    assert s.count(a) == 1
    s = s.replace(a, a + NOTE, 1); open(f, "w", encoding="utf-8").write(s); print("about: design note added")
f = "index.html"; s = open(f, encoding="utf-8").read()
NOTE = " New design: the homepage opens with a cost chart of every pair."
if NOTE not in s:
    a = "Connector-based integrations (Make, Zapier) gained numbered setup steps."
    assert s.count(a) == 1
    s = s.replace(a, a + NOTE, 1); open(f, "w", encoding="utf-8").write(s); print("home: design note added")
