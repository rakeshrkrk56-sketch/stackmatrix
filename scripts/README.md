# Site maintenance toolkit

These scripts generate and check stackcostmatrix.com. The site itself is plain HTML served by GitHub Pages from the repo root, with no build step: **every change is made by editing files and committing them.** `robots.txt` keeps this folder out of search engines.

Run everything **from the repo root**. Needs `python3`, plus `node` with Playwright for the browser checks.

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
| Security tags | every page | `security.py` writes a Content-Security-Policy `<meta>` (with hashes of the page's inline scripts) and a referrer policy. **Run it last, after any script that changes a page's scripts** (`check_all.sh` fails until you do). If you add an image or script from a new outside site, add its host in `security.py`. |
| Open data | `data/integration-pairs.json` | Keep it in sync with the pages; see `wire13.py` for the field format. |

## Common jobs

**Change a price** (example: Slack Pro goes from $8.75 to $9.25 per seat, monthly):
```bash
# 1. edit scripts/pairdata5.py -> TOOL_TIERS5["slack"]   (name, base, per-seat monthly, per-seat annual or None)
python3 scripts/pairfix.py apply      # re-renders every pair page that uses that tool
python3 scripts/hubs.py               # tool hubs
python3 scripts/apipages.py           # API pages (plan price column)
python3 scripts/research.py           # only if the change corrects the report's figures
python3 scripts/ui13.py               # finder data on homepage/404
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
