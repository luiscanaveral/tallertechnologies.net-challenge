from typing import Annotated
from fastapi import Depends
from my_app.services.projects_service import ProjectsService
from my_app.services.tasks_service import TaskService


ProjectsServiceDI = Annotated[ProjectsService, Depends(ProjectsService)]
TaskServiceDI = Annotated[TaskService, Depends(TaskService)]
