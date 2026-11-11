# Notion + Calendly Integration Cost (2026): True Price, Minimum Plan & Hidden API Fees

> Notion + Calendly runs via middleware (+$10.59/mo) on Notion Plus and Calendly Standard: $250.59/mo for 10 seats.

Source page: https://stackcostmatrix.com/stack/notion-and-calendly/  
Publisher: StackCostMatrix · Editor: Rakesh Kumar · Data licence: CC BY 4.0 (credit StackCostMatrix and link to https://stackcostmatrix.com)

---

[Home](https://stackcostmatrix.com/) / Notion + Calendly 

Notion can embed Calendly booking pages, but there's no native sync; logging bookings in Notion needs Make or Zapier, and Calendly webhooks need its Standard plan. Requires Notion on the 'Plus' plan and Calendly on the 'Standard' plan. Route it through Make Core ($10.59/mo, or $9/mo billed annually).

Edited by [Rakesh Kumar](https://stackcostmatrix.com/about/#editor), founder of StackCostMatrix | Integration requirements and prices checked against official vendor docs · Nov 3, 2026 (Make fee: $9 annual price Oct 17, 2026; $10.59 monthly price from third-party pricing reviews, Nov 3, 2026, as make.com blocks automated checks) · Setup steps: Nov 11, 2026 | [Spot an outdated price? Report a correction →](mailto:admin@stackcostmatrix.com?subject=Price%20Correction)

## How the Notion + Calendly integration works

Notion's Calendly integration lets you paste a Calendly booking page link into Notion and embed it, so teammates or clients can book time from a Notion page.

Diagram of how Notion and Calendly connect. Calendly: Standard plan · $120/mo for 10 seats. Notion: Plus plan · $120/mo for 10 seats. Calendly sends a trigger (meeting booked) to Make Core ($10.59/mo), which performs an action in Notion (log it in a database). Each automation runs one way.

Diagram: how Notion and Calendly connect, through Make Core, shown with the example automation described above. Drawn from the facts on this page.

 

### How do you set up Notion + Calendly?

1. Log in to Make, create a scenario and add the Calendly module Watch events as the trigger.
2. Connect Calendly: click Create a connection, click Save and sign in to Calendly if prompted. If the module has an instant tag, click Create a webhook first.
3. Add a Notion module that creates a database item. Connect Notion: click Create a connection, choose Notion Internal as the connection type, paste the internal integration token from your Notion account and click Save. In Notion, add the databases Make should see to that integration.
4. Fill in the database item's properties with values from the Calendly event.
5. Click Run once in the toolbar to test it, then activate the scenario with the ON/OFF button on its details page. It runs every 15 minutes by default; click Every 15 minutes on the toolbar to change that.

Steps follow [Make's setup guide ↗](https://apps.make.com/calendly), read Nov 11, 2026.

**Limitations:** Embedding doesn't sync bookings. Logging meetings in a Notion database needs Make or Zapier, and Calendly's webhooks need a paid Calendly plan from Standard up.

[Setup guide: Make: Calendly app ↗](https://apps.make.com/calendly)

Sources (checked Nov 3, 2026; Make's guides for the steps read on Nov 11, 2026): [Notion: Calendly integration ↗](https://www.notion.com/integrations/calendly) · [Calendly: API overview ↗](https://calendly.com/help/calendly-api-overview) · [Make: Calendly app ↗](https://apps.make.com/calendly) · [Make: Notion app ↗](https://apps.make.com/notion) · [Make Help: Active and inactive scenarios ↗](https://help.make.com/active-and-inactive-scenarios) · [Make Help: Schedule a scenario ↗](https://help.make.com/schedule-a-scenario)

*Interactive cost calculator: open the web page to change team size, billing and add-ons.*

## Default 10-seat TCO summary

**Middleware integration costs $250.59/mo ($3,007.08/yr)** for a 10-seat team —
Notion 'Plus' ($120.00/mo) + Calendly 'Standard' ($120.00/mo)
+ $10.59/mo middleware. No native connector exists for this pair.

 

## Native vs middleware for Notion + Calendly

There's no native Notion + Calendly connector, so a connector such as Make or Zapier is the integration rather than an alternative. Each automation runs one way (a trigger in one tool, an action in the other), and the connector's bill grows with the number of tasks or operations you run.

Chart: Notion + Calendly: monthly cost for 10 seats by route: Make Core (modeled here) $250.59; Zapier Professional instead $269.99

Monthly cost for 10 seats by route, Notion + Calendly.

 

Integration routes compared for a 10-seat team

| Route | Plans | 10 seats / month | Sync |
| --- | --- | --- | --- |
| Make Core (modeled here) | Notion 'Plus' + Calendly 'Standard' | $250.59 | 1-way per automation |
| Zapier Professional instead | Notion 'Plus' + Calendly 'Standard' | $269.99 | 1-way per automation |

Connector prices are monthly-billing list prices: Zapier Professional $29.99 (zapier.com/pricing) and Make Core $10.59 (from third-party pricing reviews, because make.com blocks automated checks). Both bill by usage, so high volumes cost more.

Image: [Notion + Calendly integration cost summary: $250.59 a month for 10 seats, $10.59 of it is the hidden cost to connect; plans needed: Notion Plus and Calendly Standard](https://stackcostmatrix.com/og/notion-and-calendly.jpg)

## ✓ Verified Vendor Facts

- **Plan prices:** from each vendor's pricing page; any exception is flagged next to the date at the top.
- **Required tiers:** 'Plus' / 'Standard' — the minimum plans this integration needs.
- **API & webhook gates:** audited in official developer docs (see spec matrix).
- **Native app availability:** No native app — connected via middleware.

Last checked: Nov 3, 2026 (exceptions listed at the top) · Sources linked below.

## ! Hidden Cost Trap

Requires Notion on the 'Plus' plan or higher — Requires Calendly on the 'Standard' plan or higher — Plus $10.59/month middleware on top of both tools.

Notion minimum tier
:   'Plus'

Calendly minimum tier
:   'Standard'

Middleware fee
:   $10.59/mo

The hidden cost here is the connector: there's no native Notion + Calendly app, so you pay for Make Core ($10.59/mo) on top of both tools.

 [Connect Notion + Calendly via Make.com — the middleware this integration runs on](https://stackcostmatrix.com/go/make) 

Affiliate link — we may earn a commission at no extra cost to you.

## Side-by-side spec matrix

Side-by-side spec matrix

| Spec | Notion | Calendly |
| --- | --- | --- |
| Connection type | Middleware   Source: [Notion docs ↗](https://developers.notion.com/) · [Calendly docs ↗](https://developer.calendly.com/) · Verified Nov 3, 2026 | |
| Data sync direction | 1-way (trigger → action) | |
| Setup time | Under 1 hour (difficulty 1/5) | |
| Native integration supported | No — requires middleware (Zapier / Make) | |
| API available (distinct from native app) | Yes  — API ≠ native UI; API enables custom/middleware builds Source: [Notion API docs ↗](https://developers.notion.com/) · Verified Oct 17, 2026 | Yes  — API ≠ native UI; API enables custom/middleware builds Source: [Calendly API docs ↗](https://developer.calendly.com/) · Verified Oct 17, 2026 |
| API access at required tier | Yes  ('Plus') Source: [Notion developers: Webhooks ↗](https://developers.notion.com/reference/webhooks) · Verified Nov 3, 2026 | Yes  ('Standard') Source: [Calendly: API overview ↗](https://calendly.com/help/calendly-api-overview) · Verified Nov 3, 2026 |
| Webhook support at required tier | Yes  ('Plus') Source: [Notion developers: Webhooks ↗](https://developers.notion.com/reference/webhooks) · Verified Nov 3, 2026 | Yes  ('Standard') Source: [Calendly: API overview ↗](https://calendly.com/help/calendly-api-overview) · Verified Nov 3, 2026 |

[Visit Notion](https://stackcostmatrix.com/go/notion)  [Visit Calendly](https://stackcostmatrix.com/go/calendly)

Some outbound links may earn us a referral commission at no extra cost to you. [Read our affiliate disclosure](https://stackcostmatrix.com/about/).

## Notion + Calendly integration: frequently asked questions

### What are the minimum plan tiers required for the Notion + Calendly integration?

To unlock the integration, Notion must be on the 'Plus' plan or higher and Calendly must be on the 'Standard' plan or higher. Those are each tool's cheapest plan with API access (Notion 'Plus' at $120/mo and Calendly 'Standard' at $120/mo for 10 seats), so the integration doesn't force an upgrade.

### How much does the Notion + Calendly stack cost per month for a 10-person team?

At 10 seats with the required tiers (Notion 'Plus' + Calendly 'Standard' + $10.59/month middleware), the stack costs $250.59 per month.

### Why does Notion + Calendly need middleware, and what does it cost?

The Notion + Calendly connection runs through middleware: neither vendor offers a native app for this pair, so this page models Make Core at $10.59 per month on top of both tools. Sync is one-way (a trigger in one tool runs an action in the other).

### What are the limitations of the Notion + Calendly integration?

Embedding doesn't sync bookings. Logging meetings in a Notion database needs Make or Zapier, and Calendly's webhooks need a paid Calendly plan from Standard up.

## Integrations related to Notion + Calendly

[All Notion integrations →](https://stackcostmatrix.com/notion-integrations-cost/) · [All Calendly integrations →](https://stackcostmatrix.com/calendly-integrations-cost/) · [Notion API access by plan →](https://stackcostmatrix.com/notion-api-access/) · [Calendly API access by plan →](https://stackcostmatrix.com/calendly-api-access/)

[### HubSpot + Calendly

Native](https://stackcostmatrix.com/stack/hubspot-and-calendly/)[### Mailchimp + Calendly

Native](https://stackcostmatrix.com/stack/mailchimp-and-calendly/)[### Slack + Calendly

Native](https://stackcostmatrix.com/stack/slack-and-calendly/)[### Slack + Notion

Native](https://stackcostmatrix.com/stack/slack-and-notion/)[### Notion + Stripe

Middleware](https://stackcostmatrix.com/stack/notion-and-stripe/)[### Zendesk + Notion

Middleware](https://stackcostmatrix.com/stack/zendesk-and-notion/)

Last checked: Nov 3, 2026 (exceptions listed at the top)

## Verified sources

Every figure on this page links to its source below; prices that don't come straight from the vendor's page are flagged next to the date:

- [Notion official pricing ↗](https://www.notion.so/pricing)
- [Notion API / developer docs ↗](https://developers.notion.com/)
- [Calendly official pricing ↗](https://calendly.com/pricing)
- [Calendly API / developer docs ↗](https://developer.calendly.com/)
