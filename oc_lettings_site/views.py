from django.shortcuts import render
from django.http import HttpResponseServerError
from sentry_sdk import capture_message
import logging

logger = logging.getLogger(__name__)


def view_that_raises_500(request):
    raise HttpResponseServerError()


def index(request):
    """
    This function returns the index.html template when a GET request is made to the root URL.
    """
    logger.info("Home page connection")
    return render(request, "index.html")


def handler500(request):
    """
    This function returns the 500.html template when a GET request is made to a URL that
    does not exist.
    """
    capture_message("Internal Server Error! Error 500 ", level="error")
    return render(request, "500.html", status=500)


def handler404(request, exception):
    """
    This function returns the 404.html template when a GET request is made to a URL that
    does not exist.
    """
    capture_message("Page not found! Error 404", level="error")
    return render(request, "404.html", status=404)
