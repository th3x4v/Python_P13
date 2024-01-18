from django.shortcuts import render
from .models import Letting


def index(request):
    """
    This function returns a list of all lettings.

    Args:
        request (HttpRequest): The incoming request object.

    Returns:
        HttpResponse: The response with the list of lettings.
    """
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings/index.html", context)


def letting(request, letting_id):
    """
    This function returns a letting based on the id.

    Args:
        request (HttpRequest): The incoming request object.
        letting_id (int): The id of the letting to retrieve.

    Returns:
        HttpResponse: The response with the letting details.
    """
    letting = Letting.objects.get(id=letting_id)
    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "lettings/letting.html", context)
