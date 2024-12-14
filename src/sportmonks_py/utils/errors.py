class ApiTokenMissingError(Exception):
    """Raised when API key is not provided."""

    pass


class BaseUrlMissingError(Exception):
    """Raised when base url is not provided."""

    pass


class BadRequestsError(Exception):
    """Raised when a bad request is made"""

    pass


class UnauthorizedError(Exception):
    """Raised when an unauthorized request is made"""

    pass


class ForbiddenError(Exception):
    """Raised when a forbidden request is made"""

    pass


class TooManyRequestsError(Exception):
    """Raised when too many requests are made"""

    pass


class InternalServerError(Exception):
    """Raised when an internal server error occurs"""

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


status_code_to_exception = {
    400: BadRequestsError("Bad request."),
    401: UnauthorizedError("Unauthorized request."),
    403: ForbiddenError("Forbidden request."),
    429: TooManyRequestsError("Too many requests, please try again later."),
    500: InternalServerError("Internal server error."),
}
