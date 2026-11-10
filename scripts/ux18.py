"""In-page navigation (2026-11-10): an "On this page" row of jump links under each page's intro, with the anchors they
point to. Long pages put the calculator and tables well below the fold; this gets readers there in one tap.
Idempotent. Run after the page generators and pairfix, before site16/agent17/security:   python3 scripts/ux18.py

Pair pages: anchors are separate <span class="scm-anchor"> elements placed where pairfix.py's patterns don't reach
(pairfix re-renders must reproduce the page byte for byte). Other pages: ids go on the <h2> elements."""
import glob, html, re

SKIP = {"index.html", "404.html", "privacy/index.html", "terms/index.html"}
NAV_RE = re.compile(r' ?<nav class="scm-jump" aria-label="On this page">.*?</nav>', re.S)
ANCHOR_RE = re.compile(r'<span id="[a-z0-9-]+" class="scm-anchor"></span> ?')

PRIMARY = {"calculator", "calculators"}   # the chip that leads to the cost calculator(s) is filled

def nav(items):
    return (' <nav class="scm-jump" aria-label="On this page"><span class="scm-jump-l">On this page</span>'
            + "".join(f'<a href="#{i}"{" class=\"scm-jump-p\"" if i in PRIMARY else ""}>{html.escape(t, quote=False)}</a>' for i, t in items) + "</nav>")

def slug(t):
    return re.sub(r"[^a-z0-9]+", "-", html.unescape(re.sub(r"<[^>]+>", "", t)).lower()).strip("-")[:48]

PAIR_ANCHORS = [  # (id, marker that starts the section, anchor goes inside the tag?)
    ("calculator", '<section class="mt-10 rounded-2xl border border-slate-200 bg-white p-6 shadow-sm sm:p-8" aria-label="True Cost of Ownership Calculator">', False),
    ("routes", '<section class="mt-10 rounded-xl border border-slate-200 bg-white p-6 shadow-sm sm:p-8" aria-label="Native versus middleware">', False),
    ("requirements", '<section class="mt-8 rounded-2xl bg-amber-50 p-6 ring-1 ring-amber-300 sm:p-8" aria-label="Hidden Cost Trap">', False),
    ("specs", '<section class="mt-10" aria-label="Specification matrix">', True),
    ("faq", '<section class="mt-12" aria-label="Frequently asked questions">', False),
]
PAIR_CHIPS = [("how-it-works", "How it works"), ("calculator", "Cost calculator"), ("routes", "Native vs Make or Zapier"),
              ("requirements", "Plans needed"), ("specs", "Spec matrix"), ("faq", "FAQ")]

def pair_page(s):
    for i, marker, inside in PAIR_ANCHORS:
        assert s.count(marker) == 1, (i, s.count(marker))
        a = f'<span id="{i}" class="scm-anchor"></span>'
        s = s.replace(marker, marker + " " + a if inside else a + " " + marker, 1)
    chips = [c for c in PAIR_CHIPS if f'id="{c[0]}"' in s]
    lede = re.search(r'<p class="mt-4 max-w-3xl text-lg leading-relaxed text-slate-700">.*?</p>', s, re.S)
    return s[:lede.end()] + nav(chips) + s[lede.end():]

def other_page(s):
    a, b = s.index("<main"), s.index("</main>")
    main = s[a:b]
    items = []
    def h2(m):
        attrs, inner = m.group(1), m.group(2)
        text = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", inner))).strip()
        mid = re.search(r'\bid="([^"]+)"', attrs)
        i = mid.group(1) if mid else slug(text)
        if not i or not text: return m.group(0)
        items.append((i, text if len(text) <= 46 else text[:44].rsplit(" ", 1)[0] + "…"))
        return m.group(0) if mid else f'<h2{attrs} id="{i}">{inner}</h2>'
    main = re.sub(r"<h2([^>]*)>(.*?)</h2>", h2, main, flags=re.S)
    if len(items) < 3: return s
    faq = [x for x in items if "frequently asked" in x[1].lower()]
    items = [x for x in items if x not in faq][:5] + ([(faq[0][0], "FAQ")] if faq else [])
    # the first table that links to pair calculators gets an anchor and a filled "Cost calculators" chip
    main = re.sub(r' id="calculators"', "", main)
    for m in re.finditer(r'<div class="[^"]*overflow-x-auto[^"]*">', main):
        end = main.find("</table>", m.end())
        if end > 0 and 'href="/stack/' in main[m.end():end]:
            main = main[:m.end() - 1] + ' id="calculators">' + main[m.end():]
            items.insert(0, ("calculators", "Cost calculators"))
            break
    h1 = main.index("</h1>")
    by = re.compile(r'<p class="mt-3 text-sm text-slate-500">.*?</p>', re.S).search(main, h1)
    first_h2 = main.index("<h2", h1)
    pos = by.end() if by and by.start() < first_h2 and by.start() - h1 < 40 else main.index("</p>", h1) + 4
    main = main[:pos] + nav(items) + main[pos:]
    return s[:a] + main + s[b:]

GUIDE_FIG_RE = re.compile(r' ?<figure class="mt-6" data-guide="1">.*?</figure>', re.S)
def guide_figures():
    """The hand-written HubSpot and Salesforce hubs and the CRM guide get their summary card as an in-page figure."""
    import os, sys
    sys.path.insert(0, os.path.dirname(__file__))
    from hubs import load_pairs
    from model import money
    m0 = lambda x: money(x).replace(".00", "")
    pairs = {p["slug"]: p for p in load_pairs()}
    done = 0
    for d, label in (("hubspot-integrations-cost", "HubSpot integration costs"), ("salesforce-integrations-cost", "Salesforce integration costs"),
                     ("crm-integration-pricing-guide", "CRM integration costs for HubSpot, Salesforce and Pipedrive")):
        f = f"{d}/index.html"
        if not os.path.exists(f"og/{d}.jpg"): continue
        s0 = open(f, encoding="utf-8").read(); s = GUIDE_FIG_RE.sub("", s0)
        mine = [pairs[x]["v"]["N"] for x in set(re.findall(r'href="/stack/([^"/]+)/"', s[s.index("<main"):s.index("</main>")])) if x in pairs]
        fig = (f' <figure class="mt-6" data-guide="1"> <img src="/og/{d}.jpg" width="1200" height="630" loading="lazy" class="scm-fig" '
               f'alt="{label} summary: {len(mine)} integrations priced, from {m0(min(mine))} to {m0(max(mine))} a month for 10 seats"> '
               f'<figcaption class="mt-2 text-xs text-slate-500">{label} at a glance. Free to reuse with credit (CC BY 4.0).</figcaption> </figure>')
        a = s.index("</table> </div>", s.index("<main")) + len("</table> </div>")
        s = s[:a] + fig + s[a:]
        if s != s0: open(f, "w", encoding="utf-8").write(s); done += 1
    return done

def main():
    n = guide_figures()
    for f in sorted(set(glob.glob("*/index.html") + glob.glob("stack/*/index.html"))):
        if f in SKIP or f.startswith(("site/", "scripts/", "go/")): continue
        s0 = open(f, encoding="utf-8").read()
        if "<main" not in s0: continue
        s = ANCHOR_RE.sub("", NAV_RE.sub("", s0))
        s = pair_page(s) if f.startswith("stack/") else other_page(s)
        if s != s0: open(f, "w", encoding="utf-8").write(s); n += 1
    print(f"jump links: {n} pages updated")

if __name__ == "__main__":
    main()
