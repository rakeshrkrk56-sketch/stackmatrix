# 2026-11-03 Xero + Calendly re-check. Zapier Xero prerequisites: "A paid Xero account. Standard or Adviser level user
# permissions in your Xero organization. A paid Zapier plan." and "Organizations using Xero's "Starter" pricing plan can
# only enter up to 20 approved Accounts Receivable invoices and 5 approved Accounts Payable invoices per month via the API."
ZAP = "Zapier Professional ($29.99/mo, or $19.99/mo billed annually)"
PAIRS11 = {
 "xero-and-calendly": dict(native=False, req={"xero": "Early", "calendly": "Standard"}, sync="1-way (trigger → action)",
   summary="There's no native Calendly–Xero integration, so Zapier Professional bridges bookings into Xero; Calendly's webhooks need its Standard plan, and Zapier needs only a paid Xero account. Requires Xero on the 'Early' plan and Calendly on the 'Standard' plan. Route it through " + ZAP + "."),
}
COPY11 = {
 "xero-and-calendly": dict(
   how="Calendly and Xero don't have a native integration. Zapier, Make and similar tools connect them, for example creating a Xero contact or a draft invoice when someone books a Calendly meeting.",
   limits="Calendly's webhooks need a paid plan from Standard up. Zapier needs a paid Xero account, Standard or Adviser permissions in Xero and a paid Zapier plan, because Xero is a premium app on Zapier. On Xero's Early plan you can enter up to 20 approved sales invoices and 5 bills a month through the API, so if each booking creates an invoice and you take more than 20 bookings a month, you'll need Growing ($59/mo).",
   sources=[("Zapier: Get started with Xero", "https://help.zapier.com/hc/en-us/articles/38844152391821-How-to-get-started-with-Xero-on-Zapier"),
            ("Calendly: API overview", "https://calendly.com/help/calendly-api-overview"), ("Xero: US pricing plans", "https://www.xero.com/us/pricing-plans/")]),
}
