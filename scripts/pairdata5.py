# Monthly-billing base prices + vendor annual-billing prices (checked 2026-11-03 on each vendor's pricing page with
# the monthly toggle selected). base/perSeat = monthly price; annualBase/annualPerSeat = per-month price when billed
# annually. Tools absent here keep their current single price (ActiveCampaign and Pipedrive publish annual-only rates,
# Salesforce annual contracts; Mailchimp, Xero, QuickBooks and Stripe are monthly with no annual price modeled; HubSpot
# Starter's regular price is $20 on both; HubSpot Pro $800 kept per owner).
TOOL_TIERS5 = {
 "airtable":  [("Team", 0, 24, 20), ("Business", 0, 54, 45)],                                        # airtable.com/pricing
 "asana":     [("Starter", 0, 13.49, 10.99), ("Advanced", 0, 30.49, 24.99)],                         # asana.com/pricing
 "calendly":  [("Standard", 0, 12, 10), ("Teams", 0, 20, 16)],                                       # calendly.com/pricing
 "clickup":   [("Core", 0, 12, 9), ("Business", 0, 25, 17)],                                         # clickup.com/pricing
 "freshdesk": [("Growth", 0, 23, 19), ("Pro", 0, 66, 55), ("Enterprise", 0, 107, 89)],               # freshworks.com/freshdesk/pricing
 "intercom":  [("Essential", 0, 39, 29), ("Advanced", 0, 99, 85)],                                   # intercom.com help "Seats" + pricing guide
 "monday":    [("Basic", 0, 12, 9), ("Standard", 0, 14, 12), ("Pro", 0, 24, 19)],                    # monday.com/pricing (min 3 seats)
 "notion":    [("Plus", 0, 12, 10), ("Business", 0, 24, 20)],                                        # notion.com/pricing
 "zendesk":   [("Suite Team", 0, 69, 55), ("Suite Growth", 0, 115, 89), ("Suite Professional", 0, 149, 115)],  # Zendesk pricing article
 "slack":     [("Pro", 0, 8.75, None), ("Business+", 0, 18, None)],                                   # slack.com/pricing ("when paying monthly")
}
SUMMARY_FIXES = {  # pair: (old fragment, new fragment)
 "hubspot-and-calendly": ("needs Calendly Teams ($16/seat)", "needs Calendly Teams ($20/seat)"),
 "asana-and-quickbooks": ("the Advanced plan ($24.99/seat)", "the Advanced plan ($30.49/seat)"),
}
