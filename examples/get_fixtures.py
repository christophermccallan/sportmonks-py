import os
from sportmonks_py.client import APIClient

client = APIClient(sport="football", api_token=os.environ.get("SPORTMONKS_API_TOKEN"))

fixture_id = [18528480]
response = client.fixtures.get_fixtures(
    fixture_ids=fixture_id, includes=["venue", "sport", "events.player"]
)

for page in response:
    print(page)
