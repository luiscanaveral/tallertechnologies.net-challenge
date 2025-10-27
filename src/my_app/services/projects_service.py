

from my_app.data_layer.connection import get_session
from my_app.orm import Project

class ProjectsService:
    def get_project_by_id(self, project_id):
        # Implementation to retrieve project details
        with get_session() as session:
            project = session.query(Project).filter(Project.id == project_id).first()
            return project