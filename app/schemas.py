from pydantic import BaseModel

class Reading(BaseModel):
    sensor_id: str
    metric: str
    value: float
    unit: str