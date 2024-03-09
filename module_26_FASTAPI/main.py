from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def async_func():
    return {"message": "Hello world"}


