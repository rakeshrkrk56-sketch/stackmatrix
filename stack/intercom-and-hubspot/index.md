# Intercom + HubSpot Integration: How It Works & Cost (2026)

> How the Intercom + HubSpot integration works, how to set it up, and the plans it needs: Intercom Essential + HubSpot Free, $390/mo for 10 seats.

Source page: https://stackcostmatrix.com/stack/intercom-and-hubspot/  
Publisher: StackCostMatrix · Editor: Rakesh Kumar · Data licence: CC BY 4.0 (credit StackCostMatrix and link to https://stackcostmatrix.com)

---

[Home](https://stackcostmatrix.com/) / Intercom + HubSpot 

# Intercom + HubSpot Integration (2026): How It Works, Setup & True Cost

Intercom's HubSpot app works on Intercom Essential and any HubSpot plan, but it only syncs one way, from Intercom into HubSpot. Requires Intercom on the 'Essential' plan and HubSpot on the 'Free' plan.

Edited by [Rakesh Kumar](https://stackcostmatrix.com/about/#editor), founder of StackCostMatrix | Integration requirements and prices checked against official vendor docs · Nov 3, 2026 | [Spot an outdated price? Report a correction →](mailto:admin@stackcostmatrix.com?subject=Price%20Correction)

## How the Intercom + HubSpot integration works

**Does Intercom integrate with HubSpot?** Yes. Intercom's HubSpot app, available on Intercom's Essential, Advanced and Expert plans, sends leads from Intercom to HubSpot as contacts and logs their conversations on the HubSpot timeline.

Intercom's HubSpot app sends leads captured in Intercom to HubSpot as contacts and logs Intercom conversations on their HubSpot activity timeline, so sales can pick up where a chat left off.

### How to set it up

**1.** Make sure you have admin access in HubSpot.

**2.** In Intercom, open the App Store, find HubSpot and click Install now.

**3.** Connect your HubSpot account when prompted.

**4.** In App Store > HubSpot > Settings, choose how leads and their conversations are sent to HubSpot.

**Limitations:** It only sends data one way, from Intercom to HubSpot. Customer replies sync in real time but teammate replies sync only once the conversation is closed, and company attributes other than the company name aren't sent. For HubSpot data in Intercom you need HubSpot's separate Data Sync app.

Sources (checked Nov 3, 2026): [Intercom: HubSpot app ↗](https://www.intercom.com/help/en/articles/2128216-hubspot-app) · [HubSpot Marketplace: Intercom ↗](https://ecosystem.hubspot.com/marketplace/listing/intercom)

*Interactive cost calculator: open the web page to change team size, billing and add-ons.*

## Default 10-seat TCO summary

**Native integration costs $390.00/mo ($4,680.00/yr)** for a 10-seat team —
Intercom 'Essential' ($390.00/mo) + HubSpot 'Free' ($0.00/mo),
no middleware required.
Middleware via Make/Zapier would add ~$10.59/mo on top of the cheapest API-capable tiers ($400.59/mo all-in) — the native path is cheaper.

## Native vs middleware for Intercom + HubSpot

The native path runs on the required tiers (Intercom 'Essential' + HubSpot 'Free') at $390.00/mo for a 10-seat team, with no middleware fee. The middleware path — the cheapest API-capable tiers plus about $10.59/mo for Make Core — would cost $400.59/mo all-in, so on cost alone there is no reason to switch: middleware would only make sense if you already run other automations through it.

API access at the required tiers: Intercom Yes, HubSpot Yes (see the spec matrix). That API access is what the middleware path runs on.

Integration routes compared for a 10-seat team

| Route | Plans | 10 seats / month | Sync |
| --- | --- | --- | --- |
| Native Intercom + HubSpot connector | Intercom 'Essential' + HubSpot 'Free' | $390.00 | As listed in the spec matrix |
| Make Core on the cheapest API plans | Intercom 'Essential' + HubSpot 'Free' + Make | $400.59 | 1-way per scenario |

Make Core's $10.59 monthly price comes from third-party pricing reviews, because make.com blocks automated checks; Zapier's is from zapier.com/pricing.

## ✓ Verified Vendor Facts

- **Plan prices:** from each vendor's pricing page; any exception is flagged next to the date at the top.
- **Required tiers:** 'Essential' / 'Free' — the minimum plans this integration needs.
- **API & webhook gates:** audited in official developer docs (see spec matrix).
- **Native app availability:** Native app available in vendor marketplace.

Last checked: Nov 3, 2026 · Sources linked below.

## ◐ Model Estimates (your assumptions)

- **Usage / task add-ons:** middleware overage costs you enter above.
- **Setup & maintenance:** implementation hours and ongoing ops — adjust freely.
- **Annual billing saving:** uses each vendor's published annual price where one exists; otherwise no discount is applied.

Estimates never change the verified facts — they only model your scenario.

## ! Plan requirements

Requires Intercom on the 'Essential' plan or higher — Requires HubSpot on the 'Free' plan or higher.

Intercom minimum tier
:   'Essential'

HubSpot minimum tier
:   'Free'

Middleware fee
:   None

No hidden cost: the native connector works on Intercom 'Essential' and HubSpot 'Free', so connecting them adds nothing to what you already pay for the two tools.

✓ Native is the cheapest path — $0 incremental integration cost

The native Intercom + HubSpot connector runs on the required tiers with no middleware fee
and no forced tier upgrade — paying for middleware here would only add cost.

## Side-by-side spec matrix

Side-by-side spec matrix

| Spec | Intercom | HubSpot |
| --- | --- | --- |
| Connection type | Native   Source: [Intercom docs ↗](https://developers.intercom.com/) · [HubSpot docs ↗](https://developers.hubspot.com/docs/api/overview) · Verified Nov 3, 2026 | |
| Data sync direction | 1-way (Intercom → HubSpot) | |
| Setup time | Half a day (difficulty 3/5) | |
| Native integration supported | Yes — official native app/connector | |
| API available (distinct from native app) | Yes  — API ≠ native UI; API enables custom/middleware builds Source: [Intercom API docs ↗](https://developers.intercom.com/) · Verified Oct 17, 2026 | Yes  — API ≠ native UI; API enables custom/middleware builds Source: [HubSpot API docs ↗](https://developers.hubspot.com/docs/api/overview) · Verified Oct 17, 2026 |
| API access at required tier | Yes  ('Essential') Paid workspaces Source: [Intercom developers: Webhooks ↗](https://developers.intercom.com/docs/webhooks) · Verified Nov 3, 2026 | Yes  ('Free') 100 req/10 s · 250,000/day (private apps) Source: [HubSpot developers: Usage guidelines ↗](https://developers.hubspot.com/docs/developer-tooling/platform/usage-guidelines) · Verified Nov 3, 2026 |
| Webhook support at required tier | Yes  ('Essential') Source: [Intercom developers: Webhooks ↗](https://developers.intercom.com/docs/webhooks) · Verified Nov 3, 2026 | No  ('Free') Workflow webhooks need Data Hub Professional Source: [HubSpot KB: Webhooks in workflows ↗](https://knowledge.hubspot.com/workflows/how-do-i-use-webhooks-with-hubspot-workflows) · Verified Nov 3, 2026 |

[Visit Intercom](https://stackcostmatrix.com/go/intercom)  [Visit HubSpot](https://stackcostmatrix.com/go/hubspot)

Some outbound links may earn us a referral commission at no extra cost to you. [Read our affiliate disclosure](https://stackcostmatrix.com/about/).

## Frequently asked questions

### What are the minimum plan tiers required for the Intercom + HubSpot integration?

To unlock the native integration, Intercom must be on the 'Essential' plan or higher and HubSpot must be on the 'Free' plan or higher. Neither plan is an upgrade over the cheapest plan with API access.

### How much does the Intercom + HubSpot stack cost per month for a 10-person team?

At 10 seats with the required tiers (Intercom 'Essential' + HubSpot 'Free'), the stack costs $390.00 per month.

### Is the Intercom + HubSpot integration native, and would Make or Zapier be cheaper?

The Intercom + HubSpot connection is native — no third-party middleware subscription is required. Make would cost about $400.59/month on the cheapest API plans, more than the native route, so it only makes sense if you already use it.

### What are the limitations of the Intercom + HubSpot integration?

It only sends data one way, from Intercom to HubSpot. Customer replies sync in real time but teammate replies sync only once the conversation is closed, and company attributes other than the company name aren't sent. For HubSpot data in Intercom you need HubSpot's separate Data Sync app.

## Related integrations

[All Intercom integrations →](https://stackcostmatrix.com/intercom-integrations-cost/) · [All HubSpot integrations →](https://stackcostmatrix.com/hubspot-integrations-cost/) · [Intercom API access by plan →](https://stackcostmatrix.com/intercom-api-access/) · [HubSpot API access by plan →](https://stackcostmatrix.com/hubspot-api-access/)

Part of our [HubSpot integration cost guide](https://stackcostmatrix.com/hubspot-integrations-cost/) and [CRM integration hidden-costs guide](https://stackcostmatrix.com/crm-integration-pricing-guide/).

[### HubSpot + Slack

Native](https://stackcostmatrix.com/stack/hubspot-and-slack/)[### HubSpot + Stripe

Native](https://stackcostmatrix.com/stack/hubspot-and-stripe/)[### Slack + Intercom

Native](https://stackcostmatrix.com/stack/slack-and-intercom/)[### Freshdesk + HubSpot

Native](https://stackcostmatrix.com/stack/freshdesk-and-hubspot/)[### HubSpot + Asana

Native](https://stackcostmatrix.com/stack/hubspot-and-asana/)[### Intercom + Stripe

Native](https://stackcostmatrix.com/stack/intercom-and-stripe/)

Last checked: Nov 3, 2026

## Verified sources

Every figure on this page links to its source below; prices that don't come straight from the vendor's page are flagged next to the date:

- [Intercom official pricing ↗](https://www.intercom.com/pricing)
- [Intercom API / developer docs ↗](https://developers.intercom.com/)
- [HubSpot official pricing ↗](https://www.hubspot.com/pricing)
- [HubSpot API / developer docs ↗](https://developers.hubspot.com/docs/api/overview)
