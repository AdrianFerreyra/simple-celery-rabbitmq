from fastapi import FastAPI
from app.celery import app as celery_app
from celery.result import AsyncResult
from app.tasks import add

app = FastAPI()


@app.get("/tasks")
def status(task_id):
    result = AsyncResult(task_id, app=celery_app)
    if result.ready():
        if result.successful():
            return {
                "status": "SUCCESS",
                "result": result.get(),
            }
        else:
            return {
                "status": "FAILURE",
                "error": str(result.result),
            }
    return {"status": "PENDING", "task_id": task_id}


@app.post("/tasks")
def create():
    result = add.delay(2, 2)
    return {"message": f"task '{result.id}' created"}
