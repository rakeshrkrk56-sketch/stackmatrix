# Salesforce Sales Cloud + Airtable Integration (2026): How It Works, Setup & True Cost

> How the Salesforce Sales Cloud + Airtable integration works and how to set it up, plus the plans it needs and the 10-seat cost ($1,790/mo).

Source page: https://stackcostmatrix.com/stack/salesforce-and-airtable/  
Publisher: StackCostMatrix · Editor: Rakesh Kumar · Data licence: CC BY 4.0 (credit StackCostMatrix and link to https://stackcostmatrix.com)

---

[Home](https://stackcostmatrix.com/) / Salesforce Sales Cloud + Airtable 

Airtable's own Salesforce sync copies a Salesforce report into an Airtable table, one way, manually or about every hour; it's only on Airtable's Business and Enterprise Scale plans. Requires Salesforce Sales Cloud on the 'Professional' plan and Airtable on the 'Business' plan.

Edited by [Rakesh Kumar](https://stackcostmatrix.com/about/#editor), founder of StackCostMatrix | Integration requirements checked against official vendor docs · Nov 12, 2026 · Prices checked · Nov 3, 2026 (Salesforce prices: Oct 17, 2026) · Setup steps: Nov 12, 2026 | [Spot an outdated price? Report a correction →](mailto:admin@stackcostmatrix.com?subject=Price%20Correction)

## How the Salesforce Sales Cloud + Airtable integration works

**Does Salesforce Sales Cloud integrate with Airtable?** Yes. Airtable builds a Salesforce sync integration that brings a Salesforce report into Airtable as a synced table. It runs one way, from Salesforce to Airtable, and it's only on Airtable's Business and Enterprise Scale plans.

You pick a Salesforce report and a unique ID column, and Airtable creates a read-only synced table that refreshes manually or automatically, about every hour. Fields you add to the table yourself stay editable. To send data back, Airtable's Salesforce automation actions can create or update a Salesforce record when something happens in the base.

[Setup guide: Airtable: Sync integration: Salesforce ↗](https://support.airtable.com/docs/airtable-sync-integration-salesforce)

Diagram of how Salesforce Sales Cloud and Airtable connect. Salesforce Sales Cloud: Professional + API add-on · $1,250/mo for 10 seats. Airtable: Business plan · $540/mo for 10 seats. Salesforce Sales Cloud to Airtable: a Salesforce report as a synced table. Native app, 1-way, no connector fee.

Diagram: how Salesforce Sales Cloud and Airtable connect, a native app. Drawn from the facts on this page.

 

### How do you set up Salesforce Sales Cloud + Airtable?

1. Have a Salesforce report with the records you want, and make sure the Salesforce user who connects it has the View and Run Report permissions on that report.
2. In the Airtable base, click + Add or import and choose Salesforce; if it isn't listed, click the more sources option at the bottom and search for it.
3. Select or link your Salesforce account, then choose the report and its unique ID column.
4. Pick the primary field, choose to sync all fields or specific ones, set how often to sync and how deleted records are handled, then create the synced table.

Steps follow [Airtable's setup guide ↗](https://support.airtable.com/docs/airtable-sync-integration-salesforce), read Nov 12, 2026.

**Limitations:** It needs Airtable Business or Enterprise Scale, so Free and Team workspaces can't use it. If a report's filters change, records that no longer match are deleted from Airtable along with anything added to them, and the unique ID and primary field can't be changed after the table is created. The sync stops if the connecting Salesforce user is deactivated. Airtable reads the report through Salesforce's API, so this page models Salesforce Professional with the API add-on.

Sources (checked Nov 12, 2026): [Airtable: Sync integration: Salesforce ↗](https://support.airtable.com/docs/airtable-sync-integration-salesforce)

*Interactive cost calculator: open the web page to change team size, billing and add-ons.*

## Default 10-seat TCO summary

**Native integration costs $1,790.00/mo ($21,480.00/yr)** for a 10-seat team —
Salesforce Sales Cloud 'Professional' ($1,250.00/mo) + Airtable 'Business' ($540.00/mo),
no middleware required.
Alternative: skip the native tier upgrade and run via Make/Zapier middleware for ~$1,260.59/mo all-in (adds a third-party dependency). Salesforce's $1,250.00 is the Professional plan ($100/user) plus the API add-on, which Salesforce sells through an account executive; this page models it at $25/user ($250 at 10 seats).

 

## Native vs middleware for Salesforce Sales Cloud + Airtable

The connector routes are cheaper on paper because they skip the forced plan upgrade. The trade-off: you swap the native connector for a third-party automation you build and maintain, sync stays 1-way per automation, and the connector bills by usage.

Chart: Salesforce Sales Cloud + Airtable: monthly cost for 10 seats by route: Native connector $1,790.00; Make Core route $1,260.59; Zapier Professional route $1,279.99

Monthly cost for 10 seats by route, Salesforce Sales Cloud + Airtable.

 

Integration routes compared for a 10-seat team

| Route | Plans | 10 seats / month | Sync |
| --- | --- | --- | --- |
| Native Salesforce Sales Cloud + Airtable connector | Salesforce Sales Cloud 'Professional' + Airtable 'Business' | $1,790.00 | 1-way (Salesforce → Airtable) |
| Make Core on the cheapest API plans | Salesforce Sales Cloud 'Professional' + Airtable 'Free' + Make | $1,260.59 | 1-way per scenario |
| Zapier Professional on the cheapest API plans | Salesforce Sales Cloud 'Professional' + Airtable 'Free' + Zapier | $1,279.99 | 1-way per Zap |

Connector prices are monthly-billing list prices: Zapier Professional $29.99 (zapier.com/pricing) and Make Core $10.59 (from third-party pricing reviews, because make.com blocks automated checks). Both bill by usage, so high volumes cost more.

Image: [Salesforce Sales Cloud + Airtable integration cost summary: $1,790 a month for 10 seats, $540 of it is the hidden cost to connect; plans needed: Salesforce Sales Cloud Professional and Airtable Business](https://stackcostmatrix.com/og/salesforce-and-airtable.jpg)

## ✓ Verified Vendor Facts

- **Plan prices:** from each vendor's pricing page; any exception is flagged next to the date at the top.
- **Required tiers:** 'Professional' / 'Business' — the minimum plans this integration needs.
- **API & webhook gates:** audited in official developer docs (see spec matrix).
- **Native app availability:** Native app available in vendor marketplace.

Requirements checked: Nov 12, 2026; prices: Nov 3, 2026 (exceptions listed at the top) · Sources linked below.

## ! Hidden Cost Trap

Requires Salesforce Sales Cloud on the 'Professional' plan or higher — Requires Airtable on the 'Business' plan or higher.

Salesforce Sales Cloud minimum tier
:   'Professional'

Airtable minimum tier
:   'Business'

Middleware fee
:   None

The hidden cost is a forced plan upgrade: Airtable needs 'Business', $540/mo more than 'Free', its cheapest plan with API access. That adds $540/mo for 10 seats just to connect the two tools. Running the same connection through Make on the cheapest API plans would cost about $1,260.59/mo in total instead of $1,790/mo, but you'd give up the native connector.

 [Skip the native tier upgrade: connect Salesforce Sales Cloud + Airtable via Make.com middleware instead](https://stackcostmatrix.com/go/make) 

Affiliate link — we may earn a commission at no extra cost to you.

## Side-by-side spec matrix

Side-by-side spec matrix

| Spec | Salesforce Sales Cloud | Airtable |
| --- | --- | --- |
| Connection type | Native   Source: [Salesforce Sales Cloud docs ↗](https://developer.salesforce.com/) · [Airtable docs ↗](https://airtable.com/developers/web/api/introduction) · Verified Nov 12, 2026 | |
| Data sync direction | 1-way (Salesforce → Airtable) | |
| Setup time | 1–3 hours (difficulty 2/5) | |
| Native integration supported | Yes — official native app/connector | |
| API available (distinct from native app) | Yes  — API ≠ native UI; API enables custom/middleware builds Source: [Salesforce Sales Cloud API docs ↗](https://developer.salesforce.com/) · Verified Oct 17, 2026 | Yes  — API ≠ native UI; API enables custom/middleware builds Source: [Airtable API docs ↗](https://airtable.com/developers/web/api/introduction) · Verified Oct 17, 2026 |
| API access at required tier | Yes  ('Professional') Web Services API add-on (modeled at $25/user) Source: [Salesforce developers: Supported editions ↗](https://developer.salesforce.com/docs/platform/api-rest/guide/intro-rest-compatible-editions.html) · Verified Nov 3, 2026 | Yes  ('Business') Not stated in the article we read Source: [Airtable: Managing API call limits ↗](https://support.airtable.com/articles/7735693959-managing-api-call-limits-in-airtable) · Verified Nov 3, 2026 |
| Webhook support at required tier | No  ('Professional') Change Data Capture (Salesforce's change-event feed) isn't available on Professional, so sync runs through the REST API. Source: [Salesforce developers: Change Data Capture ↗](https://developer.salesforce.com/docs/atlas.en-us.change_data_capture.meta/change_data_capture/cdc_intro.htm) · Verified Nov 8, 2026 | Yes  ('Business') Source: [Airtable: Create a webhook ↗](https://airtable.com/developers/web/api/create-a-webhook) · Verified Nov 3, 2026 |

[Visit Salesforce Sales Cloud](https://stackcostmatrix.com/go/salesforce)  [Visit Airtable](https://stackcostmatrix.com/go/airtable)

Some outbound links may earn us a referral commission at no extra cost to you. [Read our affiliate disclosure](https://stackcostmatrix.com/about/).

## Salesforce Sales Cloud + Airtable integration: frequently asked questions

### What are the minimum plan tiers required for the Salesforce Sales Cloud + Airtable integration?

To unlock the native integration, Salesforce Sales Cloud must be on the 'Professional' plan or higher and Airtable must be on the 'Business' plan or higher. Airtable's cheapest plan with API access is 'Free', so 'Business' is a $540/mo upgrade at 10 seats.

### How much does the Salesforce Sales Cloud + Airtable stack cost per month for a 10-person team?

At 10 seats with the required tiers (Salesforce Sales Cloud 'Professional' + Airtable 'Business'), the stack costs $1,790.00 per month.

### Is the Salesforce Sales Cloud + Airtable integration native, and would Make or Zapier be cheaper?

The Salesforce Sales Cloud + Airtable connection is native — no third-party middleware subscription is required. Connecting through Make on the cheapest API plans would cost about $1,260.59/month in total instead of $1,790.00, but you'd replace the native connector with a third-party automation.

### What are the limitations of the Salesforce Sales Cloud + Airtable integration?

It needs Airtable Business or Enterprise Scale, so Free and Team workspaces can't use it. If a report's filters change, records that no longer match are deleted from Airtable along with anything added to them, and the unique ID and primary field can't be changed after the table is created. The sync stops if the connecting Salesforce user is deactivated. Airtable reads the report through Salesforce's API, so this page models Salesforce Professional with the API add-on.

## Integrations related to Salesforce Sales Cloud + Airtable

[All Salesforce integrations →](https://stackcostmatrix.com/salesforce-integrations-cost/) · [All Airtable integrations →](https://stackcostmatrix.com/airtable-integrations-cost/) · [Salesforce API access by plan →](https://stackcostmatrix.com/salesforce-api-access/) · [Airtable API access by plan →](https://stackcostmatrix.com/airtable-api-access/)

Part of our [CRM integration hidden-costs guide](https://stackcostmatrix.com/crm-integration-pricing-guide/).

[### Asana + Salesforce

Native](https://stackcostmatrix.com/stack/asana-and-salesforce/)[### HubSpot + Salesforce

Native](https://stackcostmatrix.com/stack/hubspot-and-salesforce/)[### Intercom + Salesforce

Native](https://stackcostmatrix.com/stack/intercom-and-salesforce/)[### Pipedrive + Salesforce

Middleware](https://stackcostmatrix.com/stack/pipedrive-and-salesforce/)[### Salesforce + Calendly

Native](https://stackcostmatrix.com/stack/salesforce-and-calendly/)[### Salesforce + Mailchimp

Native](https://stackcostmatrix.com/stack/salesforce-and-mailchimp/)

Requirements checked: Nov 12, 2026; prices: Nov 3, 2026 (exceptions listed at the top)

## Verified sources

Every figure on this page links to its source below; prices that don't come straight from the vendor's page are flagged next to the date:

- [Salesforce Sales Cloud official pricing ↗](https://www.salesforce.com/sales/pricing/)
- [Salesforce Sales Cloud API / developer docs ↗](https://developer.salesforce.com/)
- [Airtable official pricing ↗](https://www.airtable.com/pricing)
- [Airtable API / developer docs ↗](https://airtable.com/developers/web/api/introduction)
