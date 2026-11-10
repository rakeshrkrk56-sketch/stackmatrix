# About StackCostMatrix: Methodology & Sources

> Who publishes StackCostMatrix, our 3-step pricing verification methodology, and the official vendor documentation index behind every cost figure.

Source page: https://stackcostmatrix.com/about/  
Publisher: StackCostMatrix · Editor: Rakesh Kumar · Data licence: CC BY 4.0 (credit StackCostMatrix and link to https://stackcostmatrix.com)

---

# About StackCostMatrix

StackCostMatrix is an independent B2B software cost index. We research what
popular business tools *really* cost to connect — not the sticker
price on the pricing page, but the true monthly cost once you factor in
required plan tiers, API and webhook access gates, and middleware fees.

## Publisher & editor

**Editor: Rakesh Kumar.** StackCostMatrix is built and run by Rakesh Kumar, who checks each price and plan requirement against the vendor's own pricing pages and documentation and reviews every change before it's published. Corrections go to the email below and are logged in the changelog. Profiles: [LinkedIn ↗](https://www.linkedin.com/in/rakesh-kumar-23960a204/) · [GitHub ↗](https://github.com/rakeshrkrk56-sketch).

StackCostMatrix is published as an independent research project. Our dataset
— 18 tools plus 2 middleware services (Zapier and Make), 53 pricing plans, 59 integration pairs — is open and
auditable:

- **Contact:** [admin@stackcostmatrix.com](mailto:admin@stackcostmatrix.com)
- **Open dataset:** [github.com/rakeshrkrk56-sketch/stackmatrix](https://github.com/rakeshrkrk56-sketch/stackmatrix)
  — the current prices, plan gates and pair data are in [data/integration-pairs.json](https://github.com/rakeshrkrk56-sketch/stackmatrix/blob/main/data/integration-pairs.json) (CC BY 4.0). The older `database/seed.sql` snapshot predates the Nov 3, 2026 update and is kept for history only.
- **Corrections policy:** pricing
  changes reported by readers are re-verified against the vendor's
  official pages and updated with a new audit timestamp.

## 3-step verification methodology

**Step 1 — Audit official pricing pages.**
For each tool we record per-seat or per-user pricing for every public
plan tier directly from the vendor's own pricing page (linked below).
Two exceptions are flagged wherever they apply: Pipedrive's prices come from an indexed copy of its pricing page and Make's monthly price from third-party reviews, because both sites block automated checks. ActiveCampaign, Pipedrive and Salesforce publish annual-billing rates only, so those are the rates used.

**Step 2 — Audit API & webhook tier gates.**
We read each vendor's developer documentation and API rate-limit pages
to identify exactly which plan tier unlocks API access, outgoing
webhooks, and custom integrations — plus any paid API add-ons (e.g.
Salesforce's $25/user/month API add-on on Professional). This gate is
flagged as the integration's "hidden cost trap" because it is the most
commonly missed expense.

**Step 3 — Model middleware alternatives.**
Where no native path exists (or the native path forces an expensive tier
jump), we price the connection through published Zapier and Make plan
pricing, so the "via middleware" total reflects reality — and the
calculator lets you compare both totals at your team size.

Pricing pages for 17 of the 20 tools below were re-checked between **Nov 3 and Nov 5, 2026**; API documentation and the remaining pricing pages were last audited in **October 2026**.
When a vendor changes a price or tier gate, the mismatch is flagged for
re-verification — never silently rewritten.

## Official vendor documentation index

Every cost figure on StackCostMatrix traces to one of these official sources.
Last audited: **pricing Nov 2026 for 17 tools; API docs and other pricing Oct 2026**.

Official vendor documentation index

| Tool | Official pricing page | API / developer docs | Last audited |
| --- | --- | --- | --- |
| HubSpot | [Pricing ↗](https://www.hubspot.com/pricing) | [API docs ↗](https://developers.hubspot.com/docs/api/overview) | Pricing Nov 5, 2026 (all plans) · API docs Oct 2026 |
| Salesforce Sales Cloud | [Pricing ↗](https://www.salesforce.com/sales/pricing/) | [API docs ↗](https://developer.salesforce.com/) | Oct 2026 |
| Pipedrive | [Pricing ↗](https://www.pipedrive.com/pricing) | [API docs ↗](https://developers.pipedrive.com/docs/api/v1) | Oct 2026 · pricing updated Nov 2026 from an indexed copy |
| Monday.com | [Pricing ↗](https://monday.com/pricing) | [API docs ↗](https://developer.monday.com/) | Pricing Nov 2026 · API docs Oct 2026 |
| ClickUp | [Pricing ↗](https://clickup.com/pricing) | [API docs ↗](https://developer.clickup.com/) | Pricing Nov 2026 · API docs Oct 2026 |
| Asana | [Pricing ↗](https://asana.com/pricing) | [API docs ↗](https://developers.asana.com/docs) | Pricing Nov 2026 · API docs Oct 2026 |
| Slack | [Pricing ↗](https://slack.com/pricing) | [API docs ↗](https://api.slack.com/) | Pricing Nov 2026 · API docs Oct 2026 |
| Stripe | [Pricing ↗](https://stripe.com/pricing) | [API docs ↗](https://docs.stripe.com/api) | Pricing Nov 2026 · API docs Oct 2026 |
| ActiveCampaign | [Pricing ↗](https://www.activecampaign.com/pricing) | [API docs ↗](https://developers.activecampaign.com/) | Pricing Nov 2026 · API docs Oct 2026 |
| Mailchimp | [Pricing ↗](https://mailchimp.com/pricing/) | [API docs ↗](https://mailchimp.com/developer/) | Pricing Nov 2026 · API docs Oct 2026 |
| Zendesk | [Pricing ↗](https://www.zendesk.com/pricing/) | [API docs ↗](https://developer.zendesk.com/) | Pricing Nov 2026 · API docs Oct 2026 |
| Freshdesk | [Pricing ↗](https://www.freshworks.com/freshdesk/pricing/) | [API docs ↗](https://developers.freshdesk.com/) | Pricing Nov 2026 · API docs Oct 2026 |
| Intercom | [Pricing ↗](https://www.intercom.com/pricing) | [API docs ↗](https://developers.intercom.com/) | Pricing Nov 2026 · API docs Oct 2026 |
| Notion | [Pricing ↗](https://www.notion.so/pricing) | [API docs ↗](https://developers.notion.com/) | Pricing Nov 2026 · API docs Oct 2026 |
| Airtable | [Pricing ↗](https://www.airtable.com/pricing) | [API docs ↗](https://airtable.com/developers/web/api/introduction) | Pricing Nov 2026 · API docs Oct 2026 |
| Zapier | [Pricing ↗](https://zapier.com/pricing) | [API docs ↗](https://zapier.com/developer/documentation) | Pricing Nov 2026 · API docs Oct 2026 |
| Make | [Pricing ↗](https://www.make.com/en/pricing) | [API docs ↗](https://www.make.com/en/api-documentation) | Oct 2026 · monthly price Nov 2026 from third-party reviews |
| QuickBooks Online | [Pricing ↗](https://quickbooks.intuit.com/pricing/) | [API docs ↗](https://developer.intuit.com/app/developer/qbo/docs/get-started) | Pricing Nov 2026 · API docs Oct 2026 |
| Xero | [Pricing ↗](https://www.xero.com/pricing/) | [API docs ↗](https://developer.xero.com/) | Pricing Nov 2026 · API docs Oct 2026 |
| Calendly | [Pricing ↗](https://calendly.com/pricing) | [API docs ↗](https://developer.calendly.com/) | Pricing Nov 2026 · API docs Oct 2026 |

## 2026 SaaS Pricing & API Gate Changelog

Every change to our pricing data and cost models is logged here with a
date.

- **Nov 10, 2026 — Setup guides, clearer Salesforce requirements, share images.** Every integration page now opens with how the integration works and a link to the vendor's setup guide, and compares the native route with Make and Zapier in one table. Stripe + Slack gained step-by-step setup from Stripe's documentation. The Salesforce API page now explains how Professional gets API access and that some AppExchange apps work without the add-on, from Salesforce's developer docs; the HubSpot Professional guide covers the Salesforce side and HubSpot's one-time onboarding fees. The Integration Tax report adds a section on the three kinds of integration cost and a chart image. No prices or plan requirements changed.
- **Nov 8, 2026 — Three integrations corrected; site-wide accuracy pass.** Re-read on the vendors' own pages: ActiveCampaign's app directory lists its Stripe integration as included with Plus, Professional and Enterprise, so ActiveCampaign + Stripe now models Plus ($15 → $49 a month); Calendly's help article says any Mailchimp account works, including Free, so Mailchimp + Calendly drops from $133 to $120; and Pipedrive's own Xero integration is no longer offered (the Marketplace app is a paid third-party app), so Pipedrive + Xero now models Make Core ($167 → $177.59). Slack + Airtable and Slack + Calendly are now shown as one-way notifications. In the Integration Tax report, 31 of 55 integrations now carry a hidden cost (was 29) and 24 cost nothing extra (was 26); the typical forced-upgrade range is unchanged at $120–$251. Also fixed: stale integration counts and connector prices on the HubSpot, Salesforce and CRM guides, the sourcing note in our methodology, and 15 integration pages that had no setup notes now explain how the integration works, with sources. Every page now names its editor.
- **Nov 5, 2026 — HubSpot Professional repriced; new HubSpot Professional guide.** HubSpot's help docs list the Salesforce connector and the Asana workflow action as available on *any* Professional subscription, and the cheapest is Smart CRM Professional at $50 per seat a month ($45 on an annual commitment). The site had modeled Professional as a flat $800 a month (Marketing Hub's annual price, which includes only 3 seats). At 10 seats, HubSpot + Salesforce drops from $2,050 to $1,750 a month and HubSpot + Asana from $934.90 to $634.90. In the Integration Tax report the most expensive integrations now cost $500 a month extra (was $800) and forced upgrades make up 93% of the tax (was 94%); the headline figures are unchanged. HubSpot Enterprise is now Smart CRM Enterprise at $75 per seat. New page: [which integrations need HubSpot Professional](https://stackcostmatrix.com/hubspot-professional-integrations/).
- **Nov 4, 2026 — QuickBooks prices updated.** QuickBooks Online now lists Simple Start at $38, Essentials at $75 and Plus at $115 a month (was $35, $65 and $99), read on Intuit's pricing page. Every QuickBooks integration page is updated.
- **Nov 4, 2026 — Pipedrive + Mailchimp re-checked; Make wording corrected.** Pipedrive's Marketplace lists its Mailchimp sync app as free and neither vendor names a Mailchimp plan, so the pair now models Mailchimp's free plan ($153 → $140 a month at 10 seats). The Integration Tax report updates accordingly: 29 of 55 integrations carry a hidden cost (was 30). Native pages now compare against Make Core at its $10.59 monthly price instead of $9, and the outdated “free up to 1,000 ops/mo” note on Make buttons is removed, since Make now bills in credits.
- **Nov 4, 2026 — Four new integration pairs.** HubSpot + QuickBooks Online and Pipedrive + QuickBooks Online (both native), and Salesforce + QuickBooks Online and Pipedrive + Salesforce (both through Make, with Salesforce's API add-on), each checked against the vendors' own documentation. The index now covers 59 pairs.
- **Nov 3, 2026 — Xero + Calendly re-checked.** Zapier's Xero app needs a paid Xero account but no particular plan, so the pair now models Xero Early instead of Growing ($208.99 → $176.99 a month at 10 seats). The page notes that Early allows 20 approved sales invoices a month through the API, so invoicing more than 20 bookings a month needs Growing.
- **Nov 3, 2026 — Xero + ActiveCampaign re-checked.** ActiveCampaign lists its Xero connection as middleware enabled by Zapier, and Make's Xero app asks only for a Xero account, so the pair now models Xero Early instead of Growing ($84.59 → $52.59 a month at 10 seats), with Early's 20-invoice monthly limit disclosed. No integration is waiting for a requirements re-check any more.
- **Nov 3, 2026 — QuickBooks requirements re-checked.** Zapier, Make and Mailchimp's QuickBooks integrations ask only for a QuickBooks Online account (Zapier: a paid one), so five integrations now model QuickBooks Simple Start instead of Plus, $64 a month less at 10 seats. Stripe + QuickBooks is reclassified from native to middleware: Stripe's QuickBooks integrations are third-party apps, so it now models Make Core ($65.00 → $45.59 a month).
- **Nov 3, 2026 — Published [The Integration Tax 2026](https://stackcostmatrix.com/integration-tax-2026/).** Original research on the extra monthly cost of connecting SaaS tools, built from the 55 pair calculators and released under CC BY 4.0.
- **Nov 3, 2026 — API and webhook access re-checked for every plan.** All 53 plans were checked against the vendors' developer and help-center docs, separating developer webhooks from no-code webhook automation actions. Webhook facts were corrected on 54 pair pages; most of the October data had marked webhooks unavailable where the vendor documents them. Four pairs no longer require a plan upgrade that rested on a disproved webhook gate: Asana + QuickBooks (Asana Starter, $414.49 → $244.49/mo), Notion + Stripe (Notion Plus, $250.59 → $130.59), Monday.com + QuickBooks (Monday Standard, $349.59 → $249.59) and Zendesk + Notion (Suite Team, $1,299.99 → $839.99), at 10 seats. New API & webhook access pages for 18 tools publish the per-plan facts with sources.
- **Nov 3, 2026 — Connector fees put on the same billing basis as tool plans.** Middleware fees now use the monthly-billing price in monthly totals and the annual-billing price in annual totals: Make Core $10.59 monthly / $9 annual, Zapier Professional (formerly Starter) $29.99 / $19.99, Data Mapper for Mailchimp $15 / $12.75. The three Airtable pairs that run through Make now model Airtable Team, because the Free plan's 1,000 API calls a month are too few for an ongoing sync. Stripe + Mailchimp now states that Data Mapper's Starter plan syncs customers only and purchase sync needs Pro ($30/month).
- **Nov 3, 2026 — Integration requirements re-checked against vendor docs.** 53 of 55 pairs checked against the vendors' help centers and integration listings; connection type or minimum plan corrected on 37 pairs, counting a free plan as the minimum where the vendor documents the integration working on it. Xero prices updated to Early $27 · Growing $59 · Established $97 per month and Pipedrive to Lite $14 · Growth $39 · Premium $59 · Ultimate $79 per seat (billed annually). ActiveCampaign, ClickUp, Freshdesk, Notion, Slack and Zendesk prices updated from the vendors' pricing pages. Plan prices are now monthly-billing list prices (for example Zendesk Suite Team $69 per agent), and the calculator's annual-billing option uses each vendor's published annual price instead of a flat 20%; ActiveCampaign, Pipedrive and Salesforce publish annual-billing rates only, so no further discount is applied to them. 28 pairs now have a sourced "How it works" section.
- **Oct 20, 2026 — Accuracy pass on all 55 pairs.** Calculator outputs now server-rendered (no empty states for crawlers); spec tables carry a per-claim source link and verified date; reviewer byline and correction link added to every pair page.
- **Oct 19, 2026 — TCO Calculator 2.0 launched site-wide.** Full cost model (Cm = SA + SB + M + U + H) with incremental-cost mode, annual-billing toggle, and shareable cost reports on all 55 pair pages.
- **Oct 19, 2026 — Vendor documentation index published.** All 40 official pricing and API-doc URLs (20 tools × 2) re-checked live and linked with "Last Audited: October 2026".
- **Oct 18, 2026 — Pillar cost guides published.** HubSpot, Salesforce, and CRM pricing-guide hubs interlinking every relevant calculator; sitemap submitted to Google Search Console and IndexNow.
- **Oct 17, 2026 — Full pricing re-audit.** HubSpot Starter confirmed at $20/seat; Salesforce Professional confirmed at $100/user plus the $25/user/mo API add-on; Pipedrive Enterprise confirmed at $99.
- **Oct 17, 2026 — Launch.** 55 integration pairs across 20 tools, each with verified minimum plan tiers and hidden-cost analysis.

## Independence & affiliate disclosure

StackCostMatrix is an independent B2B software cost index. Some outbound
links may earn us a referral commission at no extra cost to you. These
commissions never influence our cost figures, tier requirements, or
source citations — the numbers are the numbers, and the sources are
linked above for anyone to verify.
