"""2026-11-14. One-time, idempotent: the changelog entries for the Integration Tax report's update to all 90 pairs,
on the About page and the homepage. The figures are a dated record of that day's report (research.py), so they are
written out here rather than computed. Run from the repo root, before site16.py (it reads the newest changelog date)."""
n = 0
UL_A = '<ul class="mt-4 space-y-3 text-sm leading-relaxed text-slate-600"> '
UL_H = '<ul class="mt-5 space-y-3 text-sm leading-relaxed text-slate-600"> '

f = "about/index.html"; s = open(f, encoding="utf-8").read(); s0 = s
ENTRY = ('<li><strong class="text-slate-800">Nov 14, 2026 — The Integration Tax report now covers all 90 pairs.</strong> '
         'The report was published on Nov 3 with the 55 integrations then in the index; it now includes the 35 added since, and will follow the index from here on. '
         'Its figures changed accordingly: 53 of 90 integrations carry a hidden cost (was 31 of 55); 28 force a plan upgrade (was 19), typically $120 to $320 a month '
         'for 10 seats (was $120 to $251); 25 only need a connector (was 12); and the highest is $600 a month, for Intercom + Salesforce and Salesforce + Calendly '
         '(was $500, for the two integrations that need HubSpot Professional). The method is unchanged. No prices or plan requirements changed.</li> ')
if "Nov 14, 2026 — The Integration Tax report now covers" not in s:
    a = UL_A + '<li><strong class="text-slate-800">Nov 12, 2026'
    assert s.count(a) == 1
    s = s.replace(a, UL_A + ENTRY + '<li><strong class="text-slate-800">Nov 12, 2026', 1)
if s != s0: open(f, "w", encoding="utf-8").write(s); n += 1

f = "index.html"; s = open(f, encoding="utf-8").read(); s0 = s
HOME = ('<li><strong class="text-slate-800">Nov 14, 2026</strong> — The Integration Tax report now covers all 90 integrations, not only the 55 it was published with: '
        '53 of 90 carry a hidden cost. No prices changed.</li> ')
if "Nov 14, 2026</strong> — The Integration Tax report now covers" not in s:
    a = UL_H + '<li><strong class="text-slate-800">Nov 12, 2026</strong>'
    assert s.count(a) == 1
    s = s.replace(a, UL_H + HOME + '<li><strong class="text-slate-800">Nov 12, 2026</strong>', 1)
if s != s0: open(f, "w", encoding="utf-8").write(s); n += 1
print("pages changed:", n)
