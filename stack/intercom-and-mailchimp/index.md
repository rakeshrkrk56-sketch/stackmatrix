# Intercom + Mailchimp Integration (2026): How It Works, Setup & True Cost

> How the Intercom + Mailchimp integration works, how to set it up, and the plans it needs: Intercom Essential + Mailchimp Free, $390/mo for 10 seats.

Source page: https://stackcostmatrix.com/stack/intercom-and-mailchimp/  
Publisher: StackCostMatrix · Editor: Rakesh Kumar · Data licence: CC BY 4.0 (credit StackCostMatrix and link to https://stackcostmatrix.com)

---

[Home](https://stackcostmatrix.com/) / Intercom + Mailchimp 

Intercom's Mailchimp apps add Messenger and chat sign-ups to a Mailchimp audience, show each person's subscription status in the inbox and keep unsubscribes in step both ways; the Subscribe app needs any paid Intercom plan. Requires Intercom on the 'Essential' plan and Mailchimp on the 'Free' plan.

Edited by [Rakesh Kumar](https://stackcostmatrix.com/about/#editor), founder of StackCostMatrix | Integration requirements checked against official vendor docs · Nov 12, 2026 · Prices checked · Nov 3, 2026 · Setup steps: Nov 12, 2026 | [Spot an outdated price? Report a correction →](mailto:admin@stackcostmatrix.com?subject=Price%20Correction)

## How the Intercom + Mailchimp integration works

**Does Intercom integrate with Mailchimp?** Yes. Intercom has two Mailchimp apps: Mailchimp Subscribe, which captures email subscribers in the Messenger and in conversations, and Mailchimp Sync, which keeps unsubscribes matched in both tools. The Subscribe app needs a Mailchimp account and any paid Intercom plan.

Mailchimp Subscribe adds a sign-up card to the Messenger home, or agents send it in a conversation, and new subscribers join the Mailchimp list you choose. For people already on the list, the app shows their status, audience, star rating, open and click rates, sign-up date and tags, and agents can unsubscribe them. Mailchimp Sync uses a Mailchimp webhook, so unsubscribing in either tool carries over to the other.

[Setup guide: Intercom: Mailchimp Subscribe app ↗](https://www.intercom.com/help/en/articles/1829462-mailchimp-subscribe-app-capture-new-subscribers)

Diagram of how Intercom and Mailchimp connect. Intercom: Essential plan · $390/mo for 10 seats. Mailchimp: Free plan · $0/mo for 10 seats. Intercom to Mailchimp: new subscribers from the Messenger. Both ways: unsubscribes (Mailchimp Sync). Native app, 2-way, no connector fee.

Diagram: how Intercom and Mailchimp connect, a native app. Drawn from the facts on this page.

 

### How do you set up Intercom + Mailchimp?

1. In Intercom's App Store, search for Mailchimp Subscribe, click Install now, click Connect and allow access to your Mailchimp account.
2. Select the Mailchimp list to sync, then write the card's title, description, confirmation message and any reward.
3. Add the app to the Messenger home (Settings > Channels > Messenger > Customize Home with apps), or pin it in the inbox to send it in conversations.
4. For unsubscribes, install Mailchimp Sync, click Sync your subscribers, choose the list and paste Intercom's callback URL into a new webhook in Mailchimp.

Steps follow [Intercom's setup guide ↗](https://www.intercom.com/help/en/articles/1829462-mailchimp-subscribe-app-capture-new-subscribers), read Nov 12, 2026.

**Limitations:** A Mailchimp list with required merge fields can't be used with the Subscribe app until those fields are made optional. The open and click rates it shows cover emails sent through Mailchimp only. Mailchimp Sync doesn't create a Mailchimp record for someone who isn't already there.

Sources (checked Nov 12, 2026): [Intercom: Mailchimp Subscribe app ↗](https://www.intercom.com/help/en/articles/1829462-mailchimp-subscribe-app-capture-new-subscribers) · [Intercom: Sync unsubscribed users with the Mailchimp app ↗](https://www.intercom.com/help/en/articles/255-sync-unsubscribed-users-with-the-mailchimp-app)

*Interactive cost calculator: open the web page to change team size, billing and add-ons.*

## Default 10-seat TCO summary

**Native integration costs $390.00/mo ($4,680.00/yr)** for a 10-seat team —
Intercom 'Essential' ($390.00/mo) + Mailchimp 'Free' ($0.00/mo),
no middleware required.
Middleware via Make/Zapier would add ~$10.59/mo on top of the cheapest API-capable tiers ($400.59/mo all-in) — the native path is cheaper.

 

## Native vs middleware for Intercom + Mailchimp

The native connector is the cheapest route here and the only one with 2-way sync. Make or Zapier only makes sense if you already run other automations through it, or need a step the native app doesn't offer.

Chart: Intercom + Mailchimp: monthly cost for 10 seats by route: Native connector $390.00; Make Core route $400.59; Zapier Professional route $419.99

Monthly cost for 10 seats by route, Intercom + Mailchimp.

 

Integration routes compared for a 10-seat team

| Route | Plans | 10 seats / month | Sync |
| --- | --- | --- | --- |
| Native Intercom + Mailchimp connector | Intercom 'Essential' + Mailchimp 'Free' | $390.00 | 2-way |
| Make Core on the cheapest API plans | Intercom 'Essential' + Mailchimp 'Free' + Make | $400.59 | 1-way per scenario |
| Zapier Professional on the cheapest API plans | Intercom 'Essential' + Mailchimp 'Free' + Zapier | $419.99 | 1-way per Zap |

Connector prices are monthly-billing list prices: Zapier Professional $29.99 (zapier.com/pricing) and Make Core $10.59 (from third-party pricing reviews, because make.com blocks automated checks). Both bill by usage, so high volumes cost more.

Image: [Intercom + Mailchimp integration cost summary: $390 a month for 10 seats, nothing extra to connect; plans needed: Intercom Essential and Mailchimp Free](https://stackcostmatrix.com/og/intercom-and-mailchimp.jpg)

## ✓ Verified Vendor Facts

- **Plan prices:** from each vendor's pricing page; any exception is flagged next to the date at the top.
- **Required tiers:** 'Essential' / 'Free' — the minimum plans this integration needs.
- **API & webhook gates:** audited in official developer docs (see spec matrix).
- **Native app availability:** Native app available in vendor marketplace.

Requirements checked: Nov 12, 2026; prices: Nov 3, 2026 · Sources linked below.

## ! Plan requirements

Requires Intercom on the 'Essential' plan or higher — Requires Mailchimp on the 'Free' plan or higher.

Intercom minimum tier
:   'Essential'

Mailchimp minimum tier
:   'Free'

Middleware fee
:   None

No hidden cost: the native connector works on Intercom 'Essential' and Mailchimp 'Free', so connecting them adds nothing to what you already pay for the two tools.

## Side-by-side spec matrix

Side-by-side spec matrix

| Spec | Intercom | Mailchimp |
| --- | --- | --- |
| Connection type | Native   Source: [Intercom docs ↗](https://developers.intercom.com/) · [Mailchimp docs ↗](https://mailchimp.com/developer/) · Verified Nov 12, 2026 | |
| Data sync direction | 2-way | |
| Setup time | Under 1 hour (difficulty 1/5) | |
| Native integration supported | Yes — official native app/connector | |
| API available (distinct from native app) | Yes  — API ≠ native UI; API enables custom/middleware builds Source: [Intercom API docs ↗](https://developers.intercom.com/) · Verified Oct 17, 2026 | Yes  — API ≠ native UI; API enables custom/middleware builds Source: [Mailchimp API docs ↗](https://mailchimp.com/developer/) · Verified Oct 17, 2026 |
| API access at required tier | Yes  ('Essential') Paid workspaces Source: [Intercom developers: Webhooks ↗](https://developers.intercom.com/docs/webhooks) · Verified Nov 3, 2026 | Yes  ('Free') No plan requirement in Mailchimp's API key article Source: [Mailchimp: About API keys ↗](https://mailchimp.com/help/about-api-keys/) · Verified Nov 3, 2026 |
| Webhook support at required tier | Yes  ('Essential') Source: [Intercom developers: Webhooks ↗](https://developers.intercom.com/docs/webhooks) · Verified Nov 3, 2026 | No  ('Free') Webhook automation step needs Standard Source: [Mailchimp: About webhooks ↗](https://mailchimp.com/help/about-webhooks/) · Verified Nov 3, 2026 |

[Visit Intercom](https://stackcostmatrix.com/go/intercom)  [Visit Mailchimp](https://stackcostmatrix.com/go/mailchimp)

Some outbound links may earn us a referral commission at no extra cost to you. [Read our affiliate disclosure](https://stackcostmatrix.com/about/).

## Intercom + Mailchimp integration: frequently asked questions

### What are the minimum plan tiers required for the Intercom + Mailchimp integration?

To unlock the native integration, Intercom must be on the 'Essential' plan or higher and Mailchimp must be on the 'Free' plan or higher. Those are each tool's cheapest plan with API access (Intercom 'Essential' at $390/mo and Mailchimp 'Free' at $0/mo for 10 seats), so the integration doesn't force an upgrade.

### How much does the Intercom + Mailchimp stack cost per month for a 10-person team?

At 10 seats with the required tiers (Intercom 'Essential' + Mailchimp 'Free'), the stack costs $390.00 per month.

### Is the Intercom + Mailchimp integration native, and would Make or Zapier be cheaper?

The Intercom + Mailchimp connection is native — no third-party middleware subscription is required. Make would cost about $400.59/month on the cheapest API plans, more than the native route, so it only makes sense if you already use it.

### What are the limitations of the Intercom + Mailchimp integration?

A Mailchimp list with required merge fields can't be used with the Subscribe app until those fields are made optional. The open and click rates it shows cover emails sent through Mailchimp only. Mailchimp Sync doesn't create a Mailchimp record for someone who isn't already there.

## Integrations related to Intercom + Mailchimp

[All Intercom integrations →](https://stackcostmatrix.com/intercom-integrations-cost/) · [All Mailchimp integrations →](https://stackcostmatrix.com/mailchimp-integrations-cost/) · [Intercom API access by plan →](https://stackcostmatrix.com/intercom-api-access/) · [Mailchimp API access by plan →](https://stackcostmatrix.com/mailchimp-api-access/)

[### Intercom + Calendly

Native](https://stackcostmatrix.com/stack/intercom-and-calendly/)[### Intercom + HubSpot

Native](https://stackcostmatrix.com/stack/intercom-and-hubspot/)[### Intercom + Salesforce

Native](https://stackcostmatrix.com/stack/intercom-and-salesforce/)[### Intercom + Stripe

Native](https://stackcostmatrix.com/stack/intercom-and-stripe/)[### Pipedrive + Intercom

Native](https://stackcostmatrix.com/stack/pipedrive-and-intercom/)[### Slack + Intercom

Native](https://stackcostmatrix.com/stack/slack-and-intercom/)

Requirements checked: Nov 12, 2026; prices: Nov 3, 2026

## Verified sources

Every figure on this page links to its source below; prices that don't come straight from the vendor's page are flagged next to the date:

- [Intercom official pricing ↗](https://www.intercom.com/pricing)
- [Intercom API / developer docs ↗](https://developers.intercom.com/)
- [Mailchimp official pricing ↗](https://mailchimp.com/pricing/)
- [Mailchimp API / developer docs ↗](https://mailchimp.com/developer/)
