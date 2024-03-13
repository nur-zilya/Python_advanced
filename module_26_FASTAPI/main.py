from fastapi import FastAPI
from sqlalchemy.future import select

import models
import schemas
from datebase import engine, session

app = FastAPI()


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)


@app.on_event("shutdown")
async def shutdown():
    await session.close()
    await engine.dispose()


@app.get("/")
async def async_func():
    return {"message": "Hello world"}


