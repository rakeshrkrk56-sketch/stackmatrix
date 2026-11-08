"""2026-11-08 round 2 (re-audit follow-ups). One-time, idempotent edits to text the generators don't manage.
Run from the repo root: python3 scripts/polish17.py   (then pairfix apply, site16, agent17, sitemap16, security)."""
import glob, json, re, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from model import compute

def rep(s, a, b, n=None):
    if a not in s: return s
    if n is not None: assert s.count(a) == n, (a[:60], s.count(a))
    return s.replace(a, b)

CDC = '<a href="https://developer.salesforce.com/docs/atlas.en-us.change_data_capture.meta/change_data_capture/cdc_intro.htm" rel="noopener" class="underline hover:text-indigo-600">Salesforce developers: Change Data Capture ↗</a> · Verified Nov 8, 2026'
SF_OLD = ('Salesforce has no native webhook primitive — sync runs via the Salesforce REST API.</span> <span class="block text-xs text-slate-500">Source: '
          '<a href="https://developer.salesforce.com/" rel="noopener" class="underline hover:text-indigo-600">Salesforce Sales Cloud API docs ↗</a> · Verified Oct 17, 2026')
SF_NEW = {
    "Professional": "Change Data Capture (Salesforce&#39;s change-event feed) isn&#39;t available on Professional, so sync runs through the REST API.</span> <span class=\"block text-xs text-slate-500\">Source: " + CDC,
    "Enterprise": "Change Data Capture (Salesforce&#39;s change-event feed) is available on Enterprise.</span> <span class=\"block text-xs text-slate-500\">Source: " + CDC,
}
BYLINE_OLD = "<span>Integration requirements and prices checked against official vendor docs · Nov 3, 2026"
BYLINE16 = {   # pairs whose requirements were re-read on Nov 8 (pairdata16)
    "activecampaign-and-stripe": "<span>Integration requirements re-checked against the vendors&#39; pages · Nov 8, 2026 (prices: Nov 3, 2026)",
    "mailchimp-and-calendly": "<span>Integration requirements re-checked against the vendors&#39; pages · Nov 8, 2026 (prices: Nov 3, 2026)",
    "pipedrive-and-xero": "<span>Integration requirements re-checked against the vendors&#39; pages · Nov 8, 2026 (prices: Nov 3, 2026",
}
n = 0
for f in sorted(glob.glob("stack/*/index.html")):
    p = f.split("/")[1]
    s = open(f, encoding="utf-8").read(); s0 = s
    d = json.loads(re.search(r'id="calc-data">(.*?)</script>', s, re.S).group(1))
    # Salesforce webhook cell: name the real feature and its edition gate instead of "no webhook primitive"
    for tier, new in SF_NEW.items():
        s = s.replace(f"('{tier}')</span> <span class=\"block text-xs text-slate-500\">" + SF_OLD, f"('{tier}')</span> <span class=\"block text-xs text-slate-500\">" + new)
    # calculator label said "native" on middleware pairs too
    s = s.replace("Minimum plan on each tool that unlocks the native integration.", "Minimum plan on each tool that this integration needs.")
    # sourcing claim: name the exceptions
    s = s.replace("Every figure on this page traces to official vendor documentation:",
                  "Every figure on this page links to its source below; prices that don&#39;t come straight from the vendor&#39;s page are flagged next to the date:")
    s = s.replace("— the minimum plans that unlock the native integration.", "— the minimum plans this integration needs.")
    s = s.replace("<li><strong>Plan prices:</strong> per-seat costs verified on official vendor pricing pages.</li>",
                  "<li><strong>Plan prices:</strong> from each vendor&#39;s pricing page; any exception is flagged next to the date at the top.</li>")
    if p in BYLINE16 and BYLINE_OLD in s:
        s = s.replace(BYLINE_OLD, BYLINE16[p], 1)
    if p == "pipedrive-and-xero" and "Make&#39;s monthly price" not in s:
        s = s.replace("(Pipedrive prices: from an indexed copy of its pricing page)", "; Pipedrive prices: from an indexed copy of its pricing page; Make&#39;s monthly price: from third-party reviews)", 1)
        s = s.replace("(prices: Nov 3, 2026; Pipedrive prices", "(prices: Nov 3, 2026; Pipedrive prices", 1)
    if s != s0: open(f, "w", encoding="utf-8").write(s); n += 1

# homepage title aimed at the "which plan does it need" intent
f = "index.html"; s = open(f, encoding="utf-8").read(); s0 = s
T_OLD, T_NEW = "SaaS Integration Costs: Which Plan Each One Needs (2026)", "Which Plan Does Each SaaS Integration Need? (2026 Costs)"
s = s.replace(f"<title>{T_OLD}</title>", f"<title>{T_NEW}</title>").replace(f'<meta property="og:title" content="{T_OLD}"', f'<meta property="og:title" content="{T_NEW}"')
s = s.replace("Every cost figure on this index traces to official vendor documentation. Pricing pages for 17 of 20 tools were re-checked on <strong>Nov 3, 2026</strong>; the rest were last audited in October 2026.",
              "Every cost figure on this index links to its source. Pricing pages for 17 of 20 tools were re-checked on <strong>Nov 3–5, 2026</strong>; Salesforce was last checked in October 2026, and Pipedrive and Make prices come from an indexed copy and third-party reviews because their pricing pages block automated checks.")
s = s.replace('<p class="text-3xl font-bold">Nov 3, 2026</p>', '<p class="text-3xl font-bold">Nov 3–5, 2026</p>')
if s != s0: open(f, "w", encoding="utf-8").write(s); n += 1
print("pages changed:", n)
