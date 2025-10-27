from typing import Union

from fastapi import FastAPI

from .api_models import Task
from .services import ProjectsServiceDI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/project/{project_id}")
def _(project_id: int, service: ProjectsServiceDI):
    return service.get_project_by_id(project_id)

@app.post("/project/{project_id}/tasks")
def read_item(project_id: int, task: Task):
    # service
    # verify project exists first
    # If not, return 404
    return {"project_id": project_id, "task": task}
