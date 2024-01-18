from django.shortcuts import render


def index(request):
    """
    This function returns the index.html template when a GET request is made to the root URL.
    """
    return render(request, "index.html")


def handler500(request):
    """
    This function returns the 500.html template when a GET request is made to a URL that does not exist.
    """
    return render(request, "500.html", status=500)


def handler404(request, exception):
    """
    This function returns the 404.html template when a GET request is made to a URL that does not exist.
    """
    return render(request, "404.html", status=404)
