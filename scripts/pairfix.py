"""Re-render tier-dependent parts of StackCostMatrix pair pages.

Usage (run from repo root):
  python3 pairfix.py selftest   # re-render all pages from current data; must produce zero diffs
  python3 pairfix.py apply      # apply PAIRS corrections + pair copy, write files
"""
import re, json, glob, html, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from model import compute, render_tco, render_nvm, money, cheapest_api, tiers, cost as tier_cost, MAKE_MONTHLY, svg_bars, svg_flow
from pairdata import PAIRS, COPY
from pairdata2 import PAIRS2, COPY2
PAIRS.update(PAIRS2); COPY.update(COPY2)
from pairdata3 import PAIRS3, TOOL_TIERS, RENAME, COPY3_PATCH
import copy as _copy
PAIRS.update(PAIRS3)
from pairdata4 import TOOL_TIERS4, RENAME4, PAIRS4, COPY4_PATCH
TOOL_TIERS.update(TOOL_TIERS4); RENAME.update(RENAME4); PAIRS.update(PAIRS4)
from pairdata5 import TOOL_TIERS5, SUMMARY_FIXES
_MIN = {"monday": 3}
for _slug, _rows in TOOL_TIERS5.items():
    _new = []
    for _name, _base, _seat, _ann in _rows:
        _t = {"tier_name": _name, "base": _base, "perSeat": _seat, "minSeats": _MIN.get(_slug, 1), "api": None}
        if _ann is not None: _t["annualPerSeat"] = _ann
        _new.append(_t)
    TOOL_TIERS[_slug] = _new
for _p, (_a, _b) in SUMMARY_FIXES.items():
    if _p in PAIRS: assert _a in PAIRS[_p]["summary"] or _b in PAIRS[_p]["summary"], _p; PAIRS[_p]["summary"] = PAIRS[_p]["summary"].replace(_a, _b)
from pairdata6 import PAIRS6, COPY6, COPY6_PATCH, COPY6_SOURCES
PAIRS.update(PAIRS6); COPY.update(COPY6)
for _p, _lst in COPY6_PATCH.items():
    for _a, _b in _lst:
        assert _a in COPY[_p]['limits'] + COPY[_p]['how'], _p
        for _k in ('how', 'limits'): COPY[_p][_k] = COPY[_p][_k].replace(_a, _b)
for _p, _src in COPY6_SOURCES.items(): COPY[_p]['sources'] = COPY[_p]['sources'] + _src
from pairdata8 import PAIRS8
PAIRS.update(PAIRS8)
from pairdata7 import MW7, SUMMARY7, SUMMARY7_GENERIC, REQ7, COPY7, COPY7_PATCH, COPY7_SOURCES
COPY.update(COPY7)
for _p, _lst in COPY7_PATCH.items():
    for _a, _b in _lst:
        assert _a in COPY[_p]['limits'] + COPY[_p]['how'], (_p, _a[:40])
        for _k in ('how', 'limits'): COPY[_p][_k] = COPY[_p][_k].replace(_a, _b)
for _p, _src in COPY7_SOURCES.items(): COPY[_p]['sources'] = COPY[_p]['sources'] + _src
from pairdata9 import PAIRS9, COPY9, COPY9_EXTRA_SOURCES
from pairdata10 import PAIRS10, COPY10
PAIRS.update(PAIRS10); COPY.update(COPY10)
from pairdata11 import PAIRS11, COPY11
PAIRS.update(PAIRS11); COPY.update(COPY11)
from pairdata12 import TOP12
for _p, _t in TOP12.items():
    _c = COPY.setdefault(_p, dict(how="", limits="", sources=[]))
    for _k in ("how", "limits", "sources"):
        if _k in _t: _c[_k] = _t[_k]
    _c["answer"], _c["setup"], _c["top"] = _t["answer"], _t["setup"], True
    if "summary" in _t:
        assert _p in PAIRS, _p
        PAIRS[_p] = dict(PAIRS[_p], summary=_t["summary"])
from pairdata14 import TOOL_TIERS14
TOOL_TIERS.update(TOOL_TIERS14)
from pairdata13 import PAIRS13, COPY13, NEW13
# 2026-11-04: Pipedrive + Mailchimp. Pipedrive's Marketplace lists "Mailchimp by Pipedrive" as FREE and neither vendor
# names a Mailchimp plan (Pipedrive: "The number of audiences you can create depends on your Mailchimp plan").
PAIRS["pipedrive-and-mailchimp"] = dict(PAIRS["pipedrive-and-mailchimp"], req=dict(PAIRS["pipedrive-and-mailchimp"]["req"], mailchimp="Free"),
    summary="Pipedrive's own Mailchimp sync app is free and keeps contacts in step both ways: Pipedrive filters push contacts into a Mailchimp audience, and Mailchimp segments or tags bring contacts into Pipedrive. Neither vendor names a Mailchimp plan for it. Requires Pipedrive on the 'Lite' plan and Mailchimp on the 'Free' plan.")
PAIRS.update(PAIRS13); COPY.update(COPY13)
for _p, _c in NEW13.items():
    if _c["mw"]: MW7[_p] = tuple(_c["mw"])
PAIRS.update(PAIRS9); COPY.update(COPY9)
for _p, _src in COPY9_EXTRA_SOURCES.items():
    if _p in COPY: COPY[_p]['sources'] = COPY[_p]['sources'] + [x for x in _src if x not in COPY[_p]['sources']]
for _p, (_a, _b) in COPY4_PATCH.items():
    for _k in ('how', 'limits'):
        COPY[_p][_k] = COPY[_p][_k].replace(_a, _b)
    assert _b in COPY[_p]['how'] + COPY[_p]['limits'], _p
for _p, (_a, _b) in COPY3_PATCH.items():
    for _k in ('how', 'limits'):
        COPY[_p][_k] = COPY[_p][_k].replace(_a, _b)
    assert _b in COPY[_p]['how'] + COPY[_p]['limits'], _p
from pairdata15 import TOOL_TIERS15, SUMMARY15, HS_CHECKED
TOOL_TIERS.update(TOOL_TIERS15)
for _p, _s in SUMMARY15.items():
    PAIRS[_p] = dict(PAIRS[_p], summary=_s)
from pairdata16 import PAIRS16, COPY16, MW16
PAIRS.update(PAIRS16)
# Airtable and Calendly only post notifications into Slack (support.airtable.com, calendly.com/help/calendly-slack)
PAIRS["slack-and-airtable"] = dict(PAIRS["slack-and-airtable"], sync="1-way (Airtable → Slack)")
PAIRS["slack-and-calendly"] = dict(PAIRS["slack-and-calendly"], sync="1-way (Calendly → Slack)")
for _p, _c in COPY16.items():
    assert not (COPY.get(_p) or {}).get("how"), _p   # round 16 only fills pairs that had no copy
    COPY[_p] = _c
MW7.update(MW16)
from pairdata18 import PATCH18
for _p, _t in PATCH18.items():
    _c = dict(COPY[_p])
    for _k, _v in _t.items():
        if _k == "extra_sources": _c["sources"] = list(_c["sources"]) + [x for x in _v if x not in _c["sources"]]
        else: _c[_k] = _v
    COPY[_p] = _c
# 2026-11-10: numbered setup steps for 19 more native pairs, each from the vendor's setup guide (pairdata19)
from pairdata19 import SETUP19, SETUP19_CHECKED, RECHECK19, STEP_FIX19
for _p, _t in SETUP19.items():
    _c = dict(COPY[_p])
    assert not _c.get("setup"), _p   # only pairs that had no steps
    _c.update(setup=_t["setup"], setup_src=_t["setup_src"], setup_checked=SETUP19_CHECKED)
    _c["sources"] = list(_c["sources"]) + [x for x in _t.get("extra_sources", []) if x not in _c["sources"]]
    COPY[_p] = _c
for _p, _src in RECHECK19.items():   # older step lists, compared with the guide again on the same day
    _c = dict(COPY[_p]); _steps = list(_c["setup"])
    for _i, _x in STEP_FIX19.get(_p, {}).items(): _steps[_i] = _x
    _c.update(setup=_steps, setup_src=_src, setup_checked=SETUP19_CHECKED)
    COPY[_p] = _c
STEPS_DATE = "2026-11-10"   # pages whose setup steps were written or re-read that day carry it as dateModified
MODIFIED = {_p: STEPS_DATE for _p in list(SETUP19) + list(RECHECK19)}
FACTS16 = {("activecampaign", "Plus"): ("Yes", "Yes")}   # apidata: API and webhooks on every ActiveCampaign plan

FACTS_EXTRA = {("salesforce", "Enterprise"): ("Yes", "Yes"), ("slack", "Free"): ("Yes", "Yes"),
               ("clickup", "Free"): ("Yes", "No"),    # API on all plans (ClickUp); webhook value copied from Unlimited
               ("airtable", "Free"): ("Yes", "Yes"), ("airtable", "Team"): ("Yes", "Yes"), ("quickbooks", "Simple Start"): ("Yes", "Yes"),  # Airtable webhooks: "Billing plans: All plans"
               ("calendly", "Free"): ("Yes", "No"),   # API on any plan; webhooks need paid Standard+
               ("mailchimp", "Free"): ("Yes", "No")}  # webhook value copied from Essentials
SHORT = {"Salesforce Sales Cloud": "Salesforce", "QuickBooks Online": "QuickBooks"}
TODAY = "2026-11-03"
ROUND_DATE = "2026-11-11"  # last change to every pair page (Nov 11: connection diagram; Nov 8: trap text, FAQ, descriptions)

def esc(s):  # matches the site's escaping of summaries/FAQ text
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("'", "&#39;")

def read(f): return open(f, encoding="utf-8").read()

def sub1(pat, repl, s, flags=re.S, what=""):
    new, n = re.subn(pat, repl, s, count=1, flags=flags)
    assert n == 1, f"pattern not found: {what or pat[:80]}"
    return new

def calc_data(s):
    return json.loads(re.search(r'<script type="application/json" id="calc-data">(.*?)</script>', s, re.S).group(1))

def tco_b(v): return v["native"] and v["MP"] < v["N"]  # was: and UP >= 100 (contradicted the native-vs-middleware section)
def nvm_b(v): return v["MP"] < v["N"]

def build_facts():
    facts = dict(FACTS_EXTRA); facts.update(FACTS16)
    for f in glob.glob("stack/*/index.html"):
        s = read(f); d = calc_data(s)
        for row, idx in (("API access at required tier", 0), ("Webhook support at required tier", 1)):
            m = re.search(row + r'</td> <td class="px-4 py-3">(.*?)</td> <td class="px-4 py-3">(.*?)</td> </tr>', s, re.S)
            for t, cell in zip(d["tools"], (m.group(1), m.group(2))):
                yn = re.match(r"\s*(Yes|No)", cell).group(1)
                cur = list(facts.get((t["slug"], t["required"]), ("?", "?"))); cur[idx] = yn
                facts[(t["slug"], t["required"])] = tuple(cur)
    for slug, ren in RENAME.items():
        for old, new in ren.items():
            if (slug, old) in facts: facts.setdefault((slug, new), facts[(slug, old)])
    if ("xero", "Growing") in facts: facts.setdefault(("xero", "Established"), facts[("xero", "Growing")])
    return facts

CONNECTOR = {10.59: "Make Core", 29.99: "Zapier Professional", 15: "Data Mapper for Mailchimp"}
def m0(x): return money(x).replace(".00", "")

def upgrades(d):
    """[(tool name, required tier, cheapest API tier, extra $/mo)] for each tool forced above its cheapest API plan."""
    out = []
    for t in d["tools"]:
        req = next(u for u in tiers(t) if u["tier_name"] == t["required"]); ch = cheapest_api(t)
        if ch and tier_cost(req, t["slug"]) > tier_cost(ch, t["slug"]) + 0.004:
            out.append((t["name"], t["required"], ch["tier_name"], tier_cost(req, t["slug"]) - tier_cost(ch, t["slug"])))
    return out

def trap_label(v):
    return "Hidden Cost Trap" if (not v["native"] or v["UP"] > 0.004) else "Plan requirements"

def trap_text(v, d):
    """The trap box's own sentence: the specific extra cost, instead of repeating the lede."""
    A, B = v["na"], v["nb"]
    ups = upgrades(d)
    upt = "; ".join(f"{n} needs '{req}', {m0(x)}/mo more than '{ch}', its cheapest plan with API access" for n, req, ch, x in ups)
    if not v["native"]:
        conn = CONNECTOR.get(v["mw"], "a connector")
        out = f"The hidden cost here is the connector: there's no native {A} + {B} app, so you pay for {conn} ({m0(v['mw'])}/mo) on top of both tools."
        if ups: out += f" On top of that, {upt}."
    elif ups:
        out = f"The hidden cost is a forced plan upgrade: {upt}. That adds {m0(v['UP'])}/mo for 10 seats just to connect the two tools."
        if v["MP"] < v["N"]: out += f" Running the same connection through Make on the cheapest API plans would cost about {m0(v['MP'])}/mo in total instead of {m0(v['N'])}/mo, but you'd give up the native connector."
    else:
        out = f"No hidden cost: the native connector works on {A} '{v['ta']}' and {B} '{v['tb']}', so connecting them adds nothing to what you already pay for the two tools."
    if any(t["slug"] == "stripe" for t in d["tools"]):
        out += " Stripe has no monthly plan fee; it charges per transaction, so it counts as $0/month here."
    return out

TH_ = '<th class="px-4 py-3 font-semibold">'; TD_ = '<td class="px-4 py-3">'
def nvm_table(v, d, sync="2-way"):
    """Native (or modeled connector) route vs the connector alternatives, at 10 seats."""
    A, B = v["na"], v["nb"]
    ch = [cheapest_api(t)["tier_name"] for t in d["tools"]]
    rows = []
    if v["native"]:
        chp = f"{html.escape(A)} &#39;{ch[0]}&#39; + {html.escape(B)} &#39;{ch[1]}&#39;"
        rows.append((f"Native {html.escape(A)} + {html.escape(B)} connector", f"{html.escape(A)} &#39;{v['ta']}&#39; + {html.escape(B)} &#39;{v['tb']}&#39;", money(v["N"]), sync))
        rows.append(("Make Core on the cheapest API plans", chp + " + Make", money(v["MP"]), "1-way per scenario"))
        rows.append(("Zapier Professional on the cheapest API plans", chp + " + Zapier", money(v["MP"] - MAKE_MONTHLY + 29.99), "1-way per Zap"))
    else:
        conn = CONNECTOR.get(v["mw"], "Connector")
        alt, altfee = ("Zapier Professional", 29.99) if v["mw"] != 29.99 else ("Make Core", MAKE_MONTHLY)
        plans = f"{html.escape(A)} &#39;{v['ta']}&#39; + {html.escape(B)} &#39;{v['tb']}&#39;"
        rows.append((f"{conn} (modeled here)", plans, money(v["N"]), "1-way per automation"))
        rows.append((f"{alt} instead", plans, money(v["N"] - v["mw"] + altfee), "1-way per automation"))
    body = "".join(f'<tr class="border-t border-slate-100"> <td class="px-4 py-3 font-medium">{r[0]}</td> {TD_}{r[1]}</td> {TD_}{r[2]}</td> {TD_}{r[3]}</td> </tr>' for r in rows)
    cols = ["#4f46e5", "#0e7490", "#b45309"]
    short = (["Native connector", "Make Core route", "Zapier Professional route"] if v["native"] else [html.unescape(re.sub(r"<[^>]+>", "", r[0])) for r in rows])
    chart = (' <figure class="mt-5"> ' + svg_bars([(short[i], float(r[2].replace("$", "").replace(",", "")), cols[i]) for i, r in enumerate(rows)],
                                                    f"{A} + {B}: monthly cost for 10 seats by route")
             + f' <figcaption class="mt-1 text-xs text-slate-500">Monthly cost for 10 seats by route, {html.escape(A)} + {html.escape(B)}.</figcaption> </figure>')
    return (chart + ' <div class="mt-4 overflow-x-auto rounded-xl border border-slate-200"> <table class="spec-matrix w-full text-sm"> '
            '<caption class="sr-only">Integration routes compared for a 10-seat team</caption> <thead class="bg-slate-50"> <tr class="text-left"> '
            f'{TH_}Route</th> {TH_}Plans</th> {TH_}10 seats / month</th> {TH_}Sync</th> </tr> </thead> <tbody> {body} </tbody> </table> </div> '
            '<p class="mt-2 text-xs text-slate-500">Connector prices are monthly-billing list prices: Zapier Professional $29.99 (zapier.com/pricing) and Make Core $10.59 '
            '(from third-party pricing reviews, because make.com blocks automated checks). Both bill by usage, so high volumes cost more.</p> ')

def meta_desc(v, d=None):
    A, B, ta, tb = v["na"], v["nb"], v["ta"], v["tb"]
    cost = money(v["N"]).replace(".00", "")
    mw = money(v["mw"]).replace(".00", "")
    up = m0(v["UP"])
    for nA, nB in ((A, B), (SHORT.get(A, A), SHORT.get(B, B))):
        if not v["native"]:
            fact = f"no native app, so the {CONNECTOR.get(v['mw'], 'connector')} fee is the extra cost."
            opts = [f"{nA} + {nB} runs via middleware (+{mw}/mo) on {nA} {ta} and {nB} {tb}: {cost}/mo for 10 seats; {fact}",
                    f"{nA} + {nB} runs via middleware (+{mw}/mo) on {nA} {ta} and {nB} {tb}: {cost}/mo for 10 seats."]
        elif v["UP"] > 0.004:
            opts = [f"{nA} + {nB} needs {nA} {ta} and {nB} {tb} for the native integration: {cost}/mo for 10 seats, including a +{up}/mo forced upgrade.",
                    f"{nA} + {nB} needs {nA} {ta} and {nB} {tb}: {cost}/mo for 10 seats, including a +{up}/mo forced upgrade."]
        else:
            opts = [f"{nA} + {nB} needs {nA} {ta} and {nB} {tb} for the native integration: {cost}/mo for 10 seats, with no extra cost to connect them.",
                    f"{nA} + {nB} needs {nA} {ta} and {nB} {tb}: {cost}/mo for 10 seats, with no extra cost to connect them."]
        out = next((o for o in opts if len(o) <= 155), None)
        if out: return out
    raise ValueError("no description fits")

def meta_desc_top(v):
    A, B, ta, tb = v["na"], v["nb"], v["ta"], v["tb"]
    cost = money(v["N"]).replace(".00", "")
    for nA, nB in ((A, B), (SHORT.get(A, A), SHORT.get(B, B))):
        for o in (f"How the {nA} + {nB} integration works, how to set it up, and the plans it needs: {nA} {ta} + {nB} {tb}, {cost}/mo for 10 seats.",
                  f"How the {nA} + {nB} integration works and how to set it up, plus the plans it needs and the 10-seat cost ({cost}/mo).",
                  f"How the {nA} + {nB} integration works, setup steps and the 10-seat cost ({cost}/mo)."):
            if len(o) <= 155: return o
    raise ValueError("no top description fits")

def faq_answers(v, d):
    A, B, ta, tb = v["na"], v["nb"], v["ta"], v["tb"]
    ups = upgrades(d)
    why = (" " + " ".join(f"{n}'s cheapest plan with API access is '{ch}', so '{req}' is a {m0(x)}/mo upgrade at 10 seats." for n, req, ch, x in ups)) if ups else f" Those are each tool's cheapest plan with API access ({A} '{ta}' at {m0(v['ca'])}/mo and {B} '{tb}' at {m0(v['cb'])}/mo for 10 seats), so the integration doesn't force an upgrade."
    q3 = f"Is the {A} + {B} integration native, and would Make or Zapier be cheaper?" if v["native"] else f"Why does {A} + {B} need middleware, and what does it cost?"
    if v["native"]:
        alt = (f" Connecting through Make on the cheapest API plans would cost about {money(v['MP'])}/month in total instead of {money(v['N'])}, but you'd replace the native connector with a third-party automation."
               if v["MP"] < v["N"] else f" Make would cost about {money(v['MP'])}/month on the cheapest API plans, more than the native route, so it only makes sense if you already use it.")
        return (f"To unlock the native integration, {A} must be on the '{ta}' plan or higher and {B} must be on the '{tb}' plan or higher." + why,
                f"At 10 seats with the required tiers ({A} '{ta}' + {B} '{tb}'), the stack costs {money(v['N'])} per month.",
                f"The {A} + {B} connection is native — no third-party middleware subscription is required." + alt, q3)
    conn = CONNECTOR.get(v["mw"], "a connector")
    return (f"To unlock the integration, {A} must be on the '{ta}' plan or higher and {B} must be on the '{tb}' plan or higher." + why,
            f"At 10 seats with the required tiers ({A} '{ta}' + {B} '{tb}' + {money(v['mw'])}/month middleware), the stack costs {money(v['N'])} per month.",
            f"The {A} + {B} connection runs through middleware: neither vendor offers a native app for this pair, so this page models {conn} at {money(v['mw'])} per month on top of both tools. Sync is one-way (a trigger in one tool runs an action in the other).", q3)

def pair_figure(v, d, pair):
    """The pair's summary card (og17.py) shown in the page, so the numbers are also available as an image."""
    extra = (v["mw"] + max(0.0, v["UP"] - v["mw"])) if not v["native"] else v["UP"]
    alt = (f"{v['na']} + {v['nb']} integration cost summary: {m0(v['N'])} a month for 10 seats, "
           + (f"{m0(extra)} of it is the hidden cost to connect" if extra > 0.004 else "nothing extra to connect")
           + f"; plans needed: {v['na']} {v['ta']} and {v['nb']} {v['tb']}")
    return (f'<figure class="mt-6"> <img src="/og/{pair}.jpg" width="1200" height="630" loading="lazy" class="scm-fig" alt="{html.escape(alt, quote=True)}"> '
            f'<figcaption class="mt-2 text-xs text-slate-500">{html.escape(v["na"])} + {html.escape(v["nb"])} at a glance. Free to reuse with credit (CC BY 4.0).</figcaption> </figure> ')

from pairdata20 import FLOW20, VIA20
def flow_figure(v, d, pair, sync):
    """The connection diagram under "How it works": which tool sends what to which, through what, on which plans."""
    A, B = d["tools"]; names = {A["slug"]: v["na"], B["slug"]: v["nb"]}; sync = html.unescape(sync)
    def detail(t, tier, c):
        plan = "Professional + API add-on" if t["slug"] == "salesforce" and tier == "Professional" else f"{tier} plan"
        return f"{plan} · {m0(c)}/mo for 10 seats"
    box = {A["slug"]: (v["na"], detail(A, v["ta"], v["ca"])), B["slug"]: (v["nb"], detail(B, v["tb"], v["cb"]))}
    one_way = re.match(r"1-way \((.+?) → (.+?)\)$", sync)   # e.g. "1-way (Stripe → Slack)"
    def check(src, dst):   # an arrow must not contradict the page's sync cell
        if one_way and one_way.group(1) != "trigger":
            want = (one_way.group(1).lower(), one_way.group(2).lower())
            got = (names[src].lower(), names[dst].lower())
            assert got[0].startswith(want[0].split()[0]) and got[1].startswith(want[1].split()[0]), (pair, sync, src, dst)
    if v["native"]:
        flows = FLOW20[pair]
        for fl in flows:
            if fl[0] == "both": assert sync.startswith("2-way"), (pair, sync)
            else: assert fl[0] in box and fl[1] in box, (pair, fl); check(fl[0], fl[1])
        srcs = {fl[0] for fl in flows}
        top = flows[0][0] if len(srcs) == 1 and "both" not in srcs else A["slug"]   # one direction: the sender goes on top
        bot = B["slug"] if top == A["slug"] else A["slug"]
        rows = [("both" if fl[0] == "both" else "down" if fl[0] == top else "up", fl[-1]) for fl in flows]
        short = sync.split(" (")[0]
        link = f"Native app · {short} · no connector fee"
        said = " ".join((f"Both ways: {fl[1]}." if fl[0] == "both" else f"{names[fl[0]]} to {names[fl[1]]}: {fl[2]}.") for fl in flows)
        label = (f"Diagram of how {v['na']} and {v['nb']} connect. {box[top][0]}: {box[top][1]}. {box[bot][0]}: {box[bot][1]}. {said} {link.replace(' · ', ', ')}.")
        svg = svg_flow(box[top], box[bot], label, flows=rows, link=link)
        how = "a native app"
    else:
        via = VIA20[pair]; conn = CONNECTOR.get(d["middleware"], "Middleware"); fee = f"{money(d['middleware'])}/mo"
        mid = (conn, f"connector · {fee} · runs the automation")
        if via and via[-1] == "sync":   # a sync app in the middle: no trigger/action wording
            top = via[0]; assert top in box, (pair, via); bot = B["slug"] if top == A["slug"] else A["slug"]; check(top, bot)
            mid = (conn, f"connector app · {fee}")
            segs = (via[1], via[2], "down")
            said = f"{conn} ({fee}) copies {via[1]} from {names[top]} into {names[bot]} as {via[2]}. Data flows one way."
        elif via:
            top = via[0]; assert top in box, (pair, via); bot = B["slug"] if top == A["slug"] else A["slug"]; check(top, bot)
            segs = (f"trigger: {via[1]}", f"action: {via[2]}", "down")
            said = f"{names[top]} sends a trigger ({via[1]}) to {conn} ({fee}), which performs an action in {names[bot]} ({via[2]}). Each automation runs one way."
        else:
            top, bot = A["slug"], B["slug"]
            segs = ("a trigger in one tool", "an action in the other", "both")
            said = f"{conn} ({fee}) watches for a trigger in one tool and performs an action in the other. Each automation runs one way."
        label = f"Diagram of how {v['na']} and {v['nb']} connect. {box[top][0]}: {box[top][1]}. {box[bot][0]}: {box[bot][1]}. {said}"
        svg = svg_flow(box[top], box[bot], label, mid=mid, segs=segs, hue="#0e7490")
        how = f"through {conn}" + (", shown with the example automation described above" if via and via[-1] != "sync" else "")
    return (f'<figure class="mt-6"> {svg} <figcaption class="mt-2 text-xs text-slate-500">Diagram: how {html.escape(v["na"])} and {html.escape(v["nb"])} connect, {html.escape(how)}. '
            f'Drawn from the facts on this page.</figcaption> </figure> ')

def setup_led(v, copy):
    """Pages whose searchers want "how do I connect these": the reworked top pages and every native pair with no extra cost."""
    return bool((copy or {}).get("top")) or (v["native"] and v["UP"] <= 0.004)

def sf_addon_note(v, d):
    """Salesforce Professional's line bundles the API add-on; say so next to the total."""
    for t, c in zip(d["tools"], (v["ca"], v["cb"])):
        if t["slug"] == "salesforce" and t["required"] == "Professional":
            seat = next(x["perSeat"] for x in t["tiers"] if x["tier_name"] == "Professional")
            return (f"Salesforce&#39;s {money(c)} is the Professional plan (${seat:g}/user) plus the API add-on, which Salesforce sells through an account executive; "
                    f"this page models it at $25/user (${25 * 10} at 10 seats). ")
    return ""

def trap_tail(v, pair, cta=True):
    end = "  </section>  "
    if not v["native"] and not cta:
        return '</p> ' + end
    if not v["native"]:
        return (f'</p>   <a href="/go/make" target="_blank" rel="sponsored noopener" data-cta="tool" data-tool="make" data-pair="{pair}" class="mt-5 block rounded-xl bg-emerald-700 px-6 py-4 text-center font-bold text-white shadow-md ring-2 ring-emerald-300 transition hover:bg-emerald-800"> Connect {v["na"]} + {v["nb"]} via Make.com — the middleware this integration runs on </a> <p class="mt-2 text-center text-xs text-amber-800">\nAffiliate link — we may earn a commission at no extra cost to you.\n</p>' + end)
    if tco_b(v):
        return (f'</p>   <a href="/go/make" target="_blank" rel="sponsored noopener" data-cta="tool" data-tool="make" data-pair="{pair}" class="mt-5 block rounded-xl bg-emerald-700 px-6 py-4 text-center font-bold text-white shadow-md ring-2 ring-emerald-300 transition hover:bg-emerald-800"> Skip the native tier upgrade: connect {v["na"]} + {v["nb"]} via Make.com middleware instead </a> <p class="mt-2 text-center text-xs text-amber-800">\nAffiliate link — we may earn a commission at no extra cost to you.\n</p>' + end)
    return '</p> ' + end   # the green "native is the cheapest path" box repeated the sentence above it; removed 2026-11-10

def render_page(s, pair, d, summary, sync, facts, date_modified=None, copy=None, cta=True):
    v = compute(d)
    A, B, ta, tb = v["na"], v["nb"], v["ta"], v["tb"]
    sync2 = sync == "2-way"
    # title + H1 by search intent (hand-tuned "top" pages keep their title); the WebPage name follows the H1
    cur_title = html.unescape(re.search(r"<title>(.*?)</title>", s, re.S).group(1)).strip()
    a_, b_ = SHORT.get(A, A), SHORT.get(B, B)
    if (copy or {}).get("top"):
        title, h1 = cur_title, html.unescape(re.sub(r"\s+", " ", re.search(r"<h1[^>]*>(.*?)</h1>", s, re.S).group(1))).strip()
    elif setup_led(v, copy):
        title = next(t for t in (f"{a_} + {b_} Integration: Setup, Plans & Cost (2026)", f"{a_} + {b_} Integration: Setup & Cost (2026)", f"{a_} + {b_} Integration (2026)") if len(t) <= 60)
        h1 = f"{A} + {B} Integration (2026): How It Works, Setup & True Cost"
    else:
        title = next(t for t in (f"{a_} + {b_} Integration Cost (2026): Plans & Setup", f"{a_} + {b_} Integration Cost (2026)") if len(t) <= 60)
        h1 = f"{A} + {B} Integration Cost (2026): True Price, Minimum Plan & Hidden API Fees"
    s = sub1(r"(<title>).*?(</title>)", lambda m: m.group(1) + html.escape(title, quote=False) + m.group(2), s, what="title")
    s = sub1(r'(<meta property="og:title" content=")[^"]*(")', lambda m: m.group(1) + html.escape(title, quote=True) + m.group(2), s, what="og:title")
    s = sub1(r'(<h1 class="text-3xl font-bold tracking-tight sm:text-4xl">).*?(</h1>)', lambda m: m.group(1) + html.escape(h1, quote=False) + m.group(2), s, what="h1")
    # calc data
    s = sub1(r'(<script type="application/json" id="calc-data">).*?(</script>)', lambda m: m.group(1) + json.dumps(d, separators=(",", ":"), ensure_ascii=False) + m.group(2), s, what="calc-data")
    # lede + trap summary
    s = sub1(r'(<p class="mt-4 max-w-3xl text-lg leading-relaxed text-slate-700">).*?(</p>)', lambda m: m.group(1) + " " + esc(summary) + " " + m.group(2), s, what="lede")
    # calculator pre-render
    cells = {"calc-line-a-tier": f"{ta} (required)", "calc-line-a-cost": money(v["ca"]), "calc-line-b-tier": f"{tb} (required)", "calc-line-b-cost": money(v["cb"]),
             "calc-line-m-note": d["middlewareLabel"], "calc-line-m-cost": money(v["mw"]), "calc-total": money(v["N"]), "calc-incr": money(v["N"]),
             "calc-year1": money(v["N"] * 12), "calc-tco3": money(v["N"] * 36)}
    for k, val in cells.items():
        s = sub1(r'(id="' + k + r'"(?: for="[^"]*")?>)[^<]*(<)', lambda m, val=val: m.group(1) + val + m.group(2), s, what=k)
    s = re.sub(r' <p class="mt-2 text-xs text-slate-500" data-sf-addon="1">.*?</p>', "", s, flags=re.S)
    if any(t["slug"] == "salesforce" and t["required"] == "Professional" for t in d["tools"]):
        note = (' <p class="mt-2 text-xs text-slate-500" data-sf-addon="1">The Salesforce line is the Professional plan plus the API add-on, modeled at $25 per user a month; '
                'ask Salesforce whether your connector needs it (<a href="/salesforce-api-access/" class="underline hover:text-indigo-600">Salesforce API access by edition</a>).</p>')
        s = sub1(r'(id="calc-line-h-cost">[^<]*</td> </tr> </tbody> </table> </div>)', lambda m: m.group(1) + note, s, what="sf addon note")
    # TCO summary + native vs middleware
    s = sub1(r'(aria-label="Default 10-seat TCO summary">.*?<p class="mt-2 text-sm leading-relaxed text-indigo-950">).*?(</p> </aside>)', lambda m: m.group(1) + render_tco(v, tco_b) + sf_addon_note(v, d) + m.group(2), s, what="tco")
    s = sub1(r'(aria-label="Native versus middleware"> <h2 class="text-xl font-bold">.*?</h2>).*?(</section>)', lambda m: m.group(1) + render_nvm(v, nvm_b, sync2) + nvm_table(v, d, sync) + pair_figure(v, d, pair) + m.group(2), s, what="nvm")
    # verified facts
    s = sub1(r"(<li><strong>Required tiers:</strong> ).*?( — the minimum plans)", lambda m: m.group(1) + f"'{ta}' / '{tb}'" + m.group(2), s, what="facts")
    s = sub1(r"(<li><strong>Native app availability:</strong>).*?(</li>)", lambda m: m.group(1) + (" Native app available in vendor marketplace." if v["native"] else " No native app — connected via middleware.") + m.group(2), s, what="avail")
    # hidden cost trap
    req = f"Requires {A} on the &#39;{ta}&#39; plan or higher — Requires {B} on the &#39;{tb}&#39; plan or higher" + ("." if v["native"] else f" — Plus {money(v['mw'])}/month middleware on top of both tools.")
    s = sub1(r'(aria-label="Hidden Cost Trap">.*?<p class="mt-3 font-medium text-amber-950">).*?(</p>)', lambda m: m.group(1) + req + m.group(2), s, what="requires")
    for name, tier in ((A, ta), (B, tb)):
        s = sub1(r'(<dt class="text-sm text-amber-800">' + re.escape(name) + r' minimum tier</dt> <dd class="text-lg font-bold text-amber-950">).*?(</dd>)', lambda m, tier=tier: m.group(1) + f"'{tier}'" + m.group(2), s, what="dd " + name)
    s = sub1(r'(<dt class="text-sm text-amber-800">Middleware fee</dt> <dd class="text-lg font-bold text-amber-950">).*?(</dd>)', lambda m: m.group(1) + (" None " if v["native"] else f" {money(v['mw'])}/mo ") + m.group(2), s, what="fee")
    s = sub1(r'(aria-label="Hidden Cost Trap"> <h2 class="flex items-center gap-2 text-xl font-bold text-amber-900"> <span[^>]*>!</span>\n)[^<\n]*(\n</h2>)', lambda m: m.group(1) + trap_label(v) + m.group(2), s, what="trap label")
    s = sub1(r'(<p class="mt-4 text-sm leading-relaxed text-amber-900">).*?(<section class="mt-10" aria-label="Specification matrix">)', lambda m: m.group(1) + esc(trap_text(v, d)) + trap_tail(v, pair, cta) + m.group(2), s, what="trap tail")
    # spec matrix
    badge = ('<span class="inline-block rounded-full px-2.5 py-0.5 text-xs font-medium ring-1 bg-emerald-100 text-emerald-800 ring-emerald-200"> Native </span>' if v["native"]
             else '<span class="inline-block rounded-full px-2.5 py-0.5 text-xs font-medium ring-1 bg-sky-100 text-sky-800 ring-sky-200"> Middleware </span>')
    s = sub1(r'(Connection type</td> <td class="px-4 py-3" colspan="2"> )<span class="inline-block[^>]*>[^<]*</span>', lambda m: m.group(1) + badge, s, what="badge")
    s = sub1(r'(Data sync direction</td> <td class="px-4 py-3" colspan="2">).*?(</td>)', lambda m: m.group(1) + sync + m.group(2), s, what="sync")
    s = sub1(r'(Native integration supported</td> <td class="px-4 py-3" colspan="2">).*?(</td>)', lambda m: m.group(1) + (" Yes — official native app/connector " if v["native"] else " No — requires middleware (Zapier / Make) ") + m.group(2), s, what="native row")
    for row, idx in (("API access at required tier", 0), ("Webhook support at required tier", 1)):
        def cellfix(m):
            out = [m.group(1)]
            for tool, cell, tier in ((d["tools"][0], m.group(2), ta), (d["tools"][1], m.group(4), tb)):
                yn = facts[(tool["slug"], tier)][idx]
                assert yn in ("Yes", "No"), (pair, tool["slug"], tier)
                out.append(re.sub(r"^\s*(Yes|No) <span class=\"text-slate-500\"> \('[^']*'\)", f" {yn} <span class=\"text-slate-500\"> ('{tier}')", cell))
                out.append(m.group(3) if tool is d["tools"][0] else m.group(5))
            return "".join(out)
        s = sub1(r'(' + row + r'</td> <td class="px-4 py-3">)(.*?)(</td> <td class="px-4 py-3">)(.*?)(</td> </tr>)', cellfix, s, what=row)
    # FAQ (visible + JSON-LD)
    q1, q2, q3, q3q = faq_answers(v, d)
    blocks = re.findall(r'(<div> <h3 class="font-semibold text-slate-900">)([^<]*)(</h3> <p class="mt-1 leading-relaxed text-slate-700">)(.*?)(</p> </div>)', s, re.S)
    assert len(blocks) == 4, pair
    for i, ((h, q, mid, old, post), new) in enumerate(zip(blocks[:3], (q1, q2, q3))):
        s = s.replace(h + q + mid + old + post, h + (esc(q3q) if i == 2 else q) + mid + esc(new) + post, 1)
    q4q, q4 = (f"What are the limitations of the {A} + {B} integration?", copy["limits"]) if (copy or {}).get("limits") else (None, None)
    if q4q:
        h, q, mid, old, post = blocks[3]
        s = s.replace(h + q + mid + old + post, h + esc(q4q) + mid + esc(q4) + post, 1)
    def faqfix(m):
        o = json.loads(m.group(1))
        if o.get("@type") == "FAQPage":
            for q, new in zip(o["mainEntity"][:3], (q1, q2, q3)): q["acceptedAnswer"]["text"] = new
            o["mainEntity"][2]["name"] = q3q
            if q4q: o["mainEntity"][3]["name"] = q4q; o["mainEntity"][3]["acceptedAnswer"]["text"] = q4
        if o.get("@type") == "WebPage":
            o["name"] = h1
            o["description"] = meta_desc_top(v) if setup_led(v, copy) else meta_desc(v, d)
            if date_modified: o["dateModified"] = date_modified
        return '<script type="application/ld+json">' + json.dumps(o, ensure_ascii=False, separators=(",", ":")) + "</script>"
    s = re.sub(r'<script type="application/ld\+json">(.*?)</script>', faqfix, s, flags=re.S)
    # meta + og descriptions
    md = html.escape(meta_desc_top(v) if setup_led(v, copy) else meta_desc(v, d), quote=True)
    s = sub1(r'(<meta name="description" content=")[^"]*(")', lambda m: m.group(1) + md + m.group(2), s, what="meta")
    s = sub1(r'(<meta property="og:description" content=")[^"]*(")', lambda m: m.group(1) + md + m.group(2), s, what="og")
    # pair-specific copy section, above the calculator: answer, how it works, numbered setup steps, limits, setup-guide button
    if copy:
        P_ = '<p class="mt-3 leading-relaxed text-slate-700">'
        src = " · ".join(f'<a href="{html.escape(u, quote=True)}" rel="noopener" class="underline hover:text-indigo-600">{html.escape(l)} ↗</a>' for l, u in copy["sources"])
        parts = [f'<h2 class="text-xl font-bold">How the {html.escape(A)} + {html.escape(B)} integration works</h2> ']
        if copy.get("answer"): parts.append(f'{P_}<strong>Does {html.escape(A)} integrate with {html.escape(B)}?</strong> {esc(copy["answer"])}</p> ')
        parts.append(f'{P_}{esc(copy["how"])}</p> ')
        cta_html = ""
        if copy["sources"]:
            cl, cu = copy.get("cta") or ("Setup guide: " + copy["sources"][0][0], copy["sources"][0][1])
            cta_html = f'<p class="mt-4"><a href="{html.escape(cu, quote=True)}" rel="noopener" class="scm-cta">{html.escape(cl)} ↗</a></p> '
        early = setup_led(v, copy)   # searchers on these pages want to connect the tools: the button goes right under the answer
        if early: parts.append(cta_html)
        parts.append(flow_figure(v, d, pair, sync))
        if copy.get("setup"):
            parts.append(f'<h3 class="mt-6 font-semibold text-slate-900">How do you set up {html.escape(A)} + {html.escape(B)}?</h3> <ol class="scm-steps"> '
                         + " ".join(f"<li>{esc(x)}</li>" for x in copy["setup"]) + " </ol> ")
            if copy.get("setup_src"):
                sl, su = copy["setup_src"]
                parts.append(f'<p class="mt-2 text-xs text-slate-500">Steps follow <a href="{html.escape(su, quote=True)}" rel="noopener" class="underline hover:text-indigo-600">'
                             f'{html.escape(sl)}&#39;s setup guide ↗</a>, read {copy["setup_checked"]}.</p> ')
        parts.append(f'{P_}<strong>Limitations:</strong> {esc(copy["limits"])}</p> ')
        if copy.get("note"): parts.append(f'{P_}<strong>Before you budget:</strong> {esc(copy["note"])}</p> ')
        if not early: parts.append(cta_html)
        chk = copy.get("checked", "Nov 3, 2026")
        if copy.get("setup_checked") and copy["setup_checked"] != chk:   # one guide, two dates: say which is which
            chk += f"; setup guide read again for the steps on {copy['setup_checked']}"
        parts.append(f'<p class="mt-3 text-xs text-slate-500">Sources (checked {chk}): {src}</p> ')
        sec = (' <section class="mt-10 rounded-xl border border-slate-200 bg-white p-6 shadow-sm sm:p-8" aria-label="How the integration works" id="how-it-works"> '
               + "".join(parts) + '</section>')
        s = re.sub(r' <section class="mt-10 rounded-xl border border-slate-200 bg-white p-6 shadow-sm sm:p-8" aria-label="How the integration works"[^>]*>.*?</section>', "", s, flags=re.S)
        s = sub1(r'(Report a correction →</a> </div>)', lambda m: m.group(1) + sec, s, what="copy insert top")
    return s, v

def excerpt(summary, limit):
    cut = summary[:limit]
    return cut[:cut.rfind(" ")] + "…"

def render_home_card(home, pair, v, summary, limit):
    i = home.index(f'href="/stack/{pair}/"'); j = home.index("</a>", i)
    card = home[i:j]
    card = sub1(r'(data-search="[^"]*) (?:native|middleware)(")', lambda m: m.group(1) + (" native" if v["native"] else " middleware") + m.group(2), card, what="data-search")
    badge = ('<span class="shrink-0 rounded-full px-2.5 py-0.5 text-xs font-medium ring-1 bg-emerald-100 text-emerald-800 ring-emerald-200"> Native </span>' if v["native"]
             else '<span class="shrink-0 rounded-full px-2.5 py-0.5 text-xs font-medium ring-1 bg-sky-100 text-sky-800 ring-sky-200"> Middleware </span>')
    card = sub1(r'<span class="shrink-0 rounded-full[^>]*>[^<]*</span>', badge, card, what="home badge")
    card = sub1(r'(<p class="mt-2 flex-1 text-sm leading-relaxed text-slate-600">).*?(</p>)', lambda m: m.group(1) + " " + esc(excerpt(summary, limit)) + " " + m.group(2), card, what="home excerpt")
    return home[:i] + card + home[j:]

GUIDE_BADGE = {True: '<span class="rounded-full px-2 py-0.5 text-xs font-medium ring-1 bg-emerald-100 text-emerald-800 ring-emerald-200"> Native </span>',
               False: '<span class="rounded-full px-2 py-0.5 text-xs font-medium ring-1 bg-sky-100 text-sky-800 ring-sky-200"> Middleware </span>'}

def render_guide_row(g, pair, v, hubspot_tier=None):
    i = g.find(f'href="/stack/{pair}/"')
    if i < 0: return g
    a = g.rfind("<tr", 0, i); b = g.index("</tr>", i)
    row = g[a:b]
    row = sub1(r'<span class="rounded-full px-2 py-0\.5[^>]*>[^<]*</span>', GUIDE_BADGE[v["native"]], row, what="guide badge")
    if hubspot_tier is not None:
        row = sub1(r'(</span> </td> <td class="px-4 py-3">)[^<]*(</td>)', lambda m: m.group(1) + hubspot_tier + m.group(2), row, what="guide tier")
    return g[:a] + row + g[b:]

def current_state(s):
    summary = html.unescape(re.search(r'<p class="mt-4 max-w-3xl text-lg leading-relaxed text-slate-700">(.*?)</p>', s, re.S).group(1)).strip()
    sync = re.search(r'Data sync direction</td> <td class="px-4 py-3" colspan="2">(.*?)</td>', s, re.S).group(1)
    return summary, sync

def main(mode):
    facts = build_facts()
    pages = sorted(glob.glob("stack/*/index.html"))
    home = read("index.html"); guides = {g: read(f"{g}/index.html") for g in ("hubspot-integrations-cost", "salesforce-integrations-cost", "crm-integration-pricing-guide")}
    # find the homepage excerpt limit that reproduces every card
    limit = None
    for lim in range(70, 101):
        ok = True
        for f in pages:
            p = f.split("/")[1]; summ, _ = current_state(read(f))
            i = home.index(f'href="/stack/{p}/"')
            ex = html.unescape(re.search(r'<p class="mt-2 flex-1 text-sm leading-relaxed text-slate-600">(.*?)</p>', home[i:], re.S).group(1)).strip()
            if excerpt(summ, lim) != ex: ok = False; break
        if ok: limit = lim; break
    assert limit, "could not reproduce homepage excerpts"
    print("homepage excerpt limit:", limit)
    out = {}; home2 = home; guides2 = dict(guides); bad = []
    for f in pages:
        p = f.split("/")[1]; s = read(f); d = calc_data(s); summ, sync = current_state(s)
        if mode == "selftest":
            s2, v = render_page(s, p, d, summ, sync, facts, copy=COPY[p] if COPY.get(p, {}).get('top') else None, cta=PAIRS.get(p, {}).get('cta', True))
            if s2 != s: bad.append(p)
            h2 = render_home_card(home2, p, v, summ, limit)
            if h2 != home2: bad.append("home:" + p)
            for g in guides2:
                if render_guide_row(guides2[g], p, v, next((t["required"] for t in d["tools"] if t["slug"] == "hubspot"), None) if g == "hubspot-integrations-cost" else None) != guides2[g]: bad.append(g + ":" + p)
            continue
        fix = PAIRS.get(p); cp = COPY.get(p)
        if not fix and any(t["slug"] in TOOL_TIERS for t in d["tools"]):
            fix = dict(native=d["middleware"] == 0, req={}, sync=sync, summary=summ)
            if p in SUMMARY_FIXES:
                assert SUMMARY_FIXES[p][0] in summ or SUMMARY_FIXES[p][1] in summ, p; fix["summary"] = summ.replace(*SUMMARY_FIXES[p])
        if p in MW7:
            if not fix: fix = dict(native=False, req={}, sync=sync, summary=summ)
            if p in SUMMARY7: fix["summary"] = SUMMARY7[p]
            else:
                for _a, _b in SUMMARY7_GENERIC:
                    fix["summary"] = fix["summary"].replace(_a, _b)
            if p in REQ7: fix["req"] = dict(fix["req"], **REQ7[p])
        if not fix and not cp:   # round 16 (2026-11-08) re-renders every pair: new trap text, FAQ and descriptions
            fix = dict(native=d["middleware"] == 0, req={}, sync=sync, summary=summ)
        if fix:
            for t in d["tools"]:
                if t["slug"] in TOOL_TIERS:
                    t["required"] = RENAME.get(t["slug"], {}).get(t["required"], t["required"])
                    _free = [x for x in t["tiers"] if x["tier_name"] == "Free"]
                    _api = {x["tier_name"]: x.get("api", True) for x in t["tiers"]}
                    t["tiers"] = _copy.deepcopy(TOOL_TIERS[t["slug"]])
                    for x in t["tiers"]:
                        if x.get("api") is None: x["api"] = _api.get(x["tier_name"], True)
                    if _free and not any(x["tier_name"] == "Free" for x in t["tiers"]): t["tiers"] = _free + t["tiers"]
                if t["slug"] in fix["req"]: t["required"] = fix["req"][t["slug"]]
                if fix["req"].get(t["slug"]) == "Free" and not any(x["tier_name"] == "Free" for x in t["tiers"]):
                    t["tiers"].insert(0, {"tier_name": "Free", "base": 0, "perSeat": 0, "minSeats": 1, "api": True})
            if fix["native"]: d["middleware"], d["middlewareLabel"] = 0, "No middleware required"
            else: d["middleware"], d["middlewareLabel"] = (fix.get("mw") or d["middleware"] or 9), "Middleware"
            if p in MW7: d["middleware"], d["middlewareAnnual"] = MW7[p]
            summ, sync = fix["summary"], fix["sync"]
        s2, v = render_page(s, p, d, summ, sync, facts, date_modified=max(MODIFIED.get(p, ROUND_DATE), ROUND_DATE), copy=cp, cta=(fix or {}).get('cta', True))
        out[f] = s2
        if fix:
            home2 = render_home_card(home2, p, v, summ, limit)
            for g in guides2:
                guides2[g] = render_guide_row(guides2[g], p, v, next((t["required"] for t in d["tools"] if t["slug"] == "hubspot"), None) if g == "hubspot-integrations-cost" else None)
    if mode == "selftest":
        print("selftest mismatches:", len(bad), bad[:10]); return
    # related-card labels on every page for pairs whose connection type changed
    changed = {p: ("Native" if PAIRS[p]["native"] else "Middleware") for p in PAIRS}
    for f in pages:
        s = out.get(f, read(f))
        for p, lab in changed.items():
            s = re.sub(r'(<a href="/stack/' + re.escape(p) + r'/" class="rounded-xl[^>]*> <h3[^>]*> [^<]+ </h3> <p class="mt-1 text-xs font-medium text-slate-500"> )\w+( </p>)', lambda m: m.group(1) + lab + m.group(2), s)
        if s != read(f): out[f] = s
    out["index.html"] = home2
    for g, txt in guides2.items(): out[f"{g}/index.html"] = txt
    for f, s in out.items():
        if s != read(f): open(f, "w", encoding="utf-8").write(s); print("wrote", f)

if __name__ == "__main__":
    main(sys.argv[1])
