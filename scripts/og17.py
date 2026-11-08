"""Per-pair share images (1200x630 JPEG) for link previews and AI answers that show images.
Run from the repo root after pair data changes:  python3 scripts/og17.py   (then site16.py points each pair page at its image)
Needs node + playwright. Only re-renders images whose text changed (hash stored in og/manifest.json)."""
import glob, hashlib, html, json, os, re, subprocess, sys, tempfile
sys.path.insert(0, os.path.dirname(__file__))
from model import compute, money

SHORT = {"Salesforce Sales Cloud": "Salesforce", "QuickBooks Online": "QuickBooks"}
TPL = """<!doctype html><html><head><meta charset="utf-8"><style>
html,body{margin:0;width:1200px;height:630px}
body{font-family:Inter,system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;background:#3730a3;background:linear-gradient(135deg,#4f46e5,#312e81);color:#fff;
display:flex;flex-direction:column;justify-content:space-between;padding:64px 76px;box-sizing:border-box}
.top{display:flex;align-items:center;gap:18px;font-size:34px;font-weight:800}.top img{width:64px;height:64px;border-radius:16px}
.k{font-size:26px;font-weight:700;letter-spacing:3px;text-transform:uppercase;color:#a5b4fc}
h1{font-size:76px;line-height:1.05;margin:10px 0 0;font-weight:800;letter-spacing:-1.5px}
.row{display:flex;gap:18px;flex-wrap:wrap}.box{background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.28);border-radius:20px;padding:18px 26px}
.box b{display:block;font-size:44px;font-weight:800}.box span{font-size:22px;color:#e0e7ff}.trap b{color:#6ee7b7}
</style></head><body>
<div class="top"><img src="%%LOGO%%">StackCostMatrix</div>
<div><div class="k">Integration cost · 2026</div><h1>%%TITLE%%</h1></div>
<div class="row"><div class="box"><b>%%TOTAL%%</b><span>a month for 10 seats</span></div><div class="box trap"><b>%%EXTRA%%</b><span>%%EXTRA_LABEL%%</span></div><div class="box"><b style="font-size:30px;line-height:1.5">%%PLANS%%</b><span>plans needed</span></div></div>
</body></html>"""

def card(p, d):
    v = compute(d)
    A, B = (SHORT.get(t["name"], t["name"]) for t in d["tools"])
    extra = (v["mw"] + max(0.0, v["UP"] - v["mw"])) if not v["native"] else v["UP"]
    m0 = lambda x: money(x).replace(".00", "")
    return {"TITLE": html.escape(f"{A} + {B}"), "TOTAL": m0(v["N"]),
            "EXTRA": ("+" + m0(extra)) if extra > 0.004 else "$0",
            "EXTRA_LABEL": "hidden cost to connect" if extra > 0.004 else "extra to connect",
            "PLANS": html.escape(f"{A} {v['ta']} · {B} {v['tb']}")}

def main():
    os.makedirs("og", exist_ok=True)
    man_f = "og/manifest.json"
    man = json.load(open(man_f)) if os.path.exists(man_f) else {}
    todo = []
    for f in sorted(glob.glob("stack/*/index.html")):
        p = f.split("/")[1]
        d = json.loads(re.search(r'id="calc-data">(.*?)</script>', open(f, encoding="utf-8").read(), re.S).group(1))
        c = card(p, d); h = hashlib.sha256(json.dumps(c, sort_keys=True).encode()).hexdigest()[:16]
        if man.get(p) != h or not os.path.exists(f"og/{p}.jpg"): todo.append((p, c, h))
    if todo:
        tmp = tempfile.mkdtemp()
        logo = "file://" + os.path.abspath("icon-192.png")
        jobs = []
        for p, c, h in todo:
            page = TPL.replace("%%LOGO%%", logo)
            for k, val in c.items(): page = page.replace(f"%%{k}%%", val)
            open(f"{tmp}/{p}.html", "w").write(page); jobs.append([f"file://{tmp}/{p}.html", os.path.abspath(f"og/{p}.png")])
        js = ("const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const pg=await b.newPage({viewport:{width:1200,height:630},deviceScaleFactor:1});"
              f"for(const [u,o] of {json.dumps(jobs)}){{await pg.goto(u);await pg.screenshot({{path:o}})}}await b.close()}})()")
        subprocess.run(["node", "-e", js], check=True)
        from PIL import Image
        for p, c, h in todo:
            Image.open(f"og/{p}.png").convert("RGB").save(f"og/{p}.jpg", "JPEG", quality=82, optimize=True, progressive=True)
            os.remove(f"og/{p}.png"); man[p] = h
        json.dump(man, open(man_f, "w"), indent=1, sort_keys=True)
    print(f"share images: {len(todo)} rendered, {len(man)} total")

if __name__ == "__main__":
    main()
