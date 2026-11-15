"""2026-11-15. The "How this site is made" section on the About page, asked for by the owner.

Google's guidance on AI-generated content (developers.google.com/search/docs/fundamentals/using-gen-ai-content,
"Give users context") suggests telling readers how automated content is made. This says plainly what software and AI
tools do here and what they don't decide. Keep every sentence true: if the process changes, change the text.

Idempotent: inserts the section before the methodology heading, or refreshes it if it is already there.
Run before ux18.py (it adds the jump link) and site16/agent17/security:   python3 scripts/about25.py
"""
import re

F = "about/index.html"
H2 = '<h2 class="mt-10 text-xl font-bold" data-about="made" id="how-this-site-is-made">How this site is made</h2>'
P = '<p>'
SECTION = (H2 + ' <div class="mt-4 space-y-4 leading-relaxed text-slate-600" data-about="made"> '
           + P + 'StackCostMatrix is a small, independent project, and software does much of the routine work. AI tools help read vendors&#39; '
           'pricing pages and help-centre articles, draft the text of the pages and write the scripts that build the site. The pages are generated '
           'by those scripts from one set of data, so a price corrected in one place is corrected everywhere it appears.</p> '
           + P + '<strong class="font-semibold text-slate-800">What the software doesn&#39;t decide.</strong> Every price, plan requirement and API fact '
           'comes from the vendor&#39;s own page, read on the date shown next to it, and each page links the pages it relies on so you can check them. '
           'Two exceptions are flagged wherever they apply: Pipedrive&#39;s prices come from an indexed copy of its pricing page and Make&#39;s monthly '
           'price from third-party reviews, because both sites block automated checks. Where a vendor page couldn&#39;t be read, the page says so '
           'instead of guessing. Rakesh Kumar reviews and approves every change before it&#39;s published.</p> '
           + P + 'Nothing here claims hands-on testing: the costs are what vendors publish, added up for a 10-person team. The connection diagrams are '
           'drawn from the facts on each page and labelled as diagrams.</p> </div> ')
OLD_RE = re.compile(re.escape(H2) + r' <div class="mt-4 space-y-4 leading-relaxed text-slate-600" data-about="made">.*?</div> ', re.S)
BEFORE = re.compile(r'<h2 class="mt-10 text-xl font-bold"(?: id="[^"]*")?>3-step verification methodology</h2>')

def main():
    s0 = open(F, encoding="utf-8").read()
    if OLD_RE.search(s0):
        s = OLD_RE.sub(lambda m: SECTION, s0, count=1)
    else:
        m = BEFORE.search(s0)
        assert m and len(BEFORE.findall(s0)) == 1, "methodology heading not found once on the About page"
        s = s0[:m.start()] + SECTION + s0[m.start():]
    assert s.count('data-about="made" id="how-this-site-is-made"') == 1
    if s != s0: open(F, "w", encoding="utf-8").write(s)
    print("about25: How this site is made", "updated" if s != s0 else "unchanged")

if __name__ == "__main__":
    main()
