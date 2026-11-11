import re, json, glob
def money(x): return "${:,.2f}".format(x)
MAKE_MONTHLY = 10.59  # Make Core, billed monthly (the annual-billing price is $9)
def tiers(t): return [dict(tier_name=u["tier_name"], base=u.get("base", 0), perSeat=u.get("perSeat", 0), minSeats=u.get("minSeats", 1), api=u.get("api", False)) for u in t["tiers"]]
def cost(tier, slug, seats=10):
    addon = 25 if slug == "salesforce" and tier["tier_name"] == "Professional" else 0
    return tier["base"] + tier["perSeat"] * max(seats, tier["minSeats"]) + addon * max(seats, tier["minSeats"])
def cheapest_api(t):
    ts = [u for u in tiers(t) if u["api"]]
    if not ts: return None
    best = ts[0]
    for u in ts[1:]:
        if cost(u, t["slug"]) < cost(best, t["slug"]): best = u
    return best
def compute(d):
    v = {}
    A, B = d["tools"]
    for k, t in (("a", A), ("b", B)):
        req = next(u for u in tiers(t) if u["tier_name"] == t["required"])
        v[f"n{k}"] = t["name"]; v[f"t{k}"] = t["required"]; v[f"c{k}"] = cost(req, t["slug"]); v[f"api{k}"] = "Yes" if req["api"] else "No"
        ca = cheapest_api(t); v[f"ch{k}"] = cost(ca, t["slug"]) if ca else 0
    v["mw"] = d["middleware"]; v["native"] = d["middleware"] == 0
    v["N"] = v["ca"] + v["cb"] + v["mw"]
    v["MP"] = v["cha"] + v["chb"] + MAKE_MONTHLY; v["UP"] = v["N"] - (v["cha"] + v["chb"])
    return v
def render_tco(v, rule_b):
    head = f"  <strong>{'Native' if v['native'] else 'Middleware'} integration costs {money(v['N'])}/mo ({money(v['N']*12)}/yr)</strong> for a 10-seat team —\n"
    if not v["native"]:
        return head + f"{v['na']} '{v['ta']}' ({money(v['ca'])}/mo) + {v['nb']} '{v['tb']}' ({money(v['cb'])}/mo)\n          + {money(v['mw'])}/mo middleware. No native connector exists for this pair.\n "
    head += f"{v['na']} '{v['ta']}' ({money(v['ca'])}/mo) + {v['nb']} '{v['tb']}' ({money(v['cb'])}/mo),\n          no middleware required.\n"
    if rule_b(v): return head + f" Alternative: skip the native tier upgrade and run via Make/Zapier middleware for ~{money(v['MP'])}/mo all-in (adds a third-party dependency). "
    return head + f" Middleware via Make/Zapier would add ~{money(MAKE_MONTHLY)}/mo on top of the cheapest API-capable tiers ({money(v['MP'])}/mo all-in) — the native path is cheaper. "
def render_nvm(v, rule_b, sync2=True):
    """One sentence on the trade-off; the chart and the route table under it carry the numbers (2026-11-10)."""
    P = ' <p class="mt-3 leading-relaxed text-slate-700">\n'
    if not v["native"]:
        p1 = (f"There's no native {v['na']} + {v['nb']} connector, so a connector such as Make or Zapier is the integration rather than an alternative. "
              "Each automation runs one way (a trigger in one tool, an action in the other), and the connector's bill grows with the number of tasks or operations you run.")
    elif rule_b(v):
        p1 = ("The connector routes are cheaper on paper because they skip the forced plan upgrade. The trade-off: you swap the native connector for a third-party automation you build and maintain, "
              + ("sync drops from 2-way to 1-way per automation, " if sync2 else "sync stays 1-way per automation, ") + "and the connector bills by usage.")
    else:
        p1 = ("The native connector is the cheapest route here" + (" and the only one with 2-way sync" if sync2 else "")
              + ". Make or Zapier only makes sense if you already run other automations through it, or need a step the native app doesn't offer.")
    return P + p1 + "\n</p> "

def svg_bars(rows, title, fmt=money):
    """A small horizontal bar chart as inline SVG (label above each bar, so it stays readable on phones).
    rows: [(label, value, colour)]. Screen readers get `title` plus every value through aria-label."""
    import html as _h
    w, bar_h, row_h, pad = 360, 16, 46, 4
    vmax = max(v for _, v, _ in rows) or 1
    label = title + ": " + "; ".join(f"{l} {fmt(v)}" for l, v, _ in rows)
    out = [f'<svg class="scm-chart" viewBox="0 0 {w} {len(rows) * row_h + 4}" role="img" aria-label="{_h.escape(label, quote=True)}" xmlns="http://www.w3.org/2000/svg">']
    for i, (l, v, c) in enumerate(rows):
        y = i * row_h + pad
        bw = max(3, round((w - 96) * v / vmax))
        out.append(f'<text x="0" y="{y + 13}" font-size="13" fill="#334155">{_h.escape(l)}</text>'
                   f'<rect x="0" y="{y + 20}" width="{bw}" height="{bar_h}" rx="3" fill="{c}"/>'
                   f'<text x="{bw + 6}" y="{y + 33}" font-size="13" font-weight="700" fill="#0f172a">{_h.escape(fmt(v))}</text>')
    out.append("</svg>")
    return "".join(out)

def svg_flow(top, bottom, label, flows=(), link=None, mid=None, segs=None, hue="#16223f"):
    """A connection diagram as inline SVG: two tool boxes stacked top to bottom (so the text stays readable on phones)
    with labelled arrows between them, or a connector box in the middle when the link runs through one.
    top, bottom, mid: (name, detail). flows: [("down" | "up" | "both", text)] for a direct link; link: one line under them.
    segs: (text above the connector, text below it, "down" | "both") when mid is given. label: the aria-label sentence.
    340 units wide: on a phone the drawing is about 0.9 of that, so 12-unit text still renders near 11px."""
    import html as _h
    e = _h.escape
    W, NH, MH, X, TX, ROW, SEG = 340, 50, 46, 24, 44, 22, 34
    out = []
    def node(y, name, detail, h=NH, fill="#fff", stroke="#cbd5e1", ink="#0f172a", ink2="#475569"):
        out.append(f'<rect x="1" y="{y}" width="{W - 2}" height="{h}" rx="8" fill="{fill}" stroke="{stroke}" stroke-width="1.25"/>'
                   f'<text x="14" y="{y + 21}" font-size="14" font-weight="700" fill="{ink}">{e(name)}</text>'
                   f'<text x="14" y="{y + h - 11}" font-size="12" fill="{ink2}">{e(detail)}</text>')
    def arrow(y1, y2, d, c):
        a, b = y1 + (3 if d in ("up", "both") else 0), y2 - (3 if d in ("down", "both") else 0)
        out.append(f'<line x1="{X}" y1="{a}" x2="{X}" y2="{b}" stroke="{c}" stroke-width="1.5"/>')
        if d in ("down", "both"): out.append(f'<polygon points="{X - 4},{y2 - 6} {X + 4},{y2 - 6} {X},{y2}" fill="{c}"/>')
        if d in ("up", "both"): out.append(f'<polygon points="{X - 4},{y1 + 6} {X + 4},{y1 + 6} {X},{y1}" fill="{c}"/>')
    def note(y, text, size=12.5, fill="#0f172a", weight="400"):
        out.append(f'<text x="{TX}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{fill}">{e(text)}</text>')
    node(0, *top)
    if mid:
        up, down, d = segs
        arrow(NH + 3, NH + SEG - 3, d, hue); note(NH + SEG // 2 + 4, up)
        node(NH + SEG, *mid, h=MH, fill="#ecfeff", stroke=hue, ink="#155e75", ink2="#155e75")
        arrow(NH + SEG + MH + 3, NH + 2 * SEG + MH - 3, d, hue); note(NH + SEG + MH + SEG // 2 + 4, down)
        y = NH + 2 * SEG + MH
    else:
        y = NH + 8
        for d, text in flows:
            arrow(y + 1, y + ROW - 5, d, hue); note(y + 14, text); y += ROW
        if link: note(y + 13, link, size=11.5, fill="#16223f", weight="600"); y += 20
        y += 6
    node(y, *bottom)
    return (f'<svg class="scm-diagram" viewBox="0 0 {W} {y + NH + 1}" role="img" aria-label="{e(label, quote=True)}" xmlns="http://www.w3.org/2000/svg">'
            + "".join(out) + "</svg>")
