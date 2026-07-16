import random
import httpx

URL = "http://127.0.0.1:8000/readings"

def main() -> None:
    for i in range(20):
        payload = {
            "sensor_id": "Blueberry",
            "metric": "temperature",
            "value": round(random.uniform(18.0, 26.0), 1),
            "unit": "C",
        }

        response = httpx.post(URL, json=payload)
        response.raise_for_status()
        print(response.status_code, response.json())

if __name__ == "__main__":
    main()