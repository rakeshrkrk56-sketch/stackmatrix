# ClickUp + Salesforce Sales Cloud Integration (2026): How It Works, Setup & True Cost

> How the ClickUp + Salesforce Sales Cloud integration works and how to set it up, plus the plans it needs and the 10-seat cost ($1,260.59/mo).

Source page: https://stackcostmatrix.com/stack/clickup-and-salesforce/  
Publisher: StackCostMatrix · Editor: Rakesh Kumar · Data licence: CC BY 4.0 (credit StackCostMatrix and link to https://stackcostmatrix.com)

---

[Home](https://stackcostmatrix.com/) / ClickUp + Salesforce Sales Cloud 

There's no native ClickUp–Salesforce connector: ClickUp's own Salesforce page points to Zapier, and Make Core also links them through Salesforce's API, which Professional Edition gets only as a paid add-on. Requires ClickUp on the 'Free' plan and Salesforce Sales Cloud on the 'Professional' plan. Route it through Make Core ($10.59/mo, or $9/mo billed annually).

Edited by [Rakesh Kumar](https://stackcostmatrix.com/about/#editor), founder of StackCostMatrix | Integration requirements checked against official vendor docs · Nov 12, 2026 · Prices checked · Nov 3, 2026 (Salesforce prices: Oct 17, 2026; Make fee: $9 annual price Oct 17, 2026; $10.59 monthly price from third-party pricing reviews, Nov 3, 2026, as make.com blocks automated checks) · Setup steps: Nov 12, 2026 | [Spot an outdated price? Report a correction →](mailto:admin@stackcostmatrix.com?subject=Price%20Correction)

## How the ClickUp + Salesforce Sales Cloud integration works

**Does ClickUp integrate with Salesforce Sales Cloud?** Not natively. ClickUp's own Salesforce page offers to connect the two through Zapier, for example to create ClickUp tasks from Salesforce actions and update Salesforce records as tasks are completed. Make does the same through Salesforce's API, which Professional Edition only gets as a paid add-on.

With Make, a scenario watches Salesforce, for example for a won opportunity, and creates a ClickUp task for the team that delivers; another can watch ClickUp and update the Salesforce record when the task is done. Each scenario runs one way. Make's Salesforce guide notes that not all Salesforce editions have API access.

[Setup guide: Make: Salesforce app ↗](https://apps.make.com/salesforce)

Diagram of how ClickUp and Salesforce Sales Cloud connect. Salesforce Sales Cloud: Professional + API add-on · $1,250/mo for 10 seats. ClickUp: Free plan · $0/mo for 10 seats. Salesforce Sales Cloud sends a trigger (opportunity won) to Make Core ($10.59/mo), which performs an action in ClickUp (create a task). Each automation runs one way.

Diagram: how ClickUp and Salesforce Sales Cloud connect, through Make Core, shown with the example automation described above. Drawn from the facts on this page.

 

### How do you set up ClickUp + Salesforce Sales Cloud?

1. Make sure your Salesforce org has API access: Enterprise and Unlimited include it, Professional needs the API add-on.
2. Log in to Make, create a scenario and add the Salesforce module Watch records as the trigger.
3. Connect Salesforce: click Create a connection, choose the Salesforce connection type, say whether you're using a Salesforce Sandbox, click Save and sign in.
4. Add a ClickUp module that creates a task. Connect ClickUp: click Create a connection, click Save and sign in to ClickUp if prompted.
5. Map the Salesforce fields into the task's name, list and description.
6. Click Run once in the toolbar to test it, then activate the scenario with the ON/OFF button on its details page. It runs every 15 minutes by default; click Every 15 minutes on the toolbar to change that.

Steps follow [Make's setup guide ↗](https://apps.make.com/salesforce), read Nov 12, 2026.

**Limitations:** This calculator models Salesforce Professional with the $25/user API add-on plus Make Core; Enterprise includes API access without the add-on. ClickUp's page suggests Zapier, which would cost more. Each Make scenario runs one way.

Sources (checked Nov 12, 2026): [ClickUp: Salesforce integration ↗](https://clickup.com/integrations/salesforce) · [Make: Salesforce app ↗](https://apps.make.com/salesforce) · [Make: ClickUp app ↗](https://apps.make.com/clickup) · [Make Help: Active and inactive scenarios ↗](https://help.make.com/active-and-inactive-scenarios) · [Make Help: Schedule a scenario ↗](https://help.make.com/schedule-a-scenario)

*Interactive cost calculator: open the web page to change team size, billing and add-ons.*

## Default 10-seat TCO summary

**Middleware integration costs $1,260.59/mo ($15,127.08/yr)** for a 10-seat team —
ClickUp 'Free' ($0.00/mo) + Salesforce Sales Cloud 'Professional' ($1,250.00/mo)
+ $10.59/mo middleware. No native connector exists for this pair.
Salesforce's $1,250.00 is the Professional plan ($100/user) plus the API add-on, which Salesforce sells through an account executive; this page models it at $25/user ($250 at 10 seats).

 

## Native vs middleware for ClickUp + Salesforce Sales Cloud

There's no native ClickUp + Salesforce Sales Cloud connector, so a connector such as Make or Zapier is the integration rather than an alternative. Each automation runs one way (a trigger in one tool, an action in the other), and the connector's bill grows with the number of tasks or operations you run.

Chart: ClickUp + Salesforce Sales Cloud: monthly cost for 10 seats by route: Make Core (modeled here) $1,260.59; Zapier Professional instead $1,279.99

Monthly cost for 10 seats by route, ClickUp + Salesforce Sales Cloud.

 

Integration routes compared for a 10-seat team

| Route | Plans | 10 seats / month | Sync |
| --- | --- | --- | --- |
| Make Core (modeled here) | ClickUp 'Free' + Salesforce Sales Cloud 'Professional' | $1,260.59 | 1-way per automation |
| Zapier Professional instead | ClickUp 'Free' + Salesforce Sales Cloud 'Professional' | $1,279.99 | 1-way per automation |

Connector prices are monthly-billing list prices: Zapier Professional $29.99 (zapier.com/pricing) and Make Core $10.59 (from third-party pricing reviews, because make.com blocks automated checks). Both bill by usage, so high volumes cost more.

Image: [ClickUp + Salesforce Sales Cloud integration cost summary: $1,260.59 a month for 10 seats, $10.59 of it is the hidden cost to connect; plans needed: ClickUp Free and Salesforce Sales Cloud Professional](https://stackcostmatrix.com/og/clickup-and-salesforce.jpg)

## ✓ Verified Vendor Facts

- **Plan prices:** from each vendor's pricing page; any exception is flagged next to the date at the top.
- **Required tiers:** 'Free' / 'Professional' — the minimum plans this integration needs.
- **API & webhook gates:** audited in official developer docs (see spec matrix).
- **Native app availability:** No native app — connected via middleware.

Requirements checked: Nov 12, 2026; prices: Nov 3, 2026 (exceptions listed at the top) · Sources linked below.

## ! Hidden Cost Trap

Requires ClickUp on the 'Free' plan or higher — Requires Salesforce Sales Cloud on the 'Professional' plan or higher — Plus $10.59/month middleware on top of both tools.

ClickUp minimum tier
:   'Free'

Salesforce Sales Cloud minimum tier
:   'Professional'

Middleware fee
:   $10.59/mo

The hidden cost here is the connector: there's no native ClickUp + Salesforce Sales Cloud app, so you pay for Make Core ($10.59/mo) on top of both tools.

 [Connect ClickUp + Salesforce Sales Cloud via Make.com — the middleware this integration runs on](https://stackcostmatrix.com/go/make) 

Affiliate link — we may earn a commission at no extra cost to you.

## Side-by-side spec matrix

Side-by-side spec matrix

| Spec | ClickUp | Salesforce Sales Cloud |
| --- | --- | --- |
| Connection type | Middleware   Source: [ClickUp docs ↗](https://developer.clickup.com/) · [Salesforce Sales Cloud docs ↗](https://developer.salesforce.com/) · Verified Nov 12, 2026 | |
| Data sync direction | 1-way (trigger → action) | |
| Setup time | 1–3 hours (difficulty 2/5) | |
| Native integration supported | No — requires middleware (Zapier / Make) | |
| API available (distinct from native app) | Yes  — API ≠ native UI; API enables custom/middleware builds Source: [ClickUp API docs ↗](https://developer.clickup.com/) · Verified Oct 17, 2026 | Yes  — API ≠ native UI; API enables custom/middleware builds Source: [Salesforce Sales Cloud API docs ↗](https://developer.salesforce.com/) · Verified Oct 17, 2026 |
| API access at required tier | Yes  ('Free') 100 requests/min per token Source: [ClickUp developers: API availability by plan ↗](https://developer.clickup.com/docs/apis-available-by-plan) · Verified Nov 3, 2026 | Yes  ('Professional') Web Services API add-on (modeled at $25/user) Source: [Salesforce developers: Supported editions ↗](https://developer.salesforce.com/docs/platform/api-rest/guide/intro-rest-compatible-editions.html) · Verified Nov 3, 2026 |
| Webhook support at required tier | Yes  ('Free') API webhooks Source: [ClickUp: Automation webhooks ↗](https://help.clickup.com/hc/en-us/articles/35313844961943-Integrate-ClickUp-using-Automation-webhooks) · Verified Nov 3, 2026 | No  ('Professional') Change Data Capture (Salesforce's change-event feed) isn't available on Professional, so sync runs through the REST API. Source: [Salesforce developers: Change Data Capture ↗](https://developer.salesforce.com/docs/atlas.en-us.change_data_capture.meta/change_data_capture/cdc_intro.htm) · Verified Nov 8, 2026 |

[Visit ClickUp](https://stackcostmatrix.com/go/clickup)  [Visit Salesforce Sales Cloud](https://stackcostmatrix.com/go/salesforce)

Some outbound links may earn us a referral commission at no extra cost to you. [Read our affiliate disclosure](https://stackcostmatrix.com/about/).

## ClickUp + Salesforce Sales Cloud integration: frequently asked questions

### What are the minimum plan tiers required for the ClickUp + Salesforce Sales Cloud integration?

To unlock the integration, ClickUp must be on the 'Free' plan or higher and Salesforce Sales Cloud must be on the 'Professional' plan or higher. Those are each tool's cheapest plan with API access (ClickUp 'Free' at $0/mo and Salesforce Sales Cloud 'Professional' at $1,250/mo for 10 seats), so the integration doesn't force an upgrade.

### How much does the ClickUp + Salesforce Sales Cloud stack cost per month for a 10-person team?

At 10 seats with the required tiers (ClickUp 'Free' + Salesforce Sales Cloud 'Professional' + $10.59/month middleware), the stack costs $1,260.59 per month.

### Why does ClickUp + Salesforce Sales Cloud need middleware, and what does it cost?

The ClickUp + Salesforce Sales Cloud connection runs through middleware: neither vendor offers a native app for this pair, so this page models Make Core at $10.59 per month on top of both tools. Sync is one-way (a trigger in one tool runs an action in the other).

### What are the limitations of the ClickUp + Salesforce Sales Cloud integration?

This calculator models Salesforce Professional with the $25/user API add-on plus Make Core; Enterprise includes API access without the add-on. ClickUp's page suggests Zapier, which would cost more. Each Make scenario runs one way.

## Integrations related to ClickUp + Salesforce Sales Cloud

[All ClickUp integrations →](https://stackcostmatrix.com/clickup-integrations-cost/) · [All Salesforce integrations →](https://stackcostmatrix.com/salesforce-integrations-cost/) · [ClickUp API access by plan →](https://stackcostmatrix.com/clickup-api-access/) · [Salesforce API access by plan →](https://stackcostmatrix.com/salesforce-api-access/)

Part of our [CRM integration hidden-costs guide](https://stackcostmatrix.com/crm-integration-pricing-guide/).

[### ClickUp + ActiveCampaign

Middleware](https://stackcostmatrix.com/stack/clickup-and-activecampaign/)[### ClickUp + Notion

Native](https://stackcostmatrix.com/stack/clickup-and-notion/)[### ClickUp + Slack

Native](https://stackcostmatrix.com/stack/clickup-and-slack/)[### ClickUp + Stripe

Middleware](https://stackcostmatrix.com/stack/clickup-and-stripe/)[### ClickUp + Zendesk

Native](https://stackcostmatrix.com/stack/clickup-and-zendesk/)[### HubSpot + ClickUp

Native](https://stackcostmatrix.com/stack/hubspot-and-clickup/)

Requirements checked: Nov 12, 2026; prices: Nov 3, 2026 (exceptions listed at the top)

## Verified sources

Every figure on this page links to its source below; prices that don't come straight from the vendor's page are flagged next to the date:

- [ClickUp official pricing ↗](https://clickup.com/pricing)
- [ClickUp API / developer docs ↗](https://developer.clickup.com/)
- [Salesforce Sales Cloud official pricing ↗](https://www.salesforce.com/sales/pricing/)
- [Salesforce Sales Cloud API / developer docs ↗](https://developer.salesforce.com/)
