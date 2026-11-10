# 2026-11-10: search-intent round. Vendor pages read today:
#  - docs.stripe.com/use-stripe-apps/stripe-workflows-slack (install, connect, /invite @Stripe, Test, workflow action)
#  - knowledge.hubspot.com/salesforce/install-the-hubspot-salesforce-integration ("Have a Salesforce edition with API
#    access, or Salesforce Professional ... does not support Salesforce Group Edition"), read Nov 5
#  - developer.salesforce.com packaging guide, "API Access in Group and Professional Editions" ("after your app passes
#    the security review ... your app can make calls to Group and Professional Edition orgs ... even if the customer
#    doesn't have API access")
#  - hubspot.com/pricing (one-time Professional Onboarding: $1,500 Sales/Service Hub, $3,000 Marketing Hub; none shown
#    for Smart CRM Professional), read Nov 5
# PATCH18 adds fields to existing copy blocks; nothing here changes a price or a plan requirement.
SF_PKG = ("Salesforce developers: API access in Group and Professional Editions",
          "https://developer.salesforce.com/docs/atlas.en-us.packagingGuide.meta/packagingGuide/dev_packages_api_access.htm")
HS_PRICING = ("HubSpot pricing", "https://www.hubspot.com/pricing")
ONBOARD = ("HubSpot charges a required one-time Professional Onboarding fee on some Hubs ($1,500 for Sales Hub or Service Hub, $3,000 for Marketing Hub; "
           "its pricing page shows none for Smart CRM Professional). It isn't in the monthly totals here, so add it under one-time setup cost in the calculator.")

PATCH18 = {
 "stripe-and-slack": dict(
   answer="Yes. Stripe builds its own Slack app, Stripe Workflows for Slack, which posts a Slack message when something happens in Stripe, such as a payment, a new subscription or a dispute. It works with Slack's free plan, so you don't need Zapier or Make for notifications.",
   setup=["In the Stripe App Marketplace, open the Slack app page, pick your account and click Install.",
          "Open the app from Stripe's right sidebar, go to its settings page and click Add to Slack. Choose your workspace and click Allow.",
          "In Slack, type /invite @Stripe in each channel that should get notifications. Back in the app settings, click Test next to the channel to send a test message.",
          "In Stripe, open Workflows and click Create workflow. Add your trigger, then click Add a step, choose Add action and pick Send Slack Notification.",
          "Choose the Slack channel, write the message template (the + button inserts details from the event) and decide whether to include a Dashboard link. Click Publish."],
   cta=("Set up Stripe Workflows for Slack", "https://docs.stripe.com/use-stripe-apps/stripe-workflows-slack"),
   checked="Nov 10, 2026"),
 "hubspot-and-salesforce": dict(
   note=ONBOARD + " On the Salesforce side, HubSpot's requirements read \"a Salesforce edition with API access, or Salesforce Professional\" (Group Edition isn't supported), and Salesforce says security-reviewed AppExchange apps can reach Professional orgs even if the customer doesn't have API access. So ask Salesforce whether your org needs the API add-on for HubSpot's connector before paying for it; the totals here include it.",
   extra_sources=[SF_PKG, HS_PRICING]),
 "hubspot-and-asana": dict(note=ONBOARD, extra_sources=[HS_PRICING]),
}
