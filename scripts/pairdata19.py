# 2026-11-10 (later the same day): numbered setup steps for 19 more native pairs. Each list follows the vendor's own
# setup guide as read on Nov 10, 2026 (the page named in setup_src). Nothing here changes a price, a plan requirement
# or the existing "how it works" text, so each block keeps its own "checked" date; the steps carry their own date.
# Not done, because the vendor's help centre can't be reached from the build environment (help.clickup.com,
# support.monday.com, help.activecampaign.com): activecampaign-and-pipedrive, activecampaign-and-stripe,
# clickup-and-slack, clickup-and-zendesk, monday-and-zendesk, hubspot-and-clickup, hubspot-and-monday.
SETUP19_CHECKED = "Nov 10, 2026"

HS_SYNC = ("HubSpot Knowledge Base: Connect and use HubSpot data sync", "https://knowledge.hubspot.com/integrations/connect-and-use-hubspot-data-sync")
MC_QBO = ("Mailchimp help: Connect or disconnect Mailchimp for QuickBooks Online", "https://mailchimp.com/help/connect-disconnect-quickbooks-online/")

SETUP19 = {
 "asana-and-slack": dict(
   setup_src=("Asana", "https://asana.com/apps/slack"),
   setup=["Sign up for a Slack account and an Asana account if you don't have both.",
          "Install the Asana app for Slack from Asana's Slack page and follow Slack's instructions to authenticate your Asana account.",
          "Type /asana in Slack to list, create, complete or comment on tasks.",
          "Link a Slack channel to an Asana project to get an update in the channel when a task is created or completed."]),
 "freshdesk-and-hubspot": dict(
   setup_src=("HubSpot", HS_SYNC[1]), extra_sources=[HS_SYNC],
   setup=["In HubSpot, click the Marketplace icon in the top navigation bar and select HubSpot Marketplace. You need to be a Super Admin or have App Marketplace permissions.",
          "Search for Freshdesk, open the app and click Install.",
          "In the dialog box, click Next and log in to Freshdesk. Review the requested access permissions and click Allow.",
          "Go to Settings > Integrations > Connected Apps, click the app, then click Set up your sync.",
          "Select the Freshdesk object and the HubSpot object it should sync with, choose the sync direction (both ways, only to HubSpot or only to Freshdesk) and map the fields.",
          "On the Review page, check your rules and click Save and sync. The first sync starts straight away."]),
 "freshdesk-and-slack": dict(
   setup_src=("Freshdesk", "https://support.freshdesk.com/support/solutions/articles/50000001687-simplifying-collaboration-using-the-latest-slack-app"),
   setup=["A Freshdesk admin installs the app first. Freshdesk says the admin must be on a Freshdesk plan that provides API access.",
          "Log in to your Slack workspace and click Apps in the left pane to open the app directory.",
          "Search for Freshdesk and click Add, then click Add to Slack and Allow.",
          "On the app's home page, go to Settings and click Proceed to link your Freshdesk domain.",
          "Enter your Freshdesk domain (for example company.freshdesk.com) and a valid Freshdesk API key, then click OK.",
          "Back in Settings, click Connect to map each Freshdesk group to the Slack channel that should get its ticket notifications."]),
 "hubspot-and-asana": dict(
   setup_src=("HubSpot", "https://knowledge.hubspot.com/workflows/create-asana-tasks-with-workflows"),
   setup=["Connect Asana to your HubSpot account, either from the App Marketplace or from inside a workflow. You need Super Admin or Workflows permissions.",
          "In HubSpot, go to Automation > Workflows (it may sit under More) and open an existing workflow or create a new one.",
          "Click the + icon to add a workflow action.",
          "In the left panel, select Create an Asana task and set up the action.",
          "Click Save. Private Asana projects won't appear in HubSpot, and the Asana user who connected the integration is added as a collaborator on each task."]),
 "hubspot-and-calendly": dict(
   setup_src=("Calendly", "https://calendly.com/help/calendly-hubspot"),
   setup=["In Calendly, go to Automations → Integrations & apps. You need Calendly administrator privileges and HubSpot admin privileges.",
          "Find and select HubSpot, then select Connect HubSpot.",
          "Sign in to HubSpot if prompted. If you have more than one HubSpot account, pick the one to connect and select Choose Account.",
          "Review the requested permissions, tick the checkbox to confirm and select Connect app. You're taken back to Calendly.",
          "In the integration settings, turn on Push Calendly events and contacts to HubSpot, and choose whether to sync events from the entire organization or from specific groups."]),
 "hubspot-and-salesforce": dict(
   setup_src=("HubSpot", "https://knowledge.hubspot.com/salesforce/install-the-hubspot-salesforce-integration"),
   setup=["Check the Salesforce user who will connect it: HubSpot asks for a Salesforce system administrator with the API Enabled, View Setup and Configuration and Download AppExchange Packages permissions, and Modify All on the objects you want to sync.",
          "In HubSpot, click the Marketplace icon in the top navigation bar and select HubSpot Marketplace.",
          "Search for and select the Salesforce app, then click Install.",
          "If you're connecting a Salesforce sandbox, tick Yes, this will connect to a sandbox. Click Install.",
          "In the pop-up window, enter your Salesforce credentials and click Log In. You're sent back to HubSpot.",
          "Records don't sync on their own after installation: import your Salesforce records into HubSpot, or let them sync gradually as records change."]),
 "hubspot-and-stripe": dict(
   setup_src=("HubSpot", "https://knowledge.hubspot.com/payment-processing/connect-your-stripe-account-as-a-payment-processor-in-hubspot"),
   setup=["In HubSpot, go to Revenue > Payments (it may sit under More) and click Set up payments.",
          "Select Integrate with a Stripe payment processing account and click Next.",
          "Choose your company's country, tick the checkbox to agree to the Stripe Payment Processing Terms and click Next.",
          "On Stripe, enter the email address and password for your Stripe account and complete two-factor authentication.",
          "Select a business you've already set up in Stripe (or register your business) and click Connect.",
          "Review your personal and business information and click Agree and submit. You're sent back to HubSpot."]),
 "intercom-and-stripe": dict(
   setup_src=("Intercom", "https://www.intercom.com/help/en/articles/1829591-stripe-app"),
   setup=["Find Stripe in the Intercom App Store and click Install now. You need to be an admin in Stripe; a Stripe developer account can't connect third-party apps.",
          "Connect your Stripe account. To add another account later, go to App Store > Stripe > Settings and click Add new account.",
          "Turn on sync to import your Stripe customer data into Intercom.",
          "In the inbox, click Edit apps in the right sidebar and pin Stripe so agents see billing details next to each conversation."]),
 "mailchimp-and-calendly": dict(
   setup_src=("Calendly", "https://calendly.com/help/calendly-mailchimp"),
   setup=["In Calendly, go to Automations → Integrations & apps.",
          "Find and select Mailchimp, then select Connect Mailchimp.",
          "Sign in to Mailchimp if prompted, review the requested permissions and select Allow. You're taken back to Calendly.",
          "On the Mailchimp page in Calendly, select Create a Rule for the event you want to automate and choose the event type.",
          "Select the Mailchimp audience to add invitees to, add tags if you want them, and select Save."]),
 "quickbooks-and-mailchimp": dict(
   setup_src=("Mailchimp", MC_QBO[1]), extra_sources=[MC_QBO],
   setup=["In Mailchimp, open the integrations directory.",
          "Choose Mailchimp for QuickBooks Online.",
          "Select the Mailchimp audience you want to sync your QuickBooks Online customers to.",
          "Click Connect to QuickBooks, enter your QuickBooks ID and password and click Sign In.",
          "A success message on the integration page confirms the connection. To see the imported contacts, click the Analytics icon and choose Audience."]),
 "salesforce-and-mailchimp": dict(
   setup_src=("Mailchimp", "https://mailchimp.com/help/connect-mailchimp-for-salesforce/"),
   setup=["On Salesforce Professional, ask your Salesforce account executive to enable API access before you install.",
          "Follow the link on Mailchimp's integration page to the Salesforce AppExchange listing and click Get it Now.",
          "Log in with your Trailblazer.me account and click Install in Production.",
          "Agree to the terms and click Confirm and Install, choose Install for All Users and click Install. Approve third-party access when asked.",
          "In Salesforce, open Mailchimp for Salesforce from the App Launcher, click the MC Setup tab and click Login.",
          "Enter your Mailchimp username and password and click Log In. The Mailchimp user needs Manager access or higher."]),
 "salesforce-and-slack": dict(
   setup_src=("Slack", "https://slack.com/help/articles/227838227-Salesforce-apps-for-Slack"),
   setup=["A Salesforce System Administrator first installs and configures the Slack app in Salesforce.",
          "Open the Salesforce page in the Slack Marketplace and click Add to Slack. On the Salesforce app landing page, click Add to Slack again.",
          "Follow the prompts to authenticate your Salesforce account and finish installing the app.",
          "In Slack, click Apps at the top of the left sidebar, then search for and select Salesforce.",
          "On the app's Home tab, click Connect Account. Once the accounts are connected, click Open Slack to return."]),
 "salesforce-and-stripe": dict(
   setup_src=("Stripe", "https://docs.stripe.com/plugins/stripe-connector-for-salesforce/installation-guide"),
   setup=["In Salesforce, make sure Lightning Web Security is enabled under Setup > Session Management > Session Settings.",
          "Open the app's Salesforce AppExchange listing, log in to the org where you want it and click Continue. Stripe recommends choosing Install for Admins Only.",
          "Tick the Approve Third-Party Access box and click Continue to start the installation.",
          "Go to App Launcher > Stripe for Salesforce Platform, click Get Started, then Authorize, and click Allow in the new window.",
          "Enter your Stripe publishable key and restricted access key, then click Add Account.",
          "Pick the Stripe API version, click Install Package to add the extension package, then click Finish."]),
 "salesforce-and-zendesk": dict(
   setup_src=("Zendesk", "https://support.zendesk.com/hc/en-us/articles/4408821555482-Connecting-your-Salesforce-organization-to-Zendesk"),
   setup=["In Salesforce Setup, open Security > Session Settings and clear the Lock sessions to the IP address from which they originated checkbox. Otherwise the integration disconnects when a session expires.",
          "In Zendesk Admin Center, click Apps and integrations, select Integrations > Integrations and click Salesforce.",
          "Choose the Salesforce instance, Production or Sandbox. Zendesk suggests testing with sandboxes first.",
          "Tick the checkbox to agree to the Built by Zendesk Terms of Use and click Connect Salesforce.",
          "Sign in to Salesforce with admin credentials. You're sent back to Admin Center, where the new connection appears with every feature still inactive.",
          "Click the options menu next to the Salesforce organization and click Configure to turn on the features you plan to use."]),
 "slack-and-airtable": dict(
   setup_src=("Airtable", "https://support.airtable.com/docs/receiving-base-activity-notifications-in-slack"),
   setup=["Open the Airtable base you want notifications from.",
          "Click the drop-down arrow next to the base name, then the ellipsis (…) icon, and select Slack notifications.",
          "Choose the base to post updates from and the Slack channel to post them to.",
          "Click Allow if an authorization window appears.",
          "Send a test message from the rule, or change something in the base and watch the channel for the update."]),
 "slack-and-calendly": dict(
   setup_src=("Calendly", "https://calendly.com/help/calendly-slack"),
   setup=["Sign in to Slack and open the Slack app directory.",
          "Find Calendly, select Add to Slack and then Allow.",
          "Select Connect to Calendly, then Open Slack to return to the app. A welcome message from the Calendly app confirms the setup.",
          "Teammates connect their own accounts: in Slack, go to Apps, select + and search for Calendly, open its Home page and select Connect.",
          "To share a link, type /Calendly in a channel or direct message, select Share an event type with Calendly and choose the event type. Sharing doesn't work inside threads."]),
 "slack-and-intercom": dict(
   setup_src=("Intercom", "https://www.intercom.com/help/en/articles/11534476-connect-your-slack-channel"),
   setup=["In Intercom, go to Settings > Channels > Slack.",
          "Authenticate your Slack workspace. The app can't be installed in the primary workspace of a Slack Enterprise Grid account, only in the secondary workspaces.",
          "Select Add channels, search for the channel you want to connect and tick its checkbox.",
          "Click Add channels to save. The workspace and its channels now appear under Settings > Channels > Slack."]),
 "slack-and-notion": dict(
   setup_src=("Notion", "https://www.notion.com/help/slack"),
   setup=["In Notion, select ••• at the top of the database you want alerts from.",
          "Select Automations, then Add trigger.",
          "Choose Page added or Property edited, then Send Slack notification to...",
          "Select a Slack channel. If you haven't connected Slack yet, Notion asks you to connect your account at this point."]),
 "stripe-and-xero": dict(
   setup_src=("Xero", "https://central.xero.com/0/article/Stripe-AU"),
   setup=["In Xero, open the Sales menu and select Online payments. You need the administrator or standard user role.",
          "Click Add a Stripe account. If online payments are already set up, use the Add a new service tab instead.",
          "Under Cards and digital wallets, click Set up cards & digital wallets, then choose Sign up for Stripe or I have a Stripe account.",
          "Follow the steps on Stripe's website to log in or sign up.",
          "Back in Xero, select the bank account for Stripe payouts and click Continue.",
          "Create an expense account for Stripe fees or pick an existing one, click Complete set up, then Save. Stripe is added to your invoice templates automatically."]),
}

# Later on Nov 10, 2026: the step lists written in earlier rounds were compared with that day's version of the guide
# they came from. RECHECK19 names the guide for each list that matched; these pages get the same dated line under
# their steps. Two lists are left out: monday-and-slack (monday.com's help centre can't be reached, and its
# integration page has no steps) and pipedrive-and-calendly (an outline of the options, not one vendor's guide).
RECHECK19 = {
 "activecampaign-and-calendly": ("Calendly", "https://calendly.com/help/calendly-activecampaign"),
 "hubspot-and-mailchimp": ("HubSpot", "https://knowledge.hubspot.com/forms/connect-non-hubspot-forms-to-mailchimp"),
 "hubspot-and-quickbooks": ("HubSpot", "https://knowledge.hubspot.com/integrations/connect-hubspot-and-quickbooks-online"),
 "hubspot-and-slack": ("HubSpot", "https://knowledge.hubspot.com/integrations/how-do-i-use-the-slack-integration"),
 "hubspot-and-zendesk": ("Zendesk", "https://support.zendesk.com/hc/en-us/articles/4408884090650-Setting-up-the-Zendesk-Support-for-HubSpot-integration"),
 "intercom-and-hubspot": ("Intercom", "https://www.intercom.com/help/en/articles/2128216-hubspot-app"),
 "pipedrive-and-mailchimp": ("Pipedrive", "https://support.pipedrive.com/en/article/pipedrive-integration-mailchimp-sync"),
 "pipedrive-and-quickbooks": ("Pipedrive", "https://support.pipedrive.com/en/article/pipedrive-integration-quickbooks"),
 "pipedrive-and-salesforce": ("Make", "https://apps.make.com/salesforce"),
 "pipedrive-and-slack": ("Pipedrive", "https://support.pipedrive.com/en/article/workflow-automation-slack-notifications"),
 "salesforce-and-quickbooks": ("Make", "https://apps.make.com/salesforce"),
 "slack-and-zendesk": ("Zendesk", "https://support.zendesk.com/hc/en-us/articles/4408833756698-Understanding-and-installing-the-Slack-for-Zendesk-Support-integration"),
 "stripe-and-slack": ("Stripe", "https://docs.stripe.com/use-stripe-apps/stripe-workflows-slack"),
}
# Steps reworded where the guide is more specific than the old text (0-based index -> new text).
MAKE_SF_CONNECT = ("add a Salesforce module and click Create a connection. Choose the connection type, say whether it's a Salesforce sandbox and click Save")
STEP_FIX19 = {
 # HubSpot only asks you to map emails when your HubSpot and Slack addresses differ
 "hubspot-and-slack": {3: "If your HubSpot email differs from your Slack email, HubSpot asks you to map the two: enter your Slack email, click Verify in Slack, then click Verify in the message the HubSpot app sends you in Slack."},
 "pipedrive-and-salesforce": {1: f"In Make, create a scenario, {MAKE_SF_CONNECT}. Connect your Pipedrive account the same way."},
 "salesforce-and-quickbooks": {1: f"In Make, create a scenario, {MAKE_SF_CONNECT}. Connect your QuickBooks account the same way."},
}
