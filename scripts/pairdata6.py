# High-severity fixes from the post-update audit (checked 2026-11-03).
SLACK_FREE = None
PAIRS6 = {
 # Data Mapper pricing page: $15/month billed monthly ($12.75/month billed annually), 30-day free trial.
 "stripe-and-mailchimp": dict(native=False, mw=15, cta=False, req={"mailchimp": "Free"}, sync="1-way (Stripe → Mailchimp)",
   summary="Mailchimp's Stripe connection runs through Data Mapper for Mailchimp, a third-party app that costs $15/mo billed monthly and works with any Mailchimp plan, including Free. Requires Stripe on the 'Standard' plan and Mailchimp on the 'Free' plan. Route it through Data Mapper for Mailchimp ($15/mo)."),
 # No native Airtable–Mailchimp sync (Mailchimp's directory lists third-party sync tools; Airtable has no listing).
 "mailchimp-and-airtable": dict(native=False, mw=9, req={"mailchimp": "Essentials", "airtable": "Free"}, sync="1-way (trigger → action)",
   summary="There's no native Airtable–Mailchimp sync; Make Core ($9/mo) or a third-party sync app connects them, and Airtable's webhooks work on every plan, including Free. Requires Mailchimp on the 'Essentials' plan and Airtable on the 'Free' plan. Route it through Make Core ($9/mo)."),
 # No first-party Calendly–Pipedrive integration; third-party Marketplace apps or Make/Zapier.
 "pipedrive-and-calendly": dict(native=False, mw=9, req={}, sync="1-way (trigger → action)",
   summary="Neither Pipedrive nor Calendly builds a native integration; third-party Pipedrive Marketplace apps or Make connect them, and Calendly's webhooks need its Standard plan. Requires Pipedrive on the 'Lite' plan and Calendly on the 'Standard' plan. Route it through Make Core ($9/mo)."),
}
COPY6 = {
 "mailchimp-and-airtable": dict(
   how="Airtable and Mailchimp don't have a native integration. Teams connect them with an automation tool such as Make or Zapier, for example adding a Mailchimp contact when an Airtable record is created, or with a dedicated sync app such as Syncgrip or Unito, which Mailchimp lists in its integrations directory.",
   limits="Each Make or Zapier scenario runs one way, so two-way sync needs a second automation or a dedicated sync app, which is a separate paid product. Airtable's webhooks are available on all plans; this calculator assumes Mailchimp's Essentials plan.",
   sources=[("Mailchimp: Syncgrip integration", "https://mailchimp.com/integrations/syncgrip/"), ("Mailchimp: Unito integration", "https://mailchimp.com/integrations/unito/"), ("Airtable: Create a webhook", "https://airtable.com/developers/web/api/create-a-webhook")]),
 "pipedrive-and-calendly": dict(
   how="Pipedrive and Calendly don't build a native integration with each other. Third-party apps on the Pipedrive Marketplace, such as Outfunnel's Calendly Sync and Ulgebra's Calendly Events for Pipedrive, add Calendly bookings to Pipedrive, and Calendly's own integration directory lists Outfunnel for this. Make or Zapier can do the same.",
   limits="These apps aren't made by Pipedrive or Calendly, so check each one's pricing and support before relying on it. Calendly's webhooks, which real-time automations use, need a paid Calendly plan from Standard up.",
   sources=[("Calendly: Outfunnel integration", "https://calendly.com/integration/outfunnel"), ("Pipedrive Marketplace: Calendly Sync", "https://www.pipedrive.com/en/marketplace/app/calendly-sync/0356741bcb89ba03"), ("Calendly: API overview", "https://calendly.com/help/calendly-api-overview")]),
}
COPY6_PATCH = {
 "stripe-and-mailchimp": [
   ("Mailchimp calls it a paid integration: you need a Data Mapper for Mailchimp subscription on top of your Mailchimp plan, and that cost isn't included in the calculator above. Mailchimp lists any Mailchimp Marketing Platform plan as compatible.",
    "Mailchimp calls it a paid integration: Data Mapper for Mailchimp costs $15/month billed monthly ($12.75/month billed annually) after a 30-day free trial, on top of your Mailchimp plan. The calculator includes it as the $15/month connector fee. Mailchimp lists any Mailchimp Marketing Platform plan as compatible."),
 ],
}
COPY6_SOURCES = {"stripe-and-mailchimp": [("Data Mapper for Mailchimp: Pricing", "https://data-mapper-for-mailchimp.thisdot.co/pricing")]}
