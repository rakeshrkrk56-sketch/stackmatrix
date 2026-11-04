# PR #2 pre-approval fixes (approved 2026-11-03).
# 1. Data Mapper: disclose that Starter syncs customers only; purchase sync needs Pro ($30/mo).
# 2. Connector fees on the same basis as tool plans: monthly-billing price + annual-billing price.
#    Zapier Professional: $29.99 paying monthly / $19.99 paying yearly (zapier.com/pricing, both toggles, 2026-11-03).
#    Make Core: $9 billed annually (make.com, Oct 17 check); $10.59 billed monthly per several third-party
#    pricing reviews (make.com blocks automated fetches; $9 / 0.85 = $10.59 matches its ~15% annual discount).
#    Data Mapper Starter: $15 monthly / $12.75 annual (data-mapper-for-mailchimp.thisdot.co/pricing).
# 3. Airtable Free allows 1,000 API calls/month (Team 100,000), too few for an ongoing Make sync -> model Team.
MAKE = (10.59, 9)
ZAPIER = (29.99, 19.99)
MW7 = {p: MAKE for p in ("airtable-and-quickbooks", "airtable-and-stripe", "asana-and-quickbooks", "clickup-and-stripe",
                         "hubspot-and-pipedrive", "mailchimp-and-airtable", "monday-and-quickbooks", "notion-and-calendly",
                         "notion-and-stripe", "pipedrive-and-calendly", "xero-and-activecampaign", "zendesk-and-stripe")}
MW7.update({p: ZAPIER for p in ("asana-and-mailchimp", "quickbooks-and-slack", "xero-and-calendly", "zendesk-and-notion")})
MW7["stripe-and-mailchimp"] = (15, 12.75)

MAKE_TXT = "Make Core ($10.59/mo, or $9/mo billed annually)"
ZAP_TXT = "Zapier Professional ($29.99/mo, or $19.99/mo billed annually)"
# (old, new) replacements applied to every affected summary, in order; each must be idempotent
SUMMARY7_GENERIC = [("Make Core ($9/mo)", MAKE_TXT), ("Zapier Starter ($19.99/mo)", ZAP_TXT), ("Zapier Starter", "Zapier Professional"),
                    ("~$9/mo middleware", "~$10.59/mo middleware ($9/mo billed annually)")]
SUMMARY7 = {
 "airtable-and-stripe": "Airtable's Stripe integration runs through an iPaaS tool such as Make, not natively. Airtable's Free plan allows only 1,000 API calls a month, too few for an ongoing sync, so this models Airtable Team. Requires Airtable on the 'Team' plan and Stripe on the 'Standard' plan. Route it through " + MAKE_TXT + ".",
 "airtable-and-quickbooks": "Make Core can bridge Airtable and QuickBooks invoices without Airtable Business, but Airtable's Free plan allows only 1,000 API calls a month, too few for an ongoing sync, so this models Airtable Team. Requires Airtable on the 'Team' plan and QuickBooks Online on the 'Plus' plan. Route it through " + MAKE_TXT + ".",
 "mailchimp-and-airtable": "There's no native Airtable–Mailchimp sync; Make Core or a third-party sync app connects them. Airtable's Free plan allows only 1,000 API calls a month, too few for an ongoing sync, so this models Airtable Team. Requires Mailchimp on the 'Essentials' plan and Airtable on the 'Team' plan. Route it through " + MAKE_TXT + ".",
 "stripe-and-mailchimp": "Mailchimp's Stripe connection runs through Data Mapper for Mailchimp, a third-party app whose Starter plan costs $15/mo billed monthly and works with any Mailchimp plan, including Free. Starter syncs customers only; purchase-data sync needs Data Mapper Pro ($30/mo). Requires Stripe on the 'Standard' plan and Mailchimp on the 'Free' plan. Route it through Data Mapper for Mailchimp ($15/mo).",
}
REQ7 = {"airtable-and-stripe": {"airtable": "Team"}, "airtable-and-quickbooks": {"airtable": "Team"}, "mailchimp-and-airtable": {"airtable": "Team"}}

AT_SRC = [("Airtable: Managing API call limits", "https://support.airtable.com/articles/7735693959-managing-api-call-limits-in-airtable"),
          ("Airtable: Create a webhook", "https://airtable.com/developers/web/api/create-a-webhook")]
AT_LIMIT = ("Every Make run that reads or writes Airtable uses API calls. Airtable's Free plan allows 1,000 a month and Team 100,000; "
            "a scenario that checks Airtable every 15 minutes uses about 2,880 a month, so this calculator models Team "
            "($24/seat billed monthly, $20 billed annually). Free works only for very low-volume syncs.")
COPY7 = {  # new "How it works" sections
 "airtable-and-stripe": dict(
   how="Airtable and Stripe don't have a native integration. An automation tool such as Make or Zapier connects them, for example adding an Airtable record when a Stripe payment succeeds or a customer is created.",
   limits="Each Make or Zapier scenario runs one way. " + AT_LIMIT,
   sources=AT_SRC),
 "airtable-and-quickbooks": dict(
   how="Airtable and QuickBooks Online don't have a native integration. An automation tool such as Make or Zapier connects them, for example creating a QuickBooks invoice from an Airtable record or logging paid invoices back in Airtable.",
   limits="Each Make or Zapier scenario runs one way. " + AT_LIMIT,
   sources=AT_SRC),
}
COPY7_PATCH = {  # (old, new) on existing copy; idempotent
 "mailchimp-and-airtable": [
   ("Airtable's webhooks are available on all plans; this calculator assumes Mailchimp's Essentials plan.",
    "Airtable's webhooks are available on all plans, but " + AT_LIMIT[0].lower() + AT_LIMIT[1:] +
    " It also assumes Mailchimp's Essentials plan, whose $13/month starting price covers up to 500 contacts and rises with your contact count."),
 ],
 "stripe-and-mailchimp": [
   ("with the marketing permission you pick.",
    "with the marketing permission you pick. Data Mapper's Starter plan ($15/month) syncs Stripe customers and tags charge, invoice and quote events; syncing purchase data into a Mailchimp store, for purchase-based journeys and segments, needs its Pro ($30/month) or Ultimate ($60/month) plan."),
   ("Mailchimp lists any Mailchimp Marketing Platform plan as compatible.",
    "Mailchimp lists any Mailchimp Marketing Platform plan as compatible. Data Mapper says its plans are tiered by the number of customer syncs but doesn't publish the limits, and Pro adds unlimited customer syncing. Purchase sync also needs a Mailchimp store and products created in Stripe."),
 ],
}
COPY7_SOURCES = {
 "mailchimp-and-airtable": [("Airtable: Managing API call limits", "https://support.airtable.com/articles/7735693959-managing-api-call-limits-in-airtable"),
                            ("Mailchimp: About pricing plans", "https://mailchimp.com/help/about-mailchimp-pricing-plans/")],
 "stripe-and-mailchimp": [("Data Mapper: Sync your customer purchases", "https://thisdot.gitbook.io/data-mapper-for-mailchimp/e-commerce/sync-your-customer-purchases"),
                          ("Data Mapper: Choosing a plan", "https://thisdot.gitbook.io/data-mapper-for-mailchimp/getting-started/choosing-a-plan")],
}
