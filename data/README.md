# StackCostMatrix open data

`integration-pairs.json` is the current data behind every calculator on https://stackcostmatrix.com, exported from the live pages:

- `tools`: each tool's plans with monthly-billing prices (USD), the vendor's annual-billing price where published, minimum seats and API access.
- `pairs`: all 55 integration pairs, with connection type (native or middleware), minimum plans, middleware fee, sync direction, the 10-seat monthly cost, what was verified and when, and the vendor sources behind each pair's "How it works" section.

Read the `notes` and each pair's `verification` field before reusing a figure: they say which prices are modeled assumptions and which facts are still pending a re-check.

**License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Reuse and adapt it, including commercially, as long as you credit StackCostMatrix and link to https://stackcostmatrix.com.

`database/seed.sql` and `site/src/data/` are older snapshots (before the November 3, 2026 update) and are kept for history only.
