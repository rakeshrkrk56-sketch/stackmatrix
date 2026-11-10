# Slack + Airtable Integration (2026): How It Works, Setup & True Cost

> How the Slack + Airtable integration works, how to set it up, and the plans it needs: Slack Free + Airtable Free, $0/mo for 10 seats.

Source page: https://stackcostmatrix.com/stack/slack-and-airtable/  
Publisher: StackCostMatrix · Editor: Rakesh Kumar · Data licence: CC BY 4.0 (credit StackCostMatrix and link to https://stackcostmatrix.com)

---

[Home](https://stackcostmatrix.com/) / Slack + Airtable 

Airtable's Slack features work on all Airtable plan types, including Free, and on Slack's free plan. Requires Slack on the 'Free' plan and Airtable on the 'Free' plan.

Edited by [Rakesh Kumar](https://stackcostmatrix.com/about/#editor), founder of StackCostMatrix | Integration requirements and prices checked against official vendor docs · Nov 3, 2026 | [Spot an outdated price? Report a correction →](mailto:admin@stackcostmatrix.com?subject=Price%20Correction)

## How the Slack + Airtable integration works

In an Airtable base, open the base menu and choose Slack notifications, then create rules that post to a Slack channel when the base changes, or when specific records or views change. You can make as many rules as you need, so different bases can notify different channels.

[Setup guide: Airtable support: Base activity notifications in Slack ↗](https://support.airtable.com/docs/receiving-base-activity-notifications-in-slack)

### How to set it up

1. Open the Airtable base you want notifications from.
2. Click the drop-down arrow next to the base name, then the ellipsis (…) icon, and select Slack notifications.
3. Choose the base to post updates from and the Slack channel to post them to.
4. Click Allow if an authorization window appears.
5. Send a test message from the rule, or change something in the base and watch the channel for the update.

Steps follow [Airtable's setup guide ↗](https://support.airtable.com/docs/receiving-base-activity-notifications-in-slack), read Nov 10, 2026.

**Limitations:** It's one-way (Airtable → Slack) and only posts notifications. Your organization's admins can block the integration, and only the person who set up a rule can turn it off.

Sources (checked Nov 8, 2026): [Airtable support: Base activity notifications in Slack ↗](https://support.airtable.com/docs/receiving-base-activity-notifications-in-slack)

*Interactive cost calculator: open the web page to change team size, billing and add-ons.*

## Default 10-seat TCO summary

**Native integration costs $0.00/mo ($0.00/yr)** for a 10-seat team —
Slack 'Free' ($0.00/mo) + Airtable 'Free' ($0.00/mo),
no middleware required.
Middleware via Make/Zapier would add ~$10.59/mo on top of the cheapest API-capable tiers ($10.59/mo all-in) — the native path is cheaper.

 

## Native vs middleware for Slack + Airtable

The native connector is the cheapest route here. Make or Zapier only makes sense if you already run other automations through it, or need a step the native app doesn't offer.

Chart: Slack + Airtable: monthly cost for 10 seats by route: Native connector $0.00; Make Core route $10.59; Zapier Professional route $29.99

Monthly cost for 10 seats by route, Slack + Airtable.

 

Integration routes compared for a 10-seat team

| Route | Plans | 10 seats / month | Sync |
| --- | --- | --- | --- |
| Native Slack + Airtable connector | Slack 'Free' + Airtable 'Free' | $0.00 | 1-way (Airtable → Slack) |
| Make Core on the cheapest API plans | Slack 'Free' + Airtable 'Free' + Make | $10.59 | 1-way per scenario |
| Zapier Professional on the cheapest API plans | Slack 'Free' + Airtable 'Free' + Zapier | $29.99 | 1-way per Zap |

Connector prices are monthly-billing list prices: Zapier Professional $29.99 (zapier.com/pricing) and Make Core $10.59 (from third-party pricing reviews, because make.com blocks automated checks). Both bill by usage, so high volumes cost more.

Image: [Slack + Airtable integration cost summary: $0 a month for 10 seats, nothing extra to connect; plans needed: Slack Free and Airtable Free](https://stackcostmatrix.com/og/slack-and-airtable.jpg)

## ✓ Verified Vendor Facts

- **Plan prices:** from each vendor's pricing page; any exception is flagged next to the date at the top.
- **Required tiers:** 'Free' / 'Free' — the minimum plans this integration needs.
- **API & webhook gates:** audited in official developer docs (see spec matrix).
- **Native app availability:** Native app available in vendor marketplace.

Last checked: Nov 3, 2026 · Sources linked below.

## ! Plan requirements

Requires Slack on the 'Free' plan or higher — Requires Airtable on the 'Free' plan or higher.

Slack minimum tier
:   'Free'

Airtable minimum tier
:   'Free'

Middleware fee
:   None

No hidden cost: the native connector works on Slack 'Free' and Airtable 'Free', so connecting them adds nothing to what you already pay for the two tools.

## Side-by-side spec matrix

Side-by-side spec matrix

| Spec | Slack | Airtable |
| --- | --- | --- |
| Connection type | Native   Source: [Slack docs ↗](https://api.slack.com/) · [Airtable docs ↗](https://airtable.com/developers/web/api/introduction) · Verified Nov 3, 2026 | |
| Data sync direction | 1-way (Airtable → Slack) | |
| Setup time | Under 1 hour (difficulty 1/5) | |
| Native integration supported | Yes — official native app/connector | |
| API available (distinct from native app) | Yes  — API ≠ native UI; API enables custom/middleware builds Source: [Slack API docs ↗](https://api.slack.com/) · Verified Oct 17, 2026 | Yes  — API ≠ native UI; API enables custom/middleware builds Source: [Airtable API docs ↗](https://airtable.com/developers/web/api/introduction) · Verified Oct 17, 2026 |
| API access at required tier | Yes  ('Free') Source: [Slack developers: Incoming webhooks ↗](https://api.slack.com/messaging/webhooks) · Verified Nov 3, 2026 | Yes  ('Free') 1,000 API calls a month Source: [Airtable: Managing API call limits ↗](https://support.airtable.com/articles/7735693959-managing-api-call-limits-in-airtable) · Verified Nov 3, 2026 |
| Webhook support at required tier | Yes  ('Free') Incoming webhooks Source: [Slack developers: Incoming webhooks ↗](https://api.slack.com/messaging/webhooks) · Verified Nov 3, 2026 | Yes  ('Free') Source: [Airtable: Create a webhook ↗](https://airtable.com/developers/web/api/create-a-webhook) · Verified Nov 3, 2026 |

[Visit Slack](https://stackcostmatrix.com/go/slack)  [Visit Airtable](https://stackcostmatrix.com/go/airtable)

Some outbound links may earn us a referral commission at no extra cost to you. [Read our affiliate disclosure](https://stackcostmatrix.com/about/).

## Slack + Airtable integration: frequently asked questions

### What are the minimum plan tiers required for the Slack + Airtable integration?

To unlock the native integration, Slack must be on the 'Free' plan or higher and Airtable must be on the 'Free' plan or higher. Those are each tool's cheapest plan with API access (Slack 'Free' at $0/mo and Airtable 'Free' at $0/mo for 10 seats), so the integration doesn't force an upgrade.

### How much does the Slack + Airtable stack cost per month for a 10-person team?

At 10 seats with the required tiers (Slack 'Free' + Airtable 'Free'), the stack costs $0.00 per month.

### Is the Slack + Airtable integration native, and would Make or Zapier be cheaper?

The Slack + Airtable connection is native — no third-party middleware subscription is required. Make would cost about $10.59/month on the cheapest API plans, more than the native route, so it only makes sense if you already use it.

### What are the limitations of the Slack + Airtable integration?

It's one-way (Airtable → Slack) and only posts notifications. Your organization's admins can block the integration, and only the person who set up a rule can turn it off.

## Integrations related to Slack + Airtable

[All Slack integrations →](https://stackcostmatrix.com/slack-integrations-cost/) · [All Airtable integrations →](https://stackcostmatrix.com/airtable-integrations-cost/) · [Slack API access by plan →](https://stackcostmatrix.com/slack-api-access/) · [Airtable API access by plan →](https://stackcostmatrix.com/airtable-api-access/)

[### Airtable + QuickBooks Online

Middleware](https://stackcostmatrix.com/stack/airtable-and-quickbooks/)[### Airtable + Stripe

Middleware](https://stackcostmatrix.com/stack/airtable-and-stripe/)[### Mailchimp + Airtable

Middleware](https://stackcostmatrix.com/stack/mailchimp-and-airtable/)[### Slack + Calendly

Native](https://stackcostmatrix.com/stack/slack-and-calendly/)[### Slack + Intercom

Native](https://stackcostmatrix.com/stack/slack-and-intercom/)[### Slack + Notion

Native](https://stackcostmatrix.com/stack/slack-and-notion/)

Last checked: Nov 3, 2026

## Verified sources

Every figure on this page links to its source below; prices that don't come straight from the vendor's page are flagged next to the date:

- [Slack official pricing ↗](https://slack.com/pricing)
- [Slack API / developer docs ↗](https://api.slack.com/)
- [Airtable official pricing ↗](https://www.airtable.com/pricing)
- [Airtable API / developer docs ↗](https://airtable.com/developers/web/api/introduction)
