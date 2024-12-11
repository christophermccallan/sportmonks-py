# # tests/core_test.py
# import pytest
#
#
# @pytest.fixture
# def core_client():
#     # Initialize Core with a dummy token
#     return Core(api_token="dummy_token")
#
#
# def test_core_continents_all(core_client, mocker):
#     # Mock the _get method to return a predefined response similar to the actual API
#     mock_response = {
#         "data": [
#             {"id": 1, "name": "Europe", "code": "EU"},
#             {"id": 2, "name": "Asia", "code": "AS"},
#             {"id": 3, "name": "Africa", "code": "AF"},
#             {"id": 4, "name": "Oceania", "code": "OC"},
#             {"id": 5, "name": "Antarctica", "code": "AT"},
#             {"id": 6, "name": "North America", "code": "NA"},
#             {"id": 7, "name": "South America", "code": "SA"},
#         ],
#         "timezone": "UTC",
#     }
#     mocker.patch.object(core_client, "_get", return_value=mock_response)
#     response = core_client.continents()
#
#     assert response["data"][1]["name"] == "Asia"
#     assert response["data"][1]["code"] == "AS"
#     assert response["timezone"] == "UTC"
#
#
# def test_core_continent_by_id(core_client, mocker):
#     # Mock the _get method for a single continent response
#     mock_response = {"data": {"id": 2, "name": "Asia", "code": "AS"}}
#     mocker.patch.object(core_client, "_get", return_value=mock_response)
#     response = core_client.continents(continent_id=2)
#
#     # Assertions to check the specific continent response
#     assert response["data"]["id"] == 2
#     assert response["data"]["name"] == "Asia"
#     assert response["data"]["code"] == "AS"
