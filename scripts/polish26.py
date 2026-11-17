"""2026-11-17. One-time, idempotent: the changelog entries for the fix in pairdata26.py (14 calculators now list each tool's
free plan when it has API access, as the report does) on the About page and the homepage. The figures are a dated record
of that day, so they are written out here rather than computed. Run before site16.py (it reads the newest changelog date)."""
n = 0
UL_A = '<ul class="mt-4 space-y-3 text-sm leading-relaxed text-slate-600"> '
UL_H = '<ul class="mt-5 space-y-3 text-sm leading-relaxed text-slate-600"> '

f = "about/index.html"; s = open(f, encoding="utf-8").read(); s0 = s
ENTRY = ('<li><strong class="text-slate-800">Nov 17, 2026 — 14 calculators now start from the free plan.</strong> '
         'The calculators on 14 integration pages started from the cheapest paid plan of Calendly, Mailchimp, ClickUp or Slack, although each '
         'of those tools&#39; free plan includes API access. They now start from the free plan, as the Integration Tax report always has, so each '
         'page&#39;s hidden cost matches the report: HubSpot + Calendly, for example, now shows a $120 a month upgrade (Calendly Standard for 10 seats) '
         'instead of none. 53 of the 90 integrations now show a hidden cost on their pages and on the homepage chart, as in the report (48 did before). '
         'The comparison with Make and Zapier now uses Calendly Standard, because Make&#39;s Calendly trigger needs a paid Calendly plan. '
         'No prices or plan requirements changed.</li> ')
MARK_A = "Nov 17, 2026 — 14 calculators now start from the free plan."
if MARK_A not in s:
    a = UL_A + '<li><strong class="text-slate-800">Nov 15, 2026'
    assert s.count(a) == 1
    s = s.replace(a, UL_A + ENTRY + '<li><strong class="text-slate-800">Nov 15, 2026', 1)
if s != s0: open(f, "w", encoding="utf-8").write(s); n += 1

f = "index.html"; s = open(f, encoding="utf-8").read(); s0 = s
HOME = ('<li><strong class="text-slate-800">Nov 17, 2026</strong> — 14 integration pages now count the free plan of Calendly, Mailchimp, ClickUp '
        'or Slack as the starting point, as the report does, so 53 of 90 show a hidden cost. No prices changed.</li> ')
MARK_H = "Nov 17, 2026</strong> — 14 integration pages now count the free plan"
if MARK_H not in s:
    a = UL_H + '<li><strong class="text-slate-800">Nov 15, 2026</strong>'
    assert s.count(a) == 1
    s = s.replace(a, UL_H + HOME + '<li><strong class="text-slate-800">Nov 15, 2026</strong>', 1)
if s != s0: open(f, "w", encoding="utf-8").write(s); n += 1
print("pages changed:", n)
