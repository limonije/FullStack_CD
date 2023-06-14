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


def test_succes(client):
    response = client.get("/succes")

    assert response.status_code == 200
    assert response.data == b"<h1>Deployment is wederom een succes</h1>"
