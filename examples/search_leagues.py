import os
from sportmonks_py.client import APIClient

client = APIClient(sport="football", api_token=os.environ.get("SPORTMONKS_API_TOKEN"))

fixture_id = [18528480]
response = client.leagues.search_leagues(search="premier")

for page in response:
    print(page)
