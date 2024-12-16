from typing import Union
from sportmonks_py.utils.common_types import StdResponse, AsyncResponse
from sportmonks_py.base_client import BaseClient


class CoreClient(BaseClient):
    """
    A client for accessing common endpoints data from the SportMonks API.
    """

    def __init__(self, base_url: str, api_token: str) -> None:
        """
        Initialize the Common Client with a base_url, sport and API token.

        :param api_token: API token for authenticating requests.
        :param base_url: Base URL for the API.
        """
        super().__init__(base_url=base_url, api_token=api_token)

    def get_all_cities(
        self, async_mode: bool = False
    ) -> Union[StdResponse, AsyncResponse]:
        """
        This endpoint returns all available filters for the entities.
        :param async_mode: Whether to use async mode.

        :return: StdResponse | AsyncResponse
        """
        return self._get("core/cities", async_mode=async_mode)

    def get_city_by_id(
        self, city_id: int, async_mode: bool = False
    ) -> Union[StdResponse, AsyncResponse]:
        """
        This endpoint returns a city by its ID.

        :param city_id: ID of the city.
        :param async_mode: Whether to use async mode.
        :return: StdResponse | AsyncResponse
        """
        return self._get(f"core/cities/{city_id}", async_mode=async_mode)

    def search_cities(
        self, search: str, async_mode: bool = False
    ) -> Union[StdResponse, AsyncResponse]:
        """
        This endpoint returns all available filters for the entities.
        :param search: Search string to search for.
        :param async_mode: Whether to use async mode.

        :return: StdResponse | AsyncResponse
        """
        return self._get(f"core/cities/search/{search}", async_mode=async_mode)

    def get_all_continents(
        self, async_mode: bool = False
    ) -> Union[StdResponse, AsyncResponse]:
        """
        This endpoint returns all available filters for the entities.
        :param async_mode: Whether to use async mode.

        :return: StdResponse | AsyncResponse
        """
        return self._get("core/continents", async_mode=async_mode)

    def get_continent_by_id(
        self, continent_id: int, async_mode: bool = False
    ) -> Union[StdResponse, AsyncResponse]:
        """
        This endpoint returns a continent by its ID.

        :param continent_id: ID of the continent.
        :param async_mode: Whether to use async mode.
        :return: StdResponse | AsyncResponse
        """
        return self._get(f"core/continents/{continent_id}", async_mode=async_mode)

    def get_all_countries(
        self, async_mode: bool = False
    ) -> Union[StdResponse, AsyncResponse]:
        """
        This endpoint returns all available filters for the entities.
        :param async_mode: Whether to use async mode.

        :return: StdResponse | AsyncResponse
        """
        return self._get("core/countries", async_mode=async_mode)

    def get_country_by_id(
        self, country_id: int, async_mode: bool = False
    ) -> Union[StdResponse, AsyncResponse]:
        """
        This endpoint returns a country by its ID.

        :param country_id: ID of the country.
        :param async_mode: Whether to use async mode.

        :return: StdResponse | AsyncResponse
        """
        return self._get(f"core/countries/{country_id}", async_mode=async_mode)

    def search_countries(
        self, search: str, async_mode: bool = False
    ) -> Union[StdResponse, AsyncResponse]:
        """
        This endpoint returns all available filters for the entities.
        :param search: string to search for.
        :param async_mode: Whether to use async mode.

        :return: StdResponse | AsyncResponse
        """
        return self._get(f"core/countries/search/{search}", async_mode=async_mode)

    def get_all_regions(
        self, async_mode: bool = False
    ) -> Union[StdResponse, AsyncResponse]:
        """
        This endpoint returns all available filters for the entities.

        :return: StdResponse | AsyncResponse
        """
        return self._get("core/regions", async_mode=async_mode)

    def get_region_by_id(
        self, region_id: int, async_mode: bool = False
    ) -> Union[StdResponse, AsyncResponse]:
        """
        This endpoint returns a region by its ID.

        :param region_id: ID of the region.
        :param async_mode: Whether to use async mode.

        :return: StdResponse | AsyncResponse
        """
        return self._get(f"core/regions/{region_id}", async_mode=async_mode)

    def search_regions(
        self, search: str, async_mode: bool = False
    ) -> Union[StdResponse, AsyncResponse]:
        """
        This endpoint returns all available filters for the entities.
        :param search: string to search for.
        :param async_mode: Whether to use async mode.

        :return: StdResponse | AsyncResponse
        """
        return self._get(f"core/regions/search/{search}", async_mode=async_mode)

    def get_all_types(
        self, async_mode: bool = False
    ) -> Union[StdResponse, AsyncResponse]:
        """
        This endpoint returns all available filters  for the entities.
        :param async_mode: Whether to use async mode.

        :return: StdResponse | AsyncResponse
        """
        return self._get("core/types", async_mode=async_mode)

    def get_type_by_id(
        self, type_id: int, async_mode: bool = False
    ) -> Union[StdResponse, AsyncResponse]:
        """
        This endpoint returns a type by its ID.

        :param type_id: ID of the type.
        :param async_mode: Whether to use async mode.

        :return: StdResponse | AsyncResponse
        """
        return self._get(f"core/types/{type_id}", async_mode=async_mode)
