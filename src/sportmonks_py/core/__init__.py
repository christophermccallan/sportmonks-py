from .custom_exceptions import ParameterLengthException

"""
Core endpoints common to all sports within SportMonks included in all subscriptions
"""

__all__ = ["ParameterLengthException"]


class Core:
    def __init__(self, api_token: str, base_url: str):
        """
        Initialize core clients functions.

        :param api_token: API token for authenticating requests.
        :param base_url: Base URL for football-related endpoints.
        """
        if not api_token:
            raise ValueError("API token is required.")

        # core_base_url = f"{base_url}my/"
