import asyncio
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from settings import TRAIN_LOCK
from homework.tasks import task


app = FastAPI()


@app.post("/train", status_code=200)
def train():
    task()
    return JSONResponse(content={"message": "OK"})


@app.get("/check_status", status_code=200)
def check_status():
    if TRAIN_LOCK:
        return JSONResponse(content={"message": "Task is running"})
    return JSONResponse(content={"message": "Task is done"})