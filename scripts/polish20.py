"""2026-11-11. One-time, idempotent: the Nov 11 changelog entries on the About page and the homepage.
Run from the repo root: python3 scripts/polish20.py   (then site16.py, which reads the newest changelog date)."""
n = 0
f = "about/index.html"; s = open(f, encoding="utf-8").read(); s0 = s
ENTRY = ('<li><strong class="text-slate-800">Nov 11, 2026 — Connection diagrams, question headings, editor background.</strong> '
         'Every integration page gained a diagram of how the two tools connect: what moves, in which direction, through which connector and on which plans. '
         'Each diagram is drawn from the facts already on its page; none is a screenshot. '
         'Section headings on the tool hubs and API pages became questions answered in their first sentence, and the About page now gives the editor&#39;s background. '
         'No prices or plan requirements changed.</li> ')
if "Nov 11, 2026 — Connection diagrams" not in s:
    a = '<ul class="mt-4 space-y-3 text-sm leading-relaxed text-slate-600"> <li><strong class="text-slate-800">Nov 10, 2026'
    assert s.count(a) == 1
    s = s.replace(a, '<ul class="mt-4 space-y-3 text-sm leading-relaxed text-slate-600"> ' + ENTRY + '<li><strong class="text-slate-800">Nov 10, 2026', 1)
if s != s0: open(f, "w", encoding="utf-8").write(s); n += 1

f = "index.html"; s = open(f, encoding="utf-8").read(); s0 = s
if "Nov 11, 2026</strong>" not in s:
    a = '<ul class="mt-5 space-y-3 text-sm leading-relaxed text-slate-600"> <li><strong class="text-slate-800">Nov 10, 2026</strong>'
    assert s.count(a) == 1
    s = s.replace(a, '<ul class="mt-5 space-y-3 text-sm leading-relaxed text-slate-600"> <li><strong class="text-slate-800">Nov 11, 2026</strong> — '
                  'Every integration page gained a diagram of how the two tools connect: what moves, in which direction and on which plans. '
                  'Hub and API page headings became questions. No prices changed.</li> '
                  '<li><strong class="text-slate-800">Nov 10, 2026</strong>', 1)
if s != s0: open(f, "w", encoding="utf-8").write(s); n += 1
print("pages changed:", n)
