# Slack + Intercom Integration (2026): How It Works, Setup & True Cost

> How the Slack + Intercom integration works, how to set it up, and the plans it needs: Slack Free + Intercom Essential, $390/mo for 10 seats.

Source page: https://stackcostmatrix.com/stack/slack-and-intercom/  
Publisher: StackCostMatrix · Editor: Rakesh Kumar · Data licence: CC BY 4.0 (credit StackCostMatrix and link to https://stackcostmatrix.com)

---

[Home](https://stackcostmatrix.com/) / Slack + Intercom 

Intercom's native Slack integration is on every Intercom plan and works with Slack's free plan, but automatic Slack alerts for new conversations need Intercom Advanced. Requires Slack on the 'Free' plan and Intercom on the 'Essential' plan.

Edited by [Rakesh Kumar](https://stackcostmatrix.com/about/#editor), founder of StackCostMatrix | Integration requirements and prices checked against official vendor docs · Nov 3, 2026 | [Spot an outdated price? Report a correction →](mailto:admin@stackcostmatrix.com?subject=Price%20Correction)

## How the Slack + Intercom integration works

Intercom's native Slack integration lets you connect Slack as a channel in Intercom, so your team can handle conversations and tickets that start in Slack. Intercom says it's available on all of its helpdesk plans.

[Setup guide: Intercom: Connect your Slack channel ↗](https://www.intercom.com/help/en/articles/11534476-connect-your-slack-channel)

**Limitations:** Automatic Slack notifications for new conversations rely on Workflows, which are only on Intercom's Advanced and Expert plans, not Essential. Slack's free plan allows only 10 apps, and the app can't be installed in the primary workspace of a Slack Enterprise Grid account.

Sources (checked Nov 3, 2026): [Intercom: Connect your Slack channel ↗](https://www.intercom.com/help/en/articles/11534476-connect-your-slack-channel) · [Slack: Free plan limits ↗](https://slack.com/help/articles/27204752526611-Feature-limitations-on-the-free-version-of-Slack)

*Interactive cost calculator: open the web page to change team size, billing and add-ons.*

## Default 10-seat TCO summary

**Native integration costs $390.00/mo ($4,680.00/yr)** for a 10-seat team —
Slack 'Free' ($0.00/mo) + Intercom 'Essential' ($390.00/mo),
no middleware required.
Middleware via Make/Zapier would add ~$10.59/mo on top of the cheapest API-capable tiers ($400.59/mo all-in) — the native path is cheaper.

 

## Native vs middleware for Slack + Intercom

The native connector is the cheapest route here and the only one with 2-way sync. Make or Zapier only makes sense if you already run other automations through it, or need a step the native app doesn't offer.

Chart: Slack + Intercom: monthly cost for 10 seats by route: Native connector $390.00; Make Core route $400.59; Zapier Professional route $419.99

Monthly cost for 10 seats by route, Slack + Intercom.

 

Integration routes compared for a 10-seat team

| Route | Plans | 10 seats / month | Sync |
| --- | --- | --- | --- |
| Native Slack + Intercom connector | Slack 'Free' + Intercom 'Essential' | $390.00 | 2-way |
| Make Core on the cheapest API plans | Slack 'Free' + Intercom 'Essential' + Make | $400.59 | 1-way per scenario |
| Zapier Professional on the cheapest API plans | Slack 'Free' + Intercom 'Essential' + Zapier | $419.99 | 1-way per Zap |

Connector prices are monthly-billing list prices: Zapier Professional $29.99 (zapier.com/pricing) and Make Core $10.59 (from third-party pricing reviews, because make.com blocks automated checks). Both bill by usage, so high volumes cost more.

Image: [Slack + Intercom integration cost summary: $390 a month for 10 seats, nothing extra to connect; plans needed: Slack Free and Intercom Essential](https://stackcostmatrix.com/og/slack-and-intercom.jpg)

## ✓ Verified Vendor Facts

- **Plan prices:** from each vendor's pricing page; any exception is flagged next to the date at the top.
- **Required tiers:** 'Free' / 'Essential' — the minimum plans this integration needs.
- **API & webhook gates:** audited in official developer docs (see spec matrix).
- **Native app availability:** Native app available in vendor marketplace.

Last checked: Nov 3, 2026 · Sources linked below.

## ! Plan requirements

Requires Slack on the 'Free' plan or higher — Requires Intercom on the 'Essential' plan or higher.

Slack minimum tier
:   'Free'

Intercom minimum tier
:   'Essential'

Middleware fee
:   None

No hidden cost: the native connector works on Slack 'Free' and Intercom 'Essential', so connecting them adds nothing to what you already pay for the two tools.

## Side-by-side spec matrix

Side-by-side spec matrix

| Spec | Slack | Intercom |
| --- | --- | --- |
| Connection type | Native   Source: [Slack docs ↗](https://api.slack.com/) · [Intercom docs ↗](https://developers.intercom.com/) · Verified Nov 3, 2026 | |
| Data sync direction | 2-way | |
| Setup time | Under 1 hour (difficulty 1/5) | |
| Native integration supported | Yes — official native app/connector | |
| API available (distinct from native app) | Yes  — API ≠ native UI; API enables custom/middleware builds Source: [Slack API docs ↗](https://api.slack.com/) · Verified Oct 17, 2026 | Yes  — API ≠ native UI; API enables custom/middleware builds Source: [Intercom API docs ↗](https://developers.intercom.com/) · Verified Oct 17, 2026 |
| API access at required tier | Yes  ('Free') Source: [Slack developers: Incoming webhooks ↗](https://api.slack.com/messaging/webhooks) · Verified Nov 3, 2026 | Yes  ('Essential') Paid workspaces Source: [Intercom developers: Webhooks ↗](https://developers.intercom.com/docs/webhooks) · Verified Nov 3, 2026 |
| Webhook support at required tier | Yes  ('Free') Incoming webhooks Source: [Slack developers: Incoming webhooks ↗](https://api.slack.com/messaging/webhooks) · Verified Nov 3, 2026 | Yes  ('Essential') Source: [Intercom developers: Webhooks ↗](https://developers.intercom.com/docs/webhooks) · Verified Nov 3, 2026 |

[Visit Slack](https://stackcostmatrix.com/go/slack)  [Visit Intercom](https://stackcostmatrix.com/go/intercom)

Some outbound links may earn us a referral commission at no extra cost to you. [Read our affiliate disclosure](https://stackcostmatrix.com/about/).

## Slack + Intercom integration: frequently asked questions

### What are the minimum plan tiers required for the Slack + Intercom integration?

To unlock the native integration, Slack must be on the 'Free' plan or higher and Intercom must be on the 'Essential' plan or higher. Those are each tool's cheapest plan with API access (Slack 'Free' at $0/mo and Intercom 'Essential' at $390/mo for 10 seats), so the integration doesn't force an upgrade.

### How much does the Slack + Intercom stack cost per month for a 10-person team?

At 10 seats with the required tiers (Slack 'Free' + Intercom 'Essential'), the stack costs $390.00 per month.

### Is the Slack + Intercom integration native, and would Make or Zapier be cheaper?

The Slack + Intercom connection is native — no third-party middleware subscription is required. Make would cost about $400.59/month on the cheapest API plans, more than the native route, so it only makes sense if you already use it.

### What are the limitations of the Slack + Intercom integration?

Automatic Slack notifications for new conversations rely on Workflows, which are only on Intercom's Advanced and Expert plans, not Essential. Slack's free plan allows only 10 apps, and the app can't be installed in the primary workspace of a Slack Enterprise Grid account.

## Integrations related to Slack + Intercom

[All Slack integrations →](https://stackcostmatrix.com/slack-integrations-cost/) · [All Intercom integrations →](https://stackcostmatrix.com/intercom-integrations-cost/) · [Slack API access by plan →](https://stackcostmatrix.com/slack-api-access/) · [Intercom API access by plan →](https://stackcostmatrix.com/intercom-api-access/)

[### Pipedrive + Slack

Native](https://stackcostmatrix.com/stack/pipedrive-and-slack/)[### Freshdesk + Slack

Native](https://stackcostmatrix.com/stack/freshdesk-and-slack/)[### QuickBooks Online + Slack

Middleware](https://stackcostmatrix.com/stack/quickbooks-and-slack/)[### Slack + Airtable

Native](https://stackcostmatrix.com/stack/slack-and-airtable/)[### Slack + Calendly

Native](https://stackcostmatrix.com/stack/slack-and-calendly/)[### Slack + Zendesk

Native](https://stackcostmatrix.com/stack/slack-and-zendesk/)

Last checked: Nov 3, 2026

## Verified sources

Every figure on this page links to its source below; prices that don't come straight from the vendor's page are flagged next to the date:

- [Slack official pricing ↗](https://slack.com/pricing)
- [Slack API / developer docs ↗](https://api.slack.com/)
- [Intercom official pricing ↗](https://www.intercom.com/pricing)
- [Intercom API / developer docs ↗](https://developers.intercom.com/)
