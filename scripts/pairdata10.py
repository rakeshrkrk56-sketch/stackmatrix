# 2026-11-03 Xero + ActiveCampaign re-check. ActiveCampaign's listing: "Middleware App ... Xero and ActiveCampaign
# together, enabled by the power of Zapier", included with Starter/Plus/Professional/Enterprise. Make: "To use the
# Xero modules, you must have a Xero account." Xero US pricing: Early includes "Send quotes and 20 invoices",
# "Accept online invoice payments", "5 bills".
MAKE = "Make Core ($10.59/mo, or $9/mo billed annually)"
PAIRS10 = {
 "xero-and-activecampaign": dict(native=False, req={"xero": "Early", "activecampaign": "Starter"}, sync="1-way (trigger → action)",
   summary="ActiveCampaign's Xero connection runs through Zapier or Make, not natively; an invoice paid in Xero can start an ActiveCampaign email sequence, and Make needs only a Xero account. Requires Xero on the 'Early' plan and ActiveCampaign on the 'Starter' plan. Route it through " + MAKE + "."),
}
COPY10 = {
 "xero-and-activecampaign": dict(
   how="ActiveCampaign lists Xero as a middleware integration enabled by Zapier, not a native connector. Make or Zapier watches Xero, for example for a new contact or a paid invoice, and adds the contact to ActiveCampaign or starts an automation.",
   limits="Xero's Early plan allows 20 invoices and 5 bills a month; if you send more invoices than that you'll need Growing ($59/mo) regardless of the integration. Each Make or Zapier scenario runs one way. ActiveCampaign lists the integration for all of its plans, from Starter up.",
   sources=[("ActiveCampaign: Xero integration", "https://www.activecampaign.com/apps/xero"), ("Make: Xero app", "https://apps.make.com/xero"),
            ("Xero: US pricing plans", "https://www.xero.com/us/pricing-plans/")]),
}
