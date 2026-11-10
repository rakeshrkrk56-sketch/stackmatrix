# HubSpot + Zendesk Integration (2026): How It Works, Setup & True Cost

> How the HubSpot + Zendesk integration works, how to set it up, and the plans it needs: HubSpot Free + Zendesk Suite Team, $690/mo for 10 seats.

Source page: https://stackcostmatrix.com/stack/hubspot-and-zendesk/  
Publisher: StackCostMatrix · Editor: Rakesh Kumar · Data licence: CC BY 4.0 (credit StackCostMatrix and link to https://stackcostmatrix.com)

---

[Home](https://stackcostmatrix.com/) / HubSpot + Zendesk 

Zendesk tickets show on HubSpot contact timelines on any HubSpot plan, but only on contacts and only one way. Requires HubSpot on the 'Free' plan and Zendesk on the 'Suite Team' plan.

Edited by [Rakesh Kumar](https://stackcostmatrix.com/about/#editor), founder of StackCostMatrix | Integration requirements and prices checked against official vendor docs · Nov 3, 2026 | [Spot an outdated price? Report a correction →](mailto:admin@stackcostmatrix.com?subject=Price%20Correction)

## How the HubSpot + Zendesk integration works

**Does HubSpot integrate with Zendesk?** Yes. Zendesk's HubSpot integration shows Zendesk tickets, including the conversation, status and CSAT rating, on HubSpot contact timelines, and it works with every HubSpot subscription.

Zendesk's HubSpot integration adds Zendesk ticket events and chat transcripts to the HubSpot contact timeline, and creates new HubSpot contacts for ticket requesters who don't match an existing contact. It's available on all HubSpot subscriptions.

[Setup guide: Zendesk: Zendesk Support for HubSpot ↗](https://support.zendesk.com/hc/en-us/articles/4408884090650-Setting-up-the-Zendesk-Support-for-HubSpot-integration)

### How to set it up

1. Go to hubspot.zendesk-integrations.com/zendesk and enter your Zendesk subdomain.
2. Authorize the Zendesk app, then allow access to HubSpot.
3. In HubSpot, open any contact, go to the Activities tab, click Filter activity and tick Integrations > Zendesk.
4. Zendesk creates three triggers (ticket created, solved and CSAT rated) that send tickets to HubSpot; edit their conditions to control which tickets sync.

**Limitations:** Tickets can only be shown on the contact timeline, not on companies or deals, and data only flows from Zendesk into HubSpot. You need a Zendesk Suite plan from Team up.

Sources (checked Nov 3, 2026): [Zendesk: Zendesk Support for HubSpot ↗](https://support.zendesk.com/hc/en-us/articles/4408884090650-Setting-up-the-Zendesk-Support-for-HubSpot-integration) · [HubSpot Marketplace: Zendesk ↗](https://ecosystem.hubspot.com/marketplace/listing/zendesk)

*Interactive cost calculator: open the web page to change team size, billing and add-ons.*

## Default 10-seat TCO summary

**Native integration costs $690.00/mo ($8,280.00/yr)** for a 10-seat team —
HubSpot 'Free' ($0.00/mo) + Zendesk 'Suite Team' ($690.00/mo),
no middleware required.
Middleware via Make/Zapier would add ~$10.59/mo on top of the cheapest API-capable tiers ($700.59/mo all-in) — the native path is cheaper.

 

## Native vs middleware for HubSpot + Zendesk

The native connector is the cheapest route here. Make or Zapier only makes sense if you already run other automations through it, or need a step the native app doesn't offer.

Chart: HubSpot + Zendesk: monthly cost for 10 seats by route: Native connector $690.00; Make Core route $700.59; Zapier Professional route $719.99

Monthly cost for 10 seats by route, HubSpot + Zendesk.

 

Integration routes compared for a 10-seat team

| Route | Plans | 10 seats / month | Sync |
| --- | --- | --- | --- |
| Native HubSpot + Zendesk connector | HubSpot 'Free' + Zendesk 'Suite Team' | $690.00 | 1-way (Zendesk → HubSpot) |
| Make Core on the cheapest API plans | HubSpot 'Free' + Zendesk 'Suite Team' + Make | $700.59 | 1-way per scenario |
| Zapier Professional on the cheapest API plans | HubSpot 'Free' + Zendesk 'Suite Team' + Zapier | $719.99 | 1-way per Zap |

Connector prices are monthly-billing list prices: Zapier Professional $29.99 (zapier.com/pricing) and Make Core $10.59 (from third-party pricing reviews, because make.com blocks automated checks). Both bill by usage, so high volumes cost more.

Image: [HubSpot + Zendesk integration cost summary: $690 a month for 10 seats, nothing extra to connect; plans needed: HubSpot Free and Zendesk Suite Team](https://stackcostmatrix.com/og/hubspot-and-zendesk.jpg)

## ✓ Verified Vendor Facts

- **Plan prices:** from each vendor's pricing page; any exception is flagged next to the date at the top.
- **Required tiers:** 'Free' / 'Suite Team' — the minimum plans this integration needs.
- **API & webhook gates:** audited in official developer docs (see spec matrix).
- **Native app availability:** Native app available in vendor marketplace.

Last checked: Nov 3, 2026 · Sources linked below.

## ! Plan requirements

Requires HubSpot on the 'Free' plan or higher — Requires Zendesk on the 'Suite Team' plan or higher.

HubSpot minimum tier
:   'Free'

Zendesk minimum tier
:   'Suite Team'

Middleware fee
:   None

No hidden cost: the native connector works on HubSpot 'Free' and Zendesk 'Suite Team', so connecting them adds nothing to what you already pay for the two tools.

## Side-by-side spec matrix

Side-by-side spec matrix

| Spec | HubSpot | Zendesk |
| --- | --- | --- |
| Connection type | Native   Source: [HubSpot docs ↗](https://developers.hubspot.com/docs/api/overview) · [Zendesk docs ↗](https://developer.zendesk.com/) · Verified Nov 3, 2026 | |
| Data sync direction | 1-way (Zendesk → HubSpot) | |
| Setup time | 1–3 hours (difficulty 2/5) | |
| Native integration supported | Yes — official native app/connector | |
| API available (distinct from native app) | Yes  — API ≠ native UI; API enables custom/middleware builds Source: [HubSpot API docs ↗](https://developers.hubspot.com/docs/api/overview) · Verified Oct 17, 2026 | Yes  — API ≠ native UI; API enables custom/middleware builds Source: [Zendesk API docs ↗](https://developer.zendesk.com/) · Verified Oct 17, 2026 |
| API access at required tier | Yes  ('Free') 100 req/10 s · 250,000/day (private apps) Source: [HubSpot developers: Usage guidelines ↗](https://developers.hubspot.com/docs/developer-tooling/platform/usage-guidelines) · Verified Nov 3, 2026 | Yes  ('Suite Team') 200 requests/min Source: [Zendesk developers: Rate limits ↗](https://developer.zendesk.com/api-reference/introduction/rate-limits/) · Verified Nov 3, 2026 |
| Webhook support at required tier | No  ('Free') Workflow webhooks need Data Hub Professional Source: [HubSpot KB: Webhooks in workflows ↗](https://knowledge.hubspot.com/workflows/how-do-i-use-webhooks-with-hubspot-workflows) · Verified Nov 3, 2026 | Yes  ('Suite Team') Source: [Zendesk: Creating webhooks ↗](https://support.zendesk.com/hc/en-us/articles/4408839108378) · Verified Nov 3, 2026 |

[Visit HubSpot](https://stackcostmatrix.com/go/hubspot)  [Visit Zendesk](https://stackcostmatrix.com/go/zendesk)

Some outbound links may earn us a referral commission at no extra cost to you. [Read our affiliate disclosure](https://stackcostmatrix.com/about/).

## HubSpot + Zendesk integration: frequently asked questions

### What are the minimum plan tiers required for the HubSpot + Zendesk integration?

To unlock the native integration, HubSpot must be on the 'Free' plan or higher and Zendesk must be on the 'Suite Team' plan or higher. Those are each tool's cheapest plan with API access (HubSpot 'Free' at $0/mo and Zendesk 'Suite Team' at $690/mo for 10 seats), so the integration doesn't force an upgrade.

### How much does the HubSpot + Zendesk stack cost per month for a 10-person team?

At 10 seats with the required tiers (HubSpot 'Free' + Zendesk 'Suite Team'), the stack costs $690.00 per month.

### Is the HubSpot + Zendesk integration native, and would Make or Zapier be cheaper?

The HubSpot + Zendesk connection is native — no third-party middleware subscription is required. Make would cost about $700.59/month on the cheapest API plans, more than the native route, so it only makes sense if you already use it.

### What are the limitations of the HubSpot + Zendesk integration?

Tickets can only be shown on the contact timeline, not on companies or deals, and data only flows from Zendesk into HubSpot. You need a Zendesk Suite plan from Team up.

## Integrations related to HubSpot + Zendesk

[All HubSpot integrations →](https://stackcostmatrix.com/hubspot-integrations-cost/) · [All Zendesk integrations →](https://stackcostmatrix.com/zendesk-integrations-cost/) · [HubSpot API access by plan →](https://stackcostmatrix.com/hubspot-api-access/) · [Zendesk API access by plan →](https://stackcostmatrix.com/zendesk-api-access/)

Part of our [HubSpot integration cost guide](https://stackcostmatrix.com/hubspot-integrations-cost/) and [CRM integration hidden-costs guide](https://stackcostmatrix.com/crm-integration-pricing-guide/).

[### HubSpot + Calendly

Native](https://stackcostmatrix.com/stack/hubspot-and-calendly/)[### HubSpot + Mailchimp

Native](https://stackcostmatrix.com/stack/hubspot-and-mailchimp/)[### Monday.com + Zendesk

Native](https://stackcostmatrix.com/stack/monday-and-zendesk/)[### Salesforce Sales Cloud + Zendesk

Native](https://stackcostmatrix.com/stack/salesforce-and-zendesk/)[### Zendesk + Notion

Middleware](https://stackcostmatrix.com/stack/zendesk-and-notion/)[### Zendesk + Stripe

Middleware](https://stackcostmatrix.com/stack/zendesk-and-stripe/)

Last checked: Nov 3, 2026

## Verified sources

Every figure on this page links to its source below; prices that don't come straight from the vendor's page are flagged next to the date:

- [HubSpot official pricing ↗](https://www.hubspot.com/pricing)
- [HubSpot API / developer docs ↗](https://developers.hubspot.com/docs/api/overview)
- [Zendesk official pricing ↗](https://www.zendesk.com/pricing/)
- [Zendesk API / developer docs ↗](https://developer.zendesk.com/)
