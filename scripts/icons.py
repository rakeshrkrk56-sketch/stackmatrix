"""Brand icons from logo.svg and favicon.svg (2026-11-11). Run from the repo root:  python3 scripts/icons.py
Writes icon-512.png, icon-192.png and apple-touch-icon.png (square, colour to the corners), favicon-48.png and
favicon.ico (rounded, transparent corners). The mark's shape is the owner's choice; only its colours follow the theme:
navy square, and the coin in the same yellow that marks hidden costs across the site. Needs node + playwright and PIL."""
import json, os, re, subprocess, tempfile
from PIL import Image

INK, COIN = "#16223f", "#ffe45c"

def recolour(svg):
    svg = re.sub(r'(<rect width="64" height="64" rx="14" fill=")#[0-9a-f]{6}', r"\g<1>" + INK, svg)                      # the square
    svg = re.sub(r'(<circle [^>]*fill=")#[0-9a-f]{6}(" stroke=")#[0-9a-f]{6}', r"\g<1>" + COIN + r"\g<2>" + INK, svg)      # the coin and its ring
    svg = re.sub(r'(<path d="[^"]*" fill="none" stroke=")#[0-9a-f]{3,6}', r"\g<1>" + INK, svg)                              # the dollar sign
    return svg

def main():
    svgs = {}
    for f in ("logo.svg", "favicon.svg"):
        s = recolour(open(f, encoding="utf-8").read()); open(f, "w", encoding="utf-8").write(s); svgs[f] = s
    tmp = tempfile.mkdtemp(); jobs = []
    square = svgs["logo.svg"].replace('rx="14" fill="' + INK, 'rx="0" fill="' + INK, 1)   # colour to the corners
    for name, size, svg, clear in (("icon-512.png", 512, square, False), ("icon-192.png", 192, square, False), ("apple-touch-icon.png", 180, square, False),
                                   ("favicon-48.png", 48, svgs["favicon.svg"], True), ("_fav32.png", 32, svgs["favicon.svg"], True), ("_fav16.png", 16, svgs["favicon.svg"], True)):
        sized = svg.replace("<svg ", '<svg width="%d" height="%d" style="display:block" ' % (size, size), 1)
        html = '<!doctype html><html><body style="margin:0;background:transparent">' + sized + "</body></html>"
        open(f"{tmp}/{name}.html", "w", encoding="utf-8").write(html)
        jobs.append([f"file://{tmp}/{name}.html", os.path.abspath(name if not name.startswith("_") else f"{tmp}/{name}"), size, clear])
    js = ("const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();"
          f"for(const [u,o,s,c] of {json.dumps(jobs)}){{const pg=await b.newPage({{viewport:{{width:s,height:s}},deviceScaleFactor:1}});await pg.goto(u);"
          "await pg.screenshot({path:o,omitBackground:c});await pg.close()}await b.close()})()")
    subprocess.run(["node", "-e", js], check=True)
    for name in ("icon-512.png", "icon-192.png", "apple-touch-icon.png"):
        Image.open(name).convert("RGB").save(name, optimize=True)
    Image.open("favicon-48.png").save("favicon-48.png", optimize=True)
    ico = [Image.open("favicon-48.png").convert("RGBA"), Image.open(f"{tmp}/_fav32.png").convert("RGBA"), Image.open(f"{tmp}/_fav16.png").convert("RGBA")]
    ico[0].save("favicon.ico", format="ICO", sizes=[(48, 48), (32, 32), (16, 16)], append_images=ico[1:])
    print("icons written from logo.svg and favicon.svg")

if __name__ == "__main__":
    main()
