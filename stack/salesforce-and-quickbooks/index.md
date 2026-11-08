# Salesforce + QuickBooks Integration: Setup & Cost (2026)

> How the Salesforce Sales Cloud + QuickBooks Online integration works and how to set it up, plus the plans it needs and the 10-seat cost ($1,298.59/mo).

Source page: https://stackcostmatrix.com/stack/salesforce-and-quickbooks/  
Publisher: StackCostMatrix · Editor: Rakesh Kumar · Data licence: CC BY 4.0 (credit StackCostMatrix and link to https://stackcostmatrix.com)

---

[Home](https://stackcostmatrix.com/) / Salesforce Sales Cloud + QuickBooks Online 

# Salesforce Sales Cloud + QuickBooks Online Integration (2026): How It Works, Setup & True Cost

Salesforce doesn't build a QuickBooks connector; AppExchange apps such as Breadwinner (from $310/mo) or Make Core link them through Salesforce's API, which Professional Edition gets only as a paid add-on. Requires Salesforce Sales Cloud on the 'Professional' plan and QuickBooks Online on the 'Simple Start' plan. Route it through Make Core ($10.59/mo, or $9/mo billed annually).

Edited by [Rakesh Kumar](https://stackcostmatrix.com/about/#editor), founder of StackCostMatrix | Integration requirements checked against official vendor docs · Nov 4, 2026 · Prices checked · Nov 3, 2026 (Salesforce prices: Oct 17, 2026; QuickBooks prices: Nov 4, 2026; Make fee: $9 annual price Oct 17, 2026; $10.59 monthly price from third-party pricing reviews, Nov 3, 2026, as make.com blocks automated checks) | [Spot an outdated price? Report a correction →](mailto:admin@stackcostmatrix.com?subject=Price%20Correction)

## How the Salesforce Sales Cloud + QuickBooks Online integration works

**Does Salesforce Sales Cloud integrate with QuickBooks Online?** Not with a Salesforce-built connector. Salesforce points to AppExchange apps such as Breadwinner, which starts at $310 a month, and Make or Zapier can connect the two through Salesforce's API, which Professional Edition only gets as a paid add-on.

With Make, a scenario watches Salesforce, for example for a won opportunity, and creates the customer or invoice in QuickBooks Online, or the other way round. Breadwinner is a native Salesforce app with real-time QuickBooks sync, priced separately.

### How to set it up

**1.** Make sure your Salesforce org has API access: Enterprise or Unlimited include it, Professional needs the API add-on.

**2.** In Make, create a scenario and connect your Salesforce account and your QuickBooks account.

**3.** Pick a trigger, such as a won opportunity, and a QuickBooks action, such as creating an invoice, then map the fields and turn the scenario on.

**Limitations:** This calculator models Salesforce Professional with the $25/user API add-on plus Make Core; Enterprise includes API access without the add-on. Breadwinner's own price, from $310 a month, isn't included. Each Make scenario runs one way.

Sources (checked Nov 4, 2026): [Make: Salesforce app ↗](https://apps.make.com/salesforce) · [Salesforce developers: Supported editions ↗](https://developer.salesforce.com/docs/platform/api-rest/guide/intro-rest-compatible-editions.html) · [Breadwinner: Pricing ↗](https://breadwinner.com/pricing) · [Make: QuickBooks app ↗](https://apps.make.com/quickbooks)

*Interactive cost calculator: open the web page to change team size, billing and add-ons.*

## Default 10-seat TCO summary

**Middleware integration costs $1,298.59/mo ($15,583.08/yr)** for a 10-seat team —
Salesforce Sales Cloud 'Professional' ($1,250.00/mo) + QuickBooks Online 'Simple Start' ($38.00/mo)
+ $10.59/mo middleware. No native connector exists for this pair.

## Native vs middleware for Salesforce Sales Cloud + QuickBooks Online

No native connector exists for this pair, so middleware is not an alternative — it is the integration. The modeled middleware cost is $10.59/mo on top of both tools, for $1,298.59/mo all-in at 10 seats on the modeled tiers (Salesforce Sales Cloud 'Professional' + QuickBooks Online 'Simple Start'). Sync is 1-way (trigger → action). The middleware figure is the modeled cost for this pair; your actual middleware bill scales with task and operation volume, which is not verified here — check your expected volume against the middleware plan before budgeting.

API access at the required tiers: Salesforce Sales Cloud Yes, QuickBooks Online Yes (see the spec matrix). That API access is what the middleware path runs on.

Integration routes compared for a 10-seat team

| Route | Plans | 10 seats / month | Sync |
| --- | --- | --- | --- |
| Make Core (modeled here) | Salesforce Sales Cloud 'Professional' + QuickBooks Online 'Simple Start' | $1,298.59 | 1-way per automation |
| Zapier Professional instead | Salesforce Sales Cloud 'Professional' + QuickBooks Online 'Simple Start' | $1,317.99 | 1-way per automation |

## ✓ Verified Vendor Facts

- **Plan prices:** per-seat costs verified on official vendor pricing pages.
- **Required tiers:** 'Professional' / 'Simple Start' — the minimum plans that unlock the native integration.
- **API & webhook gates:** audited in official developer docs (see spec matrix).
- **Native app availability:** No native app — connected via middleware.

Last checked: Nov 4, 2026 (exceptions listed at the top) · Sources linked below.

## ◐ Model Estimates (your assumptions)

- **Usage / task add-ons:** middleware overage costs you enter above.
- **Setup & maintenance:** implementation hours and ongoing ops — adjust freely.
- **Annual billing saving:** uses each vendor's published annual price where one exists, including the middleware or connector fee; otherwise no discount is applied.

Estimates never change the verified facts — they only model your scenario.

## ! Hidden Cost Trap

Requires Salesforce Sales Cloud on the 'Professional' plan or higher — Requires QuickBooks Online on the 'Simple Start' plan or higher — Plus $10.59/month middleware on top of both tools.

Salesforce Sales Cloud minimum tier
:   'Professional'

QuickBooks Online minimum tier
:   'Simple Start'

Middleware fee
:   $10.59/mo

The hidden cost here is the connector: there's no native Salesforce Sales Cloud + QuickBooks Online app, so you pay for Make Core ($10.59/mo) on top of both tools.

 [Connect Salesforce Sales Cloud + QuickBooks Online via Make.com — the middleware this integration runs on](https://stackcostmatrix.com/go/make) 

Affiliate link — we may earn a commission at no extra cost to you.

## Side-by-side spec matrix

Side-by-side spec matrix

| Spec | Salesforce Sales Cloud | QuickBooks Online |
| --- | --- | --- |
| Connection type | Middleware   Source: [Salesforce Sales Cloud docs ↗](https://developer.salesforce.com/) · [QuickBooks Online docs ↗](https://developer.intuit.com/app/developer/qbo/docs/get-started) · Verified Nov 4, 2026 | |
| Data sync direction | 1-way (trigger → action) | |
| Setup time | Half a day (difficulty 3/5) | |
| Native integration supported | No — requires middleware (Zapier / Make) | |
| API available (distinct from native app) | Yes  — API ≠ native UI; API enables custom/middleware builds Source: [Salesforce Sales Cloud API docs ↗](https://developer.salesforce.com/) · Verified Oct 17, 2026 | Yes  — API ≠ native UI; API enables custom/middleware builds Source: [QuickBooks Online API docs ↗](https://developer.intuit.com/app/developer/qbo/docs/get-started) · Verified Oct 17, 2026 |
| API access at required tier | Yes  ('Professional') Web Services API add-on (modeled at $25/user) Source: [Salesforce developers: Supported editions ↗](https://developer.salesforce.com/docs/platform/api-rest/guide/intro-rest-compatible-editions.html) · Verified Nov 3, 2026 | Yes  ('Simple Start') Any paid plan (Zapier, Make and Mailchimp name no tier) Source: [Zapier help: QuickBooks Online API prerequisites ↗](https://help.zapier.com/hc/en-us/articles/8495935103885) · Verified Nov 3, 2026 |
| Webhook support at required tier | No  ('Professional') Change Data Capture (Salesforce's change-event feed) isn't available on Professional, so sync runs through the REST API. Source: [Salesforce developers: Change Data Capture ↗](https://developer.salesforce.com/docs/atlas.en-us.change_data_capture.meta/change_data_capture/cdc_intro.htm) · Verified Nov 8, 2026 | Yes  ('Simple Start') App-level webhooks Source: [Intuit developers: Webhooks ↗](https://developer.intuit.com/app/developer/qbo/docs/develop/webhooks) · Verified Nov 3, 2026 |

[Visit Salesforce Sales Cloud](https://stackcostmatrix.com/go/salesforce)  [Visit QuickBooks Online](https://stackcostmatrix.com/go/quickbooks)

Some outbound links may earn us a referral commission at no extra cost to you. [Read our affiliate disclosure](https://stackcostmatrix.com/about/).

## Frequently asked questions

### What are the minimum plan tiers required for the Salesforce Sales Cloud + QuickBooks Online integration?

To unlock the integration, Salesforce Sales Cloud must be on the 'Professional' plan or higher and QuickBooks Online must be on the 'Simple Start' plan or higher. Neither plan is an upgrade over the cheapest plan with API access.

### How much does the Salesforce Sales Cloud + QuickBooks Online stack cost per month for a 10-person team?

At 10 seats with the required tiers (Salesforce Sales Cloud 'Professional' + QuickBooks Online 'Simple Start' + $10.59/month middleware), the stack costs $1,298.59 per month.

### Why does Salesforce Sales Cloud + QuickBooks Online need middleware, and what does it cost?

The Salesforce Sales Cloud + QuickBooks Online connection runs through middleware: neither vendor offers a native app for this pair, so this page models Make Core at $10.59 per month on top of both tools. Sync is one-way (a trigger in one tool runs an action in the other).

### What are the limitations of the Salesforce Sales Cloud + QuickBooks Online integration?

This calculator models Salesforce Professional with the $25/user API add-on plus Make Core; Enterprise includes API access without the add-on. Breadwinner's own price, from $310 a month, isn't included. Each Make scenario runs one way.

## Related integrations

[All Salesforce integrations →](https://stackcostmatrix.com/salesforce-integrations-cost/) · [All QuickBooks integrations →](https://stackcostmatrix.com/quickbooks-integrations-cost/) · [Salesforce API access by plan →](https://stackcostmatrix.com/salesforce-api-access/) · [QuickBooks API access by plan →](https://stackcostmatrix.com/quickbooks-api-access/)

Part of our [CRM integration hidden-costs guide](https://stackcostmatrix.com/crm-integration-pricing-guide/).

[### HubSpot + Salesforce

Native](https://stackcostmatrix.com/stack/hubspot-and-salesforce/)[### Pipedrive + Salesforce

Middleware](https://stackcostmatrix.com/stack/pipedrive-and-salesforce/)[### Salesforce + Mailchimp

Native](https://stackcostmatrix.com/stack/salesforce-and-mailchimp/)[### Salesforce + Slack

Native](https://stackcostmatrix.com/stack/salesforce-and-slack/)[### Salesforce + Stripe

Native](https://stackcostmatrix.com/stack/salesforce-and-stripe/)[### Salesforce + Zendesk

Native](https://stackcostmatrix.com/stack/salesforce-and-zendesk/)

Last checked: Nov 4, 2026 (exceptions listed at the top)

## Verified sources

Every figure on this page links to its source below; prices that don't come straight from the vendor's page are flagged next to the date:

- [Salesforce Sales Cloud official pricing ↗](https://www.salesforce.com/sales/pricing/)
- [Salesforce Sales Cloud API / developer docs ↗](https://developer.salesforce.com/)
- [QuickBooks Online official pricing ↗](https://quickbooks.intuit.com/pricing/)
- [QuickBooks Online API / developer docs ↗](https://developer.intuit.com/app/developer/qbo/docs/get-started)
