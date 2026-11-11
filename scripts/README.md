# Site maintenance toolkit

These scripts generate and check stackcostmatrix.com. The site itself is plain HTML served by GitHub Pages from the repo root, with no build step: **every change is made by editing files and committing them.** `robots.txt` keeps this folder out of search engines.

Run everything **from the repo root**. Needs `python3`, plus `node` with Playwright for the browser checks.

**Shortcut:** `bash scripts/build_all.sh` runs every generator in the right order, twice, and fails if the second run changes anything. Then run `bash scripts/check_all.sh`. The step-by-step lists below show what it runs. `CLAUDE.md` at the repo root holds the short working notes.

## Golden rules
1. **Every fact comes from the vendor's own page,** read on the day you change it. If a page can't be read (make.com, quickbooks.intuit.com/pricing and pipedrive.com/pricing block automated reads), leave the fact and its date unchanged and say so in the PR.
2. **Never change a "checked" date unless you actually re-read that fact.** Dates are part of the site's credibility.
3. **Never merge.** Open a pull request describing exactly what changed and why, with links to the evidence. The owner reviews and merges.
4. **Run `bash scripts/check_all.sh` before every commit.** It must end with `ALL CHECKS PASSED`.
5. **The Integration Tax report** (`/integration-tax-2026/`) is scoped to the 55 pairs it was published with (pairs added later are excluded in `research.py`). Regenerate it after *corrections*, not just because new pairs were added.

## How the site is put together
| Thing | Where it lives | How it's produced |
|---|---|---|
| 59 pair pages | `stack/<a>-and-<b>/index.html` | Each has a `calc-data` JSON block (plans, prices, required plan, connector fee). `pairfix.py` renders the rest of the page from it: summary, TCO box, FAQ, meta, spec matrix, "How it works". |
| Pair content | `pairdata*.py` | Each file is one dated round of verified changes. Later files override earlier ones; `pairfix.py` imports them in order. |
| Tool plan prices | `pairdata5.py` `TOOL_TIERS5` (Airtable, Asana, Calendly, ClickUp, Freshdesk, Intercom, monday.com, Notion, Slack, Zendesk), `pairdata4.py` (ActiveCampaign), `pairdata3.py` (Pipedrive, Xero) | For HubSpot, Mailchimp, QuickBooks, Salesforce and Stripe, prices live only in the pages' `calc-data`. To change one, add its tiers to a new `pairdataN.py` `TOOL_TIERS` entry in the same format and hook it into `pairfix.py` like the others. |
| Connector fees | `pairdata7.py` `MW7` (monthly, annual) and `model.py` `MAKE_MONTHLY` | |
| Tool hubs | `<tool>-integrations-cost/` | `hubs.py`. HubSpot and Salesforce hubs are hand-written. |
| API & webhook pages | `<tool>-api-access/` | `apipages.py`, from `apidata.py` (per-plan facts with sources). `cells8.py` writes the same facts into pair pages' spec tables. |
| Research report | `integration-tax-2026/` | `research.py`. It also updates the homepage research card. |
| Header menu, finder | every page / homepage + 404 | `ui13.py` |
| Homepage FAQ markup | `index.html` | `homefaq.py` rebuilds the JSON-LD from the visible FAQ |
| HubSpot Professional guide | `hubspot-professional-integrations/` | `hspro.py`. Integration requirements come from the pair pages; each Professional Hub's prices are in its `PRO` list (re-read them on HubSpot's pricing pages, clicking the billing toggles). |
| Editor & site identity | every page | `site16.py`: "Edited by Rakesh" byline, one Organization/WebSite/Person @id graph (homepage, /about/) that every page's schema points to, the 1200x630 `og-image.png`, breadcrumbs on the hand-written guides, and the 404 page's redirect for reversed pair URLs (/stack/b-and-a/). Run after the generators. |
| Sitemap | `sitemap-0.xml` | `sitemap16.py` rebuilds it from the pages on disk, with lastmod from each page's dateModified (or its last commit). |
| Jump links | every long page | `ux18.py` adds the "On this page" row under the intro and the anchors it points to. Run it after `pairfix.py` and the generators (they rebuild pages without it). |
| AI/agent files | `llms.txt`, `llms-full.txt`, `<page>/index.md`, robots.txt Content-Signal | `agent17.py` regenerates them from the pages and the open data. |
| Share images | `og/<pair>.jpg`, `og-image.png` | `og17.py` renders a 1200x630 card per pair (cost, extra cost, plans); `site16.py` points each page at it. |
| Security tags | every page | `security.py` writes a Content-Security-Policy `<meta>` (with hashes of the page's inline scripts) and a referrer policy. **Run it last, after any script that changes a page's scripts** (`check_all.sh` fails until you do). If you add an image or script from a new outside site, add its host in `security.py`. |
| Open data | `data/integration-pairs.json` | Keep it in sync with the pages; see `wire13.py` for the field format. |

## Theme (how the site looks)
The look lives in one place: the `CSS` string in `ui13.py`, written into every page as `<style id="scm-ui">`.
- **Idea:** a printed fare chart. White paper, navy ink (`--ink`), thin rules, and one yellow highlighter (`--hl`). The yellow means exactly one thing everywhere: money the sticker price doesn't show (a forced plan upgrade or a connector fee). Don't use it as decoration.
- **How it reaches every page:** the pages' base CSS exposes design tokens (`--font-sans`, `--color-indigo-*`, `--color-amber-*`, `--radius-*`). The theme re-points them, so class names such as `bg-indigo-600` now render navy. Change a colour in `ui13.py`, not in the pages.
- **Fonts:** Barlow and Barlow Semi Condensed (SIL Open Font License, `fonts/OFL.txt`), self-hosted in `fonts/` and preloaded. The "fallback" faces are Arial scaled to Barlow's width (95.8% for text, 82% for headings, measured in Chromium), so the page doesn't jump when the web font loads.
- **Homepage chart:** `ui13.py` `fare_chart()` rebuilds it from the pair pages on every run. `PRICE_NOTE` under it repeats the price-check dates from `/about/`; update both together.
- **Charts, diagrams, share images, icons:** bar colours are set where each chart is built (`model.py`, `pairfix.py`, `hubs.py`, `research.py`, `ux18.py`); share images in `og17.py` (it also writes `/og-image.png`); icons come from `logo.svg` and `favicon.svg` through `icons.py`.

## Common jobs

**Change a price** (example: Slack Pro goes from $8.75 to $9.25 per seat, monthly):
```bash
# 1. edit scripts/pairdata5.py -> TOOL_TIERS5["slack"]   (name, base, per-seat monthly, per-seat annual or None)
python3 scripts/pairfix.py apply      # re-renders every pair page that uses that tool
python3 scripts/hubs.py               # tool hubs
python3 scripts/apipages.py           # API pages (plan price column)
python3 scripts/research.py           # only if the change corrects the report's figures
python3 scripts/ui13.py               # finder data on homepage/404
python3 scripts/og17.py               # share images for pairs, hubs, API pages and the report chart (only re-renders changed ones)
python3 scripts/ux18.py               # "On this page" jump links and their anchors
python3 scripts/site16.py             # editor byline, shared Organization/Person schema, share images, 404 redirects
python3 scripts/agent17.py            # Markdown copies, llms.txt, llms-full.txt, table captions, calculator form markup
python3 scripts/sitemap16.py          # sitemap with lastmod dates
python3 scripts/security.py           # always last: refreshes each page's security policy
bash scripts/check_all.sh
```
Then update `data/integration-pairs.json` (that tool's plan prices and each affected pair's `ten_seat_monthly_cost_usd`), and add a dated entry to the changelog on `about/index.html`.

**Change which plan an integration needs:** add a new dated `pairdataN.py` with a `PAIRS` entry (`native`, `req`, `sync`, `summary`) and, if needed, `COPY` text with its sources. See `pairdata8.py` to `pairdata13.py` for examples. Then run the same commands as above.

**Read a vendor page the way the checks did:** `node scripts/docread.js <outdir> name=https://vendor.com/pricing` saves the page text to `<outdir>/name.txt` and prints plan-related sentences.

## Monthly price re-check (what the scheduled task does)
1. For each tool, open its official pricing page (URLs in the "Official vendor documentation index" table on `about/index.html`) and compare the monthly and annual prices with the site's data.
2. Re-read the connector prices: Zapier (zapier.com/pricing, monthly and yearly toggles) and Data Mapper. make.com blocks automated reads, so leave Make alone unless it can be read.
3. **If nothing changed:** open no PR. Report "no price changes found" with the list of pages checked and which couldn't be read.
4. **If something changed:** make the change as above, update only the dates of facts you re-read, run `check_all.sh`, and open a PR. The description should give a before/after table per affected page (10-seat monthly cost) and quote the vendor page for each change.
