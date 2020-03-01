import pytest
import flask
import app
import json
from unittest.mock import patch


@pytest.fixture
def client():
    yield app.app.test_client()


def test_ping(client):
    response = client.get("/api/ping")
    assert response.status_code == 200
    assert response.data == b"Response"


def test_display_game_state(client):
    response = client.get("/api/game_state/TEST")
    assert response.status_code == 200


def test_click(client,):
    response = client.post(
        "/api/click", data=json.dumps({"x": 0, "y": 1, "game_id": "TEST"})
    )
    assert response.status_code == 200


def test_create(client):
    response = client.post(
        "/api/create", data=json.dumps({"x_max": 10, "y_max": 10, "num_mines": 20})
    )
    assert response.status_code == 200
