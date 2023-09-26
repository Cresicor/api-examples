# This is an example of how to call Vividly's API from a Python script.
# You will need to use your own company ID and API token.

import requests

# IMPORTANT: We highly recommend not storing these values in plaintext on the web!
# Please use a secret manager or some other method of encrypted storage.
VIVIDLY_API_TOKEN = "TODO"
VIVIDLY_COMPANY_ID = "TODO"

# The query you wish to perform.
# This retrieves a subset of information from all the promotions in your company
# whose names contain "KeHE".
GRAPHQL_QUERY = """
query {
    promotions (filters: { name: { contains: "KeHE" } }) {
        name
        isStarred
        promotionlinePromotion {
            buyinEndDate
            buyinStartDate
            scanbackEndDate
            scanbackStartDate
        }
    }
}
"""

# Call the Vividly API.
response = requests.post(
    "https://portal.govividly.com/public/graphql/",
    json={"query": GRAPHQL_QUERY},
    headers={
        "Authorization": f"Token {VIVIDLY_API_TOKEN}",
        "Company": VIVIDLY_COMPANY_ID,
    }
)

# Here, we print the response.
# You (the user) can choose what to do with this response.
print(f"Response code {response.status_code}")
print(f"Body:\n{response.text}")
