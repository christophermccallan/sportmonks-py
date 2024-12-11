from typing import Dict, Any, Iterator, Optional

from sportmonks_py.base_client import BaseClient
from sportmonks_py.core.common_types import Includes, Selects, Filters


class OtherClient(BaseClient):
    """
    A client for accessing fixture-related data from the SportMonks API.
    """

    def __init__(self, api_token: str, base_url: str) -> None:
        """
        Initialize the FixturesClient with an API token and base URL.

        :param api_token: API token for authenticating requests.
        :param base_url: Base URL for the API.
        """
        super().__init__(api_token=api_token, base_url=base_url)

    def get_prematch_news(
        self,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
    ) -> Iterator[Dict[str, Any]]:
        """
        This endpoint returns all the available pre-match news articles within your subscription

        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :return: Iterator over fixture data.
        """

        return self._get(
            "news/prematch",
            params={"include": includes, "select": selects, "filter": filters},
        )

    def get_prematch_news_by_season(
        self,
        season_id: int,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
    ) -> Iterator[Dict[str, Any]]:
        """
        This endpoint returns all pre-match news articles from your requested season ID.

        :param season_id: ID to retrieve.
        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :return: Iterator over fixture data.
        """

        if not season_id:
            raise ValueError("Season ID must be provided")

        return self._get(
            f"news/prematch/seasons/{season_id}",
            params={"include": includes, "select": selects, "filter": filters},
        )

    def get_upcoming_prematch_news(
        self,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
    ) -> Iterator[Dict[str, Any]]:
        """
        This endpoint returns all pre-match news articles for the upcoming fixtures within your subscription.

        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :return: Iterator over fixture data.
        """

        return self._get(
            "news/prematch/upcoming",
            params={"include": includes, "select": selects, "filter": filters},
        )

    def get_postmatch_news(
        self,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
    ) -> Iterator[Dict[str, Any]]:
        """
        This endpoint returns all the available post-match news articles within your subscription.

        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :return: Iterator over fixture data.
        """

        return self._get(
            "news/postmatch",
            params={"include": includes, "select": selects, "filter": filters},
        )

    def get_postmatch_news_by_season(
        self,
        season_id: int,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
    ) -> Iterator[Dict[str, Any]]:
        """
        This endpoint returns all post-match news articles from your requested season ID.

        :param season_id: ID to retrieve.
        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :return: Iterator over fixture data.
        """

        if not season_id:
            raise ValueError("Season ID must be provided")

        return self._get(
            f"news/postmatch/seasons/{season_id}",
            params={"include": includes, "select": selects, "filter": filters},
        )

    def get_rivals(
        self,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
    ) -> Iterator[Dict[str, Any]]:
        """
        This endpoint returns all the teams within your subscription with the rivals information (if available).

        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :return: Iterator over fixture data.
        """

        return self._get(
            "rivals",
            params={"include": includes, "select": selects, "filter": filters},
        )

    def get_team_rivals(
        self,
        team_id: int,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
    ) -> Iterator[Dict[str, Any]]:
        """
        This endpoint returns the rivals of your requested team ID (if available).

        :param team_id: Int
        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :return: Iterator over fixture data.
        """

        if not team_id:
            raise ValueError("Team ID must be provided.")

        return self._get(
            f"teams/rivals/{team_id}",
            params={"include": includes, "select": selects, "filter": filters},
        )

    def get_commentaries(
        self,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
    ) -> Iterator[Dict[str, Any]]:
        """
        Returns a textual representation of commentaries

        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :return: Iterator over fixture data.
        """

        return self._get(
            "commentaries",
            params={"include": includes, "select": selects, "filter": filters},
        )

    def get_fixture_commentary(
        self,
        fixture_id: int,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
    ) -> Iterator[Dict[str, Any]]:
        """
        RReturns a textual representation from the requested fixture ID.

        :param fixture_id: int
        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :return: Iterator over fixture data.
        """

        if not fixture_id:
            raise ValueError("Fixture ID is required")

        return self._get(
            "commentaries",
            params={"include": includes, "select": selects, "filter": filters},
        )
