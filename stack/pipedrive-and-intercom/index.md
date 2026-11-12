# Pipedrive + Intercom Integration (2026): How It Works, Setup & True Cost

> How the Pipedrive + Intercom integration works, how to set it up, and the plans it needs: Pipedrive Lite + Intercom Essential, $530/mo for 10 seats.

Source page: https://stackcostmatrix.com/stack/pipedrive-and-intercom/  
Publisher: StackCostMatrix · Editor: Rakesh Kumar · Data licence: CC BY 4.0 (credit StackCostMatrix and link to https://stackcostmatrix.com)

---

[Home](https://stackcostmatrix.com/) / Pipedrive + Intercom 

Intercom's own Pipedrive app creates Pipedrive deals from a lead's profile, syncs later conversations to the matching Pipedrive person and shows deal details in the inbox. Requires Pipedrive on the 'Lite' plan and Intercom on the 'Essential' plan.

Edited by [Rakesh Kumar](https://stackcostmatrix.com/about/#editor), founder of StackCostMatrix | Integration requirements checked against official vendor docs · Nov 12, 2026 · Prices checked · Nov 3, 2026 (Pipedrive prices: from an indexed copy of its pricing page) · Setup steps: Nov 12, 2026 | [Spot an outdated price? Report a correction →](mailto:admin@stackcostmatrix.com?subject=Price%20Correction)

## How the Pipedrive + Intercom integration works

**Does Pipedrive integrate with Intercom?** Yes. Intercom makes a Pipedrive app: install it from Intercom's App Store and connect Pipedrive, and you can create deals while you chat and sync conversations into Pipedrive.

Clicking Create Deal in a lead's or user's profile creates a deal in the first stage of your default pipeline, with the lead's name and email. From then on, conversations sync to the matching Pipedrive person, and to the deal when it was created from the inbox, as done activities whose transcript updates when someone replies and when the conversation closes.

[Setup guide: Intercom: Pipedrive app ↗](https://www.intercom.com/help/en/articles/2535853-pipedrive-app)

Diagram of how Pipedrive and Intercom connect. Pipedrive: Lite plan · $140/mo for 10 seats. Intercom: Essential plan · $390/mo for 10 seats. Intercom to Pipedrive: deals and conversations. Pipedrive to Intercom: deal details in the inbox. Native app, 2-way, no connector fee.

Diagram: how Pipedrive and Intercom connect, a native app. Drawn from the facts on this page.

 

### How do you set up Pipedrive + Intercom?

1. In Intercom, go to the App Store, click the Pipedrive app and click Install now.
2. Connect your Pipedrive account to Intercom when asked.
3. Add the External profiles app to the Inbox, then click Create Deal in a lead's or user's profile.

Steps follow [Intercom's setup guide ↗](https://www.intercom.com/help/en/articles/2535853-pipedrive-app), read Nov 12, 2026.

**Limitations:** Deals always land in the first stage of your default pipeline, and only the lead's name and email are sent. Conversations sync only if the person exists in Pipedrive with a matching email, and only conversations after you connect; later conversations with people on a deal aren't added to that deal. Intercom's article names no plan requirement, so this page models each tool's cheapest plan.

Sources (checked Nov 12, 2026): [Intercom: Pipedrive app ↗](https://www.intercom.com/help/en/articles/2535853-pipedrive-app)

*Interactive cost calculator: open the web page to change team size, billing and add-ons.*

## Default 10-seat TCO summary

**Native integration costs $530.00/mo ($6,360.00/yr)** for a 10-seat team —
Pipedrive 'Lite' ($140.00/mo) + Intercom 'Essential' ($390.00/mo),
no middleware required.
Middleware via Make/Zapier would add ~$10.59/mo on top of the cheapest API-capable tiers ($540.59/mo all-in) — the native path is cheaper.

 

## Native vs middleware for Pipedrive + Intercom

The native connector is the cheapest route here and the only one with 2-way sync. Make or Zapier only makes sense if you already run other automations through it, or need a step the native app doesn't offer.

Chart: Pipedrive + Intercom: monthly cost for 10 seats by route: Native connector $530.00; Make Core route $540.59; Zapier Professional route $559.99

Monthly cost for 10 seats by route, Pipedrive + Intercom.

 

Integration routes compared for a 10-seat team

| Route | Plans | 10 seats / month | Sync |
| --- | --- | --- | --- |
| Native Pipedrive + Intercom connector | Pipedrive 'Lite' + Intercom 'Essential' | $530.00 | 2-way |
| Make Core on the cheapest API plans | Pipedrive 'Lite' + Intercom 'Essential' + Make | $540.59 | 1-way per scenario |
| Zapier Professional on the cheapest API plans | Pipedrive 'Lite' + Intercom 'Essential' + Zapier | $559.99 | 1-way per Zap |

Connector prices are monthly-billing list prices: Zapier Professional $29.99 (zapier.com/pricing) and Make Core $10.59 (from third-party pricing reviews, because make.com blocks automated checks). Both bill by usage, so high volumes cost more.

Image: [Pipedrive + Intercom integration cost summary: $530 a month for 10 seats, nothing extra to connect; plans needed: Pipedrive Lite and Intercom Essential](https://stackcostmatrix.com/og/pipedrive-and-intercom.jpg)

## ✓ Verified Vendor Facts

- **Plan prices:** from each vendor's pricing page; any exception is flagged next to the date at the top.
- **Required tiers:** 'Lite' / 'Essential' — the minimum plans this integration needs.
- **API & webhook gates:** audited in official developer docs (see spec matrix).
- **Native app availability:** Native app available in vendor marketplace.

Requirements checked: Nov 12, 2026; prices: Nov 3, 2026 (exceptions listed at the top) · Sources linked below.

## ! Plan requirements

Requires Pipedrive on the 'Lite' plan or higher — Requires Intercom on the 'Essential' plan or higher.

Pipedrive minimum tier
:   'Lite'

Intercom minimum tier
:   'Essential'

Middleware fee
:   None

No hidden cost: the native connector works on Pipedrive 'Lite' and Intercom 'Essential', so connecting them adds nothing to what you already pay for the two tools.

## Side-by-side spec matrix

Side-by-side spec matrix

| Spec | Pipedrive | Intercom |
| --- | --- | --- |
| Connection type | Native   Source: [Pipedrive docs ↗](https://developers.pipedrive.com/docs/api/v1) · [Intercom docs ↗](https://developers.intercom.com/) · Verified Nov 12, 2026 | |
| Data sync direction | 2-way | |
| Setup time | Under 1 hour (difficulty 1/5) | |
| Native integration supported | Yes — official native app/connector | |
| API available (distinct from native app) | Yes  — API ≠ native UI; API enables custom/middleware builds Source: [Pipedrive API docs ↗](https://developers.pipedrive.com/docs/api/v1) · Verified Oct 17, 2026 | Yes  — API ≠ native UI; API enables custom/middleware builds Source: [Intercom API docs ↗](https://developers.intercom.com/) · Verified Oct 17, 2026 |
| API access at required tier | Yes  ('Lite') 20 req/2 s · daily budget ×1 Source: [Pipedrive developers: Rate limiting ↗](https://pipedrive.readme.io/docs/core-api-concepts-rate-limiting) · Verified Nov 3, 2026 | Yes  ('Essential') Paid workspaces Source: [Intercom developers: Webhooks ↗](https://developers.intercom.com/docs/webhooks) · Verified Nov 3, 2026 |
| Webhook support at required tier | Yes  ('Lite') Source: [Pipedrive: Automations webhook requests ↗](https://support.pipedrive.com/en/article/automations-webhook-requests) · Verified Nov 3, 2026 | Yes  ('Essential') Source: [Intercom developers: Webhooks ↗](https://developers.intercom.com/docs/webhooks) · Verified Nov 3, 2026 |

[Visit Pipedrive](https://stackcostmatrix.com/go/pipedrive)  [Visit Intercom](https://stackcostmatrix.com/go/intercom)

Some outbound links may earn us a referral commission at no extra cost to you. [Read our affiliate disclosure](https://stackcostmatrix.com/about/).

## Pipedrive + Intercom integration: frequently asked questions

### What are the minimum plan tiers required for the Pipedrive + Intercom integration?

To unlock the native integration, Pipedrive must be on the 'Lite' plan or higher and Intercom must be on the 'Essential' plan or higher. Those are each tool's cheapest plan with API access (Pipedrive 'Lite' at $140/mo and Intercom 'Essential' at $390/mo for 10 seats), so the integration doesn't force an upgrade.

### How much does the Pipedrive + Intercom stack cost per month for a 10-person team?

At 10 seats with the required tiers (Pipedrive 'Lite' + Intercom 'Essential'), the stack costs $530.00 per month.

### Is the Pipedrive + Intercom integration native, and would Make or Zapier be cheaper?

The Pipedrive + Intercom connection is native — no third-party middleware subscription is required. Make would cost about $540.59/month on the cheapest API plans, more than the native route, so it only makes sense if you already use it.

### What are the limitations of the Pipedrive + Intercom integration?

Deals always land in the first stage of your default pipeline, and only the lead's name and email are sent. Conversations sync only if the person exists in Pipedrive with a matching email, and only conversations after you connect; later conversations with people on a deal aren't added to that deal. Intercom's article names no plan requirement, so this page models each tool's cheapest plan.

## Integrations related to Pipedrive + Intercom

[All Pipedrive integrations →](https://stackcostmatrix.com/pipedrive-integrations-cost/) · [All Intercom integrations →](https://stackcostmatrix.com/intercom-integrations-cost/) · [Pipedrive API access by plan →](https://stackcostmatrix.com/pipedrive-api-access/) · [Intercom API access by plan →](https://stackcostmatrix.com/intercom-api-access/)

Part of our [CRM integration hidden-costs guide](https://stackcostmatrix.com/crm-integration-pricing-guide/).

[### ActiveCampaign + Pipedrive

Native](https://stackcostmatrix.com/stack/activecampaign-and-pipedrive/)[### HubSpot + Pipedrive

Middleware](https://stackcostmatrix.com/stack/hubspot-and-pipedrive/)[### Pipedrive + Asana

Native](https://stackcostmatrix.com/stack/pipedrive-and-asana/)[### Pipedrive + Calendly

Middleware](https://stackcostmatrix.com/stack/pipedrive-and-calendly/)[### Pipedrive + Mailchimp

Native](https://stackcostmatrix.com/stack/pipedrive-and-mailchimp/)[### Pipedrive + QuickBooks

Native](https://stackcostmatrix.com/stack/pipedrive-and-quickbooks/)

Requirements checked: Nov 12, 2026; prices: Nov 3, 2026 (exceptions listed at the top)

## Verified sources

Every figure on this page links to its source below; prices that don't come straight from the vendor's page are flagged next to the date:

- [Pipedrive official pricing ↗](https://www.pipedrive.com/pricing)
- [Pipedrive API / developer docs ↗](https://developers.pipedrive.com/docs/api/v1)
- [Intercom official pricing ↗](https://www.intercom.com/pricing)
- [Intercom API / developer docs ↗](https://developers.intercom.com/)
