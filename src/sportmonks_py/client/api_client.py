import logging

from sportmonks_py.utils.config import config
from sportmonks_py.clients.base_client import BaseClient
from sportmonks_py.clients.api_client import APIClient


class SportMonksClient(BaseClient):
    def __init__(self, sport: str, api_token: str):
        """
        Initialize the SportMonks API client.

        :param api_token: API token for authenticating requests.
        """

        base_url = f"{config.BASE_URL}{sport}/"
        super().__init__(base_url=base_url, api_token=api_token)
        self.client = APIClient(sport=sport, api_token=api_token)

        logging.getLogger("sportmonks-py").info(
            f"Initialized SportMonksClient with sport: {sport}"
        ).addHandler(logging.NullHandler())
