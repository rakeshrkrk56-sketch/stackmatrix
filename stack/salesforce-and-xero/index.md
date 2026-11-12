# Salesforce Sales Cloud + Xero Integration (2026): How It Works, Setup & True Cost

> How the Salesforce Sales Cloud + Xero integration works and how to set it up, plus the plans it needs and the 10-seat cost ($1,287.59/mo).

Source page: https://stackcostmatrix.com/stack/salesforce-and-xero/  
Publisher: StackCostMatrix · Editor: Rakesh Kumar · Data licence: CC BY 4.0 (credit StackCostMatrix and link to https://stackcostmatrix.com)

---

[Home](https://stackcostmatrix.com/) / Salesforce Sales Cloud + Xero 

There's no native Salesforce–Xero connector: Xero's App Store points to partner apps such as TwoCanConnect and SFX Connect, and Make Core links the two through Salesforce's API, which Professional Edition gets only as a paid add-on. Requires Salesforce Sales Cloud on the 'Professional' plan and Xero on the 'Early' plan. Route it through Make Core ($10.59/mo, or $9/mo billed annually).

Edited by [Rakesh Kumar](https://stackcostmatrix.com/about/#editor), founder of StackCostMatrix | Integration requirements checked against official vendor docs · Nov 12, 2026 · Prices checked · Nov 3, 2026 (Salesforce prices: Oct 17, 2026; Make fee: $9 annual price Oct 17, 2026; $10.59 monthly price from third-party pricing reviews, Nov 3, 2026, as make.com blocks automated checks) · Setup steps: Nov 12, 2026 | [Spot an outdated price? Report a correction →](mailto:admin@stackcostmatrix.com?subject=Price%20Correction)

## How the Salesforce Sales Cloud + Xero integration works

**Does Salesforce Sales Cloud integrate with Xero?** Not natively. Xero's App Store points to partner apps for Salesforce, such as TwoCanConnect and SFX Connect, each priced separately, and Make or Zapier can connect the two through Salesforce's API, which Professional Edition only gets as a paid add-on.

With Make, a scenario watches Salesforce, for example for a won opportunity, and creates the contact or invoice in Xero; another can watch Xero for new or paid invoices and update Salesforce. Each scenario runs one way. Make's Salesforce guide notes that not all Salesforce editions have API access.

[Setup guide: Make: Salesforce app ↗](https://apps.make.com/salesforce)

Diagram of how Salesforce Sales Cloud and Xero connect. Salesforce Sales Cloud: Professional + API add-on · $1,250/mo for 10 seats. Xero: Early plan · $27/mo for 10 seats. Salesforce Sales Cloud sends a trigger (opportunity won) to Make Core ($10.59/mo), which performs an action in Xero (create the contact or invoice). Each automation runs one way.

Diagram: how Salesforce Sales Cloud and Xero connect, through Make Core, shown with the example automation described above. Drawn from the facts on this page.

 

### How do you set up Salesforce Sales Cloud + Xero?

1. Make sure your Salesforce org has API access: Enterprise and Unlimited include it, Professional needs the API add-on.
2. Log in to Make, create a scenario and add the Salesforce module Watch records as the trigger.
3. Connect Salesforce: click Create a connection, choose the Salesforce connection type, say whether you're using a Salesforce Sandbox, click Save and sign in.
4. Add the Xero module Create an Invoice (or Create a Contact). Connect Xero: click Create a connection, click Save and sign in to Xero if prompted.
5. Map the Salesforce fields into the Xero fields.
6. Click Run once in the toolbar to test it, then activate the scenario with the ON/OFF button on its details page. It runs every 15 minutes by default; click Every 15 minutes on the toolbar to change that.

Steps follow [Make's setup guide ↗](https://apps.make.com/salesforce), read Nov 12, 2026.

**Limitations:** This calculator models Salesforce Professional with the $25/user API add-on plus Make Core; Enterprise includes API access without the add-on. Partner apps from Xero's App Store are priced separately and aren't included. Each Make scenario runs one way, and real usage can push Make onto a bigger plan.

Sources (checked Nov 12, 2026): [Xero App Store: Integrate Xero with Salesforce ↗](https://apps.xero.com/us/collection/integrate-xero-with-salesforce) · [Make: Salesforce app ↗](https://apps.make.com/salesforce) · [Make: Xero app ↗](https://apps.make.com/xero) · [Make Help: Active and inactive scenarios ↗](https://help.make.com/active-and-inactive-scenarios) · [Make Help: Schedule a scenario ↗](https://help.make.com/schedule-a-scenario)

*Interactive cost calculator: open the web page to change team size, billing and add-ons.*

## Default 10-seat TCO summary

**Middleware integration costs $1,287.59/mo ($15,451.08/yr)** for a 10-seat team —
Salesforce Sales Cloud 'Professional' ($1,250.00/mo) + Xero 'Early' ($27.00/mo)
+ $10.59/mo middleware. No native connector exists for this pair.
Salesforce's $1,250.00 is the Professional plan ($100/user) plus the API add-on, which Salesforce sells through an account executive; this page models it at $25/user ($250 at 10 seats).

 

## Native vs middleware for Salesforce Sales Cloud + Xero

There's no native Salesforce Sales Cloud + Xero connector, so a connector such as Make or Zapier is the integration rather than an alternative. Each automation runs one way (a trigger in one tool, an action in the other), and the connector's bill grows with the number of tasks or operations you run.

Chart: Salesforce Sales Cloud + Xero: monthly cost for 10 seats by route: Make Core (modeled here) $1,287.59; Zapier Professional instead $1,306.99

Monthly cost for 10 seats by route, Salesforce Sales Cloud + Xero.

 

Integration routes compared for a 10-seat team

| Route | Plans | 10 seats / month | Sync |
| --- | --- | --- | --- |
| Make Core (modeled here) | Salesforce Sales Cloud 'Professional' + Xero 'Early' | $1,287.59 | 1-way per automation |
| Zapier Professional instead | Salesforce Sales Cloud 'Professional' + Xero 'Early' | $1,306.99 | 1-way per automation |

Connector prices are monthly-billing list prices: Zapier Professional $29.99 (zapier.com/pricing) and Make Core $10.59 (from third-party pricing reviews, because make.com blocks automated checks). Both bill by usage, so high volumes cost more.

Image: [Salesforce Sales Cloud + Xero integration cost summary: $1,287.59 a month for 10 seats, $10.59 of it is the hidden cost to connect; plans needed: Salesforce Sales Cloud Professional and Xero Early](https://stackcostmatrix.com/og/salesforce-and-xero.jpg)

## ✓ Verified Vendor Facts

- **Plan prices:** from each vendor's pricing page; any exception is flagged next to the date at the top.
- **Required tiers:** 'Professional' / 'Early' — the minimum plans this integration needs.
- **API & webhook gates:** audited in official developer docs (see spec matrix).
- **Native app availability:** No native app — connected via middleware.

Requirements checked: Nov 12, 2026; prices: Nov 3, 2026 (exceptions listed at the top) · Sources linked below.

## ! Hidden Cost Trap

Requires Salesforce Sales Cloud on the 'Professional' plan or higher — Requires Xero on the 'Early' plan or higher — Plus $10.59/month middleware on top of both tools.

Salesforce Sales Cloud minimum tier
:   'Professional'

Xero minimum tier
:   'Early'

Middleware fee
:   $10.59/mo

The hidden cost here is the connector: there's no native Salesforce Sales Cloud + Xero app, so you pay for Make Core ($10.59/mo) on top of both tools.

 [Connect Salesforce Sales Cloud + Xero via Make.com — the middleware this integration runs on](https://stackcostmatrix.com/go/make) 

Affiliate link — we may earn a commission at no extra cost to you.

## Side-by-side spec matrix

Side-by-side spec matrix

| Spec | Salesforce Sales Cloud | Xero |
| --- | --- | --- |
| Connection type | Middleware   Source: [Salesforce Sales Cloud docs ↗](https://developer.salesforce.com/) · [Xero docs ↗](https://developer.xero.com/) · Verified Nov 12, 2026 | |
| Data sync direction | 1-way (trigger → action) | |
| Setup time | 1–3 hours (difficulty 2/5) | |
| Native integration supported | No — requires middleware (Zapier / Make) | |
| API available (distinct from native app) | Yes  — API ≠ native UI; API enables custom/middleware builds Source: [Salesforce Sales Cloud API docs ↗](https://developer.salesforce.com/) · Verified Oct 17, 2026 | Yes  — API ≠ native UI; API enables custom/middleware builds Source: [Xero API docs ↗](https://developer.xero.com/) · Verified Oct 17, 2026 |
| API access at required tier | Yes  ('Professional') Web Services API add-on (modeled at $25/user) Source: [Salesforce developers: Supported editions ↗](https://developer.salesforce.com/docs/platform/api-rest/guide/intro-rest-compatible-editions.html) · Verified Nov 3, 2026 | Yes  ('Early') Limits set by the app's developer tier Source: [Xero developers: Pricing and tiers ↗](https://developer.xero.com/pricing) · Verified Nov 3, 2026 |
| Webhook support at required tier | No  ('Professional') Change Data Capture (Salesforce's change-event feed) isn't available on Professional, so sync runs through the REST API. Source: [Salesforce developers: Change Data Capture ↗](https://developer.salesforce.com/docs/atlas.en-us.change_data_capture.meta/change_data_capture/cdc_intro.htm) · Verified Nov 8, 2026 | Yes  ('Early') No plan requirement in Xero's webhook docs Source: [Xero developers: Webhooks ↗](https://developer.xero.com/documentation/guides/webhooks/overview) · Verified Nov 3, 2026 |

[Visit Salesforce Sales Cloud](https://stackcostmatrix.com/go/salesforce)  [Visit Xero](https://stackcostmatrix.com/go/xero)

Some outbound links may earn us a referral commission at no extra cost to you. [Read our affiliate disclosure](https://stackcostmatrix.com/about/).

## Salesforce Sales Cloud + Xero integration: frequently asked questions

### What are the minimum plan tiers required for the Salesforce Sales Cloud + Xero integration?

To unlock the integration, Salesforce Sales Cloud must be on the 'Professional' plan or higher and Xero must be on the 'Early' plan or higher. Those are each tool's cheapest plan with API access (Salesforce Sales Cloud 'Professional' at $1,250/mo and Xero 'Early' at $27/mo for 10 seats), so the integration doesn't force an upgrade.

### How much does the Salesforce Sales Cloud + Xero stack cost per month for a 10-person team?

At 10 seats with the required tiers (Salesforce Sales Cloud 'Professional' + Xero 'Early' + $10.59/month middleware), the stack costs $1,287.59 per month.

### Why does Salesforce Sales Cloud + Xero need middleware, and what does it cost?

The Salesforce Sales Cloud + Xero connection runs through middleware: neither vendor offers a native app for this pair, so this page models Make Core at $10.59 per month on top of both tools. Sync is one-way (a trigger in one tool runs an action in the other).

### What are the limitations of the Salesforce Sales Cloud + Xero integration?

This calculator models Salesforce Professional with the $25/user API add-on plus Make Core; Enterprise includes API access without the add-on. Partner apps from Xero's App Store are priced separately and aren't included. Each Make scenario runs one way, and real usage can push Make onto a bigger plan.

## Integrations related to Salesforce Sales Cloud + Xero

[All Salesforce integrations →](https://stackcostmatrix.com/salesforce-integrations-cost/) · [All Xero integrations →](https://stackcostmatrix.com/xero-integrations-cost/) · [Salesforce API access by plan →](https://stackcostmatrix.com/salesforce-api-access/) · [Xero API access by plan →](https://stackcostmatrix.com/xero-api-access/)

Part of our [CRM integration hidden-costs guide](https://stackcostmatrix.com/crm-integration-pricing-guide/).

[### Asana + Salesforce

Native](https://stackcostmatrix.com/stack/asana-and-salesforce/)[### HubSpot + Salesforce

Native](https://stackcostmatrix.com/stack/hubspot-and-salesforce/)[### Intercom + Salesforce

Native](https://stackcostmatrix.com/stack/intercom-and-salesforce/)[### Pipedrive + Salesforce

Middleware](https://stackcostmatrix.com/stack/pipedrive-and-salesforce/)[### Salesforce + Airtable

Native](https://stackcostmatrix.com/stack/salesforce-and-airtable/)[### Salesforce + Calendly

Native](https://stackcostmatrix.com/stack/salesforce-and-calendly/)

Requirements checked: Nov 12, 2026; prices: Nov 3, 2026 (exceptions listed at the top)

## Verified sources

Every figure on this page links to its source below; prices that don't come straight from the vendor's page are flagged next to the date:

- [Salesforce Sales Cloud official pricing ↗](https://www.salesforce.com/sales/pricing/)
- [Salesforce Sales Cloud API / developer docs ↗](https://developer.salesforce.com/)
- [Xero official pricing ↗](https://www.xero.com/pricing/)
- [Xero API / developer docs ↗](https://developer.xero.com/)
