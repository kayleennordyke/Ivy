from fastapi import FastAPI
from app.schemas import Reading

app = FastAPI()

readings: list[Reading] = []

@app.post("/readings")
def create_reading(reading: Reading) -> Reading:
    readings.append(reading)
    return reading

@app.get("/readings")
def list_readings() -> list[Reading]:
    return readings