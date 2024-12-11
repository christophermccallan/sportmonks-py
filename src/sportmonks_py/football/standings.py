from typing import Dict, Any, Iterator, Optional

from sportmonks_py.base_client import BaseClient
from sportmonks_py.core.common_types import Includes, Selects, Filters


class StandingsClient(BaseClient):
    def get_all_standings(
        self,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
    ) -> Iterator[Dict[str, Any]]:
        """
        Returns all standings

        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :return: Iterator over fixture data.
        """

        return self._get(
            "standings",
            params={"include": includes, "select": selects, "filter": filters},
        )

    def get_season_standings(
        self,
        season_id: int,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
    ) -> Iterator[Dict[str, Any]]:
        """
        Returns the full league standing table from your requested season ID.

        :param season_id: Int
        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :return: Iterator over fixture data.
        """

        if not season_id:
            raise ValueError("Season ID must be provided")

        return self._get(
            f"standings/seasons/{season_id}",
            params={"include": includes, "select": selects, "filter": filters},
        )

    def get_standings_by_round(
        self,
        round_id: int,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
    ) -> Iterator[Dict[str, Any]]:
        """
        Returns the full league standing table from your requested round ID.

        :param round_id: Int
        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :return: Iterator over fixture data.
        """

        if not round_id:
            raise ValueError("Round ID must be provided")

        return self._get(
            f"standings/rounds/{round_id}",
            params={"include": includes, "select": selects, "filter": filters},
        )

    def get_standings_corrections(
        self,
        season_id: int,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
    ) -> Iterator[Dict[str, Any]]:
        """
        Returns the standing corrections from your requested season ID.

        :param season_id: Int
        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :return: Iterator over fixture data.
        """

        if not season_id:
            raise ValueError("Round ID must be provided")

        return self._get(
            f"standings/corrections/seasons/{season_id}",
            params={"include": includes, "select": selects, "filter": filters},
        )

    def get_live_standings_by_league(
        self,
        league_id: int,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
    ) -> Iterator[Dict[str, Any]]:
        """
        Returns the LIVE league standing table from your requested league ID.

        :param league_id: Int
        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :return: Iterator over fixture data.
        """

        if not league_id:
            raise ValueError("Round ID must be provided")

        return self._get(
            f"standings/live/leagues/{league_id}",
            params={"include": includes, "select": selects, "filter": filters},
        )

    def get_topscorers_by_season(
        self,
        season_id: int,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
    ) -> Iterator[Dict[str, Any]]:
        """
        This endpoint returns all the topscorers per stage of the requested season

        :param season_id: Int
        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :return: Iterator over fixture data.
        """

        if not season_id:
            raise ValueError("Round ID must be provided")

        return self._get(
            f"topscorers/seasons/{season_id}",
            params={"include": includes, "select": selects, "filter": filters},
        )

    def get_topscorers_by_stage(
        self,
        stage_id: int,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
    ) -> Iterator[Dict[str, Any]]:
        """
        This endpoint returns all the topscorers from your requested stage ID.

        :param stage_id: Int
        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :return: Iterator over fixture data.
        """

        if not stage_id:
            raise ValueError("Round ID must be provided")

        return self._get(
            f"topscorers/stages/{stage_id}",
            params={"include": includes, "select": selects, "filter": filters},
        )
