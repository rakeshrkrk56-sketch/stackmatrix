"""Rebuild the homepage FAQPage JSON-LD from the FAQ that is visible on the page, so the two always match.
Run from the repo root: python3 scripts/homefaq.py"""
import html, json, re

f = "index.html"
s = open(f, encoding="utf-8").read()
vis = re.findall(r'<summary class="cursor-pointer font-semibold text-slate-900">(.*?)</summary> <p class="mt-2 text-sm leading-relaxed text-slate-600">(.*?)</p>', s, re.S)
assert vis, "no visible FAQ found"
def text(x): return html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", x))).strip()
entities = [{"@type": "Question", "name": text(q), "acceptedAnswer": {"@type": "Answer", "text": text(a)}} for q, a in vis]

def fix(m):
    o = json.loads(m.group(1))
    if o.get("@type") == "FAQPage": o["mainEntity"] = entities
    return '<script type="application/ld+json">' + json.dumps(o, ensure_ascii=False, separators=(",", ":")) + "</script>"
s2 = re.sub(r'<script type="application/ld\+json">(.*?)</script>', fix, s, flags=re.S)
if s2 != s:
    open(f, "w", encoding="utf-8").write(s2)
print(f"homepage FAQ markup: {len(entities)} questions, matching the visible FAQ")
