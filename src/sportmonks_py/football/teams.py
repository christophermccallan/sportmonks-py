from typing import Dict, Any, Iterator, Optional

from sportmonks_py.base_client import BaseClient
from sportmonks_py.core.common_types import Includes, Selects, Filters


class TeamsClient(BaseClient):
    """
    Client for accessing team, player, coach, squad, and referee data via the SportMonks API.
    """

    def get_teams(
        self,
        team_id: Optional[int] = None,
        country_id: Optional[int] = None,
        season_id: Optional[int] = None,
        query: Optional[str] = None,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
    ) -> Iterator[Dict[str, Any]]:
        """
        Retrieve team information based on various criteria.

        :param team_id: ID of the team (optional).
        :param country_id: ID of the country to filter teams by (optional).
        :param season_id: ID of the season to filter teams by (optional).
        :param query: Search query for team names (optional).
        :param includes: Objects to include in the response (optional).
        :param selects: Fields to include or exclude in the response (optional).
        :param filters: Filters to apply to the results (optional).
        :return: Iterator of team data.
        """
        if team_id:
            return self._get(
                f"teams/{team_id}",
                params={"include": includes, "select": selects, "filter": filters},
            )
        if country_id:
            return self._get(
                f"teams/countries/{country_id}",
                params={"include": includes, "select": selects, "filter": filters},
            )
        if season_id:
            return self._get(
                f"teams/seasons/{season_id}",
                params={"include": includes, "select": selects, "filter": filters},
            )
        if query:
            return self._get(
                f"teams/search/{query}",
                params={"include": includes, "select": selects, "filter": filters},
            )
        return self._get(
            "teams", params={"include": includes, "select": selects, "filter": filters}
        )

    def get_players(
        self,
        player_id: Optional[int] = None,
        country_id: Optional[int] = None,
        query: Optional[str] = None,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
    ) -> Iterator[Dict[str, Any]]:
        """
        Retrieve player information based on various criteria.

        :param player_id: ID of the player (optional).
        :param country_id: ID of the country to filter players by (optional).
        :param query: Search query for player names (optional).
        :param includes: Objects to include in the response (optional).
        :param selects: Fields to include or exclude in the response (optional).
        :param filters: Filters to apply to the results (optional).
        :return: Iterator of player data.
        """
        if player_id:
            return self._get(
                f"players/{player_id}",
                params={"include": includes, "select": selects, "filter": filters},
            )
        if country_id:
            return self._get(
                f"players/countries/{country_id}",
                params={"include": includes, "select": selects, "filter": filters},
            )
        if query:
            return self._get(
                f"players/search/{query}",
                params={"include": includes, "select": selects, "filter": filters},
            )
        return self._get(
            "players",
            params={"include": includes, "select": selects, "filter": filters},
        )

    def get_players_latest(
        self,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
    ) -> Iterator[Dict[str, Any]]:
        """
        Retrieve all players updated within the last two hours.

        :param includes: Objects to include in the response (optional).
        :param selects: Fields to include or exclude in the response (optional).
        :param filters: Filters to apply to the results (optional).
        :return: Iterator of player data.
        """
        return self._get(
            "players/updated",
            params={"include": includes, "select": selects, "filter": filters},
        )

    def get_coaches(
        self,
        coach_id: Optional[int] = None,
        country_id: Optional[int] = None,
        query: Optional[str] = None,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
    ) -> Iterator[Dict[str, Any]]:
        """
        Retrieve coach information based on various criteria.

        :param coach_id: ID of the coach (optional).
        :param country_id: ID of the country to filter coaches by (optional).
        :param query: Search query for coach names (optional).
        :param includes: Objects to include in the response (optional).
        :param selects: Fields to include or exclude in the response (optional).
        :param filters: Filters to apply to the results (optional).
        :return: Iterator of coach data.
        """
        if coach_id:
            return self._get(
                f"coaches/{coach_id}",
                params={"include": includes, "select": selects, "filter": filters},
            )
        if country_id:
            return self._get(
                f"coaches/countries/{country_id}",
                params={"include": includes, "select": selects, "filter": filters},
            )
        if query:
            return self._get(
                f"coaches/search/{query}",
                params={"include": includes, "select": selects, "filter": filters},
            )
        return self._get(
            "coaches",
            params={"include": includes, "select": selects, "filter": filters},
        )

    def get_coaches_latest(
        self,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
    ) -> Iterator[Dict[str, Any]]:
        """
        Retrieve all coaches updated within the last two hours.

        :param includes: Objects to include in the response (optional).
        :param selects: Fields to include or exclude in the response (optional).
        :param filters: Filters to apply to the results (optional).
        :return: Iterator of coach data.
        """
        return self._get(
            "coaches/updated",
            params={"include": includes, "select": selects, "filter": filters},
        )

    def get_team_squad(
        self,
        team_id: int,
        season_id: Optional[int] = None,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
    ) -> Iterator[Dict[str, Any]]:
        """
        Retrieve a team's squad for a specific season.

        :param team_id: ID of the team.
        :param season_id: ID of the season (optional).
        :param includes: Objects to include in the response (optional).
        :param selects: Fields to include or exclude in the response (optional).
        :param filters: Filters to apply to the results (optional).
        :return: Iterator of squad data.
        """
        if not season_id:
            return self._get(
                f"squads/teams/{team_id}",
                params={"include": includes, "select": selects, "filter": filters},
            )
        return self._get(
            f"squads/seasons/{season_id}/teams/{team_id}",
            params={"include": includes, "select": selects, "filter": filters},
        )

    def get_referee(
        self,
        referee_id: Optional[int] = None,
        country_id: Optional[int] = None,
        season_id: Optional[int] = None,
        query: Optional[str] = None,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
    ) -> Iterator[Dict[str, Any]]:
        """
        Retrieve referee information based on various criteria.

        :param referee_id: ID of the referee (optional).
        :param country_id: ID of the country to filter referees by (optional).
        :param season_id: ID of the season to filter referees by (optional).
        :param query: Search query for referee names (optional).
        :param includes: Objects to include in the response (optional).
        :param selects: Fields to include or exclude in the response (optional).
        :param filters: Filters to apply to the results (optional).
        :return: Iterator of referee data.
        """
        if referee_id:
            return self._get(
                f"referees/{referee_id}",
                params={"include": includes, "select": selects, "filter": filters},
            )
        if query:
            return self._get(
                f"referees/search/{query}",
                params={"include": includes, "select": selects, "filter": filters},
            )

        return self._get(
            "referees",
            params={"include": includes, "select": selects, "filter": filters},
        )
