# StackCostMatrix: working memory for Claude

Read this first. It is the short version of what earlier sessions learned, so a new session doesn't have to
rediscover it. Details live in `scripts/README.md`. Update the "State" section at the end of each piece of work.

## What this is
- https://stackcostmatrix.com: an independent index of what B2B software integrations really cost.
- Static HTML, served by GitHub Pages straight from `main`. No build step, no framework.
- 59 pair pages (`stack/<a>-and-<b>/`), 17 tool hubs, 18 API pages, a research report, guides. 102 pages in all.

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
- Seven native pairs have no setup steps because their help centres can't be read: activecampaign-and-pipedrive,
  activecampaign-and-stripe, clickup-and-slack, clickup-and-zendesk, hubspot-and-clickup, hubspot-and-monday,
  monday-and-zendesk. The owner can paste the help text.
- Owner tasks: GitHub repo description, website and topics; real screenshots from the free pairs; the Google key
  for Search Console access (or, failing that, a Search Console export in late November).
- Optional, only if the owner asks: a short captioned video for the Integration Tax report.
- A monthly price-check task is scheduled for Dec 1.

## State (update this)
- Nov 11, 2026: PRs #24 to #29 are merged and live. #24 to #28: setup steps on 52 of 59 pairs, diagrams, editor
  background, question headings. #29: the redesign (theme, homepage chart, share images, icons, `build_all.sh`, this file).
- Checked after #29 went live: 20 of 20 sampled files match the repo, fonts load, no console errors, Lighthouse
  100 / 100 / 100 / 100 with CLS 0 on the homepage, a pair page and a hub.
- Nov 12, 2026: the owner asked for Search Console access through github.com/AminForou/mcp-gsc. The repo side is
  done in PR #30 (`.mcp.json`, `scripts/gsc_mcp.sh`; tested with a throwaway key in nine saved shapes, and the real
  server starts through the script and lists 21 tools). Waiting on the owner to create the Google service-account
  key, add it to Search Console as a user, and save it in the Default cloud environment. Until then the server
  shows "failed to connect": that is expected, not a bug.
- `robots.txt` now also keeps crawlers away from `/CLAUDE.md` and `/.mcp.json`. GitHub Pages serves every file in
  the repository, so working files that sit in the root need a Disallow line (`/scripts/` already had one).
- Not re-audited since the redesign: the claude-seo "Visual" category (was 90). Worth one run when the owner asks
  for scores again; the other categories were not touched by the redesign.
