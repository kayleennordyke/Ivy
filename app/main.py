from fastapi import FastAPI
from app.schemas import Reading, ReadingOut
from app import database
from contextlib import asynccontextmanager


@asynccontextmanager 
async def lifespan(app: FastAPI):
    """Initialize the database while the app is starting up."""
    database.init_db()
    yield

app = FastAPI(lifespan=lifespan) 

# response for this endpoint should match the ReadingOut schema
# 201 in HTTP means "created"
@app.post("/readings", response_model=ReadingOut, status_code=201)
def create_reading(reading: Reading) -> ReadingOut:
    row = database.insert_reading(reading)
    return ReadingOut(**dict(row)) # convert to dict, then to ReadingOut(type)

@app.get("/readings", response_model=list[ReadingOut], status_code=200)
def list_readings() -> list[ReadingOut]:
    rows = database.fetch_readings()
    return [ReadingOut(**dict(row)) for row in rows]