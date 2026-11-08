"""Rewrite pair-page API / webhook spec cells from apidata (verified 2026-11-03), and move the 4
re-checked pairs from 'pending' to 'partial'. Run from repo root after pairfix.py apply."""
import re, json, glob, html, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from apidata import TOOLS, API_VERIFIED
from pairdata8 import PARTIAL8
KEEP_WH = {"salesforce", "stripe"}  # webhook facts not re-checked for these
LAB = "Verified Nov 3, 2026"

def pick(srcs, keys):
    for l, u, q in srcs:
        if any(k in l.lower() for k in keys): return l, u
    return srcs[0][0], srcs[0][1]

def cell(old, yn, note, src):
    tier = re.search(r"<span class=\"text-slate-500\"> \('([^']*)'\)</span>", old).group(1)
    n = f' <span class="block text-xs text-slate-500">{html.escape(note)}</span>' if note else ""
    return (f" {yn} <span class=\"text-slate-500\"> ('{tier}')</span>{n}  <span class=\"block text-xs text-slate-500\">Source: "
            f"<a href=\"{html.escape(src[1], quote=True)}\" rel=\"noopener\" class=\"underline hover:text-indigo-600\">{html.escape(src[0])} ↗</a> · {LAB}</span> ")

changed = {"cells": 0, "pages": 0}
for f in sorted(glob.glob("stack/*/index.html")):
    s = open(f, encoding="utf-8").read(); s0 = s; p = f.split("/")[1]
    d = json.loads(re.search(r'id="calc-data">(.*?)</script>', s, re.S).group(1))
    for row, kind in (("API access at required tier", "api"), ("Webhook support at required tier", "wh")):
        m = re.search(r'(' + row + r'</td> <td class="px-4 py-3">)(.*?)(</td> <td class="px-4 py-3">)(.*?)(</td> </tr>)', s, re.S)
        parts = [m.group(2), m.group(4)]
        for i, t in enumerate(d["tools"]):
            T = TOOLS.get(t["slug"]); fact = T and T["plans"].get(t["required"])
            if not fact: continue
            if kind == "api":
                if t["slug"] not in API_VERIFIED: continue
                val = fact["api"]; note = fact["api_note"] or fact["lim"]
                if val == "Add-on": val, note = "Yes", (fact["api_note"] or "Paid API add-on")
                src = pick(T["sources"], ["api", "rate", "usage", "supported", "developers"])
            else:
                if t["slug"] in KEEP_WH or fact["wh"] not in ("Yes", "No"): continue
                val, note = fact["wh"], fact["wh_note"]
                src = pick(T["sources"], ["webhook"])
            if val not in ("Yes", "No"): continue
            new = cell(parts[i], val, note, src)
            if new != parts[i]: parts[i] = new; changed["cells"] += 1
        s = re.sub(r'(' + row + r'</td> <td class="px-4 py-3">).*?(</td> <td class="px-4 py-3">).*?(</td> </tr>)',
                   lambda mm: mm.group(1) + parts[0] + mm.group(2) + parts[1] + mm.group(3), s, count=1, flags=re.S)
    if p in PARTIAL8 and "(re-check pending)</span>" in s:
        m = re.search(r"<span>Prices checked against official vendor docs · Nov 3, 2026(.*?) · Integration requirements last checked · Oct 17, 2026 \(re-check pending\)</span>", s)
        assert m, p
        s = s[:m.start()] + f"<span>Integration requirements checked · Nov 3, 2026 ({PARTIAL8[p]}) · Prices checked · Nov 3, 2026{m.group(1)}</span>" + s[m.end():]
        a = "Prices last checked: Nov 3, 2026 · integration requirements: Oct 17, 2026"
        assert s.count(a) == 2, p
        s = s.replace(a, "Last checked: Nov 3, 2026 (exceptions listed at the top)")
        m = re.search(r'(Connection type</td> <td class="px-4 py-3" colspan="2">.*?)( · Verified Oct 17, 2026 )(</span>)', s, re.S); assert m, p
        s = s[:m.start(2)] + " · Verified Nov 3, 2026 " + s[m.end(2):]
        assert s.count('"lastReviewed":"2026-10-17"') == 1, p
        s = s.replace('"lastReviewed":"2026-10-17"', '"lastReviewed":"2026-11-03"')
    if s != s0:
        open(f, "w", encoding="utf-8").write(s); changed["pages"] += 1
print(changed)
