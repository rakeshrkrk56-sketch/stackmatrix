# 2026-11-12: batch 1 of the grid expansion, 17 new pairs between the 18 tools the site already prices.
# Every requirement, "how it works" sentence, limit and setup step below was read on the vendor's own page on
# Nov 12, 2026 (the page is listed in the pair's sources). Prices are the site's existing data (checked Nov 3, 2026,
# with the per-tool exceptions the byline names); nothing here changes a price.
#
# Where a vendor page names no plan, the pair is modeled on each tool's cheapest plan with API access, and the
# limits text says so. Three candidate pairs were left out because a fact they needed couldn't be read today:
# Zendesk + QuickBooks and Airtable + Calendly (no vendor page that settles whether a native integration exists),
# and Pipedrive + Stripe (the Marketplace apps are third-party and their pricing wasn't read).
#
# Fields: template = an existing page of the same connection type that shares one tool; swap = (tool in the
# template, tool it becomes); difficulty = the site's own setup-time rating (1-3), not a vendor-quoted time.
CHECKED22 = "Nov 12, 2026"
DATE22 = "2026-11-12"
MAKE = "Make Core ($10.59/mo, or $9/mo billed annually)"

MAKE_ACTIVE = ("Make Help: Active and inactive scenarios", "https://help.make.com/active-and-inactive-scenarios")
MAKE_SCHEDULE = ("Make Help: Schedule a scenario", "https://help.make.com/schedule-a-scenario")
MAKE_RUN = ("Click Run once in the toolbar to test it, then activate the scenario with the ON/OFF button on its details page. "
            "It runs every 15 minutes by default; click Every 15 minutes on the toolbar to change that.")
HS_SYNC = ("HubSpot: Connect and use HubSpot data sync", "https://knowledge.hubspot.com/integrations/connect-and-use-hubspot-data-sync")
CAL_SF = "https://calendly.com/help/how-to-integrate-calendly-with-salesforce"


def data_sync_steps(app, what):
    """HubSpot's data sync setup (knowledge.hubspot.com, read Nov 12) for an app whose listing needs Data Hub Starter."""
    return [f"Make sure you're a Super Admin or have App Marketplace permissions in HubSpot, and that the account has Data Hub Starter, which {app}'s listing says activating the sync needs.",
            f"In HubSpot, click the Marketplace icon in the top navigation bar, select HubSpot Marketplace, search for {app} and click Install.",
            f"In the dialog box, click Next, log in to your {app} account, review the requested access permissions and click Allow.",
            f"Pick the {what} to sync; HubSpot recommends a HubSpot object for it. Review the field mappings and the sync direction, then turn the sync on."]


NEW22 = {
 # ---- Calendly -------------------------------------------------------------------------------------------------
 "salesforce-and-calendly": dict(template="hubspot-and-calendly", swap=("hubspot", "salesforce"), A="salesforce", B="calendly",
   req={"salesforce": "Enterprise", "calendly": "Teams"}, native=True, mw=0, sync="1-way (Calendly → Salesforce)", difficulty=3, cats="CRM|Scheduling",
   summary="Calendly's own Salesforce package creates and updates Salesforce records, leads and events by default, as invitees book, cancel or reschedule; it needs Calendly Teams or higher and Salesforce Enterprise edition or higher. Requires Salesforce Sales Cloud on the 'Enterprise' plan and Calendly on the 'Teams' plan.",
   answer="Yes. Calendly builds a Salesforce integration, a package you install in your Salesforce org, but it needs Calendly's Teams plan or higher and Salesforce Enterprise edition or higher. Calendly says an error during installation may mean the org is on Salesforce Group or Professional edition.",
   how="As invitees schedule, cancel or reschedule, the package creates and updates Salesforce records: leads and events by default, and any Salesforce object if you customize it. It can also store routing form responses in Salesforce and send each user's Calendly links to their Salesforce user, for merge fields in email templates. Upcoming Calendly events show in the record's open activities, and canceled or rescheduled ones are tracked per invitee.",
   setup=["Make sure you're a Calendly owner or admin and a Salesforce admin, on Salesforce Enterprise edition or higher.",
          "In Calendly, go to Automations → Integrations & apps, select Salesforce under Sales and CRM, select Connect Salesforce and log in with your Salesforce credentials.",
          "On the Salesforce Integrations page in Calendly, select Install the Calendly package, choose Install for All Users and select Install.",
          "Grant third-party access (select Yes, then Continue), and select Done when the installation finishes.",
          "Return to Calendly and select Refresh to complete the connection."],
   setup_src=("Calendly", CAL_SF),
   limits="It needs Calendly Teams or higher and Salesforce Enterprise or higher, so Calendly Standard and Salesforce Group or Professional orgs can't use it. Routing by Salesforce lookup, such as routing to the record owner, is only on Calendly's Enterprise plan. If events stop syncing, Calendly's troubleshooting guide says to check the integration status, the Push New Events to Salesforce switch and the package's Salesforce flows.",
   sources=[("Calendly: How to integrate Calendly with Salesforce", CAL_SF),
            ("Calendly: Troubleshooting Salesforce integration", "https://calendly.com/help/troubleshooting-salesforce-integration")],
   flow=[("calendly", "salesforce", "bookings create or update leads and events")]),

 "stripe-and-calendly": dict(template="hubspot-and-calendly", swap=("hubspot", "stripe"), A="stripe", B="calendly",
   req={"stripe": "Standard", "calendly": "Standard"}, native=True, mw=0, sync="1-way (Calendly → Stripe)", difficulty=1, cats="Payments|Scheduling",
   summary="Calendly's own Stripe integration charges invitees when they book a paid event type; Calendly lists it on its paid plans, from Standard up. Requires Stripe on the 'Standard' plan and Calendly on the 'Standard' plan.",
   answer="Yes. Calendly builds a Stripe integration: connect your Stripe account in Calendly, turn on payments for an event type, and invitees pay when they book. Calendly lists it on its paid plans, from Standard up, so the free plan doesn't include it.",
   how="Each user connects their own Stripe account, then turns on Require payment to book this meeting for an event type and sets the amount and currency. Invitees can pay by card, Apple Pay, Google Pay, Link instant bank payments, or Affirm and Klarna where available, in AUD, CAD, EUR, GBP or USD. Personal event types use the host's Stripe account; shared and team event types use the organization owner's.",
   setup=["In Calendly, go to Automations, select Integrations & apps, find Stripe and connect your account; Calendly prompts you to create one if you don't have it. The Stripe account must be in live mode to take real payments.",
          "Go to the Scheduling page, choose the event type and select More options at the bottom of the editor.",
          "Expand the Payment section, toggle on Require payment to book this meeting and make sure the payment processor is set to Stripe.",
          "Enter the amount and currency, add any coupon codes, payment terms and cancellation policy, then select Save changes."],
   setup_src=("Calendly", "https://calendly.com/help/calendly-stripe"),
   limits="Each user has to connect their own Stripe account for personal event types; admins can't connect it for them. Calendly doesn't calculate or collect VAT or sales tax, so include tax in the price or the payment terms. Payments are in five currencies only: AUD, CAD, EUR, GBP and USD.",
   sources=[("Calendly: Calendly + Stripe", "https://calendly.com/help/calendly-stripe"),
            ("Calendly: Payments FAQs", "https://calendly.com/help/payments-faq")],
   flow=[("calendly", "stripe", "payment taken when an invitee books")]),

 "intercom-and-calendly": dict(template="hubspot-and-calendly", swap=("hubspot", "intercom"), A="intercom", B="calendly",
   req={"intercom": "Essential", "calendly": "Free"}, native=True, mw=0, sync="1-way (Calendly → Intercom)", difficulty=1, cats="Helpdesk|Scheduling",
   summary="Calendly's app for Intercom lets agents and bots share a scheduling link in chat, so visitors book without leaving the Messenger; Calendly lists it on all its plans, and Intercom needs a trial or paid subscription. Requires Intercom on the 'Essential' plan and Calendly on the 'Free' plan.",
   answer="Yes. Calendly makes an app for Intercom: install it from the Intercom App Store and you can put a scheduling invitation in a chat, add it to a bot's path or pin it to the Messenger home. Calendly lists it on all its plans; Intercom needs a trial or paid subscription.",
   how="An agent adds the Calendly app from the chat toolbar and picks a scheduling link; the visitor sees your availability inside the chat window and books there, and the invitation then shows the meeting details. A bot can offer the same link at the end of its path. Booking data doesn't flow into Intercom's CRM; Calendly suggests Zapier for that.",
   setup=["Install the Calendly app from the Intercom App Store. Each user sets it up for themselves; admins can't configure it for others.",
          "In a chat, open Add a messenger app in the chat toolbar, select the Calendly app and enter your scheduling link.",
          "Customize the message and button text, then click Create Invite to add the invitation to the chat.",
          "To automate it, add Calendly as a follow-up action (Send an app) at the end of a custom bot's path, then publish the bot."],
   setup_src=("Calendly", "https://calendly.com/help/calendly-intercom"),
   limits="It shares scheduling links and shows booked meetings in the conversation; it doesn't copy booking data into Intercom's CRM, which Calendly suggests doing through Zapier. Each user connects it individually, and it needs a trial or paid Intercom subscription.",
   sources=[("Calendly: Calendly + Intercom", "https://calendly.com/help/calendly-intercom")],
   flow=[("calendly", "intercom", "scheduling links and booked meetings in chat")]),

 # ---- HubSpot --------------------------------------------------------------------------------------------------
 "hubspot-and-xero": dict(template="hubspot-and-quickbooks", swap=("quickbooks", "xero"), A="hubspot", B="xero",
   req={"hubspot": "Free", "xero": "Early"}, native=True, mw=0, sync="2-way", difficulty=2, cats="CRM|Accounting",
   summary="HubSpot's own Xero app syncs contacts, products, invoices and payments one way or both ways on every HubSpot plan, including the free CRM; custom field mappings need Data Hub Starter. Requires HubSpot on the 'Free' plan and Xero on the 'Early' plan.",
   answer="Yes. HubSpot builds a Xero integration, Xero by HubSpot (Data Sync), which its knowledge base lists for all HubSpot products and plans. It syncs contacts, Xero items and HubSpot products, invoices and payments, each one way or both ways.",
   how="Contacts, products and invoices can sync in either direction, and payments applied to invoices sync from Xero to HubSpot or both ways. HubSpot recommends setting up contacts first, then products, then invoices, because Xero needs an invoice's contact and products to exist before the invoice syncs. When you set up invoice sync to Xero or both ways, the tax rates in your Xero account are imported into HubSpot's tax rate library.",
   setup=["Make sure you're a Super Admin or have App Marketplace permissions in HubSpot.",
          "In HubSpot, click the Marketplace icon in the top navigation bar, select HubSpot Marketplace, search for Xero by HubSpot (Data Sync) and click Install.",
          "Enter your Xero credentials, review the required permissions and click Accept.",
          "Go to Settings > Integrations > Connected Apps, click Xero, open the CRM syncs tab, click Contact sync and choose the sync direction.",
          "Then set up the product sync and the invoice sync, in that order."],
   setup_src=("HubSpot", "https://knowledge.hubspot.com/integrations/connect-hubspot-and-xero-data-sync"),
   limits="Invoices created in HubSpot have to be edited in HubSpot, or they fail to sync. Only six currencies are supported (USD, CAD, EUR, GBP, AUD and NZD), invoices that use HubSpot's automated sales tax don't sync to Xero, and only payments created after you connect the app sync. Custom field mappings need Data Hub Starter or higher.",
   sources=[("HubSpot: Connect HubSpot and Xero (Data Sync)", "https://knowledge.hubspot.com/integrations/connect-hubspot-and-xero-data-sync"),
            ("HubSpot Marketplace: Xero", "https://ecosystem.hubspot.com/marketplace/listing/xero-data-sync")],
   flow=[("both", "contacts, products, invoices, payments")]),

 "hubspot-and-airtable": dict(template="hubspot-and-quickbooks", swap=("quickbooks", "airtable"), A="hubspot", B="airtable",
   req={"hubspot": "Starter", "airtable": "Free"}, native=True, mw=0, sync="2-way", difficulty=2, cats="CRM|Productivity",
   summary="HubSpot's own Airtable data sync shares Airtable records with HubSpot both ways, but its Marketplace listing says activating the sync needs a paid Data Hub Starter subscription. Requires HubSpot on the 'Starter' plan and Airtable on the 'Free' plan.",
   answer="Yes. HubSpot builds an Airtable data sync app that shares Airtable records with HubSpot both ways, but its Marketplace listing says activating the sync needs a paid Data Hub Starter subscription; without it you can only try out the field mappings.",
   how="When a record is created or updated in either app, the change is shared with the other, and existing records sync as soon as you turn it on. Airtable describes two main uses: syncing contacts and syncing company information. HubSpot checks for changes on its side every five minutes and recommends a HubSpot object for each Airtable table you pick.",
   setup=data_sync_steps("Airtable", "Airtable table"),
   setup_src=("HubSpot", HS_SYNC[1]),
   limits="Activating the sync needs Data Hub Starter; this page models it at HubSpot's Starter price of $20 per seat a month for 10 seats. HubSpot's listing asks for an Airtable subscription without naming a plan, so this page assumes Airtable's Free plan. Custom field mappings also need Data Hub Starter or above.",
   sources=[("HubSpot Marketplace: Airtable (Data Sync)", "https://ecosystem.hubspot.com/marketplace/apps/airtable-data-sync4"), HS_SYNC,
            ("Airtable: Integrating HubSpot with Airtable", "https://support.airtable.com/docs/integrating-hubspot-with-airtable")],
   flow=[("both", "contacts, companies and other records")]),

 "hubspot-and-notion": dict(template="hubspot-and-quickbooks", swap=("quickbooks", "notion"), A="hubspot", B="notion",
   req={"hubspot": "Starter", "notion": "Plus"}, native=True, mw=0, sync="2-way", difficulty=2, cats="CRM|Productivity",
   summary="HubSpot's own Notion data sync shares records between Notion and HubSpot both ways, but its Marketplace listing says activating a sync with Notion requires a paid Data Hub Starter subscription. Requires HubSpot on the 'Starter' plan and Notion on the 'Plus' plan.",
   answer="Yes. HubSpot builds a Notion data sync app, but its Marketplace listing says activating a sync with Notion requires Data Hub Starter, and the app needs a Notion subscription.",
   how="When records are created or updated in either app, the change is shared with the other, and existing records sync as soon as you turn it on. On the HubSpot side the listing names contacts, companies, deals, tickets and other objects; on the Notion side it syncs the records in a workspace, and HubSpot recommends a HubSpot object for each Notion database you pick.",
   setup=data_sync_steps("Notion", "Notion database"),
   setup_src=("HubSpot", HS_SYNC[1]),
   limits="Activating the sync needs Data Hub Starter; this page models it at HubSpot's Starter price of $20 per seat a month for 10 seats. HubSpot's listing asks for a Notion subscription without naming a plan, so this page uses Notion Plus, the cheapest Notion plan this site prices. Custom field mappings also need Data Hub Starter or above.",
   sources=[("HubSpot Marketplace: Notion (Data Sync)", "https://ecosystem.hubspot.com/marketplace/listing/notion-data-sync"), HS_SYNC],
   flow=[("both", "contacts, companies, deals and database records")]),

 # ---- Intercom -------------------------------------------------------------------------------------------------
 "intercom-and-salesforce": dict(template="intercom-and-hubspot", swap=("hubspot", "salesforce"), A="intercom", B="salesforce",
   req={"intercom": "Advanced", "salesforce": "Professional"}, native=True, mw=0, sync="2-way", difficulty=3, cats="Helpdesk|CRM",
   summary="Intercom's own Salesforce app creates Salesforce leads from Intercom, syncs data and conversations and shows Salesforce details in the inbox, but it's only on Intercom's Advanced and Expert plans, and Salesforce needs API access. Requires Intercom on the 'Advanced' plan and Salesforce Sales Cloud on the 'Professional' plan.",
   answer="Yes. Intercom builds a Salesforce app, available on its Advanced and Expert plans. It needs a Salesforce edition with API access: Enterprise and Unlimited include it, and Professional can buy it as an add-on.",
   how="New leads captured in Intercom are created in Salesforce, and data and conversations sync whenever a user or lead is updated. In the Intercom inbox, teammates see Salesforce details such as lead status and owner, account and contact details, opportunity stage and value and close dates; conversations can be routed to the account owner, and Salesforce data can be used to target outbound messages.",
   setup=["Check that you have full admin permissions in Intercom (at least Apps and Integrations Access), and a regular Salesforce user, not API-only, with API Enabled, View All Data and read/write access to Leads, Contacts, Accounts and Tasks.",
          "Find Salesforce in the Intercom App Store and click Install now.",
          "Authorize Salesforce to access your Intercom workspace and log in to your Salesforce account.",
          "If that Salesforce user isn't a System Administrator, go to Setup → Connected Apps OAuth Usage in Salesforce and click Install on the Intercom app.",
          "Configure your data mapping for leads, users and their attributes."],
   setup_src=("Intercom", "https://www.intercom.com/help/en/articles/4497943-install-salesforce-integration"),
   limits="It isn't on Intercom's Essential plan, so it forces Advanced, and installing into a Salesforce sandbox needs Intercom's Expert plan. Tags and events can't be mapped and synced through the app. Salesforce's Contact, Group and Professional editions don't include API access; Professional can add it, and this page models Professional with that add-on.",
   sources=[("Intercom: Install Salesforce integration", "https://www.intercom.com/help/en/articles/4497943-install-salesforce-integration")],
   flow=[("intercom", "salesforce", "new leads, data and conversations"), ("salesforce", "intercom", "lead, account and opportunity details")]),

 "intercom-and-mailchimp": dict(template="intercom-and-hubspot", swap=("hubspot", "mailchimp"), A="intercom", B="mailchimp",
   req={"intercom": "Essential", "mailchimp": "Free"}, native=True, mw=0, sync="2-way", difficulty=1, cats="Helpdesk|Email Marketing",
   summary="Intercom's Mailchimp apps add Messenger and chat sign-ups to a Mailchimp audience, show each person's subscription status in the inbox and keep unsubscribes in step both ways; the Subscribe app needs any paid Intercom plan. Requires Intercom on the 'Essential' plan and Mailchimp on the 'Free' plan.",
   answer="Yes. Intercom has two Mailchimp apps: Mailchimp Subscribe, which captures email subscribers in the Messenger and in conversations, and Mailchimp Sync, which keeps unsubscribes matched in both tools. The Subscribe app needs a Mailchimp account and any paid Intercom plan.",
   how="Mailchimp Subscribe adds a sign-up card to the Messenger home, or agents send it in a conversation, and new subscribers join the Mailchimp list you choose. For people already on the list, the app shows their status, audience, star rating, open and click rates, sign-up date and tags, and agents can unsubscribe them. Mailchimp Sync uses a Mailchimp webhook, so unsubscribing in either tool carries over to the other.",
   setup=["In Intercom's App Store, search for Mailchimp Subscribe, click Install now, click Connect and allow access to your Mailchimp account.",
          "Select the Mailchimp list to sync, then write the card's title, description, confirmation message and any reward.",
          "Add the app to the Messenger home (Settings > Channels > Messenger > Customize Home with apps), or pin it in the inbox to send it in conversations.",
          "For unsubscribes, install Mailchimp Sync, click Sync your subscribers, choose the list and paste Intercom's callback URL into a new webhook in Mailchimp."],
   setup_src=("Intercom", "https://www.intercom.com/help/en/articles/1829462-mailchimp-subscribe-app-capture-new-subscribers"),
   limits="A Mailchimp list with required merge fields can't be used with the Subscribe app until those fields are made optional. The open and click rates it shows cover emails sent through Mailchimp only. Mailchimp Sync doesn't create a Mailchimp record for someone who isn't already there.",
   sources=[("Intercom: Mailchimp Subscribe app", "https://www.intercom.com/help/en/articles/1829462-mailchimp-subscribe-app-capture-new-subscribers"),
            ("Intercom: Sync unsubscribed users with the Mailchimp app", "https://www.intercom.com/help/en/articles/255-sync-unsubscribed-users-with-the-mailchimp-app")],
   flow=[("intercom", "mailchimp", "new subscribers from the Messenger"), ("both", "unsubscribes (Mailchimp Sync)")]),

 # ---- Asana ----------------------------------------------------------------------------------------------------
 "asana-and-salesforce": dict(template="asana-and-slack", swap=("slack", "salesforce"), A="asana", B="salesforce",
   req={"asana": "Advanced", "salesforce": "Professional"}, native=True, mw=0, sync="1-way (Salesforce → Asana)", difficulty=3, cats="Project Management|CRM",
   summary="Asana's own Salesforce integration lets Asana rules create or update tasks when something happens in Salesforce, such as a won opportunity; Asana lists it on its Advanced, Enterprise and Enterprise+ tiers. Requires Asana on the 'Advanced' plan and Salesforce Sales Cloud on the 'Professional' plan.",
   answer="Yes. Asana builds a Salesforce integration that works through Asana Rules: a Salesforce event triggers a rule that creates or updates tasks. It's on Asana's Advanced, Enterprise and Enterprise+ tiers. The older Asana app on the Salesforce AppExchange is deprecated and no longer supported.",
   how="In an Asana project you build a rule with a Salesforce trigger, for example an opportunity being closed or won, and an action such as creating a task or adding a comment or collaborator when a linked opportunity changes. Asana suggests it for hand-offs and intake when opportunities are closed or won, and for mapping revenue data into Asana to track pipeline progress.",
   setup=["Install Salesforce for Asana with your Salesforce admin, following Asana's installation guide.",
          "In your Asana project, click the Customize menu, then Rules > Add.",
          "Under rule triggers, select the Salesforce trigger from the external triggers tab.",
          "Select an action, such as Create a task, and click Publish rule."],
   setup_src=("Asana", "https://asana.com/apps/salesforce"),
   limits="It needs Asana Advanced or higher, so Asana Starter teams have to upgrade. Asana's app page doesn't say which Salesforce editions it supports, and its installation guide couldn't be read for this page, so this page models Salesforce Professional with the API add-on, the cheapest edition with API access; check the edition with your Salesforce admin. The legacy AppExchange app is no longer supported.",
   sources=[("Asana: Salesforce + Asana", "https://asana.com/apps/salesforce")],
   flow=[("salesforce", "asana", "opportunity events trigger Asana rules")]),

 "zendesk-and-asana": dict(template="hubspot-and-asana", swap=("hubspot", "zendesk"), A="zendesk", B="asana",
   req={"zendesk": "Suite Team", "asana": "Starter"}, native=True, mw=0, sync="2-way", difficulty=1, cats="Helpdesk|Project Management",
   summary="Asana's own Zendesk integration lets agents create or link Asana tasks from a ticket and see the task's status and owner in Zendesk, while Asana shows the ticket's details; Asana says it's available to customers of both tools. Requires Zendesk on the 'Suite Team' plan and Asana on the 'Starter' plan.",
   answer="Yes. Asana builds a Zendesk integration: agents create Asana tasks, with attachments, or link existing ones from a Zendesk ticket, and the task's status and owner show in Zendesk while the ticket's title, number and assignee show in Asana.",
   how="From a ticket, an agent creates a task or links an existing one. In Asana, a widget on the task shows who owns the ticket, its status and when it was last updated; when the task's assignee, due date or completion status changes in Asana, Zendesk is updated too. Asana rules can also add a comment to the Zendesk ticket automatically.",
   setup=["In Zendesk, open the Asana listing in the Zendesk Marketplace, add it and sign in to Asana.",
          "In Asana, open the project where tickets should go, click Customize in the upper right, scroll to Apps and select + Add app.",
          "Select Zendesk and follow the on-screen instructions to sign in to Zendesk.",
          "Open a ticket in Zendesk and create a new Asana task or link an existing one."],
   setup_src=("Asana", "https://asana.com/apps/zendesk"),
   limits="Only the fields Asana lists sync: the task's assignee, due date and completion status go to Zendesk, and the ticket's title, number, owner and status show in Asana. Asana says the integration is available to customers of both tools and names no plan, so this page models each tool's cheapest plan with API access (Asana Starter, Zendesk Suite Team). Zendesk's Marketplace listing couldn't be read for this page.",
   sources=[("Asana: Zendesk + Asana", "https://asana.com/apps/zendesk"),
            ("Asana: Asana for Zendesk", "https://asana.com/inside-asana/asana-for-zendesk")],
   flow=[("zendesk", "asana", "tickets create or link tasks"), ("asana", "zendesk", "task status, assignee and due date")]),

 # ---- Airtable -------------------------------------------------------------------------------------------------
 "salesforce-and-airtable": dict(template="slack-and-airtable", swap=("slack", "salesforce"), A="salesforce", B="airtable",
   req={"salesforce": "Professional", "airtable": "Business"}, native=True, mw=0, sync="1-way (Salesforce → Airtable)", difficulty=2, cats="CRM|Productivity",
   summary="Airtable's own Salesforce sync copies a Salesforce report into an Airtable table, one way, manually or about every hour; it's only on Airtable's Business and Enterprise Scale plans. Requires Salesforce Sales Cloud on the 'Professional' plan and Airtable on the 'Business' plan.",
   answer="Yes. Airtable builds a Salesforce sync integration that brings a Salesforce report into Airtable as a synced table. It runs one way, from Salesforce to Airtable, and it's only on Airtable's Business and Enterprise Scale plans.",
   how="You pick a Salesforce report and a unique ID column, and Airtable creates a read-only synced table that refreshes manually or automatically, about every hour. Fields you add to the table yourself stay editable. To send data back, Airtable's Salesforce automation actions can create or update a Salesforce record when something happens in the base.",
   setup=["Have a Salesforce report with the records you want, and make sure the Salesforce user who connects it has the View and Run Report permissions on that report.",
          "In the Airtable base, click + Add or import and choose Salesforce; if it isn't listed, click the more sources option at the bottom and search for it.",
          "Select or link your Salesforce account, then choose the report and its unique ID column.",
          "Pick the primary field, choose to sync all fields or specific ones, set how often to sync and how deleted records are handled, then create the synced table."],
   setup_src=("Airtable", "https://support.airtable.com/docs/airtable-sync-integration-salesforce"),
   limits="It needs Airtable Business or Enterprise Scale, so Free and Team workspaces can't use it. If a report's filters change, records that no longer match are deleted from Airtable along with anything added to them, and the unique ID and primary field can't be changed after the table is created. The sync stops if the connecting Salesforce user is deactivated. Airtable reads the report through Salesforce's API, so this page models Salesforce Professional with the API add-on.",
   sources=[("Airtable: Sync integration: Salesforce", "https://support.airtable.com/docs/airtable-sync-integration-salesforce")],
   flow=[("salesforce", "airtable", "a Salesforce report as a synced table")]),

 # ---- Pipedrive ------------------------------------------------------------------------------------------------
 "pipedrive-and-intercom": dict(template="pipedrive-and-slack", swap=("slack", "intercom"), A="pipedrive", B="intercom",
   req={"pipedrive": "Lite", "intercom": "Essential"}, native=True, mw=0, sync="2-way", difficulty=1, cats="CRM|Helpdesk",
   summary="Intercom's own Pipedrive app creates Pipedrive deals from a lead's profile, syncs later conversations to the matching Pipedrive person and shows deal details in the inbox. Requires Pipedrive on the 'Lite' plan and Intercom on the 'Essential' plan.",
   answer="Yes. Intercom makes a Pipedrive app: install it from Intercom's App Store and connect Pipedrive, and you can create deals while you chat and sync conversations into Pipedrive.",
   how="Clicking Create Deal in a lead's or user's profile creates a deal in the first stage of your default pipeline, with the lead's name and email. From then on, conversations sync to the matching Pipedrive person, and to the deal when it was created from the inbox, as done activities whose transcript updates when someone replies and when the conversation closes.",
   setup=["In Intercom, go to the App Store, click the Pipedrive app and click Install now.",
          "Connect your Pipedrive account to Intercom when asked.",
          "Add the External profiles app to the Inbox, then click Create Deal in a lead's or user's profile."],
   setup_src=("Intercom", "https://www.intercom.com/help/en/articles/2535853-pipedrive-app"),
   limits="Deals always land in the first stage of your default pipeline, and only the lead's name and email are sent. Conversations sync only if the person exists in Pipedrive with a matching email, and only conversations after you connect; later conversations with people on a deal aren't added to that deal. Intercom's article names no plan requirement, so this page models each tool's cheapest plan.",
   sources=[("Intercom: Pipedrive app", "https://www.intercom.com/help/en/articles/2535853-pipedrive-app")],
   flow=[("intercom", "pipedrive", "deals and conversations"), ("pipedrive", "intercom", "deal details in the inbox")]),

 "pipedrive-and-zendesk": dict(template="pipedrive-and-slack", swap=("slack", "zendesk"), A="pipedrive", B="zendesk",
   req={"pipedrive": "Lite", "zendesk": "Suite Team"}, native=True, mw=0, sync="2-way", difficulty=1, cats="CRM|Helpdesk",
   summary="Pipedrive's own Zendesk integration shows Zendesk tickets on Pipedrive people, organizations and deals, shows Pipedrive deals beside each ticket, and lets each side create the other's records. Requires Pipedrive on the 'Lite' plan and Zendesk on the 'Suite Team' plan.",
   answer="Yes. Pipedrive builds a Zendesk Support integration: sales sees a person's Zendesk tickets in Pipedrive, and agents see that person's Pipedrive deals in Zendesk. Pipedrive says anyone with access to both a Pipedrive and a Zendesk account can use it.",
   how="Records are matched by the person's email address. In Pipedrive, a Zendesk panel on deals, people and organizations lists up to 20 tickets with their status, and Create in Zendesk opens a new ticket. In Zendesk, a Pipedrive widget on each ticket shows the requester's deals with their title, status, value and creation date, and Add deal creates a deal, and a contact if there isn't one.",
   setup=["In the Pipedrive Marketplace, search for Zendesk and click Install now, choose your Pipedrive account and click Allow and install.",
          "Enter your Zendesk domain, click Authenticate with Zendesk and then Allow.",
          "To finish, open the Pipedrive app listing in the Zendesk Marketplace, click Install, select your Zendesk account and click Install again.",
          "Review the Pipedrive app details in Zendesk Support and click Install."],
   setup_src=("Pipedrive", "https://support.pipedrive.com/en/article/pipedrive-integration-zendesk"),
   limits="Pipedrive calls the sync two-way but contextual: each tool shows the other's records, and nothing is overwritten. Tickets and deals only appear when the requester's email matches a Pipedrive contact, the panel lists up to 20 tickets, and creating tickets needs the right Zendesk permissions. Neither vendor's article names a plan, so this page models each tool's cheapest plan.",
   sources=[("Pipedrive: Zendesk integration", "https://support.pipedrive.com/en/article/pipedrive-integration-zendesk"),
            ("Pipedrive: Zendesk FAQ", "https://support.pipedrive.com/en/article/zendesk-integration-faq")],
   flow=[("zendesk", "pipedrive", "tickets on people, organizations and deals"), ("pipedrive", "zendesk", "deal details beside each ticket")]),

 "pipedrive-and-asana": dict(template="pipedrive-and-slack", swap=("slack", "asana"), A="pipedrive", B="asana",
   req={"pipedrive": "Lite", "asana": "Starter"}, native=True, mw=0, sync="1-way (Pipedrive → Asana)", difficulty=1, cats="CRM|Project Management",
   summary="Pipedrive's own Asana integration creates an Asana task or project when a deal is won, lost or moved to a chosen stage, with the deal's title, value, contacts, notes and attachments; data flows one way. Requires Pipedrive on the 'Lite' plan and Asana on the 'Starter' plan.",
   answer="Yes. Pipedrive builds an Asana integration that creates Asana tasks or projects from Pipedrive deals. It runs one way, from Pipedrive to Asana.",
   how="A rule sets the trigger, a deal won, lost or moved to a stage you choose in a pipeline, and what to send: the deal title, value, contact details, pinned notes and attachments. It then creates a task in an Asana project, optionally assigned to someone, or a new project. Pipedrive's Automations add four ready-made Asana templates, one of them for new leads.",
   setup=["In the Pipedrive Marketplace, open the Asana integration, click Install now (or Authorize), choose who can use it and click Next.",
          "Review the permissions and click Allow and install, then sign in to Asana and click Allow.",
          "Open the Account menu > Tools and apps > Asana, and choose the trigger (deal won, lost or moved to a stage) and the pipeline.",
          "Choose the deal details to send and whether to create a task or a project, pick the Asana workspace and project, and click Save changes."],
   setup_src=("Pipedrive", "https://support.pipedrive.com/en/article/pipedrive-integration-asana"),
   limits="It's one-way, from Pipedrive to Asana; each admin user can create one rule, and projects can't carry attachments. Pipedrive's Asana templates in Automations need its Growth plan or higher; the article names no plan for the basic rule, so this page models Pipedrive Lite. Asana is modeled at Starter, the cheapest Asana plan this site prices.",
   sources=[("Pipedrive: Asana integration", "https://support.pipedrive.com/en/article/pipedrive-integration-asana")],
   flow=[("pipedrive", "asana", "won, lost or moved deals become tasks or projects")]),

 # ---- Mailchimp ------------------------------------------------------------------------------------------------
 "mailchimp-and-slack": dict(template="mailchimp-and-calendly", swap=("calendly", "slack"), A="mailchimp", B="slack",
   req={"mailchimp": "Free", "slack": "Free"}, native=True, mw=0, sync="1-way (Mailchimp → Slack)", difficulty=1, cats="Email Marketing|Communication",
   summary="The free Slack integration in Mailchimp's directory, made by Slack, posts subscribes, unsubscribes and campaign sending status to a Slack channel; on paid Slack plans, Workflow Builder adds Mailchimp steps such as adding a contact. Requires Mailchimp on the 'Free' plan and Slack on the 'Free' plan.",
   answer="Yes. Mailchimp's integrations directory lists a free Slack integration, developed by Slack, that posts list and campaign updates to a channel. On paid Slack plans, Slack's Workflow Builder also has Mailchimp steps.",
   how="After you authenticate Mailchimp, you choose which lists to monitor and which notifications to post to your Slack channel: subscribes, unsubscribes and campaign sending status. In the other direction, Slack's Mailchimp connector steps can add a contact to an audience, create or send a campaign and get a campaign report from inside a workflow.",
   setup=["Open the Slack integration in Mailchimp's integrations directory and authenticate your Mailchimp account.",
          "Pick the lists to monitor and the types of notifications to post to your Slack channel.",
          "For actions in Mailchimp, on a paid Slack plan, add a Mailchimp step to a workflow in Workflow Builder."],
   setup_src=("Mailchimp", "https://mailchimp.com/integrations/slack/"),
   limits="Mailchimp's directory listing was last updated on March 6, 2020, so check that it still installs as described. Workflow Builder, which the Mailchimp steps need, is available on paid Slack plans only; at Slack Free the integration only posts notifications.",
   sources=[("Mailchimp: Slack integration", "https://mailchimp.com/integrations/slack/"),
            ("Slack developers: Mailchimp connector", "https://api.slack.com/automation/connectors/mailchimp"),
            ("Slack Help: Create a workflow in Slack", "https://slack.com/help/articles/17542172840595-Build-a-workflow--Create-a-workflow-in-Slack")],
   flow=[("mailchimp", "slack", "subscribes, unsubscribes, campaign status")]),

 # ---- Through Make ---------------------------------------------------------------------------------------------
 "salesforce-and-xero": dict(template="salesforce-and-quickbooks", swap=("quickbooks", "xero"), A="salesforce", B="xero",
   req={"salesforce": "Professional", "xero": "Early"}, native=False, mw=(10.59, 9), sync="1-way (trigger → action)", difficulty=2, cats="CRM|Accounting",
   summary="There's no native Salesforce–Xero connector: Xero's App Store points to partner apps such as TwoCanConnect and SFX Connect, and Make Core links the two through Salesforce's API, which Professional Edition gets only as a paid add-on. Requires Salesforce Sales Cloud on the 'Professional' plan and Xero on the 'Early' plan. Route it through " + MAKE + ".",
   answer="Not natively. Xero's App Store points to partner apps for Salesforce, such as TwoCanConnect and SFX Connect, each priced separately, and Make or Zapier can connect the two through Salesforce's API, which Professional Edition only gets as a paid add-on.",
   how="With Make, a scenario watches Salesforce, for example for a won opportunity, and creates the contact or invoice in Xero; another can watch Xero for new or paid invoices and update Salesforce. Each scenario runs one way. Make's Salesforce guide notes that not all Salesforce editions have API access.",
   setup=["Make sure your Salesforce org has API access: Enterprise and Unlimited include it, Professional needs the API add-on.",
          "Log in to Make, create a scenario and add the Salesforce module Watch records as the trigger.",
          "Connect Salesforce: click Create a connection, choose the Salesforce connection type, say whether you're using a Salesforce Sandbox, click Save and sign in.",
          "Add the Xero module Create an Invoice (or Create a Contact). Connect Xero: click Create a connection, click Save and sign in to Xero if prompted.",
          "Map the Salesforce fields into the Xero fields.",
          MAKE_RUN],
   setup_src=("Make", "https://apps.make.com/salesforce"),
   cta=("Setup guide: Make: Salesforce app", "https://apps.make.com/salesforce"),
   limits="This calculator models Salesforce Professional with the $25/user API add-on plus Make Core; Enterprise includes API access without the add-on. Partner apps from Xero's App Store are priced separately and aren't included. Each Make scenario runs one way, and real usage can push Make onto a bigger plan.",
   sources=[("Xero App Store: Integrate Xero with Salesforce", "https://apps.xero.com/us/collection/integrate-xero-with-salesforce"),
            ("Make: Salesforce app", "https://apps.make.com/salesforce"), ("Make: Xero app", "https://apps.make.com/xero"), MAKE_ACTIVE, MAKE_SCHEDULE],
   via=("salesforce", "opportunity won", "create the contact or invoice")),

 "xero-and-slack": dict(template="xero-and-activecampaign", swap=("activecampaign", "slack"), A="xero", B="slack",
   req={"xero": "Early", "slack": "Free"}, native=False, mw=(10.59, 9), sync="1-way (trigger → action)", difficulty=1, cats="Accounting|Communication",
   summary="There's no native Xero–Slack app: Xero's App Store shows third-party apps for Slack, such as Approveit, and Make Core can post a Slack message when a Xero invoice is created or updated. Requires Xero on the 'Early' plan and Slack on the 'Free' plan. Route it through " + MAKE + ".",
   answer="Not natively. Searching Xero's App Store for Slack shows third-party apps such as Approveit, which handles approvals from Slack. Make or Zapier can connect the two, for example to post a Slack message for each new Xero invoice.",
   how="A Make scenario watches Xero, for example for new or updated invoices, and sends a message to a Slack channel with the invoice details. Each scenario runs one way; a scenario in the other direction could create a Xero record from a Slack message.",
   setup=["Log in to Make, create a scenario and add the Xero module Watch Invoices as the trigger.",
          "Connect Xero: click Create a connection, click Save and sign in to Xero if prompted. If the module has an instant tag, click Create a webhook first.",
          "Add a Slack module that sends a message to a channel. Connect Slack: click Create a connection and, if asked, choose the Slack (user) or Slack (bot) connection type, then sign in.",
          "Write the message with values from the Xero invoice.",
          MAKE_RUN],
   setup_src=("Make", "https://apps.make.com/xero"),
   cta=("Setup guide: Make: Xero app", "https://apps.make.com/xero"),
   limits="Each Make scenario runs one way. Make's Slack guide notes that Slack Watch modules only work with user connections, and that workspace owners can stop members from connecting apps that aren't in the Slack Marketplace, which Make isn't; ask an owner to allow it if the connection is blocked.",
   sources=[("Xero App Store: apps for Slack", "https://apps.xero.com/us/search?q=slack"),
            ("Make: Xero app", "https://apps.make.com/xero"), ("Make: Slack app", "https://apps.make.com/slack"), MAKE_ACTIVE, MAKE_SCHEDULE],
   via=("xero", "new or updated invoice", "post a message")),
}

# what the renderer and the wiring script read
PAIRS22 = {p: dict(native=c["native"], req=c["req"], sync=c["sync"], summary=c["summary"], date=DATE22) for p, c in NEW22.items()}
COPY22 = {p: dict(how=c["how"], limits=c["limits"], sources=c["sources"], answer=c["answer"], setup=c["setup"], setup_src=c["setup_src"],
                  setup_checked=CHECKED22, top=True, checked=CHECKED22, **({"cta": c["cta"]} if c.get("cta") else {}))
          for p, c in NEW22.items()}
FLOW22 = {p: c["flow"] for p, c in NEW22.items() if c["native"]}
VIA22 = {p: c["via"] for p, c in NEW22.items() if not c["native"]}
