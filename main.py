from fastapi import FastAPI
from fastapi.responses import JSONResponse

from homework.tasks import check_status, task


app = FastAPI()


@app.post("/train", status_code=200)
def train():
    task.run()
    return JSONResponse(content={"message": "OK"})


@app.get("/status", status_code=200)
def status():
    return JSONResponse(content={"message": check_status.check_status()})