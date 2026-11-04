# 2026-11-03: required tiers that rested on disproved webhook gates (see API-WEBHOOK-VERIFICATION.md).
MAKE = "Make Core ($10.59/mo, or $9/mo billed annually)"
ZAP = "Zapier Professional ($29.99/mo, or $19.99/mo billed annually)"
PAIRS8 = {
 "asana-and-quickbooks": dict(native=False, req={"asana": "Starter"}, sync="1-way (trigger → action)",
   summary="No native Asana–QuickBooks link; Make Core connects them through Asana's API, whose webhooks aren't limited to a higher Asana plan, so Starter is enough. Requires Asana on the 'Starter' plan and QuickBooks Online on the 'Plus' plan. Route it through " + MAKE + "."),
 "notion-and-stripe": dict(native=False, req={"notion": "Plus"}, sync="1-way (trigger → action)",
   summary="No native link - Make Core watches Stripe and logs payments to a Notion database through Notion's API, which isn't limited to a higher Notion plan; this models Plus, Notion's first paid team plan. Requires Notion on the 'Plus' plan and Stripe on the 'Standard' plan. Route it through " + MAKE + "."),
 "monday-and-quickbooks": dict(native=False, req={"monday": "Standard"}, sync="1-way (trigger → action)",
   summary="No native connector; monday.com includes integrations from its Standard plan, with 250 integration actions a month (Pro raises this to 25,000). Requires Monday.com on the 'Standard' plan and QuickBooks Online on the 'Plus' plan. Route it through " + MAKE + "."),
 "zendesk-and-notion": dict(native=False, req={"zendesk": "Suite Team"}, sync="1-way (trigger → action)",
   summary="No native docs link - Zapier Professional pushes resolved tickets to a Notion knowledge base; Zendesk's triggers and webhooks are on every Suite plan from Team up. Requires Zendesk on the 'Suite Team' plan and Notion on the 'Plus' plan. Route it through " + ZAP + "."),
}
# pending -> partial (integration requirements re-checked today, one plan still unconfirmed)
PARTIAL8 = {"asana-and-quickbooks": "QuickBooks plan unconfirmed", "notion-and-stripe": "Notion plan unconfirmed",
            "monday-and-quickbooks": "QuickBooks plan unconfirmed", "zendesk-and-notion": "Notion plan unconfirmed"}
