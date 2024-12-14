import os
import asyncio
import pytest
import responses
from sportmonks_py import APIClient
from sportmonks_py.utils.errors import ParameterLengthException, InvalidDateFormat


@pytest.fixture
def client():
    """Fixture to initialize the SportMonksClient."""
    return APIClient(sport="football", api_token=os.environ.get("SPORTMONKS_API_TOKEN"))


@responses.activate
def test_client(client):
    assert client is not None


@responses.activate
def test_multi_fixture_exceeds_allowed_length(client):
    """Test that requesting more than 50 fixture IDs raises a ParameterLengthException."""
    fixture_ids = list(range(1, 52))

    try:
        response = client.fixtures.get_fixtures(fixture_ids=fixture_ids)
    except Exception as e:
        response = e

    assert isinstance(response, ParameterLengthException)


@responses.activate
def test_get_fixtures_by_date(client):
    """Test requesting fixtures by a specific date."""
    try:
        response = client.fixtures.get_fixtures_by_date(date1="09-30-2024")
    except Exception as e:
        response = e

    assert isinstance(response, InvalidDateFormat)


@responses.activate
def test_get_fixtures_by_date_range(client):
    """Test requesting fixtures by a specific date range."""
    try:
        response = client.fixtures.get_fixtures_by_date(
            date1="2024-10-09", date2="2024-11-09", team_id=1
        )

    except Exception as e:
        response = e

    for page in response:
        assert page[0]["name"] == "Tottenham Hotspur vs West Ham United"


@responses.activate
def test_head_to_head_fixtures(client):
    """Test requesting head-to-head fixtures."""
    try:
        response = client.fixtures.get_h2h(team1=1, team2=2)
    except Exception as e:
        response = e

    for page in response:
        assert page[0]["result_info"] == "Blackburn Rovers won after penalties."


@responses.activate
def test_fixture_odds(client):
    odds = client.odds.get_fixture_prematch_odds(fixture_id=18538184, bookmaker_id=5)
    for odd in odds:
        assert odd[0]["market_description"] == "Match Winner"


@responses.activate
def test_search_region(client):
    regions = client.core.search_regions(search="Northern Ireland")
    for region in regions:
        assert region[0]["country_id"] == 462


@responses.activate
def test_get_city_by_id(client):
    cities = client.core.get_city_by_id(city_id=50)
    for city in cities:
        assert city["name"] == "Aachen"


@responses.activate
def test_get_player_by_search(client):
    players = client.teams.get_players(search="Salah")
    for player in players:
        assert player[0]["display_name"] == "Mohamed Salah"


# @responses.activate
# async def test_get_teams_by_country(client):
#     teams = await client.teams.get_teams(country_id=462)
#     for team in teams:
#         assert team[0]["name"] == "Northern Ireland"
