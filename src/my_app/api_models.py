from datetime import datetime, date
from typing import Optional, List
from pydantic import BaseModel, Field


# ---------- Project Schemas ----------

class ProjectBase(BaseModel):
    name: str = Field(..., example="Website Redesign")
    description: Optional[str] = Field(None, example="Improve UX/UI and add landing pages")


class ProjectCreate(ProjectBase):
    pass


class ProjectRead(ProjectBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


# ---------- Task Schemas ----------

class TaskBase(BaseModel):
    title: str = Field(..., example="Create wireframes")
    priority: int = Field(0, example=3)
    completed: bool = Field(False)
    due_date: Optional[date] = Field(None, example="2025-11-15")


class TaskCreate(TaskBase):
    project_id: int


class TaskRead(TaskBase):
    id: int
    project_id: int

    class Config:
        orm_mode = True


# ---------- Nested Relationships ----------

class ProjectWithTasks(ProjectRead):
    tasks: List[TaskRead] = []