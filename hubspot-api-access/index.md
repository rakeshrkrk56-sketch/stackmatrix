# HubSpot API & Webhook Access by Plan (2026)

> Which HubSpot plans include API access and webhooks in 2026, with rate limits and the vendor source for each plan, checked Nov 3, 2026.

Source page: https://stackcostmatrix.com/hubspot-api-access/  
Publisher: StackCostMatrix · Editor: Rakesh Kumar · Data licence: CC BY 4.0 (credit StackCostMatrix and link to https://stackcostmatrix.com)

---

Checked against HubSpot's developer and help-center documentation · Nov 3, 2026 · Edited by [Rakesh Kumar](https://stackcostmatrix.com/about/#editor)

## Which HubSpot plans include API access and webhooks?

**Short answer:** HubSpot's API is available on every plan, including the free CRM, with higher limits on Professional and Enterprise. Webhook actions in workflows need Data Hub Professional or Enterprise.

Which HubSpot plans include API access and webhooks?

| Plan | Price | API access | API limit | Webhooks | Webhook automation action |
| --- | --- | --- | --- | --- | --- |
| Free | Free | Yes | 100 req/10 s · 250,000/day (private apps) | Not stated Developer webhooks via apps; plan not stated | Needs Data Hub Professional |
| Starter | $20/seat/mo | Yes | 100 req/10 s · 250,000/day (private apps) | Not stated Developer webhooks via apps; plan not stated | Needs Data Hub Professional |
| Professional | $50/seat/mo ($45 billed annually) | Yes | 190 req/10 s · 625,000/day (private apps) | Not stated Developer webhooks via apps; plan not stated | Only with Data Hub Professional |
| Enterprise | $75/seat/mo | Yes | 190 req/10 s · 1,000,000/day (private apps) | Not stated Developer webhooks via apps; plan not stated | Only with Data Hub Enterprise |

"Not stated" means HubSpot's documentation that we read doesn't say either way. Prices are monthly-billing list prices from this site's calculators.

Limits depend on the subscription of the account an app is installed in; an API limit increase add-on adds capacity. Apps can also receive events through HubSpot's developer webhooks API, which isn't covered by the workflow requirement.

Chart: HubSpot plans: monthly price for 10 seats and whether the API is included: Free (API included) $0.00; Starter (API included) $200.00; Professional (API included) $500.00; Enterprise (API included) $750.00

HubSpot monthly price for 10 seats by plan. Green: API included; amber: paid add-on (included in the bar); grey: no API.

 

Image: [HubSpot API access by plan: Free yes; Starter yes; Professional yes; Enterprise yes](https://stackcostmatrix.com/og/hubspot-api-access.jpg)

## What is the difference between developer webhooks and workflow webhooks?

Vendors use "webhooks" for two different features. **Developer webhooks** let an app or a tool like Make or Zapier subscribe to events, and are usually available wherever the API is. A **webhook automation action** is a no-code step that sends data out from the tool's own automations, and is often limited to paid plans. The table lists them separately so you can see which one an integration actually needs.

## Which HubSpot plan do the integrations here need?

**Free** (11): [Freshdesk + HubSpot](https://stackcostmatrix.com/stack/freshdesk-and-hubspot/), [HubSpot + Calendly](https://stackcostmatrix.com/stack/hubspot-and-calendly/), [HubSpot + ClickUp](https://stackcostmatrix.com/stack/hubspot-and-clickup/), [HubSpot + Mailchimp](https://stackcostmatrix.com/stack/hubspot-and-mailchimp/), [HubSpot + Monday.com](https://stackcostmatrix.com/stack/hubspot-and-monday/), [HubSpot + Pipedrive](https://stackcostmatrix.com/stack/hubspot-and-pipedrive/), [HubSpot + QuickBooks](https://stackcostmatrix.com/stack/hubspot-and-quickbooks/), [HubSpot + Slack](https://stackcostmatrix.com/stack/hubspot-and-slack/), [HubSpot + Stripe](https://stackcostmatrix.com/stack/hubspot-and-stripe/), [HubSpot + Zendesk](https://stackcostmatrix.com/stack/hubspot-and-zendesk/), [Intercom + HubSpot](https://stackcostmatrix.com/stack/intercom-and-hubspot/)  
**Professional** (2): [HubSpot + Asana](https://stackcostmatrix.com/stack/hubspot-and-asana/), [HubSpot + Salesforce](https://stackcostmatrix.com/stack/hubspot-and-salesforce/)

Full costs, including the other tool's plan and any connector fee: [HubSpot integration costs →](https://stackcostmatrix.com/hubspot-integrations-cost/)

## Sources

Checked Nov 3, 2026.

- [HubSpot developers: Usage guidelines ↗](https://developers.hubspot.com/docs/developer-tooling/platform/usage-guidelines) “The number of calls your app can make is based on your account subscription”
- [HubSpot KB: Webhooks in workflows ↗](https://knowledge.hubspot.com/workflows/how-do-i-use-webhooks-with-hubspot-workflows) “Available with any of the following subscriptions, except where noted: Data Hub Professional, Enterprise”

## API access by plan for other tools

[ActiveCampaign](https://stackcostmatrix.com/activecampaign-api-access/) · [Airtable](https://stackcostmatrix.com/airtable-api-access/) · [Asana](https://stackcostmatrix.com/asana-api-access/) · [Calendly](https://stackcostmatrix.com/calendly-api-access/) · [ClickUp](https://stackcostmatrix.com/clickup-api-access/) · [Freshdesk](https://stackcostmatrix.com/freshdesk-api-access/) · [Intercom](https://stackcostmatrix.com/intercom-api-access/) · [Mailchimp](https://stackcostmatrix.com/mailchimp-api-access/) · [Monday.com](https://stackcostmatrix.com/monday-api-access/) · [Notion](https://stackcostmatrix.com/notion-api-access/) · [Pipedrive](https://stackcostmatrix.com/pipedrive-api-access/) · [QuickBooks](https://stackcostmatrix.com/quickbooks-api-access/) · [Salesforce](https://stackcostmatrix.com/salesforce-api-access/) · [Slack](https://stackcostmatrix.com/slack-api-access/) · [Stripe](https://stackcostmatrix.com/stripe-api-access/) · [Xero](https://stackcostmatrix.com/xero-api-access/) · [Zendesk](https://stackcostmatrix.com/zendesk-api-access/)

## HubSpot API access: frequently asked questions

### Does HubSpot Free include API access?

Yes. The limit is 100 req/10 s · 250,000/day (private apps). HubSpot's API is available on every plan, including the free CRM, with higher limits on Professional and Enterprise. Webhook actions in workflows need Data Hub Professional or Enterprise.

### Which HubSpot plans include webhooks?

Webhook actions in workflows need Data Hub Professional or Enterprise; no other Hub unlocks them. Developer webhooks, which apps subscribe to through HubSpot's Webhooks API, are a separate feature, and HubSpot's documentation doesn't tie them to a plan.

### What are HubSpot's API rate limits by plan?

Free: 100 req/10 s · 250,000/day (private apps); Starter: 100 req/10 s · 250,000/day (private apps); Professional: 190 req/10 s · 625,000/day (private apps); Enterprise: 190 req/10 s · 1,000,000/day (private apps). Limits depend on the subscription of the account an app is installed in; an API limit increase add-on adds capacity. Apps can also receive events through HubSpot's developer webhooks API, which isn't covered by the workflow requirement.
