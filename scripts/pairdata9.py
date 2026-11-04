# 2026-11-03 QuickBooks requirement re-check. Zapier: "A paid QuickBooks Online subscription. Admin permissions
# in your QuickBooks Online account. A paid Zapier plan." Make: "you must have a QuickBooks account". Mailchimp:
# "You will need a QuickBooks Online account to use the features of this integration." Stripe: QuickBooks
# integrations are "Stripe Apps built by 3rd party developers" (QuickBooks Sync by Acodei). No connector names a tier.
import pairdata7
MAKE = "Make Core ($10.59/mo, or $9/mo billed annually)"
ZAP = "Zapier Professional ($29.99/mo, or $19.99/mo billed annually)"
QB = {"quickbooks": "Simple Start"}
PAIRS9 = {
 "airtable-and-quickbooks": dict(native=False, req={"airtable": "Team", **QB}, sync="1-way (trigger → action)",
   summary="Make Core can bridge Airtable and QuickBooks invoices with any QuickBooks Online plan, but Airtable's Free plan allows only 1,000 API calls a month, too few for an ongoing sync, so this models Airtable Team. Requires Airtable on the 'Team' plan and QuickBooks Online on the 'Simple Start' plan. Route it through " + MAKE + "."),
 "asana-and-quickbooks": dict(native=False, req={"asana": "Starter", **QB}, sync="1-way (trigger → action)",
   summary="No native Asana–QuickBooks link; Make Core connects them through Asana's API, whose webhooks aren't limited to a higher Asana plan, and Make needs only a QuickBooks account. Requires Asana on the 'Starter' plan and QuickBooks Online on the 'Simple Start' plan. Route it through " + MAKE + "."),
 "monday-and-quickbooks": dict(native=False, req={"monday": "Standard", **QB}, sync="1-way (trigger → action)",
   summary="No native connector; monday.com includes integrations from its Standard plan, with 250 integration actions a month (Pro raises this to 25,000), and Make works with any QuickBooks plan. Requires Monday.com on the 'Standard' plan and QuickBooks Online on the 'Simple Start' plan. Route it through " + MAKE + "."),
 "quickbooks-and-mailchimp": dict(native=True, req={**QB, "mailchimp": "Free"}, sync="1-way (QuickBooks → Mailchimp)",
   summary="Mailchimp's own QuickBooks Online integration syncs QuickBooks customers into a Mailchimp audience, one way and with no middleware; it needs only a QuickBooks Online account and works on Mailchimp's free plan. Requires QuickBooks Online on the 'Simple Start' plan and Mailchimp on the 'Free' plan."),
 "quickbooks-and-slack": dict(native=False, req={**QB, "slack": "Free"}, sync="1-way (trigger → action)",
   summary="No official QuickBooks Online app for Slack, so alerts run through " + ZAP + ", which needs a paid QuickBooks Online plan but no particular one; Slack's free plan is enough. Requires QuickBooks Online on the 'Simple Start' plan and Slack on the 'Free' plan. Route it through " + ZAP + "."),
 "stripe-and-quickbooks": dict(native=False, req={"stripe": "Standard", **QB}, sync="1-way (Stripe → QuickBooks)",
   summary="Stripe has no native QuickBooks Online connector: its QuickBooks integrations are third-party apps such as QuickBooks Sync by Acodei, or Make Core, and none needs more than a basic QuickBooks plan. Requires Stripe on the 'Standard' plan and QuickBooks Online on the 'Simple Start' plan. Route it through " + MAKE + "."),
}
pairdata7.MW7["stripe-and-quickbooks"] = pairdata7.MAKE
pairdata7.SUMMARY7["airtable-and-quickbooks"] = PAIRS9["airtable-and-quickbooks"]["summary"]
SRC_ZAP = ("Zapier: Get started with QuickBooks Online", "https://help.zapier.com/hc/en-us/articles/8495935103885")
SRC_MAKE = ("Make: QuickBooks app", "https://apps.make.com/quickbooks")
COPY9 = {
 "quickbooks-and-mailchimp": dict(
   how="Mailchimp's QuickBooks Online integration, listed in Mailchimp's integrations directory, syncs data from QuickBooks Online into Mailchimp, including contacts and purchase data, so you can segment and email your QuickBooks customers. Data flows one way, from QuickBooks to Mailchimp.",
   limits="Mailchimp's stated requirement is a QuickBooks Online account, with no particular QuickBooks plan, so this calculator models Simple Start, QuickBooks' cheapest plan. Mailchimp notes that features vary by Mailchimp plan.",
   sources=[("Mailchimp: QuickBooks Online integration", "https://mailchimp.com/integrations/quickbooksonline/")]),
 "quickbooks-and-slack": dict(
   how="There's no official QuickBooks Online app for Slack. Zapier connects them, for example posting a Slack message when a new invoice or customer is added in QuickBooks.",
   limits="Zapier needs a paid QuickBooks Online subscription, admin permissions in QuickBooks and a paid Zapier plan, because QuickBooks Online is a premium app on Zapier. No specific QuickBooks plan is required, so this calculator models Simple Start. QuickBooks limits its API to 500 requests per minute per company.",
   sources=[SRC_ZAP]),
 "stripe-and-quickbooks": dict(
   how="Stripe doesn't build a native QuickBooks Online connector. Stripe's documentation says its QuickBooks Online integrations are Stripe Apps built by third-party developers, such as QuickBooks Sync by Acodei, which syncs Stripe transactions, fees, payouts and customers into QuickBooks. Make or Zapier can connect them too.",
   limits="Third-party sync apps have their own pricing, which isn't included here; this calculator models Make Core instead. Make only requires a QuickBooks account, so QuickBooks Simple Start is enough. Data flows one way, from Stripe into QuickBooks.",
   sources=[("Stripe: Accounting integrations", "https://docs.stripe.com/stripe-apps/embedded-apps/accounting-integrations"), SRC_MAKE,
            ("Stripe Partners: Acodei", "https://stripe.partners/directory/quickbooks-online-sync-by-acodei")]),
}
COPY9_EXTRA_SOURCES = {"airtable-and-quickbooks": [SRC_MAKE], "asana-and-quickbooks": [SRC_MAKE], "monday-and-quickbooks": [SRC_MAKE]}
# byline status after the re-check: these become fully verified
VERIFIED9 = {"asana-and-quickbooks", "monday-and-quickbooks", "stripe-and-quickbooks"}
