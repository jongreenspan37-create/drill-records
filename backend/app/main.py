from fastapi import FastAPI
from sqlalchemy import text

from app.database import engine

app = FastAPI(title="Drill Records API")


@app.get("/health")
async def health():
    async with engine.connect() as conn:
        await conn.execute(text("SELECT 1"))
    return {"status": "ok", "database": "ok"}
