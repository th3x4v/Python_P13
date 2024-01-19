from django.urls import path
from conftest import temporary_error_view  # Make sure to use the correct import path

urlpatterns = [
    path("test-500/", temporary_error_view, name="test-500"),
]
