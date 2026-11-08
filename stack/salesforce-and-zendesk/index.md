# Salesforce + Zendesk Integration Cost (2026)

> Salesforce + Zendesk needs Salesforce Professional and Zendesk Suite Team: $1,940/mo for 10 seats, with no extra cost to connect them.

Source page: https://stackcostmatrix.com/stack/salesforce-and-zendesk/  
Publisher: StackCostMatrix · Editor: Rakesh Kumar · Data licence: CC BY 4.0 (credit StackCostMatrix and link to https://stackcostmatrix.com)

---

[Home](https://stackcostmatrix.com/) / Salesforce Sales Cloud + Zendesk 

# Salesforce Sales Cloud + Zendesk Integration Cost (2026): Plans, Setup & True Price

Zendesk's Salesforce integration works on every Zendesk Suite plan from Team up, but Salesforce Professional still needs the $25/user API add-on. Requires Salesforce Sales Cloud on the 'Professional' plan and Zendesk on the 'Suite Team' plan.

Edited by [Rakesh Kumar](https://stackcostmatrix.com/about/#editor), founder of StackCostMatrix | Integration requirements and prices checked against official vendor docs · Nov 3, 2026 (Salesforce prices: Oct 17, 2026) | [Spot an outdated price? Report a correction →](mailto:admin@stackcostmatrix.com?subject=Price%20Correction)

## How the Salesforce Sales Cloud + Zendesk integration works

Zendesk's Salesforce integration creates and updates Zendesk organizations from Salesforce accounts (and users from contacts or leads), syncs Zendesk tickets to Salesforce Cases, and can show Zendesk tickets inside Salesforce with Ticket View.

**Limitations:** It needs Salesforce Enterprise or above, or Professional with the API add-on. Account data syncs one way, from Salesforce to Zendesk, and ticket comments aren't synced to a Case field (Ticket View can display them).

Sources (checked Nov 3, 2026): [Zendesk: Connecting Salesforce to Zendesk ↗](https://support.zendesk.com/hc/en-us/articles/4408821555482-Connecting-your-Salesforce-organization-to-Zendesk) · [Zendesk: Data sync from Salesforce ↗](https://support.zendesk.com/hc/en-us/articles/4408828539290-Configuring-data-sync-from-Salesforce-to-Zendesk) · [Zendesk: Ticket sync to Salesforce ↗](https://support.zendesk.com/hc/en-us/articles/4408828449050-Setting-up-ticket-sync-from-Zendesk-to-Salesforce)

*Interactive cost calculator: open the web page to change team size, billing and add-ons.*

## Default 10-seat TCO summary

**Native integration costs $1,940.00/mo ($23,280.00/yr)** for a 10-seat team —
Salesforce Sales Cloud 'Professional' ($1,250.00/mo) + Zendesk 'Suite Team' ($690.00/mo),
no middleware required.
Middleware via Make/Zapier would add ~$10.59/mo on top of the cheapest API-capable tiers ($1,950.59/mo all-in) — the native path is cheaper.

## Native vs middleware for Salesforce Sales Cloud + Zendesk

The native path runs on the required tiers (Salesforce Sales Cloud 'Professional' + Zendesk 'Suite Team') at $1,940.00/mo for a 10-seat team, with no middleware fee. The middleware path — the cheapest API-capable tiers plus about $10.59/mo for Make Core — would cost $1,950.59/mo all-in, so on cost alone there is no reason to switch: middleware would only make sense if you already run other automations through it.

API access at the required tiers: Salesforce Sales Cloud Yes, Zendesk Yes (see the spec matrix). That API access is what the middleware path runs on.

Integration routes compared for a 10-seat team

| Route | Plans | 10 seats / month | Sync |
| --- | --- | --- | --- |
| Native Salesforce Sales Cloud + Zendesk connector | Salesforce Sales Cloud 'Professional' + Zendesk 'Suite Team' | $1,940.00 | As listed in the spec matrix |
| Make Core on the cheapest API plans | Salesforce Sales Cloud 'Professional' + Zendesk 'Suite Team' + Make | $1,950.59 | 1-way per scenario |

Make Core's $10.59 monthly price comes from third-party pricing reviews, because make.com blocks automated checks; Zapier's is from zapier.com/pricing.

## ✓ Verified Vendor Facts

- **Plan prices:** from each vendor's pricing page; any exception is flagged next to the date at the top.
- **Required tiers:** 'Professional' / 'Suite Team' — the minimum plans this integration needs.
- **API & webhook gates:** audited in official developer docs (see spec matrix).
- **Native app availability:** Native app available in vendor marketplace.

Last checked: Nov 3, 2026 (exceptions listed at the top) · Sources linked below.

## ◐ Model Estimates (your assumptions)

- **Usage / task add-ons:** middleware overage costs you enter above.
- **Setup & maintenance:** implementation hours and ongoing ops — adjust freely.
- **Annual billing saving:** uses each vendor's published annual price where one exists; otherwise no discount is applied.

Estimates never change the verified facts — they only model your scenario.

## ! Plan requirements

Requires Salesforce Sales Cloud on the 'Professional' plan or higher — Requires Zendesk on the 'Suite Team' plan or higher.

Salesforce Sales Cloud minimum tier
:   'Professional'

Zendesk minimum tier
:   'Suite Team'

Middleware fee
:   None

No hidden cost: the native connector works on Salesforce Sales Cloud 'Professional' and Zendesk 'Suite Team', so connecting them adds nothing to what you already pay for the two tools.

✓ Native is the cheapest path — $0 incremental integration cost

The native Salesforce Sales Cloud + Zendesk connector runs on the required tiers with no middleware fee
and no forced tier upgrade — paying for middleware here would only add cost.

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

## Frequently asked questions

### What are the minimum plan tiers required for the Salesforce Sales Cloud + Zendesk integration?

To unlock the native integration, Salesforce Sales Cloud must be on the 'Professional' plan or higher and Zendesk must be on the 'Suite Team' plan or higher. Neither plan is an upgrade over the cheapest plan with API access.

### How much does the Salesforce Sales Cloud + Zendesk stack cost per month for a 10-person team?

At 10 seats with the required tiers (Salesforce Sales Cloud 'Professional' + Zendesk 'Suite Team'), the stack costs $1,940.00 per month.

### Is the Salesforce Sales Cloud + Zendesk integration native, and would Make or Zapier be cheaper?

The Salesforce Sales Cloud + Zendesk connection is native — no third-party middleware subscription is required. Make would cost about $1,950.59/month on the cheapest API plans, more than the native route, so it only makes sense if you already use it.

### What are the limitations of the Salesforce Sales Cloud + Zendesk integration?

It needs Salesforce Enterprise or above, or Professional with the API add-on. Account data syncs one way, from Salesforce to Zendesk, and ticket comments aren't synced to a Case field (Ticket View can display them).

## Related integrations

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
