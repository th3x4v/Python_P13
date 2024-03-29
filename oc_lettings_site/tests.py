import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed
from django.test import Client


@pytest.mark.django_db
def test_index_view(client):
    response = client.get(reverse("index"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_index_view_template(client):
    response = client.get(reverse("index"))
    assertTemplateUsed(response, "index.html")


@pytest.mark.django_db
def test_handler404():
    client = Client()
    response = client.get("/nonexisting/page")
    assert response.status_code == 404
    # Test that the correct template is used
    templates = [t.name for t in response.templates]
    assert "404.html" in templates


@pytest.mark.django_db
def test_handler500(client):
    with pytest.raises(Exception):
        # Force a server error by calling a view that will raise an exception
        response = client.get(reverse("view_that_raises_500"))
        assert response.status_code == 500
        # Test that the correct template is used
        templates = [t.name for t in response.templates]
        assert "500.html" in templates
