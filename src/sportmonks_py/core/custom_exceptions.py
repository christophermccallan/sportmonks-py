class ApiTokenMissingError(Exception):
    """Raised when API key is not provided."""

    pass


class BaseUrlMissingError(Exception):
    """Raised when base url is not provided."""

    pass


class SportMonksAPIError(Exception):
    """Raised when SportMonks returns an API error."""

    pass


class IncompatibleDictionarySchema(Exception):
    """Raised when a dictionary cannot be unnested."""

    pass


class InvalidTimezoneError(Exception):
    """Raised when an unrecognized or invalid timezone is provided"""

    pass


class ParameterException(Exception):
    """Raised when an incorrect parameter type is provided"""

    pass


class ParameterLengthException(Exception):
    """Raised when the number of parameters requested in a single API call exceeds the allow amount"""

    pass


class InvalidDateFormat(Exception):
    """Raised when the date provided is in an incorrect or unsupported format"""

    pass


class InvalidIncludes(Exception):
    """Raised when an invalid object is passed as an includes argument"""

    pass
