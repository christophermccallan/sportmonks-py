from typing import Union, Dict, Any, Iterator, Optional

from sportmonks_py.base_client import BaseClient
from sportmonks_py.core.common_types import Includes, Selects, Filters

from ..core.custom_exceptions import InvalidDateFormat
from ..core.utils import validate_date_format


class LeaguesClient(BaseClient):
    """
    A client for accessing league-related data from the SportMonks API.
    """

    def __init__(self, api_token: str, base_url: str) -> None:
        """
        Initialize the FixturesClient with an API token and base URL.

        :param api_token: API token for authenticating requests.
        :param base_url: Base URL for the API.
        """
        super().__init__(api_token=api_token, base_url=base_url)

    def get_all_leagues(
        self,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
    ) -> Iterator[Dict[str, Any]]:
        """
        Returns all the leagues available within your subscription

        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :return: Iterator over fixture data.
        """
        return self._get(
            "leagues",
            params={"include": includes, "select": selects, "filter": filters},
        )

    def get_league(
        self,
        league_id: int,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
    ) -> Iterator[Dict[str, Any]]:
        """
        Returns the league you've requested by ID.

        :param league_id: Int
        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :return: Iterator over fixture data.
        :raises ValueError: If no fixture IDs are provided.
        """

        if not league_id:
            raise ValueError("You must provide a League ID")

        return self._get(
            f"leagues/{league_id}",
            params={"include": includes, "select": selects, "filter": filters},
        )

    def get_live_leagues(
        self,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
    ) -> Iterator[Dict[str, Any]]:
        """
        Returns all the leagues that with fixtures that are currently being played.

        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :return: Iterator over fixture data.
        """

        return self._get(
            "leagues/live",
            params={"include": includes, "select": selects, "filter": filters},
        )

    def get_league_by_fixture_date(
        self,
        date: str,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
    ) -> Iterator[Dict[str, Any]]:
        """
        Returns all the leagues with fixtures from your requested fixture date.

        :param date: Date in 'YYYY-MM-DD' format.
        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :raises InvalidDateFormat: If a date is in an invalid format.
        :return: Iterator over fixture data.
        """

        if not validate_date_format(date):
            raise InvalidDateFormat(f"Invalid date format: '{date}'.")

        return self._get(
            f"leagues/fixtures/{date}",
            params={"include": includes, "select": selects, "filter": filters},
        )

    def get_leagues_by_country_id(
        self,
        country_id: int,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
    ) -> Iterator[Dict[str, Any]]:
        """
        Returns all the leagues with fixtures from your requested fixture date.

        :param country_id: Int
        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :raises InvalidDateFormat: If a date is in an invalid format.
        :return: Iterator over fixture data.
        """

        if not country_id:
            raise ValueError("Country ID not supplied")

        return self._get(
            f"leagues/countries/{country_id}",
            params={"include": includes, "select": selects, "filter": filters},
        )

    def get_leagues_query(
        self,
        query: Union[int, str],
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
    ) -> Iterator[Dict[str, Any]]:
        """
        Returns all the leagues that match your search query.

        :param query: Query string or ID to search.
        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :return: Iterator over fixture data.
        """
        return self._get(
            f"leagues/search/{query}",
            params={"include": includes, "select": selects, "filter": filters},
        )

    def get_all_leagues_by_team(
        self,
        team_id: int,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
    ) -> Iterator[Dict[str, Any]]:
        """
        Returns all the current and historical leagues from your requested team id.

        :param team_id: Team ID to search.
        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :return: Iterator over fixture data.
        """
        return self._get(
            f"leagues/teams/{team_id}",
            params={"include": includes, "select": selects, "filter": filters},
        )

    def get_current_leagues_by_team(
        self,
        team_id: int,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
    ) -> Iterator[Dict[str, Any]]:
        """
        Returns all the current leagues of your requested team id.

        :param team_id: Team ID to search.
        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :return: Iterator over fixture data.
        """
        return self._get(
            f"leagues/teams/{team_id}/current",
            params={"include": includes, "select": selects, "filter": filters},
        )

    def get_all_seasons(
        self,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
    ) -> Iterator[Dict[str, Any]]:
        """
        Returns all the seasons available within your subscription

        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :return: Iterator over fixture data.
        """

        return self._get(
            "seasons",
            params={"include": includes, "select": selects, "filter": filters},
        )

    def get_season(
        self,
        season_id: int,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
    ) -> Iterator[Dict[str, Any]]:
        """
        Returns the league you've requested by ID.

        :param season_id: Int
        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :return: Iterator over fixture data.
        :raises ValueError: If no fixture IDs are provided.
        """

        if not season_id:
            raise ValueError("You must provide a League ID")

        return self._get(
            f"seasons/{season_id}",
            params={"include": includes, "select": selects, "filter": filters},
        )

    def get_season_by_team_id(
        self,
        team_id: int,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
    ) -> Iterator[Dict[str, Any]]:
        """
        Returns seasons by team ID.

        :param team_id: Int
        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :raises InvalidDateFormat: If a date is in an invalid format.
        :return: Iterator over fixture data.
        """

        if not team_id:
            raise ValueError("Country ID not supplied")

        return self._get(
            f"seasons/{team_id}",
            params={"include": includes, "select": selects, "filter": filters},
        )

    def get_seasons_query(
        self,
        query: Union[int, str],
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
    ) -> Iterator[Dict[str, Any]]:
        """
        Returns all the seasons that match your search query.

        :param query: Query string or ID to search.
        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :return: Iterator over fixture data.
        """
        return self._get(
            f"seasons/search/{query}",
            params={"include": includes, "select": selects, "filter": filters},
        )

    def get_all_stages(
        self,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
    ) -> Iterator[Dict[str, Any]]:
        """
        Returns all stages available within your subscription

        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :return: Iterator over fixture data.
        """
        return self._get(
            "stages",
            params={"include": includes, "select": selects, "filter": filters},
        )

    def get_stage_by_id(
        self,
        stage_id: int,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
    ) -> Iterator[Dict[str, Any]]:
        """
        Returns stage information from your requested stage ID.

        :param stage_id: Int
        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :raises InvalidDateFormat: If a date is in an invalid format.
        :return: Iterator over fixture data.
        """

        if not stage_id:
            raise ValueError("Country ID not supplied")

        return self._get(
            f"stages/{stage_id}",
            params={"include": includes, "select": selects, "filter": filters},
        )

    def get_stages_by_season_id(
        self,
        season_id: int,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
    ) -> Iterator[Dict[str, Any]]:
        """
        Returns stage information from your requested stage ID.

        :param season_id: Int
        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :raises InvalidDateFormat: If a date is in an invalid format.
        :return: Iterator over fixture data.
        """

        if not season_id:
            raise ValueError("Country ID not supplied")

        return self._get(f"stages/seasons/{season_id}")

    def get_stages_query(
        self,
        query: Union[int, str],
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
    ) -> Iterator[Dict[str, Any]]:
        """
        Returns all stages that matches your search query

        :param query: Query string or ID to search.
        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :return: Iterator over fixture data.
        """
        return self._get(
            f"stages/search/{query}",
            params={"include": includes, "select": selects, "filter": filters},
        )

    def get_all_rounds(
        self,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
    ) -> Iterator[Dict[str, Any]]:
        """
        Returns all the rounds available within your subscription.

        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :return: Iterator over fixture data.
        """
        return self._get(
            "rounds",
            params={"include": includes, "select": selects, "filter": filters},
        )

    def get_round(
        self,
        round_id: int,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
    ) -> Iterator[Dict[str, Any]]:
        """
        Returns round information from your requested round ID.

        :param round_id: Int
        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :return: Iterator over fixture data.
        """
        if not round_id:
            raise ValueError("A Round ID is required")

        return self._get(
            f"rounds/{round_id}",
            params={"include": includes, "select": selects, "filter": filters},
        )

    def get_round_by_season_id(
        self,
        season_id: int,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
    ) -> Iterator[Dict[str, Any]]:
        """
        Returns round information from your requested round ID.

        :param season_id: Int
        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :return: Iterator over fixture data.
        """
        if not season_id:
            raise ValueError("A Season ID is required")

        return self._get(
            f"rounds/{season_id}",
            params={"include": includes, "select": selects, "filter": filters},
        )

    def get_rounds_query(
        self,
        query: Union[int, str],
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
    ) -> Iterator[Dict[str, Any]]:
        """
        Returns all stages that matches your search query

        :param query: Query string or ID to search.
        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :return: Iterator over fixture data.
        """
        if not query:
            raise ValueError("A query string must be supplied")
        return self._get(
            f"rounds/search/{query}",
            params={"include": includes, "select": selects, "filter": filters},
        )
