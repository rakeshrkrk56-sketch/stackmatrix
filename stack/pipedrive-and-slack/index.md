# Pipedrive + Slack Integration (2026): How It Works, Setup & True Cost

> How the Pipedrive + Slack integration works, how to set it up, and the plans it needs: Pipedrive Growth + Slack Free, $390/mo for 10 seats.

Source page: https://stackcostmatrix.com/stack/pipedrive-and-slack/  
Publisher: StackCostMatrix · Editor: Rakesh Kumar · Data licence: CC BY 4.0 (credit StackCostMatrix and link to https://stackcostmatrix.com)

---

[Home](https://stackcostmatrix.com/) / Pipedrive + Slack 

Trap: Pipedrive sends Slack messages through its Automations feature, which is only on Growth and higher ($39/seat). Requires Pipedrive on the 'Growth' plan and Slack on the 'Free' plan.

Edited by [Rakesh Kumar](https://stackcostmatrix.com/about/#editor), founder of StackCostMatrix | Integration requirements and prices checked against official vendor docs · Nov 3, 2026 (Pipedrive prices: from an indexed copy of its pricing page) · Setup steps: Nov 10, 2026 | [Spot an outdated price? Report a correction →](mailto:admin@stackcostmatrix.com?subject=Price%20Correction)

## How the Pipedrive + Slack integration works

**Does Pipedrive integrate with Slack?** Yes, through Pipedrive's Automations: an automation can post to a Slack channel or send a direct message when something happens in Pipedrive, such as a new or won deal. Automations need Pipedrive Growth or higher.

Pipedrive connects to Slack through its Automations feature: after you authorize the Slack app, an automation can post to a Slack channel or send a direct message when something happens in Pipedrive, such as a new or won deal.

[Setup guide: Pipedrive: Automations Slack notifications ↗](https://support.pipedrive.com/en/article/workflow-automation-slack-notifications)

### How do you set up Pipedrive + Slack?

1. In Pipedrive, go to Tools and apps > Slack > Authorize Slack account.
2. Create an automation, pick a trigger such as a deal being won, and add a Slack notification action.
3. Choose a channel or a direct message, then pick the Pipedrive fields to include in the message.

Steps follow [Pipedrive's setup guide ↗](https://support.pipedrive.com/en/article/workflow-automation-slack-notifications), read Nov 10, 2026.

**Limitations:** Pipedrive says Automations are only available on Growth and higher plans (Advanced under its older plan names), so the cheapest Lite plan can't send Slack messages this way. Slack's free plan allows up to 10 app installations.

Sources (checked Nov 3, 2026; setup guide read again for the steps on Nov 10, 2026): [Pipedrive: Automations Slack notifications ↗](https://support.pipedrive.com/en/article/workflow-automation-slack-notifications) · [Slack: Free plan limits ↗](https://slack.com/help/articles/27204752526611-Feature-limitations-on-the-free-version-of-Slack)

*Interactive cost calculator: open the web page to change team size, billing and add-ons.*

## Default 10-seat TCO summary

**Native integration costs $390.00/mo ($4,680.00/yr)** for a 10-seat team —
Pipedrive 'Growth' ($390.00/mo) + Slack 'Free' ($0.00/mo),
no middleware required.
Alternative: skip the native tier upgrade and run via Make/Zapier middleware for ~$150.59/mo all-in (adds a third-party dependency).

 

## Native vs middleware for Pipedrive + Slack

The connector routes are cheaper on paper because they skip the forced plan upgrade. The trade-off: you swap the native connector for a third-party automation you build and maintain, sync stays 1-way per automation, and the connector bills by usage.

Chart: Pipedrive + Slack: monthly cost for 10 seats by route: Native connector $390.00; Make Core route $150.59; Zapier Professional route $169.99

Monthly cost for 10 seats by route, Pipedrive + Slack.

 

Integration routes compared for a 10-seat team

| Route | Plans | 10 seats / month | Sync |
| --- | --- | --- | --- |
| Native Pipedrive + Slack connector | Pipedrive 'Growth' + Slack 'Free' | $390.00 | 1-way (Pipedrive → Slack) |
| Make Core on the cheapest API plans | Pipedrive 'Lite' + Slack 'Free' + Make | $150.59 | 1-way per scenario |
| Zapier Professional on the cheapest API plans | Pipedrive 'Lite' + Slack 'Free' + Zapier | $169.99 | 1-way per Zap |

Connector prices are monthly-billing list prices: Zapier Professional $29.99 (zapier.com/pricing) and Make Core $10.59 (from third-party pricing reviews, because make.com blocks automated checks). Both bill by usage, so high volumes cost more.

Image: [Pipedrive + Slack integration cost summary: $390 a month for 10 seats, $250 of it is the hidden cost to connect; plans needed: Pipedrive Growth and Slack Free](https://stackcostmatrix.com/og/pipedrive-and-slack.jpg)

## ✓ Verified Vendor Facts

- **Plan prices:** from each vendor's pricing page; any exception is flagged next to the date at the top.
- **Required tiers:** 'Growth' / 'Free' — the minimum plans this integration needs.
- **API & webhook gates:** audited in official developer docs (see spec matrix).
- **Native app availability:** Native app available in vendor marketplace.

Last checked: Nov 3, 2026 (exceptions listed at the top) · Sources linked below.

## ! Hidden Cost Trap

Requires Pipedrive on the 'Growth' plan or higher — Requires Slack on the 'Free' plan or higher.

Pipedrive minimum tier
:   'Growth'

Slack minimum tier
:   'Free'

Middleware fee
:   None

The hidden cost is a forced plan upgrade: Pipedrive needs 'Growth', $250/mo more than 'Lite', its cheapest plan with API access. That adds $250/mo for 10 seats just to connect the two tools. Running the same connection through Make on the cheapest API plans would cost about $150.59/mo in total instead of $390/mo, but you'd give up the native connector.

 [Skip the native tier upgrade: connect Pipedrive + Slack via Make.com middleware instead](https://stackcostmatrix.com/go/make) 

Affiliate link — we may earn a commission at no extra cost to you.

## Side-by-side spec matrix

Side-by-side spec matrix

| Spec | Pipedrive | Slack |
| --- | --- | --- |
| Connection type | Native   Source: [Pipedrive docs ↗](https://developers.pipedrive.com/docs/api/v1) · [Slack docs ↗](https://api.slack.com/) · Verified Nov 3, 2026 | |
| Data sync direction | 1-way (Pipedrive → Slack) | |
| Setup time | Under 1 hour (difficulty 1/5) | |
| Native integration supported | Yes — official native app/connector | |
| API available (distinct from native app) | Yes  — API ≠ native UI; API enables custom/middleware builds Source: [Pipedrive API docs ↗](https://developers.pipedrive.com/docs/api/v1) · Verified Oct 17, 2026 | Yes  — API ≠ native UI; API enables custom/middleware builds Source: [Slack API docs ↗](https://api.slack.com/) · Verified Oct 17, 2026 |
| API access at required tier | Yes  ('Growth') 40 req/2 s · daily budget ×2 Source: [Pipedrive developers: Rate limiting ↗](https://pipedrive.readme.io/docs/core-api-concepts-rate-limiting) · Verified Nov 3, 2026 | Yes  ('Free') Source: [Slack developers: Incoming webhooks ↗](https://api.slack.com/messaging/webhooks) · Verified Nov 3, 2026 |
| Webhook support at required tier | Yes  ('Growth') Source: [Pipedrive: Automations webhook requests ↗](https://support.pipedrive.com/en/article/automations-webhook-requests) · Verified Nov 3, 2026 | Yes  ('Free') Incoming webhooks Source: [Slack developers: Incoming webhooks ↗](https://api.slack.com/messaging/webhooks) · Verified Nov 3, 2026 |

[Visit Pipedrive](https://stackcostmatrix.com/go/pipedrive)  [Visit Slack](https://stackcostmatrix.com/go/slack)

Some outbound links may earn us a referral commission at no extra cost to you. [Read our affiliate disclosure](https://stackcostmatrix.com/about/).

## Pipedrive + Slack integration: frequently asked questions

### What are the minimum plan tiers required for the Pipedrive + Slack integration?

To unlock the native integration, Pipedrive must be on the 'Growth' plan or higher and Slack must be on the 'Free' plan or higher. Pipedrive's cheapest plan with API access is 'Lite', so 'Growth' is a $250/mo upgrade at 10 seats.

### How much does the Pipedrive + Slack stack cost per month for a 10-person team?

At 10 seats with the required tiers (Pipedrive 'Growth' + Slack 'Free'), the stack costs $390.00 per month.

### Is the Pipedrive + Slack integration native, and would Make or Zapier be cheaper?

The Pipedrive + Slack connection is native — no third-party middleware subscription is required. Connecting through Make on the cheapest API plans would cost about $150.59/month in total instead of $390.00, but you'd replace the native connector with a third-party automation.

### What are the limitations of the Pipedrive + Slack integration?

Pipedrive says Automations are only available on Growth and higher plans (Advanced under its older plan names), so the cheapest Lite plan can't send Slack messages this way. Slack's free plan allows up to 10 app installations.

## Integrations related to Pipedrive + Slack

[All Pipedrive integrations →](https://stackcostmatrix.com/pipedrive-integrations-cost/) · [All Slack integrations →](https://stackcostmatrix.com/slack-integrations-cost/) · [Pipedrive API access by plan →](https://stackcostmatrix.com/pipedrive-api-access/) · [Slack API access by plan →](https://stackcostmatrix.com/slack-api-access/)

Part of our [CRM integration hidden-costs guide](https://stackcostmatrix.com/crm-integration-pricing-guide/).

[### Pipedrive + Calendly

Middleware](https://stackcostmatrix.com/stack/pipedrive-and-calendly/)[### Pipedrive + Mailchimp

Native](https://stackcostmatrix.com/stack/pipedrive-and-mailchimp/)[### Pipedrive + Xero

Middleware](https://stackcostmatrix.com/stack/pipedrive-and-xero/)[### Salesforce Sales Cloud + Slack

Native](https://stackcostmatrix.com/stack/salesforce-and-slack/)[### ActiveCampaign + Pipedrive

Native](https://stackcostmatrix.com/stack/activecampaign-and-pipedrive/)[### ClickUp + Slack

Native](https://stackcostmatrix.com/stack/clickup-and-slack/)

Last checked: Nov 3, 2026 (exceptions listed at the top)

## Verified sources

Every figure on this page links to its source below; prices that don't come straight from the vendor's page are flagged next to the date:

- [Pipedrive official pricing ↗](https://www.pipedrive.com/pricing)
- [Pipedrive API / developer docs ↗](https://developers.pipedrive.com/docs/api/v1)
- [Slack official pricing ↗](https://slack.com/pricing)
- [Slack API / developer docs ↗](https://api.slack.com/)
