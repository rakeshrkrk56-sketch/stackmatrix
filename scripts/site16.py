"""Site-wide identity (2026-11-08): name the editor, and link every page's structured data to one Organization,
WebSite and Person (@id graph on the homepage and /about/). Idempotent; run after the generators and before
security.py:   python3 scripts/site16.py
Generators (apipages, hubs, hspro, research) already emit EDITOR/PUBLISHER from here, so this mainly covers
hand-written pages and the pair pages' static JSON-LD."""
import glob, json, re, os, sys

SITE = "https://stackcostmatrix.com"
EDITOR_NAME = "Rakesh Kumar"
EDITOR_URL = f"{SITE}/about/#editor"
EDITOR_PROFILE = "https://github.com/rakeshrkrk56-sketch"
EDITOR_LINKEDIN = "https://www.linkedin.com/in/rakesh-kumar-23960a204/"
ORG_ID, SITE_ID = f"{SITE}/#organization", f"{SITE}/#website"
EDITOR = {"@type": "Person", "@id": EDITOR_URL, "name": EDITOR_NAME, "url": EDITOR_URL}
PUBLISHER = {"@type": "Organization", "@id": ORG_ID, "name": "StackCostMatrix", "url": f"{SITE}/", "logo": f"{SITE}/icon-512.png"}
GRAPH = {"@context": "https://schema.org", "@graph": [
    {"@type": "Organization", "@id": ORG_ID, "name": "StackCostMatrix", "url": f"{SITE}/", "logo": f"{SITE}/icon-512.png",
     "email": "admin@stackcostmatrix.com", "founder": {"@id": EDITOR_URL},
     "description": "Independent index of what B2B software integrations really cost: the plan each integration needs, connector fees and API access by plan, checked against vendor documentation.",
     "sameAs": ["https://github.com/rakeshrkrk56-sketch/stackmatrix"]},
    {"@type": "WebSite", "@id": SITE_ID, "url": f"{SITE}/", "name": "StackCostMatrix", "publisher": {"@id": ORG_ID}, "inLanguage": "en"},
    {"@type": "Person", "@id": EDITOR_URL, "name": EDITOR_NAME, "url": EDITOR_URL, "jobTitle": "Founder and editor",
     "worksFor": {"@id": ORG_ID}, "sameAs": [EDITOR_LINKEDIN, EDITOR_PROFILE]}]}
BREADCRUMBS = {
    "hubspot-integrations-cost/index.html": [("HubSpot integration costs", f"{SITE}/hubspot-integrations-cost/")],
    "salesforce-integrations-cost/index.html": [("Salesforce integration costs", f"{SITE}/salesforce-integrations-cost/")],
    "crm-integration-pricing-guide/index.html": [("CRM integration pricing guide", f"{SITE}/crm-integration-pricing-guide/")],
    "about/index.html": [("About", f"{SITE}/about/")],
}
LINK = 'class="font-medium text-indigo-600 hover:underline"'
BYLINE_PAIR_OLD = 'Reviewed by the <strong class="text-slate-800">StackCostMatrix RevOps Research Team</strong>'
BYLINE_PAIR_NEW = f'Edited by <a href="/about/#editor" {LINK}>{EDITOR_NAME}</a>, founder of StackCostMatrix'
PROFILE_HTML = (f'Profiles: <a href="{EDITOR_LINKEDIN}" rel="noopener me" {LINK}>LinkedIn ↗</a> · '
                f'<a href="{EDITOR_PROFILE}" rel="noopener me" {LINK}>GitHub ↗</a>')
ABOUT_OLD = '<p class="leading-relaxed text-slate-600">\nStackCostMatrix is published as an independent research project. Our dataset'
ABOUT_NEW = ('<p class="leading-relaxed text-slate-600" id="editor">\n<strong class="text-slate-800">Editor: ' + EDITOR_NAME + '.</strong> '
             'StackCostMatrix is built and run by ' + EDITOR_NAME + ', who checks each price and plan requirement against the vendor&#39;s own pricing '
             'pages and documentation and reviews every change before it&#39;s published. Corrections go to the email below and are logged in the changelog. '
             f'{PROFILE_HTML}.\n</p> <p class="mt-3 leading-relaxed text-slate-600">\n'
             'StackCostMatrix is published as an independent research project. Our dataset')

def fix_ld(o):
    """Point authors/reviewers/publishers at the shared entities."""
    if isinstance(o, list): return [fix_ld(x) for x in o]
    if not isinstance(o, dict): return o
    out = {}
    for k, v in o.items():
        if k in ("author", "reviewedBy") and isinstance(v, dict) and ((v.get("@type") == "Organization" and "StackCostMatrix" in v.get("name", "")) or v.get("@id") == EDITOR_URL):
            out[k] = EDITOR
        elif k == "publisher" and isinstance(v, dict) and v.get("name") == "StackCostMatrix":
            out[k] = PUBLISHER
        else:
            out[k] = fix_ld(v)
    return out

def main():
    pages = sorted(set(glob.glob("*.html") + glob.glob("*/index.html") + glob.glob("stack/*/index.html")))
    n = 0
    for f in pages:
        if f.startswith(("site/", "scripts/", "agent_scripts/")) or f.startswith("google"): continue
        s = open(f, encoding="utf-8").read(); s0 = s
        if "<body" not in s: continue
        s = s.replace(BYLINE_PAIR_OLD, BYLINE_PAIR_NEW)
        def rep(m):
            o = json.loads(m.group(1))
            if f in ("index.html", "about/index.html") and (o.get("@type") in ("Organization", "WebSite") or "@graph" in o):
                return ""          # replaced by GRAPH below (the old WebSite SearchAction pointed at a search URL the site doesn't support)
            if f == "index.html" and o.get("@type") == "Dataset":
                o["description"] = ("Open dataset of what 59 B2B software integrations cost across 18 tools plus 2 connectors (Zapier and Make): per-seat prices per plan, "
                                    "the plan each integration needs, API and webhook access by plan, and connector fees. Every figure links to the vendor's pricing page or documentation, "
                                    "with the date it was checked; exceptions are flagged on each page.")
                o["creator"] = {"@id": ORG_ID}; o["publisher"] = {"@id": ORG_ID}
                o["distribution"] = [{"@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": f"{SITE}/data/integration-pairs.json"}]
                o["dateModified"] = "2026-11-08"
            return '<script type="application/ld+json">' + json.dumps(fix_ld(o), ensure_ascii=False, separators=(",", ":")) + "</script>"
        s = re.sub(r'<script type="application/ld\+json">(.*?)</script>', rep, s, flags=re.S)
        crumbs = BREADCRUMBS.get(f)
        if crumbs and '"@type":"BreadcrumbList"' not in s:
            bl = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": i, "name": n, "item": u} for i, (n, u) in enumerate([("Home", f"{SITE}/")] + crumbs, 1)]}
            s = s.replace("</head>", '<script type="application/ld+json">' + json.dumps(bl, ensure_ascii=False, separators=(",", ":")) + "</script></head>", 1)
        if f in ("index.html", "about/index.html"):
            s = s.replace("</head>", '<script type="application/ld+json">' + json.dumps(GRAPH, ensure_ascii=False, separators=(",", ":")) + "</script></head>", 1)
        if f == "about/index.html" and ABOUT_OLD in s:
            s = s.replace(ABOUT_OLD, ABOUT_NEW, 1)
        if f == "about/index.html":   # keep the editor's profile links current
            s = re.sub(r'Profiles?: <a href="[^"]*"[^>]*>(?:LinkedIn|GitHub) ↗</a>(?: · <a href="[^"]*"[^>]*>GitHub ↗</a>)?', lambda m: PROFILE_HTML, s, count=1)
        # 1200x630 share image for link previews (was the 512px square logo)
        s = s.replace('<meta property="og:image" content="https://stackcostmatrix.com/icon-512.png">',
                      '<meta property="og:image" content="https://stackcostmatrix.com/og-image.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">')
        s = s.replace('<meta name="twitter:card" content="summary">', '<meta name="twitter:card" content="summary_large_image">')
        # pair pages: their own card (og17.py); every page: article schema image = the share image, not the logo
        img = f"{SITE}/og-image.png"
        if f.startswith("stack/") and os.path.exists(f"og/{f.split('/')[1]}.jpg"):
            img = f"{SITE}/og/{f.split('/')[1]}.jpg"
            s = re.sub(r'<meta property="og:image" content="[^"]*">', f'<meta property="og:image" content="{img}">', s, count=1)
        s = s.replace('"image":"https://stackcostmatrix.com/icon-512.png"', f'"image":"{img}"')
        t = re.search(r'<meta property="og:title" content="([^"]*)"', s)
        s = re.sub(r'<meta property="og:image:alt"[^>]*>', "", s)   # generated pages inherit their template's
        if t:
            s = re.sub(r'(<meta property="og:image" content="[^"]*">(?:<meta property="og:image:width"[^>]*><meta property="og:image:height"[^>]*>)?)',
                       lambda m: m.group(1) + f'<meta property="og:image:alt" content="{t.group(1)} — StackCostMatrix">', s, count=1)
        if s != s0: open(f, "w", encoding="utf-8").write(s); n += 1
    # 404: send reversed pair URLs (/stack/b-and-a/) to the page that exists; drop the 404 page's canonical
    pairs = sorted(f.split("/")[1] for f in glob.glob("stack/*/index.html"))
    rev = {"-and-".join(p.split("-and-")[::-1]): p for p in pairs if p.count("-and-") == 1}
    js = ('(function(){var r=' + json.dumps(rev, separators=(",", ":")) + ';var m=location.pathname.match(/^\\/stack\\/([a-z0-9-]+)\\/?$/);'
          'if(m&&r[m[1]])location.replace("/stack/"+r[m[1]]+"/"+location.search+location.hash)})();')
    f = "404.html"; s = open(f, encoding="utf-8").read(); s0 = s
    s = re.sub(r'<link rel="canonical"[^>]*>', "", s)
    s = re.sub(r'<script id="scm-rev">.*?</script>', "", s, flags=re.S)
    s = s.replace("</head>", f'<script id="scm-rev">{js}</script></head>', 1)
    if s != s0: open(f, "w", encoding="utf-8").write(s); n += 1
    # /go redirect pages: noindex already; a cross-domain canonical only sends a mixed signal
    for f in glob.glob("go/*.html"):
        s = open(f, encoding="utf-8").read(); s2 = re.sub(r'<link rel="canonical"[^>]*>\n?', "", s)
        if s2 != s: open(f, "w", encoding="utf-8").write(s2); n += 1
    print(f"site identity: {n} pages updated")

if __name__ == "__main__":
    main()
