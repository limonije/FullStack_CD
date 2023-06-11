import pytest

from main import app


@pytest.fixture
def client():
    client = app.test_client()
    return client


def test_index(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.data == b"<h1>Home, sweet home.</h1>"


def test_winc(client):
    response = client.get("/winc")

    assert response.status_code == 200
    assert response.data == b"<h1>Hello, Winc Academy!</h1>"
