# Intercom + ActiveCampaign Integration (2026): How It Works, Setup & True Cost

> How the Intercom + ActiveCampaign integration works and how to set it up, plus the plans it needs and the 10-seat cost ($415.59/mo).

Source page: https://stackcostmatrix.com/stack/intercom-and-activecampaign/  
Publisher: StackCostMatrix · Editor: Rakesh Kumar · Data licence: CC BY 4.0 (credit StackCostMatrix and link to https://stackcostmatrix.com)

---

[Home](https://stackcostmatrix.com/) / Intercom + ActiveCampaign 

There's no native Intercom–ActiveCampaign link: ActiveCampaign's app directory lists Intercom as a middleware app, available on every ActiveCampaign plan. Requires Intercom on the 'Essential' plan and ActiveCampaign on the 'Starter' plan. Route it through Make Core ($10.59/mo, or $9/mo billed annually).

Edited by [Rakesh Kumar](https://stackcostmatrix.com/about/#editor), founder of StackCostMatrix | Integration requirements checked against official vendor docs · Nov 12, 2026 · Prices checked · Nov 3, 2026 (Make fee: $9 annual price Oct 17, 2026; $10.59 monthly price from third-party pricing reviews, Nov 3, 2026, as make.com blocks automated checks) · Setup steps: Nov 12, 2026 | [Spot an outdated price? Report a correction →](mailto:admin@stackcostmatrix.com?subject=Price%20Correction)

## How the Intercom + ActiveCampaign integration works

**Does Intercom integrate with ActiveCampaign?** Not natively. ActiveCampaign's app directory lists Intercom as a "Middleware App" that it doesn't build, included with every ActiveCampaign plan: it creates or updates a contact in ActiveCampaign when a new email address is added to a lead in Intercom. A connector such as Make or Zapier provides the link.

With Make, a scenario watches Intercom for events, such as a lead getting an email address, and creates or updates the contact in ActiveCampaign. Each scenario runs one way.

[Setup guide: Make: Intercom app ↗](https://apps.make.com/intercom)

Diagram of how Intercom and ActiveCampaign connect. Intercom: Essential plan · $390/mo for 10 seats. ActiveCampaign: Starter plan · $15/mo for 10 seats. Intercom sends a trigger (lead gets an email address) to Make Core ($10.59/mo), which performs an action in ActiveCampaign (create or update the contact). Each automation runs one way.

Diagram: how Intercom and ActiveCampaign connect, through Make Core, shown with the example automation described above. Drawn from the facts on this page.

 

### How do you set up Intercom + ActiveCampaign?

1. Log in to Make, create a scenario and add the Intercom module Watch Events as the trigger.
2. Connect Intercom: click Create a connection, enter a connection name, click Save, select your Make account to continue to intercom.com and follow the onscreen instructions. If the module has an instant tag, click Create a webhook first.
3. Add an ActiveCampaign module that creates or updates a contact. Connect ActiveCampaign: click Create a connection, enter the API key copied from your ActiveCampaign account, then the account name from its API URL, and click Save.
4. Map the lead's email address and name from Intercom into the contact's fields.
5. Click Run once in the toolbar to test it, then activate the scenario with the ON/OFF button on its details page. It runs every 15 minutes by default; click Every 15 minutes on the toolbar to change that.

Steps follow [Make's setup guide ↗](https://apps.make.com/intercom), read Nov 12, 2026.

**Limitations:** Each Make scenario runs one way. Make's ActiveCampaign guide says the app needs a paid ActiveCampaign account, so Starter is the minimum, and Make only needs an active Intercom account, so this page uses Intercom Essential. ActiveCampaign's listing doesn't say which connector it uses; this page models Make Core, the cheaper one.

Sources (checked Nov 12, 2026): [ActiveCampaign: Intercom integration ↗](https://www.activecampaign.com/apps/intercom) · [Make: Intercom app ↗](https://apps.make.com/intercom) · [Make: ActiveCampaign app ↗](https://apps.make.com/activecampaign) · [Make Help: Active and inactive scenarios ↗](https://help.make.com/active-and-inactive-scenarios) · [Make Help: Schedule a scenario ↗](https://help.make.com/schedule-a-scenario)

*Interactive cost calculator: open the web page to change team size, billing and add-ons.*

## Default 10-seat TCO summary

**Middleware integration costs $415.59/mo ($4,987.08/yr)** for a 10-seat team —
Intercom 'Essential' ($390.00/mo) + ActiveCampaign 'Starter' ($15.00/mo)
+ $10.59/mo middleware. No native connector exists for this pair.

 

## Native vs middleware for Intercom + ActiveCampaign

There's no native Intercom + ActiveCampaign connector, so a connector such as Make or Zapier is the integration rather than an alternative. Each automation runs one way (a trigger in one tool, an action in the other), and the connector's bill grows with the number of tasks or operations you run.

Chart: Intercom + ActiveCampaign: monthly cost for 10 seats by route: Make Core (modeled here) $415.59; Zapier Professional instead $434.99

Monthly cost for 10 seats by route, Intercom + ActiveCampaign.

 

Integration routes compared for a 10-seat team

| Route | Plans | 10 seats / month | Sync |
| --- | --- | --- | --- |
| Make Core (modeled here) | Intercom 'Essential' + ActiveCampaign 'Starter' | $415.59 | 1-way per automation |
| Zapier Professional instead | Intercom 'Essential' + ActiveCampaign 'Starter' | $434.99 | 1-way per automation |

Connector prices are monthly-billing list prices: Zapier Professional $29.99 (zapier.com/pricing) and Make Core $10.59 (from third-party pricing reviews, because make.com blocks automated checks). Both bill by usage, so high volumes cost more.

Image: [Intercom + ActiveCampaign integration cost summary: $415.59 a month for 10 seats, $10.59 of it is the hidden cost to connect; plans needed: Intercom Essential and ActiveCampaign Starter](https://stackcostmatrix.com/og/intercom-and-activecampaign.jpg)

## ✓ Verified Vendor Facts

- **Plan prices:** from each vendor's pricing page; any exception is flagged next to the date at the top.
- **Required tiers:** 'Essential' / 'Starter' — the minimum plans this integration needs.
- **API & webhook gates:** audited in official developer docs (see spec matrix).
- **Native app availability:** No native app — connected via middleware.

Requirements checked: Nov 12, 2026; prices: Nov 3, 2026 (exceptions listed at the top) · Sources linked below.

## ! Hidden Cost Trap

Requires Intercom on the 'Essential' plan or higher — Requires ActiveCampaign on the 'Starter' plan or higher — Plus $10.59/month middleware on top of both tools.

Intercom minimum tier
:   'Essential'

ActiveCampaign minimum tier
:   'Starter'

Middleware fee
:   $10.59/mo

The hidden cost here is the connector: there's no native Intercom + ActiveCampaign app, so you pay for Make Core ($10.59/mo) on top of both tools.

 [Connect Intercom + ActiveCampaign via Make.com — the middleware this integration runs on](https://stackcostmatrix.com/go/make) 

Affiliate link — we may earn a commission at no extra cost to you.

## Side-by-side spec matrix

Side-by-side spec matrix

| Spec | Intercom | ActiveCampaign |
| --- | --- | --- |
| Connection type | Middleware   Source: [Intercom docs ↗](https://developers.intercom.com/) · [ActiveCampaign docs ↗](https://developers.activecampaign.com/) · Verified Nov 12, 2026 | |
| Data sync direction | 1-way (trigger → action) | |
| Setup time | Under 1 hour (difficulty 1/5) | |
| Native integration supported | No — requires middleware (Zapier / Make) | |
| API available (distinct from native app) | Yes  — API ≠ native UI; API enables custom/middleware builds Source: [Intercom API docs ↗](https://developers.intercom.com/) · Verified Oct 17, 2026 | Yes  — API ≠ native UI; API enables custom/middleware builds Source: [ActiveCampaign API docs ↗](https://developers.activecampaign.com/) · Verified Oct 17, 2026 |
| API access at required tier | Yes  ('Essential') Paid workspaces Source: [Intercom developers: Webhooks ↗](https://developers.intercom.com/docs/webhooks) · Verified Nov 3, 2026 | Yes  ('Starter') Source: [ActiveCampaign: Getting started with the API ↗](https://help.activecampaign.com/hc/en-us/articles/207317590) · Verified Nov 3, 2026 |
| Webhook support at required tier | Yes  ('Essential') Source: [Intercom developers: Webhooks ↗](https://developers.intercom.com/docs/webhooks) · Verified Nov 3, 2026 | Yes  ('Starter') Source: [ActiveCampaign: Use webhooks ↗](https://help.activecampaign.com/hc/en-us/articles/115001403484) · Verified Nov 3, 2026 |

[Visit Intercom](https://stackcostmatrix.com/go/intercom)  [Visit ActiveCampaign](https://stackcostmatrix.com/go/activecampaign)

Some outbound links may earn us a referral commission at no extra cost to you. [Read our affiliate disclosure](https://stackcostmatrix.com/about/).

## Intercom + ActiveCampaign integration: frequently asked questions

### What are the minimum plan tiers required for the Intercom + ActiveCampaign integration?

To unlock the integration, Intercom must be on the 'Essential' plan or higher and ActiveCampaign must be on the 'Starter' plan or higher. Those are each tool's cheapest plan with API access (Intercom 'Essential' at $390/mo and ActiveCampaign 'Starter' at $15/mo for 10 seats), so the integration doesn't force an upgrade.

### How much does the Intercom + ActiveCampaign stack cost per month for a 10-person team?

At 10 seats with the required tiers (Intercom 'Essential' + ActiveCampaign 'Starter' + $10.59/month middleware), the stack costs $415.59 per month.

### Why does Intercom + ActiveCampaign need middleware, and what does it cost?

The Intercom + ActiveCampaign connection runs through middleware: neither vendor offers a native app for this pair, so this page models Make Core at $10.59 per month on top of both tools. Sync is one-way (a trigger in one tool runs an action in the other).

### What are the limitations of the Intercom + ActiveCampaign integration?

Each Make scenario runs one way. Make's ActiveCampaign guide says the app needs a paid ActiveCampaign account, so Starter is the minimum, and Make only needs an active Intercom account, so this page uses Intercom Essential. ActiveCampaign's listing doesn't say which connector it uses; this page models Make Core, the cheaper one.

## Integrations related to Intercom + ActiveCampaign

[All Intercom integrations →](https://stackcostmatrix.com/intercom-integrations-cost/) · [All ActiveCampaign integrations →](https://stackcostmatrix.com/activecampaign-integrations-cost/) · [Intercom API access by plan →](https://stackcostmatrix.com/intercom-api-access/) · [ActiveCampaign API access by plan →](https://stackcostmatrix.com/activecampaign-api-access/)

[### Intercom + Calendly

Native](https://stackcostmatrix.com/stack/intercom-and-calendly/)[### Intercom + HubSpot

Native](https://stackcostmatrix.com/stack/intercom-and-hubspot/)[### Intercom + Mailchimp

Native](https://stackcostmatrix.com/stack/intercom-and-mailchimp/)[### Intercom + Salesforce

Native](https://stackcostmatrix.com/stack/intercom-and-salesforce/)[### Intercom + Stripe

Native](https://stackcostmatrix.com/stack/intercom-and-stripe/)[### Pipedrive + Intercom

Native](https://stackcostmatrix.com/stack/pipedrive-and-intercom/)

Requirements checked: Nov 12, 2026; prices: Nov 3, 2026 (exceptions listed at the top)

## Verified sources

Every figure on this page links to its source below; prices that don't come straight from the vendor's page are flagged next to the date:

- [Intercom official pricing ↗](https://www.intercom.com/pricing)
- [Intercom API / developer docs ↗](https://developers.intercom.com/)
- [ActiveCampaign official pricing ↗](https://www.activecampaign.com/pricing)
- [ActiveCampaign API / developer docs ↗](https://developers.activecampaign.com/)
