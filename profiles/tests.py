import pytest
from django.test import Client
from django.urls import reverse
from profiles.models import Profile
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_index_view():
    client = Client()
    test_user = User.objects.create_user(username="testuser")
    Profile.objects.create(user=test_user)

    # Act
    response = client.get(
        reverse("profiles_index")
    )  # Assuming 'index' is the name of the url pattern for the index view

    # Assert
    assert response.status_code == 200
    assert "Profiles" in response.content.decode("utf-8")
    assert "testuser" in response.content.decode("utf-8")


@pytest.mark.django_db
def test_profile_view():
    client = Client()
    test_user = User.objects.create_user(username="testuser", password="12345")
    Profile.objects.create(user=test_user, favorite_city="testcity")

    # Act
    response = client.get(
        reverse("profile", kwargs={"username": "testuser"})
    )  # Assuming 'profile' is the name of the url pattern for the profile view

    # Assert
    assert response.status_code == 200
    assert "testcity" in response.content.decode("utf-8")
    assert "testuser" in response.content.decode("utf-8")
