# Price/plan-name update for 6 more tools (vendor pricing pages, checked 2026-11-03).
# Basis kept the same as the existing data for each tool (annual-billing per-month price, except Slack which was monthly).
TOOL_TIERS4 = {
 # activecampaign.com/pricing (billed yearly, "starts at"): Starter $15, Plus $49, Pro $79, Enterprise $145
 "activecampaign": [{"tier_name": "Starter", "base": 15, "perSeat": 0, "minSeats": 1, "api": True},
                    {"tier_name": "Plus", "base": 49, "perSeat": 0, "minSeats": 1, "api": True},
                    {"tier_name": "Pro", "base": 79, "perSeat": 0, "minSeats": 1, "api": True}],
 # clickup.com/pricing (user/mo, billed yearly): Core $9 (formerly Unlimited), Business $17
 "clickup": [{"tier_name": "Core", "base": 0, "perSeat": 9, "minSeats": 1, "api": True},
             {"tier_name": "Business", "base": 0, "perSeat": 17, "minSeats": 1, "api": True}],
 # freshworks.com/freshdesk/pricing (agent/mo, billed annually): Growth $19, Pro $55, Enterprise $89
 "freshdesk": [{"tier_name": "Growth", "base": 0, "perSeat": 19, "minSeats": 1, "api": True},
               {"tier_name": "Pro", "base": 0, "perSeat": 55, "minSeats": 1, "api": True},
               {"tier_name": "Enterprise", "base": 0, "perSeat": 89, "minSeats": 1, "api": True}],
 # notion.com/pricing (seat/mo): Plus $10, Business $20
 "notion": [{"tier_name": "Plus", "base": 0, "perSeat": 10, "minSeats": 1, "api": True},
            {"tier_name": "Business", "base": 0, "perSeat": 20, "minSeats": 1, "api": True}],
 # slack.com/pricing (monthly list price, as before): Pro $8.75, Business+ $18
 "slack": [{"tier_name": "Pro", "base": 0, "perSeat": 8.75, "minSeats": 1, "api": True},
           {"tier_name": "Business+", "base": 0, "perSeat": 18, "minSeats": 1, "api": True}],
 # zendesk.com/pricing (agent/mo, paid yearly): Suite Team $55, Suite Professional $115;
 # Suite Growth $89 from Zendesk's pricing-update article / pricing page variant (not on the default view)
 "zendesk": [{"tier_name": "Suite Team", "base": 0, "perSeat": 55, "minSeats": 1, "api": True},
             {"tier_name": "Suite Growth", "base": 0, "perSeat": 89, "minSeats": 1, "api": True},
             {"tier_name": "Suite Professional", "base": 0, "perSeat": 115, "minSeats": 1, "api": True}],
}
RENAME4 = {"clickup": {"Unlimited": "Core"}, "activecampaign": {"Professional": "Pro"}}

PAIRS4 = {
 "hubspot-and-clickup": dict(native=True, req={"hubspot": "Free", "clickup": "Core"}, sync="1-way (automation triggers)",
   summary="ClickUp's native HubSpot integration runs on automations, such as creating a ClickUp task when a HubSpot deal closes. Requires HubSpot on the 'Free' plan and ClickUp on the 'Core' plan."),
}
COPY4_PATCH = {
 "hubspot-and-clickup": ("but this calculator assumes Unlimited, which ClickUp's help center lists for the integration.",
                         "but this calculator assumes Core (ClickUp's former Unlimited plan), which ClickUp's help center lists for the integration."),
}
