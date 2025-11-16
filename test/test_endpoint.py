from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/version")
    assert response.status_code == 200
    assert response.json() == {"Application Version": "0.0.2"}


def test_avg_temperature():
    response = client.get("/temperature")
    assert response.status_code == 200
