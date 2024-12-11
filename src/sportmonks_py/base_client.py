import json
import http.client
import urllib.parse
import logging
from typing import Dict, Iterable, Union, Any, Optional
from sportmonks_py.core.custom_exceptions import ApiTokenMissingError
from sportmonks_py.core.common_types import Includes, Response, Selects, Filters

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s : %(levelname)s : %(name)s : %(message)s",
    handlers=[logging.StreamHandler()],
)
logger = logging.getLogger(__name__)


class BaseClient:
    def __init__(self, api_token: str, base_url: str):
        """
        Initialize the base client with an API token and base URL.

        :param api_token: API token for authenticating requests.
        :param base_url: Base URL for the API.
        """
        if not api_token:
            raise ApiTokenMissingError("API token is required.")

        self.api_token = api_token
        self.base_url = base_url.rstrip("/")

    def _get(
        self,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
    ) -> Response:
        """
        Execute a GET request to a paginated API endpoint and yield results.

        :param endpoint: API endpoint to request.
        :param params: Query parameters to include in the request.
        :param includes: List of includes to add to the request.
        :param selects: Fields to select or exclude in the response.
        :param filters: Filters to apply to the request.
        :return: Iterator yielding API results.
        """
        params = params or {}

        if includes:
            params["include"] = self._prepare_includes(includes)
        if selects:
            params["select"] = self._prepare_selects(selects)
        if filters:
            params.update(self._prepare_filters(filters))

        params = {key: value for key, value in params.items() if value}

        query_string = self._build_query_string(params) if params else ""
        url = f"{self.base_url}/{endpoint}"
        if query_string:
            url = f"{url}?{query_string}"

        logger.info(f"Request URL: {url}")

        while url:
            try:
                response_data = self._make_request(url)
                yield response_data["data"]

                pagination = response_data.get("pagination", {})
                url = (
                    pagination.get("next_page") if pagination.get("has_more") else None
                )
            except http.client.HTTPException as http_err:
                logger.error(f"HTTP error occurred: {http_err}")
                raise
            except json.JSONDecodeError as json_err:
                logger.error(f"JSON decode error: {json_err}")
                raise
            except Exception as e:
                logger.exception(f"Error processing URL {url}: {e}")
                raise

    def _make_request(self, url: str) -> Dict[str, Any]:
        """
        Make a GET request to the given URL.

        :param url: Fully constructed URL.
        :return: JSON-decoded response.
        """
        parsed_url = urllib.parse.urlparse(url)
        conn = http.client.HTTPSConnection(parsed_url.netloc)
        path = parsed_url.path + (f"?{parsed_url.query}" if parsed_url.query else "")

        conn.request("GET", path, headers=self._build_headers())
        response = conn.getresponse()
        response_content = response.read()

        if response.status != 200:
            logger.error(
                f"API error: {response.status} - {response.reason}. URL: {url}"
            )
            raise Exception(f"API request failed with status {response.status}")

        return json.loads(response_content.decode("utf-8"))

    def _build_headers(self) -> Dict[str, str]:
        """
        Build default headers for API requests.

        :return: Dictionary of headers.
        """
        return {
            "Authorization": f"{self.api_token}",
            "Content-Type": "application/json",
            "User-Agent": "sportmonks-py (https://github.com/cmccallan/sportmonks-py)",
        }

    @staticmethod
    def _prepare_includes(includes: Iterable[str]) -> str:
        """
        Prepare the 'includes' parameter for the API request.

        :param includes: Iterable of includes.
        :return: Semicolon-separated string of includes.
        """
        return ";".join(map(str, includes))

    @staticmethod
    def _prepare_selects(selects: dict[Union[str, Any]]) -> str:
        """
        Prepare the 'selects' parameter for the API request.
        :param selects: Dictionary of fields to include/exclude.
        :return: JSON-encoded string of selects.
        """
        return json.dumps(selects, separators=(",", ":"))

    @staticmethod
    def _prepare_filters(filters: Dict[str, Any]) -> Dict[str, Any]:
        """
        Prepare the filters for the API request.
        :param filters: Dictionary of filters.
        :return: Dictionary of prepared filters.
        """
        return {f"filter[{key}]": value for key, value in filters.items()}

    @staticmethod
    def _build_query_string(params: Dict[str, Any]) -> str:
        """
        Build the query string for the URL.

        :param params: Dictionary of query parameters.
        :return: URL-encoded query string.
        """
        return urllib.parse.urlencode(params, doseq=True)
