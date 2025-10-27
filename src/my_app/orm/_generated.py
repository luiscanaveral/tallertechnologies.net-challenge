from typing import Optional
import datetime

from sqlalchemy import (
    BigInteger,
    Boolean,
    Date,
    DateTime,
    ForeignKeyConstraint,
    Index,
    Integer,
    PrimaryKeyConstraint,
    String,
    Text,
    text,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Project(Base):
    __tablename__ = "project"
    __table_args__ = (PrimaryKeyConstraint("id", name="project_pkey"),)

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text)
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime(True), server_default=text("now()")
    )

    task: Mapped[list["Task"]] = relationship("Task", back_populates="project")


class Task(Base):
    __tablename__ = "task"
    __table_args__ = (
        ForeignKeyConstraint(
            ["project_id"],
            ["project.id"],
            ondelete="CASCADE",
            name="task_project_id_fkey",
        ),
        PrimaryKeyConstraint("id", name="task_pkey"),
        Index("idx_task_completed", "completed"),
        Index("idx_task_priority", "priority"),
        Index("idx_task_project_id", "project_id"),
    )

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    project_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    priority: Mapped[Optional[int]] = mapped_column(Integer, server_default=text("0"))
    completed: Mapped[Optional[bool]] = mapped_column(
        Boolean, server_default=text("false")
    )
    due_date: Mapped[Optional[datetime.date]] = mapped_column(Date)

    project: Mapped["Project"] = relationship("Project", back_populates="task")
