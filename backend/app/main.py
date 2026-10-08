import os

from fastapi import FastAPI
from sqlalchemy import create_engine, text

engine = create_engine(os.environ["DATABASE_URL"])

app = FastAPI(title="Drill Records API")


@app.get("/health")
def health():
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
    return {"status": "ok", "database": "ok"}
