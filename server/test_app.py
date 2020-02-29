import pytest
import flask
import app
import json


@pytest.fixture
def client():
    yield app.app.test_client()


def test_ping(client):
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.data == b"Response"


def test_display_game_state(client):
    response = client.get("/game_state")
    assert response.status_code == 200


def test_click(client):
    response = client.post("/click", data=json.dumps({"x": 0, "y": 1}))
    assert response.status_code == 200
