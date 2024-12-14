import os
import pytest
from unittest.mock import patch
from sportmonks_py import APIClient

@pytest.fixture
def client():
    """Fixture to initialize the SportMonksClient."""
    return APIClient(sport="football", api_token=os.environ.get("SPORTMONKS_API_TOKEN"))

@pytest.mark.asyncio
async def test_async_get_generator_single_page(client):

    fixture_ids = [18528480]

    async for page in  client.fixtures.get_fixtures(fixture_ids=fixture_ids, async_mode=True):
        assert page["result_info"] == "AGF won after full-time."

@pytest.mark.asyncio
async def test_async_get_team_single_page(client):
    async for page in  client.teams.get_teams(team_id=100, async_mode=True):
        assert page["name"] == "Ebbsfleet United"