"""Site UI pass (2026-11-04): header navigation on every page, an integration finder on the homepage hero
and the 404 page, a mobile fix for the byline separators, and a readable hero date. Idempotent. Run from repo root."""
import glob, html, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hubs import SHORT, load_pairs

STYLE_ID = "scm-ui"
# The site's theme (2026-11-11). The page's base CSS exposes design tokens (--font-sans, --color-indigo-*, --radius-*);
# this block re-points them, so every page follows without its markup changing.
# The idea is a printed fare chart: white paper, navy ink, thin rules, and one yellow highlighter that only ever marks
# money the sticker price doesn't show (a forced plan upgrade or a connector fee). Don't use the yellow as decoration.
CSS = r"""
@font-face{font-family:"Barlow";src:url(/fonts/barlow-400.woff2) format("woff2");font-weight:400 500;font-style:normal;font-display:swap}
@font-face{font-family:"Barlow";src:url(/fonts/barlow-600.woff2) format("woff2");font-weight:600 900;font-style:normal;font-display:swap}
@font-face{font-family:"Barlow Semi Condensed";src:url(/fonts/barlow-semi-condensed-600.woff2) format("woff2");font-weight:500 900;font-style:normal;font-display:swap}
@font-face{font-family:"Barlow fallback";src:local("Arial"),local("Liberation Sans"),local("Helvetica");size-adjust:FB_BODY%}
@font-face{font-family:"Barlow SC fallback";src:local("Arial"),local("Liberation Sans"),local("Helvetica");size-adjust:FB_HEAD%}
:root{
--ink:#16223f;--paper:#fff;--wash:#f2f4f8;--rule:#cfd6e2;--hl:#ffe45c;
--font-sans:"Barlow","Barlow fallback",system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;
--font-display:"Barlow Semi Condensed","Barlow SC fallback","Barlow",system-ui,-apple-system,"Segoe UI",Arial,sans-serif;
--color-indigo-50:#eef1f7;--color-indigo-100:#e1e6f0;--color-indigo-200:#c2cbdd;--color-indigo-400:#6b7ba3;--color-indigo-500:#3a4c7c;--color-indigo-600:#16223f;--color-indigo-700:#0d1730;--color-indigo-950:#0a1124;
--color-slate-900:#16223f;--color-slate-800:#1f2c4a;--color-slate-700:#2f3b58;--color-slate-600:#44506b;--color-slate-500:#5a6680;--color-slate-200:#cfd6e2;--color-slate-100:#e6eaf1;--color-slate-50:#f2f4f8;
--color-amber-50:#fff8cf;--color-amber-200:#ffe98a;--color-amber-300:#ffe45c;--color-amber-400:#ffd91a;--color-amber-700:#4d3f00;--color-amber-800:#332a00;--color-amber-900:#16223f;--color-amber-950:#16223f;
--radius-lg:4px;--radius-xl:6px;--radius-2xl:8px;--tracking-tight:0;--tracking-widest:0;
}
body{background:var(--paper)}
h1,h2,h3,th,output{font-family:var(--font-display);letter-spacing:0}
main h1{font-weight:700;line-height:1.08}
table,output{font-variant-numeric:tabular-nums lining-nums}
th{font-size:1.02em}
.uppercase{text-transform:none}
a.text-indigo-600,a.hover\:underline,main p a,main li a,main td a,main dd a,footer a,.scm-finder-msg a{text-decoration:underline;text-decoration-thickness:1px;text-underline-offset:.18em}
a.text-indigo-600:hover,main p a:hover,main li a:hover,main td a:hover,main dd a:hover,footer a:hover{text-decoration-thickness:2px}
a:focus-visible,button:focus-visible,select:focus-visible,input:focus-visible,summary:focus-visible{outline:2px solid var(--ink);outline-offset:2px}
.shadow-sm,.shadow-md,.hover\:shadow-md:hover{--tw-shadow:0 0 #0000;box-shadow:none}
.hover\:-translate-y-0\.5:hover{translate:none;transform:none}
a.rounded-xl.border:hover,a.rounded-2xl.border:hover{border-color:var(--ink)}
.cat-pill,.rounded-full{border-radius:4px}
main a[class*="bg-"]{text-decoration:none}
header.border-b{border-bottom:2px solid var(--ink)}
header a span{font-family:var(--font-display);font-weight:700;font-size:1.4rem}
.scm-nav{display:flex;align-items:center;gap:12px;font-size:.9375rem;font-weight:500;color:var(--ink)}
.scm-nav a{display:inline-block;padding:12px 2px;min-width:44px;text-align:center}
.scm-nav a:hover{text-decoration:underline;text-underline-offset:.3em}
@media (min-width:640px){.scm-nav{gap:18px}}
@media (max-width:479px){header .justify-between:has(.scm-nav){flex-wrap:wrap}.scm-nav{width:100%;justify-content:space-between}}
.scm-nav .scm-wide{display:none}
.scm-sep{display:none}
@media (min-width:640px){.scm-nav .scm-wide,.scm-sep{display:inline}.scm-nav .scm-narrow{display:none}}
.scm-finder{margin-top:26px;max-width:44rem;text-align:left}
.scm-finder-grid{display:grid;gap:12px}
@media (min-width:640px){.scm-finder-grid{grid-template-columns:1fr 1fr auto;align-items:end}}
.scm-finder label{display:block;margin-bottom:6px;font-size:.9375rem;font-weight:600;color:var(--ink)}
.scm-finder select{width:100%;border-radius:4px;border:1px solid var(--ink);padding:11px 12px;font-size:1rem;color:var(--ink);background:#fff}
.scm-finder button{border-radius:4px;border:0;padding:12px 20px;font-size:.95rem;font-weight:700;cursor:pointer;background:var(--ink);color:#fff}
.scm-finder button:hover{background:#0d1730}
.scm-finder-msg{margin-top:12px;font-size:.9rem;line-height:1.5}
.scm-finder-msg:empty{display:none}
.scm-finder-msg a{font-weight:600}
output{display:block}
.scm-steps{margin-top:.5rem;padding-left:1.5rem;list-style:decimal}
.scm-steps li{margin-top:.5rem;line-height:1.625;color:var(--color-slate-700)}
.scm-cta{display:inline-block;border-radius:4px;background:var(--ink);color:#fff;font-weight:700;font-size:.95rem;padding:12px 18px;text-decoration:none}
.scm-cta:hover{background:#0d1730}
.scm-fig{display:block;width:100%;max-width:560px;height:auto;border-radius:4px;border:1px solid var(--rule)}
.scm-chart{display:block;width:100%;max-width:480px;height:auto;font-family:inherit}
.scm-diagram{display:block;width:100%;max-width:400px;height:auto;font-family:inherit}
.scm-jump{display:flex;flex-wrap:wrap;align-items:center;gap:10px;margin-top:16px}
.scm-jump-l{font-size:.875rem;font-weight:600;color:var(--color-slate-600);margin-right:2px}
.scm-jump a{display:inline-flex;align-items:center;min-height:44px;padding:0 14px;border-radius:4px;border:1px solid var(--rule);background:#fff;color:var(--ink);font-size:.9375rem;font-weight:500;text-decoration:none}
.scm-jump a:hover{background:var(--wash);border-color:var(--ink)}
.scm-jump a.scm-jump-p,.scm-jump a.scm-jump-p:hover{background:var(--ink);border-color:var(--ink);color:#fff}
.scm-anchor{display:block;height:0;scroll-margin-top:16px}
h2[id],div[id=calculators]{scroll-margin-top:16px}
.text-xs{font-size:.8125rem;line-height:1.2rem}
nav[aria-label="Breadcrumb"] a{display:inline-block;padding:12px 4px 12px 0}
footer a{display:inline-block;padding:12px 0}
.sr-only{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border-width:0}
[data-msg]::before{content:attr(data-msg)}
.bg-emerald-700{background-color:#047857}
.hover\:bg-emerald-800:hover{background-color:#065f46}
.scm-hero{position:relative}
.scm-hero h1{font-size:clamp(2.1rem,7vw,3rem);line-height:1.06}
.scm-hero-lede{margin-top:14px;max-width:60ch;font-size:1.0625rem;line-height:1.6;color:var(--color-slate-700)}
.scm-hl{background:var(--hl);padding:0 .2em}
.scm-fare-wrap{margin-top:28px;padding:14px 0 6px;border-top:2px solid var(--ink);overflow-x:auto;-webkit-overflow-scrolling:touch}
.scm-fare{border-collapse:separate;border-spacing:2px;margin-left:-2px;font-family:var(--font-display);font-size:.9375rem;line-height:1.2;font-variant-numeric:tabular-nums lining-nums}
.scm-fare td{width:50px;min-width:50px;height:32px;padding:0;text-align:right}
.scm-fare td.scm-e{text-align:center;color:#c3cbd9}
.scm-fare td a{display:block;padding:7px 6px 6px;background:var(--wash);color:var(--ink);text-decoration:none;font-weight:500}
.scm-fare td.scm-x a{background:var(--hl)}
.scm-fare td a:hover,.scm-fare td a:focus-visible{background:var(--ink);color:#fff;outline:none}
.scm-fare td.scm-n{width:auto;padding:0 0 0 8px;text-align:left;font-weight:600;font-size:1rem;white-space:nowrap;color:var(--ink)}
.scm-fare tr:first-child td.scm-n{padding-left:2px}
.scm-skip{position:absolute;left:-9999px}
.scm-skip:focus{position:static;display:inline-block;margin-top:14px;font-weight:600;text-decoration:underline}
.scm-fare-key{margin-top:12px;display:flex;flex-wrap:wrap;gap:6px 22px;font-size:.9375rem;color:var(--color-slate-700)}
.scm-fare-key span{display:inline-flex;align-items:center;gap:8px}
.scm-fare-key i{display:inline-block;width:22px;height:14px;background:var(--wash)}
.scm-fare-key i.scm-x{background:var(--hl)}
.scm-fare-key i.scm-e{background:none;border:1px dotted #9aa5b8}
.scm-fare-note{margin-top:10px;max-width:70ch;font-size:.9375rem;line-height:1.55;color:var(--color-slate-600)}
@media (pointer:coarse){.scm-fare td{height:44px}.scm-fare td a{padding:13px 6px 12px}}
@media (min-width:1200px) and (pointer:fine){
.scm-hero-text{position:absolute;top:0;right:0;width:540px}
.scm-hero-text .scm-finder{margin:22px 0 0 auto;max-width:300px}
.scm-hero-text .scm-finder-grid{grid-template-columns:1fr;gap:10px}
.scm-fare-wrap{margin-top:0;padding-top:0;border-top:0;overflow:visible}
}
@media (max-width:639px){
.scm-jump{flex-wrap:nowrap;overflow-x:auto;-webkit-overflow-scrolling:touch;padding-bottom:6px;scrollbar-width:thin}
.scm-jump a,.scm-jump-l{flex:0 0 auto;white-space:nowrap}
td a{display:inline-block;padding:10px 0}
main h1{font-size:1.625rem;line-height:1.9rem}
.scm-fare td a{display:block;padding:13px 6px 12px}
.overflow-x-auto:has(table[class*="min-w-"])::before{content:"Swipe sideways to see the whole table";position:sticky;left:0;display:block;padding:8px 12px;font-size:.8125rem;color:var(--color-slate-600);background:var(--wash);border-bottom:1px solid var(--rule)}
}
@media (max-width:1099px){.scm-fare-wrap::before{content:"Swipe sideways to see the whole chart";position:sticky;left:0;display:block;margin-bottom:10px;padding:8px 12px;font-size:.8125rem;color:var(--color-slate-600);background:var(--wash)}}
"""
# Fallback faces are scaled so text set in Arial takes about the room Barlow will, which keeps the page from jumping
# when the web font arrives. The percentages were measured in Chromium (see scripts/README.md, "Theme").
CSS = CSS.replace("FB_BODY", "95.8").replace("FB_HEAD", "82")
STYLE = f'<style id="{STYLE_ID}">' + CSS + "</style>"
PRELOAD = ('<link rel="preload" href="/fonts/barlow-400.woff2" as="font" type="font/woff2" crossorigin>'
           '<link rel="preload" href="/fonts/barlow-semi-condensed-600.woff2" as="font" type="font/woff2" crossorigin>')
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

PRICE_NOTE = "Prices were re-checked on Nov 3–5, 2026 for 17 of 20 tools; exceptions are flagged on each page."   # keep in step with /about/
HERO_RE = re.compile(r'<section class="(?:rounded-2xl bg-indigo-600 px-6 py-12 text-white sm:px-12 sm:py-16|scm-hero)"[^>]*>.*?</section>', re.S)

def fare_chart():
    """The homepage chart: every indexed pair's 10-seat monthly total, laid out like a printed fare table.
    Each tool is named on the diagonal; a cell is the pair formed by its row and its column."""
    pairs = load_pairs()
    names, count, cell = {}, {}, {}
    for p in pairs:
        a, b = p["d"]["tools"]
        for t in (a, b):
            names[t["slug"]] = SHORT.get(t["slug"], t["name"]); count[t["slug"]] = count.get(t["slug"], 0) + 1
        cell[frozenset((a["slug"], b["slug"]))] = p
    order = sorted(names, key=lambda x: (-count[x], names[x].lower()))   # busiest tools first, so the chart is densest at the top left
    rows = []
    for i, sl in enumerate(order):
        tds = []
        for j in range(i):
            p = cell.get(frozenset((sl, order[j])))
            if not p:
                tds.append('<td class="scm-e" aria-hidden="true">·</td>'); continue
            v = p["v"]; extra = v["UP"] > 0.004; total = f"{round(v['N']):,}"
            label = html.escape(f"{v['na']} + {v['nb']}: ${total} a month for 10 seats, " + ("including a cost the pricing pages don't show up front" if extra else "no extra cost to connect"), quote=True)
            tds.append(f'<td{" class=\"scm-x\"" if extra else ""}><a href="/stack/{p["slug"]}/" aria-label="{label}" title="{label}">{total}</a></td>')
        rows.append(f'<tr>{"".join(tds)}<td class="scm-n" colspan="{len(order) - i}">{html.escape(names[sl])}</td></tr>')
    # A triangular chart has no column headers, so it isn't marked up as a data table: each cell's link names both tools
    # and the cost for screen readers, and the group label says what the chart is.
    table = ('<div class="scm-fare-wrap" role="group" aria-label="Cost chart: the monthly cost of each integration for 10 seats, in US dollars">'
             '<table class="scm-fare" role="presentation">' + "".join(rows) + "</table></div>")
    return table, len(pairs), len(order), sum(1 for p in pairs if p["v"]["UP"] > 0.004)

def hero_html(D):
    chart, n, tools, n_extra = fare_chart()
    return ('<section class="scm-hero" aria-label="Integration cost chart"> <div class="scm-hero-text"> '
            '<h1>What a SaaS integration really costs</h1> '
            f'<p class="scm-hero-lede">{n} integrations between {tools} business tools, priced for a 10-person team from each vendor&#39;s own pages, with the plan each one needs. '
            f'<span class="scm-hl">Yellow</span> marks the {n_extra} that include a cost the pricing page doesn&#39;t show up front: a forced plan upgrade or a connector fee.</p> '
            + finder_html(D, light=True) + ' <a class="scm-skip" href="#after-chart">Skip the chart</a> </div> ' + chart +
            ' <p class="scm-fare-key"><span><i class="scm-x"></i>Includes a forced upgrade or a connector fee</span><span><i></i>No extra cost to connect</span>'
            '<span><i class="scm-e"></i>Not priced in this index</span></p> '
            '<p class="scm-fare-note">Find one tool on the diagonal and the other below it; their cell is the monthly total in US dollars for 10 seats, on the plans the integration needs. '
            + PRICE_NOTE + '</p> <span id="after-chart" class="scm-anchor"></span> </section>')

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
        s = re.sub(r'<link rel="preload" href="/fonts/[^>]*>', "", s)   # font preloads sit right before the shared style block
        s = s.replace(f'<style id="{STYLE_ID}">', PRELOAD + f'<style id="{STYLE_ID}">', 1)
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
    assert len(HERO_RE.findall(s)) == 1
    s = HERO_RE.sub(lambda m: hero_html(D), s, count=1)   # replaces the old indigo block, or refreshes an earlier copy of the chart
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
