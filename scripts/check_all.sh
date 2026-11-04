#!/usr/bin/env bash
# Run every site check. Usage (from the repo root): bash scripts/check_all.sh
# Exits non-zero if any check fails. Needs python3 and node with playwright (for the calculator check).
set -u
cd "$(dirname "$0")/.."
OUT=scripts/.out; mkdir -p "$OUT"
fail=0
step() { echo; echo "== $1"; }

step "Pair renderer self-test (re-renders every pair page; must reproduce it exactly)"
python3 scripts/pairfix.py selftest | tee "$OUT/selftest.txt"
grep -q "selftest mismatches: 0 " "$OUT/selftest.txt" || fail=1

step "Consistency audit (calculator data vs every place a page states it)"
python3 scripts/consistency.py | tail -1 | tee "$OUT/consistency.txt"
grep -q "issues: 0 " "$OUT/consistency.txt" || fail=1

step "CSS classes, JSON blocks, internal links, FAQ markup, titles"
python3 - <<'EOF' || fail=1
import glob, html, json, os, re, sys
sys.path.insert(0, "scripts")
src = open("scripts/classcheck.py").read().split("for f in sys.argv[1:]")[0]
exec(src)
pages = [f for f in glob.glob("*.html") + glob.glob("*/index.html") + glob.glob("stack/*/index.html") if "<body" in open(f, encoding="utf-8").read()]
bad = 0
for f in pages:
    s = open(f, encoding="utf-8").read()
    miss = [c for c in check(f) if not c.startswith("scm-") and c != "cat-pill"]
    if miss: print("missing CSS classes:", f, miss[:5]); bad += 1
    for b in re.findall(r'<script type="application/(?:ld\+)?json"[^>]*>(.*?)</script>', s, re.S):
        try: json.loads(b)
        except Exception as e: print("bad JSON:", f, e); bad += 1
    for h in re.findall(r'href="(/[^"#?]*)', s):
        p = h.lstrip("/")
        if p and not (os.path.exists(p) or os.path.exists(os.path.join(p, "index.html")) or os.path.exists(p + ".html")):
            print("broken link:", f, h); bad += 1
    lds = [json.loads(b) for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)]
    faq = next((o for o in lds if o.get("@type") == "FAQPage"), None)
    if faq:
        norm = lambda x: html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", x))).strip()
        pairs = re.findall(r'<h3 class="font-semibold text-slate-900">([^<]*)</h3> <p class="mt-1 leading-relaxed text-slate-700">(.*?)</p>', s, re.S)
        pairs += re.findall(r'<summary class="cursor-pointer font-semibold text-slate-900">(.*?)</summary> <p class="mt-2 text-sm leading-relaxed text-slate-600">(.*?)</p>', s, re.S)
        vis = {norm(x) for t in pairs for x in t}
        for q in faq["mainEntity"]:
            if norm(q["name"]) not in vis or norm(q["acceptedAnswer"]["text"]) not in vis: print("FAQ markup differs from visible text:", f, q["name"][:60]); bad += 1
    t = re.search(r"<title>(.*?)</title>", s)
    if t and len(html.unescape(t.group(1))) > 60 and "/stack/" in f: print("title over 60 chars:", f); bad += 1
print(f"{len(pages)} pages checked, {bad} problems")
sys.exit(1 if bad else 0)
EOF

step "Calculator in a real browser (all pair pages, monthly + annual)"
python3 - > "$OUT/expected.json" <<'EOF'
import glob, json, re
out = {}
for f in sorted(glob.glob("stack/*/index.html")):
    p = f.split("/")[1]; d = json.loads(re.search(r'id="calc-data">(.*?)</script>', open(f).read(), re.S).group(1)); m = a = 0
    for t in d["tools"]:
        x = next(u for u in t["tiers"] if u["tier_name"] == t["required"]); seats = max(10, x.get("minSeats", 1))
        add = 25 * seats if t["slug"] == "salesforce" and x["tier_name"] == "Professional" else 0
        m += x["base"] + x["perSeat"] * seats + add
        a += x.get("annualBase", x["base"]) + x.get("annualPerSeat", x["perSeat"]) * seats + add
    m += d["middleware"]; a += d.get("middlewareAnnual", d["middleware"])
    out[p] = [round(m, 2), round(m * 12, 2), round(a * 12, 2), round(a * 36, 2)]
print(json.dumps(out))
EOF
python3 -m http.server 8765 >/dev/null 2>&1 & SRV=$!
sleep 1
node scripts/check7.js "$PWD/$OUT/expected.json" | tee "$OUT/calc.txt"
kill $SRV 2>/dev/null
grep -q "mismatches 0 js errors 0" "$OUT/calc.txt" || fail=1

echo
if [ $fail -eq 0 ]; then echo "ALL CHECKS PASSED"; else echo "SOME CHECKS FAILED"; fi
exit $fail
