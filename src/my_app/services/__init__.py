



from typing import Annotated
from fastapi import Depends
from my_app.services.projects_service import ProjectsService


ProjectsServiceDI = Annotated[ProjectsService, Depends(ProjectsService)]