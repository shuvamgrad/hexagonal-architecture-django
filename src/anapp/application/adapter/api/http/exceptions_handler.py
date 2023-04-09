import logging
from http import HTTPStatus

from rest_framework.views import exception_handler

from anapp.application.adapter.api.http.problem_response import problem_response
from anapp.application.adapter.spi.persistence.exceptions.user_not_found import (
    UserNotFound
)

logger = logging.getLogger(__name__)


def exceptions_handler(exc, context):
    logger.error("Unexpected error occurred: %s", exc)

    # Call REST framework's default exception handler first,
    # to get the standard error response.
    # NOTE: this is not formatted as Problem response,
    #       currently left as-is for cleaner demo code.
    response = exception_handler(exc, context)
    if response is not None:
        return response

    if isinstance(exc, UserNotFound):
        return problem_response("Error", str(exc), HTTPStatus.NOT_FOUND)

    logger.exception("Unhandled error: %s", exc, exc_info=True)
    return problem_response(
        "Unknown error",
        "Our deepest apologies, an unexpected error occurred "
        "and we are already working on it.",
        HTTPStatus.INTERNAL_SERVER_ERROR
    )
