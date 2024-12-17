from typing import Union, Optional
from sportmonks_py.utils.common_types import StdResponse, AsyncResponse, Ordering
from sportmonks_py.client.base_client import BaseClient


class MyClient(BaseClient):
    """
    A client for accessing common endpoints data from the SportMonks API.
    """

    def __init__(self, base_url: str, api_token: str) -> None:
        """
        Initialize the My Client with a base_url and API token.

        :param api_token: API token for authenticating requests.
        :param base_url: Base URL for the API.
        """
        super().__init__(base_url=base_url, api_token=api_token)

    def enrichments(
        self, async_mode: bool = False, order: Optional[Ordering] = None
    ) -> Union[StdResponse, AsyncResponse]:
        """
        This endpoint returns all available enrichments for the entities.
        :param async_mode: Whether to use async mode.
        :param order: Order to sort the results in (asc or desc).

        :return: StdResponse | AsyncResponse
        """
        return self._get("my/enrichments", async_mode=async_mode)

    def leagues(
        self, async_mode: bool = False, order: Optional[Ordering] = None
    ) -> Union[StdResponse, AsyncResponse]:
        """
        This endpoint returns all available leagues for the entities.
        :param async_mode: Whether to use async mode.
        :param order: Order to sort the results in (asc or desc).

        :return: StdResponse | AsyncResponse
        """
        return self._get("my/leagues", async_mode=async_mode, order=order)

    def resources(
        self, async_mode: bool = False, order: Optional[Ordering] = None
    ) -> Union[StdResponse, AsyncResponse]:
        """
        This endpoint returns all available resources for the entities.
        :param async_mode: Whether to use async mode.
        :param order: Order to sort the results in (asc or desc).

        :return: StdResponse | AsyncResponse
        """
        return self._get("my/resources", async_mode=async_mode, order=order)
