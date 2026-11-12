# Intercom + Calendly Integration (2026): How It Works, Setup & True Cost

> How the Intercom + Calendly integration works, how to set it up, and the plans it needs: Intercom Essential + Calendly Free, $390/mo for 10 seats.

Source page: https://stackcostmatrix.com/stack/intercom-and-calendly/  
Publisher: StackCostMatrix · Editor: Rakesh Kumar · Data licence: CC BY 4.0 (credit StackCostMatrix and link to https://stackcostmatrix.com)

---

[Home](https://stackcostmatrix.com/) / Intercom + Calendly 

Calendly's app for Intercom lets agents and bots share a scheduling link in chat, so visitors book without leaving the Messenger; Calendly lists it on all its plans, and Intercom needs a trial or paid subscription. Requires Intercom on the 'Essential' plan and Calendly on the 'Free' plan.

Edited by [Rakesh Kumar](https://stackcostmatrix.com/about/#editor), founder of StackCostMatrix | Integration requirements checked against official vendor docs · Nov 12, 2026 · Prices checked · Nov 3, 2026 · Setup steps: Nov 12, 2026 | [Spot an outdated price? Report a correction →](mailto:admin@stackcostmatrix.com?subject=Price%20Correction)

## How the Intercom + Calendly integration works

**Does Intercom integrate with Calendly?** Yes. Calendly makes an app for Intercom: install it from the Intercom App Store and you can put a scheduling invitation in a chat, add it to a bot's path or pin it to the Messenger home. Calendly lists it on all its plans; Intercom needs a trial or paid subscription.

An agent adds the Calendly app from the chat toolbar and picks a scheduling link; the visitor sees your availability inside the chat window and books there, and the invitation then shows the meeting details. A bot can offer the same link at the end of its path. Booking data doesn't flow into Intercom's CRM; Calendly suggests Zapier for that.

[Setup guide: Calendly: Calendly + Intercom ↗](https://calendly.com/help/calendly-intercom)

Diagram of how Intercom and Calendly connect. Calendly: Free plan · $0/mo for 10 seats. Intercom: Essential plan · $390/mo for 10 seats. Calendly to Intercom: scheduling links and booked meetings in chat. Native app, 1-way, no connector fee.

Diagram: how Intercom and Calendly connect, a native app. Drawn from the facts on this page.

 

### How do you set up Intercom + Calendly?

1. Install the Calendly app from the Intercom App Store. Each user sets it up for themselves; admins can't configure it for others.
2. In a chat, open Add a messenger app in the chat toolbar, select the Calendly app and enter your scheduling link.
3. Customize the message and button text, then click Create Invite to add the invitation to the chat.
4. To automate it, add Calendly as a follow-up action (Send an app) at the end of a custom bot's path, then publish the bot.

Steps follow [Calendly's setup guide ↗](https://calendly.com/help/calendly-intercom), read Nov 12, 2026.

**Limitations:** It shares scheduling links and shows booked meetings in the conversation; it doesn't copy booking data into Intercom's CRM, which Calendly suggests doing through Zapier. Each user connects it individually, and it needs a trial or paid Intercom subscription.

Sources (checked Nov 12, 2026): [Calendly: Calendly + Intercom ↗](https://calendly.com/help/calendly-intercom)

*Interactive cost calculator: open the web page to change team size, billing and add-ons.*

## Default 10-seat TCO summary

**Native integration costs $390.00/mo ($4,680.00/yr)** for a 10-seat team —
Intercom 'Essential' ($390.00/mo) + Calendly 'Free' ($0.00/mo),
no middleware required.
Middleware via Make/Zapier would add ~$10.59/mo on top of the cheapest API-capable tiers ($400.59/mo all-in) — the native path is cheaper.

 

## Native vs middleware for Intercom + Calendly

The native connector is the cheapest route here. Make or Zapier only makes sense if you already run other automations through it, or need a step the native app doesn't offer.

Chart: Intercom + Calendly: monthly cost for 10 seats by route: Native connector $390.00; Make Core route $400.59; Zapier Professional route $419.99

Monthly cost for 10 seats by route, Intercom + Calendly.

 

Integration routes compared for a 10-seat team

| Route | Plans | 10 seats / month | Sync |
| --- | --- | --- | --- |
| Native Intercom + Calendly connector | Intercom 'Essential' + Calendly 'Free' | $390.00 | 1-way (Calendly → Intercom) |
| Make Core on the cheapest API plans | Intercom 'Essential' + Calendly 'Free' + Make | $400.59 | 1-way per scenario |
| Zapier Professional on the cheapest API plans | Intercom 'Essential' + Calendly 'Free' + Zapier | $419.99 | 1-way per Zap |

Connector prices are monthly-billing list prices: Zapier Professional $29.99 (zapier.com/pricing) and Make Core $10.59 (from third-party pricing reviews, because make.com blocks automated checks). Both bill by usage, so high volumes cost more.

Image: [Intercom + Calendly integration cost summary: $390 a month for 10 seats, nothing extra to connect; plans needed: Intercom Essential and Calendly Free](https://stackcostmatrix.com/og/intercom-and-calendly.jpg)

## ✓ Verified Vendor Facts

- **Plan prices:** from each vendor's pricing page; any exception is flagged next to the date at the top.
- **Required tiers:** 'Essential' / 'Free' — the minimum plans this integration needs.
- **API & webhook gates:** audited in official developer docs (see spec matrix).
- **Native app availability:** Native app available in vendor marketplace.

Requirements checked: Nov 12, 2026; prices: Nov 3, 2026 · Sources linked below.

## ! Plan requirements

Requires Intercom on the 'Essential' plan or higher — Requires Calendly on the 'Free' plan or higher.

Intercom minimum tier
:   'Essential'

Calendly minimum tier
:   'Free'

Middleware fee
:   None

No hidden cost: the native connector works on Intercom 'Essential' and Calendly 'Free', so connecting them adds nothing to what you already pay for the two tools.

## Side-by-side spec matrix

Side-by-side spec matrix

| Spec | Intercom | Calendly |
| --- | --- | --- |
| Connection type | Native   Source: [Intercom docs ↗](https://developers.intercom.com/) · [Calendly docs ↗](https://developer.calendly.com/) · Verified Nov 12, 2026 | |
| Data sync direction | 1-way (Calendly → Intercom) | |
| Setup time | Under 1 hour (difficulty 1/5) | |
| Native integration supported | Yes — official native app/connector | |
| API available (distinct from native app) | Yes  — API ≠ native UI; API enables custom/middleware builds Source: [Intercom API docs ↗](https://developers.intercom.com/) · Verified Oct 17, 2026 | Yes  — API ≠ native UI; API enables custom/middleware builds Source: [Calendly API docs ↗](https://developer.calendly.com/) · Verified Oct 17, 2026 |
| API access at required tier | Yes  ('Essential') Paid workspaces Source: [Intercom developers: Webhooks ↗](https://developers.intercom.com/docs/webhooks) · Verified Nov 3, 2026 | Yes  ('Free') Source: [Calendly: API overview ↗](https://calendly.com/help/calendly-api-overview) · Verified Nov 3, 2026 |
| Webhook support at required tier | Yes  ('Essential') Source: [Intercom developers: Webhooks ↗](https://developers.intercom.com/docs/webhooks) · Verified Nov 3, 2026 | No  ('Free') Webhooks need a paid plan Source: [Calendly: API overview ↗](https://calendly.com/help/calendly-api-overview) · Verified Nov 3, 2026 |

[Visit Intercom](https://stackcostmatrix.com/go/intercom)  [Visit Calendly](https://stackcostmatrix.com/go/calendly)

Some outbound links may earn us a referral commission at no extra cost to you. [Read our affiliate disclosure](https://stackcostmatrix.com/about/).

## Intercom + Calendly integration: frequently asked questions

### What are the minimum plan tiers required for the Intercom + Calendly integration?

To unlock the native integration, Intercom must be on the 'Essential' plan or higher and Calendly must be on the 'Free' plan or higher. Those are each tool's cheapest plan with API access (Intercom 'Essential' at $390/mo and Calendly 'Free' at $0/mo for 10 seats), so the integration doesn't force an upgrade.

### How much does the Intercom + Calendly stack cost per month for a 10-person team?

At 10 seats with the required tiers (Intercom 'Essential' + Calendly 'Free'), the stack costs $390.00 per month.

### Is the Intercom + Calendly integration native, and would Make or Zapier be cheaper?

The Intercom + Calendly connection is native — no third-party middleware subscription is required. Make would cost about $400.59/month on the cheapest API plans, more than the native route, so it only makes sense if you already use it.

### What are the limitations of the Intercom + Calendly integration?

It shares scheduling links and shows booked meetings in the conversation; it doesn't copy booking data into Intercom's CRM, which Calendly suggests doing through Zapier. Each user connects it individually, and it needs a trial or paid Intercom subscription.

## Integrations related to Intercom + Calendly

[All Intercom integrations →](https://stackcostmatrix.com/intercom-integrations-cost/) · [All Calendly integrations →](https://stackcostmatrix.com/calendly-integrations-cost/) · [Intercom API access by plan →](https://stackcostmatrix.com/intercom-api-access/) · [Calendly API access by plan →](https://stackcostmatrix.com/calendly-api-access/)

[### Intercom + HubSpot

Native](https://stackcostmatrix.com/stack/intercom-and-hubspot/)[### Intercom + Mailchimp

Native](https://stackcostmatrix.com/stack/intercom-and-mailchimp/)[### Intercom + Salesforce

Native](https://stackcostmatrix.com/stack/intercom-and-salesforce/)[### Intercom + Stripe

Native](https://stackcostmatrix.com/stack/intercom-and-stripe/)[### Pipedrive + Intercom

Native](https://stackcostmatrix.com/stack/pipedrive-and-intercom/)[### Slack + Intercom

Native](https://stackcostmatrix.com/stack/slack-and-intercom/)

Requirements checked: Nov 12, 2026; prices: Nov 3, 2026

## Verified sources

Every figure on this page links to its source below; prices that don't come straight from the vendor's page are flagged next to the date:

- [Intercom official pricing ↗](https://www.intercom.com/pricing)
- [Intercom API / developer docs ↗](https://developers.intercom.com/)
- [Calendly official pricing ↗](https://calendly.com/pricing)
- [Calendly API / developer docs ↗](https://developer.calendly.com/)
