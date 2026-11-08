# Pipedrive + Salesforce Integration: Setup & Cost (2026)

> How the Pipedrive + Salesforce Sales Cloud integration works and how to set it up, plus the plans it needs and the 10-seat cost ($1,400.59/mo).

Source page: https://stackcostmatrix.com/stack/pipedrive-and-salesforce/  
Publisher: StackCostMatrix · Editor: Rakesh Kumar · Data licence: CC BY 4.0 (credit StackCostMatrix and link to https://stackcostmatrix.com)

---

[Home](https://stackcostmatrix.com/) / Pipedrive + Salesforce Sales Cloud 

# Pipedrive + Salesforce Sales Cloud Integration (2026): How It Works, Setup & True Cost

Pipedrive and Salesforce don't build an integration with each other; Make Core connects them through both APIs, and Salesforce Professional needs its paid API add-on for that. Requires Pipedrive on the 'Lite' plan and Salesforce Sales Cloud on the 'Professional' plan. Route it through Make Core ($10.59/mo, or $9/mo billed annually).

Edited by [Rakesh Kumar](https://stackcostmatrix.com/about/#editor), founder of StackCostMatrix | Integration requirements checked against official vendor docs · Nov 4, 2026 · Prices checked · Nov 3, 2026 (Pipedrive prices: from an indexed copy of its pricing page; Salesforce prices: Oct 17, 2026; Make fee: $9 annual price Oct 17, 2026; $10.59 monthly price from third-party pricing reviews, Nov 3, 2026, as make.com blocks automated checks) | [Spot an outdated price? Report a correction →](mailto:admin@stackcostmatrix.com?subject=Price%20Correction)

## How the Pipedrive + Salesforce Sales Cloud integration works

**Does Pipedrive integrate with Salesforce Sales Cloud?** Not natively. Pipedrive and Salesforce don't build an integration with each other, but Make or Zapier connects them through both tools' APIs; Salesforce Professional needs its paid API add-on for that.

A Make scenario watches one CRM and acts in the other, for example creating a Salesforce lead or contact when a deal or person is added in Pipedrive. Each scenario runs one way, so keeping both sides in step needs one scenario per direction.

### How to set it up

**1.** Make sure your Salesforce org has API access: Enterprise or Unlimited include it, Professional needs the API add-on.

**2.** In Make, create a scenario and connect your Pipedrive and Salesforce accounts.

**3.** Pick a trigger in one tool and an action in the other, map the fields and turn the scenario on.

**Limitations:** This calculator models Salesforce Professional with the $25/user API add-on; Enterprise includes API access without it. Pipedrive's API is available on every plan, with rate limits that rise with the plan. Real usage can push Make onto a bigger plan.

Sources (checked Nov 4, 2026): [Make: Salesforce app ↗](https://apps.make.com/salesforce) · [Salesforce developers: Supported editions ↗](https://developer.salesforce.com/docs/platform/api-rest/guide/intro-rest-compatible-editions.html) · [Pipedrive developers: Rate limiting ↗](https://pipedrive.readme.io/docs/core-api-concepts-rate-limiting)

*Interactive cost calculator: open the web page to change team size, billing and add-ons.*

## Default 10-seat TCO summary

**Middleware integration costs $1,400.59/mo ($16,807.08/yr)** for a 10-seat team —
Pipedrive 'Lite' ($140.00/mo) + Salesforce Sales Cloud 'Professional' ($1,250.00/mo)
+ $10.59/mo middleware. No native connector exists for this pair.

## Native vs middleware for Pipedrive + Salesforce Sales Cloud

No native connector exists for this pair, so middleware is not an alternative — it is the integration. The modeled middleware cost is $10.59/mo on top of both tools, for $1,400.59/mo all-in at 10 seats on the modeled tiers (Pipedrive 'Lite' + Salesforce Sales Cloud 'Professional'). Sync is 1-way (trigger → action). The middleware figure is the modeled cost for this pair; your actual middleware bill scales with task and operation volume, which is not verified here — check your expected volume against the middleware plan before budgeting.

API access at the required tiers: Pipedrive Yes, Salesforce Sales Cloud Yes (see the spec matrix). That API access is what the middleware path runs on.

Integration routes compared for a 10-seat team

| Route | Plans | 10 seats / month | Sync |
| --- | --- | --- | --- |
| Make Core (modeled here) | Pipedrive 'Lite' + Salesforce Sales Cloud 'Professional' | $1,400.59 | 1-way per automation |
| Zapier Professional instead | Pipedrive 'Lite' + Salesforce Sales Cloud 'Professional' | $1,419.99 | 1-way per automation |

## ✓ Verified Vendor Facts

- **Plan prices:** per-seat costs verified on official vendor pricing pages.
- **Required tiers:** 'Lite' / 'Professional' — the minimum plans that unlock the native integration.
- **API & webhook gates:** audited in official developer docs (see spec matrix).
- **Native app availability:** No native app — connected via middleware.

Last checked: Nov 4, 2026 (exceptions listed at the top) · Sources linked below.

## ◐ Model Estimates (your assumptions)

- **Usage / task add-ons:** middleware overage costs you enter above.
- **Setup & maintenance:** implementation hours and ongoing ops — adjust freely.
- **Annual billing saving:** uses each vendor's published annual price where one exists, including the middleware or connector fee; otherwise no discount is applied.

Estimates never change the verified facts — they only model your scenario.

## ! Hidden Cost Trap

Requires Pipedrive on the 'Lite' plan or higher — Requires Salesforce Sales Cloud on the 'Professional' plan or higher — Plus $10.59/month middleware on top of both tools.

Pipedrive minimum tier
:   'Lite'

Salesforce Sales Cloud minimum tier
:   'Professional'

Middleware fee
:   $10.59/mo

The hidden cost here is the connector: there's no native Pipedrive + Salesforce Sales Cloud app, so you pay for Make Core ($10.59/mo) on top of both tools.

 [Connect Pipedrive + Salesforce Sales Cloud via Make.com — the middleware this integration runs on](https://stackcostmatrix.com/go/make) 

Affiliate link — we may earn a commission at no extra cost to you.

## Side-by-side spec matrix

Side-by-side spec matrix

| Spec | Pipedrive | Salesforce Sales Cloud |
| --- | --- | --- |
| Connection type | Middleware   Source: [Pipedrive docs ↗](https://developers.pipedrive.com/docs/api/v1) · [Salesforce Sales Cloud docs ↗](https://developer.salesforce.com/) · Verified Nov 4, 2026 | |
| Data sync direction | 1-way (trigger → action) | |
| Setup time | Under 1 hour (difficulty 1/5) | |
| Native integration supported | No — requires middleware (Zapier / Make) | |
| API available (distinct from native app) | Yes  — API ≠ native UI; API enables custom/middleware builds Source: [Pipedrive API docs ↗](https://developers.pipedrive.com/docs/api/v1) · Verified Oct 17, 2026 | Yes  — API ≠ native UI; API enables custom/middleware builds Source: [Salesforce Sales Cloud API docs ↗](https://developer.salesforce.com/) · Verified Oct 17, 2026 |
| API access at required tier | Yes  ('Lite') 20 req/2 s · daily budget ×1 Source: [Pipedrive developers: Rate limiting ↗](https://pipedrive.readme.io/docs/core-api-concepts-rate-limiting) · Verified Nov 3, 2026 | Yes  ('Professional') Web Services API add-on (modeled at $25/user) Source: [Salesforce developers: Supported editions ↗](https://developer.salesforce.com/docs/platform/api-rest/guide/intro-rest-compatible-editions.html) · Verified Nov 3, 2026 |
| Webhook support at required tier | Yes  ('Lite') Source: [Pipedrive: Automations webhook requests ↗](https://support.pipedrive.com/en/article/automations-webhook-requests) · Verified Nov 3, 2026 | No  ('Professional') Change Data Capture (Salesforce's change-event feed) isn't available on Professional, so sync runs through the REST API. Source: [Salesforce developers: Change Data Capture ↗](https://developer.salesforce.com/docs/atlas.en-us.change_data_capture.meta/change_data_capture/cdc_intro.htm) · Verified Nov 8, 2026 |

[Visit Pipedrive](https://stackcostmatrix.com/go/pipedrive)  [Visit Salesforce Sales Cloud](https://stackcostmatrix.com/go/salesforce)

Some outbound links may earn us a referral commission at no extra cost to you. [Read our affiliate disclosure](https://stackcostmatrix.com/about/).

## Frequently asked questions

### What are the minimum plan tiers required for the Pipedrive + Salesforce Sales Cloud integration?

To unlock the integration, Pipedrive must be on the 'Lite' plan or higher and Salesforce Sales Cloud must be on the 'Professional' plan or higher. Neither plan is an upgrade over the cheapest plan with API access.

### How much does the Pipedrive + Salesforce Sales Cloud stack cost per month for a 10-person team?

At 10 seats with the required tiers (Pipedrive 'Lite' + Salesforce Sales Cloud 'Professional' + $10.59/month middleware), the stack costs $1,400.59 per month.

### Why does Pipedrive + Salesforce Sales Cloud need middleware, and what does it cost?

The Pipedrive + Salesforce Sales Cloud connection runs through middleware: neither vendor offers a native app for this pair, so this page models Make Core at $10.59 per month on top of both tools. Sync is one-way (a trigger in one tool runs an action in the other).

### What are the limitations of the Pipedrive + Salesforce Sales Cloud integration?

This calculator models Salesforce Professional with the $25/user API add-on; Enterprise includes API access without it. Pipedrive's API is available on every plan, with rate limits that rise with the plan. Real usage can push Make onto a bigger plan.

## Related integrations

[All Pipedrive integrations →](https://stackcostmatrix.com/pipedrive-integrations-cost/) · [All Salesforce integrations →](https://stackcostmatrix.com/salesforce-integrations-cost/) · [Pipedrive API access by plan →](https://stackcostmatrix.com/pipedrive-api-access/) · [Salesforce API access by plan →](https://stackcostmatrix.com/salesforce-api-access/)

Part of our [CRM integration hidden-costs guide](https://stackcostmatrix.com/crm-integration-pricing-guide/).

[### ActiveCampaign + Pipedrive

Native](https://stackcostmatrix.com/stack/activecampaign-and-pipedrive/)[### HubSpot + Pipedrive

Middleware](https://stackcostmatrix.com/stack/hubspot-and-pipedrive/)[### Pipedrive + Calendly

Middleware](https://stackcostmatrix.com/stack/pipedrive-and-calendly/)[### Pipedrive + Mailchimp

Native](https://stackcostmatrix.com/stack/pipedrive-and-mailchimp/)[### Pipedrive + QuickBooks

Native](https://stackcostmatrix.com/stack/pipedrive-and-quickbooks/)[### Pipedrive + Slack

Native](https://stackcostmatrix.com/stack/pipedrive-and-slack/)

Last checked: Nov 4, 2026 (exceptions listed at the top)

## Verified sources

Every figure on this page links to its source below; prices that don't come straight from the vendor's page are flagged next to the date:

- [Pipedrive official pricing ↗](https://www.pipedrive.com/pricing)
- [Pipedrive API / developer docs ↗](https://developers.pipedrive.com/docs/api/v1)
- [Salesforce Sales Cloud official pricing ↗](https://www.salesforce.com/sales/pricing/)
- [Salesforce Sales Cloud API / developer docs ↗](https://developer.salesforce.com/)
