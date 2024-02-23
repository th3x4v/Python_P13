API interfaces
==============

The web app is structure in 3 Django application.

**In lettings**:
    - URL patterns for lettings:
    - /lettings/ maps to the index view function with the name lettings_index.
    - /lettings/<int:letting_id>/ maps to the letting view function with the name letting.

**In profiles**:
    - URL patterns for profiles:
    - /profiles/ maps to the index view function with the name profiles_index.
    - /profiles/<str:username>/ maps to the profile view function with the name profile.

**In oc_lettings_site**:
    - Main URL patterns for the site:
    - Root URL 1 maps to the index view function.
    - Includes URLs from lettings.urls and profiles.urls.
    - /admin/ maps to the Django admin site.
    - /test-500/ maps to a view that raises a 500 error.
    - /sentry-debug/ triggers a division by zero error.
    - Custom error handlers for 404 and 500 errors are specified.