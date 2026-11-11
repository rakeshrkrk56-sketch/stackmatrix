# 2026-11-11: numbered setup steps for the 19 pairs that run through a connector. Each list follows the connector's own
# documentation as read on Nov 11, 2026:
#   - Make: the app guide for each tool (apps.make.com/<app>: how to create the connection, and the module names where
#     the guide lists them), plus help.make.com "Active and inactive scenarios" and "Schedule a scenario".
#     Where a guide doesn't list its module names (ClickUp, Notion, Zendesk, ActiveCampaign, HubSpot CRM), the step
#     describes the module instead of naming it.
#   - Zapier: help.zapier.com "Set up your Zap trigger" and "What is a Zap?", plus each pair's page on zapier.com for
#     the trigger names that page shows.
#   - Stripe + Mailchimp: Mailchimp's help article for the Data Mapper connection.
# Nothing here changes a price, a plan requirement or the existing "how it works" text.
SETUP21_CHECKED = "Nov 11, 2026"
# This page had a three-line outline of the options (no single guide behind it). The Make steps below replace it,
# because Make is the route the page's calculator models; the other options stay in its "how it works" text.
REPLACE21 = {"pipedrive-and-calendly"}

MAKE_ACTIVE = ("Make Help: Active and inactive scenarios", "https://help.make.com/active-and-inactive-scenarios")
MAKE_SCHEDULE = ("Make Help: Schedule a scenario", "https://help.make.com/schedule-a-scenario")
ZAP_TRIGGER = ("Zapier Help: Set up your Zap trigger", "https://help.zapier.com/hc/en-us/articles/8496288188429")
ZAP_BASICS = ("Zapier Help: What is a Zap?", "https://help.zapier.com/hc/en-us/articles/8496309697421-Create-Zaps")

# tool -> (name as Make shows it, apps.make.com slug, how its guide says to create the connection)
APPS = {
 "stripe": ("Stripe", "stripe", "click Create a connection, choose Stripe API Key or Stripe OAuth as the connection type, click Save and confirm access if prompted"),
 "airtable": ("Airtable", "airtable", "click Add next to Connection type and choose Airtable OAuth, click Save, then click Add a base, pick the base and click Grant access"),
 "quickbooks": ("QuickBooks", "quickbooks", "click Create a connection, click Save and sign in to QuickBooks if prompted"),
 "clickup": ("ClickUp", "clickup", "click Create a connection, click Save and sign in to ClickUp if prompted"),
 "asana": ("Asana", "asana", "click Create a connection and continue to Asana; if you're already logged in to Asana, the connection is made straight away"),
 "pipedrive": ("Pipedrive", "pipedrive", "click Create a connection, click Save and sign in to Pipedrive if prompted"),
 "mailchimp": ("Mailchimp", "mailchimp", "click Create a connection, click Save and sign in to Mailchimp if prompted"),
 "monday": ("monday.com", "monday", "click Create a connection, choose monday.com as the connection type, paste your Personal API Token from monday.com into the API key field and click Save"),
 "notion": ("Notion", "notion", "click Create a connection, choose Notion Internal as the connection type, paste the internal integration token from your Notion account and click Save. In Notion, add the databases Make should see to that integration"),
 "calendly": ("Calendly", "calendly", "click Create a connection, click Save and sign in to Calendly if prompted"),
 "xero": ("Xero", "xero", "click Create a connection, click Save and sign in to Xero if prompted"),
 "activecampaign": ("ActiveCampaign", "activecampaign", "click Create a connection and enter your API key, account name and domain. The API URL and key are in ActiveCampaign under Settings > Developer"),
 "zendesk": ("Zendesk", "zendesk", "click Create a connection, choose Zendesk as the connection type, enter your Zendesk subdomain, click Save and sign in if prompted"),
 "hubspot": ("HubSpot", "hubspotcrm", "click Create a connection, click Save and sign in to HubSpot if prompted. A HubSpot Super Admin has to pre-approve the Make app first"),
}
INSTANT = "If the module has an instant tag, click Create a webhook first. "   # the note these guides carry
HAS_INSTANT_NOTE = {"stripe", "clickup", "calendly", "xero", "monday", "zendesk", "activecampaign", "hubspot"}
RUN = ("Click Run once in the toolbar to test it, then activate the scenario with the ON/OFF button on its details page. "
       "It runs every 15 minutes by default; click Every 15 minutes on the toolbar to change that.")

def make_src(app): return (f"Make: {APPS[app][0]} app", f"https://apps.make.com/{APPS[app][1]}")

def make(trig, trig_mod, act, act_mod, fill):
    tn, _, tc = APPS[trig]; an, _, ac = APPS[act]
    return dict(setup_src=("Make", make_src(trig)[1]), extra_sources=[make_src(trig), make_src(act), MAKE_ACTIVE, MAKE_SCHEDULE],
                setup=[f"Log in to Make, create a scenario and add {trig_mod} as the trigger.",
                       f"Connect {tn}: {tc}." + (" " + INSTANT.strip() if trig in HAS_INSTANT_NOTE else ""),
                       f"Add {act_mod}. Connect {an}: {ac}.",
                       fill, RUN])

def zap(trig_app, trig_event, act_app, act_what):
    return dict(setup_src=("Zapier", ZAP_TRIGGER[1]), extra_sources=[ZAP_TRIGGER, ZAP_BASICS],
                setup=["In Zapier, click + Create in the left sidebar and select Zap workflows to open the Zap editor.",
                       f"Select the Trigger step, search for {trig_app} and choose the trigger event{trig_event}. In the Account field, pick your {trig_app} account or click Connect a new account.",
                       "Click the Test tab, click Test trigger and continue with one of the test records.",
                       f"Add the action: choose {act_app}, pick the event that {act_what}, connect the account and map fields from the trigger into it.",
                       "Test the action, then publish the Zap to turn it on. It only processes data created after it's published."])

SETUP21 = {
 "airtable-and-quickbooks": make("airtable", "the Airtable module Watch Records", "quickbooks", "the QuickBooks module Create an Invoice",
                                 "Fill in the invoice's fields with values from the Airtable record."),
 "airtable-and-stripe": make("stripe", "the Stripe module Watch Events", "airtable", "the Airtable module Create a Record",
                             "Fill in the record's fields with values from the Stripe event."),
 "asana-and-quickbooks": make("asana", "an Asana trigger module such as Watch Tasks or Subtasks", "quickbooks", "the QuickBooks module Create an Invoice",
                              "Fill in the invoice's fields with values from the Asana task."),
 "clickup-and-stripe": make("stripe", "the Stripe module Watch Events", "clickup", "a ClickUp module that creates or updates a task",
                            "Fill in the task's fields with values from the Stripe event."),
 "mailchimp-and-airtable": make("airtable", "the Airtable module Watch Records", "mailchimp", "the Mailchimp module Add/Update a Subscriber",
                                "Fill in the subscriber's email address and other fields with values from the Airtable record."),
 "monday-and-quickbooks": make("monday", "the monday.com module Watch Board's Column Values", "quickbooks", "the QuickBooks module Create an Invoice",
                               "Fill in the invoice's fields with values from the monday.com item."),
 "notion-and-calendly": make("calendly", "the Calendly module Watch events", "notion", "a Notion module that creates a database item",
                             "Fill in the database item's properties with values from the Calendly event."),
 "notion-and-stripe": make("stripe", "the Stripe module Watch Events", "notion", "a Notion module that creates a database item",
                           "Fill in the database item's properties with values from the Stripe event."),
 "pipedrive-and-calendly": make("calendly", "the Calendly module Watch events", "pipedrive", "the Pipedrive CRM module Create a Person or Create an Activity",
                                "Fill in the person's or activity's fields with values from the Calendly event."),
 "pipedrive-and-xero": make("pipedrive", "the Pipedrive CRM module Watch Deals", "xero", "the Xero module Create an Invoice",
                            "Fill in the invoice's fields with values from the deal."),
 "stripe-and-quickbooks": make("stripe", "the Stripe module Watch Events", "quickbooks", "a QuickBooks module such as Create a Sales Receipt or Create a Payment",
                               "Fill in its fields with values from the Stripe event."),
 "xero-and-activecampaign": make("xero", "the Xero module Watch Contacts or Watch Invoices", "activecampaign", "an ActiveCampaign module that creates or updates a contact",
                                 "Fill in the contact's fields with values from Xero."),
 "zendesk-and-stripe": make("stripe", "the Stripe module Watch Events", "zendesk", "a Zendesk module that creates or updates a ticket",
                            "Fill in the ticket's fields with values from the Stripe event."),
 # no example automation on this page, so the steps name one direction only as an example
 "hubspot-and-pipedrive": dict(setup_src=("Make", make_src("pipedrive")[1]), extra_sources=[make_src("pipedrive"), make_src("hubspot"), MAKE_ACTIVE, MAKE_SCHEDULE],
   setup=["Log in to Make and create a scenario. Add a trigger module from the CRM you want to watch, for example the Pipedrive CRM module Watch Deals.",
          f"Connect Pipedrive: {APPS['pipedrive'][2]}.",
          f"Add a HubSpot CRM module for the action. Connect HubSpot: {APPS['hubspot'][2]}.",
          "Fill in the action module's fields with values from the trigger.",
          RUN + " Each scenario runs one way, so build a second one if you need the other direction."]),
 "asana-and-mailchimp": zap("Asana", ", for example New Task", "Mailchimp", "adds or updates a subscriber"),
 "quickbooks-and-slack": zap("QuickBooks Online", ", for example New Customer", "Slack", "posts a message to a channel"),
 "xero-and-calendly": zap("Calendly", " Invitee Created or Rescheduled", "Xero", "creates a contact or a draft invoice"),
 "zendesk-and-notion": zap("Zendesk", " for a new ticket", "Notion", "creates a database item or page"),
 "stripe-and-mailchimp": dict(setup_src=("Mailchimp", "https://mailchimp.com/help/connect-disconnect-mailchimp-stripe/"),
   setup=["On the Stripe integration page in your Mailchimp account, click Connect. It's a paid integration: if you don't have a Data Mapper for Mailchimp account, you create one during the connection.",
          "On the Data Mapper for Mailchimp page in the Stripe App Marketplace, click Install app, confirm in the pop-up window and click Continue.",
          "Click Sign in to Mailchimp, log in, review the connection details and click Allow. If you're new to Data Mapper, choose a plan and pay for it at this point.",
          "Select the Mailchimp audience to sync with and the marketing permission to apply (Double opt-in, Transactional or Subscribed), then click Next.",
          "To sync product and purchase data too, enter a nickname for your store and click Next; to sync customers only, click Skip.",
          "Select the customer fields to sync (the email address is required), click Next, review the options and click Sync."]),
}
