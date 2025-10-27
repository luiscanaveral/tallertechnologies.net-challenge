from my_app.data_layer.connection import get_session
from my_app.orm import Project
from my_app.services.exceptions import ProjectNotFoundException


class ProjectsService:
    def get_all_projects(self):
        with get_session() as session:
            projects = session.query(Project).all()
            return projects

    def get_project_by_id(self, project_id: int) -> Project:
        with get_session() as session:
            project = session.query(Project).filter(Project.id == project_id).first()
            if not project:
                raise ProjectNotFoundException(
                    f"Project with id {project_id} not found"
                )
            return project
