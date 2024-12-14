from typing import Optional, Union

from sportmonks_py.base_client import BaseClient
from sportmonks_py.utils.common_types import Includes, Selects, Filters, StdResponse, AsyncResponse


class OddsClient(BaseClient):
    """
    A client for accessing odds-related data from the SportMonks API.
    """

    def __init__(self, base_url: str, api_token: str) -> None:
        """
        Initialize the Odds Client with a base_url, sport and API token.

        :param api_token: API token for authenticating requests.
        :param base_url: Base URL for the API.
        """
        super().__init__(base_url=base_url, api_token=api_token)

    def get_all_prematch_odds(
        self,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
        async_mode: bool = False,
    ) -> Union[StdResponse, AsyncResponse]:
        """
        Retrieve all available pre-match odds.

        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :param async_mode: Whether to use async mode.
        :return: Iterator over pre-match odds data.
        """
        return self._get(
            "odds/pre-match",
            params={"include": includes, "select": selects, "filter": filters},
            async_mode=async_mode,
        )

    def get_fixture_prematch_odds(
        self,
        fixture_id: int,
        bookmaker_id: Optional[int] = None,
        market_id: Optional[int] = None,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
        async_mode: bool = False,
    ) -> Union[StdResponse, AsyncResponse]:
        """
        Retrieve pre-match odds for a specific fixture. Optionally filter by bookmaker or market.

        :param fixture_id: ID of the fixture.
        :param bookmaker_id: (Optional) ID of the bookmaker.
        :param market_id: (Optional) ID of the market.
        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :param async_mode: Whether to use async mode.
        :return: Iterator over pre-match odds data.
        """
        if bookmaker_id:
            return self._get(
                f"odds/pre-match/fixtures/{fixture_id}/bookmakers/{bookmaker_id}",
                params={"include": includes, "select": selects, "filter": filters},
                async_mode=async_mode,
            )
        if market_id:
            return self._get(
                f"odds/pre-match/fixtures/{fixture_id}/markets/{market_id}",
                params={"include": includes, "select": selects, "filter": filters},
                async_mode=async_mode,
            )
        return self._get(
            f"odds/pre-match/fixtures/{fixture_id}",
            params={"include": includes, "select": selects, "filter": filters},
            async_mode=async_mode,
        )

    def get_latest_prematch_odds(
        self,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
        async_mode: bool = False,
    ) -> Union[StdResponse, AsyncResponse]:
        """
        Retrieve pre-match odds for fixtures updated within the last 10 seconds.

        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :param async_mode: Whether to use async mode.
        :return: Iterator over updated pre-match odds data.
        """
        return self._get(
            "odds/pre-match/latest",
            params={"include": includes, "select": selects, "filter": filters},
            async_mode=async_mode,
        )

    def get_all_inplay_odds(
        self,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
        async_mode: bool = False,
    ) -> Union[StdResponse, AsyncResponse]:
        """
        Retrieve all available in-play odds.

        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :param async_mode: Whether to use async mode.
        :return: Iterator over in-play odds data.
        """
        return self._get(
            "odds/inplay",
            params={"include": includes, "select": selects, "filter": filters},
            async_mode=async_mode,
        )

    def get_fixture_inplay_odds(
        self,
        fixture_id: int,
        bookmaker_id: Optional[int] = None,
        market_id: Optional[int] = None,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
        async_mode: bool = False,
    ) -> Union[StdResponse, AsyncResponse]:
        """
        Retrieve in-play odds for a specific fixture. Optionally filter by bookmaker or market.

        :param fixture_id: ID of the fixture.
        :param bookmaker_id: (Optional) ID of the bookmaker.
        :param market_id: (Optional) ID of the market.
        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :param async_mode: Whether to use async mode.
        :return: Iterator over in-play odds data.
        """
        if bookmaker_id:
            return self._get(
                f"odds/inplay/fixtures/{fixture_id}/bookmakers/{bookmaker_id}",
                params={"include": includes, "select": selects, "filter": filters},
                async_mode=async_mode,
            )
        if market_id:
            return self._get(
                f"odds/inplay/fixtures/{fixture_id}/markets/{market_id}",
                params={"include": includes, "select": selects, "filter": filters},
                async_mode=async_mode,
            )
        return self._get(
            f"odds/inplay/fixtures/{fixture_id}",
            params={"include": includes, "select": selects, "filter": filters},
            async_mode=async_mode,
        )

    def get_latest_inplay_odds(
        self,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
        async_mode: bool = False,
    ) -> Union[StdResponse, AsyncResponse]:
        """
        Retrieve in-play odds for fixtures updated within the last 10 seconds.

        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :param async_mode: Whether to use async mode.
        :return: Iterator over updated in-play odds data.
        """
        return self._get(
            "odds/inplay/latest",
            params={"include": includes, "select": selects, "filter": filters},
            async_mode=async_mode,
        )

    def get_premium_fixture_prematch_odds(
        self,
        fixture_id: int,
        bookmaker_id: Optional[int] = None,
        market_id: Optional[int] = None,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
        async_mode: bool = False,
    ) -> Union[StdResponse, AsyncResponse]:
        """
        Retrieve pre-match odds for a specific fixture from the Premium feed.
        Optionally filter by bookmaker or market.

        For more information about the Premium feed, visit:
        https://docs.sportmonks.com/football/endpoints-and-entities/endpoints/premium-odds-feed

        :param fixture_id: ID of the fixture.
        :param bookmaker_id: (Optional) ID of the bookmaker.
        :param market_id: (Optional) ID of the market.
        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :param async_mode: Whether to use async mode.
        :return: Iterator over Premium pre-match odds data.
        """
        if bookmaker_id:
            return self._get(
                f"odds/premium/pre-match/fixtures/{fixture_id}/bookmakers/{bookmaker_id}",
                params={"include": includes, "select": selects, "filter": filters},
                async_mode=async_mode,
            )
        if market_id:
            return self._get(
                f"odds/premium/pre-match/fixtures/{fixture_id}/markets/{market_id}",
                params={"include": includes, "select": selects, "filter": filters},
                async_mode=async_mode,
            )
        return self._get(
            f"odds/premium/pre-match/fixtures/{fixture_id}",
            params={"include": includes, "select": selects, "filter": filters},
            async_mode=async_mode,
        )
