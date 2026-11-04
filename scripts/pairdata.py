# Corrected pair data (verified 2026-11-03 against vendor docs; see PAIR-RESEARCH-FINDINGS.md)
# and pair-specific copy. Every claim below was checked against the fetched source text.

KB = "https://knowledge.hubspot.com"
MKT = "https://ecosystem.hubspot.com/marketplace/listing"

PAIRS = {
 "hubspot-and-salesforce": dict(native=True, req={"hubspot": "Professional", "salesforce": "Professional"}, sync="2-way",
   summary="Big trap: HubSpot's native Salesforce connector only works on HubSpot Professional or Enterprise ($800/mo) — the free CRM can't use it. Requires HubSpot on the 'Professional' plan and Salesforce Sales Cloud on the 'Professional' plan for full 2-way sync."),
 "hubspot-and-asana": dict(native=True, req={"hubspot": "Professional", "asana": "Starter"}, sync="1-way (HubSpot → Asana)",
   summary="Trap: the native Asana action runs inside HubSpot workflows, which need HubSpot Professional ($800/mo), and tasks only flow one way. Requires HubSpot on the 'Professional' plan and Asana on the 'Starter' plan."),
 "intercom-and-hubspot": dict(native=True, req={"intercom": "Essential", "hubspot": "Free"}, sync="1-way (Intercom → HubSpot)",
   summary="Intercom's HubSpot app works on Intercom Essential and any HubSpot plan, but it only syncs one way, from Intercom into HubSpot. Requires Intercom on the 'Essential' plan and HubSpot on the 'Free' plan."),
 "hubspot-and-slack": dict(native=True, req={"hubspot": "Free", "slack": "Free"}, sync="2-way",
   summary="Notifications and record actions work on HubSpot's free CRM and Slack's free plan; custom Slack messages from workflows need HubSpot Professional ($800/mo). Requires HubSpot on the 'Free' plan and Slack on the 'Free' plan."),
 "hubspot-and-stripe": dict(native=True, req={"hubspot": "Free", "stripe": "Standard"}, sync="2-way",
   summary="Stripe connects as a payment processor on any HubSpot plan for quotes, invoices and payment links; Stripe's per-transaction fees still apply. Requires HubSpot on the 'Free' plan and Stripe on the 'Standard' plan."),
 "hubspot-and-zendesk": dict(native=True, req={"hubspot": "Free", "zendesk": "Suite Team"}, sync="1-way (Zendesk → HubSpot)",
   summary="Zendesk tickets show on HubSpot contact timelines on any HubSpot plan, but only on contacts and only one way. Requires HubSpot on the 'Free' plan and Zendesk on the 'Suite Team' plan."),
 "hubspot-and-calendly": dict(native=True, req={"hubspot": "Free", "calendly": "Standard"}, sync="1-way (Calendly → HubSpot)",
   summary="Bookings create or update HubSpot contacts and log meetings on any HubSpot plan; routing from HubSpot forms needs Calendly Teams ($16/seat). Requires HubSpot on the 'Free' plan and Calendly on the 'Standard' plan."),
 "hubspot-and-mailchimp": dict(native=True, req={"hubspot": "Free"}, sync="1-way (HubSpot → Mailchimp)",
   summary="The free built-in integration only pushes name and email from non-HubSpot forms into Mailchimp; choosing two-way sync needs HubSpot Data Hub Starter. Requires HubSpot on the 'Free' plan and Mailchimp on the 'Standard' plan."),
 "freshdesk-and-hubspot": dict(native=True, req={"hubspot": "Free"}, sync="2-way",
   summary="HubSpot's Data Sync app syncs Freshdesk companies, contacts and tickets two ways on any HubSpot plan; custom field mappings need Data Hub Starter. Requires Freshdesk on the 'Growth' plan and HubSpot on the 'Free' plan."),
 "hubspot-and-clickup": dict(native=True, req={"hubspot": "Free", "clickup": "Unlimited"}, sync="1-way (automation triggers)",
   summary="ClickUp's native HubSpot integration runs on automations, such as creating a ClickUp task when a HubSpot deal closes. Requires HubSpot on the 'Free' plan and ClickUp on the 'Unlimited' plan."),
 "hubspot-and-monday": dict(native=True, req={"hubspot": "Free", "monday": "Standard"}, sync="1-way (HubSpot → monday.com)",
   summary="monday.com's native HubSpot recipes create board items from HubSpot companies, deals and contacts; two-way sync is a separate app that needs Data Hub Starter. Requires HubSpot on the 'Free' plan and Monday.com on the 'Standard' plan."),
 "salesforce-and-slack": dict(native=True, req={"salesforce": "Enterprise", "slack": "Pro"}, sync="2-way",
   summary="Big trap: Salesforce's current Slack apps need Enterprise edition or higher ($165/user/mo); the older Slack-built app that worked with lower editions no longer accepts new installs. Requires Salesforce Sales Cloud on the 'Enterprise' plan and Slack on the 'Pro' plan."),
 "salesforce-and-zendesk": dict(native=True, req={"zendesk": "Suite Team"}, sync="1-way per object (accounts → Zendesk, tickets → Salesforce)",
   summary="Zendesk's Salesforce integration works on every Zendesk Suite plan from Team up, but Salesforce Professional still needs the $25/user API add-on. Requires Salesforce Sales Cloud on the 'Professional' plan and Zendesk on the 'Suite Team' plan."),
}

COPY = {
 "hubspot-and-salesforce": dict(
   how="HubSpot's own Salesforce connector syncs leads, contacts, accounts, opportunities and custom objects between the two CRMs, and can embed HubSpot contact, company and deal insights inside Salesforce. It suits teams that run marketing in HubSpot and sales in Salesforce.",
   limits="The connector is only available on HubSpot Professional or Enterprise subscriptions, every sync uses part of your Salesforce API call allowance, and the Salesforce user who connects it needs the API Enabled permission.",
   sources=[("HubSpot: Connect HubSpot and Salesforce", f"{KB}/salesforce/install-the-hubspot-salesforce-integration"), ("HubSpot Marketplace: Salesforce", f"{MKT}/salesforce")]),
 "hubspot-and-asana": dict(
   how="The native integration is a HubSpot workflow action: when a deal closes or a ticket changes, HubSpot creates a task in an Asana project. It's useful for handing work from sales or support to delivery and onboarding teams.",
   limits="It needs HubSpot workflows, so a Professional or Enterprise subscription. Tasks only go from HubSpot to Asana, private Asana projects don't appear in HubSpot, and the Asana user who connects the integration becomes a collaborator on every task it creates.",
   sources=[("HubSpot: Create Asana tasks with workflows", f"{KB}/workflows/create-asana-tasks-with-workflows"), ("HubSpot Marketplace: Asana", f"{MKT}/asana")]),
 "intercom-and-hubspot": dict(
   how="Intercom's HubSpot app sends leads captured in Intercom to HubSpot as contacts and logs Intercom conversations on their HubSpot activity timeline, so sales can pick up where a chat left off.",
   limits="It only sends data one way, from Intercom to HubSpot. Customer replies sync in real time but teammate replies sync only once the conversation is closed, and company attributes other than the company name aren't sent. For HubSpot data in Intercom you need HubSpot's separate Data Sync app.",
   sources=[("Intercom: HubSpot app", "https://www.intercom.com/help/en/articles/2128216-hubspot-app"), ("HubSpot Marketplace: Intercom", f"{MKT}/intercom")]),
 "hubspot-and-slack": dict(
   how="The HubSpot app for Slack sends HubSpot notifications such as reminders, mentions and form submissions to Slack, and lets your team turn Slack messages into HubSpot tasks, tickets or notes. It's available on every HubSpot plan, including the free CRM.",
   limits="One Slack workspace can connect per HubSpot account, private channels need the app added to each one, and custom Slack messages sent from HubSpot workflows need a Professional or Enterprise subscription because workflows do. Slack's free plan allows up to 10 app installations.",
   sources=[("HubSpot: Connect HubSpot and Slack", f"{KB}/integrations/how-do-i-use-the-slack-integration"), ("HubSpot Marketplace: Slack", f"{MKT}/slack"), ("Slack: Free plan limits", "https://slack.com/help/articles/27204752526611-Feature-limitations-on-the-free-version-of-Slack")]),
 "hubspot-and-stripe": dict(
   how="You can connect Stripe as a payment processor in HubSpot and collect payments through HubSpot quotes, invoices and payment links on any HubSpot plan. HubSpot's separate Stripe Data Sync app keeps Stripe customers and HubSpot contacts in sync.",
   limits="Stripe's per-transaction processing fees still apply and aren't included in the cost above. Invoices and subscriptions you create in HubSpot aren't created in Stripe, the processor option isn't offered in every country (India is one exception), and custom field mappings in Data Sync need Operations Hub (now Data Hub) Starter.",
   sources=[("HubSpot: Connect Stripe as a payment processor", f"{KB}/payment-processing/connect-your-stripe-account-as-a-payment-processor-in-hubspot"), ("HubSpot Marketplace: Stripe Data Sync", f"{MKT}/stripe-data-sync")]),
 "hubspot-and-zendesk": dict(
   how="Zendesk's HubSpot integration adds Zendesk ticket events and chat transcripts to the HubSpot contact timeline, and creates new HubSpot contacts for ticket requesters who don't match an existing contact. It's available on all HubSpot subscriptions.",
   limits="Tickets can only be shown on the contact timeline, not on companies or deals, and data only flows from Zendesk into HubSpot. You need a Zendesk Suite plan from Team up.",
   sources=[("Zendesk: Zendesk Support for HubSpot", "https://support.zendesk.com/hc/en-us/articles/4408884090650-Setting-up-the-Zendesk-Support-for-HubSpot-integration"), ("HubSpot Marketplace: Zendesk", f"{MKT}/zendesk")]),
 "hubspot-and-calendly": dict(
   how="When someone books through Calendly, the integration creates a HubSpot contact if one doesn't exist yet, or logs the meeting on the existing contact. Reschedules update the meeting, and cancellations are marked [Canceled].",
   limits="Routing from HubSpot forms needs Calendly Teams or Enterprise. Changing a meeting's length in HubSpot doesn't update Calendly, and using Calendly's and HubSpot's calendar sync together can create duplicate meetings.",
   sources=[("Calendly: Calendly + HubSpot", "https://calendly.com/help/calendly-hubspot"), ("HubSpot Marketplace: Calendly", f"{MKT}/calendly-199720")]),
 "hubspot-and-mailchimp": dict(
   how="HubSpot's built-in Mailchimp integration, available on every HubSpot plan, adds people who fill in non-HubSpot forms to a Mailchimp list and can show Mailchimp email activity on contact records. HubSpot's Mailchimp Data Sync app can also sync contacts in the background.",
   limits="The built-in integration only sends contacts from HubSpot to Mailchimp, not the other way, and only their first name, last name and email address. Choosing one- or two-way sync in the Data Sync app needs Data Hub Starter.",
   sources=[("HubSpot: Use HubSpot's integration with Mailchimp", f"{KB}/forms/connect-non-hubspot-forms-to-mailchimp"), ("HubSpot Marketplace: Mailchimp Data Sync", f"{MKT}/mailchimp-data-sync")]),
 "freshdesk-and-hubspot": dict(
   how="HubSpot's Data Sync app for Freshdesk syncs companies, contacts and tickets between the two tools in both directions, with default field mappings and a historical sync of your existing records.",
   limits="Custom field mappings need Data Hub Starter or Professional. HubSpot doesn't name a minimum Freshdesk plan, so check Freshdesk's pricing page; this calculator assumes Growth.",
   sources=[("HubSpot Marketplace: Freshdesk Data Sync", f"{MKT}/freshdesk-data-sync")]),
 "hubspot-and-clickup": dict(
   how="ClickUp's native HubSpot integration works through automations, with over 20 ways to move work between the two, such as creating a ClickUp task or project when a HubSpot deal closes.",
   limits="It's automation-based rather than a continuous field-level sync. HubSpot's listing names ClickUp's Free Forever plan as compatible, but this calculator assumes Unlimited, which ClickUp's help center lists for the integration.",
   sources=[("HubSpot Marketplace: ClickUp", f"{MKT}/clickup")]),
 "hubspot-and-monday": dict(
   how="monday.com's HubSpot integration offers recipes that create monday.com board items from HubSpot companies, deals and contacts, so delivery or onboarding teams can pick up work as soon as it's sold.",
   limits="It needs monday.com Standard or Pro. HubSpot's separate monday.com Data Sync app adds two-way sync, but activating it needs Data Hub Starter.",
   sources=[("HubSpot Marketplace: monday.com", f"{MKT}/monday-com-203938"), ("HubSpot Marketplace: monday.com Data Sync", f"{MKT}/mondaycom-data-sync")]),
 "salesforce-and-slack": dict(
   how="Salesforce builds its own suite of Slack integrations that bring Salesforce records and notifications into Slack. The original Slack-built Salesforce app is no longer supported.",
   limits="Salesforce lists Enterprise, Performance, Unlimited and Developer editions for its Sales Cloud app for Slack, so Starter and Professional teams would need to upgrade or use middleware instead.",
   sources=[("Slack: Salesforce apps for Slack", "https://slack.com/help/articles/227838227-Salesforce-apps-for-Slack"), ("Salesforce Help: Enable Sales Cloud for Slack", "https://help.salesforce.com/s/articleView?id=slack.slack_apps_sales_enable_the_sales_cloud_for_slack_app.htm&language=en_US&type=5")]),
 "salesforce-and-zendesk": dict(
   how="Zendesk's Salesforce integration creates and updates Zendesk organizations from Salesforce accounts (and users from contacts or leads), syncs Zendesk tickets to Salesforce Cases, and can show Zendesk tickets inside Salesforce with Ticket View.",
   limits="It needs Salesforce Enterprise or above, or Professional with the API add-on. Account data syncs one way, from Salesforce to Zendesk, and ticket comments aren't synced to a Case field (Ticket View can display them).",
   sources=[("Zendesk: Connecting Salesforce to Zendesk", "https://support.zendesk.com/hc/en-us/articles/4408821555482-Connecting-your-Salesforce-organization-to-Zendesk"), ("Zendesk: Data sync from Salesforce", "https://support.zendesk.com/hc/en-us/articles/4408828539290-Configuring-data-sync-from-Salesforce-to-Zendesk"), ("Zendesk: Ticket sync to Salesforce", "https://support.zendesk.com/hc/en-us/articles/4408828449050-Setting-up-ticket-sync-from-Zendesk-to-Salesforce")]),
 "hubspot-and-pipedrive": dict(
   how="There's no first-party integration that keeps HubSpot and Pipedrive in sync. HubSpot Smart Transfer can import Pipedrive data into HubSpot, which suits a one-time move rather than running both CRMs side by side.",
   limits="For ongoing sync you need middleware such as Make or Zapier, which works trigger by trigger; your real middleware bill depends on task volume.",
   sources=[("HubSpot: Supported apps for Smart Transfer", f"{KB}/integrations/supported-apps-for-hubspot-smart-transfer")]),
 "salesforce-and-stripe": dict(
   how="The Stripe app for Salesforce Platform lets you process and reconcile Stripe payments inside Salesforce and call Stripe from Flow and Apex, for example to create Stripe subscriptions when orders are activated.",
   limits="Stripe says it works best on core clouds such as Sales Cloud, and the app now authenticates with a Stripe API key because OAuth sign-in was retired in version 1.17.",
   sources=[("Stripe: Stripe app for Salesforce Platform", "https://docs.stripe.com/connectors/stripe-connector-for-salesforce/overview"), ("Stripe: Installation guide", "https://docs.stripe.com/plugins/stripe-connector-for-salesforce/installation-guide")]),
 "salesforce-and-mailchimp": dict(
   how="Mailchimp for Salesforce connects Salesforce contacts and leads with your Mailchimp audience and brings Mailchimp campaign activity into Salesforce.",
   limits="It supports Enterprise, Unlimited, Performance, Developer and Professional editions, but on Professional your Salesforce account executive must enable API access first. Field mapping is limited by Mailchimp plan; Premium accounts can map up to 80 fields.",
   sources=[("Mailchimp: Connect Mailchimp for Salesforce", "https://mailchimp.com/help/connect-mailchimp-for-salesforce/"), ("Mailchimp: About Mailchimp for Salesforce", "https://mailchimp.com/help/about-mailchimp-for-salesforce/")]),
}
