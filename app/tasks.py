from time import sleep
from app.celery import app


@app.task
def add(x, y):
    sleep(5)
    return x + y
