from datetime import datetime


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


def validate_positive_id(value: int, name: str) -> None:
    """
    Validates that a given value is a positive integer.

    :param value: The value to validate.
    :param name: The parameter name for error messages.
    """
    if not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer.")


def validate_locale(locale: str) -> None:
    """
    Validates that the provided locale is supported by SportMonks.

    Args:
        locale (str): The locale to validate.
    """
    if locale not in supported_locales:
        raise ValueError(
            f"Unsupported locale: {locale}. Supported locales: {supported_locales}"
        )
