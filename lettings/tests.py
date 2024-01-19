# lettings/tests.py

import pytest
from django.test import Client
from django.urls import reverse
from lettings.models import Letting, Address
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_letting_index_view():
    client = Client()
    # Create test data for letting
    address_data = {
        "number": 1234,
        "street": "Test Street",
        "city": "Test City",
        "state": "TS",
        "zip_code": 12345,
        "country_iso_code": "TST",
    }

    # Act
    address = Address.objects.create(**address_data)
    Letting.objects.create(title="test_letting", address=address)
    # Act
    response = client.get(reverse("lettings_index"))
    # Assert
    assert response.status_code == 200
    assert "Lettings" in response.content.decode("utf-8")
    assert "test_letting" in response.content.decode("utf-8")


@pytest.mark.django_db
def test_letting_detail_view():
    client = Client()
    # Create test data for letting
    address_data = {
        "number": 1234,
        "street": "Test Street",
        "city": "Test City",
        "state": "TS",
        "zip_code": 12345,
        "country_iso_code": "TST",
    }

    # Act
    address = Address.objects.create(**address_data)
    Letting.objects.create(title="test_letting", address=address)
    # Act
    response = client.get(
        reverse("letting", kwargs={"letting_id": 1})
    )  # Assuming 'letting_detail' is the name of the url pattern for the letting detail view
    # Assert
    assert response.status_code == 200
    assert "test_letting" in response.content.decode("utf-8")
    assert "Test City" in response.content.decode("utf-8")
