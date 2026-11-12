# Open B2B SaaS Integration Cost & API Gate Index (2026)

**The true cost of your software stack — not the sticker price.**

This is the open data behind [StackMatrix](https://stackcostmatrix.com), a free index of **90 B2B software integration pairs** across 20 tools. For every pair, we publish the **true monthly and annual cost**: minimum required plan tiers, hidden API and webhook gates, per-seat pricing traps, and native vs middleware (Zapier/Make) totals.

🌐 **Live site:** https://stackcostmatrix.com

## Why this exists

Vendors advertise integrations as "free" or "included" — then gate the API access, webhooks, or automation features the integration depends on behind a plan tier costing 3–5x more. Examples we've documented:

- **Salesforce** charges **$25/user/month extra** for API access on the $100/user Professional plan — a $12,000/year hidden tax for a 40-person team. ([Salesforce + Stripe breakdown](https://stackcostmatrix.com/stack/salesforce-and-stripe/))
- **HubSpot's** native Salesforce connector only works on **HubSpot Professional or Enterprise**, so the free CRM can't use it. ([HubSpot + Salesforce breakdown](https://stackcostmatrix.com/stack/hubspot-and-salesforce/))
- **Per-seat traps:** a $20/seat tier jump across 50 users = $12,000/year, even if only 5 people use the connected workflow.

## What's inside

- **90 integration calculators** — interactive true-cost calculator (1–100 seat slider, required-tier toggle), hidden-cost trap callout, spec matrix, and setup guide per pair. [Browse all pairs](https://stackcostmatrix.com)
- **Pillar cost guides:**
  - [Complete 2026 HubSpot Integration Cost & API Tier Matrix](https://stackcostmatrix.com/hubspot-integrations-cost/)
  - [Complete 2026 Salesforce Integration Cost & API Tier Matrix](https://stackcostmatrix.com/salesforce-integrations-cost/)
  - [B2B CRM Integration Hidden Costs: Native vs Zapier/Make Middleware Guide](https://stackcostmatrix.com/crm-integration-pricing-guide/)
- **Popular calculators:**
  - [HubSpot + Slack](https://stackcostmatrix.com/stack/hubspot-and-slack/) · [HubSpot + Stripe](https://stackcostmatrix.com/stack/hubspot-and-stripe/) · [HubSpot + Mailchimp](https://stackcostmatrix.com/stack/hubspot-and-mailchimp/) · [HubSpot + Salesforce](https://stackcostmatrix.com/stack/hubspot-and-salesforce/)
  - [Salesforce + Slack](https://stackcostmatrix.com/stack/salesforce-and-slack/) · [Salesforce + Stripe](https://stackcostmatrix.com/stack/salesforce-and-stripe/) · [Salesforce + Zendesk](https://stackcostmatrix.com/stack/salesforce-and-zendesk/)
  - [Pipedrive + Slack](https://stackcostmatrix.com/stack/pipedrive-and-slack/) · [Pipedrive + Xero](https://stackcostmatrix.com/stack/pipedrive-and-xero/) · [Stripe + Slack](https://stackcostmatrix.com/stack/stripe-and-slack/)

## Methodology

Prices and integration requirements are checked against the vendors' own pricing pages, help centers and integration listings. Each pair page and each record in `data/integration-pairs.json` states what was checked and when, including exceptions (for example, Salesforce prices were last verified on 2026-10-17). Mismatches are flagged for review, never silently rewritten.

## Data

- `data/integration-pairs.json` — **current data**: 18 tools plus Zapier and Make, 53 pricing plans and all 90 integration pairs, exported from the live site (see `data/README.md`)
- `scripts/` — the maintenance toolkit that regenerates and checks the pages (see `scripts/README.md`). The original Astro source, database snapshot and seeding scripts were removed on 2026-11-08 and remain in the git history.

The pricing data (`data/integration-pairs.json` and the published cost figures on stackcostmatrix.com) is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/): you may reuse and adapt it, including commercially, as long as you credit StackCostMatrix and link to https://stackcostmatrix.com.

## Affiliate disclosure

Some outbound links on the live site may earn a referral commission at no extra cost to the user.

---

© 2026 StackCostMatrix.com

---

## Complete page directory (crawlable index)

Every calculator and guide on the live site, for search engines and researchers:

### Pillar guides
- [Crm Integration Pricing Guide](https://stackcostmatrix.com/crm-integration-pricing-guide/)
- [Hubspot Integrations Cost](https://stackcostmatrix.com/hubspot-integrations-cost/)
- [Salesforce Integrations Cost](https://stackcostmatrix.com/salesforce-integrations-cost/)

### All 90 integration cost calculators
- [Activecampaign + Calendly](https://stackcostmatrix.com/stack/activecampaign-and-calendly/)
- [Activecampaign + Pipedrive](https://stackcostmatrix.com/stack/activecampaign-and-pipedrive/)
- [Activecampaign + Slack](https://stackcostmatrix.com/stack/activecampaign-and-slack/)
- [Activecampaign + Stripe](https://stackcostmatrix.com/stack/activecampaign-and-stripe/)
- [Airtable + Quickbooks](https://stackcostmatrix.com/stack/airtable-and-quickbooks/)
- [Airtable + Stripe](https://stackcostmatrix.com/stack/airtable-and-stripe/)
- [Asana + Activecampaign](https://stackcostmatrix.com/stack/asana-and-activecampaign/)
- [Asana + Mailchimp](https://stackcostmatrix.com/stack/asana-and-mailchimp/)
- [Asana + Notion](https://stackcostmatrix.com/stack/asana-and-notion/)
- [Asana + Quickbooks](https://stackcostmatrix.com/stack/asana-and-quickbooks/)
- [Asana + Salesforce](https://stackcostmatrix.com/stack/asana-and-salesforce/)
- [Asana + Slack](https://stackcostmatrix.com/stack/asana-and-slack/)
- [Clickup + Activecampaign](https://stackcostmatrix.com/stack/clickup-and-activecampaign/)
- [Clickup + Notion](https://stackcostmatrix.com/stack/clickup-and-notion/)
- [Clickup + Salesforce](https://stackcostmatrix.com/stack/clickup-and-salesforce/)
- [Clickup + Slack](https://stackcostmatrix.com/stack/clickup-and-slack/)
- [Clickup + Stripe](https://stackcostmatrix.com/stack/clickup-and-stripe/)
- [Clickup + Zendesk](https://stackcostmatrix.com/stack/clickup-and-zendesk/)
- [Freshdesk + Activecampaign](https://stackcostmatrix.com/stack/freshdesk-and-activecampaign/)
- [Freshdesk + Hubspot](https://stackcostmatrix.com/stack/freshdesk-and-hubspot/)
- [Freshdesk + Slack](https://stackcostmatrix.com/stack/freshdesk-and-slack/)
- [Hubspot + Airtable](https://stackcostmatrix.com/stack/hubspot-and-airtable/)
- [Hubspot + Asana](https://stackcostmatrix.com/stack/hubspot-and-asana/)
- [Hubspot + Calendly](https://stackcostmatrix.com/stack/hubspot-and-calendly/)
- [Hubspot + Clickup](https://stackcostmatrix.com/stack/hubspot-and-clickup/)
- [Hubspot + Mailchimp](https://stackcostmatrix.com/stack/hubspot-and-mailchimp/)
- [Hubspot + Monday](https://stackcostmatrix.com/stack/hubspot-and-monday/)
- [Hubspot + Notion](https://stackcostmatrix.com/stack/hubspot-and-notion/)
- [Hubspot + Pipedrive](https://stackcostmatrix.com/stack/hubspot-and-pipedrive/)
- [Hubspot + Quickbooks](https://stackcostmatrix.com/stack/hubspot-and-quickbooks/)
- [Hubspot + Salesforce](https://stackcostmatrix.com/stack/hubspot-and-salesforce/)
- [Hubspot + Slack](https://stackcostmatrix.com/stack/hubspot-and-slack/)
- [Hubspot + Stripe](https://stackcostmatrix.com/stack/hubspot-and-stripe/)
- [Hubspot + Xero](https://stackcostmatrix.com/stack/hubspot-and-xero/)
- [Hubspot + Zendesk](https://stackcostmatrix.com/stack/hubspot-and-zendesk/)
- [Intercom + Activecampaign](https://stackcostmatrix.com/stack/intercom-and-activecampaign/)
- [Intercom + Calendly](https://stackcostmatrix.com/stack/intercom-and-calendly/)
- [Intercom + Hubspot](https://stackcostmatrix.com/stack/intercom-and-hubspot/)
- [Intercom + Mailchimp](https://stackcostmatrix.com/stack/intercom-and-mailchimp/)
- [Intercom + Salesforce](https://stackcostmatrix.com/stack/intercom-and-salesforce/)
- [Intercom + Stripe](https://stackcostmatrix.com/stack/intercom-and-stripe/)
- [Mailchimp + Airtable](https://stackcostmatrix.com/stack/mailchimp-and-airtable/)
- [Mailchimp + Calendly](https://stackcostmatrix.com/stack/mailchimp-and-calendly/)
- [Mailchimp + Slack](https://stackcostmatrix.com/stack/mailchimp-and-slack/)
- [Monday + Activecampaign](https://stackcostmatrix.com/stack/monday-and-activecampaign/)
- [Monday + Mailchimp](https://stackcostmatrix.com/stack/monday-and-mailchimp/)
- [Monday + Quickbooks](https://stackcostmatrix.com/stack/monday-and-quickbooks/)
- [Monday + Slack](https://stackcostmatrix.com/stack/monday-and-slack/)
- [Monday + Zendesk](https://stackcostmatrix.com/stack/monday-and-zendesk/)
- [Notion + Calendly](https://stackcostmatrix.com/stack/notion-and-calendly/)
- [Notion + Stripe](https://stackcostmatrix.com/stack/notion-and-stripe/)
- [Pipedrive + Asana](https://stackcostmatrix.com/stack/pipedrive-and-asana/)
- [Pipedrive + Calendly](https://stackcostmatrix.com/stack/pipedrive-and-calendly/)
- [Pipedrive + Intercom](https://stackcostmatrix.com/stack/pipedrive-and-intercom/)
- [Pipedrive + Mailchimp](https://stackcostmatrix.com/stack/pipedrive-and-mailchimp/)
- [Pipedrive + Quickbooks](https://stackcostmatrix.com/stack/pipedrive-and-quickbooks/)
- [Pipedrive + Salesforce](https://stackcostmatrix.com/stack/pipedrive-and-salesforce/)
- [Pipedrive + Slack](https://stackcostmatrix.com/stack/pipedrive-and-slack/)
- [Pipedrive + Xero](https://stackcostmatrix.com/stack/pipedrive-and-xero/)
- [Pipedrive + Zendesk](https://stackcostmatrix.com/stack/pipedrive-and-zendesk/)
- [Quickbooks + Mailchimp](https://stackcostmatrix.com/stack/quickbooks-and-mailchimp/)
- [Quickbooks + Slack](https://stackcostmatrix.com/stack/quickbooks-and-slack/)
- [Salesforce + Airtable](https://stackcostmatrix.com/stack/salesforce-and-airtable/)
- [Salesforce + Calendly](https://stackcostmatrix.com/stack/salesforce-and-calendly/)
- [Salesforce + Mailchimp](https://stackcostmatrix.com/stack/salesforce-and-mailchimp/)
- [Salesforce + Quickbooks](https://stackcostmatrix.com/stack/salesforce-and-quickbooks/)
- [Salesforce + Slack](https://stackcostmatrix.com/stack/salesforce-and-slack/)
- [Salesforce + Stripe](https://stackcostmatrix.com/stack/salesforce-and-stripe/)
- [Salesforce + Xero](https://stackcostmatrix.com/stack/salesforce-and-xero/)
- [Salesforce + Zendesk](https://stackcostmatrix.com/stack/salesforce-and-zendesk/)
- [Slack + Airtable](https://stackcostmatrix.com/stack/slack-and-airtable/)
- [Slack + Calendly](https://stackcostmatrix.com/stack/slack-and-calendly/)
- [Slack + Intercom](https://stackcostmatrix.com/stack/slack-and-intercom/)
- [Slack + Notion](https://stackcostmatrix.com/stack/slack-and-notion/)
- [Slack + Zendesk](https://stackcostmatrix.com/stack/slack-and-zendesk/)
- [Stripe + Calendly](https://stackcostmatrix.com/stack/stripe-and-calendly/)
- [Stripe + Mailchimp](https://stackcostmatrix.com/stack/stripe-and-mailchimp/)
- [Stripe + Quickbooks](https://stackcostmatrix.com/stack/stripe-and-quickbooks/)
- [Stripe + Slack](https://stackcostmatrix.com/stack/stripe-and-slack/)
- [Stripe + Xero](https://stackcostmatrix.com/stack/stripe-and-xero/)
- [Xero + Activecampaign](https://stackcostmatrix.com/stack/xero-and-activecampaign/)
- [Xero + Airtable](https://stackcostmatrix.com/stack/xero-and-airtable/)
- [Xero + Asana](https://stackcostmatrix.com/stack/xero-and-asana/)
- [Xero + Calendly](https://stackcostmatrix.com/stack/xero-and-calendly/)
- [Xero + Slack](https://stackcostmatrix.com/stack/xero-and-slack/)
- [Xero + Zendesk](https://stackcostmatrix.com/stack/xero-and-zendesk/)
- [Zendesk + Airtable](https://stackcostmatrix.com/stack/zendesk-and-airtable/)
- [Zendesk + Asana](https://stackcostmatrix.com/stack/zendesk-and-asana/)
- [Zendesk + Notion](https://stackcostmatrix.com/stack/zendesk-and-notion/)
- [Zendesk + Stripe](https://stackcostmatrix.com/stack/zendesk-and-stripe/)

### Site pages
- [Stackcostmatrix.Com](https://stackcostmatrix.com/)
- [About](https://stackcostmatrix.com/about/)
- [Privacy](https://stackcostmatrix.com/privacy/)
- [Terms](https://stackcostmatrix.com/terms/)
