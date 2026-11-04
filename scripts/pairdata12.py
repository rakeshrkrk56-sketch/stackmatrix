# 2026-11-03 Top-10 pages by Search Console impressions: integration-intent rework.
# 86% of impressions were "<A> <B> integration" queries, 4% cost queries. These pages get a direct answer, setup
# steps and the "How it works" section moved under the headline. Every step is from the vendor page listed in sources.

SLACK_FREE = ("Slack: Free plan limits", "https://slack.com/help/articles/27204752526611-Feature-limitations-on-the-free-version-of-Slack")
TOP12 = {
 "monday-and-slack": dict(
   answer="Yes. monday.com has its own Slack integration: it notifies Slack channels about board activity, such as new tasks, status changes, finished projects and due-date changes, and lets your team mention @monday in Slack to check status or create tasks.",
   how="Board events go out to the Slack channels you choose as they happen, and from Slack you can ask @monday about project status or create a task, so updates move both ways without anyone switching apps.",
   setup=["Open monday.com's Slack integration page and click Add to Slack.", "Authorize monday.com in your Slack workspace.", "Choose which monday.com board updates should notify which Slack channels."],
   limits="monday.com includes integrations from its Standard plan, with 250 integration actions a month (Pro raises this to 25,000), so the Basic plan doesn't include it. Slack's free plan allows up to 10 app installations.",
   sources=[("monday.com: Slack integration", "https://monday.com/integrations/slack"), ("monday.com: Automations and integrations pricing", "https://support.monday.com/hc/en-us/articles/360002826680"), SLACK_FREE],
   summary="monday.com's own Slack integration posts board updates such as new tasks, status changes and due dates to Slack channels; monday.com integrations start on its Standard plan, and Slack's free plan is enough. Requires Monday.com on the 'Standard' plan and Slack on the 'Free' plan."),
 "slack-and-zendesk": dict(
   answer="Yes. Zendesk builds the Slack for Zendesk Support integration: it sends ticket notifications to Slack channels and lets your team create tickets, handle approval requests and use side conversations from Slack.",
   setup=["Make sure you have admin rights in Zendesk and permission to install apps in the Slack workspace.", "In Zendesk Admin Center, click Apps and integrations, then Integrations > Integrations.", "Click the options menu next to Slack, click View, then Connect workspace.", "Pick the Slack workspace, click Allow, then click Set up in Zendesk Admin Center and use triggers to choose which ticket events notify which channels."]),
 "hubspot-and-zendesk": dict(
   answer="Yes. Zendesk's HubSpot integration shows Zendesk tickets, including the conversation, status and CSAT rating, on HubSpot contact timelines, and it works with every HubSpot subscription.",
   setup=["Go to hubspot.zendesk-integrations.com/zendesk and enter your Zendesk subdomain.", "Authorize the Zendesk app, then allow access to HubSpot.", "In HubSpot, open any contact, go to the Activities tab, click Filter activity and tick Integrations > Zendesk.", "Zendesk creates three triggers (ticket created, solved and CSAT rated) that send tickets to HubSpot; edit their conditions to control which tickets sync."]),
 "hubspot-and-mailchimp": dict(
   answer="Yes. HubSpot's built-in Mailchimp integration, on every HubSpot plan, sends contacts from non-HubSpot forms to a Mailchimp list and shows Mailchimp email activity such as sends, opens and clicks on HubSpot contact records.",
   setup=["Make sure you have App Marketplace access in HubSpot.", "In HubSpot, click the Marketplace icon, open HubSpot Marketplace and search for Mailchimp.", "Install it, log in to Mailchimp and click Allow.", "To sync a form, go to Marketing > Forms, hover over a non-HubSpot form, click Actions > Edit Mailchimp lists and choose a list.", "To log email activity, go to Settings > Integrations > Email service provider and turn the Mailchimp sync on; HubSpot then syncs events every 15 minutes."]),
 "pipedrive-and-slack": dict(
   answer="Yes, through Pipedrive's Automations: an automation can post to a Slack channel or send a direct message when something happens in Pipedrive, such as a new or won deal. Automations need Pipedrive Growth or higher.",
   setup=["In Pipedrive, go to Tools and apps > Slack > Authorize Slack account.", "Create an automation, pick a trigger such as a deal being won, and add a Slack notification action.", "Choose a channel or a direct message, then pick the Pipedrive fields to include in the message."]),
 "pipedrive-and-mailchimp": dict(
   answer="Yes. Pipedrive's own Mailchimp sync app syncs contacts both ways: Pipedrive filters can push contacts into a Mailchimp audience, and Mailchimp segments or tags can bring contacts into Pipedrive.",
   how="Pipedrive's Mailchimp sync works through flows. Each flow has its own trigger and field mapping: one kind keeps Pipedrive contacts that match your filters updated in a Mailchimp audience, the other brings Mailchimp contacts that match chosen segments or tags into Pipedrive.",
   setup=["In Pipedrive, go to Tools and apps > Integrations > Mailchimp sync and click Get started.", "Click Connect Mailchimp, log in and click Allow.", "Create a sync flow: pick a trigger, map the fields, click Save and turn the flow on."],
   limits="Flows run on a schedule, so new matches can take a while to appear; the first sync starts within ten minutes of turning a flow on. If a contact stops matching a Mailchimp segment or tag, it stays in Pipedrive but stops updating. Each field can be mapped only once per flow, and the number of Mailchimp audiences you can create depends on your Mailchimp plan.",
   sources=[("Pipedrive: Mailchimp sync", "https://support.pipedrive.com/en/article/pipedrive-integration-mailchimp-sync")]),
 "hubspot-and-slack": dict(
   answer="Yes. The HubSpot app for Slack works on every HubSpot plan, including the free CRM: it sends HubSpot notifications to Slack and lets your team turn Slack messages into HubSpot tasks, tickets or notes.",
   setup=["Make sure you're a Super Admin (or have App Marketplace permissions) in HubSpot and an admin of the Slack workspace.", "In HubSpot, click the Marketplace icon, open HubSpot Marketplace, search for Slack and click Install.", "Review the requested permissions in Slack and allow access.", "In Slack, the HubSpot app sends you a message: click Verify to map your HubSpot user to your Slack user."]),
 "activecampaign-and-calendly": dict(
   answer="Yes. ActiveCampaign builds and manages a Calendly integration that adds people who book a Calendly meeting to ActiveCampaign as contacts, with their event details. It needs a paid Calendly plan.",
   how="When someone books a Calendly meeting, the integration creates or updates the contact in ActiveCampaign with the event information, so you can start automations from it. Data flows one way, from Calendly into ActiveCampaign, and past bookings aren't synced.",
   setup=["In ActiveCampaign, click your profile icon at the bottom left and select Apps.", "Select Calendly, then Add an account and Connect.", "Under Choose an Event, pick the Calendly event type to sync and click Continue.", "Map Calendly fields to ActiveCampaign fields and click Finish."],
   limits="Calendly lists the integration for its Professional, Standard, Standard Plus, Teams, Teams Plus and Enterprise plans, so Calendly's free plan doesn't include it. Each connection syncs the event type you choose during setup.",
   sources=[("Calendly: ActiveCampaign integration", "https://calendly.com/help/calendly-activecampaign"), ("ActiveCampaign: Integrate Calendly", "https://help.activecampaign.com/hc/en-us/articles/360010946759")]),
 "pipedrive-and-calendly": dict(
   answer="Not natively. Pipedrive and Calendly don't build an integration with each other, but third-party apps such as Outfunnel's Calendly Sync, or Make and Zapier, add Calendly bookings to Pipedrive.",
   setup=["Pick a connector: a Pipedrive Marketplace app such as Outfunnel's Calendly Sync, or Make or Zapier.", "Connect your Calendly account (Standard plan or higher) and your Pipedrive account in that connector.", "Choose what a new booking should create in Pipedrive, such as a new person record."]),
 "intercom-and-hubspot": dict(
   answer="Yes. Intercom's HubSpot app, available on Intercom's Essential, Advanced and Expert plans, sends leads from Intercom to HubSpot as contacts and logs their conversations on the HubSpot timeline.",
   setup=["Make sure you have admin access in HubSpot.", "In Intercom, open the App Store, find HubSpot and click Install now.", "Connect your HubSpot account when prompted.", "In App Store > HubSpot > Settings, choose how leads and their conversations are sent to HubSpot."]),
}
