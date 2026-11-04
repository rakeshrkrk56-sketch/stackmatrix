# Price/plan-name update for Pipedrive and Xero (checked 2026-11-03).
# Xero US pricing page (xero.com/us/pricing-plans): Early $27, Growing $59, Established $97 per month (flat per org).
# Pipedrive pricing page (pipedrive.com/en/pricing, via search index; page blocks automated fetches):
#   Lite $14, Growth $39, Premium $59, Ultimate $79 per seat per month, billed annually (same basis as the old data).
TOOL_TIERS = {
 "pipedrive": [{"tier_name": "Lite", "base": 0, "perSeat": 14, "minSeats": 1, "api": True},
               {"tier_name": "Growth", "base": 0, "perSeat": 39, "minSeats": 1, "api": True},
               {"tier_name": "Premium", "base": 0, "perSeat": 59, "minSeats": 1, "api": True},
               {"tier_name": "Ultimate", "base": 0, "perSeat": 79, "minSeats": 1, "api": True}],
 "xero": [{"tier_name": "Early", "base": 27, "perSeat": 0, "minSeats": 1, "api": True},
          {"tier_name": "Growing", "base": 59, "perSeat": 0, "minSeats": 1, "api": True},
          {"tier_name": "Established", "base": 97, "perSeat": 0, "minSeats": 1, "api": True}],
}
RENAME = {"pipedrive": {"Essential": "Lite", "Advanced": "Growth", "Professional": "Premium", "Enterprise": "Ultimate"},
          "xero": {"Starter": "Early", "Standard": "Growing"}}

PAIRS3 = {
 "activecampaign-and-pipedrive": dict(native=True, req={"activecampaign": "Starter", "pipedrive": "Growth"}, sync="2-way",
   summary="ActiveCampaign's native Pipedrive integration is included on every ActiveCampaign plan: it imports Pipedrive contacts and can push contacts to Pipedrive from an automation. Requires ActiveCampaign on the 'Starter' plan and Pipedrive on the 'Growth' plan."),
 "hubspot-and-pipedrive": dict(native=False, req={"hubspot": "Free", "pipedrive": "Lite"}, sync="1-way (trigger → action)",
   summary="Pipedrive opens its REST API on every plan including Lite ($14/seat), and HubSpot Free includes API access — so middleware (Make or Zapier) syncs contacts and deals both ways without forcing a tier upgrade on either side. Minimum viable stack: HubSpot 'Free' + Pipedrive 'Lite' + ~$9/mo middleware."),
 "pipedrive-and-calendly": dict(native=True, req={"pipedrive": "Lite"}, sync="2-way",
   summary="Booked meetings create activities automatically. Requires Pipedrive on the 'Lite' plan and Calendly on the 'Standard' plan for full 2-way sync."),
 "pipedrive-and-mailchimp": dict(native=True, req={"pipedrive": "Lite"}, sync="2-way",
   summary="Pipedrive's native Mailchimp integration exports Pipedrive contacts to Mailchimp, and Pipedrive's newer Mailchimp sync adds two-way flows. Requires Pipedrive on the 'Lite' plan and Mailchimp on the 'Essentials' plan."),
 "pipedrive-and-slack": dict(native=True, req={"pipedrive": "Growth", "slack": "Free"}, sync="1-way (Pipedrive → Slack)",
   summary="Trap: Pipedrive sends Slack messages through its Automations feature, which is only on Growth and higher ($39/seat). Requires Pipedrive on the 'Growth' plan and Slack on the 'Free' plan."),
 "pipedrive-and-xero": dict(native=True, req={"pipedrive": "Lite", "xero": "Early"}, sync="2-way",
   summary="Invoices generate from won deals and their status in Pipedrive follows Xero; multi-currency needs Xero's top Established plan ($97/mo). Requires Pipedrive on the 'Lite' plan and Xero on the 'Early' plan."),
 "stripe-and-xero": dict(native=True, req={"xero": "Early"}, sync="2-way",
   summary="Xero accepts online invoice payments through Stripe on its cheapest Early plan; multi-currency needs Xero's top Established plan ($97/mo). Requires Stripe on the 'Standard' plan and Xero on the 'Early' plan."),
 "xero-and-activecampaign": dict(native=False, req={"xero": "Growing"}, sync="1-way (trigger → action)",
   summary="Invoice-paid triggers email sequences through Make Core. Requires Xero on the 'Growing' plan and ActiveCampaign on the 'Starter' plan for full 1-way (trigger → action) sync. Route it through Make Core ($9/mo)."),
 "xero-and-calendly": dict(native=False, req={"xero": "Growing", "calendly": "Standard"}, sync="1-way (trigger → action)",
   summary="Calendly webhooks need a paid plan from Standard up, not Teams, so Zapier Starter can bridge bookings into Xero. Requires Xero on the 'Growing' plan and Calendly on the 'Standard' plan. Route it through Zapier Starter ($19.99/mo)."),
}

COPY3_PATCH = {  # text replacements inside existing copy entries
 "pipedrive-and-slack": ("Pipedrive says Automations are only available on Advanced and higher plans, so the cheapest plan can't send Slack messages this way.",
                         "Pipedrive says Automations are only available on Growth and higher plans (Advanced under its older plan names), so the cheapest Lite plan can't send Slack messages this way."),
 "stripe-and-xero": ("Xero's cheapest plan accepts online invoice payments but limits you to 20 invoices, and using multiple currencies needs the top Established plan.",
                     "Xero's cheapest Early plan ($27/mo) accepts online invoice payments but limits you to 20 invoices, and using multiple currencies needs the top Established plan ($97/mo)."),
}
