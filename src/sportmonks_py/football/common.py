from typing import Any, Iterator

from sportmonks_py.base_client import BaseClient


class CommonClient(BaseClient):
    """
    A client for accessing common endpoints data from the SportMonks API.
    """

    def __init__(self, api_token: str, base_url: str) -> None:
        """
        Initialize the FixturesClient with an API token and base URL.

        :param api_token: API token for authenticating requests.
        :param base_url: Base URL for the API.
        """
        super().__init__(api_token=api_token, base_url=base_url)

    def get_entity_filters(self) -> Iterator[dict[str, Any]]:
        """
        This endpoint returns all available filters for the entities.

        :return: Dictionary of filters.
        """
        return self._get("filters")
