from typing import Union

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from my_app.services.exceptions import ProjectNotFoundException

from .api_models import *
from .services import ProjectsServiceDI, TaskServiceDI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/projects")
def _(service: ProjectsServiceDI):
    return service.get_all_projects()


@app.exception_handler(ProjectNotFoundException)
def project_not_found_exception_handler(request, exc: ProjectNotFoundException):
    return JSONResponse(
        status_code=404,
        content={"detail": str(exc)},
    )

@app.get("/project/{project_id}")
def _(project_id: int, service: ProjectsServiceDI):
    return service.get_project_by_id(project_id)

@app.post("/project/{project_id}/tasks")
def create_task(project_id: int, 
                task: TaskCreate, 
                project_service: ProjectsServiceDI, 
                task_service: TaskServiceDI):
    # Verify project exists first
    project = project_service.get_project_by_id(project_id)
    if not project:
        return {"error": "Project not found"}, 404

    # If project exists, create the task
    return task_service.create_task(project_id, task)
