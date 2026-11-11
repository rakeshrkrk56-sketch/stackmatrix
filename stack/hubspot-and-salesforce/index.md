# HubSpot + Salesforce Sales Cloud Integration Cost (2026): True Price, Minimum Plan & Hidden API Fees

> HubSpot + Salesforce needs HubSpot Professional and Salesforce Professional: $1,750/mo for 10 seats, including a +$500/mo forced upgrade.

Source page: https://stackcostmatrix.com/stack/hubspot-and-salesforce/  
Publisher: StackCostMatrix · Editor: Rakesh Kumar · Data licence: CC BY 4.0 (credit StackCostMatrix and link to https://stackcostmatrix.com)

---

[Home](https://stackcostmatrix.com/) / HubSpot + Salesforce Sales Cloud 

Big trap: HubSpot's native Salesforce connector needs a HubSpot Professional or Enterprise subscription — the free CRM can't use it. The cheapest route is Smart CRM Professional at $50 per seat a month ($45 on annual billing). Requires HubSpot on the 'Professional' plan and Salesforce Sales Cloud on the 'Professional' plan for full 2-way sync.

Edited by [Rakesh Kumar](https://stackcostmatrix.com/about/#editor), founder of StackCostMatrix | Integration requirements and prices checked against official vendor docs · Nov 3, 2026 (HubSpot prices: Nov 5, 2026; Salesforce prices: Oct 17, 2026) · Setup steps: Nov 10, 2026 | [Spot an outdated price? Report a correction →](mailto:admin@stackcostmatrix.com?subject=Price%20Correction)

## How the HubSpot + Salesforce Sales Cloud integration works

HubSpot's own Salesforce connector syncs leads, contacts, accounts, opportunities and custom objects between the two CRMs, and can embed HubSpot contact, company and deal insights inside Salesforce. It suits teams that run marketing in HubSpot and sales in Salesforce.

Diagram of how HubSpot and Salesforce Sales Cloud connect. HubSpot: Professional plan · $500/mo for 10 seats. Salesforce Sales Cloud: Professional + API add-on · $1,250/mo for 10 seats. Both ways: leads, contacts, accounts, opportunities. Native app, 2-way, no connector fee.

Diagram: how HubSpot and Salesforce Sales Cloud connect, a native app. Drawn from the facts on this page.

 

### How do you set up HubSpot + Salesforce Sales Cloud?

1. Check the Salesforce user who will connect it: HubSpot asks for a Salesforce system administrator with the API Enabled, View Setup and Configuration and Download AppExchange Packages permissions, and Modify All on the objects you want to sync.
2. In HubSpot, click the Marketplace icon in the top navigation bar and select HubSpot Marketplace.
3. Search for and select the Salesforce app, then click Install.
4. If you're connecting a Salesforce sandbox, tick Yes, this will connect to a sandbox. Click Install.
5. In the pop-up window, enter your Salesforce credentials and click Log In. You're sent back to HubSpot.
6. Records don't sync on their own after installation: import your Salesforce records into HubSpot, or let them sync gradually as records change.

Steps follow [HubSpot's setup guide ↗](https://knowledge.hubspot.com/salesforce/install-the-hubspot-salesforce-integration), read Nov 10, 2026.

**Limitations:** The connector is only available on HubSpot Professional or Enterprise subscriptions, every sync uses part of your Salesforce API call allowance, and the Salesforce user who connects it needs the API Enabled permission.

**Before you budget:** HubSpot charges a required one-time Professional Onboarding fee on some Hubs ($1,500 for Sales Hub or Service Hub, $3,000 for Marketing Hub; its pricing page shows none for Smart CRM Professional). It isn't in the monthly totals here, so add it under one-time setup cost in the calculator. On the Salesforce side, HubSpot's requirements read "a Salesforce edition with API access, or Salesforce Professional" (Group Edition isn't supported), and Salesforce says security-reviewed AppExchange apps can reach Professional orgs even if the customer doesn't have API access. So ask Salesforce whether your org needs the API add-on for HubSpot's connector before paying for it; the totals here include it.

[Setup guide: HubSpot: Connect HubSpot and Salesforce ↗](https://knowledge.hubspot.com/salesforce/install-the-hubspot-salesforce-integration)

Sources (checked Nov 3, 2026; setup guide read again for the steps on Nov 10, 2026): [HubSpot: Connect HubSpot and Salesforce ↗](https://knowledge.hubspot.com/salesforce/install-the-hubspot-salesforce-integration) · [HubSpot Marketplace: Salesforce ↗](https://ecosystem.hubspot.com/marketplace/listing/salesforce) · [Salesforce developers: API access in Group and Professional Editions ↗](https://developer.salesforce.com/docs/atlas.en-us.packagingGuide.meta/packagingGuide/dev_packages_api_access.htm) · [HubSpot pricing ↗](https://www.hubspot.com/pricing)

*Interactive cost calculator: open the web page to change team size, billing and add-ons.*

## Default 10-seat TCO summary

**Native integration costs $1,750.00/mo ($21,000.00/yr)** for a 10-seat team —
HubSpot 'Professional' ($500.00/mo) + Salesforce Sales Cloud 'Professional' ($1,250.00/mo),
no middleware required.
Alternative: skip the native tier upgrade and run via Make/Zapier middleware for ~$1,260.59/mo all-in (adds a third-party dependency). Salesforce's $1,250.00 is the Professional plan ($100/user) plus the API add-on, which Salesforce sells through an account executive; this page models it at $25/user ($250 at 10 seats).

 

## Native vs middleware for HubSpot + Salesforce Sales Cloud

The connector routes are cheaper on paper because they skip the forced plan upgrade. The trade-off: you swap the native connector for a third-party automation you build and maintain, sync drops from 2-way to 1-way per automation, and the connector bills by usage.

Chart: HubSpot + Salesforce Sales Cloud: monthly cost for 10 seats by route: Native connector $1,750.00; Make Core route $1,260.59; Zapier Professional route $1,279.99

Monthly cost for 10 seats by route, HubSpot + Salesforce Sales Cloud.

 

Integration routes compared for a 10-seat team

| Route | Plans | 10 seats / month | Sync |
| --- | --- | --- | --- |
| Native HubSpot + Salesforce Sales Cloud connector | HubSpot 'Professional' + Salesforce Sales Cloud 'Professional' | $1,750.00 | 2-way |
| Make Core on the cheapest API plans | HubSpot 'Free' + Salesforce Sales Cloud 'Professional' + Make | $1,260.59 | 1-way per scenario |
| Zapier Professional on the cheapest API plans | HubSpot 'Free' + Salesforce Sales Cloud 'Professional' + Zapier | $1,279.99 | 1-way per Zap |

Connector prices are monthly-billing list prices: Zapier Professional $29.99 (zapier.com/pricing) and Make Core $10.59 (from third-party pricing reviews, because make.com blocks automated checks). Both bill by usage, so high volumes cost more.

Image: [HubSpot + Salesforce Sales Cloud integration cost summary: $1,750 a month for 10 seats, $500 of it is the hidden cost to connect; plans needed: HubSpot Professional and Salesforce Sales Cloud Professional](https://stackcostmatrix.com/og/hubspot-and-salesforce.jpg)

## ✓ Verified Vendor Facts

- **Plan prices:** from each vendor's pricing page; any exception is flagged next to the date at the top.
- **Required tiers:** 'Professional' / 'Professional' — the minimum plans this integration needs.
- **API & webhook gates:** audited in official developer docs (see spec matrix).
- **Native app availability:** Native app available in vendor marketplace.

Last checked: Nov 3, 2026 (exceptions listed at the top) · Sources linked below.

## ! Hidden Cost Trap

Requires HubSpot on the 'Professional' plan or higher — Requires Salesforce Sales Cloud on the 'Professional' plan or higher.

HubSpot minimum tier
:   'Professional'

Salesforce Sales Cloud minimum tier
:   'Professional'

Middleware fee
:   None

The hidden cost is a forced plan upgrade: HubSpot needs 'Professional', $500/mo more than 'Free', its cheapest plan with API access. That adds $500/mo for 10 seats just to connect the two tools. Running the same connection through Make on the cheapest API plans would cost about $1,260.59/mo in total instead of $1,750/mo, but you'd give up the native connector.

 [Skip the native tier upgrade: connect HubSpot + Salesforce Sales Cloud via Make.com middleware instead](https://stackcostmatrix.com/go/make) 

Affiliate link — we may earn a commission at no extra cost to you.

## Side-by-side spec matrix

Side-by-side spec matrix

| Spec | HubSpot | Salesforce Sales Cloud |
| --- | --- | --- |
| Connection type | Native   Source: [HubSpot docs ↗](https://developers.hubspot.com/docs/api/overview) · [Salesforce Sales Cloud docs ↗](https://developer.salesforce.com/) · Verified Nov 3, 2026 | |
| Data sync direction | 2-way | |
| Setup time | Half a day (difficulty 3/5) | |
| Native integration supported | Yes — official native app/connector | |
| API available (distinct from native app) | Yes  — API ≠ native UI; API enables custom/middleware builds Source: [HubSpot API docs ↗](https://developers.hubspot.com/docs/api/overview) · Verified Oct 17, 2026 | Yes  — API ≠ native UI; API enables custom/middleware builds Source: [Salesforce Sales Cloud API docs ↗](https://developer.salesforce.com/) · Verified Oct 17, 2026 |
| API access at required tier | Yes  ('Professional') 190 req/10 s · 625,000/day (private apps) Source: [HubSpot developers: Usage guidelines ↗](https://developers.hubspot.com/docs/developer-tooling/platform/usage-guidelines) · Verified Nov 3, 2026 | Yes  ('Professional') Web Services API add-on (modeled at $25/user) Source: [Salesforce developers: Supported editions ↗](https://developer.salesforce.com/docs/platform/api-rest/guide/intro-rest-compatible-editions.html) · Verified Nov 3, 2026 |
| Webhook support at required tier | No  ('Professional') Only with Data Hub Professional Source: [HubSpot KB: Webhooks in workflows ↗](https://knowledge.hubspot.com/workflows/how-do-i-use-webhooks-with-hubspot-workflows) · Verified Nov 3, 2026 | No  ('Professional') Change Data Capture (Salesforce's change-event feed) isn't available on Professional, so sync runs through the REST API. Source: [Salesforce developers: Change Data Capture ↗](https://developer.salesforce.com/docs/atlas.en-us.change_data_capture.meta/change_data_capture/cdc_intro.htm) · Verified Nov 8, 2026 |

[Visit HubSpot](https://stackcostmatrix.com/go/hubspot)  [Visit Salesforce Sales Cloud](https://stackcostmatrix.com/go/salesforce)

Some outbound links may earn us a referral commission at no extra cost to you. [Read our affiliate disclosure](https://stackcostmatrix.com/about/).

## HubSpot + Salesforce Sales Cloud integration: frequently asked questions

### What are the minimum plan tiers required for the HubSpot + Salesforce Sales Cloud integration?

To unlock the native integration, HubSpot must be on the 'Professional' plan or higher and Salesforce Sales Cloud must be on the 'Professional' plan or higher. HubSpot's cheapest plan with API access is 'Free', so 'Professional' is a $500/mo upgrade at 10 seats.

### How much does the HubSpot + Salesforce Sales Cloud stack cost per month for a 10-person team?

At 10 seats with the required tiers (HubSpot 'Professional' + Salesforce Sales Cloud 'Professional'), the stack costs $1,750.00 per month.

### Is the HubSpot + Salesforce Sales Cloud integration native, and would Make or Zapier be cheaper?

The HubSpot + Salesforce Sales Cloud connection is native — no third-party middleware subscription is required. Connecting through Make on the cheapest API plans would cost about $1,260.59/month in total instead of $1,750.00, but you'd replace the native connector with a third-party automation.

### What are the limitations of the HubSpot + Salesforce Sales Cloud integration?

The connector is only available on HubSpot Professional or Enterprise subscriptions, every sync uses part of your Salesforce API call allowance, and the Salesforce user who connects it needs the API Enabled permission.

## Integrations related to HubSpot + Salesforce Sales Cloud

[All HubSpot integrations →](https://stackcostmatrix.com/hubspot-integrations-cost/) · [All Salesforce integrations →](https://stackcostmatrix.com/salesforce-integrations-cost/) · [HubSpot API access by plan →](https://stackcostmatrix.com/hubspot-api-access/) · [Salesforce API access by plan →](https://stackcostmatrix.com/salesforce-api-access/)

Part of our [HubSpot integration cost guide](https://stackcostmatrix.com/hubspot-integrations-cost/), [Salesforce integration cost guide](https://stackcostmatrix.com/salesforce-integrations-cost/) and [CRM integration hidden-costs guide](https://stackcostmatrix.com/crm-integration-pricing-guide/).

[### HubSpot + Calendly

Native](https://stackcostmatrix.com/stack/hubspot-and-calendly/)[### HubSpot + Mailchimp

Native](https://stackcostmatrix.com/stack/hubspot-and-mailchimp/)[### HubSpot + Slack

Native](https://stackcostmatrix.com/stack/hubspot-and-slack/)[### HubSpot + Stripe

Native](https://stackcostmatrix.com/stack/hubspot-and-stripe/)[### Salesforce Sales Cloud + Slack

Native](https://stackcostmatrix.com/stack/salesforce-and-slack/)[### Salesforce Sales Cloud + Zendesk

Native](https://stackcostmatrix.com/stack/salesforce-and-zendesk/)

Last checked: Nov 3, 2026 (exceptions listed at the top)

## Verified sources

Every figure on this page links to its source below; prices that don't come straight from the vendor's page are flagged next to the date:

- [HubSpot official pricing ↗](https://www.hubspot.com/pricing)
- [HubSpot API / developer docs ↗](https://developers.hubspot.com/docs/api/overview)
- [Salesforce Sales Cloud official pricing ↗](https://www.salesforce.com/sales/pricing/)
- [Salesforce Sales Cloud API / developer docs ↗](https://developer.salesforce.com/)
