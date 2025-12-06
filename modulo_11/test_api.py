# test_api.py

import pytest # type: ignore
from api import app


@pytest.fixture
def client():
    app.testing = True
    return app.test_client()


def test_soma(client):
    response = client.get("/soma?a=3&b=7")
    data = response.get_json()
    assert data["resultado"] == 10


def test_divide(client):
    response = client.get("/divide?a=20&b=4")
    data = response.get_json()
    assert data["resultado"] == 5


def test_divide_por_zero(client):
    response = client.get("/divide?a=10&b=0")
    assert response.status_code == 400
    data = response.get_json()
    assert data["erro"] == "Divisão por zero"
