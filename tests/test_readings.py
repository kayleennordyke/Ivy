from fastapi.testclient import TestClient
from app.main import app, readings
import pytest

client = TestClient(app)

@pytest.fixture(autouse=True)
def clear_readings():
    """Clear the readings list before and after each test."""
    readings.clear()
    yield
    readings.clear()

def test_create_reading() -> None:
    """Test the POST /readings endpoint."""
    payload = {
        "sensor_id": "Blueberry",
        "metric": "temperature",
        "value": 22.5,
        "unit": "C",
    }
    response = client.post("/readings", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert data["sensor_id"] == "Blueberry"
    assert data["metric"] == "temperature"
    assert data["value"] == 22.5
    assert data["unit"] == "C"

def test_list_readings() -> None:
    """Test the GET /readings endpoint."""
    payload = {
        "sensor_id": "Blueberry",
        "metric": "temp",
        "value": 23.0,
        "unit": "C",
    }
    client.post("/readings", json=payload)

    response = client.get("/readings")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["sensor_id"] == "Blueberry"
    assert data[0]["metric"] == "temp"
    assert data[0]["value"] == 23.0
    assert data[0]["unit"] == "C"

def test_create_reading_rejects_bad_value() -> None:
    """Invalid value should fail validation."""
    payload = {
        "sensor_id": "Blueberry",
        "metric": 3,
        "value": "nope",
        "unit": "C",
    }
    response = client.post("/readings", json=payload)
    assert response.status_code == 422

