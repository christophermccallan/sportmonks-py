import os
import pytest
import responses
import logging

from sportmonks_py.core.custom_exceptions import (
    ParameterLengthException,
    InvalidDateFormat,
)
from sportmonks_py import SportMonksClient

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
console_handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
logger.setLevel(logging.INFO)

# Mock data for the API response
MOCK_SINGLE_FIXTURE_RESPONSE = {
    "data": {
        "id": 18528480,
        "sport_id": 1,
        "league_id": 271,
        "season_id": 19686,
        "stage_id": 77457696,
        "group_id": None,
        "aggregate_id": None,
        "round_id": 273989,
        "state_id": 5,
        "venue_id": 1708,
        "name": "AGF vs Viborg",
        "starting_at": "2022-07-24 12:00:00",
        "result_info": "AGF won after full-time.",
        "leg": "1/1",
        "details": None,
        "length": 90,
        "placeholder": False,
        "has_odds": True,
        "has_premium_odds": False,
        "starting_at_timestamp": 1658664000,
    },
    "timezone": "UTC",
}

MOCK_MULTI_FIXTURE_RESPONSE = {
    "data": [
        {
            "id": 463,
            "sport_id": 1,
            "league_id": 8,
            "season_id": 2,
            "stage_id": 2,
            "group_id": None,
            "aggregate_id": None,
            "round_id": 43,
            "state_id": 5,
            "venue_id": 209,
            "name": "Tottenham Hotspur vs Manchester City",
            "starting_at": "2010-08-14 11:45:00",
            "result_info": "Game ended in draw.",
            "leg": "1/1",
            "details": None,
            "length": 90,
            "placeholder": False,
            "has_odds": False,
            "has_premium_odds": False,
            "starting_at_timestamp": 1281786300,
        },
        {
            "id": 464,
            "sport_id": 1,
            "league_id": 8,
            "season_id": 3,
            "stage_id": 3,
            "group_id": None,
            "aggregate_id": None,
            "round_id": 44,
            "state_id": 5,
            "venue_id": 230,
            "name": "Liverpool vs Stoke City",
            "starting_at": "2013-08-17 11:45:00",
            "result_info": "Liverpool won after full-time.",
            "leg": "1/1",
            "details": None,
            "length": 90,
            "placeholder": False,
            "has_odds": False,
            "has_premium_odds": False,
            "starting_at_timestamp": 1376739900,
        },
    ],
    "timezone": "UTC",
}


@pytest.fixture
def client():
    """Fixture to initialize the SportMonksClient."""
    return SportMonksClient(api_token=os.environ.get("SPORTMONKS_API_TOKEN"))


# @responses.activate
# def test_get_all_fixtures(client):
#     response = client.football.fixtures.get_all_fixtures()
#     all_fixtures = []
#
#     for page in response:
#         all_fixtures.extend(page.get("data", []))
#
#     assert len(all_fixtures) > 0


@responses.activate
def test_get_fixture(client):
    """Test retrieving a specific fixture."""
    fixture_id = [18528480]
    mock_url = f"https://api.sportmonks.com/v3/football/fixtures/{fixture_id[0]}"
    responses.add(
        responses.GET,
        mock_url,
        json=MOCK_SINGLE_FIXTURE_RESPONSE,
        status=200,
        content_type="application/json",
    )
    response = client.football.fixtures.get_fixtures(
        fixture_ids=fixture_id, includes=["venue", "sport", "events.player"]
    )

    for page in response:
        assert page["id"] == MOCK_SINGLE_FIXTURE_RESPONSE["data"]["id"]
        assert page["name"] == MOCK_SINGLE_FIXTURE_RESPONSE["data"]["name"]
        assert (
            page["starting_at_timestamp"]
            == MOCK_SINGLE_FIXTURE_RESPONSE["data"]["starting_at_timestamp"]
        )
        assert page["stage_id"] == MOCK_SINGLE_FIXTURE_RESPONSE["data"]["stage_id"]


@responses.activate
def test_get_multi_fixture(client):
    """Test retrieving multiple fixtures."""
    fixture_ids = [463, 464]
    mock_url = f"https://api.sportmonks.com/v3/football/fixtures/{fixture_ids}"
    responses.add(
        responses.GET,
        mock_url,
        json=MOCK_MULTI_FIXTURE_RESPONSE,
        status=200,
        content_type="application/json",
    )
    response = client.football.fixtures.get_fixtures(fixture_ids=fixture_ids)

    for page in response:
        assert page[0]["id"] == MOCK_MULTI_FIXTURE_RESPONSE["data"][0]["id"]
        assert page[1]["id"] == MOCK_MULTI_FIXTURE_RESPONSE["data"][1]["id"]
        assert (
            page[0]["starting_at_timestamp"]
            == MOCK_MULTI_FIXTURE_RESPONSE["data"][0]["starting_at_timestamp"]
        )
        assert page[1]["stage_id"] == MOCK_MULTI_FIXTURE_RESPONSE["data"][1]["stage_id"]


@responses.activate
def test_multi_fixture_exceeds_allowed_length(client):
    """Test that requesting more than 50 fixture IDs raises a ParameterLengthException."""
    fixture_ids = list(range(1, 52))

    try:
        response = client.football.fixtures.get_fixtures(fixture_ids=fixture_ids)
    except Exception as e:
        response = e

    assert isinstance(response, ParameterLengthException)


@responses.activate
def test_get_fixtures_by_date(client):
    """Test requesting fixtures by a specific date."""
    try:
        response = client.football.fixtures.get_fixtures_by_date(date1="09-30-2024")
    except Exception as e:
        response = e

    assert isinstance(response, InvalidDateFormat)


# @responses.activate
# def test_get_fixtures_by_date_range(client):
#     """Test requesting fixtures by a specific date range."""
#     try:
#         response = client.football.fixtures.get_fixtures_by_date(
#             date1="2024-10-09", date2="2024-11-09", team_id=1
#         )
#
#     except Exception as e:
#         response = e
#
#     for page in response:
#         assert page[0]["name"] == "Tottenham Hotspur vs West Ham United"
#
#
# @responses.activate
# def test_head_to_head_fixtures(client):
#     """Test requesting head-to-head fixtures."""
#     try:
#         response = client.football.fixtures.get_h2h(team1=1, team2=2)
#     except Exception as e:
#         response = e
#
#     for page in response:
#         logger.info(page)
#         print(page)
#         assert page[0]["result_info"] == "Blackburn Rovers won after penalties."


# @responses.activate
# def test_all_odds(client):
#     odds = client.football.odds.get_all_prematch_odds()
#     for odd in odds:
#         print(odd["data"][0]["id"])

# @responses.activate
# def test_get_rivals(client):
#     rivals = client.football.other.get_rivals()
#     for rival in rivals:
#         print(rival)

# @responses.activate
# def test_commentaries(client):
#     commentaries = client.football.other.get_commentaries()
#     for commentary in commentaries:
#         print(commentary)
#
#
# @responses.activate
# def test_fixture_odds(client):
#     odds = client.football.odds.get_fixture_prematch_odds(fixture_id=18538184)
#     for odd in odds:
#         assert odd[0]["market_description"] == "Goals Over/Under 1st Half"
#
#
# @responses.activate
# def test_missing_fixture_commentary(client):
#     with pytest.raises(TypeError, match="missing 1 required positional argument: 'fixture_id'"):
#         client.football.other.get_fixture_commentary()

# @responses.activate
# def test_fixture_odds(client):
#     odds = client.football.odds.get_fixture_prematch_odds(
#         fixture_id=18538184, bookmaker_id=5, filters=["venue"]
#     )
#     for odd in odds:
#         assert odd["data"][0]["fractional"] == "9/4"

# @responses.activate
# def test_get_all_players(client):
#     players = client.football.teams.get_players()
#     for player in players:
#         assert player["data"][0]["common_name"] == "T. Tainio"
#
#
# @responses.activate
# def test_get_player_by_id(client):
#     player_data = client.football.teams.get_players(player_id=1)
#     for player in player_data:
#         assert player["data"]["common_name"] == "T. Tainio"


# @responses.activate
# def test_get_player_by_country_id(client):
#     player = client.football.teams.get_players(country_id=462)
#     assert player["data"][0]["common_name"] == "R. Hulse"
#
#
# @responses.activate
# def test_get_player_by_query(client):
#     player = client.football.teams.get_players(query="Salah")
#     assert player["data"][0]["display_name"] == "Mohamed Salah"
