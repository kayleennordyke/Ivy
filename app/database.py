import sqlite3

DB_PATH = "ivy.db"

def get_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row # sets a row factory so rows act like dicts
    return conn

def init_db() -> None:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS readings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sensor_id TEXT NOT NULL,
                metric TEXT NOT NULL,
                value REAL NOT NULL,
                unit TEXT NOT NULL,
                recorded_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        conn.commit()

def insert_reading(reading) -> sqlite3.Row:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO readings (sensor_id, metric, value, unit)
            VALUES (?, ?, ?, ?)
            RETURNING *
            """, 
            (reading.sensor_id, reading.metric, reading.value, reading.unit)
        )
        created_reading = cursor.fetchone()
        conn.commit()
        return created_reading

def fetch_readings() -> list[sqlite3.Row]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT * FROM readings
            ORDER BY recorded_at DESC
            """
        )
        return cursor.fetchall()

        