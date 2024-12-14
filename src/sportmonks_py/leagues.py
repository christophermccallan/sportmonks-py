from typing import Union, Optional

from .base_client import BaseClient
from .utils.common_types import Includes, Selects, Filters, StdResponse, AsyncResponse

from .utils.errors import InvalidDateFormat
from .utils.helper import validate_date_format


class LeaguesClient(BaseClient):
    """
    A client for accessing league-related data from the SportMonks API.
    """

    def __init__(self, base_url: str, api_token: str) -> None:
        """
        Initialize the League Client with a base_url, sport and API token.

        :param api_token: API token for authenticating requests.
        :param base_url: Base URL for the API.
        """
        super().__init__(base_url=base_url, api_token=api_token)

    def get_all_leagues(
        self,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
        async_mode: bool = False,
    ) -> StdResponse | AsyncResponse:
        """
        Returns all the leagues available within your subscription

        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :param async_mode: Boolean flag for asynchronous mode.
        :return: Iterator over fixture data.
        """
        return self._get(
            "leagues",
            params={"include": includes, "select": selects, "filter": filters},
            async_mode=async_mode,
        )

    def get_league(
        self,
        league_id: int,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
        async_mode: bool = False,
    ) -> StdResponse | AsyncResponse:
        """
        Returns the league you've requested by ID.

        :param league_id: Int
        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :param async_mode: Boolean flag for asynchronous mode.
        :return: Iterator over fixture data.
        :raises ValueError: If no fixture IDs are provided.
        """

        if not league_id:
            raise ValueError("You must provide a League ID")

        return self._get(
            f"leagues/{league_id}",
            params={"include": includes, "select": selects, "filter": filters},
            async_mode=async_mode,
        )

    def get_live_leagues(
        self,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
        async_mode: bool = False,
    ) -> StdResponse | AsyncResponse:
        """
        Returns all the leagues that with fixtures that are currently being played.

        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :param async_mode: Boolean flag for asynchronous mode.
        :return: Iterator over fixture data.
        """

        return self._get(
            "leagues/live",
            params={"include": includes, "select": selects, "filter": filters},
            async_mode=async_mode,
        )

    def get_league_by_fixture_date(
        self,
        date: str,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
        async_mode: bool = False,
    ) -> StdResponse | AsyncResponse:
        """
        Returns all the leagues with fixtures from your requested fixture date.

        :param date: Date in 'YYYY-MM-DD' format.
        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :param async_mode: Boolean flag for asynchronous mode.
        :raises InvalidDateFormat: If a date is in an invalid format.
        :return: Iterator over fixture data.
        """

        if not validate_date_format(date):
            raise InvalidDateFormat(f"Invalid date format: '{date}'.")

        return self._get(
            f"leagues/fixtures/{date}",
            params={"include": includes, "select": selects, "filter": filters},
            async_mode=async_mode,
        )

    def get_leagues_by_country_id(
        self,
        country_id: int,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
        async_mode: bool = False,
    ) -> StdResponse | AsyncResponse:
        """
        Returns all the leagues with fixtures from your requested fixture date.

        :param country_id: Int
        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :param async_mode: Boolean flag for asynchronous mode.
        :raises InvalidDateFormat: If a date is in an invalid format.
        :return: Iterator over fixture data.
        """

        if not country_id:
            raise ValueError("Country ID not supplied")

        return self._get(
            f"leagues/countries/{country_id}",
            params={"include": includes, "select": selects, "filter": filters},
            async_mode=async_mode,
        )

    def search_leagues(
        self,
        search: Union[int, str],
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
        async_mode: bool = False,
    ) -> StdResponse | AsyncResponse:
        """
        Returns all the leagues that match your search.

        :param search: String or ID to search.
        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :param async_mode: Boolean flag for asynchronous mode.
        :return: Iterator over fixture data.
        """
        return self._get(
            f"leagues/search/{search}",
            params={"include": includes, "select": selects, "filter": filters},
            async_mode=async_mode,
        )

    def get_all_leagues_by_team(
        self,
        team_id: int,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
        async_mode: bool = False,
    ) -> StdResponse | AsyncResponse:
        """
        Returns all the current and historical leagues from your requested team id.

        :param team_id: Team ID to search.
        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :param async_mode: Boolean flag for asynchronous mode.
        :return: Iterator over fixture data.
        """
        return self._get(
            f"leagues/teams/{team_id}",
            params={"include": includes, "select": selects, "filter": filters},
            async_mode=async_mode,
        )

    def get_current_leagues_by_team(
        self,
        team_id: int,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
        async_mode: bool = False,
    ) -> StdResponse | AsyncResponse:
        """
        Returns all the current leagues of your requested team id.

        :param team_id: Team ID to search.
        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :param async_mode: Boolean flag for asynchronous mode.
        :return: Iterator over fixture data.
        """
        return self._get(
            f"leagues/teams/{team_id}/current",
            params={"include": includes, "select": selects, "filter": filters},
            async_mode=async_mode,
        )

    def get_all_seasons(
        self,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
        async_mode: bool = False,
    ) -> StdResponse | AsyncResponse:
        """
        Returns all the seasons available within your subscription

        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :param async_mode: Boolean flag for asynchronous mode.
        :return: Iterator over fixture data.
        """

        return self._get(
            "seasons",
            params={"include": includes, "select": selects, "filter": filters},
            async_mode=async_mode,
        )

    def get_season(
        self,
        season_id: int,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
        async_mode: bool = False,
    ) -> StdResponse | AsyncResponse:
        """
        Returns the league you've requested by ID.

        :param season_id: Int
        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :param async_mode: Boolean flag for asynchronous mode.
        :return: Iterator over fixture data.
        :raises ValueError: If no fixture IDs are provided.
        """

        if not season_id:
            raise ValueError("You must provide a League ID")

        return self._get(
            f"seasons/{season_id}",
            params={"include": includes, "select": selects, "filter": filters},
            async_mode=async_mode,
        )

    def get_season_by_team_id(
        self,
        team_id: int,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
        async_mode: bool = False,
    ) -> StdResponse | AsyncResponse:
        """
        Returns seasons by team ID.

        :param team_id: Int
        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :param async_mode: Boolean flag for asynchronous mode.
        :raises InvalidDateFormat: If a date is in an invalid format.
        :return: Iterator over fixture data.
        """

        if not team_id:
            raise ValueError("Country ID not supplied")

        return self._get(
            f"seasons/{team_id}",
            params={"include": includes, "select": selects, "filter": filters},
            async_mode=async_mode,
        )

    def search_seasons(
        self,
        search: Union[int, str],
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
        async_mode: bool = False,
    ) -> StdResponse | AsyncResponse:
        """
        Returns all the seasons that match your search.

        :param search: String or ID to search.
        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :param async_mode: Boolean flag for asynchronous mode.
        :return: Iterator over fixture data.
        """
        return self._get(
            f"seasons/search/{search}",
            params={"include": includes, "select": selects, "filter": filters},
            async_mode=async_mode,
        )

    def get_all_stages(
        self,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
        async_mode: bool = False,
    ) -> StdResponse | AsyncResponse:
        """
        Returns all stages available within your subscription

        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :param async_mode: Boolean flag for asynchronous mode.
        :return: Iterator over fixture data.
        """
        return self._get(
            "stages",
            params={"include": includes, "select": selects, "filter": filters},
            async_mode=async_mode,
        )

    def get_stage_by_id(
        self,
        stage_id: int,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
        async_mode: bool = False,
    ) -> StdResponse | AsyncResponse:
        """
        Returns stage information from your requested stage ID.

        :param stage_id: Int
        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :param async_mode: Boolean flag for asynchronous mode.
        :raises InvalidDateFormat: If a date is in an invalid format.
        :return: Iterator over fixture data.
        """

        if not stage_id:
            raise ValueError("Country ID not supplied")

        return self._get(
            f"stages/{stage_id}",
            params={"include": includes, "select": selects, "filter": filters},
            async_mode=async_mode,
        )

    def get_stages_by_season_id(
        self,
        season_id: int,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
        async_mode: bool = False,
    ) -> StdResponse | AsyncResponse:
        """
        Returns stage information from your requested stage ID.

        :param season_id: Int
        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :param async_mode: Boolean flag for asynchronous mode.
        :raises InvalidDateFormat: If a date is in an invalid format.
        :return: Iterator over fixture data.
        """

        if not season_id:
            raise ValueError("Country ID not supplied")

        return self._get(
            f"stages/seasons/{season_id}",
            params={"include": includes, "select": selects, "filter": filters},
            async_mode=async_mode,
        )

    def search_stages(
        self,
        search: Union[int, str],
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
        async_mode: bool = False,
    ) -> StdResponse | AsyncResponse:
        """
        Returns all stages that matches your search.

        :param search: String or ID to search.
        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :param async_mode: Boolean flag for asynchronous mode.
        :return: Iterator over fixture data.
        """
        return self._get(
            f"stages/search/{search}",
            params={"include": includes, "select": selects, "filter": filters},
            async_mode=async_mode,
        )

    def get_all_rounds(
        self,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
        async_mode: bool = False,
    ) -> StdResponse | AsyncResponse:
        """
        Returns all the rounds available within your subscription.

        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :param async_mode: Boolean flag for asynchronous mode.
        :return: Iterator over fixture data.
        """
        return self._get(
            "rounds",
            params={"include": includes, "select": selects, "filter": filters},
            async_mode=async_mode,
        )

    def get_round(
        self,
        round_id: int,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
        async_mode: bool = False,
    ) -> StdResponse | AsyncResponse:
        """
        Returns round information from your requested round ID.

        :param round_id: Int
        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :param async_mode: Boolean flag for asynchronous mode.
        :return: Iterator over fixture data.
        """
        if not round_id:
            raise ValueError("A Round ID is required")

        return self._get(
            f"rounds/{round_id}",
            params={"include": includes, "select": selects, "filter": filters},
            async_mode=async_mode,
        )

    def get_round_by_season_id(
        self,
        season_id: int,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
        async_mode: bool = False,
    ) -> StdResponse | AsyncResponse:
        """
        Returns round information from your requested round ID.

        :param season_id: Int
        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :param async_mode: Boolean flag for asynchronous mode.
        :return: Iterator over fixture data.
        """
        if not season_id:
            raise ValueError("A Season ID is required")

        return self._get(
            f"rounds/{season_id}",
            params={"include": includes, "select": selects, "filter": filters},
            async_mode=async_mode,
        )

    def search_rounds(
        self,
        search: Union[int, str],
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
        async_mode: bool = False,
    ) -> StdResponse | AsyncResponse:
        """
        Returns all stages that matches your search

        :param search: String or ID to search.
        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :param async_mode: Boolean flag for asynchronous mode.
        :return: Iterator over fixture data.
        """
        if not search:
            raise ValueError("A search string must be supplied")
        return self._get(
            f"rounds/search/{search}",
            params={"include": includes, "select": selects, "filter": filters},
            async_mode=async_mode,
        )
