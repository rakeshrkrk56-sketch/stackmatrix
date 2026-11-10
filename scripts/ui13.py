"""Site UI pass (2026-11-04): header navigation on every page, an integration finder on the homepage hero
and the 404 page, a mobile fix for the byline separators, and a readable hero date. Idempotent. Run from repo root."""
import glob, html, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hubs import SHORT

STYLE_ID = "scm-ui"
STYLE = f"""<style id="{STYLE_ID}">
.scm-nav{{display:flex;align-items:center;gap:12px;font-size:.875rem;font-weight:500;color:#475569}}
.scm-nav a{{display:inline-block;padding:12px 2px}}
@media (min-width:640px){{.scm-nav{{gap:18px}}}}
@media (max-width:479px){{header .justify-between:has(.scm-nav){{flex-wrap:wrap}}.scm-nav{{width:100%;justify-content:space-between}}.scm-nav a{{padding:12px 2px}}}}
.scm-nav a:hover{{color:#4f46e5}}
.scm-nav .scm-wide{{display:none}}
.scm-sep{{display:none}}
@media (min-width:640px){{.scm-nav .scm-wide,.scm-sep{{display:inline}}.scm-nav .scm-narrow{{display:none}}}}
.scm-finder{{margin-top:28px;max-width:46rem;border-radius:16px;padding:16px;background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.28)}}
.scm-finder.scm-light{{background:#fff;border:1px solid #e2e8f0;box-shadow:0 1px 2px rgba(0,0,0,.05);text-align:left}}
.scm-finder-grid{{display:grid;gap:12px}}
@media (min-width:640px){{.scm-finder-grid{{grid-template-columns:1fr 1fr auto;align-items:end}}}}
.scm-finder label{{display:block;margin-bottom:6px;font-size:.75rem;font-weight:600;letter-spacing:.05em;text-transform:uppercase;color:#fff}}
.scm-finder.scm-light label{{color:#475569}}
.scm-finder select{{width:100%;border-radius:12px;border:1px solid #cbd5e1;padding:11px 12px;font-size:1rem;color:#0f172a;background:#fff}}
.scm-finder button{{border-radius:12px;border:0;padding:12px 20px;font-size:.95rem;font-weight:700;cursor:pointer;background:#fff;color:#4338ca}}
.scm-finder.scm-light button{{background:#4f46e5;color:#fff}}
.scm-finder button:hover{{background:#eef2ff}}
.scm-finder.scm-light button:hover{{background:#4338ca}}
.scm-finder select:focus-visible,.scm-finder button:focus-visible{{outline:2px solid #fff;outline-offset:2px}}
.scm-finder.scm-light select:focus-visible,.scm-finder.scm-light button:focus-visible{{outline-color:#4f46e5}}
.scm-finder-msg{{margin-top:12px;font-size:.9rem;line-height:1.5}}
.scm-finder-msg:empty{{display:none}}
.scm-finder-msg a{{text-decoration:underline;font-weight:600}}
output{{display:block}}
.scm-steps{{margin-top:.5rem;padding-left:1.5rem;list-style:decimal}}
.scm-steps li{{margin-top:.5rem;line-height:1.625;color:#334155}}
.scm-cta{{display:inline-block;border-radius:.75rem;background:#4f46e5;color:#fff;font-weight:700;font-size:.95rem;padding:12px 18px}}
.scm-cta:hover{{background:#4338ca}}
.scm-fig{{display:block;width:100%;max-width:560px;height:auto;border-radius:12px;border:1px solid #e2e8f0}}
.scm-chart{{display:block;width:100%;max-width:480px;height:auto;font-family:inherit}}
.scm-jump{{display:flex;flex-wrap:wrap;align-items:center;gap:10px;margin-top:16px}}
.scm-jump-l{{font-size:.8125rem;font-weight:600;color:#475569;margin-right:2px}}
.scm-jump a.scm-jump-p{{background:#4f46e5;border-color:#4f46e5;color:#fff}}
.scm-jump a.scm-jump-p:hover{{background:#4338ca}}
.scm-jump a{{display:inline-flex;align-items:center;min-height:44px;padding:0 14px;border-radius:999px;border:1px solid #c7d2fe;background:#eef2ff;color:#3730a3;font-size:.875rem;font-weight:600}}
.scm-jump a:hover{{background:#e0e7ff}}
.scm-anchor{{display:block;height:0;scroll-margin-top:16px}}
h2[id],div[id=calculators]{{scroll-margin-top:16px}}
.text-xs{{font-size:.8125rem;line-height:1.2rem}}
.scm-nav a{{min-width:44px;text-align:center}}
nav[aria-label="Breadcrumb"] a{{display:inline-block;padding:12px 4px 12px 0}}
footer a{{display:inline-block;padding:11px 0}}
@media (max-width:639px){{
.scm-jump{{flex-wrap:nowrap;overflow-x:auto;-webkit-overflow-scrolling:touch;padding-bottom:6px;scrollbar-width:thin}}
.scm-jump a,.scm-jump-l{{flex:0 0 auto;white-space:nowrap}}
td a{{display:inline-block;padding:10px 0}}
main h1{{font-size:1.5rem;line-height:2rem}}
.overflow-x-auto:has(table[class*="min-w-"])::before{{content:"Swipe sideways to see the whole table \2192";position:sticky;left:0;display:block;padding:8px 12px;font-size:.8125rem;color:#475569;background:#f8fafc;border-bottom:1px solid #e2e8f0}}
}}
.sr-only{{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border-width:0}}
[data-msg]::before{{content:attr(data-msg)}}
.bg-emerald-700{{background-color:#047857}}
.hover\\:bg-emerald-800:hover{{background-color:#065f46}}
</style>"""
OLD_NAV = '<nav class="flex items-center gap-4 text-sm font-medium text-slate-600"> <a href="/" class="hover:text-indigo-600">All pairs</a> </nav>'
NEW_NAV = ('<nav class="scm-nav" aria-label="Main"> <a href="/#tools" class="scm-wide">Integrations by tool</a> <a href="/#tools" class="scm-narrow">Tools</a> '
           '<a href="/#pairs" class="scm-wide">All pairs</a> <a href="/#pairs" class="scm-narrow">Pairs</a> <a href="/integration-tax-2026/">Research</a> <a href="/about/">About</a> </nav>')
SEP_OLD = '<span class="text-slate-300" aria-hidden="true">|</span>'
SEP_NEW = '<span class="text-slate-300 scm-sep" aria-hidden="true">|</span>'

def finder_html(D, light=False):
    hubs = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "hubs.json")))
    tools = sorted(((sl, SHORT.get(sl, t["name"])) for sl, t in D["tools"].items()), key=lambda x: x[1].lower())
    pairs = {"|".join(sorted(p["pair"].split("-and-"))): p["url"].replace("https://stackcostmatrix.com", "") for p in D["pairs"]}
    data = {"t": dict(tools), "p": pairs, "h": {k: v["url"] for k, v in hubs.items()}}
    opts = "".join(f'<option value="{sl}">{html.escape(n)}</option>' for sl, n in tools)
    cls = "scm-finder scm-light" if light else "scm-finder"
    return (f'<form class="{cls}" id="scm-finder" role="search" aria-label="Find an integration"> <div class="scm-finder-grid"> '
            f'<div><label for="scm-a">Tool you use</label><select id="scm-a" required><option value="">Choose a tool…</option>{opts}</select></div> '
            f'<div><label for="scm-b">Tool to connect</label><select id="scm-b" required><option value="">Choose a tool…</option>{opts}</select></div> '
            f'<div><button type="submit">See the cost</button></div> </div> <p class="scm-finder-msg" id="scm-msg" aria-live="polite"></p> </form>'
            f'<script type="application/json" id="scm-finder-data">{json.dumps(data, separators=(",", ":"))}</script>'
            '<script>(function(){var f=document.getElementById("scm-finder");if(!f)return;var d=JSON.parse(document.getElementById("scm-finder-data").textContent),'
            'a=document.getElementById("scm-a"),b=document.getElementById("scm-b"),m=document.getElementById("scm-msg");'
            'function key(x,y){return [x,y].sort().join("|")}'
            'function fillB(){var sel=b.value,av=a.value,on=[],off=[];Object.keys(d.t).forEach(function(s){if(s===av)return;'
            '(av&&d.p[key(av,s)]?on:off).push(s)});b.innerHTML="";var o=document.createElement("option");o.value="";o.textContent="Choose a tool…";b.appendChild(o);'
            'function grp(label,list){if(!list.length)return;var g=document.createElement("optgroup");g.label=label;list.forEach(function(s){var op=document.createElement("option");'
            'op.value=s;op.textContent=d.t[s];g.appendChild(op)});b.appendChild(g)}'
            'if(av){grp("Covered with "+d.t[av],on);grp("Not covered yet",off)}else{grp("All tools",off)}if(sel&&sel!==av)b.value=sel;m.textContent=""}'
            'a.addEventListener("change",fillB);b.addEventListener("change",function(){m.textContent=""});'
            'f.addEventListener("submit",function(e){e.preventDefault();var x=a.value,y=b.value;m.textContent="";'
            'if(!x||!y){m.textContent="Pick two tools.";return}var u=d.p[key(x,y)];if(u){window.location.href=u;return}'
            'm.textContent="We haven\\u2019t covered "+d.t[x]+" + "+d.t[y]+" yet. ";var hub=d.h[x]||d.h[y];'
            'if(hub){var l=document.createElement("a");l.href=hub.url||hub;l.textContent="See all "+d.t[d.h[x]?x:y]+" integrations";m.appendChild(l);m.appendChild(document.createTextNode(" \\u00b7 "))}'
            'var r=document.createElement("a");r.href="mailto:admin@stackcostmatrix.com?subject="+encodeURIComponent("Please add "+d.t[x]+" + "+d.t[y]);'
            'r.textContent="Ask us to add it";m.appendChild(r)});fillB()})();</script>')

def main():
    D = json.load(open("data/integration-pairs.json", encoding="utf-8"))
    files = sorted(set(glob.glob("*.html") + glob.glob("*/index.html") + glob.glob("stack/*/index.html")))
    n = {"style": 0, "nav": 0, "sep": 0}
    for f in files:
        s = open(f, encoding="utf-8").read(); s0 = s
        if OLD_NAV not in s and 'class="scm-nav"' not in s: continue
        if f'id="{STYLE_ID}"' not in s:
            s = s.replace("</head>", STYLE + "</head>", 1); n["style"] += 1
        else:   # refresh an older copy of the shared style block
            s2 = re.sub(r'<style id="' + STYLE_ID + r'">.*?</style>', lambda m: STYLE, s, count=1, flags=re.S)
            if s2 != s: s = s2; n["style"] += 1
        if OLD_NAV in s: s = s.replace(OLD_NAV, NEW_NAV, 1); n["nav"] += 1
        else:   # refresh an older copy of the menu
            s2 = re.sub(r'<nav class="scm-nav" aria-label="Main">.*?</nav>', lambda m: NEW_NAV, s, count=1, flags=re.S)
            if s2 != s: s = s2; n["nav"] += 1
        if SEP_OLD in s: n["sep"] += s.count(SEP_OLD); s = s.replace(SEP_OLD, SEP_NEW)
        if s != s0: open(f, "w", encoding="utf-8").write(s)
    # homepage: anchors, finder, readable date
    f = "index.html"; s = open(f, encoding="utf-8").read()
    s = s.replace('<section class="mt-12" aria-label="Integration costs by tool">', '<section class="mt-12" id="tools" aria-label="Integration costs by tool">', 1)
    s = s.replace('<section class="mt-12"> <h2 class="text-2xl font-bold tracking-tight">All integration pairs</h2>', '<section class="mt-12" id="pairs"> <h2 class="text-2xl font-bold tracking-tight">All integration pairs</h2>', 1)
    s = s.replace('<p class="text-3xl font-bold">2026-11-03</p>', '<p class="text-3xl font-bold">Nov 3, 2026</p>', 1)
    s = re.sub(r' ?<form class="scm-finder[^"]*" id="scm-finder".*?\}\)\(\);</script>', "", s, flags=re.S)
    a = 'before you sign up.\n</p>'
    assert s.count(a) == 1
    s = s.replace(a, a + " " + finder_html(D), 1)
    open(f, "w", encoding="utf-8").write(s)
    # 404 page
    f = "404.html"; s = open(f, encoding="utf-8").read()
    s = re.sub(r'<form class="scm-finder[^"]*" id="scm-finder".*?\}\)\(\);</script>', "", s, flags=re.S)
    a = '<p class="mt-4 text-sm text-slate-500">\nLooking for a specific pair? Try the search on the  <a href="/" class="font-medium text-indigo-600 hover:underline">homepage</a>.\n</p>'
    if a in s:
        s = s.replace(a, '<p class="mt-8 text-sm text-slate-500"> Looking for a specific pair? Pick your two tools: </p> ' + finder_html(D, light=True), 1)
    else:
        s = s.replace("Pick your two tools: </p> ", "Pick your two tools: </p> " + finder_html(D, light=True), 1)
    open(f, "w", encoding="utf-8").write(s)
    print(n, "pages scanned", len(files))

if __name__ == "__main__":
    main()
