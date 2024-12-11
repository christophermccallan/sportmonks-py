"""Types used for clearer documentation and type hinting"""

from typing import Union, Dict, Any, List, Optional, Iterator

Response = Iterator[Dict[str, Any]]

Includes = Optional[List[str]]
Selects = Optional[dict[Union[str, Any]]]
Filters = Optional[dict[Union[str, Any]]]
