# 2026-11-12: batch 2 of the grid expansion, 14 new pairs between the 18 tools the site already prices.
# Same rules and format as pairdata22.py: every requirement, "how it works" sentence, limit and setup step was read on
# the vendor's own page on Nov 12, 2026 (listed in the pair's sources); prices are the site's existing data.
#
# Sources that made this batch possible, all read today: ActiveCampaign's app directory (activecampaign.com/apps/...:
# who built each integration and which ActiveCampaign plans include it), Notion's connection gallery
# (notion.com/integrations/...), Airtable's sync integration articles, monday.com's integration and pricing pages,
# Mailchimp's integrations directory, Xero's App Store search and Make's app guides (apps.make.com, help.make.com).
# ActiveCampaign's, monday.com's and ClickUp's help centres still can't be read, so pairs that need them have no step
# list or describe a module instead of naming it.
#
# Left out today: Xero + Mailchimp (Mailchimp's directory lists a Xero-built integration, but Xero's own App Store
# doesn't show it, so it may no longer be offered), Intercom + Notion (its value is Fin, priced per resolution),
# ClickUp + Intercom and ClickUp + Calendly (ClickUp's pages don't say how they connect or on which plan; ClickUp's
# site started refusing reads part-way through), and monday.com + Salesforce (monday.com sells it for Enterprise only).
CHECKED23 = "Nov 12, 2026"
DATE23 = "2026-11-12"
MAKE = "Make Core ($10.59/mo, or $9/mo billed annually)"

MAKE_ACTIVE = ("Make Help: Active and inactive scenarios", "https://help.make.com/active-and-inactive-scenarios")
MAKE_SCHEDULE = ("Make Help: Schedule a scenario", "https://help.make.com/schedule-a-scenario")
MAKE_RUN = ("Click Run once in the toolbar to test it, then activate the scenario with the ON/OFF button on its details page. "
            "It runs every 15 minutes by default; click Every 15 minutes on the toolbar to change that.")
INSTANT = "If the module has an instant tag, click Create a webhook first."
AC_CONNECT = ("Connect ActiveCampaign: click Create a connection, enter the API key copied from your ActiveCampaign account, "
              "then the account name from its API URL, and click Save.")
XERO_CONNECT = "Connect Xero: click Create a connection, click Save and sign in to Xero if prompted. " + INSTANT


MAKE_AC = ("Make: ActiveCampaign app", "https://apps.make.com/activecampaign")


def ac_middleware(other, other_plan_note, what, how, via, steps, extra_sources, limits_extra=""):
    """A pair that ActiveCampaign's app directory lists as a "Middleware App", modeled on Make Core."""
    return dict(how_text=how, summary_lead=f"There's no native {other}–ActiveCampaign link: ActiveCampaign's app directory lists {other} as a middleware app, available on every ActiveCampaign plan",
                answer=(f"Not natively. ActiveCampaign's app directory lists {other} as a \"Middleware App\" that it doesn't build, included with every ActiveCampaign plan: "
                        f"{what} A connector such as Make or Zapier provides the link."),
                limits=("Each Make scenario runs one way. Make's ActiveCampaign guide says the app needs a paid ActiveCampaign account, so Starter is the minimum, and "
                        f"{other_plan_note} ActiveCampaign's listing doesn't say which connector it uses; this page models Make Core, the cheaper one." + limits_extra),
                steps=steps, via=via, extra_sources=extra_sources + [MAKE_AC])


AC_INTERCOM = ac_middleware("Intercom", "Make only needs an active Intercom account, so this page uses Intercom Essential.",
    "it creates or updates a contact in ActiveCampaign when a new email address is added to a lead in Intercom.",
    "With Make, a scenario watches Intercom for events, such as a lead getting an email address, and creates or updates the contact in ActiveCampaign. Each scenario runs one way.",
    ("intercom", "lead gets an email address", "create or update the contact"),
    ["Log in to Make, create a scenario and add the Intercom module Watch Events as the trigger.",
     "Connect Intercom: click Create a connection, enter a connection name, click Save, select your Make account to continue to intercom.com and follow the onscreen instructions. " + INSTANT,
     "Add an ActiveCampaign module that creates or updates a contact. " + AC_CONNECT,
     "Map the lead's email address and name from Intercom into the contact's fields.", MAKE_RUN],
    [("ActiveCampaign: Intercom integration", "https://www.activecampaign.com/apps/intercom"), ("Make: Intercom app", "https://apps.make.com/intercom")])
AC_ASANA = ac_middleware("Asana", "Asana is modeled at Starter, the cheapest Asana plan this site prices.",
    "ActiveCampaign says it keeps your team's contacts and deal activity in step with Asana.",
    "With Make, a scenario watches ActiveCampaign deals and creates an Asana task, for example when a deal moves to a new stage. Each scenario runs one way, so keeping both sides in step needs one scenario per direction.",
    ("activecampaign", "a deal moves to a new stage", "create a task"),
    ["Log in to Make, create a scenario and add an ActiveCampaign module that watches deals as the trigger. " + AC_CONNECT,
     "Add the Asana module Create a Task. Connect Asana: click Create a connection and continue to Asana; if you're already logged in to Asana, the connection is made straight away.",
     "Pick the Asana project and fill in the task's name and notes with values from the ActiveCampaign deal.", MAKE_RUN],
    [("ActiveCampaign: Asana integration", "https://www.activecampaign.com/apps/asana"), ("Make: Asana app", "https://apps.make.com/asana")])
AC_CLICKUP = ac_middleware("ClickUp", "Make only asks for a ClickUp account, so this page uses ClickUp Free.",
    "ActiveCampaign describes adding task comments for new contacts and changing deal stages when new tasks are created.",
    "With Make, a scenario watches ClickUp for new tasks and moves the matching ActiveCampaign deal to a new stage; another scenario can add a task comment when a contact is created. Each scenario runs one way.",
    ("clickup", "new task", "change a deal's stage"),
    ["Log in to Make, create a scenario and add a ClickUp module that watches for new tasks as the trigger.",
     "Connect ClickUp: click Create a connection, enter a connection name, click Save and sign in to ClickUp if prompted. " + INSTANT,
     "Add an ActiveCampaign module that updates a deal. " + AC_CONNECT,
     "Map the ClickUp task to the deal and choose the stage to move it to.", MAKE_RUN],
    [("ActiveCampaign: ClickUp integration", "https://www.activecampaign.com/apps/clickup"), ("Make: ClickUp app", "https://apps.make.com/clickup")])
AC_MONDAY = ac_middleware("monday.com", "monday.com's integrations and API start on its Standard plan, which this page uses.",
    "it moves items to a group in monday.com when a new contact is created in ActiveCampaign.",
    "With Make, a scenario watches ActiveCampaign for new contacts and moves an item to a group on a monday.com board, or creates the item. Each scenario runs one way.",
    ("activecampaign", "new contact", "move an item to a group"),
    ["Log in to Make, create a scenario and add an ActiveCampaign module that watches new contacts as the trigger. " + AC_CONNECT,
     "Add the monday.com module Move an Item Between Groups (or Create an Item). Connect monday.com: click Create a connection, choose monday.com as the connection type, paste your Personal API Token from monday.com into the API key field and click Save.",
     "Pick the board, the item and the group to move it to, using values from the new contact.", MAKE_RUN],
    [("ActiveCampaign: monday.com integration", "https://www.activecampaign.com/apps/monday"), ("Make: monday.com app", "https://apps.make.com/monday"),
     ("monday.com: Pricing", "https://monday.com/pricing")])
AC_FRESHDESK = ac_middleware("Freshdesk", "Freshdesk is modeled at Growth, the cheapest Freshdesk plan this site prices.",
    "its listing describes Zapier zaps that start campaigns, automations or deal actions in ActiveCampaign.",
    "With Make, a scenario watches Freshdesk tickets and, for example, adds the requester to an ActiveCampaign automation or updates their deal. Each scenario runs one way.",
    ("freshdesk", "new or updated ticket", "start an automation or update a deal"),
    ["In Freshdesk, click your profile picture, select Profile Settings, click View API key and copy it.",
     "Log in to Make, create a scenario and add a Freshdesk module that watches tickets as the trigger, then click Create a connection and enter your Freshdesk details and the API key.",
     "Add an ActiveCampaign module that adds the contact to an automation or updates a deal. " + AC_CONNECT,
     "Map the ticket's requester and details into the ActiveCampaign fields.", MAKE_RUN],
    [("ActiveCampaign: Freshdesk integration", "https://www.activecampaign.com/apps/freshdesk"), ("Make: Freshdesk app", "https://apps.make.com/freshdesk")],
    " ActiveCampaign's own listing builds it on Zapier, which would cost more.")


NEW23 = {
 # ---- native ---------------------------------------------------------------------------------------------------
 "activecampaign-and-slack": dict(template="activecampaign-and-calendly", swap=("calendly", "slack"), A="activecampaign", B="slack",
   req={"activecampaign": "Plus", "slack": "Free"}, native=True, mw=0, sync="1-way (ActiveCampaign → Slack)", difficulty=1, cats="Email Marketing|Communication",
   summary="ActiveCampaign's own Slack integration posts real-time alerts from its automations to Slack, for example when a customer asks for a demo or needs support; its app directory lists it with the Plus, Professional and Enterprise plans, not Starter. Requires ActiveCampaign on the 'Plus' plan and Slack on the 'Free' plan.",
   answer="Yes. ActiveCampaign builds a Slack integration that sends alerts from its automations to Slack channels. Its app directory marks it as outbound (ActiveCampaign to Slack) and includes it with the Plus, Professional and Enterprise plans, so Starter doesn't get it.",
   how="Inside an ActiveCampaign automation, a step posts a message to Slack the moment a contact does something your team should act on, such as asking for a quote, redeeming a promotion or needing support. ActiveCampaign pitches it for sales, marketing and support alerts, including ticket alerts.",
   setup=None, setup_src=None,
   limits="It isn't included with ActiveCampaign Starter, so it forces Plus. It only sends alerts from ActiveCampaign to Slack. ActiveCampaign's help centre, where its setup steps are, can't be read from here, so this page has no step list; the button below goes to ActiveCampaign's listing.",
   sources=[("ActiveCampaign: Slack integration", "https://www.activecampaign.com/apps/slack")],
   flow=[("activecampaign", "slack", "real-time alerts from automations")]),

 "zendesk-and-airtable": dict(template="slack-and-airtable", swap=("slack", "zendesk"), A="zendesk", B="airtable",
   req={"zendesk": "Suite Team", "airtable": "Business"}, native=True, mw=0, sync="1-way (Zendesk → Airtable)", difficulty=1, cats="Helpdesk|Productivity",
   summary="Airtable's own Zendesk sync copies the tickets in a Zendesk view into an Airtable table, one way, manually or about every hour; Airtable lists it as a premium sync for its Business and Enterprise Scale plans only. Requires Zendesk on the 'Suite Team' plan and Airtable on the 'Business' plan.",
   answer="Yes. Airtable builds a Zendesk sync that brings the tickets from a Zendesk view into Airtable as a synced table. It runs one way, from Zendesk to Airtable, and it's a premium sync on Airtable's Business and Enterprise Scale plans only.",
   how="You connect your Zendesk account, pick a Zendesk view, and Airtable creates a synced table of its tickets that refreshes manually or automatically about every hour. By default it syncs 14 common fields, among them subject, status, assignee, priority, requester, tags and due date; you can sync all fields instead, custom ones included. Changes made in Airtable don't go back to Zendesk.",
   setup=["In the Airtable base, click + Add or import, scroll to the bottom of the list and click the more sources option, then search for Zendesk and click it.",
          "Click Select account and pick a connected Zendesk account, or click + Connect new Zendesk account, enter your company's subdomain and sign in.",
          "Click the Select View dropdown, choose the Zendesk view whose tickets you want and click Next.",
          "Choose to sync specific fields (the default) or all fields, set how often to sync and whether deleted records are removed, then click Create table."],
   setup_src=("Airtable", "https://support.airtable.com/docs/airtable-sync-integration-zendesk"),
   limits="It needs Airtable Business or Enterprise Scale, so it forces Business. It's one-way: changes made in Airtable can't be synced back to Zendesk. Each synced table follows one Zendesk view, and Zendesk's Due date field only applies to tickets of the Task type. Airtable doesn't name a Zendesk plan, so this page uses Suite Team, Zendesk's cheapest plan with API access.",
   sources=[("Airtable: Sync integration: Zendesk", "https://support.airtable.com/docs/airtable-sync-integration-zendesk"),
            ("Airtable: Sync integrations overview", "https://support.airtable.com/docs/airtable-sync-integrations-overview")],
   flow=[("zendesk", "airtable", "tickets from a Zendesk view")]),

 "asana-and-notion": dict(template="slack-and-notion", swap=("slack", "asana"), A="asana", B="notion",
   req={"asana": "Starter", "notion": "Plus"}, native=True, mw=0, sync="1-way (Asana → Notion)", difficulty=1, cats="Project Management|Productivity",
   summary="Notion's own Asana connection shows live previews of Asana tasks in Notion pages and can copy a project's tasks into a Notion database; Notion notes that the copy isn't a two-way sync and won't pick up later changes. Requires Asana on the 'Starter' plan and Notion on the 'Plus' plan.",
   answer="Yes, in a limited way. Notion makes an Asana connection: paste an Asana link to see a live preview of the task, or paste it as a database to bring a project's tasks into Notion. Notion notes that this isn't a two-way sync.",
   how="Paste an Asana link and choose Paste as preview, or type /asana, to show the task's details in a Notion page. Pasting a project or task link as a database creates a Notion database with Asana properties that fills with the tasks; Notion says the data is duplicated into Notion at the moment of import and won't sync any changes.",
   setup=["Paste an Asana link into a Notion page and select Paste as preview, or type /asana to paste links from a menu.",
          "The first time, authorize the Asana connection when Notion prompts you.",
          "To bring tasks into a database, copy an Asana project or task link, paste it into Notion and select Paste as database."],
   setup_src=("Notion", "https://www.notion.com/integrations/asana"),
   limits="It's one-way, and a database made from Asana is a one-time copy: Notion says the data won't sync any changes after the import. Notion's page names no plan for either tool, so this page uses Asana Starter and Notion Plus, the cheapest plans of each that this site prices.",
   sources=[("Notion: Asana connection", "https://www.notion.com/integrations/asana")],
   flow=[("asana", "notion", "task previews and a one-time project copy")]),

 "clickup-and-notion": dict(template="slack-and-notion", swap=("slack", "clickup"), A="clickup", B="notion",
   req={"clickup": "Free", "notion": "Plus"}, native=True, mw=0, sync="1-way (ClickUp → Notion)", difficulty=1, cats="Project Management|Productivity",
   summary="Notion's own ClickUp connection turns pasted ClickUp links into live previews inside Notion pages; Notion lists link previews as its only feature, so no data is copied or synced. Requires ClickUp on the 'Free' plan and Notion on the 'Plus' plan.",
   answer="Only through link previews. Notion makes a ClickUp connection that shows a pasted ClickUp task as a rich, real-time preview in a Notion page. Notion lists that as its only feature; unlike its Asana connection, it has no database sync.",
   how="Paste a ClickUp link into Notion and choose Paste as preview, or type /clickup, and Notion shows the task with its latest updates. That's the whole connection: nothing is written back to ClickUp and no Notion database is created.",
   setup=["Paste a ClickUp link into a Notion page and select Paste as preview, or type /clickup to paste links from a menu.",
          "The first time, authorize the ClickUp connection when Notion prompts you; after that, the preview shows the task's details."],
   setup_src=("Notion", "https://www.notion.com/integrations/clickup"),
   limits="It's previews only: no database sync and nothing sent back to ClickUp, so moving data between the two needs a connector such as Make or Zapier. Notion's page names no plan for either tool, so this page uses ClickUp Free and Notion Plus.",
   sources=[("Notion: ClickUp connection", "https://www.notion.com/integrations/clickup")],
   flow=[("clickup", "notion", "live previews of pasted task links")]),

 "monday-and-mailchimp": dict(template="hubspot-and-mailchimp", swap=("hubspot", "monday"), A="monday", B="mailchimp",
   req={"monday": "Standard", "mailchimp": "Free"}, native=True, mw=0, sync="2-way", difficulty=1, cats="Project Management|Email Marketing",
   summary="monday.com's own Mailchimp integration adds Mailchimp subscribers to boards, turns board contacts into subscribers and posts campaign stats; Mailchimp lists it as free, and monday.com's integrations start on its Standard plan. Requires Monday.com on the 'Standard' plan and Mailchimp on the 'Free' plan.",
   answer="Yes. monday.com builds a Mailchimp integration that syncs leads and subscribers both ways and brings campaign notifications and stats into your boards. Mailchimp's directory lists it as free; on monday.com, integrations start on the Standard plan, with 250 integration actions a month.",
   how="From a board's integrations section you connect Mailchimp and pick a recipe: add new Mailchimp subscribers to monday.com, turn contacts and incoming leads on a board into Mailchimp subscribers, or get notified with stats after a campaign is sent.",
   setup=["In monday.com, open the board's integrations section.", "Connect your Mailchimp account.",
          "Set up the recipe that fits your use case, such as adding new subscribers to the board."],
   setup_src=("Mailchimp", "https://mailchimp.com/integrations/monday/"),
   limits="monday.com's Basic plan doesn't include integrations; Standard includes 250 integration actions a month and Pro 25,000, so a busy list may need Pro. monday.com's help centre can't be read from here, so the recipes come from monday.com's and Mailchimp's listing pages. Neither names a Mailchimp plan, so this page uses Mailchimp Free.",
   sources=[("monday.com: Mailchimp integration", "https://monday.com/integrations/mailchimp"), ("Mailchimp: monday.com integration", "https://mailchimp.com/integrations/monday/"),
            ("monday.com: Pricing", "https://monday.com/pricing")],
   flow=[("both", "leads and subscribers"), ("mailchimp", "monday", "campaign notifications and stats")]),

 # ---- through Make: pairs ActiveCampaign's directory lists as middleware apps ----------------------------------
 "intercom-and-activecampaign": dict(template="xero-and-activecampaign", swap=("xero", "intercom"), A="intercom", B="activecampaign",
   req={"intercom": "Essential", "activecampaign": "Starter"}, cats="Helpdesk|Email Marketing", difficulty=1, src_app="intercom", **AC_INTERCOM),
 "asana-and-activecampaign": dict(template="xero-and-activecampaign", swap=("xero", "asana"), A="asana", B="activecampaign",
   req={"asana": "Starter", "activecampaign": "Starter"}, cats="Project Management|Email Marketing", difficulty=1, src_app="activecampaign", **AC_ASANA),
 "clickup-and-activecampaign": dict(template="xero-and-activecampaign", swap=("xero", "clickup"), A="clickup", B="activecampaign",
   req={"clickup": "Free", "activecampaign": "Starter"}, cats="Project Management|Email Marketing", difficulty=1, src_app="clickup", **AC_CLICKUP),
 "monday-and-activecampaign": dict(template="xero-and-activecampaign", swap=("xero", "monday"), A="monday", B="activecampaign",
   req={"monday": "Standard", "activecampaign": "Starter"}, cats="Project Management|Email Marketing", difficulty=1, src_app="activecampaign", **AC_MONDAY),
 "freshdesk-and-activecampaign": dict(template="xero-and-activecampaign", swap=("xero", "freshdesk"), A="freshdesk", B="activecampaign",
   req={"freshdesk": "Growth", "activecampaign": "Starter"}, cats="Helpdesk|Email Marketing", difficulty=1, src_app="freshdesk", **AC_FRESHDESK),

 # ---- through Make: other pairs with no native link on the vendor's side ---------------------------------------
 "clickup-and-salesforce": dict(template="clickup-and-stripe", swap=("stripe", "salesforce"), A="clickup", B="salesforce",
   req={"clickup": "Free", "salesforce": "Professional"}, cats="Project Management|CRM", difficulty=2, src_app="salesforce",
   summary_lead="There's no native ClickUp–Salesforce connector: ClickUp's own Salesforce page points to Zapier, and Make Core also links them through Salesforce's API, which Professional Edition gets only as a paid add-on",
   answer="Not natively. ClickUp's own Salesforce page offers to connect the two through Zapier, for example to create ClickUp tasks from Salesforce actions and update Salesforce records as tasks are completed. Make does the same through Salesforce's API, which Professional Edition only gets as a paid add-on.",
   how_text="With Make, a scenario watches Salesforce, for example for a won opportunity, and creates a ClickUp task for the team that delivers; another can watch ClickUp and update the Salesforce record when the task is done. Each scenario runs one way. Make's Salesforce guide notes that not all Salesforce editions have API access.",
   steps=["Make sure your Salesforce org has API access: Enterprise and Unlimited include it, Professional needs the API add-on.",
          "Log in to Make, create a scenario and add the Salesforce module Watch records as the trigger.",
          "Connect Salesforce: click Create a connection, choose the Salesforce connection type, say whether you're using a Salesforce Sandbox, click Save and sign in.",
          "Add a ClickUp module that creates a task. Connect ClickUp: click Create a connection, click Save and sign in to ClickUp if prompted.",
          "Map the Salesforce fields into the task's name, list and description.", MAKE_RUN],
   limits="This calculator models Salesforce Professional with the $25/user API add-on plus Make Core; Enterprise includes API access without the add-on. ClickUp's page suggests Zapier, which would cost more. Each Make scenario runs one way.",
   via=("salesforce", "opportunity won", "create a task"),
   extra_sources=[("ClickUp: Salesforce integration", "https://clickup.com/integrations/salesforce"), ("Make: Salesforce app", "https://apps.make.com/salesforce"), ("Make: ClickUp app", "https://apps.make.com/clickup")]),

 "xero-and-zendesk": dict(template="xero-and-activecampaign", swap=("activecampaign", "zendesk"), A="xero", B="zendesk",
   req={"xero": "Early", "zendesk": "Suite Team"}, cats="Accounting|Helpdesk", difficulty=1, src_app="xero",
   summary_lead="There's no native Xero–Zendesk link: a search of Xero's App Store for Zendesk finds no app at all, and Make Core can open or update a Zendesk ticket when, for example, a Xero invoice changes",
   answer="Not natively. Searching Xero's App Store for Zendesk finds no app. Make or Zapier can connect the two, for example to open a Zendesk ticket for a customer whose Xero invoice is overdue.",
   how_text="A Make scenario watches Xero invoices and, for the ones you filter for, such as overdue invoices, creates or updates a ticket in Zendesk with the invoice details. Each scenario runs one way.",
   steps=["Log in to Make, create a scenario and add the Xero module Watch Invoices as the trigger.", XERO_CONNECT,
          "Add a Zendesk module that creates or updates a ticket. Connect Zendesk: click Create a connection, choose Zendesk as the connection type, enter your Zendesk subdomain, click Save and sign in if prompted.",
          "Add a filter for the invoices you care about and map the invoice details into the ticket.", MAKE_RUN],
   limits="Each Make scenario runs one way, and you build the filter and the ticket mapping yourself. Zendesk's Marketplace can't be read from here, so this page only checked Xero's side for a ready-made app.",
   via=("xero", "invoice overdue or paid", "create or update a ticket"),
   extra_sources=[("Xero App Store: search for Zendesk", "https://apps.xero.com/us/search?q=zendesk"), ("Make: Xero app", "https://apps.make.com/xero"), ("Make: Zendesk app", "https://apps.make.com/zendesk")]),

 "xero-and-asana": dict(template="xero-and-activecampaign", swap=("activecampaign", "asana"), A="xero", B="asana",
   req={"xero": "Early", "asana": "Starter"}, cats="Accounting|Project Management", difficulty=1, src_app="xero",
   summary_lead="There's no native Xero–Asana link: a search of Xero's App Store for Asana finds only Appy Pie Connect, a third-party workflow builder, and Make Core can create an Asana task when a Xero invoice is created or paid",
   answer="Not natively. Searching Xero's App Store for Asana finds one app, Appy Pie Connect, a third-party workflow builder. Make or Zapier can connect the two, for example to create an Asana task for each new or paid Xero invoice.",
   how_text="A Make scenario watches Xero invoices and creates a task in an Asana project, for example to follow up on a new invoice or to start work once it's paid. Each scenario runs one way.",
   steps=["Log in to Make, create a scenario and add the Xero module Watch Invoices as the trigger.", XERO_CONNECT,
          "Add the Asana module Create a Task. Connect Asana: click Create a connection and continue to Asana; if you're already logged in to Asana, the connection is made straight away.",
          "Pick the Asana project and fill in the task with values from the Xero invoice.", MAKE_RUN],
   limits="Each Make scenario runs one way, and you build the task mapping yourself. Appy Pie Connect is a separate product with its own pricing, not included here. Asana is modeled at Starter, the cheapest Asana plan this site prices.",
   via=("xero", "new or paid invoice", "create a task"),
   extra_sources=[("Xero App Store: search for Asana", "https://apps.xero.com/us/search?q=asana"), ("Make: Xero app", "https://apps.make.com/xero"), ("Make: Asana app", "https://apps.make.com/asana")]),

 "xero-and-airtable": dict(template="xero-and-activecampaign", swap=("activecampaign", "airtable"), A="xero", B="airtable",
   req={"xero": "Early", "airtable": "Free"}, cats="Accounting|Productivity", difficulty=1, src_app="xero",
   summary_lead="There's no native Xero–Airtable link: Airtable's sync integrations don't include Xero, Xero's App Store lists only third-party apps such as Data Fetcher, and Make Core can add a record to Airtable for each new or updated Xero invoice",
   answer="Not natively. Airtable's sync integrations don't include Xero, and searching Xero's App Store for Airtable shows third-party apps such as Data Fetcher. Make or Zapier can connect the two, for example to add an Airtable record for each new or updated Xero invoice.",
   how_text="A Make scenario watches Xero invoices and adds or updates a record in an Airtable table with the invoice's contact, amount, status and dates. Each scenario runs one way.",
   steps=["Log in to Make, create a scenario and add the Xero module Watch Invoices as the trigger.", XERO_CONNECT,
          "Add an Airtable module that creates a record. Connect Airtable: click Add next to Connection type and choose Airtable OAuth, click Save, then click Add a base, pick the base and click Grant access.",
          "Pick the table and map the invoice's fields into its columns.", MAKE_RUN],
   limits="Each Make scenario runs one way, and you build the field mapping yourself. Third-party Xero apps such as Data Fetcher are priced separately and aren't included.",
   via=("xero", "new or updated invoice", "add a record"),
   extra_sources=[("Xero App Store: search for Airtable", "https://apps.xero.com/us/search?q=airtable"),
                  ("Airtable: Sync integrations overview", "https://support.airtable.com/docs/airtable-sync-integrations-overview"),
                  ("Make: Xero app", "https://apps.make.com/xero"), ("Make: Airtable app", "https://apps.make.com/airtable")]),
}

# Fill in the Make pairs: same summary/limits/sources shape as batch 1's Make pages
NAMES = {"intercom": "Intercom", "asana": "Asana", "clickup": "ClickUp", "monday": "Monday.com", "freshdesk": "Freshdesk", "xero": "Xero",
         "activecampaign": "ActiveCampaign", "salesforce": "Salesforce Sales Cloud", "zendesk": "Zendesk", "airtable": "Airtable"}
for _p, _c in NEW23.items():
    if _c.get("native"): continue
    _c.update(native=False, mw=(10.59, 9), sync="1-way (trigger → action)")
    _req = " and ".join(f"{NAMES[t]} on the '{_c['req'][t]}' plan" for t in (_c["A"], _c["B"]))
    _c["summary"] = f"{_c.pop('summary_lead')}. Requires {_req}. Route it through {MAKE}."
    _c["how"] = _c.pop("how_text")
    _c["setup"] = _c.pop("steps"); _c["setup_src"] = ("Make", f"https://apps.make.com/{_c.pop('src_app')}")
    _c["sources"] = list(_c.pop("extra_sources")) + [MAKE_ACTIVE, MAKE_SCHEDULE]
    _guide = next(s for s in _c["sources"] if s[1] == _c["setup_src"][1])   # the button points at the guide the steps follow
    _c["cta"] = ("Setup guide: " + _guide[0], _guide[1])

PAIRS23 = {p: dict(native=c["native"], req=c["req"], sync=c["sync"], summary=c["summary"], date=DATE23) for p, c in NEW23.items()}
COPY23 = {p: dict(how=c["how"], limits=c["limits"], sources=c["sources"], answer=c["answer"], setup=c["setup"] or None, setup_src=c["setup_src"],
                  setup_checked=CHECKED23 if c["setup"] else None, top=True, checked=CHECKED23, **({"cta": c["cta"]} if c.get("cta") else {}))
          for p, c in NEW23.items()}
FLOW23 = {p: c["flow"] for p, c in NEW23.items() if c["native"]}
VIA23 = {p: c["via"] for p, c in NEW23.items() if not c["native"]}
