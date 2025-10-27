from typing import Union

from fastapi import FastAPI

from .api_models import Task

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/project/{project_id}/tasks")
def read_item(project_id: int, task: Task):
    # service
    # verify project exists first
    # If not, return 404
    return {"project_id": project_id, "task": task}
