# Intercom + Salesforce Sales Cloud Integration (2026): How It Works, Setup & True Cost

> How the Intercom + Salesforce Sales Cloud integration works and how to set it up, plus the plans it needs and the 10-seat cost ($2,240/mo).

Source page: https://stackcostmatrix.com/stack/intercom-and-salesforce/  
Publisher: StackCostMatrix · Editor: Rakesh Kumar · Data licence: CC BY 4.0 (credit StackCostMatrix and link to https://stackcostmatrix.com)

---

[Home](https://stackcostmatrix.com/) / Intercom + Salesforce Sales Cloud 

Intercom's own Salesforce app creates Salesforce leads from Intercom, syncs data and conversations and shows Salesforce details in the inbox, but it's only on Intercom's Advanced and Expert plans, and Salesforce needs API access. Requires Intercom on the 'Advanced' plan and Salesforce Sales Cloud on the 'Professional' plan.

Edited by [Rakesh Kumar](https://stackcostmatrix.com/about/#editor), founder of StackCostMatrix | Integration requirements checked against official vendor docs · Nov 12, 2026 · Prices checked · Nov 3, 2026 (Salesforce prices: Oct 17, 2026) · Setup steps: Nov 12, 2026 | [Spot an outdated price? Report a correction →](mailto:admin@stackcostmatrix.com?subject=Price%20Correction)

## How the Intercom + Salesforce Sales Cloud integration works

**Does Intercom integrate with Salesforce Sales Cloud?** Yes. Intercom builds a Salesforce app, available on its Advanced and Expert plans. It needs a Salesforce edition with API access: Enterprise and Unlimited include it, and Professional can buy it as an add-on.

New leads captured in Intercom are created in Salesforce, and data and conversations sync whenever a user or lead is updated. In the Intercom inbox, teammates see Salesforce details such as lead status and owner, account and contact details, opportunity stage and value and close dates; conversations can be routed to the account owner, and Salesforce data can be used to target outbound messages.

[Setup guide: Intercom: Install Salesforce integration ↗](https://www.intercom.com/help/en/articles/4497943-install-salesforce-integration)

Diagram of how Intercom and Salesforce Sales Cloud connect. Intercom: Advanced plan · $990/mo for 10 seats. Salesforce Sales Cloud: Professional + API add-on · $1,250/mo for 10 seats. Intercom to Salesforce Sales Cloud: new leads, data and conversations. Salesforce Sales Cloud to Intercom: lead, account and opportunity details. Native app, 2-way, no connector fee.

Diagram: how Intercom and Salesforce Sales Cloud connect, a native app. Drawn from the facts on this page.

 

### How do you set up Intercom + Salesforce Sales Cloud?

1. Check that you have full admin permissions in Intercom (at least Apps and Integrations Access), and a regular Salesforce user, not API-only, with API Enabled, View All Data and read/write access to Leads, Contacts, Accounts and Tasks.
2. Find Salesforce in the Intercom App Store and click Install now.
3. Authorize Salesforce to access your Intercom workspace and log in to your Salesforce account.
4. If that Salesforce user isn't a System Administrator, go to Setup → Connected Apps OAuth Usage in Salesforce and click Install on the Intercom app.
5. Configure your data mapping for leads, users and their attributes.

Steps follow [Intercom's setup guide ↗](https://www.intercom.com/help/en/articles/4497943-install-salesforce-integration), read Nov 12, 2026.

**Limitations:** It isn't on Intercom's Essential plan, so it forces Advanced, and installing into a Salesforce sandbox needs Intercom's Expert plan. Tags and events can't be mapped and synced through the app. Salesforce's Contact, Group and Professional editions don't include API access; Professional can add it, and this page models Professional with that add-on.

Sources (checked Nov 12, 2026): [Intercom: Install Salesforce integration ↗](https://www.intercom.com/help/en/articles/4497943-install-salesforce-integration)

*Interactive cost calculator: open the web page to change team size, billing and add-ons.*

## Default 10-seat TCO summary

**Native integration costs $2,240.00/mo ($26,880.00/yr)** for a 10-seat team —
Intercom 'Advanced' ($990.00/mo) + Salesforce Sales Cloud 'Professional' ($1,250.00/mo),
no middleware required.
Alternative: skip the native tier upgrade and run via Make/Zapier middleware for ~$1,650.59/mo all-in (adds a third-party dependency). Salesforce's $1,250.00 is the Professional plan ($100/user) plus the API add-on, which Salesforce sells through an account executive; this page models it at $25/user ($250 at 10 seats).

 

## Native vs middleware for Intercom + Salesforce Sales Cloud

The connector routes are cheaper on paper because they skip the forced plan upgrade. The trade-off: you swap the native connector for a third-party automation you build and maintain, sync drops from 2-way to 1-way per automation, and the connector bills by usage.

Chart: Intercom + Salesforce Sales Cloud: monthly cost for 10 seats by route: Native connector $2,240.00; Make Core route $1,650.59; Zapier Professional route $1,669.99

Monthly cost for 10 seats by route, Intercom + Salesforce Sales Cloud.

 

Integration routes compared for a 10-seat team

| Route | Plans | 10 seats / month | Sync |
| --- | --- | --- | --- |
| Native Intercom + Salesforce Sales Cloud connector | Intercom 'Advanced' + Salesforce Sales Cloud 'Professional' | $2,240.00 | 2-way |
| Make Core on the cheapest API plans | Intercom 'Essential' + Salesforce Sales Cloud 'Professional' + Make | $1,650.59 | 1-way per scenario |
| Zapier Professional on the cheapest API plans | Intercom 'Essential' + Salesforce Sales Cloud 'Professional' + Zapier | $1,669.99 | 1-way per Zap |

Connector prices are monthly-billing list prices: Zapier Professional $29.99 (zapier.com/pricing) and Make Core $10.59 (from third-party pricing reviews, because make.com blocks automated checks). Both bill by usage, so high volumes cost more.

Image: [Intercom + Salesforce Sales Cloud integration cost summary: $2,240 a month for 10 seats, $600 of it is the hidden cost to connect; plans needed: Intercom Advanced and Salesforce Sales Cloud Professional](https://stackcostmatrix.com/og/intercom-and-salesforce.jpg)

## ✓ Verified Vendor Facts

- **Plan prices:** from each vendor's pricing page; any exception is flagged next to the date at the top.
- **Required tiers:** 'Advanced' / 'Professional' — the minimum plans this integration needs.
- **API & webhook gates:** audited in official developer docs (see spec matrix).
- **Native app availability:** Native app available in vendor marketplace.

Requirements checked: Nov 12, 2026; prices: Nov 3, 2026 (exceptions listed at the top) · Sources linked below.

## ! Hidden Cost Trap

Requires Intercom on the 'Advanced' plan or higher — Requires Salesforce Sales Cloud on the 'Professional' plan or higher.

Intercom minimum tier
:   'Advanced'

Salesforce Sales Cloud minimum tier
:   'Professional'

Middleware fee
:   None

The hidden cost is a forced plan upgrade: Intercom needs 'Advanced', $600/mo more than 'Essential', its cheapest plan with API access. That adds $600/mo for 10 seats just to connect the two tools. Running the same connection through Make on the cheapest API plans would cost about $1,650.59/mo in total instead of $2,240/mo, but you'd give up the native connector.

 [Skip the native tier upgrade: connect Intercom + Salesforce Sales Cloud via Make.com middleware instead](https://stackcostmatrix.com/go/make) 

Affiliate link — we may earn a commission at no extra cost to you.

## Side-by-side spec matrix

Side-by-side spec matrix

| Spec | Intercom | Salesforce Sales Cloud |
| --- | --- | --- |
| Connection type | Native   Source: [Intercom docs ↗](https://developers.intercom.com/) · [Salesforce Sales Cloud docs ↗](https://developer.salesforce.com/) · Verified Nov 12, 2026 | |
| Data sync direction | 2-way | |
| Setup time | Half a day (difficulty 3/5) | |
| Native integration supported | Yes — official native app/connector | |
| API available (distinct from native app) | Yes  — API ≠ native UI; API enables custom/middleware builds Source: [Intercom API docs ↗](https://developers.intercom.com/) · Verified Oct 17, 2026 | Yes  — API ≠ native UI; API enables custom/middleware builds Source: [Salesforce Sales Cloud API docs ↗](https://developer.salesforce.com/) · Verified Oct 17, 2026 |
| API access at required tier | Yes  ('Advanced') Paid workspaces Source: [Intercom developers: Webhooks ↗](https://developers.intercom.com/docs/webhooks) · Verified Nov 3, 2026 | Yes  ('Professional') Web Services API add-on (modeled at $25/user) Source: [Salesforce developers: Supported editions ↗](https://developer.salesforce.com/docs/platform/api-rest/guide/intro-rest-compatible-editions.html) · Verified Nov 3, 2026 |
| Webhook support at required tier | Yes  ('Advanced') Source: [Intercom developers: Webhooks ↗](https://developers.intercom.com/docs/webhooks) · Verified Nov 3, 2026 | No  ('Professional') Change Data Capture (Salesforce's change-event feed) isn't available on Professional, so sync runs through the REST API. Source: [Salesforce developers: Change Data Capture ↗](https://developer.salesforce.com/docs/atlas.en-us.change_data_capture.meta/change_data_capture/cdc_intro.htm) · Verified Nov 8, 2026 |

[Visit Intercom](https://stackcostmatrix.com/go/intercom)  [Visit Salesforce Sales Cloud](https://stackcostmatrix.com/go/salesforce)

Some outbound links may earn us a referral commission at no extra cost to you. [Read our affiliate disclosure](https://stackcostmatrix.com/about/).

## Intercom + Salesforce Sales Cloud integration: frequently asked questions

### What are the minimum plan tiers required for the Intercom + Salesforce Sales Cloud integration?

To unlock the native integration, Intercom must be on the 'Advanced' plan or higher and Salesforce Sales Cloud must be on the 'Professional' plan or higher. Intercom's cheapest plan with API access is 'Essential', so 'Advanced' is a $600/mo upgrade at 10 seats.

### How much does the Intercom + Salesforce Sales Cloud stack cost per month for a 10-person team?

At 10 seats with the required tiers (Intercom 'Advanced' + Salesforce Sales Cloud 'Professional'), the stack costs $2,240.00 per month.

### Is the Intercom + Salesforce Sales Cloud integration native, and would Make or Zapier be cheaper?

The Intercom + Salesforce Sales Cloud connection is native — no third-party middleware subscription is required. Connecting through Make on the cheapest API plans would cost about $1,650.59/month in total instead of $2,240.00, but you'd replace the native connector with a third-party automation.

### What are the limitations of the Intercom + Salesforce Sales Cloud integration?

It isn't on Intercom's Essential plan, so it forces Advanced, and installing into a Salesforce sandbox needs Intercom's Expert plan. Tags and events can't be mapped and synced through the app. Salesforce's Contact, Group and Professional editions don't include API access; Professional can add it, and this page models Professional with that add-on.

## Integrations related to Intercom + Salesforce Sales Cloud

[All Intercom integrations →](https://stackcostmatrix.com/intercom-integrations-cost/) · [All Salesforce integrations →](https://stackcostmatrix.com/salesforce-integrations-cost/) · [Intercom API access by plan →](https://stackcostmatrix.com/intercom-api-access/) · [Salesforce API access by plan →](https://stackcostmatrix.com/salesforce-api-access/)

Part of our [CRM integration hidden-costs guide](https://stackcostmatrix.com/crm-integration-pricing-guide/).

[### Intercom + Calendly

Native](https://stackcostmatrix.com/stack/intercom-and-calendly/)[### Intercom + HubSpot

Native](https://stackcostmatrix.com/stack/intercom-and-hubspot/)[### Intercom + Mailchimp

Native](https://stackcostmatrix.com/stack/intercom-and-mailchimp/)[### Intercom + Stripe

Native](https://stackcostmatrix.com/stack/intercom-and-stripe/)[### Pipedrive + Intercom

Native](https://stackcostmatrix.com/stack/pipedrive-and-intercom/)[### Slack + Intercom

Native](https://stackcostmatrix.com/stack/slack-and-intercom/)

Requirements checked: Nov 12, 2026; prices: Nov 3, 2026 (exceptions listed at the top)

## Verified sources

Every figure on this page links to its source below; prices that don't come straight from the vendor's page are flagged next to the date:

- [Intercom official pricing ↗](https://www.intercom.com/pricing)
- [Intercom API / developer docs ↗](https://developers.intercom.com/)
- [Salesforce Sales Cloud official pricing ↗](https://www.salesforce.com/sales/pricing/)
- [Salesforce Sales Cloud API / developer docs ↗](https://developer.salesforce.com/)
