"""2026-11-17. Every calculator lists the tool's free plan when that plan has API access.

The owner asked for this fix. Until then, 14 pair calculators started from the cheapest *paid* plan of Calendly, Mailchimp,
ClickUp or Slack. Each of those tools' free plan includes API access (see their API pages and data/integration-pairs.json,
where each plan's `api_access` is recorded with its source). So those pages showed a smaller hidden cost than the
Integration Tax report, which always starts from the cheapest plan with API access, and five of them said "No hidden cost"
while calling a paid plan "the cheapest plan with API access".

pairfix.py now adds the free plan to a calculator whenever the open data says that plan has API access (FREE_API there).
No price or plan requirement changed and no "checked" date moved: the free plans' prices ($0) and API access were already
on the site. FREE26 lists the pages that changed that day, so their dateModified says so.
"""
FREE26 = [
    "activecampaign-and-calendly", "hubspot-and-calendly", "mailchimp-and-calendly", "notion-and-calendly",
    "pipedrive-and-calendly", "salesforce-and-calendly", "stripe-and-calendly", "xero-and-calendly",
    "asana-and-mailchimp", "hubspot-and-mailchimp", "mailchimp-and-airtable", "salesforce-and-mailchimp",
    "hubspot-and-clickup", "salesforce-and-slack",
]
# Two more pages changed that day without a new tier: they already listed Calendly's free plan, and their Make and Zapier
# rows now use Calendly Standard, the plan those triggers need (model.MW_FLOOR).
MW26 = ["intercom-and-calendly", "slack-and-calendly"]
DATE26 = "2026-11-17"
FREE_TIER = {"tier_name": "Free", "base": 0, "perSeat": 0, "minSeats": 1, "api": True}   # same shape as on the pages that already list it
