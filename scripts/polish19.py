"""2026-11-11. One-time, idempotent edits to the three hand-written guides, which the generators don't manage.
Run from the repo root before ux18.py:   python3 scripts/polish19.py
- HubSpot and Salesforce hubs: the hidden-cost heading becomes a question (its first sentence already answers it),
  with a short label for the "On this page" row
- all three: dateModified moves to 2026-11-11, because their tables, charts and headings changed on Nov 10 and 11"""
import re

H2S = {
    "hubspot-integrations-cost": ("The HubSpot API tier trap", "Which HubSpot integrations need a Professional plan?", "The Professional trap"),
    "salesforce-integrations-cost": ("The $25/user/month API trap, explained", "Does Salesforce Professional need a paid API add-on?", "The API add-on"),
}
n = 0
for d in ("hubspot-integrations-cost", "salesforce-integrations-cost", "crm-integration-pricing-guide"):
    f = f"{d}/index.html"; s = open(f, encoding="utf-8").read(); s0 = s
    if d in H2S:
        old, new, chip = H2S[d]
        s = re.sub(r"<h2((?:(?!data-chip)[^>])*)>(\s*)" + re.escape(old) + r"(\s*)</h2>",
                   lambda m: f'<h2{m.group(1)} data-chip="{chip}">{m.group(2)}{new}{m.group(3)}</h2>', s, count=1)
        assert new in s, d
    s = s.replace('"dateModified":"2026-11-03"', '"dateModified":"2026-11-11"').replace('"dateModified": "2026-11-03"', '"dateModified": "2026-11-11"')
    if s != s0: open(f, "w", encoding="utf-8").write(s); n += 1
print("guides changed:", n)
