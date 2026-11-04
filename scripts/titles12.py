import re, json, html, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pairdata12 import TOP12
for p in TOP12:
    f = f"stack/{p}/index.html"; s = open(f, encoding="utf-8").read()
    h1 = re.search(r'(<h1 class="text-3xl font-bold tracking-tight sm:text-4xl">)(.*?)(</h1>)', s, re.S)
    name = html.unescape(h1.group(2)).split(" Integration")[0].strip()          # e.g. "Monday.com + Slack"
    t_old = html.unescape(re.search(r"<title>(.*?)</title>", s).group(1))
    short = t_old.split(" Integration")[0].strip()
    title = next(o for o in (f"{short} Integration: How It Works & Cost (2026) | StackCostMatrix", f"{short} Integration: How It Works & Cost (2026)",
                             f"{short} Integration: Setup & Cost (2026)") if len(o) <= 60)
    new_h1 = f"{name} Integration (2026): How It Works, Setup & True Cost"
    s = s.replace(f"<title>{html.escape(t_old, quote=False)}</title>", f"<title>{html.escape(title, quote=False)}</title>", 1)
    s = re.sub(r'(<meta property="og:title" content=")[^"]*(")', lambda m: m.group(1) + html.escape(title, quote=True) + m.group(2), s, count=1)
    s = re.sub(r'(<h1 class="text-3xl font-bold tracking-tight sm:text-4xl">).*?(</h1>)', lambda m: m.group(1) + html.escape(new_h1, quote=False) + m.group(2), s, count=1, flags=re.S)
    def ld(m):
        o = json.loads(m.group(1))
        if o.get("@type") == "WebPage": o["name"] = new_h1
        return '<script type="application/ld+json">' + json.dumps(o, ensure_ascii=False, separators=(",", ":")) + "</script>"
    s = re.sub(r'<script type="application/ld\+json">(.*?)</script>', ld, s, flags=re.S)
    assert f"<title>{html.escape(title, quote=False)}</title>" in s, p
    open(f, "w", encoding="utf-8").write(s); print(f"{len(title):2} {title}  ||  {new_h1}")
