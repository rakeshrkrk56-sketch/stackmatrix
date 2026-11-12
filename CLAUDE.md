# StackCostMatrix: working memory for Claude

Read this first. It is the short version of what earlier sessions learned, so a new session doesn't have to
rediscover it. Details live in `scripts/README.md`. Update the "State" section at the end of each piece of work.

## What this is
- https://stackcostmatrix.com: an independent index of what B2B software integrations really cost.
- Static HTML, served by GitHub Pages straight from `main`. No build step, no framework.
- 76 pair pages (`stack/<a>-and-<b>/`), 17 tool hubs, 18 API pages, a research report, guides. 119 pages in all.
- 18 tools, so 153 possible pairs; 76 are covered. The plan (owner agreed Nov 12, 2026): fill the grid in batches of
  15 to 25 verified pairs, one PR each, then add tools a few at a time (35 to 40 tools at most, not hundreds).

## The owner's standing rules
- Reply to the owner in the language they write in: short, direct, no jargon. Commits, PRs and site text stay in plain English.
- Always open a PR. Merge only when the owner says "merge PR #N" (squash merge). Never merge or deploy on your own.
- Every fact comes from the vendor's own page, read that day. Never move a "checked" date unless that fact was re-read.
- No invented evidence: no imitation screenshots, no made-up credentials, no "we tested" claims.
- Never put the owner's email or other personal details into requests to outside services.
- Keep token use low. Don't re-run audits after small changes. Don't re-read what this file already covers.

## How to change the site (every time)
1. Change data or a generator in `scripts/`. Don't hand-edit generated pages; the next build overwrites them.
2. `bash scripts/build_all.sh` runs the whole pipeline twice and must print `BUILD OK (repeatable)`.
3. `bash scripts/check_all.sh` must print `ALL CHECKS PASSED`.
4. Commit, push to the work branch, open a PR. After the owner merges: reset the branch to `origin/main`, then check the
   live site matches the repo (`curl` a few changed files and `cmp` them).

## Where things live
| Thing | File |
|---|---|
| Pair page rendering | `scripts/pairfix.py` (data in `pairdata*.py`, later files override earlier ones) |
| Cost model | `scripts/model.py` (also the SVG bar chart and connection diagram) |
| Setup steps | `pairdata19.py` (native pairs), `pairdata21.py` (Make, Zapier, Data Mapper pairs) |
| New pairs, batch 1 (all their facts, steps and diagram labels) | `pairdata22.py`; pages built once by `newpairs22.py`, wired by `wire22.py` |
| Diagram labels | `pairdata20.py` |
| Hubs, API pages, HubSpot guide, report | `hubs.py`, `apipages.py` + `apidata.py`, `hspro.py`, `research.py` |
| Theme, navigation, homepage chart and finder | `ui13.py` (see "Theme" in `scripts/README.md`) |
| Jump links, guide figures | `ux18.py` |
| Editor, schema graph, share-image tags | `site16.py` |
| Markdown copies, llms.txt | `agent17.py` |
| Share images, icons | `og17.py`, `icons.py` |
| One-time text edits | `polish18.py` to `polish21.py` (all idempotent; keep them in the build) |
| Security policy (always last) | `security.py` |

## Things that went wrong before (don't repeat)
- A polish script's regex re-matched after its own edit and pushed "Verified" dates forward on every run. Any
  one-time edit must be idempotent; `build_all.sh` catches it by running twice.
- The homepage links to each pair twice (chart cell and card). Find the card with `href="/stack/<pair>/" data-search=`.
- Every class used in HTML must exist in the CSS or start with `scm-`, or `check_all.sh` fails.
- `security.py` must run last after any change to a page's scripts.
- `pairfix.py selftest` must reproduce every pair page byte for byte. If a later script adds markup to pair pages,
  put it where pairfix's patterns don't reach (see `ux18.py`).
- New pairs: `hspro.py` asserts every HubSpot pair needs Free, Starter or Professional, and a tool's Free tier must be in
  the calculator data whenever the tool's other pages list it (Airtable, HubSpot), or the forced-upgrade amount is wrong.

## Reading vendor pages
- `node scripts/docread.js <outdir> name=https://...` saves a page's text (Playwright).
- Can't be read from here, so leave those facts and dates alone: help.clickup.com, support.monday.com,
  help.activecampaign.com (bot check: don't try to get round it), help.salesforce.com, make.com/pricing,
  quickbooks.intuit.com/pricing, pipedrive.com/pricing.
- Readable: apps.make.com/<app> and help.make.com (Make), help.zapier.com and zapier.com/apps/... (Zapier),
  knowledge.hubspot.com, calendly.com/help, docs.stripe.com, support.zendesk.com, intercom.com/help, mailchimp.com/help.

## Audits (claude-seo plugin)
- Sub-agent audits are expensive. Run only the categories a change could move, and resume an earlier auditor
  with SendMessage instead of starting a new one. Use the same rubric each round so scores stay comparable.
- Scores on Nov 11, 2026, live site, with the authority/backlink part left out (the owner's chosen measure):
  Technical 94, Sitemap 96, Performance 100, AI agents 92, Schema 92, Visual 90, GEO 91, Content 89, SXO 76.
- Content needs first-hand evidence to pass 90: real screenshots from the owner. These pairs cost $0 to connect, so
  they can be tested for free: HubSpot + Slack, Stripe + Slack, Slack + Airtable, Slack + Calendly, ClickUp + Slack,
  HubSpot + Stripe.
- SXO can't reach 90 from on-site work: it leans on authority and on the homepage's search intent.

## Search Console access
- `.mcp.json` starts a Search Console MCP server through `scripts/gsc_mcp.sh` (PyPI `mcp-search-console`, pinned to
  0.4.2, code reviewed Nov 11, 2026: it only talks to Google's APIs). Its tools appear as `mcp__search-console__*`.
- It works only when the owner has saved a Google service-account key in the cloud environment's settings, under
  Environment variables, as `GSC_SERVICE_ACCOUNT_JSON='<the whole key file>'` (the single quotes keep its line
  breaks), and has added that service account as a user on the Search Console property.
- The key is a secret. Never ask for it in chat and never print it: no `env`, `printenv` or `set` output. To see
  whether it is there: `[ -n "${GSC_SERVICE_ACCOUNT_JSON:-}" ] && echo set`.
- A session reads environment variables when its VM starts: a new value shows up in a new session, or in an old one
  after it has sat idle for a few minutes.
- Tools missing? Run `bash scripts/gsc_mcp.sh < /dev/null`. It prints the reason (variable not set, key cut off at
  the first line break because the quotes were left out, key incomplete) and exits with 0 when the key is fine.
  If the owner can't get past it, ask for a Search Console export instead (Performance report as CSV, and the Pages
  indexing report).
- The connection is read-only: the server asks Google for the read-only scope, so it can't submit a sitemap or
  change the property. Writing needs `GSC_ALLOW_DESTRUCTIVE=true`, which also switches on the delete tools. Don't
  set it unless the owner asks.

## What Search Console showed (export of Nov 12, 2026: Oct 17 to Nov 10)
- No figures are kept here: this file is public. For the next comparison ask the owner for a Performance export
  with the date range "Last 3 months"; its Chart sheet lists every day, so the trend can be read from it.
- Indexing is not the problem. 98 of 101 sitemap pages had impressions. The three without: `/stack/asana-and-slack/`
  and `/stack/salesforce-and-zendesk/` (live since Oct 19) and `/pipedrive-integrations-cost/` (new on Nov 3).
- Ranking is the limit. The average position sits around page 6 and did not move in three weeks, so clicks are
  negligible. Nearly nine in ten impressions come from "<tool> <tool> integration" searches, where the vendors'
  own pages hold page 1. Titles and headings already match those searches: more on-page work won't change this.
  The domain's age (first seen Oct 18) and the lack of links will.
- Where the site already sits on pages 2 to 4: pairs with little competition (Xero + ActiveCampaign, Intercom +
  Stripe, Zendesk + Stripe, ActiveCampaign + Stripe, Stripe + Mailchimp, Slack + Calendly, ActiveCampaign +
  Calendly, monday.com + Slack), the Salesforce hub and the CRM guide. Question-style cost searches and a few API
  pages reach page 1, with very few searches behind them.
- Impressions from page 6 and deeper are mostly not people (rank-checking tools page that deep). Judge progress by
  position and clicks, not by the impression count.
- Of the seven pairs without setup steps, ActiveCampaign + Stripe and ClickUp + Slack are the closest to page 1:
  ask for those two help texts first.

## Design (since Nov 11, 2026)
- Idea: a printed fare chart. White paper, navy ink, Barlow type, thin rules. The homepage opens with a chart of
  every pair's 10-seat cost.
- Yellow means one thing only: money the sticker price doesn't show (a forced upgrade or a connector fee).
- Skills used for it: `example-skills:frontend-design` and `ui-ux-pro-max`. Not done yet, on purpose: removing the
  "→" on link text and the "A · B · C" date lines (pairfix patterns depend on them; do it carefully or not at all).

## Decisions the owner has made
- Editor is shown as Rakesh Kumar, with LinkedIn and GitHub links and "five years of experience across SaaS tools,
  sales and marketing operations, digital marketing and SEO, and web development" (the owner's own words).
- HubSpot + Salesforce keeps the Salesforce API add-on in its total, with the note explaining HubSpot's wording.
- No imitation screenshots. Diagrams drawn from page facts are fine and are labelled as diagrams.
- Design choices are left to Claude's judgment.

## Still open
- Batch 2 candidates: the 77 empty cells. Left out of batch 1 for a reason: Zendesk + QuickBooks and Airtable + Calendly
  (no readable vendor page says whether a native integration exists; zendesk.com/marketplace has a bot check),
  Pipedrive + Stripe (third-party Marketplace apps, pricing not read), Asana + Intercom (asana.com/apps/intercom is 404),
  Notion + Salesforce (needs Notion Enterprise, which the site doesn't price). help.asana.com doesn't render here.
- Seven native pairs have no setup steps because their help centres can't be read: activecampaign-and-pipedrive,
  activecampaign-and-stripe, clickup-and-slack, clickup-and-zendesk, hubspot-and-clickup, hubspot-and-monday,
  monday-and-zendesk. The owner can paste the help text.
- Owner tasks: the GitHub repo description still says 59 integrations (now 76; update it after each batch); real
  screenshots from the free pairs; a fresh Search
  Console export in about a month ("Last 3 months"). The Google key only if the owner wants live access later.
- Optional, only if the owner asks: a short captioned video for the Integration Tax report.
- A monthly price-check task is scheduled for Dec 1.

## State (update this)
- Nov 11, 2026: PRs #24 to #29 are merged and live. #24 to #28: setup steps on 52 of 59 pairs, diagrams, editor
  background, question headings. #29: the redesign (theme, homepage chart, share images, icons, `build_all.sh`, this file).
- Checked after #29 went live: 20 of 20 sampled files match the repo, fonts load, no console errors, Lighthouse
  100 / 100 / 100 / 100 with CLS 0 on the homepage, a pair page and a hub.
- Nov 12, 2026: the owner asked for Search Console access through github.com/AminForou/mcp-gsc. The repo side is
  done in PR #30 (`.mcp.json`, `scripts/gsc_mcp.sh`; tested with a throwaway key in nine saved shapes, and the real
  server starts through the script and lists 21 tools). The owner then chose to skip the key ("leave it") and
  uploaded a Performance export instead, so the connection stays inactive: the server shows "failed to connect",
  which is expected, not a bug. The owner's steps for the key are in PR #30's description if it is wanted later.
- Nov 12, 2026: read the owner's Search Console export; the findings are in "What Search Console showed". No site
  change came out of it. Suggested to the owner: URL Inspection on the three pages without impressions, and
  getting the Integration Tax report mentioned on other sites, which is the lever the data points to.
- Nov 12, 2026: batch 1 of the grid expansion: 17 new pairs (15 native, 2 through Make), each read on the vendors' pages
  that day; pages say so where a vendor names no plan. Merged with the Search Console setup as PR #30 and live: 25 of 25
  sampled files match the repo, every new page returns 200, no console errors, fonts load, no overflow at phone width.
- `robots.txt` now also keeps crawlers away from `/CLAUDE.md` and `/.mcp.json`. GitHub Pages serves every file in
  the repository, so working files that sit in the root need a Disallow line (`/scripts/` already had one).
- Not re-audited since the redesign: the claude-seo "Visual" category (was 90). Worth one run when the owner asks
  for scores again; the other categories were not touched by the redesign.
