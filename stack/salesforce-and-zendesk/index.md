# Salesforce Sales Cloud + Zendesk Integration (2026): How It Works, Setup & True Cost

> How the Salesforce Sales Cloud + Zendesk integration works and how to set it up, plus the plans it needs and the 10-seat cost ($1,940/mo).

Source page: https://stackcostmatrix.com/stack/salesforce-and-zendesk/  
Publisher: StackCostMatrix · Editor: Rakesh Kumar · Data licence: CC BY 4.0 (credit StackCostMatrix and link to https://stackcostmatrix.com)

---

[Home](https://stackcostmatrix.com/) / Salesforce Sales Cloud + Zendesk 

Zendesk's Salesforce integration works on every Zendesk Suite plan from Team up, but Salesforce Professional still needs the $25/user API add-on. Requires Salesforce Sales Cloud on the 'Professional' plan and Zendesk on the 'Suite Team' plan.

Edited by [Rakesh Kumar](https://stackcostmatrix.com/about/#editor), founder of StackCostMatrix | Integration requirements and prices checked against official vendor docs · Nov 3, 2026 (Salesforce prices: Oct 17, 2026) | [Spot an outdated price? Report a correction →](mailto:admin@stackcostmatrix.com?subject=Price%20Correction)

## How the Salesforce Sales Cloud + Zendesk integration works

Zendesk's Salesforce integration creates and updates Zendesk organizations from Salesforce accounts (and users from contacts or leads), syncs Zendesk tickets to Salesforce Cases, and can show Zendesk tickets inside Salesforce with Ticket View.

[Setup guide: Zendesk: Connecting Salesforce to Zendesk ↗](https://support.zendesk.com/hc/en-us/articles/4408821555482-Connecting-your-Salesforce-organization-to-Zendesk)

**Limitations:** It needs Salesforce Enterprise or above, or Professional with the API add-on. Account data syncs one way, from Salesforce to Zendesk, and ticket comments aren't synced to a Case field (Ticket View can display them).

Sources (checked Nov 3, 2026): [Zendesk: Connecting Salesforce to Zendesk ↗](https://support.zendesk.com/hc/en-us/articles/4408821555482-Connecting-your-Salesforce-organization-to-Zendesk) · [Zendesk: Data sync from Salesforce ↗](https://support.zendesk.com/hc/en-us/articles/4408828539290-Configuring-data-sync-from-Salesforce-to-Zendesk) · [Zendesk: Ticket sync to Salesforce ↗](https://support.zendesk.com/hc/en-us/articles/4408828449050-Setting-up-ticket-sync-from-Zendesk-to-Salesforce)

*Interactive cost calculator: open the web page to change team size, billing and add-ons.*

## Default 10-seat TCO summary

**Native integration costs $1,940.00/mo ($23,280.00/yr)** for a 10-seat team —
Salesforce Sales Cloud 'Professional' ($1,250.00/mo) + Zendesk 'Suite Team' ($690.00/mo),
no middleware required.
Middleware via Make/Zapier would add ~$10.59/mo on top of the cheapest API-capable tiers ($1,950.59/mo all-in) — the native path is cheaper. Salesforce's $1,250.00 is the Professional plan ($100/user) plus the API add-on, which Salesforce sells through an account executive; this page models it at $25/user ($250 at 10 seats).

 

## Native vs middleware for Salesforce Sales Cloud + Zendesk

The native connector is the cheapest route here. Make or Zapier only makes sense if you already run other automations through it, or need a step the native app doesn't offer.

Chart: Salesforce Sales Cloud + Zendesk: monthly cost for 10 seats by route: Native connector $1,940.00; Make Core route $1,950.59; Zapier Professional route $1,969.99

Monthly cost for 10 seats by route, Salesforce Sales Cloud + Zendesk.

 

Integration routes compared for a 10-seat team

| Route | Plans | 10 seats / month | Sync |
| --- | --- | --- | --- |
| Native Salesforce Sales Cloud + Zendesk connector | Salesforce Sales Cloud 'Professional' + Zendesk 'Suite Team' | $1,940.00 | 1-way per object (accounts → Zendesk, tickets → Salesforce) |
| Make Core on the cheapest API plans | Salesforce Sales Cloud 'Professional' + Zendesk 'Suite Team' + Make | $1,950.59 | 1-way per scenario |
| Zapier Professional on the cheapest API plans | Salesforce Sales Cloud 'Professional' + Zendesk 'Suite Team' + Zapier | $1,969.99 | 1-way per Zap |

Connector prices are monthly-billing list prices: Zapier Professional $29.99 (zapier.com/pricing) and Make Core $10.59 (from third-party pricing reviews, because make.com blocks automated checks). Both bill by usage, so high volumes cost more.

Image: [Salesforce Sales Cloud + Zendesk integration cost summary: $1,940 a month for 10 seats, nothing extra to connect; plans needed: Salesforce Sales Cloud Professional and Zendesk Suite Team](https://stackcostmatrix.com/og/salesforce-and-zendesk.jpg)

## ✓ Verified Vendor Facts

- **Plan prices:** from each vendor's pricing page; any exception is flagged next to the date at the top.
- **Required tiers:** 'Professional' / 'Suite Team' — the minimum plans this integration needs.
- **API & webhook gates:** audited in official developer docs (see spec matrix).
- **Native app availability:** Native app available in vendor marketplace.

Last checked: Nov 3, 2026 (exceptions listed at the top) · Sources linked below.

## ! Plan requirements

Requires Salesforce Sales Cloud on the 'Professional' plan or higher — Requires Zendesk on the 'Suite Team' plan or higher.

Salesforce Sales Cloud minimum tier
:   'Professional'

Zendesk minimum tier
:   'Suite Team'

Middleware fee
:   None

No hidden cost: the native connector works on Salesforce Sales Cloud 'Professional' and Zendesk 'Suite Team', so connecting them adds nothing to what you already pay for the two tools.

## Side-by-side spec matrix

Side-by-side spec matrix

| Spec | Salesforce Sales Cloud | Zendesk |
| --- | --- | --- |
| Connection type | Native   Source: [Salesforce Sales Cloud docs ↗](https://developer.salesforce.com/) · [Zendesk docs ↗](https://developer.zendesk.com/) · Verified Nov 3, 2026 | |
| Data sync direction | 1-way per object (accounts → Zendesk, tickets → Salesforce) | |
| Setup time | 1–3 hours (difficulty 2/5) | |
| Native integration supported | Yes — official native app/connector | |
| API available (distinct from native app) | Yes  — API ≠ native UI; API enables custom/middleware builds Source: [Salesforce Sales Cloud API docs ↗](https://developer.salesforce.com/) · Verified Oct 17, 2026 | Yes  — API ≠ native UI; API enables custom/middleware builds Source: [Zendesk API docs ↗](https://developer.zendesk.com/) · Verified Oct 17, 2026 |
| API access at required tier | Yes  ('Professional') Web Services API add-on (modeled at $25/user) Source: [Salesforce developers: Supported editions ↗](https://developer.salesforce.com/docs/platform/api-rest/guide/intro-rest-compatible-editions.html) · Verified Nov 3, 2026 | Yes  ('Suite Team') 200 requests/min Source: [Zendesk developers: Rate limits ↗](https://developer.zendesk.com/api-reference/introduction/rate-limits/) · Verified Nov 3, 2026 |
| Webhook support at required tier | No  ('Professional') Change Data Capture (Salesforce's change-event feed) isn't available on Professional, so sync runs through the REST API. Source: [Salesforce developers: Change Data Capture ↗](https://developer.salesforce.com/docs/atlas.en-us.change_data_capture.meta/change_data_capture/cdc_intro.htm) · Verified Nov 8, 2026 | Yes  ('Suite Team') Source: [Zendesk: Creating webhooks ↗](https://support.zendesk.com/hc/en-us/articles/4408839108378) · Verified Nov 3, 2026 |

[Visit Salesforce Sales Cloud](https://stackcostmatrix.com/go/salesforce)  [Visit Zendesk](https://stackcostmatrix.com/go/zendesk)

Some outbound links may earn us a referral commission at no extra cost to you. [Read our affiliate disclosure](https://stackcostmatrix.com/about/).

## Salesforce Sales Cloud + Zendesk integration: frequently asked questions

### What are the minimum plan tiers required for the Salesforce Sales Cloud + Zendesk integration?

To unlock the native integration, Salesforce Sales Cloud must be on the 'Professional' plan or higher and Zendesk must be on the 'Suite Team' plan or higher. Those are each tool's cheapest plan with API access (Salesforce Sales Cloud 'Professional' at $1,250/mo and Zendesk 'Suite Team' at $690/mo for 10 seats), so the integration doesn't force an upgrade.

### How much does the Salesforce Sales Cloud + Zendesk stack cost per month for a 10-person team?

At 10 seats with the required tiers (Salesforce Sales Cloud 'Professional' + Zendesk 'Suite Team'), the stack costs $1,940.00 per month.

### Is the Salesforce Sales Cloud + Zendesk integration native, and would Make or Zapier be cheaper?

The Salesforce Sales Cloud + Zendesk connection is native — no third-party middleware subscription is required. Make would cost about $1,950.59/month on the cheapest API plans, more than the native route, so it only makes sense if you already use it.

### What are the limitations of the Salesforce Sales Cloud + Zendesk integration?

It needs Salesforce Enterprise or above, or Professional with the API add-on. Account data syncs one way, from Salesforce to Zendesk, and ticket comments aren't synced to a Case field (Ticket View can display them).

## Integrations related to Salesforce Sales Cloud + Zendesk

[All Salesforce integrations →](https://stackcostmatrix.com/salesforce-integrations-cost/) · [All Zendesk integrations →](https://stackcostmatrix.com/zendesk-integrations-cost/) · [Salesforce API access by plan →](https://stackcostmatrix.com/salesforce-api-access/) · [Zendesk API access by plan →](https://stackcostmatrix.com/zendesk-api-access/)

Part of our [Salesforce integration cost guide](https://stackcostmatrix.com/salesforce-integrations-cost/) and [CRM integration hidden-costs guide](https://stackcostmatrix.com/crm-integration-pricing-guide/).

[### ClickUp + Zendesk

Native](https://stackcostmatrix.com/stack/clickup-and-zendesk/)[### HubSpot + Zendesk

Native](https://stackcostmatrix.com/stack/hubspot-and-zendesk/)[### Salesforce Sales Cloud + Slack

Native](https://stackcostmatrix.com/stack/salesforce-and-slack/)[### Salesforce Sales Cloud + Stripe

Native](https://stackcostmatrix.com/stack/salesforce-and-stripe/)[### HubSpot + Salesforce Sales Cloud

Native](https://stackcostmatrix.com/stack/hubspot-and-salesforce/)[### Zendesk + Stripe

Middleware](https://stackcostmatrix.com/stack/zendesk-and-stripe/)

Last checked: Nov 3, 2026 (exceptions listed at the top)

## Verified sources

Every figure on this page links to its source below; prices that don't come straight from the vendor's page are flagged next to the date:

- [Salesforce Sales Cloud official pricing ↗](https://www.salesforce.com/sales/pricing/)
- [Salesforce Sales Cloud API / developer docs ↗](https://developer.salesforce.com/)
- [Zendesk official pricing ↗](https://www.zendesk.com/pricing/)
- [Zendesk API / developer docs ↗](https://developer.zendesk.com/)
