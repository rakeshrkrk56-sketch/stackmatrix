# Batch 2 of corrections (39-pair verification, Option A, high-confidence items only). Checked 2026-11-03.
SLACK_FREE = ("Slack: Free plan limits", "https://slack.com/help/articles/27204752526611-Feature-limitations-on-the-free-version-of-Slack")

PAIRS2 = {
 # --- Slack pairs: Slack's free plan supports these apps (max 10 app installs) ---
 "asana-and-slack": dict(native=True, req={"slack": "Free"}, sync="2-way",
   summary="Asana's Slack app works for any Slack user, including Slack's free plan (up to 10 app installs). Requires Asana on the 'Starter' plan and Slack on the 'Free' plan."),
 "clickup-and-slack": dict(native=True, req={"clickup": "Free", "slack": "Free"}, sync="2-way",
   summary="ClickUp's Slack integration is on every ClickUp plan, including Free Forever, and works with Slack's free plan. Requires ClickUp on the 'Free' plan and Slack on the 'Free' plan."),
 "freshdesk-and-slack": dict(native=True, req={"slack": "Free"}, sync="2-way",
   summary="Freshdesk lists its Slack integration on Growth and above; Slack's free plan is enough on the Slack side. Requires Freshdesk on the 'Growth' plan and Slack on the 'Free' plan."),
 "monday-and-slack": dict(native=True, req={"slack": "Free"}, sync="2-way",
   summary="monday.com's Slack integration is available on all plans and works with Slack's free plan. Requires Monday.com on the 'Standard' plan and Slack on the 'Free' plan."),
 "pipedrive-and-slack": dict(native=True, req={"pipedrive": "Advanced", "slack": "Free"}, sync="1-way (Pipedrive → Slack)",
   summary="Trap: Pipedrive sends Slack messages through its Automations feature, which is only on Advanced and higher ($34/seat). Requires Pipedrive on the 'Advanced' plan and Slack on the 'Free' plan."),
 "quickbooks-and-slack": dict(native=False, req={"slack": "Free"}, sync="1-way (trigger → action)",
   summary="No official QuickBooks Online app for Slack, so alerts run through Zapier Starter ($19.99/mo); Slack's free plan is enough. Requires QuickBooks Online on the 'Plus' plan and Slack on the 'Free' plan. Route it through Zapier Starter ($19.99/mo)."),
 "slack-and-airtable": dict(native=True, req={"slack": "Free", "airtable": "Free"}, sync="2-way",
   summary="Airtable's Slack features work on all Airtable plan types, including Free, and on Slack's free plan. Requires Slack on the 'Free' plan and Airtable on the 'Free' plan."),
 "slack-and-calendly": dict(native=True, req={"slack": "Free", "calendly": "Free"}, sync="2-way",
   summary="The Calendly app for Slack is available on all Calendly plans, including Free, and works with Slack's free plan. Requires Slack on the 'Free' plan and Calendly on the 'Free' plan."),
 "slack-and-intercom": dict(native=True, req={"slack": "Free"}, sync="2-way",
   summary="Intercom's native Slack integration is on every Intercom plan and works with Slack's free plan, but automatic Slack alerts for new conversations need Intercom Advanced. Requires Slack on the 'Free' plan and Intercom on the 'Essential' plan."),
 "slack-and-notion": dict(native=True, req={"slack": "Free"}, sync="1-way (Notion → Slack)",
   summary="Notion posts Slack notifications from buttons and database automations on paid Notion plans; Slack's free plan is enough. Requires Slack on the 'Free' plan and Notion on the 'Plus' plan."),
 "slack-and-zendesk": dict(native=True, req={"slack": "Free"}, sync="2-way",
   summary="The Slack for Zendesk Support integration works on every Zendesk Suite plan from Team up and with Slack's free plan. Requires Slack on the 'Free' plan and Zendesk on the 'Suite Team' plan."),
 "stripe-and-slack": dict(native=True, req={"slack": "Free"}, sync="1-way (Stripe → Slack)",
   summary="Stripe's own Stripe Workflows for Slack app posts Slack notifications when events happen in Stripe; Slack's free plan is enough. Requires Stripe on the 'Standard' plan and Slack on the 'Free' plan."),
 # --- Stripe pairs ---
 "activecampaign-and-stripe": dict(native=True, req={"activecampaign": "Starter"}, sync="2-way",
   summary="ActiveCampaign says its Stripe connector is available for all ActiveCampaign and Stripe plans, so the Starter plan is enough. Requires ActiveCampaign on the 'Starter' plan and Stripe on the 'Standard' plan."),
 "airtable-and-stripe": dict(native=False, req={"airtable": "Free"}, sync="1-way (trigger → action)",
   summary="Airtable's Stripe integration runs through an iPaaS tool such as Make, not natively, and works from Airtable's free plan. Requires Airtable on the 'Free' plan and Stripe on the 'Standard' plan. Route it through Make Core ($9/mo)."),
 "clickup-and-stripe": dict(native=False, req={"clickup": "Free"}, sync="1-way (trigger → action)",
   summary="No native ClickUp–Stripe link, but ClickUp's API is available on every plan, so Make Core can log Stripe events in ClickUp from the Free Forever plan. Requires ClickUp on the 'Free' plan and Stripe on the 'Standard' plan. Route it through Make Core ($9/mo)."),
 "stripe-and-mailchimp": dict(native=True, req={"mailchimp": "Free"}, sync="1-way (Stripe → Mailchimp)",
   summary="Hidden cost: Mailchimp's Stripe connection is a paid third-party app (Data Mapper for Mailchimp) that works with any Mailchimp plan, including Free; that subscription isn't in the totals. Requires Stripe on the 'Standard' plan and Mailchimp on the 'Free' plan."),
 "stripe-and-xero": dict(native=True, req={"xero": "Starter"}, sync="2-way",
   summary="Xero accepts online invoice payments through Stripe on its cheapest plan; multi-currency needs Xero's top Established plan. Requires Stripe on the 'Standard' plan and Xero on the 'Starter' plan."),
 "zendesk-and-stripe": dict(native=False, req={"zendesk": "Suite Team"}, sync="1-way (trigger → action)",
   summary="Zendesk webhooks are available on every Suite plan from Team up, so Make Core can bridge Stripe payment events without Suite Professional. Requires Zendesk on the 'Suite Team' plan and Stripe on the 'Standard' plan. Route it through Make Core ($9/mo)."),
 # --- QuickBooks / Xero pairs ---
 "airtable-and-quickbooks": dict(native=False, req={"airtable": "Free"}, sync="1-way (trigger → action)",
   summary="Airtable webhooks are available on all plans, including Free, so Make Core can bridge invoices without Airtable Business. Requires Airtable on the 'Free' plan and QuickBooks Online on the 'Plus' plan. Route it through Make Core ($9/mo)."),
 "quickbooks-and-mailchimp": dict(native=True, req={"mailchimp": "Free"}, sync="1-way (QuickBooks → Mailchimp)",
   summary="Mailchimp's own QuickBooks Online integration syncs QuickBooks customers into a Mailchimp audience, one way and with no middleware, and works on Mailchimp's free plan. Requires QuickBooks Online on the 'Plus' plan and Mailchimp on the 'Free' plan."),
 "xero-and-calendly": dict(native=False, req={"calendly": "Standard"}, sync="1-way (trigger → action)",
   summary="Calendly webhooks need a paid plan from Standard up, not Teams, so Zapier Starter can bridge bookings into Xero. Requires Xero on the 'Standard' plan and Calendly on the 'Standard' plan. Route it through Zapier Starter ($19.99/mo)."),
 # --- remaining pairs ---
 "activecampaign-and-pipedrive": dict(native=True, req={"activecampaign": "Starter"}, sync="2-way",
   summary="ActiveCampaign's native Pipedrive integration is included on every ActiveCampaign plan: it imports Pipedrive contacts and can push contacts to Pipedrive from an automation. Requires ActiveCampaign on the 'Starter' plan and Pipedrive on the 'Advanced' plan."),
 "clickup-and-zendesk": dict(native=True, req={"clickup": "Free"}, sync="Linked tasks (2-way sync needs ClickUp Business Plus)",
   summary="ClickUp's basic Zendesk integration (create and link tasks from tickets) is on every ClickUp plan; full two-way Zendesk Sync needs ClickUp Business Plus or Enterprise. Requires ClickUp on the 'Free' plan and Zendesk on the 'Suite Team' plan."),
 "notion-and-calendly": dict(native=False, req={}, sync="1-way (trigger → action)",
   summary="Notion can embed Calendly booking pages, but there's no native sync; logging bookings in Notion needs Make or Zapier, and Calendly webhooks need its Standard plan. Requires Notion on the 'Plus' plan and Calendly on the 'Standard' plan. Route it through Make Core ($9/mo)."),
 # --- wording-only fixes ---
 "pipedrive-and-xero": dict(native=True, req={}, sync="2-way",
   summary="Invoices generate from won deals and their status in Pipedrive follows Xero; multi-currency needs Xero's top Established plan. Requires Pipedrive on the 'Essential' plan and Xero on the 'Starter' plan."),
 "monday-and-zendesk": dict(native=True, req={}, sync="1-way (Zendesk → monday.com)",
   summary="Zendesk tickets become monday.com board items, but only the first comment is pulled and updates don't keep syncing; Zendesk Team or higher is required. Requires Monday.com on the 'Standard' plan and Zendesk on the 'Suite Team' plan."),
 "pipedrive-and-mailchimp": dict(native=True, req={}, sync="2-way",
   summary="Pipedrive's native Mailchimp integration exports Pipedrive contacts to Mailchimp, and Pipedrive's newer Mailchimp sync adds two-way flows. Requires Pipedrive on the 'Essential' plan and Mailchimp on the 'Essentials' plan."),
 "activecampaign-and-calendly": dict(native=True, req={}, sync="1-way (Calendly → ActiveCampaign)",
   summary="Calendly bookings sync contacts and event details into ActiveCampaign one way, and past bookings don't sync; Calendly needs its Standard plan. Requires ActiveCampaign on the 'Starter' plan and Calendly on the 'Standard' plan."),
}

COPY2 = {
 "clickup-and-slack": dict(
   how="ClickUp's Slack integration lets you create tasks from Slack channels or direct messages, add Slack messages as comments on tasks, and sync ClickUp activity from Spaces, Folders and Lists to Slack channels. ClickUp says it's available on every plan.",
   limits="Guests and limited members can't use it. With a Workspace connection, activity can only sync to public Slack channels (a personal connection can also use private ones), and Slack's free plan allows up to 10 app installations.",
   sources=[("ClickUp: Intro to the integration with Slack", "https://help.clickup.com/hc/en-us/articles/6304922742295-Intro-to-the-integration-with-Slack"), SLACK_FREE]),
 "freshdesk-and-slack": dict(
   how="Freshdesk's Slack app posts new-ticket and ticket-update notifications to the Slack channels you map to Freshdesk groups, lets you create tickets from Slack messages, and syncs collaboration threads in Slack back to Freshdesk.",
   limits="Freshdesk lists Slack integration on Growth and above, and the installing admin needs a plan with API access. You can't map multiple Slack channels to one Freshdesk group, and only Freshdesk agents can invite other Slack members to collaborate on a ticket.",
   sources=[("Freshdesk: The latest Slack app", "https://support.freshdesk.com/support/solutions/articles/50000001687-simplifying-collaboration-using-the-latest-slack-app"), ("Freshdesk: Overview of collaboration", "https://support.freshdesk.com/support/solutions/articles/50000006589-overview-of-collaboration")]),
 "pipedrive-and-slack": dict(
   how="Pipedrive connects to Slack through its Automations feature: after you authorize the Slack app, an automation can post to a Slack channel or send a direct message when something happens in Pipedrive, such as a new or won deal.",
   limits="Pipedrive says Automations are only available on Advanced and higher plans, so the cheapest plan can't send Slack messages this way. Slack's free plan allows up to 10 app installations.",
   sources=[("Pipedrive: Automations Slack notifications", "https://support.pipedrive.com/en/article/workflow-automation-slack-notifications"), SLACK_FREE]),
 "slack-and-intercom": dict(
   how="Intercom's native Slack integration lets you connect Slack as a channel in Intercom, so your team can handle conversations and tickets that start in Slack. Intercom says it's available on all of its helpdesk plans.",
   limits="Automatic Slack notifications for new conversations rely on Workflows, which are only on Intercom's Advanced and Expert plans, not Essential. Slack's free plan allows only 10 apps, and the app can't be installed in the primary workspace of a Slack Enterprise Grid account.",
   sources=[("Intercom: Connect your Slack channel", "https://www.intercom.com/help/en/articles/11534476-connect-your-slack-channel"), SLACK_FREE]),
 "slack-and-notion": dict(
   how="In Notion, a button, database button or database automation can send a Slack notification to a channel you choose, so updates to a Notion database can alert your team in Slack.",
   limits="Notion says these Slack automation actions are only available on paid plans. Slack's free plan allows up to 10 app installations.",
   sources=[("Notion: Connect Slack to Notion", "https://www.notion.com/help/slack"), SLACK_FREE]),
 "slack-and-zendesk": dict(
   how="The Slack for Zendesk Support integration connects one Zendesk account to one Slack workspace, and Zendesk side conversations can use Slack once you turn them on for that workspace.",
   limits="It needs a Zendesk Suite plan from Team up. Organization-shared channels on Slack Enterprise Grid aren't supported, and each additional Slack workspace needs its own installation.",
   sources=[("Zendesk: Slack for Zendesk Support", "https://support.zendesk.com/hc/en-us/articles/4408833756698-Understanding-and-installing-the-Slack-for-Zendesk-Support-integration"), SLACK_FREE]),
 "stripe-and-slack": dict(
   how="Stripe Workflows for Slack is built by Stripe: you connect your Slack workspace, invite the Stripe bot to a channel, then add a 'Send Slack notification' action to a Stripe workflow, for example when a customer subscribes.",
   limits="Notifications only go to channels the Stripe bot has been invited to, and Slack's free plan allows up to 10 app installations.",
   sources=[("Stripe: Stripe Workflows for Slack", "https://docs.stripe.com/use-stripe-apps/stripe-workflows-slack"), SLACK_FREE]),
 "stripe-and-mailchimp": dict(
   how="Mailchimp's current Stripe connection installs the Data Mapper for Mailchimp app from the Stripe App Marketplace and syncs Stripe customers into the Mailchimp audience you choose, with the marketing permission you pick.",
   limits="Mailchimp calls it a paid integration: you need a Data Mapper for Mailchimp subscription on top of your Mailchimp plan, and that cost isn't included in the calculator above. Mailchimp lists any Mailchimp Marketing Platform plan as compatible.",
   sources=[("Mailchimp: Connect Mailchimp for Stripe", "https://mailchimp.com/help/connect-disconnect-mailchimp-stripe/"), ("Mailchimp: Stripe integration", "https://mailchimp.com/integrations/stripe/")]),
 "stripe-and-xero": dict(
   how="Stripe is a built-in payment service in Xero: you add Stripe to an invoice template so customers can pay invoices online by card, and Xero can also create payment links.",
   limits="Xero's cheapest plan accepts online invoice payments but limits you to 20 invoices, and using multiple currencies needs the top Established plan. Stripe's processing fees apply and aren't included above.",
   sources=[("Xero: Connect Stripe to Xero", "https://central.xero.com/0/article/Stripe-AU"), ("Xero: US pricing plans", "https://www.xero.com/us/pricing-plans/")]),
 "activecampaign-and-pipedrive": dict(
   how="ActiveCampaign's native Pipedrive integration has two sync options: an inbound sync that imports Pipedrive contacts into ActiveCampaign, and an automation action that creates or updates people in Pipedrive.",
   limits="Both first and last names are required, so contacts missing either won't sync. Only contacts who reach the Pipedrive action in an automation are pushed to Pipedrive. The Pipedrive plan shown is this calculator's assumption; ActiveCampaign doesn't state one.",
   sources=[("ActiveCampaign: Use the Pipedrive integration", "https://help.activecampaign.com/hc/en-us/articles/360013357320-Use-the-ActiveCampaign-Pipedrive-integration")]),
 "monday-and-zendesk": dict(
   how="monday.com's Zendesk integration creates board items from Zendesk tickets, with filters on fields such as ticket type, status and priority, so other teams can track support work on a monday.com board.",
   limits="Only the ticket's initial comment is pulled into the item's updates, and that section doesn't keep syncing. You need to be a Zendesk admin on a Zendesk plan of Team or higher.",
   sources=[("monday.com: Zendesk integration", "https://support.monday.com/hc/en-us/articles/360001938339-Zendesk-Integration")]),
 "notion-and-calendly": dict(
   how="Notion's Calendly integration lets you paste a Calendly booking page link into Notion and embed it, so teammates or clients can book time from a Notion page.",
   limits="Embedding doesn't sync bookings. Logging meetings in a Notion database needs Make or Zapier, and Calendly's webhooks need a paid Calendly plan from Standard up.",
   sources=[("Notion: Calendly integration", "https://www.notion.com/integrations/calendly"), ("Calendly: API overview", "https://calendly.com/help/calendly-api-overview")]),
}
