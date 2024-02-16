from django.contrib import admin
from django.urls import path, include
from oc_lettings_site.views import index, view_that_raises_500


def trigger_error(request):
    1 / 0  # division_by_zero = 1/0


urlpatterns = [
    path("", index, name="index"),
    path("", include("lettings.urls")),
    path("", include("profiles.urls")),
    path("admin/", admin.site.urls),
    path("test-500/", view_that_raises_500, name="view_that_raises_500"),
    path("sentry-debug/", trigger_error),
]

handler404 = "oc_lettings_site.views.handler404"
handler500 = "oc_lettings_site.views.handler500"
