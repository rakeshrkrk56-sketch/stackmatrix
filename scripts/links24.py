"""Internal links, rebuilt on every build (2026-11-15).

Why: the related-pair cards, the "by tool" lists and the guide tables were written once, when a page was created, and
then went stale. None of the 59 older pair pages linked to any of the 31 pairs added later, nine pairs had no link from
another pair page, the Freshdesk hub was missing from the homepage, from three guides and from its own pair pages, and
217 links said only "Calculator →".

What this script writes. Each block is replaced on every run, so the build stays repeatable:
  pair pages     the "Related integrations" section, and one sentence under the spec table that leads to the two tools'
                 API pages (pairfix.py doesn't render either place, so its self-test is unaffected)
  homepage       the "by tool" grid and the list of API pages
  HubSpot hub, Salesforce hub, CRM guide (the three hand-written pages)
                 both link lists, one "related research" sentence, and the pair table: the pair's name is now the
                 link and the "Guide" column, which repeated one phrase on every row, is gone
  every page     the footer's "Cost guides" list. Pages built from a template by a newpairs script had the template's
                 first link rewritten (seven pages pointed "Intercom integration costs" and the like at another hub,
                 two listed Salesforce twice); the list is now the same everywhere and its pair count is computed
  About page, homepage   the changelog entry for this change (once)
The generated hubs and the API pages get the same lists from hubs.py and apipages.py (index_list).

Which pairs a page links to: each tool's partners are put in a ring, ordered by category and then by name, and a page
links to its three nearest neighbours in each of its two rings. So:
  - a pair whose two tools both have four or more integrations gets at least six links from other pair pages (a page
    whose other tool has only three integrations takes four cards from this side, so some pairs get seven);
  - a new pair is linked from older pages on the next build, with no wiring;
  - adding a pair only changes the cards of its neighbours in the two rings, not the whole site.

Run after pairfix.py, hubs.py, apipages.py and the polish scripts, and before ux18.py:   python3 scripts/links24.py
"""
import glob, html, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hubs import load_pairs, index_list, hub_links, esc, LINK, REPORT
from apipages import api_links
from model import money

HERE = os.path.dirname(os.path.abspath(__file__))
MODIFIED = "2026-11-15"          # the day the hand-written pages' links last changed (their JSON-LD dateModified)
CRM_GUIDE, HSPRO = "/crm-integration-pricing-guide/", "/hubspot-professional-integrations/"
CAT_ORDER = ["CRM", "Email Marketing", "Helpdesk", "Communication", "Scheduling", "Project Management", "Productivity", "Accounting", "Payments"]
PER_SIDE, TOTAL = 3, 6           # cards per tool, cards per page
OFFSETS = [o for k in range(1, 60) for o in (k, -k)]   # nearest first: +1, -1, +2, -2, ...
HAND_WRITTEN = {"hubspot-integrations-cost/index.html": "hubspot", "salesforce-integrations-cost/index.html": "salesforce",
                "crm-integration-pricing-guide/index.html": None}   # page -> the tool whose hub it is

def read(f): return open(f, encoding="utf-8").read()
def save(f, s, s0):
    if s != s0: open(f, "w", encoding="utf-8").write(s)
    return s != s0
def link(url, text): return f'<a href="{url}" {LINK}>{text}</a>'
def join(xs):
    xs = list(xs)
    return xs[0] if len(xs) == 1 else ", ".join(xs[:-1]) + " and " + xs[-1]


# ---------- which pairs a page links to ----------
def tool_categories(home):
    """Tool -> category, read from the homepage cards (data-cats lists the two tools' categories in the slug's order)."""
    votes = {}
    for slug, cats in re.findall(r'<a href="/stack/([^/"]+)/" data-search="[^"]*" data-cats="([^"]*)"', home):
        cs = html.unescape(cats).split("|"); a, b = slug.split("-and-")
        for t, c in ((a, cs[0]), (b, cs[-1])):
            votes.setdefault(t, {}); votes[t][c] = votes[t].get(c, 0) + 1
    return {t: max(sorted(v), key=v.get) for t, v in votes.items()}

def rings(pairs, cat, name):
    partners = {}
    for p in pairs:
        a, b = p["t"]
        partners.setdefault(a, []).append(b); partners.setdefault(b, []).append(a)
    rank = {c: i for i, c in enumerate(CAT_ORDER)}
    key = lambda t: (rank.get(cat.get(t), len(rank)), cat.get(t, ""), name[t].lower())
    return {t: sorted(ps, key=key) for t, ps in partners.items()}

def related(p, ring, slug_of, cat):
    """Up to TOTAL pair slugs: the nearest neighbours of this pair in each tool's ring, the first tool's side first.
    Within a side, a tool of the same kind as the one it replaces is shown first (HubSpot + Slack: Pipedrive + Slack)."""
    a, b = p["t"]; sides = []
    for me, other in ((a, b), (b, a)):
        r = ring[me]; i = r.index(other); near = []
        for off in OFFSETS:
            if len(near) == len(r) - 1: break
            t = r[(i + off) % len(r)]
            if t != other and t not in near: near.append(t)
        sides.append(near)
    na = min(len(sides[0]), max(PER_SIDE, TOTAL - len(sides[1])))
    nb = min(len(sides[1]), TOTAL - na)
    out = []
    for (me, other), near, k in (((a, b), sides[0], na), ((b, a), sides[1], nb)):
        out += [slug_of[frozenset((me, t))] for t in sorted(near[:k], key=lambda t: cat.get(t) != cat.get(other))]   # sorted() is stable
    return out


# ---------- pair pages ----------
REL_RE = re.compile(r'<section class="mt-12" aria-label="Related integrations">.*?</section>', re.S)
CARD = ('<a href="/stack/{slug}/" class="rounded-xl border border-slate-200 bg-white p-5 shadow-sm transition hover:-translate-y-0.5 hover:shadow-md"> '
        '<h3 class="font-semibold text-slate-900 hover:text-indigo-700"> {label} </h3> <p class="mt-1 text-xs font-medium text-slate-500"> {kind} </p> '
        '<p class="mt-2 text-sm text-slate-600">{cost} a month for 10 seats</p> </a>')   # pairfix.py and consistency.py read the kind line: keep it one word, in that <p>
API_RE = re.compile(r' <p class="mt-4 text-sm leading-relaxed text-slate-600" data-links="api">.*?</p>', re.S)
SPEC = '<section class="mt-10" aria-label="Specification matrix">'

def related_section(s, p, by_slug, picks, hubs, deg, in_crm_guide, n_pairs):
    old = REL_RE.search(s)
    assert old and len(REL_RE.findall(s)) == 1, p["slug"]
    h2 = re.search(r'<h2 class="text-xl font-bold">Integrations related to (.*?)</h2>', old.group(0))
    pair_name = h2.group(1) if h2 else esc(f'{p["v"]["na"]} + {p["v"]["nb"]}')
    lists = [link(hubs[t][1], f"all {deg[t]} {esc(hubs[t][0])} integrations") for t in p["t"] if t in hubs]
    lead = ('<p class="mt-2 text-sm leading-relaxed text-slate-600">More integrations for the same two tools, each with its connection type and what it costs a 10-person team.'
            + (f' The full {"lists" if len(lists) > 1 else "list"}: {join(lists)}.' if lists else "") + "</p>")
    cards = "".join(CARD.format(slug=q, label=esc(f'{by_slug[q]["v"]["na"]} + {by_slug[q]["v"]["nb"]}'), kind="Native" if by_slug[q]["v"]["native"] else "Middleware",
                                cost=money(by_slug[q]["v"]["N"])) for q in picks)
    also = []
    if in_crm_guide: also.append("the " + link(CRM_GUIDE, "CRM integration hidden-costs guide"))
    if "hubspot" in p["t"]: also.append("the guide to " + link(HSPRO, "which HubSpot integrations need Professional"))
    also.append("the " + link(REPORT, "Integration Tax 2026 report") + f", which adds up the hidden costs of all {n_pairs} pairs")
    foot = f'<p class="mt-4 text-sm leading-relaxed text-slate-600">{pair_name} is also covered in {join(also)}.</p>'
    new = (f'<section class="mt-12" aria-label="Related integrations"> <h2 class="text-xl font-bold">Integrations related to {pair_name}</h2> {lead} '
           f'<div class="mt-4 grid gap-4 sm:grid-cols-2 lg:grid-cols-3"> {cards} </div> {foot} </section>')
    return s[:old.start()] + new + s[old.end():]

def api_sentence(s, p, api):
    s = API_RE.sub("", s)
    links = [link(api[t][1], f"{esc(api[t][0])} API access by plan") for t in p["t"] if t in api]
    if not links: return s
    i = s.index(SPEC); j = s.index("</table> </div>", i) + len("</table> </div>")
    assert j < s.index("</section>", i), p["slug"]
    return (s[:j] + f' <p class="mt-4 text-sm leading-relaxed text-slate-600" data-links="api">API and webhook access can change with the plan you are on: see {join(links)}.</p>' + s[j:])


# ---------- homepage ----------
TOOL_CARD = '<a href="{u}" class="rounded-xl border border-slate-200 bg-white px-4 py-3 text-sm font-medium text-slate-900 shadow-sm transition hover:shadow-md hover:text-indigo-700">{t}</a>'
HOME_GRID = re.compile(r'(<section class="mt-12" id="tools" aria-label="Integration costs by tool">.*?<div class="mt-5 grid gap-3 sm:grid-cols-3">).*?(</div>)', re.S)
HOME_API = re.compile(r'<p class="mt-6 text-sm leading-relaxed text-slate-600"><strong>API &amp; webhook access by plan:</strong> .*?</p>'
                      r'|<h3 class="mt-8 font-semibold text-slate-900">API &amp; webhook access by plan</h3> <ul class="scm-index">.*?</ul>', re.S)

def homepage(s, hubs, api):
    assert len(HOME_GRID.findall(s)) == 1 and len(HOME_API.findall(s)) == 1
    s = HOME_GRID.sub(lambda m: m.group(1) + " " + " ".join(TOOL_CARD.format(u=u, t=esc(t)) for u, t in hub_links(hubs)) + " " + m.group(2), s, count=1)
    return HOME_API.sub(lambda m: '<h3 class="mt-8 font-semibold text-slate-900">API &amp; webhook access by plan</h3> ' + index_list(api_links(api)), s, count=1)


# ---------- the three hand-written pages ----------
H2_OPEN = r'<h2 class="mt-10 text-xl font-bold"(?: id="[^"]*")?>'   # ux18.py adds the id later in the build
LIST = r'(?:<p class="mt-3 leading-relaxed text-slate-600">.*?</p>|<ul class="scm-index">.*?</ul>)'
BY_TOOL = re.compile("(" + H2_OPEN + r'Integration costs by tool</h2>) ' + LIST, re.S)
BY_API = re.compile("(" + H2_OPEN + r'API &amp; webhook access by plan</h2>) ' + LIST, re.S)
RESEARCH_RE = re.compile(r' <p class="mt-6 leading-relaxed text-slate-600" data-links="research">.*?</p>', re.S)
OLD_ROW = re.compile(r'(<tr class="border-t border-slate-100"> <td class="px-4 py-3 font-medium">)([^<]+)(</td>(?:(?!</tr>).)*?) <td class="px-4 py-3"> '
                     r'<a href="(/stack/[^"/]+/)" class="font-medium text-indigo-600 hover:underline">True-cost calculator →</a> </td>( </tr>)', re.S)
OLD_HEAD = ' <th class="px-4 py-3 font-semibold">Guide</th>'

def hand_written(f, s, tool, hubs, api, n_pairs):
    # pair table: the name is the link (a row added later in the old shape is converted here too)
    s = OLD_ROW.sub(lambda m: m.group(1) + link(m.group(4), m.group(2).strip()) + m.group(3) + m.group(5), s)
    s = s.replace(OLD_HEAD, "")
    assert "True-cost calculator" not in s and '<td class="px-4 py-3 font-medium"><a href="/stack/' in s, f
    # link lists
    assert len(BY_TOOL.findall(s)) == 1 and len(BY_API.findall(s)) == 1, f
    s = BY_TOOL.sub(lambda m: m.group(1) + " " + index_list(hub_links(hubs, skip=tool)), s, count=1)
    s = BY_API.sub(lambda m: m.group(1) + " " + index_list(api_links(api)), s, count=1)
    # one sentence that leads to the other guides, after the table and its figures
    s = RESEARCH_RE.sub("", s)
    report = "the " + link(REPORT, "Integration Tax 2026 report") + f", which adds up the hidden costs of all {n_pairs} pairs in the index"
    crm = "the " + link(CRM_GUIDE, "CRM integration hidden-costs guide") + ", which sets HubSpot, Salesforce and Pipedrive side by side"
    hspro = "the guide to " + link(HSPRO, "which HubSpot integrations need Professional")
    more = {"hubspot": [crm, report], "salesforce": [crm, report], None: [hspro, report]}[tool]
    i = s.index("<h2", s.index("</table>", s.index("<main")))
    s = s[:i].rstrip(" ") + f' <p class="mt-6 leading-relaxed text-slate-600" data-links="research">Related research: {join(more)}.</p> ' + s[i:]
    # the page changed, so its structured data says so (never moves a date back)
    return re.sub(r'("dateModified":\s*")(\d{4}-\d{2}-\d{2})(")', lambda m: m.group(1) + max(m.group(2), MODIFIED) + m.group(3), s)


# ---------- footer, on every page ----------
SITE_NAV = re.compile(r'<nav aria-label="Site" class="mt-6 grid gap-6 text-sm sm:grid-cols-2">.*?</nav>', re.S)
def site_nav(n_pairs):
    li = lambda u, t: f'<li><a href="{u}" class="text-slate-600 hover:text-indigo-600">{t}</a></li>'
    col = lambda title, items: (f'<div> <p class="font-semibold text-slate-900">{title}</p> <ul class="mt-2 flex flex-col gap-2"> ' + " ".join(li(u, t) for u, t in items) + " </ul> </div>")
    guides = [("/hubspot-integrations-cost/", "HubSpot integration costs"), ("/salesforce-integrations-cost/", "Salesforce integration costs"),
              (CRM_GUIDE, "CRM integration hidden costs"), (HSPRO, "Which integrations need HubSpot Professional"),
              (REPORT, "The Integration Tax 2026 (research)"), ("/", f"All {n_pairs} integration pairs")]
    company = [("/about/", "About &amp; methodology"), ("/privacy/", "Privacy Policy"), ("/terms/", "Terms of Service"), ("mailto:admin@stackcostmatrix.com", "Contact")]
    return f'<nav aria-label="Site" class="mt-6 grid gap-6 text-sm sm:grid-cols-2"> {col("Cost guides", guides)} {col("Company", company)} </nav>'


# ---------- changelog (once) ----------
ABOUT_UL = '<ul class="mt-4 space-y-3 text-sm leading-relaxed text-slate-600"> '
HOME_UL = '<ul class="mt-5 space-y-3 text-sm leading-relaxed text-slate-600"> '
ABOUT_ENTRY = ('<li><strong class="text-slate-800">Nov 15, 2026 — Links between pages rebuilt.</strong> '
               'Every integration page now links to six related integrations that share one of its two tools, each shown with its connection type and its cost for 10 seats, '
               'and to both tools&#39; API pages from its spec table. The integrations added since Nov 12 are now linked from older pages too. '
               'Lists of tools name the page each link leads to, and the Freshdesk page is listed with the others. No prices or plan requirements changed.</li> ')
HOME_ENTRY = ('<li><strong class="text-slate-800">Nov 15, 2026</strong> — Links between pages rebuilt: every integration page now links to related integrations for both of its tools, '
              'with each one&#39;s cost for 10 seats. No prices changed.</li> ')

def changelog(s, ul, entry, mark, before):
    if mark in s:   # already there: refresh it, so a corrected wording reaches the page
        i = s.index(mark); a = s.rfind("<li>", 0, i); b = s.index("</li> ", i) + len("</li> ")
        return s[:a] + entry + s[b:]
    a = ul + before
    assert s.count(a) == 1, mark
    return s.replace(a, ul + entry + before, 1)


def main():
    pairs = load_pairs()
    for p in pairs:
        p["t"] = tuple(t["slug"] for t in p["d"]["tools"])
        assert set(p["t"]) == set(p["slug"].split("-and-")), p["slug"]
    by_slug = {p["slug"]: p for p in pairs}
    slug_of = {frozenset(p["t"]): p["slug"] for p in pairs}
    assert len(slug_of) == len(pairs)
    name = {t["slug"]: t["name"] for p in pairs for t in p["d"]["tools"]}
    deg = {t: sum(1 for p in pairs if t in p["t"]) for t in name}
    hubs = {k: (v["name"], v["url"]) for k, v in json.load(open(os.path.join(HERE, "hubs.json"), encoding="utf-8")).items()}
    api = {k: (v["name"], v["url"]) for k, v in json.load(open(os.path.join(HERE, "apipages.json"), encoding="utf-8")).items()}
    home0 = read("index.html")
    cat = tool_categories(home0)
    ring = rings(pairs, cat, name)
    crm_guide = read(CRM_GUIDE.strip("/") + "/index.html")
    picks = {p["slug"]: related(p, ring, slug_of, cat) for p in pairs}
    inbound = {p["slug"]: 0 for p in pairs}
    for src, qs in picks.items():
        assert src not in qs and len(set(qs)) == len(qs), src
        for q in qs: inbound[q] += 1
    low = {q: n for q, n in inbound.items() if n < min(3, deg[by_slug[q]["t"][0]] - 1) + min(3, deg[by_slug[q]["t"][1]] - 1)}
    assert not low, f"pairs with fewer links from other pair pages than the rings promise: {low}"

    n = 0
    for p in pairs:
        f = f'stack/{p["slug"]}/index.html'; s0 = read(f)
        s = related_section(s0, p, by_slug, picks[p["slug"]], hubs, deg, f'href="/stack/{p["slug"]}/"' in crm_guide, len(pairs))
        s = api_sentence(s, p, api)
        n += save(f, s, s0)
    for f, tool in HAND_WRITTEN.items():
        s0 = read(f); n += save(f, hand_written(f, s0, tool, hubs, api, len(pairs)), s0)
    s = homepage(home0, hubs, api)
    s = changelog(s, HOME_UL, HOME_ENTRY, "Nov 15, 2026</strong> — Links between pages rebuilt", '<li><strong class="text-slate-800">Nov 14, 2026</strong>')
    n += save("index.html", s, home0)
    s0 = read("about/index.html")
    n += save("about/index.html", changelog(s0, ABOUT_UL, ABOUT_ENTRY, "Nov 15, 2026 — Links between pages rebuilt", '<li><strong class="text-slate-800">Nov 14, 2026'), s0)
    nav = site_nav(len(pairs)); fixed = 0
    for f in sorted(set(glob.glob("*.html") + glob.glob("*/index.html") + glob.glob("stack/*/index.html"))):
        s0 = read(f)
        if not SITE_NAV.search(s0): continue
        assert len(SITE_NAV.findall(s0)) == 1, f
        fixed += save(f, SITE_NAV.sub(lambda m: nav, s0, count=1), s0)
    vals = sorted(inbound.values())
    print(f"links24: {n} pages changed, footer rewritten on {fixed} | links to a pair from other pair pages: min {vals[0]}, median {vals[len(vals) // 2]}, max {vals[-1]}")

if __name__ == "__main__":
    main()
