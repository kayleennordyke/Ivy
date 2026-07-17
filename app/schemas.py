from pydantic import BaseModel

class Reading(BaseModel): # what clients SEND
    sensor_id: str
    metric: str
    value: float
    unit: str

class ReadingOut(Reading):  # what the API RETURNS
    id: int
    recorded_at: str 