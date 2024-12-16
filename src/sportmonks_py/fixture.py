from typing import Union, List, Optional
from sportmonks_py.client.base_client import BaseClient
from sportmonks_py.utils.errors import ParameterLengthException, InvalidDateFormat
from sportmonks_py.utils.helper import validate_date_format, validate_date_order
from sportmonks_py.utils.common_types import (
    Includes,
    Selects,
    Filters,
    StdResponse,
    AsyncResponse,
)


class FixturesClient(BaseClient):
    """
    A client for accessing fixture-related data from the SportMonks API.
    """

    def __init__(self, base_url: str, api_token: str) -> None:
        """
        Initialize the Fixture Client with a base_url, sport and API token.

        :param api_token: API token for authenticating requests.
        :param base_url: Base URL for the API.
        """
        super().__init__(base_url=base_url, api_token=api_token)

    def get_all_fixtures(
        self,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
        async_mode: bool = False,
        locale: Optional[str] = None,
    ) -> Union[StdResponse, AsyncResponse]:
        """
        Retrieve all fixtures from the SportMonks database.

        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :param async_mode: Boolean flag for asynchronous mode.
        :param locale: Language to return the data in.

        :return: StdResponse | AsyncResponse
        """
        return self._get(
            "fixtures",
            params={"include": includes, "select": selects, "filter": filters},
            async_mode=async_mode,
        )

    def get_fixtures(
        self,
        fixture_ids: List[int],
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
        async_mode: bool = False,
        locale: Optional[str] = None,
    ) -> Union[StdResponse, AsyncResponse]:
        """
        Retrieve specific fixtures by their IDs.

        :param fixture_ids: List of fixture IDs to retrieve.
        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :param async_mode: Boolean flag for asynchronous mode.
        :param locale: Language to return the data in.

        :return: StdResponse | AsyncResponse

        :raises ValueError: If no fixture IDs are provided.
        :raises ParameterLengthException: If more than 50 fixture IDs are provided.
        """
        if not fixture_ids:
            raise ValueError("You must provide at least one fixture ID, ie [123456].")
        if len(fixture_ids) > 50:
            raise ParameterLengthException("Maximum of 50 fixture IDs allowed.")

        if len(fixture_ids) == 1:
            return self._get(
                f"fixtures/{fixture_ids[0]}",
                params={"include": includes, "select": selects, "filter": filters},
                async_mode=async_mode,
                locale=locale,
            )

        fixtures = ",".join(map(str, fixture_ids))
        return self._get(
            f"fixtures/multi/{fixtures}",
            params={"include": includes, "select": selects, "filter": filters},
            async_mode=async_mode,
            locale=locale,
        )

    def get_fixtures_by_date(
        self,
        date1: str,
        date2: Optional[str] = None,
        team_id: Optional[int] = None,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
        async_mode: bool = False,
        locale: Optional[str] = None,
    ) -> Union[StdResponse, AsyncResponse]:
        """
        Retrieve fixtures for a specific date or date range.

        :param date1: Start date in 'YYYY-MM-DD' format.
        :param date2: End date in 'YYYY-MM-DD' format (optional).
        :param team_id: Filter by a specific team ID (optional).
        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :param async_mode: Boolean flag for asynchronous mode.
        :param locale: Language to return the data in.

        :return: StdResponse | AsyncResponse

        :raises InvalidDateFormat: If a date is in an invalid format.
        :raises ValueError: If the start date is after the end date.
        """
        if not validate_date_format(date1):
            raise InvalidDateFormat(f"Invalid date format: '{date1}'.")
        if date2:
            if not validate_date_format(date2):
                raise InvalidDateFormat(f"Invalid date format: '{date2}'.")
            if not validate_date_order(date1, date2):
                raise ValueError("Start date must be before the end date.")

            endpoint = f"fixtures/between/{date1}/{date2}"
            if team_id:
                endpoint += f"/{team_id}"
            return self._get(
                endpoint,
                params={"include": includes, "select": selects, "filter": filters},
                async_mode=async_mode,
                locale=locale,
            )

        return self._get(
            f"fixtures/date/{date1}",
            params={"include": includes, "select": selects, "filter": filters},
            async_mode=async_mode,
            locale=locale,
        )

    def get_h2h(
        self,
        team1: int,
        team2: int,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
        async_mode: bool = False,
        locale: Optional[str] = None,
    ) -> Union[StdResponse, AsyncResponse]:
        """
        Retrieve head-to-head fixtures for two teams.

        :param team1: First team ID.
        :param team2: Second team ID.
        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :param async_mode: Boolean flag for asynchronous mode.
        :param locale: Language to return the data in.

        :return: StdResponse | AsyncResponse

        :raises ValueError: If team IDs are not positive integers.
        """
        if team1 <= 0 or team2 <= 0:
            raise ValueError("Team IDs must be positive integers.")

        return self._get(
            f"fixtures/head-to-head/{team1}/{team2}",
            params={"include": includes, "select": selects, "filter": filters},
            async_mode=async_mode,
            locale=locale,
        )

    def search_fixtures(
        self,
        search: Union[int, str],
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
        async_mode: bool = False,
        locale: Optional[str] = None,
    ) -> Union[StdResponse, AsyncResponse]:
        """
        Search fixtures by string or int.

        :param search: String or ID to search.
        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :param async_mode: Boolean flag for asynchronous mode.
        :param locale: Language to return the data in.

        :return: StdResponse | AsyncResponse
        """
        return self._get(
            f"fixtures/search/{search}",
            params={"include": includes, "select": selects, "filter": filters},
            async_mode=async_mode,
            locale=locale,
        )

    def get_fixtures_by_market(
        self,
        market_id: int,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
        async_mode: bool = False,
        locale: Optional[str] = None,
    ) -> Union[StdResponse, AsyncResponse]:
        """
        Retrieve upcoming fixtures for a specific market.

        :param market_id: Market ID.
        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :param async_mode: Boolean flag for asynchronous mode.
        :param locale: Language to return the data in.

        :return: StdResponse | AsyncResponse
        """
        return self._get(
            f"fixtures/upcoming/markets/{market_id}",
            params={"include": includes, "select": selects, "filter": filters},
            async_mode=async_mode,
            locale=locale,
        )

    def get_fixtures_by_station(
        self,
        station_id: int,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
        async_mode: bool = False,
        locale: Optional[str] = None,
    ) -> Union[StdResponse, AsyncResponse]:
        """
        Retrieve upcoming fixtures for a specific TV station.

        :param station_id: TV station ID.
        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :param async_mode: Boolean flag for asynchronous mode.
        :param locale: Language to return the data in.

        :return: StdResponse | AsyncResponse
        """
        return self._get(
            f"fixtures/upcoming/tv-stations/{station_id}",
            params={"include": includes, "select": selects, "filter": filters},
            async_mode=async_mode,
            locale=locale,
        )

    def get_fixtures_by_updates(
        self,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
        async_mode: bool = False,
        locale: Optional[str] = None,
    ) -> Union[StdResponse, AsyncResponse]:
        """
        Retrieve fixtures updated within the last 10 seconds.

        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :param async_mode: Boolean flag for asynchronous mode.
        :param locale: Language to return the data in.

        :return: StdResponse | AsyncResponse
        """
        return self._get(
            "fixtures/latest",
            params={"include": includes, "select": selects, "filter": filters},
            async_mode=async_mode,
            locale=locale,
        )

    def get_inplay_livescores(
        self,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
        async_mode: bool = False,
        locale: Optional[str] = None,
    ) -> Union[StdResponse, AsyncResponse]:
        """
        GET All Inplay Livescores: returns all the inplay fixtures.

        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :param async_mode: Boolean flag for asynchronous mode.
        :param locale: Language to return the data in.

        :return: StdResponse | AsyncResponse
        """
        return self._get(
            "fixtures/livescores/inplay",
            params={"include": includes, "select": selects, "filter": filters},
            async_mode=async_mode,
            locale=locale,
        )

    def get_all_livescores(
        self,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
        async_mode: bool = False,
        locale: Optional[str] = None,
    ) -> Union[StdResponse, AsyncResponse]:
        """
        Returns the fixtures 15 minutes before the game starts. It will also disappear 15 minutes after the game is finished.

        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :param async_mode: Boolean flag for asynchronous mode.
        :param locale: Language to return the data in.

        :return: StdResponse | AsyncResponse
        """
        return self._get(
            "fixtures/livescores",
            params={"include": includes, "select": selects, "filter": filters},
            async_mode=async_mode,
            locale=locale,
        )

    def get_livescore_updates(
        self,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
        async_mode: bool = False,
        locale: Optional[str] = None,
    ) -> Union[StdResponse, AsyncResponse]:
        """
        Returns you all livescores that have received updates within 10 seconds.

        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :param async_mode: Boolean flag for asynchronous mode.
        :param locale: Language to return the data in.

        :return: StdResponse | AsyncResponse
        """
        return self._get(
            "fixtures/livescores/latest",
            params={"include": includes, "select": selects, "filter": filters},
            async_mode=async_mode,
            locale=locale,
        )
