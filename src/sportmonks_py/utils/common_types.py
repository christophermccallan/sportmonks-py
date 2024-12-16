"""Types used for clearer documentation and type hinting"""

from typing import Union, Dict, Any, List, Optional, Iterator, Iterable, AsyncIterator

Response = Iterator[Dict[str, Any]]

Includes = Optional[List[str]]
Selects = Optional[dict[Union[str, Any]]]
Filters = Optional[dict[Union[str, Any]]]
StdResponse = Iterable[Iterator[dict[str, Any]]]
AsyncResponse = AsyncIterator[Iterator[dict[str, Any]]]
