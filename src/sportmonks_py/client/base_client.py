import json
import http.client
import urllib.parse
import aiohttp
from typing import Dict, Iterable, Any, Optional, AsyncIterator, Union, Iterator

from sportmonks_py.utils.errors import (
    status_code_to_exception,
    ApiTokenMissingError,
    MalformedResponseError,
)
from sportmonks_py.utils.common_types import Includes, Response, Selects, Filters


class BaseClient:
    def __init__(self, base_url: str, api_token: str):
        if not api_token:
            raise ApiTokenMissingError("API token is required.")

        self.base_url = base_url.rstrip("/")
        self.api_token = api_token

    def _get(
            self,
            endpoint: str,
            params: Optional[Dict[str, Any]] = None,
            includes: Optional[Includes] = None,
            selects: Optional[Selects] = None,
            filters: Optional[Filters] = None,
            async_mode: bool = False,
            locale: Optional[str] = None,
    ) -> Union[Iterable[Response], AsyncIterator[Response]]:
        """
        If async_mode=False, returns a synchronous iterator over API results.
        If async_mode=True, returns an asynchronous iterator over API results.
        Locale defaults to English if not selected or an invalid locale is provided.
        """
        url = self._build_url(endpoint, params, includes, selects, filters, locale)

        if async_mode:
            return self._get_async_generator(url)
        else:
            return self._get_sync_generator(url)

    def _get_sync_generator(self, initial_url: str) -> Iterator[Response]:
        """
        Synchronous generator that yields results from the API.
        """
        url = initial_url
        while url:
            try:
                response_data = self._make_request(url)
                message = response_data.get("message")
                if message:
                    yield {"message": message}
                else:
                    yield response_data["data"]
                pagination = response_data.get("pagination", {})
                url = (
                    pagination.get("next_page") if pagination.get("has_more") else None
                )
            except Exception as e:
                raise ValueError(f"Error processing URL {url}: {e}")

    async def _get_async_generator(self, initial_url: str) -> AsyncIterator[Response]:
        """
        Asynchronous generator that yields results from the API.
        """
        url = initial_url
        while url:
            try:
                response_data = await self._make_request_async(url)
                message = response_data.get("message")
                if message:
                    yield {"message": message}
                else:
                    yield response_data["data"]
                pagination = response_data.get("pagination", {})
                url = (
                    pagination.get("next_page") if pagination.get("has_more") else None
                )
            except Exception as e:
                raise MalformedResponseError(
                    f"Error in endpoint response, missing : {e} from {url}. Re-check the requested parameters"
                )

    def _make_request(self, url: str) -> Dict[str, Any]:
        parsed_url = urllib.parse.urlparse(url)
        conn = http.client.HTTPSConnection(parsed_url.netloc)
        path = parsed_url.path + (f"?{parsed_url.query}" if parsed_url.query else "")
        conn.request("GET", path, headers=self._build_headers())
        response = conn.getresponse()
        response_content = response.read()

        if response.status != 200:
            raise status_code_to_exception(response.status, response_content)

        return json.loads(response_content.decode("utf-8"))

    async def _make_request_async(self, url: str) -> Dict[str, Any]:
        headers = self._build_headers()
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                response_content = await response.read()
                if response.status != 200:
                    raise status_code_to_exception(response.status, response_content)
                return json.loads(response_content.decode("utf-8"))

    def _build_url(
            self,
            endpoint: str,
            params: Optional[Dict[str, Any]],
            includes: Optional[Includes],
            selects: Optional[Selects],
            filters: Optional[Filters],
            locale: Optional[str] = None,
    ) -> str:
        params = params or {}

        if includes:
            params["include"] = ";".join(includes)
        if selects:
            params["select"] = json.dumps(selects, separators=(",", ":"))
        if filters:
            params.update({f"filter[{k}]": v for k, v in filters.items()})
        if locale:
            params.update({"locale": locale})

        params = {k: v for k, v in params.items() if v}

        search_string = urllib.parse.urlencode(params, doseq=True)
        encoded_endpoint = urllib.parse.quote(endpoint, safe="/")

        url = f"{self.base_url}/{encoded_endpoint}"
        if search_string:
            url = f"{url}?{search_string}"

        return url

    def _build_headers(self) -> Dict[str, str]:
        return {
            "Authorization": self.api_token,
            "Content-Type": "application/json",
            "User-Agent": "sportmonks-py (https://github.com/cmccallan/sportmonks-py)",
        }
