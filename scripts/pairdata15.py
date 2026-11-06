# 2026-11-05: HubSpot plan prices, re-read on hubspot.com/pricing (each Hub's page, billing toggles clicked).
# HubSpot's knowledge base lists the Salesforce connector and the "Create an Asana task" workflow action as
# "Available with ... Marketing Hub / Sales Hub / Service Hub / Data Hub / Content Hub / Smart CRM: Professional,
# Enterprise", so ANY Professional subscription unlocks them. The cheapest one is Smart CRM Professional:
# $50/seat/mo paid monthly, $45/seat/mo with an annual commitment. The site previously modeled "Professional" as a
# flat $800/mo (Marketing Hub Professional on an annual commitment, which includes only 3 seats).
# Smart CRM Enterprise: $75/seat/mo, annual commitment only ("Talk to Sales").
# Starter is unchanged at its $20/seat regular price (HubSpot currently shows a limited new-customer discount).
HS_CHECKED = "2026-11-05"

TOOL_TIERS15 = {
 "hubspot": [{"tier_name": "Free", "base": 0, "perSeat": 0, "minSeats": 1, "api": True},
             {"tier_name": "Starter", "base": 0, "perSeat": 20, "minSeats": 1, "api": True},
             {"tier_name": "Professional", "base": 0, "perSeat": 50, "annualPerSeat": 45, "minSeats": 1, "api": True},
             {"tier_name": "Enterprise", "base": 0, "perSeat": 75, "minSeats": 1, "api": True}],
}

SUMMARY15 = {
 "hubspot-and-salesforce": "Big trap: HubSpot's native Salesforce connector needs a HubSpot Professional or Enterprise subscription — the free CRM can't use it. The cheapest route is Smart CRM Professional at $50 per seat a month ($45 on annual billing). Requires HubSpot on the 'Professional' plan and Salesforce Sales Cloud on the 'Professional' plan for full 2-way sync.",
 "hubspot-and-asana": "Trap: the native Asana action runs inside HubSpot workflows, which need a HubSpot Professional subscription (cheapest: Smart CRM Professional, $50 per seat a month), and tasks only flow one way. Requires HubSpot on the 'Professional' plan and Asana on the 'Starter' plan.",
 "hubspot-and-slack": "Notifications and record actions work on HubSpot's free CRM and Slack's free plan; custom Slack messages from workflows need a HubSpot Professional subscription (from $50 per seat a month). Requires HubSpot on the 'Free' plan and Slack on the 'Free' plan.",
}
