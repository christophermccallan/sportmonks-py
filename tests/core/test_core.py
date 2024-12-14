import os
import pytest
import responses
from sportmonks_py import APIClient


@pytest.fixture
def client():
    """Fixture to initialize the SportMonksClient."""
    return APIClient(sport="football", api_token=os.environ.get("SPORTMONKS_API_TOKEN"))


@responses.activate
def test_client(client):
    assert client is not None


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
def test_all_type_by_id(client):
    types = client.core.get_type_by_id(type_id=134)
    for sportmonks_type in types:
        assert sportmonks_type["developer_name"] == "OVERALL_CONCEDED"
