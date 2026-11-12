# Xero + Slack Integration (2026): How It Works, Setup & True Cost

> How the Xero + Slack integration works, how to set it up, and the plans it needs: Xero Early + Slack Free, $37.59/mo for 10 seats.

Source page: https://stackcostmatrix.com/stack/xero-and-slack/  
Publisher: StackCostMatrix · Editor: Rakesh Kumar · Data licence: CC BY 4.0 (credit StackCostMatrix and link to https://stackcostmatrix.com)

---

[Home](https://stackcostmatrix.com/) / Xero + Slack 

There's no native Xero–Slack app: Xero's App Store shows third-party apps for Slack, such as Approveit, and Make Core can post a Slack message when a Xero invoice is created or updated. Requires Xero on the 'Early' plan and Slack on the 'Free' plan. Route it through Make Core ($10.59/mo, or $9/mo billed annually).

Edited by [Rakesh Kumar](https://stackcostmatrix.com/about/#editor), founder of StackCostMatrix | Integration requirements checked against official vendor docs · Nov 12, 2026 · Prices checked · Nov 3, 2026 (Make fee: $9 annual price Oct 17, 2026; $10.59 monthly price from third-party pricing reviews, Nov 3, 2026, as make.com blocks automated checks) · Setup steps: Nov 12, 2026 | [Spot an outdated price? Report a correction →](mailto:admin@stackcostmatrix.com?subject=Price%20Correction)

## How the Xero + Slack integration works

**Does Xero integrate with Slack?** Not natively. Searching Xero's App Store for Slack shows third-party apps such as Approveit, which handles approvals from Slack. Make or Zapier can connect the two, for example to post a Slack message for each new Xero invoice.

A Make scenario watches Xero, for example for new or updated invoices, and sends a message to a Slack channel with the invoice details. Each scenario runs one way; a scenario in the other direction could create a Xero record from a Slack message.

[Setup guide: Make: Xero app ↗](https://apps.make.com/xero)

Diagram of how Xero and Slack connect. Xero: Early plan · $27/mo for 10 seats. Slack: Free plan · $0/mo for 10 seats. Xero sends a trigger (new or updated invoice) to Make Core ($10.59/mo), which performs an action in Slack (post a message). Each automation runs one way.

Diagram: how Xero and Slack connect, through Make Core, shown with the example automation described above. Drawn from the facts on this page.

 

### How do you set up Xero + Slack?

1. Log in to Make, create a scenario and add the Xero module Watch Invoices as the trigger.
2. Connect Xero: click Create a connection, click Save and sign in to Xero if prompted. If the module has an instant tag, click Create a webhook first.
3. Add a Slack module that sends a message to a channel. Connect Slack: click Create a connection and, if asked, choose the Slack (user) or Slack (bot) connection type, then sign in.
4. Write the message with values from the Xero invoice.
5. Click Run once in the toolbar to test it, then activate the scenario with the ON/OFF button on its details page. It runs every 15 minutes by default; click Every 15 minutes on the toolbar to change that.

Steps follow [Make's setup guide ↗](https://apps.make.com/xero), read Nov 12, 2026.

**Limitations:** Each Make scenario runs one way. Make's Slack guide notes that Slack Watch modules only work with user connections, and that workspace owners can stop members from connecting apps that aren't in the Slack Marketplace, which Make isn't; ask an owner to allow it if the connection is blocked.

Sources (checked Nov 12, 2026): [Xero App Store: apps for Slack ↗](https://apps.xero.com/us/search?q=slack) · [Make: Xero app ↗](https://apps.make.com/xero) · [Make: Slack app ↗](https://apps.make.com/slack) · [Make Help: Active and inactive scenarios ↗](https://help.make.com/active-and-inactive-scenarios) · [Make Help: Schedule a scenario ↗](https://help.make.com/schedule-a-scenario)

*Interactive cost calculator: open the web page to change team size, billing and add-ons.*

## Default 10-seat TCO summary

**Middleware integration costs $37.59/mo ($451.08/yr)** for a 10-seat team —
Xero 'Early' ($27.00/mo) + Slack 'Free' ($0.00/mo)
+ $10.59/mo middleware. No native connector exists for this pair.

 

## Native vs middleware for Xero + Slack

There's no native Xero + Slack connector, so a connector such as Make or Zapier is the integration rather than an alternative. Each automation runs one way (a trigger in one tool, an action in the other), and the connector's bill grows with the number of tasks or operations you run.

Chart: Xero + Slack: monthly cost for 10 seats by route: Make Core (modeled here) $37.59; Zapier Professional instead $56.99

Monthly cost for 10 seats by route, Xero + Slack.

 

Integration routes compared for a 10-seat team

| Route | Plans | 10 seats / month | Sync |
| --- | --- | --- | --- |
| Make Core (modeled here) | Xero 'Early' + Slack 'Free' | $37.59 | 1-way per automation |
| Zapier Professional instead | Xero 'Early' + Slack 'Free' | $56.99 | 1-way per automation |

Connector prices are monthly-billing list prices: Zapier Professional $29.99 (zapier.com/pricing) and Make Core $10.59 (from third-party pricing reviews, because make.com blocks automated checks). Both bill by usage, so high volumes cost more.

Image: [Xero + Slack integration cost summary: $37.59 a month for 10 seats, $10.59 of it is the hidden cost to connect; plans needed: Xero Early and Slack Free](https://stackcostmatrix.com/og/xero-and-slack.jpg)

## ✓ Verified Vendor Facts

- **Plan prices:** from each vendor's pricing page; any exception is flagged next to the date at the top.
- **Required tiers:** 'Early' / 'Free' — the minimum plans this integration needs.
- **API & webhook gates:** audited in official developer docs (see spec matrix).
- **Native app availability:** No native app — connected via middleware.

Requirements checked: Nov 12, 2026; prices: Nov 3, 2026 (exceptions listed at the top) · Sources linked below.

## ! Hidden Cost Trap

Requires Xero on the 'Early' plan or higher — Requires Slack on the 'Free' plan or higher — Plus $10.59/month middleware on top of both tools.

Xero minimum tier
:   'Early'

Slack minimum tier
:   'Free'

Middleware fee
:   $10.59/mo

The hidden cost here is the connector: there's no native Xero + Slack app, so you pay for Make Core ($10.59/mo) on top of both tools.

 [Connect Xero + Slack via Make.com — the middleware this integration runs on](https://stackcostmatrix.com/go/make) 

Affiliate link — we may earn a commission at no extra cost to you.

## Side-by-side spec matrix

Side-by-side spec matrix

| Spec | Xero | Slack |
| --- | --- | --- |
| Connection type | Middleware   Source: [Xero docs ↗](https://developer.xero.com/) · [Slack docs ↗](https://api.slack.com/) · Verified Nov 12, 2026 | |
| Data sync direction | 1-way (trigger → action) | |
| Setup time | Under 1 hour (difficulty 1/5) | |
| Native integration supported | No — requires middleware (Zapier / Make) | |
| API available (distinct from native app) | Yes  — API ≠ native UI; API enables custom/middleware builds Source: [Xero API docs ↗](https://developer.xero.com/) · Verified Oct 17, 2026 | Yes  — API ≠ native UI; API enables custom/middleware builds Source: [Slack API docs ↗](https://api.slack.com/) · Verified Oct 17, 2026 |
| API access at required tier | Yes  ('Early') Limits set by the app's developer tier Source: [Xero developers: Pricing and tiers ↗](https://developer.xero.com/pricing) · Verified Nov 3, 2026 | Yes  ('Free') Source: [Slack developers: Incoming webhooks ↗](https://api.slack.com/messaging/webhooks) · Verified Nov 3, 2026 |
| Webhook support at required tier | Yes  ('Early') No plan requirement in Xero's webhook docs Source: [Xero developers: Webhooks ↗](https://developer.xero.com/documentation/guides/webhooks/overview) · Verified Nov 3, 2026 | Yes  ('Free') Incoming webhooks Source: [Slack developers: Incoming webhooks ↗](https://api.slack.com/messaging/webhooks) · Verified Nov 3, 2026 |

[Visit Xero](https://stackcostmatrix.com/go/xero)  [Visit Slack](https://stackcostmatrix.com/go/slack)

Some outbound links may earn us a referral commission at no extra cost to you. [Read our affiliate disclosure](https://stackcostmatrix.com/about/).

## Xero + Slack integration: frequently asked questions

### What are the minimum plan tiers required for the Xero + Slack integration?

To unlock the integration, Xero must be on the 'Early' plan or higher and Slack must be on the 'Free' plan or higher. Those are each tool's cheapest plan with API access (Xero 'Early' at $27/mo and Slack 'Free' at $0/mo for 10 seats), so the integration doesn't force an upgrade.

### How much does the Xero + Slack stack cost per month for a 10-person team?

At 10 seats with the required tiers (Xero 'Early' + Slack 'Free' + $10.59/month middleware), the stack costs $37.59 per month.

### Why does Xero + Slack need middleware, and what does it cost?

The Xero + Slack connection runs through middleware: neither vendor offers a native app for this pair, so this page models Make Core at $10.59 per month on top of both tools. Sync is one-way (a trigger in one tool runs an action in the other).

### What are the limitations of the Xero + Slack integration?

Each Make scenario runs one way. Make's Slack guide notes that Slack Watch modules only work with user connections, and that workspace owners can stop members from connecting apps that aren't in the Slack Marketplace, which Make isn't; ask an owner to allow it if the connection is blocked.

## Integrations related to Xero + Slack

[All Xero integrations →](https://stackcostmatrix.com/xero-integrations-cost/) · [All Slack integrations →](https://stackcostmatrix.com/slack-integrations-cost/) · [Xero API access by plan →](https://stackcostmatrix.com/xero-api-access/) · [Slack API access by plan →](https://stackcostmatrix.com/slack-api-access/)

[### HubSpot + Xero

Native](https://stackcostmatrix.com/stack/hubspot-and-xero/)[### Pipedrive + Xero

Middleware](https://stackcostmatrix.com/stack/pipedrive-and-xero/)[### Salesforce + Xero

Middleware](https://stackcostmatrix.com/stack/salesforce-and-xero/)[### Stripe + Xero

Native](https://stackcostmatrix.com/stack/stripe-and-xero/)[### Xero + ActiveCampaign

Middleware](https://stackcostmatrix.com/stack/xero-and-activecampaign/)[### Xero + Calendly

Middleware](https://stackcostmatrix.com/stack/xero-and-calendly/)

Requirements checked: Nov 12, 2026; prices: Nov 3, 2026 (exceptions listed at the top)

## Verified sources

Every figure on this page links to its source below; prices that don't come straight from the vendor's page are flagged next to the date:

- [Xero official pricing ↗](https://www.xero.com/pricing/)
- [Xero API / developer docs ↗](https://developer.xero.com/)
- [Slack official pricing ↗](https://slack.com/pricing)
- [Slack API / developer docs ↗](https://api.slack.com/)
