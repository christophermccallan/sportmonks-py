from sportmonks_py.base_client import BaseClient
from sportmonks_py.football import Football


class SportMonksClient(BaseClient):
    def __init__(self, api_token: str):
        """
        Initialize the SportMonks API client.

        :param api_token: API token for authenticating requests.
        """
        base_url = "https://api.sportmonks.com/v3/"
        super().__init__(api_token=api_token, base_url=base_url)

        # Initialize sport-specific modules
        self.football = Football(api_token=api_token, base_url=base_url)
