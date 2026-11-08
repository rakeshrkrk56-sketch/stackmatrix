# 2026-11-08: plugin-audit round. Re-read each vendor's page today.
# Corrections:
#  - activecampaign-and-stripe: ActiveCampaign's own app directory (activecampaign.com/apps/stripe) lists the Stripe
#    integration as "INCLUDED WITH Enterprise, Plus, Professional" -> Plus. The earlier "all plans" quote came from the
#    Active Intelligence Stripe connector article, not the data-sync integration. Data flows Stripe -> ActiveCampaign.
#  - mailchimp-and-calendly: Calendly's help article (updated Aug 24, 2026) needs "A Calendly paid account with admin
#    access" and "A Mailchimp account (free or paid)" -> Mailchimp Free. Data flows Calendly -> Mailchimp only.
#  - pipedrive-and-xero: Pipedrive's own Xero KB article now returns "doesn't exist"; the Marketplace's Xero app is by
#    Cloudify ApS (third party, "Start free with 30 syncs", price not listed) -> modeled as Make Core middleware.
# COPY16: "How it works" for the 15 pairs that had none (from the audit), each with the vendor sources read today.
CHECKED16 = "Nov 8, 2026"
ROUND16_DATE = "2026-11-08"

PAIRS16 = {
 "activecampaign-and-stripe": dict(native=True, req={"activecampaign": "Plus"}, sync="1-way (Stripe → ActiveCampaign)",
   summary="ActiveCampaign's own Stripe integration copies Stripe customers, orders and subscriptions into ActiveCampaign so they can trigger automations; ActiveCampaign's app directory lists it as included with Plus, Professional and Enterprise. Requires ActiveCampaign on the 'Plus' plan and Stripe on the 'Standard' plan."),
 "mailchimp-and-calendly": dict(native=True, req={"mailchimp": "Free", "calendly": "Standard"}, sync="1-way (Calendly → Mailchimp)",
   summary="Calendly's Mailchimp integration adds invitees to a Mailchimp audience, with tags, when they book; it needs a paid Calendly plan, and any Mailchimp account works, including Free. Requires Mailchimp on the 'Free' plan and Calendly on the 'Standard' plan."),
 "pipedrive-and-xero": dict(native=False, req={"pipedrive": "Lite", "xero": "Early"}, sync="1-way (trigger → action)",
   summary="Pipedrive's own Xero integration is no longer available; the Xero app in Pipedrive's Marketplace is a paid third-party app (Cloudify, free for the first 30 syncs), so this models Make Core turning won deals into Xero invoices. Requires Pipedrive on the 'Lite' plan and Xero on the 'Early' plan. Route it through Make Core ($10.59/mo, or $9/mo billed annually)."),
}
MW16 = {"pipedrive-and-xero": (10.59, 9)}

STRIPE_WH = ("Stripe docs: Webhooks", "https://docs.stripe.com/webhooks")
COPY16 = {
 "activecampaign-and-stripe": dict(
   how="You connect Stripe from ActiveCampaign's apps page and choose which Stripe resource to sync. Customers, orders and subscriptions from Stripe arrive in ActiveCampaign as contacts and e-commerce data, tagged by the Stripe event, and Stripe-based automation triggers become available, for example a welcome series for new subscribers or a win-back for a failed payment.",
   limits="Data flows from Stripe into ActiveCampaign, not back. The integration doesn't add contacts to a list on its own (use an automation for that), and it can only map Stripe fields to fields that already exist in ActiveCampaign.",
   sources=[("ActiveCampaign: Stripe integration (app directory)", "https://www.activecampaign.com/apps/stripe"),
            ("ActiveCampaign help: Connect your Stripe account", "https://help.activecampaign.com/hc/en-us/articles/360016037040")]),
 "asana-and-mailchimp": dict(
   how="There's no native Asana–Mailchimp app, so a Zapier Zap links them. Common Zaps create an Asana task for each new Mailchimp subscriber or unsubscriber, or add or update a Mailchimp subscriber when a task is created or tagged in an Asana project.",
   limits="Each run is one-way, from the trigger app to the action app, and every run counts toward your Zapier task allowance.",
   sources=[("Zapier: Asana + Mailchimp integrations", "https://zapier.com/apps/asana/integrations/mailchimp"),
            ("Asana developers: Webhooks", "https://developers.asana.com/docs/webhooks-guide")]),
 "asana-and-quickbooks": dict(
   how="There's no native link, so a Make scenario connects them through both APIs. Typical uses are creating a QuickBooks invoice when an Asana task reaches a 'Ready to bill' section, or creating an Asana task when a QuickBooks invoice becomes overdue. Asana's webhooks let Make react to task changes as they happen.",
   limits="Sync is one-way per scenario, and you build and maintain the field mapping yourself. Make counts every run against your plan's monthly credits.",
   sources=[("Asana developers: Webhooks", "https://developers.asana.com/docs/webhooks-guide"),
            ("Intuit developers: QuickBooks Online API", "https://developer.intuit.com/app/developer/qbo/docs/get-started")]),
 "asana-and-slack": dict(
   how="Install the Asana app for Slack, then type /asana in Slack to list, create, complete or comment on tasks. You can turn any Slack message into an Asana task with a few clicks, link a Slack channel to an Asana project to get updates when tasks are created or completed, and use Asana rules to post a message to a Slack channel when something happens in Asana.",
   limits="Updates flow both ways but it isn't a full sync: Slack conversations aren't mirrored into Asana, only the message you turn into a task. Slack's free plan allows up to 10 app installations.",
   sources=[("Asana: Slack + Asana", "https://asana.com/apps/slack"),
            ("Asana help: Slack and Asana", "https://help.asana.com/s/article/slack-and-asana")]),
 "clickup-and-stripe": dict(
   how="There's no native link, so a Make scenario listens for Stripe events, such as a successful payment or a new subscription, and creates or updates a ClickUp task through ClickUp's API, for example an onboarding task for each new customer.",
   limits="It's one-way (Stripe → ClickUp). Stripe sends events through webhooks, so failed deliveries are retried by Stripe, but the mapping and any duplicate checks are yours to build.",
   sources=[STRIPE_WH, ("ClickUp API: Create task", "https://developer.clickup.com/reference/createtask")]),
 "clickup-and-zendesk": dict(
   how="Install the ClickUp app from the Zendesk Marketplace, open a ticket and launch ClickUp from the apps panel. From there you can create a ClickUp task from the ticket (with its details, assignees and due date) or link the ticket to an existing task; each task keeps a link back to the ticket, and the task's status shows inside Zendesk.",
   limits="Only Workspace owners and admins can install it. Keeping every ticket update in sync both ways needs ClickUp's separate Zendesk Sync, which is on Business Plus and Enterprise.",
   sources=[("ClickUp help: Zendesk integration", "https://help.clickup.com/hc/en-us/articles/6304890522135-Zendesk-integration"),
            ("ClickUp: Zendesk integration", "https://clickup.com/integrations/zendesk")]),
 "intercom-and-stripe": dict(
   how="Install Stripe from the Intercom App Store and turn on sync. Intercom imports each customer's Stripe data, such as plan, interval, account balance and delinquency, as custom attributes, so you can segment and message customers by billing status. Agents can see Stripe details in the inbox and add or link a customer to Stripe without leaving Intercom.",
   limits="Customers are matched by email address. Only live-mode Stripe data syncs, not test mode, and extra Stripe accounts sync attributes only, not the inbox app. You need to be a Stripe admin to connect it.",
   sources=[("Intercom help: Stripe app", "https://www.intercom.com/help/en/articles/1829591-stripe-app")]),
 "mailchimp-and-calendly": dict(
   how="In Calendly, go to Integrations & apps, connect Mailchimp, then create a rule per event type: pick the Mailchimp audience to add invitees to and, optionally, tags. When someone books, Calendly adds them to that audience and sends booked, canceled and rescheduled events to the contact's activity feed, which you can use to target campaigns or trigger automated emails.",
   limits="Data flows from Calendly to Mailchimp only. Invitees in GDPR regions are added as non-marketing contacts unless they opt in, and disconnecting Mailchimp deletes the rules you set up.",
   sources=[("Calendly help: Calendly + Mailchimp", "https://calendly.com/help/calendly-mailchimp")]),
 "monday-and-quickbooks": dict(
   how="There's no native link, so a Make scenario connects monday.com and QuickBooks through their APIs, for example creating a QuickBooks invoice when a monday.com item moves to 'Done', or adding a payment status column update when an invoice is paid.",
   limits="Sync is one-way per scenario. monday.com's Standard plan includes 250 integration actions a month (Pro raises this to 25,000), and Make counts each run against its own monthly credits.",
   sources=[("monday.com developers: API reference", "https://developer.monday.com/api-reference/docs"),
            ("Intuit developers: QuickBooks Online API", "https://developer.intuit.com/app/developer/qbo/docs/get-started")]),
 "notion-and-stripe": dict(
   how="There's no native link, so a Make scenario receives Stripe events, such as a successful payment, and creates a page in a Notion database for each one through Notion's API, giving you a payments log or customer list inside Notion.",
   limits="It's one-way (Stripe → Notion). The Notion integration must be shared with the database it writes to, and you maintain the property mapping yourself.",
   sources=[STRIPE_WH, ("Notion API: Create a page", "https://developers.notion.com/reference/post-page")]),
 "pipedrive-and-xero": dict(
   how="Pipedrive's own Xero integration is no longer offered. The Xero app in Pipedrive's Marketplace is built by Cloudify: it creates Xero invoices or quotes when a deal reaches a pipeline stage you choose and shows the invoice status (draft, awaiting payment or paid) on the deal. This page models the cheaper connector route, a Make scenario that creates a Xero invoice for each won deal.",
   limits="Cloudify's app is free for the first 30 syncs and paid after that (its price isn't listed in the Marketplace). The Make route is one-way and you build the field mapping yourself.",
   sources=[("Pipedrive Marketplace: Xero (by Cloudify)", "https://www.pipedrive.com/en/marketplace/app/xero/b217602d14d86f39"),
            ("Xero developers", "https://developer.xero.com/")]),
 "slack-and-airtable": dict(
   how="In an Airtable base, open the base menu and choose Slack notifications, then create rules that post to a Slack channel when the base changes, or when specific records or views change. You can make as many rules as you need, so different bases can notify different channels.",
   limits="It's one-way (Airtable → Slack) and only posts notifications. Your organization's admins can block the integration, and only the person who set up a rule can turn it off.",
   sources=[("Airtable support: Base activity notifications in Slack", "https://support.airtable.com/docs/receiving-base-activity-notifications-in-slack")]),
 "slack-and-calendly": dict(
   how="Install the Calendly app from the Slack App Directory and connect your Calendly account. You can share your scheduling links in channels and DMs with meeting previews, and the app messages you in Slack whenever a meeting is scheduled, rescheduled or cancelled.",
   limits="Each person connects their own Calendly account after a workspace admin installs the app, and your company can block app installation. Notifications arrive in the Calendly app's Messages tab, not in a channel.",
   sources=[("Calendly help: Calendly + Slack", "https://calendly.com/help/calendly-slack")]),
 "zendesk-and-notion": dict(
   how="There's no native link, so a Zapier Zap connects them. Common Zaps create a Notion database item or page for each new Zendesk ticket (or each ticket in a view), or add a Zendesk ticket comment when a Notion database item is added.",
   limits="Each Zap is one-way, and every run counts toward your Zapier task allowance. The Notion integration must be shared with the database it writes to.",
   sources=[("Zapier: Notion + Zendesk integrations", "https://zapier.com/apps/notion/integrations/zendesk"),
            ("Zendesk developers: Webhooks", "https://developer.zendesk.com/documentation/webhooks/")]),
 "zendesk-and-stripe": dict(
   how="There's no native link, so a Make scenario receives Stripe events, such as a failed payment or a dispute, and creates or updates a Zendesk ticket for the customer, so support sees billing problems as they happen.",
   limits="It's one-way (Stripe → Zendesk). Zendesk's webhooks and triggers are on every Suite plan from Team up, but you build the ticket mapping and duplicate checks yourself.",
   sources=[STRIPE_WH, ("Zendesk developers: Webhooks", "https://developer.zendesk.com/documentation/webhooks/")]),
}
for _c in COPY16.values(): _c["checked"] = CHECKED16
