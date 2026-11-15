# Site maintenance toolkit

These scripts generate and check stackcostmatrix.com. The site itself is plain HTML served by GitHub Pages from the repo root, with no build step: **every change is made by editing files and committing them.** `robots.txt` keeps this folder out of search engines.

Run everything **from the repo root**. Needs `python3`, plus `node` with Playwright for the browser checks.

**Shortcut:** `bash scripts/build_all.sh` runs every generator in the right order, twice, and fails if the second run changes anything. Then run `bash scripts/check_all.sh`. The step-by-step lists below show what it runs. `CLAUDE.md` at the repo root holds the short working notes.

## Golden rules
1. **Every fact comes from the vendor's own page,** read on the day you change it. If a page can't be read (make.com, quickbooks.intuit.com/pricing and pipedrive.com/pricing block automated reads), leave the fact and its date unchanged and say so in the PR.
2. **Never change a "checked" date unless you actually re-read that fact.** Dates are part of the site's credibility.
3. **Never merge.** Open a pull request describing exactly what changed and why, with links to the evidence. The owner reviews and merges.
4. **Run `bash scripts/check_all.sh` before every commit.** It must end with `ALL CHECKS PASSED`.
5. **The Integration Tax report** (`/integration-tax-2026/`) covers every pair in the index (since Nov 14, 2026; before that, only the 55 it was published with). When new pairs change its figures, add a dated changelog entry with the old and new headline numbers (see `polish22.py`) and update the "Updated" date and `dateModified` in `research.py`.

## How the site is put together
| Thing | Where it lives | How it's produced |
|---|---|---|
| 90 pair pages | `stack/<a>-and-<b>/index.html` | Each has a `calc-data` JSON block (plans, prices, required plan, connector fee). `pairfix.py` renders the rest of the page from it: summary, TCO box, FAQ, meta, spec matrix, "How it works". |
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
| Links between pages | every page | `links24.py` rebuilds them on every build: the related-pair cards and the API sentence on pair pages, the "by tool" grid and API list on the homepage, the link lists and pair tables on the three hand-written pages, and the footer's guide list. `hubs.py` and `apipages.py` write the same lists on the pages they generate. See "Links between pages" below. |
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

## Links between pages
`links24.py` owns every block of internal links that used to be written once and then went stale. It runs in `build_all.sh` after the page generators and before `ux18.py`, and replaces each block on every run.
- **Related cards on pair pages.** Each tool's partners are put in a ring, ordered by category (`CAT_ORDER`, read from the homepage cards' `data-cats`) and then by name. A page links to its three nearest neighbours in each of its two rings. A pair whose tools both have four or more integrations therefore gets at least six links from other pair pages (seven where a page's other tool has only three integrations and takes four cards from this side); a new pair is linked from older pages on the next build; adding one changes only its neighbours' cards. Each card shows the connection type and the 10-seat monthly total. `pairfix.py` and `consistency.py` read the card's one-word type line, so keep that `<p>` as it is.
- **Sentences, not chains.** Links to hubs, API pages, the CRM guide, the HubSpot Professional guide and the report sit in sentences that say what the target is. Don't go back to "A → · B → · C →" rows or to link text such as "Calculator →": the same words on 150 links tell a reader, and a search engine, nothing about the page behind each one.
- **Link lists** (`hubs.index_list`, class `scm-index`): "Slack integrations" leads to a hub, "Slack API access" to an API page. The tool's name alone used to point at both.
- **Hand-written tables** (HubSpot hub, Salesforce hub, CRM guide): the pair's name in the first cell is the link. A row added in the old shape (plain name, a last cell with "True-cost calculator →") is converted on the next build; `ux18.py` then appends the 10-seat total and the check date.
- **Footer.** `site_nav()` writes the same "Cost guides" list on every page and computes the pair count. A `newpairs` script copies a template page and swaps tool names, which used to rewrite the footer's first link on the new page; the build now puts it right.
- **Check:** `linkcheck.py` (part of `check_all.sh`) fails if a sitemap page is more than three clicks from the homepage, a pair page has fewer than three links from other pair pages or lacks a link to its tools' hubs and API pages, the homepage misses a hub or API page, link text says nothing ("Calculator", "Read more"), or the footer differs between pages.
- **IndexNow:** `python3 scripts/indexnow.py --since YYYY-MM-DD` lists the sitemap URLs changed since that day; add `--send` to notify Bing. It contacts an outside service, so it is not part of the build: run it only when the owner says so, after the change is live.

## Common jobs

**Change a price** (example: Slack Pro goes from $8.75 to $9.25 per seat, monthly):
```bash
# 1. edit scripts/pairdata5.py -> TOOL_TIERS5["slack"]   (name, base, per-seat monthly, per-seat annual or None)
python3 scripts/pairfix.py apply      # re-renders every pair page that uses that tool
python3 scripts/hubs.py               # tool hubs
python3 scripts/apipages.py           # API pages (plan price column)
python3 scripts/research.py           # only if the change corrects the report's figures
python3 scripts/ui13.py               # finder data on homepage/404
python3 scripts/links24.py            # related-pair cards (they show each pair's 10-seat cost), link lists, footer
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

**Add new pairs (between tools the site already prices):** write a dated `pairdataN.py` like `pairdata22.py` (per pair: a template page of the same connection type that shares one tool, the plans each tool needs, summary, answer, how it works, limits, setup steps, sources, diagram labels), hook it into `pairfix.py` next to `pairdata22`, then run a copy of `newpairs22.py` (builds the pages once from their templates) and of `wire22.py` (open data, homepage cards, counts, guide rows, changelogs, READMEs), then `build_all.sh` and `check_all.sh`. The build's `links24.py` step then links the new pages in by itself: related cards on the new and the neighbouring pages, the guide rows' links, the homepage "by tool" grid if a tool gains a hub, and the footer. `research.py` picks up new pairs by itself; log the report's changed figures (see rule 5). Batch 2 (`pairdata23.py`, `newpairs23.py`, `wire23.py`) is the latest worked example. A tool tier no page used before gets its spec cells from another tier with the same facts in `apidata.py`; `newpairs22.py` prints each case.

**Read a vendor page the way the checks did:** `node scripts/docread.js <outdir> name=https://vendor.com/pricing` saves the page text to `<outdir>/name.txt` and prints plan-related sentences.

## Monthly price re-check (what the scheduled task does)
1. For each tool, open its official pricing page (URLs in the "Official vendor documentation index" table on `about/index.html`) and compare the monthly and annual prices with the site's data.
2. Re-read the connector prices: Zapier (zapier.com/pricing, monthly and yearly toggles) and Data Mapper. make.com blocks automated reads, so leave Make alone unless it can be read.
3. **If nothing changed:** open no PR. Report "no price changes found" with the list of pages checked and which couldn't be read.
4. **If something changed:** make the change as above, update only the dates of facts you re-read, run `check_all.sh`, and open a PR. The description should give a before/after table per affected page (10-seat monthly cost) and quote the vendor page for each change.
