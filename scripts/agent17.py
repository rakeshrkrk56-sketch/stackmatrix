"""Agent-readiness files (2026-11-08, round 2). Run from the repo root after the page generators and site16.py,
before security.py:   python3 scripts/agent17.py
- every page gets a Markdown copy next to it (<dir>/index.md) and a <link rel="alternate" type="text/markdown">
- llms.txt (regenerated: research, hubs, API pages, every integration pair) and llms-full.txt (pair table + key pages)
- pair-page calculators: inputs wrapped in a <form method="dialog"> (no navigation) and totals marked up as <output>"""
import glob, json, re, html as H
from markdownify import markdownify

SITE = "https://stackcostmatrix.com"
SKIP = ("site/", "scripts/", "agent_scripts/", "go/", "data/", "_astro/")

def pages():
    fs = glob.glob("index.html") + glob.glob("*/index.html") + glob.glob("stack/*/index.html")
    return sorted(f for f in fs if not f.startswith(SKIP))

def url_of(f): return f"{SITE}/" + ("" if f == "index.html" else f[:-len("index.html")])
def md_path(f): return f[:-len(".html")] + ".md"
def md_href(f): return "/" + md_path(f)

def to_markdown(f, s):
    title = H.unescape(re.search(r"<title>(.*?)</title>", s, re.S).group(1)).strip()
    desc = H.unescape(re.search(r'<meta name="description" content="([^"]*)"', s).group(1))
    main = s[s.index("<main"):s.index("</main>")]
    main = re.sub(r'<section[^>]*aria-label="True Cost of Ownership Calculator">.*?</section>',
                  "<p><em>Interactive cost calculator: open the web page to change team size, billing and add-ons.</em></p>", main, flags=re.S)
    main = re.sub(r"<(script|style|form|template)[^>]*>.*?</\1>", "", main, flags=re.S)
    main = re.sub(r'<nav class="scm-jump"[^>]*>.*?</nav>', "", main, flags=re.S)   # in-page jump links mean nothing in Markdown
    main = re.sub(r'<svg class="scm-chart"[^>]*aria-label="([^"]*)"[^>]*>.*?</svg>', lambda m: f"<p>Chart: {m.group(1)}</p>", main, flags=re.S)
    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", main, re.S)
    if h1: title = H.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", h1.group(1)))).strip(); main = main[:h1.start()] + main[h1.end():]
    main = re.sub(r'<figure[^>]*> <img src="(/og/[^"]+)"[^>]*alt="([^"]*)"[^>]*> <figcaption[^>]*>.*?</figcaption> </figure>',
                  lambda m: f'<p>Image: <a href="{m.group(1)}">{m.group(2)}</a></p>', main, flags=re.S)
    main = re.sub(r'<[^>]+class="[^"]*\bhidden\b[^"]*"[^>]*>.*?</(?:p|div)>', "", main, flags=re.S)
    md = markdownify(main, heading_style="ATX", bullets="-", strip=["img", "svg", "button", "input", "label", "select", "option"])
    md = re.sub(r"\n{3,}", "\n\n", md).strip()
    md = re.sub(r"\]\((/[^)]*)\)", lambda m: "](" + SITE + m.group(1) + ")", md)   # absolute links
    head = (f"# {title}\n\n> {desc}\n\nSource page: {url_of(f)}  \nPublisher: StackCostMatrix · Editor: Rakesh Kumar · "
            f"Data licence: CC BY 4.0 (credit StackCostMatrix and link to {SITE})\n\n---\n\n")
    return head + md + "\n"

CALC_FORM_OPEN = '<section class="mt-10 rounded-2xl border border-slate-200 bg-white p-6 shadow-sm sm:p-8" aria-label="True Cost of Ownership Calculator">'
def calc_semantics(s):
    if CALC_FORM_OPEN in s and 'id="calc-form"' not in s:
        a = s.index(CALC_FORM_OPEN) + len(CALC_FORM_OPEN)
        b = s.index("</section>", a)
        s = s[:a] + ' <form method="dialog" id="calc-form" aria-label="Integration cost calculator">' + s[a:b] + "</form> " + s[b:]
    # state messages that JS shows/hides: keep the text in data-msg (rendered by CSS ::before) so it isn't
    # page text that crawlers or AI quote out of context next to the real totals
    for k in ("calc-unavailable", "calc-warning"):
        s = re.sub(r'(<p id="' + k + r'" class="[^"]*")>\s*([^<]+?)\s*</p>',
                   lambda m: m.group(1) + ' data-msg="' + m.group(2).replace('"', "&quot;") + '"></p>', s, count=1)
    s = re.sub(r'(<div id="calc-included-badge"[^>]*> )<p class="font-bold text-emerald-900">([^<]+)</p> <p class="mt-1 text-sm text-emerald-800">([^<]+)</p>',
               lambda m: m.group(1) + f'<p class="font-bold text-emerald-900" data-msg="{m.group(2)}"></p> <p class="mt-1 text-sm text-emerald-800" data-msg="{m.group(3)}"></p>', s, count=1)
    for k in ("calc-total", "calc-incr", "calc-year1", "calc-tco3"):
        s = re.sub(r'<p (class="[^"]*") id="' + k + r'">([^<]*)</p>',
                   lambda m: f'<output {m.group(1)} id="{k}" for="calc-seats calc-tier-toggle calc-incremental calc-annual">{m.group(2)}</output>', s, count=1)
    return s

def add_captions(s):
    """Give every data table a caption (screen readers and AI parsers use it), taken from the nearest heading above."""
    out, pos = [], 0
    for m in re.finditer(r"<table\b[^>]*>", s):
        out.append(s[pos:m.end()]); pos = m.end()
        if s[pos:pos + 40].lstrip().startswith("<caption"): continue
        hs = re.findall(r"<h[123][^>]*>(.*?)</h[123]>", s[:m.start()], re.S)
        if not hs: continue
        cap = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", hs[-1])).strip()
        if cap: out.append(f' <caption class="sr-only">{cap}</caption>')
    out.append(s[pos:])
    return "".join(out)

def main():
    D = json.load(open("data/integration-pairs.json", encoding="utf-8"))
    n_md = 0
    for f in pages():
        s = open(f, encoding="utf-8").read(); s0 = s
        if "<main" not in s: continue
        if f.startswith("stack/"): s = calc_semantics(s)
        s = add_captions(s)
        link = f'<link rel="alternate" type="text/markdown" href="{md_href(f)}">'
        s = re.sub(r'<link rel="alternate" type="text/markdown" href="[^"]*">', "", s)   # generated pages inherit their template's link
        s = s.replace("</head>", link + "</head>", 1)
        if f == "index.html" and 'href="/llms.txt"' not in s:
            s = s.replace("</head>", '<link rel="alternate" type="text/plain" href="/llms.txt" title="llms.txt">' + "</head>", 1)
        if s != s0: open(f, "w", encoding="utf-8").write(s)
        md = to_markdown(f, s)
        old = open(md_path(f), encoding="utf-8").read() if glob.glob(md_path(f)) else None
        if md != old: open(md_path(f), "w", encoding="utf-8").write(md); n_md += 1

    # llms.txt
    hubs = sorted(f.split("/")[0] for f in glob.glob("*-integrations-cost/index.html"))
    apis = sorted(f.split("/")[0] for f in glob.glob("*-api-access/index.html"))
    title = lambda f: H.unescape(re.search(r"<title>(.*?)</title>", open(f, encoding="utf-8").read(), re.S).group(1)).split(" | ")[0].strip()
    pairs = sorted(D["pairs"], key=lambda p: p["pair"])
    L = ["# StackCostMatrix", "",
         "> Independent index of what B2B software integrations really cost: the plan each integration needs on both tools, any connector fee (Make, Zapier), and API and webhook access by plan, "
         f"for {len(pairs)} integration pairs across 20 tools. Every figure links to the vendor's own pricing page or documentation, with the date it was checked. Edited by Rakesh Kumar. Data is free to reuse under CC BY 4.0.",
         "", "Costs are for a 10-person team at monthly-billing list prices unless a page says otherwise. Exceptions (prices that come from somewhere other than the vendor's page, or annual-only rates) are flagged on each page and on the About page. Every page also has a Markdown copy at <page>/index.md.",
         "", "## Research and data", "",
         f"- [The Integration Tax 2026]({SITE}/integration-tax-2026/): original research on the extra monthly cost of connecting 55 popular SaaS integrations, with method, figures and a suggested citation",
         f"- [Open dataset (JSON)]({SITE}/data/integration-pairs.json): every pair, plan price, minimum plan, connector fee and source, CC BY 4.0",
         f"- [Which integrations need HubSpot Professional]({SITE}/hubspot-professional-integrations/): the plan each HubSpot integration needs and the cheapest way to get Professional",
         f"- [Full text for LLMs]({SITE}/llms-full.txt): every pair in one table plus the key pages",
         "", "## Integration costs by tool", ""]
    L += [f"- [{title(h + '/index.html')}]({SITE}/{h}/)" for h in hubs]
    L += [f"- [CRM integration pricing guide]({SITE}/crm-integration-pricing-guide/)", "", "## API and webhook access by plan", ""]
    L += [f"- [{title(a + '/index.html')}]({SITE}/{a}/)" for a in apis]
    L += ["", "## Integration pairs", ""]
    for p in pairs:
        plans = " + ".join(f"{k} {v}" for k, v in p["minimum_plans"].items())
        L.append(f"- [{' + '.join(p['tools'])}]({p['url']}): {p['connection_type']}, needs {plans}, ${p['ten_seat_monthly_cost_usd']:,}/mo for 10 seats")
    L += ["", "## About", "", f"- [About, methodology and changelog]({SITE}/about/)", "- Corrections: admin@stackcostmatrix.com", ""]
    open("llms.txt", "w", encoding="utf-8").write("\n".join(L))

    # llms-full.txt: pair table + key pages in Markdown
    F = ["# StackCostMatrix: full text for LLMs", "", f"Source: {SITE} · Editor: Rakesh Kumar · Licence: CC BY 4.0 (credit StackCostMatrix and link to {SITE})", "",
         "## Every integration pair (10 seats, monthly-billing list prices)", "",
         "| Integration | Connection | Minimum plans | Connector $/mo | Total $/mo | Sync | Checked | Page |", "|---|---|---|---|---|---|---|---|"]
    for p in pairs:
        plans = "; ".join(f"{k}: {v}" for k, v in p["minimum_plans"].items())
        F.append(f"| {' + '.join(p['tools'])} | {p['connection_type']} | {plans} | {p['middleware_monthly_usd']} | {p['ten_seat_monthly_cost_usd']} | {p['sync_direction']} | {p.get('last_reviewed', p.get('date_modified', ''))} | {p['url']} |")
    for f in ("integration-tax-2026/index.html", "hubspot-professional-integrations/index.html", "about/index.html"):
        F += ["", "---", "", open(md_path(f), encoding="utf-8").read()]
    open("llms-full.txt", "w", encoding="utf-8").write("\n".join(F) + "\n")

    # robots.txt: no Content-Signal line. It's a draft (contentsignals.org) and Lighthouse/PageSpeed flag it as an
    # unknown directive, costing the SEO score; the allow-all rules already permit search and AI use.
    r = open("robots.txt", encoding="utf-8").read()
    r2 = re.sub(r"Content-Signal:[^\n]*\n", "", r)
    if r2 != r: open("robots.txt", "w", encoding="utf-8").write(r2)
    print(f"agent files: {n_md} Markdown copies written, llms.txt ({len(pairs)} pairs), llms-full.txt, robots.txt")

if __name__ == "__main__":
    main()
