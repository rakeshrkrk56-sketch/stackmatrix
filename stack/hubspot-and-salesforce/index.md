# HubSpot + Salesforce Integration Cost (2026)

> HubSpot + Salesforce needs HubSpot Professional and Salesforce Professional: $1,750/mo for 10 seats, including a +$500/mo forced upgrade.

Source page: https://stackcostmatrix.com/stack/hubspot-and-salesforce/  
Publisher: StackCostMatrix · Editor: Rakesh Kumar · Data licence: CC BY 4.0 (credit StackCostMatrix and link to https://stackcostmatrix.com)

---

[Home](https://stackcostmatrix.com/) / HubSpot + Salesforce Sales Cloud 

# HubSpot + Salesforce Sales Cloud Integration Cost (2026): True Price, Minimum Plan & Hidden API Fees

Big trap: HubSpot's native Salesforce connector needs a HubSpot Professional or Enterprise subscription — the free CRM can't use it. The cheapest route is Smart CRM Professional at $50 per seat a month ($45 on annual billing). Requires HubSpot on the 'Professional' plan and Salesforce Sales Cloud on the 'Professional' plan for full 2-way sync.

Edited by [Rakesh Kumar](https://stackcostmatrix.com/about/#editor), founder of StackCostMatrix | Integration requirements and prices checked against official vendor docs · Nov 3, 2026 (HubSpot prices: Nov 5, 2026; Salesforce prices: Oct 17, 2026) | [Spot an outdated price? Report a correction →](mailto:admin@stackcostmatrix.com?subject=Price%20Correction)

## How the HubSpot + Salesforce Sales Cloud integration works

HubSpot's own Salesforce connector syncs leads, contacts, accounts, opportunities and custom objects between the two CRMs, and can embed HubSpot contact, company and deal insights inside Salesforce. It suits teams that run marketing in HubSpot and sales in Salesforce.

**Limitations:** The connector is only available on HubSpot Professional or Enterprise subscriptions, every sync uses part of your Salesforce API call allowance, and the Salesforce user who connects it needs the API Enabled permission.

Sources (checked Nov 3, 2026): [HubSpot: Connect HubSpot and Salesforce ↗](https://knowledge.hubspot.com/salesforce/install-the-hubspot-salesforce-integration) · [HubSpot Marketplace: Salesforce ↗](https://ecosystem.hubspot.com/marketplace/listing/salesforce)

*Interactive cost calculator: open the web page to change team size, billing and add-ons.*

## Default 10-seat TCO summary

**Native integration costs $1,750.00/mo ($21,000.00/yr)** for a 10-seat team —
HubSpot 'Professional' ($500.00/mo) + Salesforce Sales Cloud 'Professional' ($1,250.00/mo),
no middleware required.
Alternative: skip the native tier upgrade and run via Make/Zapier middleware for ~$1,260.59/mo all-in (adds a third-party dependency).

## Native vs middleware for HubSpot + Salesforce Sales Cloud

The native path runs on the required tiers (HubSpot 'Professional' + Salesforce Sales Cloud 'Professional') at $1,750.00/mo for a 10-seat team, with 2-way sync and no middleware fee. The middleware path — the cheapest API-capable tiers plus about $10.59/mo for Make Core — comes to $1,260.59/mo all-in, which is cheaper on paper because it skips the $500.00/mo forced tier upgrade. The trade-off: you replace the native connector with a third-party dependency, sync becomes 1-way (trigger → action) instead of 2-way, and Make Core's fee covers a fixed monthly allowance of credits — whether that covers your volume is not verified for this pair.

API access at the required tiers: HubSpot Yes, Salesforce Sales Cloud Yes (see the spec matrix). That API access is what the middleware path runs on.

Integration routes compared for a 10-seat team

| Route | Plans | 10 seats / month | Sync |
| --- | --- | --- | --- |
| Native HubSpot + Salesforce Sales Cloud connector | HubSpot 'Professional' + Salesforce Sales Cloud 'Professional' | $1,750.00 | As listed in the spec matrix |
| Make Core on the cheapest API plans | HubSpot 'Free' + Salesforce Sales Cloud 'Professional' + Make | $1,260.59 | 1-way per scenario |

Make Core's $10.59 monthly price comes from third-party pricing reviews, because make.com blocks automated checks; Zapier's is from zapier.com/pricing.

## ✓ Verified Vendor Facts

- **Plan prices:** from each vendor's pricing page; any exception is flagged next to the date at the top.
- **Required tiers:** 'Professional' / 'Professional' — the minimum plans this integration needs.
- **API & webhook gates:** audited in official developer docs (see spec matrix).
- **Native app availability:** Native app available in vendor marketplace.

Last checked: Nov 3, 2026 (exceptions listed at the top) · Sources linked below.

## ◐ Model Estimates (your assumptions)

- **Usage / task add-ons:** middleware overage costs you enter above.
- **Setup & maintenance:** implementation hours and ongoing ops — adjust freely.
- **Annual billing saving:** uses each vendor's published annual price where one exists; otherwise no discount is applied.

Estimates never change the verified facts — they only model your scenario.

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

## Frequently asked questions

### What are the minimum plan tiers required for the HubSpot + Salesforce Sales Cloud integration?

To unlock the native integration, HubSpot must be on the 'Professional' plan or higher and Salesforce Sales Cloud must be on the 'Professional' plan or higher. HubSpot's cheapest plan with API access is 'Free', so 'Professional' is a $500/mo upgrade at 10 seats.

### How much does the HubSpot + Salesforce Sales Cloud stack cost per month for a 10-person team?

At 10 seats with the required tiers (HubSpot 'Professional' + Salesforce Sales Cloud 'Professional'), the stack costs $1,750.00 per month.

### Is the HubSpot + Salesforce Sales Cloud integration native, and would Make or Zapier be cheaper?

The HubSpot + Salesforce Sales Cloud connection is native — no third-party middleware subscription is required. Connecting through Make on the cheapest API plans would cost about $1,260.59/month in total instead of $1,750.00, but you'd replace the native connector with a third-party automation.

### What are the limitations of the HubSpot + Salesforce Sales Cloud integration?

The connector is only available on HubSpot Professional or Enterprise subscriptions, every sync uses part of your Salesforce API call allowance, and the Salesforce user who connects it needs the API Enabled permission.

## Related integrations

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
