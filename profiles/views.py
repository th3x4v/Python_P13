from django.shortcuts import render

from .models import Profile

def index(request):
    """
    This function returns a list of all profiles in the database.
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)

def profile(request, username):
    """
    This function returns a single profile based on the username passed in the URL.

    Args:
        request (HttpRequest): The incoming request.
        username (str): The username of the profile to retrieve.

    Returns:
        HttpResponse: The rendered template with the profile data.

    """
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
