from datetime import datetime
from typing import Optional

from .errors import InvalidIncludes


def validate_date_format(date_str: str) -> bool:
    """
    Validates if the provided date is in the format 'YYYY-mm-dd' that SportMonks requires.

    Args:
        date_str (str): The date string to validate.

    Returns:
        bool: True if the date is valid and in the correct format, False otherwise.
    """
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def validate_date_order(date1: str, date2: str) -> bool:
    """
    Validates if the first date is not after the second date. A range of more than 100
    days is also invalid.

    Args:
        date1 (str): The first date in 'YYYY-mm-dd' format.
        date2 (str): The second date in 'YYYY-mm-dd' format.

    Returns:
        bool: True if date1 <= date2, False if not, False if the range exeeds 100 days.
    """
    d1 = datetime.strptime(date1, "%Y-%m-%d")
    d2 = datetime.strptime(date2, "%Y-%m-%d")
    if d1 > d2:
        return False

    if (d2 - d1).days > 100:
        return False

    return True


def validate_search_params(params: Optional[set[str]], allowed_params: set[str]) -> None:
    """
    Validate that all elements in `includes` are within the `allowed_includes` set.

    :param params: A set of requested includes to validate.
    :param allowed_params: The set of allowed includes.
    :raises InvalidIncludes: If any includes are invalid.
    """
    if params and not params.issubset(allowed_params):
        invalid_includes = params - allowed_params
        raise InvalidIncludes(
            f"Invalid includes: {invalid_includes}. Allowed includes: {allowed_params}"
        )


def validate_positive_id(value: int, name: str) -> None:
    """
    Validates that a given value is a positive integer.

    :param value: The value to validate.
    :param name: The parameter name for error messages.
    """
    if not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer.")
