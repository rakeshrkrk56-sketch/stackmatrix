# Salesforce API Access by Edition (2026): Professional, Enterprise & Unlimited

> Which Salesforce plans include API access and webhooks in 2026, with rate limits and the vendor source for each plan, checked Nov 10, 2026.

Source page: https://stackcostmatrix.com/salesforce-api-access/  
Publisher: StackCostMatrix · Editor: Rakesh Kumar · Data licence: CC BY 4.0 (credit StackCostMatrix and link to https://stackcostmatrix.com)

---

Checked against Salesforce's developer and help-center documentation · Nov 10, 2026 · Edited by [Rakesh Kumar](https://stackcostmatrix.com/about/#editor)

## Which Salesforce plans include API access and webhooks?

**Short answer:** Salesforce API access is included in Enterprise and Unlimited; Professional only gets it with a paid API add-on (modeled at $25 per user a month), and Starter doesn't support the API. With API access, an org gets 100,000 API calls per 24 hours plus 1,000 per Salesforce license (Enterprise, or Professional with API access) or 5,000 per license (Unlimited). Change Data Capture, Salesforce's real-time change feed, is on Enterprise and Unlimited only.

Which Salesforce plans include API access and webhooks?

| Plan | Price | API access | API limit | Webhooks | Webhook automation action |
| --- | --- | --- | --- | --- | --- |
| Starter | $25/seat/mo | No | N/A (no API access) | No | — |
| Professional | $100/seat/mo | Add-on API add-on, sold through a Salesforce account executive (modeled here at $25/user) | 100,000 + 1,000 per Salesforce license / 24 h (with API access) | No Change Data Capture isn't available on Professional | — |
| Enterprise | $165/seat/mo | Yes | 100,000 + 1,000 per Salesforce license / 24 h | Yes Change Data Capture (change events) | — |
| Unlimited | $330/seat/mo | Yes | 100,000 + 5,000 per Salesforce license / 24 h | Yes Change Data Capture (change events) | — |

Salesforce publishes annual-billing rates only, so prices are per month, billed annually.

Each user also needs the "API Enabled" permission; without org API access Salesforce returns API\_DISABLED\_FOR\_ORG. Limits apply to the whole org, not per user, and you can buy extra API calls. For 10 Salesforce licenses that's 110,000 calls a day on Enterprise and 150,000 on Unlimited.

Chart: Salesforce plans: monthly price for 10 seats and whether the API is included: Starter (no API) $250.00; Professional (API as a paid add-on) $1,250.00; Enterprise (API included) $1,650.00; Unlimited (API included) $3,300.00

Salesforce monthly price for 10 seats by plan. Green: API included; amber: paid add-on (included in the bar); grey: no API.

 

Image: [Salesforce API access by plan: Starter no; Professional add-on; Enterprise yes; Unlimited yes](https://stackcostmatrix.com/og/salesforce-api-access.jpg)

## How to get API access on Salesforce Professional

Professional doesn't include the API. Salesforce's developer docs say "Professional Edition orgs can add API access as an add-on", bought through the Your Account app or a Salesforce account executive. This site models the add-on at $25 per user a month; ask Salesforce for your own price.

1. Ask your Salesforce account executive (or use the Your Account app) to add API access to your Professional org.
2. Give each user who will connect an integration the "API Enabled" permission on their profile. Salesforce says a user must have it to make any API call.
3. Connect your integration. If the org doesn't have API access, Salesforce returns the error API\_DISABLED\_FOR\_ORG.

Some AppExchange apps work on Professional without the add-on. Salesforce's packaging guide says that after a partner app passes its security review, the app "can make calls to Group and Professional Edition orgs ... even if the customer doesn't have API access". That covers the standard SOAP and REST data APIs; Bulk API 2.0 and Data Loader stay unavailable. So before you buy the add-on for one connector, ask that connector's vendor whether it needs it.

## What is the difference between developer webhooks and workflow webhooks?

Vendors use "webhooks" for two different features. **Developer webhooks** let an app or a tool like Make or Zapier subscribe to events, and are usually available wherever the API is. A **webhook automation action** is a no-code step that sends data out from the tool's own automations, and is often limited to paid plans. The table lists them separately so you can see which one an integration actually needs.

## Which Salesforce plan do the integrations here need?

**Professional** (10): [Asana + Salesforce](https://stackcostmatrix.com/stack/asana-and-salesforce/), [HubSpot + Salesforce](https://stackcostmatrix.com/stack/hubspot-and-salesforce/), [Intercom + Salesforce](https://stackcostmatrix.com/stack/intercom-and-salesforce/), [Pipedrive + Salesforce](https://stackcostmatrix.com/stack/pipedrive-and-salesforce/), [Salesforce + Airtable](https://stackcostmatrix.com/stack/salesforce-and-airtable/), [Salesforce + Mailchimp](https://stackcostmatrix.com/stack/salesforce-and-mailchimp/), [Salesforce + QuickBooks](https://stackcostmatrix.com/stack/salesforce-and-quickbooks/), [Salesforce + Stripe](https://stackcostmatrix.com/stack/salesforce-and-stripe/), [Salesforce + Xero](https://stackcostmatrix.com/stack/salesforce-and-xero/), [Salesforce + Zendesk](https://stackcostmatrix.com/stack/salesforce-and-zendesk/)  
**Enterprise** (2): [Salesforce + Calendly](https://stackcostmatrix.com/stack/salesforce-and-calendly/), [Salesforce + Slack](https://stackcostmatrix.com/stack/salesforce-and-slack/)

Full costs, including the other tool's plan and any connector fee: [Salesforce integration costs →](https://stackcostmatrix.com/salesforce-integrations-cost/)

## Sources

Checked Nov 10, 2026.

- [Salesforce developers: Supported editions ↗](https://developer.salesforce.com/docs/platform/api-rest/guide/intro-rest-compatible-editions.html) “API access is enabled by default in Enterprise, Performance, Unlimited, and Developer Edition orgs … Professional Edition orgs can add API access as an add-on”
- [Salesforce developers: API request limits and allocations ↗](https://developer.salesforce.com/docs/atlas.en-us.salesforce_app_limits_cheatsheet.meta/salesforce_app_limits_cheatsheet/salesforce_app_limits_platform_api.htm) “Enterprise Edition, Professional Edition with API access enabled … Salesforce: 1,000 … 100,000 + (number of licenses x calls per license type) + purchased API Call Add-Ons”
- [Salesforce developers: API access in Group and Professional Editions ↗](https://developer.salesforce.com/docs/atlas.en-us.packagingGuide.meta/packagingGuide/dev_packages_api_access.htm) “after your app passes the security review … your app can make calls to Group and Professional Edition orgs … even if the customer doesn't have API access”
- [Salesforce developers: Change Data Capture ↗](https://developer.salesforce.com/docs/atlas.en-us.change_data_capture.meta/change_data_capture/cdc_intro.htm) “Available in: Enterprise, Performance, Unlimited, and Developer editions”

## API access by plan for other tools

[ActiveCampaign](https://stackcostmatrix.com/activecampaign-api-access/) · [Airtable](https://stackcostmatrix.com/airtable-api-access/) · [Asana](https://stackcostmatrix.com/asana-api-access/) · [Calendly](https://stackcostmatrix.com/calendly-api-access/) · [ClickUp](https://stackcostmatrix.com/clickup-api-access/) · [Freshdesk](https://stackcostmatrix.com/freshdesk-api-access/) · [HubSpot](https://stackcostmatrix.com/hubspot-api-access/) · [Intercom](https://stackcostmatrix.com/intercom-api-access/) · [Mailchimp](https://stackcostmatrix.com/mailchimp-api-access/) · [Monday.com](https://stackcostmatrix.com/monday-api-access/) · [Notion](https://stackcostmatrix.com/notion-api-access/) · [Pipedrive](https://stackcostmatrix.com/pipedrive-api-access/) · [QuickBooks](https://stackcostmatrix.com/quickbooks-api-access/) · [Slack](https://stackcostmatrix.com/slack-api-access/) · [Stripe](https://stackcostmatrix.com/stripe-api-access/) · [Xero](https://stackcostmatrix.com/xero-api-access/) · [Zendesk](https://stackcostmatrix.com/zendesk-api-access/)

## Salesforce API access: frequently asked questions

### Does Salesforce Starter include API access?

No. Salesforce Starter doesn't support the API at all. API access starts with Professional plus the paid API add-on, and is included from Enterprise up.

### Which Salesforce plans include webhooks?

Salesforce's change-event feed, Change Data Capture, is available on Enterprise and Unlimited (and on Performance and Developer editions), not on Starter or Professional. On Professional, an integration reads changes through the REST API instead, which needs the API add-on.

### What are Salesforce's API rate limits by plan?

Professional: 100,000 + 1,000 per Salesforce license / 24 h (with API access); Enterprise: 100,000 + 1,000 per Salesforce license / 24 h; Unlimited: 100,000 + 5,000 per Salesforce license / 24 h. Each user also needs the "API Enabled" permission; without org API access Salesforce returns API\_DISABLED\_FOR\_ORG. Limits apply to the whole org, not per user, and you can buy extra API calls. For 10 Salesforce licenses that's 110,000 calls a day on Enterprise and 150,000 on Unlimited.

### Does Salesforce Professional have API access?

Only if you buy the API add-on. Salesforce's developer docs say API access is enabled by default in Enterprise, Performance, Unlimited and Developer Edition orgs, and that Professional Edition orgs can add API access as an add-on; this site models it at $25 per user a month. Once the org has API access, each user who connects an integration also needs the API Enabled permission on their profile or permission set.

### How many API calls does Salesforce allow per day?

API limits apply to the whole org per 24 hours: 100,000 calls plus 1,000 per Salesforce license on Enterprise (and on Professional with API access), or plus 5,000 per license on Unlimited, plus any API calls you buy. A 10-license org gets 110,000 calls a day on Enterprise and 150,000 on Unlimited.
