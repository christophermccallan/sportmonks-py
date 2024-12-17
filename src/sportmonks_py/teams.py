from typing import Optional, Union

from sportmonks_py.client.base_client import BaseClient
from sportmonks_py.utils.common_types import (
    Includes,
    Selects,
    Filters,
    StdResponse,
    AsyncResponse,
    Ordering,
)


class TeamsClient(BaseClient):
    """
    Client for accessing team, player, coach, squad, and referee data via the SportMonks API.
    """

    def __init__(self, base_url: str, api_token: str) -> None:
        """
        Initialize the Teams Client with a base_url, sport and API token.

        :param api_token: API token for authenticating requests.
        :param base_url: Base URL for the API.
        """
        super().__init__(base_url=base_url, api_token=api_token)

    def get_teams(
        self,
        team_id: Optional[int] = None,
        country_id: Optional[int] = None,
        season_id: Optional[int] = None,
        search: Optional[str] = None,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
        async_mode: bool = False,
        locale: Optional[str] = None,
        order: Optional[Ordering] = None,
    ) -> Union[StdResponse, AsyncResponse]:
        """
        Retrieve team information based on various criteria.

        :param team_id: ID of the team (optional).
        :param country_id: ID of the country to filter teams by (optional).
        :param season_id: ID of the season to filter teams by (optional).
        :param search: Search string for team names (optional).
        :param includes: Objects to include in the response (optional).
        :param selects: Fields to include or exclude in the response (optional).
        :param filters: Filters to apply to the results (optional).
        :param async_mode: Whether to use async mode.
        :param locale: Language to use for the response (optional).
        :param order: Order to sort the results in (asc or desc).

        :return: StdResponse | AsyncResponse
        """
        if team_id:
            return self._get(
                f"teams/{team_id}",
                params={"include": includes, "select": selects, "filter": filters},
                async_mode=async_mode,
                locale=locale,
                order=order,
            )
        if country_id:
            return self._get(
                f"teams/countries/{country_id}",
                params={"include": includes, "select": selects, "filter": filters},
                async_mode=async_mode,
                locale=locale,
                order=order,
            )
        if season_id:
            return self._get(
                f"teams/seasons/{season_id}",
                params={"include": includes, "select": selects, "filter": filters},
                async_mode=async_mode,
                locale=locale,
                order=order,
            )
        if search:
            return self._get(
                f"teams/search/{search}",
                params={"include": includes, "select": selects, "filter": filters},
                async_mode=async_mode,
                locale=locale,
                order=order,
            )
        return self._get(
            "teams",
            params={"include": includes, "select": selects, "filter": filters},
            async_mode=async_mode,
            locale=locale,
            order=order,
        )

    def get_players(
        self,
        player_id: Optional[int] = None,
        country_id: Optional[int] = None,
        search: Optional[str] = None,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
        async_mode: bool = False,
        locale: Optional[str] = None,
        order: Optional[Ordering] = None,
    ) -> Union[StdResponse, AsyncResponse]:
        """
        Retrieve player information based on various criteria.

        :param player_id: ID of the player (optional).
        :param country_id: ID of the country to filter players by (optional).
        :param search: Search string for player names (optional).
        :param includes: Objects to include in the response (optional).
        :param selects: Fields to include or exclude in the response (optional).
        :param filters: Filters to apply to the results (optional).
        :param async_mode: Whether to use async mode.
        :param locale: Language to use for the response (optional).
        :param order: Order to sort the results in (asc or desc).

        :return: StdResponse | AsyncResponse
        """
        if player_id:
            return self._get(
                f"players/{player_id}",
                params={"include": includes, "select": selects, "filter": filters},
                async_mode=async_mode,
                locale=locale,
                order=order,
            )
        if country_id:
            return self._get(
                f"players/countries/{country_id}",
                params={"include": includes, "select": selects, "filter": filters},
                async_mode=async_mode,
                locale=locale,
                order=order,
            )
        if search:
            return self._get(
                f"players/search/{search}",
                params={"include": includes, "select": selects, "filter": filters},
                async_mode=async_mode,
                locale=locale,
                order=order,
            )
        return self._get(
            "players",
            params={"include": includes, "select": selects, "filter": filters},
            async_mode=async_mode,
            locale=locale,
            order=order,
        )

    def get_players_latest(
        self,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
        async_mode: bool = False,
        locale: Optional[str] = None,
        order: Optional[Ordering] = None,
    ) -> Union[StdResponse, AsyncResponse]:
        """
        Retrieve all players updated within the last two hours.

        :param includes: Objects to include in the response (optional).
        :param selects: Fields to include or exclude in the response (optional).
        :param filters: Filters to apply to the results (optional).
        :param async_mode: Whether to use async mode.
        :param locale: Language to use for the response (optional).
        :param order: Order to sort the results in (asc or desc).

        :return: StdResponse | AsyncResponse
        """
        return self._get(
            "players/latest",
            params={"include": includes, "select": selects, "filter": filters},
            async_mode=async_mode,
            locale=locale,
            order=order,
        )

    def get_coaches(
        self,
        coach_id: Optional[int] = None,
        country_id: Optional[int] = None,
        search: Optional[str] = None,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
        async_mode: bool = False,
        locale: Optional[str] = None,
        order: Optional[Ordering] = None,
    ) -> Union[StdResponse, AsyncResponse]:
        """
        Retrieve coach information based on various criteria.

        :param coach_id: ID of the coach (optional).
        :param country_id: ID of the country to filter coaches by (optional).
        :param search: Search string for coach names (optional).
        :param includes: Objects to include in the response (optional).
        :param selects: Fields to include or exclude in the response (optional).
        :param filters: Filters to apply to the results (optional).
        :param async_mode: Whether to use async mode.
        :param locale: Language to use for the response (optional).
        :param order: Order to sort the results in (asc or desc).

        :return: StdResponse | AsyncResponse
        """
        if coach_id:
            return self._get(
                f"coaches/{coach_id}",
                params={"include": includes, "select": selects, "filter": filters},
                async_mode=async_mode,
                locale=locale,
                order=order,
            )
        if country_id:
            return self._get(
                f"coaches/countries/{country_id}",
                params={"include": includes, "select": selects, "filter": filters},
                async_mode=async_mode,
                locale=locale,
                order=order,
            )
        if search:
            return self._get(
                f"coaches/search/{search}",
                params={"include": includes, "select": selects, "filter": filters},
                async_mode=async_mode,
                locale=locale,
                order=order,
            )
        return self._get(
            "coaches",
            params={"include": includes, "select": selects, "filter": filters},
            async_mode=async_mode,
            locale=locale,
            order=order,
        )

    def get_coaches_latest(
        self,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
        async_mode: bool = False,
        locale: Optional[str] = None,
        order: Optional[Ordering] = None,
    ) -> Union[StdResponse, AsyncResponse]:
        """
        Retrieve all coaches updated within the last two hours.

        :param includes: Objects to include in the response (optional).
        :param selects: Fields to include or exclude in the response (optional).
        :param filters: Filters to apply to the results (optional).
        :param async_mode: Whether to use async mode.
        :param locale: Language to use for the response (optional).
        :param order: Order to sort the results in (asc or desc).

        :return: StdResponse | AsyncResponse
        """
        return self._get(
            "coaches/updated",
            params={"include": includes, "select": selects, "filter": filters},
            async_mode=async_mode,
            locale=locale,
            order=order,
        )

    def get_team_squad(
        self,
        team_id: int,
        season_id: Optional[int] = None,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
        async_mode: bool = False,
        locale: Optional[str] = None,
        order: Optional[Ordering] = None,
    ) -> Union[StdResponse, AsyncResponse]:
        """
        Retrieve a team's squad for a specific season.

        :param team_id: ID of the team.
        :param season_id: ID of the season (optional).
        :param includes: Objects to include in the response (optional).
        :param selects: Fields to include or exclude in the response (optional).
        :param filters: Filters to apply to the results (optional).
        :param async_mode: Whether to use async mode.
        :param locale: Language to use for the response (optional).
        :param order: Order to sort the results in (asc or desc).

        :return: StdResponse | AsyncResponse
        """
        if not season_id:
            return self._get(
                f"squads/teams/{team_id}",
                params={"include": includes, "select": selects, "filter": filters},
                async_mode=async_mode,
                locale=locale,
                order=order,
            )
        return self._get(
            f"squads/seasons/{season_id}/teams/{team_id}",
            params={"include": includes, "select": selects, "filter": filters},
            async_mode=async_mode,
            locale=locale,
            order=order,
        )

    def get_referee(
        self,
        referee_id: Optional[int] = None,
        country_id: Optional[int] = None,
        season_id: Optional[int] = None,
        search: Optional[str] = None,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
        async_mode: bool = False,
        locale: Optional[str] = None,
        order: Optional[Ordering] = None,
    ) -> Union[StdResponse, AsyncResponse]:
        """
        Retrieve referee information based on various criteria.

        :param referee_id: ID of the referee (optional).
        :param country_id: ID of the country to filter referees by (optional).
        :param season_id: ID of the season to filter referees by (optional).
        :param search: Search string for referee names (optional).
        :param includes: Objects to include in the response (optional).
        :param selects: Fields to include or exclude in the response (optional).
        :param filters: Filters to apply to the results (optional).
        :param async_mode: Whether to use async mode.
        :param locale: Language to use for the response (optional).
        :param order: Order to sort the results in (asc or desc).

        :return: StdResponse | AsyncResponse
        """
        if referee_id:
            return self._get(
                f"referees/{referee_id}",
                params={"include": includes, "select": selects, "filter": filters},
                async_mode=async_mode,
                locale=locale,
                order=order,
            )
        if country_id:
            return self._get(
                f"referees/countries/{country_id}",
                params={"include": includes, "select": selects, "filter": filters},
                async_mode=async_mode,
                locale=locale,
                order=order,
            )
        if search:
            return self._get(
                f"referees/search/{search}",
                params={"include": includes, "select": selects, "filter": filters},
                async_mode=async_mode,
                locale=locale,
                order=order,
            )
        if season_id:
            return self._get(
                f"referees/seasons/{season_id}",
                params={"include": includes, "select": selects, "filter": filters},
                async_mode=async_mode,
                locale=locale,
                order=order,
            )
        return self._get(
            "referees",
            params={"include": includes, "select": selects, "filter": filters},
            async_mode=async_mode,
            locale=locale,
            order=order,
        )
