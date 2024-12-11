from sportmonks_py.football.fixture import FixturesClient
from sportmonks_py.football.odds import OddsClient
from sportmonks_py.football.teams import TeamsClient
from sportmonks_py.football.leagues import LeaguesClient
from sportmonks_py.football.standings import StandingsClient
from sportmonks_py.football.misc import OtherClient


class Football:
    def __init__(self, api_token: str, base_url: str):
        """
        Initialize football-specific clients.

        :param api_token: API token for authenticating requests.
        :param base_url: Base URL for football-related endpoints.
        """
        football_base_url = f"{base_url}football/"

        self.fixtures = FixturesClient(api_token, football_base_url)
        self.odds = OddsClient(api_token, football_base_url)
        self.teams = TeamsClient(api_token, football_base_url)
        self.leagues = LeaguesClient(api_token, football_base_url)
        self.standings = StandingsClient(api_token, football_base_url)
        self.other = OtherClient(api_token, football_base_url)
