"""Share images (1200x630 JPEG) for link previews, image search and AI answers that show images.
One per integration pair, tool hub, API-access page, the HubSpot Professional guide, plus a bar chart for the research report.
Run from the repo root after data changes:  python3 scripts/og17.py   (site16.py then points each page at its image)
Needs node + playwright. Only re-renders images whose content changed (hash stored in og/manifest.json)."""
import glob, hashlib, html, json, os, re, subprocess, sys, tempfile
sys.path.insert(0, os.path.dirname(__file__))
from model import compute, money

SHORT = {"Salesforce Sales Cloud": "Salesforce", "QuickBooks Online": "QuickBooks"}
m0 = lambda x: money(x).replace(".00", "")
HOME = "og-image"   # this card is saved as /og-image.png (PNG), not in og/
# The cards follow the site theme (2026-11-11): white paper, navy ink, grey tiles like the homepage chart,
# and the yellow tile only for a hidden cost (a forced upgrade or a connector fee).
CSS = """@font-face{font-family:"Barlow";src:url(%%FONTS%%/barlow-400.woff2) format("woff2");font-weight:400 500}
@font-face{font-family:"Barlow";src:url(%%FONTS%%/barlow-600.woff2) format("woff2");font-weight:600 900}
@font-face{font-family:"Barlow Semi Condensed";src:url(%%FONTS%%/barlow-semi-condensed-600.woff2) format("woff2");font-weight:500 900}
html,body{margin:0;width:1200px;height:630px}
body{font-family:"Barlow",system-ui,sans-serif;background:#fff;color:#16223f;border-top:16px solid #16223f;
display:flex;flex-direction:column;justify-content:space-between;padding:48px 72px 56px;box-sizing:border-box}
.top{display:flex;align-items:center;gap:16px;font-family:"Barlow Semi Condensed";font-size:38px;font-weight:700}.top img{width:60px;height:60px;border-radius:8px}
.k{font-size:28px;font-weight:500;color:#44506b}
h1{font-family:"Barlow Semi Condensed";font-size:86px;line-height:1.02;margin:6px 0 0;font-weight:700}h1.s{font-size:66px}
.row{display:flex;gap:12px;flex-wrap:wrap}.box{background:#f2f4f8;padding:18px 26px 20px;min-width:150px}
.box b{display:block;font-family:"Barlow Semi Condensed";font-size:52px;font-weight:700;font-variant-numeric:tabular-nums lining-nums}.box b.t{font-size:33px;line-height:1.55}.box span{font-size:23px;color:#2f3b58}
.g{background:#ffe45c}
.bars{display:flex;flex-direction:column;gap:9px}.bar{display:flex;align-items:center;gap:14px;font-size:24px;font-weight:500}
.bar i{display:block;height:30px;background:#ffe45c}.bar .n{width:330px;text-align:right;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}.bar .v{font-family:"Barlow Semi Condensed";font-weight:700;font-variant-numeric:tabular-nums}"""

def page(kicker, title, body, small=False):
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>'
            f'<div class="top"><img src="%%LOGO%%">StackCostMatrix</div>'
            f'<div><div class="k">{html.escape(kicker)}</div><h1{" class=s" if small else ""}>{html.escape(title)}</h1></div>{body}</body></html>')

def boxes(items):
    return '<div class="row">' + "".join(f'<div class="box{" g" if g else ""}"><b{" class=t" if len(big) > 12 else ""}>{html.escape(big)}</b><span>{html.escape(lab)}</span></div>' for big, lab, g in items) + "</div>"

def cards():
    out = {}
    pairs = []
    for f in sorted(glob.glob("stack/*/index.html")):
        p = f.split("/")[1]
        d = json.loads(re.search(r'id="calc-data">(.*?)</script>', open(f, encoding="utf-8").read(), re.S).group(1)); v = compute(d)
        A, B = (SHORT.get(t["name"], t["name"]) for t in d["tools"])
        extra = (v["mw"] + max(0.0, v["UP"] - v["mw"])) if not v["native"] else v["UP"]
        out[p] = page("Integration cost, 2026", f"{A} + {B}", boxes([
            (m0(v["N"]), "a month for 10 seats", False),
            (("+" + m0(extra)) if extra > 0.004 else "$0", "hidden cost to connect" if extra > 0.004 else "extra to connect", extra > 0.004),
            (f"{A} {v['ta']} + {B} {v['tb']}", "plans needed", False)]))
        pairs.append((p, d, v))
    # tool hubs
    D = json.load(open("data/integration-pairs.json", encoding="utf-8"))
    for f in sorted(glob.glob("*-integrations-cost/index.html")):
        slug = f.split("/")[0][:-len("-integrations-cost")]
        mine = [v for _, d, v in pairs if any(t["slug"] == slug for t in d["tools"])]
        if not mine or slug not in D["tools"]: continue
        name = SHORT.get(D["tools"][slug]["name"], D["tools"][slug]["name"])
        free = sum(1 for _, d, v in pairs if any(t["slug"] == slug for t in d["tools"]) and v["native"] and v["UP"] <= 0.004)
        out[f.split("/")[0]] = page("Integration costs by tool, 2026", f"{name} integration costs", boxes([
            (str(len(mine)), "integrations priced", False),
            (f"{m0(min(v['N'] for v in mine))} – {m0(max(v['N'] for v in mine))}", "a month for 10 seats, both tools", False),
            (f"{free} of {len(mine)}", "cost nothing extra to connect", False)]), small=True)
    # API-access pages
    from apidata import TOOLS
    for slug, T in TOOLS.items():
        if not os.path.exists(f"{slug}-api-access/index.html") or slug not in D["tools"]: continue
        name = SHORT.get(D["tools"][slug]["name"], D["tools"][slug]["name"])
        items = [(pl, {"Yes": "API: yes", "No": "API: no", "Add-on": "API: paid add-on"}.get(f["api"], "API: not stated"), f["api"] == "Add-on") for pl, f in list(T["plans"].items())[:4]]   # yellow only where API access costs extra
        out[f"{slug}-api-access"] = page("API and webhooks by plan, 2026", f"{name} API access by plan", boxes(items), small=True)
    # HubSpot Professional guide
    pro = [(p, v) for p, d, v in pairs if any(t["slug"] == "hubspot" and t["required"] == "Professional" for t in d["tools"])]
    hs = [p for p, d, v in pairs if any(t["slug"] == "hubspot" for t in d["tools"])]
    out["hubspot-professional-integrations"] = page("HubSpot plans, 2026", "Which integrations need HubSpot Professional?", boxes([
        (f"{len(pro)} of {len(hs)}", "HubSpot integrations need Professional", False), ("$50/seat", "cheapest Professional plan, a month", True),
        (f"{len(hs) - len(pro)}", "work on the free CRM", False)]), small=True)
    # CRM guide
    crm = set(re.findall(r'href="/stack/([^"/]+)/"', open("crm-integration-pricing-guide/index.html", encoding="utf-8").read()))
    cv = [v for p, d, v in pairs if p in crm]
    if cv:
        out["crm-integration-pricing-guide"] = page("CRM integration costs, 2026", "HubSpot, Salesforce and Pipedrive integrations", boxes([
            (str(len(cv)), "CRM integrations priced", False), (f"{m0(min(v['N'] for v in cv))} – {m0(max(v['N'] for v in cv))}", "a month for 10 seats, both tools", False),
            (f"{sum(1 for v in cv if v['native'])} native, {sum(1 for v in cv if not v['native'])} via connector", "how they connect", False)]), small=True)
    # research report: bar chart of the most expensive integrations
    from research import dataset
    _, rows = dataset(); top = rows[:8]; vmax = top[0]["tax"]
    bars = '<div class="bars">' + "".join(
        f'<div class="bar"><span class="n">{html.escape(r["label"])}</span><i style="width:{max(6, round(520 * r["tax"] / vmax))}px"></i><span class="v">{m0(r["tax"])}/mo</span></div>' for r in top) + "</div>"
    out["integration-tax-2026"] = (f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}body{{padding:36px 64px 40px}}h1{{font-size:50px;margin:4px 0 0}}.k{{font-size:24px}}</style></head><body>'
                                   f'<div class="top"><img src="%%LOGO%%">StackCostMatrix</div>'
                                   f'<div><div class="k">The Integration Tax 2026, for 10 seats</div><h1>The most expensive SaaS integrations to connect</h1></div>{bars}</body></html>')
    # the site's own share image (og-image.png), for the homepage and pages without a card
    n_extra = sum(1 for _, d, v in pairs if v["UP"] > 0.004); n_tools = len({t["slug"] for _, d, v in pairs for t in d["tools"]})
    out[HOME] = page("An independent price index, checked on each vendor's own pages", "What a SaaS integration really costs", boxes([
        (str(len(pairs)), "integrations priced", False), (str(n_extra), "include a cost the pricing page doesn't show", True), (str(n_tools), "business tools", False)]), small=True)
    return out

def main():
    os.makedirs("og", exist_ok=True)
    man_f = "og/manifest.json"
    man = json.load(open(man_f)) if os.path.exists(man_f) else {}
    todo = []
    for key, pg in cards().items():
        h = hashlib.sha256(pg.encode()).hexdigest()[:16]
        if man.get(key) != h or not os.path.exists("og-image.png" if key == HOME else f"og/{key}.jpg"): todo.append((key, pg, h))
    if todo:
        tmp = tempfile.mkdtemp(); logo = "file://" + os.path.abspath("icon-192.png"); fonts = "file://" + os.path.abspath("fonts"); jobs = []
        for key, pg, h in todo:
            open(f"{tmp}/{key}.html", "w", encoding="utf-8").write(pg.replace("%%LOGO%%", logo).replace("%%FONTS%%", fonts)); jobs.append([f"file://{tmp}/{key}.html", os.path.abspath(f"og/{key}.png")])
        js = ("const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const pg=await b.newPage({viewport:{width:1200,height:630},deviceScaleFactor:1});"
              f"for(const [u,o] of {json.dumps(jobs)}){{await pg.goto(u);await pg.evaluate(()=>document.fonts.ready);await pg.screenshot({{path:o}})}}await b.close()}})()")
        subprocess.run(["node", "-e", js], check=True)
        from PIL import Image
        for key, pg, h in todo:
            if key == HOME: Image.open(f"og/{key}.png").convert("RGB").save("og-image.png", optimize=True)
            else: Image.open(f"og/{key}.png").convert("RGB").save(f"og/{key}.jpg", "JPEG", quality=82, optimize=True, progressive=True)
            os.remove(f"og/{key}.png"); man[key] = h
        json.dump(man, open(man_f, "w"), indent=1, sort_keys=True)
    print(f"share images: {len(todo)} rendered, {len(man)} total")

if __name__ == "__main__":
    main()
