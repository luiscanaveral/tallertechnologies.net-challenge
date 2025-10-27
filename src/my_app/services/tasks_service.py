from my_app.data_layer.connection import get_session
from my_app.orm import Project, Task

class TaskService:
    def get_all_tasks_by_project(self, project_id: int):
        with get_session() as session:
            tasks = session.query(Task).filter(Task.project_id == project_id).all()
            return tasks
    def create_task(self, project_id: int, task_data) -> Task:
        with get_session() as session:
            new_task = Task(
                title=task_data.title,
                priority=task_data.priority,
                completed=task_data.completed,
                due_date=task_data.due_date,
                project_id=project_id
            )
            session.add(new_task)
            session.commit()
            session.refresh(new_task)
            return new_task