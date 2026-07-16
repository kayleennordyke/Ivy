from fastapi.testclient import TestClient
from app.main import app, readings

client = TestClient(app)

#response = client.post("/readings", json={...})
#response = client.get("/readings")

def test_create_reading() -> None:
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
    pass