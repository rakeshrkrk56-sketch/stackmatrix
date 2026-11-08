# Salesforce API & Webhook Access by Plan (2026)

> Which Salesforce plans include API access and webhooks in 2026, with rate limits and the vendor source for each plan, checked Nov 8, 2026.

Source page: https://stackcostmatrix.com/salesforce-api-access/  
Publisher: StackCostMatrix · Editor: Rakesh Kumar · Data licence: CC BY 4.0 (credit StackCostMatrix and link to https://stackcostmatrix.com)

---

API & webhooks

# Salesforce API & Webhook Access by Plan (2026)

Checked against Salesforce's developer and help-center documentation · Nov 8, 2026 · Edited by [Rakesh Kumar](https://stackcostmatrix.com/about/#editor)

**Short answer:** Salesforce API access is included in Enterprise and Unlimited; Professional only gets it with a paid API add-on (modeled at $25 per user a month), and Starter doesn't support the API. With API access, an org gets 100,000 API calls per 24 hours plus 1,000 per Salesforce license (Enterprise, or Professional with API access) or 5,000 per license (Unlimited). Change Data Capture, Salesforce's real-time change feed, is on Enterprise and Unlimited only.

| Plan | Price | API access | API limit | Webhooks | Webhook automation action |
| --- | --- | --- | --- | --- | --- |
| Starter | $25/seat/mo | No | Not published per plan | No | — |
| Professional | $100/seat/mo | Add-on Web Services API add-on (modeled at $25/user) | 100,000 + 1,000 per Salesforce license / 24 h (with API access) | No Change Data Capture isn't available on Professional | — |
| Enterprise | $165/seat/mo | Yes | 100,000 + 1,000 per Salesforce license / 24 h | Yes Change Data Capture (change events) | — |
| Unlimited | $330/seat/mo | Yes | 100,000 + 5,000 per Salesforce license / 24 h | Yes Change Data Capture (change events) | — |

"Not stated" means Salesforce's documentation that we read doesn't say either way. Prices are monthly-billing list prices from this site's calculators.

Each user also needs the "API Enabled" permission; without org API access Salesforce returns API\_DISABLED\_FOR\_ORG. Limits apply to the whole org, not per user, and you can buy extra API calls. For 10 Salesforce licenses that's 110,000 calls a day on Enterprise and 150,000 on Unlimited.

## Two kinds of webhooks

Vendors use "webhooks" for two different features. **Developer webhooks** let an app or a tool like Make or Zapier subscribe to events, and are usually available wherever the API is. A **webhook automation action** is a no-code step that sends data out from the tool's own automations, and is often limited to paid plans. The table lists them separately so you can see which one an integration actually needs.

## Which Salesforce plan the integrations here need

**Professional** (6): [HubSpot + Salesforce](https://stackcostmatrix.com/stack/hubspot-and-salesforce/), [Pipedrive + Salesforce](https://stackcostmatrix.com/stack/pipedrive-and-salesforce/), [Salesforce + Mailchimp](https://stackcostmatrix.com/stack/salesforce-and-mailchimp/), [Salesforce + QuickBooks](https://stackcostmatrix.com/stack/salesforce-and-quickbooks/), [Salesforce + Stripe](https://stackcostmatrix.com/stack/salesforce-and-stripe/), [Salesforce + Zendesk](https://stackcostmatrix.com/stack/salesforce-and-zendesk/)  
**Enterprise** (1): [Salesforce + Slack](https://stackcostmatrix.com/stack/salesforce-and-slack/)

Full costs, including the other tool's plan and any connector fee: [Salesforce integration costs →](https://stackcostmatrix.com/salesforce-integrations-cost/)

## Sources

Checked Nov 8, 2026.

- [Salesforce developers: Supported editions ↗](https://developer.salesforce.com/docs/platform/api-rest/guide/intro-rest-compatible-editions.html) “API access is enabled by default in Enterprise, Performance, Unlimited, and Developer Edition orgs … Professional Edition orgs can add API access as an add-on”
- [Salesforce developers: API request limits and allocations ↗](https://developer.salesforce.com/docs/atlas.en-us.salesforce_app_limits_cheatsheet.meta/salesforce_app_limits_cheatsheet/salesforce_app_limits_platform_api.htm) “Enterprise Edition, Professional Edition with API access enabled … Salesforce: 1,000 … 100,000 + (number of licenses x calls per license type) + purchased API Call Add-Ons”
- [Salesforce developers: Change Data Capture ↗](https://developer.salesforce.com/docs/atlas.en-us.change_data_capture.meta/change_data_capture/cdc_intro.htm) “Available in: Enterprise, Performance, Unlimited, and Developer editions”

## API access by plan for other tools

[ActiveCampaign](https://stackcostmatrix.com/activecampaign-api-access/) · [Airtable](https://stackcostmatrix.com/airtable-api-access/) · [Asana](https://stackcostmatrix.com/asana-api-access/) · [Calendly](https://stackcostmatrix.com/calendly-api-access/) · [ClickUp](https://stackcostmatrix.com/clickup-api-access/) · [Freshdesk](https://stackcostmatrix.com/freshdesk-api-access/) · [HubSpot](https://stackcostmatrix.com/hubspot-api-access/) · [Intercom](https://stackcostmatrix.com/intercom-api-access/) · [Mailchimp](https://stackcostmatrix.com/mailchimp-api-access/) · [Monday.com](https://stackcostmatrix.com/monday-api-access/) · [Notion](https://stackcostmatrix.com/notion-api-access/) · [Pipedrive](https://stackcostmatrix.com/pipedrive-api-access/) · [QuickBooks](https://stackcostmatrix.com/quickbooks-api-access/) · [Slack](https://stackcostmatrix.com/slack-api-access/) · [Stripe](https://stackcostmatrix.com/stripe-api-access/) · [Xero](https://stackcostmatrix.com/xero-api-access/) · [Zendesk](https://stackcostmatrix.com/zendesk-api-access/)

## Frequently asked questions

### Does Salesforce Starter include API access?

No. Salesforce API access is included in Enterprise and Unlimited; Professional only gets it with a paid API add-on (modeled at $25 per user a month), and Starter doesn't support the API. With API access, an org gets 100,000 API calls per 24 hours plus 1,000 per Salesforce license (Enterprise, or Professional with API access) or 5,000 per license (Unlimited). Change Data Capture, Salesforce's real-time change feed, is on Enterprise and Unlimited only.

### Which Salesforce plans include webhooks?

Webhooks are available on Enterprise and Unlimited, but not on Starter and Professional.

### What are Salesforce's API rate limits by plan?

Professional: 100,000 + 1,000 per Salesforce license / 24 h (with API access); Enterprise: 100,000 + 1,000 per Salesforce license / 24 h; Unlimited: 100,000 + 5,000 per Salesforce license / 24 h. Each user also needs the "API Enabled" permission; without org API access Salesforce returns API\_DISABLED\_FOR\_ORG. Limits apply to the whole org, not per user, and you can buy extra API calls. For 10 Salesforce licenses that's 110,000 calls a day on Enterprise and 150,000 on Unlimited.

### Does Salesforce Professional have API access?

Only if you buy the API add-on. Salesforce's developer docs say API access is enabled by default in Enterprise, Performance, Unlimited and Developer Edition orgs, and that Professional Edition orgs can add API access as an add-on; this site models it at $25 per user a month. Once the org has API access, each user who connects an integration also needs the API Enabled permission on their profile or permission set.

### How many API calls does Salesforce allow per day?

API limits apply to the whole org per 24 hours: 100,000 calls plus 1,000 per Salesforce license on Enterprise (and on Professional with API access), or plus 5,000 per license on Unlimited, plus any API calls you buy. A 10-license org gets 110,000 calls a day on Enterprise and 150,000 on Unlimited.
