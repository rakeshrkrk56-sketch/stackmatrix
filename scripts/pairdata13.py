# 2026-11-04: four new pairs. Requirements read on the vendors' pages on Nov 4, 2026; prices are the site's
# Nov 3 data (Salesforce prices last verified Oct 17; QuickBooks re-checked Nov 4).
MAKE = "Make Core ($10.59/mo, or $9/mo billed annually)"
SF_ED = ("Salesforce developers: Supported editions", "https://developer.salesforce.com/docs/platform/api-rest/guide/intro-rest-compatible-editions.html")
MAKE_SF = ("Make: Salesforce app", "https://apps.make.com/salesforce")
CHECKED = "Nov 4, 2026"
NEW13 = {
 "hubspot-and-quickbooks": dict(template="hubspot-and-stripe", swap=("stripe", "quickbooks"), A="hubspot", B="quickbooks",
   req={"hubspot": "Free", "quickbooks": "Simple Start"}, native=True, mw=0, sync="2-way", difficulty=2, cats="CRM|Accounting",
   summary="HubSpot's own QuickBooks Online integration syncs contacts, products and invoices on every HubSpot plan, including the free CRM, and shows QuickBooks payments on HubSpot deals; it supports U.S. QuickBooks accounts only. Requires HubSpot on the 'Free' plan and QuickBooks Online on the 'Simple Start' plan.",
   answer="Yes. HubSpot builds a QuickBooks Online integration, available on every HubSpot plan including the free CRM, that keeps customers, products, invoices and payments aligned between the two.",
   how="Once connected, contacts, products and invoices sync between HubSpot and QuickBooks Online according to your sync settings, and you can see QuickBooks payment information on the related HubSpot deals. Products are matched on their SKU, so products without one aren't synced by default.",
   setup=["Make sure you're a Super Admin or have App Marketplace permissions in HubSpot.", "In HubSpot, click the Marketplace icon, select HubSpot Marketplace, search for QuickBooks Online and click Install.", "Click Connect to QuickBooks Online and log in with your QuickBooks details.", "Choose your sync settings and review the mapped fields."],
   limits="The integration doesn't yet support non-U.S. QuickBooks Online accounts. Some edits to invoices created in HubSpot, such as adding or removing line items, changing prices or adding tax, have to be made in HubSpot, or the invoice fails to sync. Adding your own field mappings needs Data Hub Starter or higher.",
   sources=[("HubSpot: Connect HubSpot and QuickBooks Online", "https://knowledge.hubspot.com/integrations/connect-hubspot-and-quickbooks-online")]),
 "pipedrive-and-quickbooks": dict(template="pipedrive-and-xero", swap=("xero", "quickbooks"), A="pipedrive", B="quickbooks",
   req={"pipedrive": "Lite", "quickbooks": "Simple Start"}, native=True, mw=0, sync="2-way", difficulty=1, cats="CRM|Accounting",
   summary="Pipedrive's own QuickBooks integration creates QuickBooks invoices from Pipedrive deals and shows whether they're paid or overdue on the deal; it needs a paying or trial account in both tools, and it works with QuickBooks Online only. Requires Pipedrive on the 'Lite' plan and QuickBooks Online on the 'Simple Start' plan.",
   answer="Yes. Pipedrive's own QuickBooks integration lets you create QuickBooks invoices from a Pipedrive deal and shows whether they're paid or overdue back on the deal. It works with QuickBooks Online only.",
   how="You create an invoice from the deal detail view in Pipedrive, using the deal's contact and products, and it's sent to your QuickBooks account without copying anything by hand. The invoice's status, such as paid or overdue, then updates on the deal in Pipedrive.",
   setup=["In Pipedrive, open the account menu, go to Tools and apps > Invoicing and click Install next to QuickBooks.", "Finish the installation in the Pipedrive Marketplace and grant access to your QuickBooks account.", "Open a deal and create an invoice from the deal detail view; if Pipedrive shows a warning on the To field, link the contact to a QuickBooks customer."],
   limits="It needs an active paying or trial account with both Pipedrive and QuickBooks, and it works with QuickBooks Online only. Pipedrive no longer supports it in France. Keep products up to date in both tools before creating invoices.",
   sources=[("Pipedrive: QuickBooks integration", "https://support.pipedrive.com/en/article/pipedrive-integration-quickbooks"), ("Pipedrive: Invoicing feature", "https://support.pipedrive.com/en/article/invoicing-feature-in-pipedrive")]),
 "salesforce-and-quickbooks": dict(template="airtable-and-quickbooks", swap=("airtable", "salesforce"), A="salesforce", B="quickbooks",
   req={"salesforce": "Professional", "quickbooks": "Simple Start"}, native=False, mw=(10.59, 9), sync="1-way (trigger → action)", difficulty=2, cats="CRM|Accounting",
   summary="Salesforce doesn't build a QuickBooks connector; AppExchange apps such as Breadwinner (from $310/mo) or Make Core link them through Salesforce's API, which Professional Edition gets only as a paid add-on. Requires Salesforce Sales Cloud on the 'Professional' plan and QuickBooks Online on the 'Simple Start' plan. Route it through " + MAKE + ".",
   answer="Not with a Salesforce-built connector. Salesforce points to AppExchange apps such as Breadwinner, which starts at $310 a month, and Make or Zapier can connect the two through Salesforce's API, which Professional Edition only gets as a paid add-on.",
   how="With Make, a scenario watches Salesforce, for example for a won opportunity, and creates the customer or invoice in QuickBooks Online, or the other way round. Breadwinner is a native Salesforce app with real-time QuickBooks sync, priced separately.",
   setup=["Make sure your Salesforce org has API access: Enterprise or Unlimited include it, Professional needs the API add-on.", "In Make, create a scenario and connect your Salesforce account and your QuickBooks account.", "Pick a trigger, such as a won opportunity, and a QuickBooks action, such as creating an invoice, then map the fields and turn the scenario on."],
   limits="This calculator models Salesforce Professional with the $25/user API add-on plus Make Core; Enterprise includes API access without the add-on. Breadwinner's own price, from $310 a month, isn't included. Each Make scenario runs one way.",
   sources=[MAKE_SF, SF_ED, ("Breadwinner: Pricing", "https://breadwinner.com/pricing"), ("Make: QuickBooks app", "https://apps.make.com/quickbooks")]),
 "pipedrive-and-salesforce": dict(template="pipedrive-and-calendly", swap=("calendly", "salesforce"), A="pipedrive", B="salesforce",
   req={"pipedrive": "Lite", "salesforce": "Professional"}, native=False, mw=(10.59, 9), sync="1-way (trigger → action)", difficulty=2, cats="CRM|CRM",
   summary="Pipedrive and Salesforce don't build an integration with each other; Make Core connects them through both APIs, and Salesforce Professional needs its paid API add-on for that. Requires Pipedrive on the 'Lite' plan and Salesforce Sales Cloud on the 'Professional' plan. Route it through " + MAKE + ".",
   answer="Not natively. Pipedrive and Salesforce don't build an integration with each other, but Make or Zapier connects them through both tools' APIs; Salesforce Professional needs its paid API add-on for that.",
   how="A Make scenario watches one CRM and acts in the other, for example creating a Salesforce lead or contact when a deal or person is added in Pipedrive. Each scenario runs one way, so keeping both sides in step needs one scenario per direction.",
   setup=["Make sure your Salesforce org has API access: Enterprise or Unlimited include it, Professional needs the API add-on.", "In Make, create a scenario and connect your Pipedrive and Salesforce accounts.", "Pick a trigger in one tool and an action in the other, map the fields and turn the scenario on."],
   limits="This calculator models Salesforce Professional with the $25/user API add-on; Enterprise includes API access without it. Pipedrive's API is available on every plan, with rate limits that rise with the plan. Real usage can push Make onto a bigger plan.",
   sources=[MAKE_SF, SF_ED, ("Pipedrive developers: Rate limiting", "https://pipedrive.readme.io/docs/core-api-concepts-rate-limiting")]),
}
TIER_SOURCE = {"hubspot": "hubspot-and-stripe", "quickbooks": "airtable-and-quickbooks", "salesforce": "salesforce-and-stripe", "pipedrive": "pipedrive-and-xero"}
PAIRS13 = {p: dict(native=c["native"], req=c["req"], sync=c["sync"], summary=c["summary"], date="2026-11-04") for p, c in NEW13.items()}
COPY13 = {p: dict(how=c["how"], limits=c["limits"], sources=c["sources"], answer=c["answer"], setup=c["setup"], top=True, checked=CHECKED) for p, c in NEW13.items()}
