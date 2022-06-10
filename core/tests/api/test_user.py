import pytest
from rest_framework.test import APIClient

client = APIClient()


@pytest.mark.django_db
def test_createuser():
    payload = dict(
        username='Harry',
        email='harrypotter@mail.com',
        password='alohamora'
    )

    response = client.post("/api/createuser/", payload)
    my_data = response.data
    assert my_data["username"] == payload["username"]

