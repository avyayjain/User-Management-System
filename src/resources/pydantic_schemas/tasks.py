from datetime import datetime, date
from enum import Enum
from pydantic import BaseModel, constr, validator


class TaskStatus(str, Enum):
    INCOMPLETE = "Incomplete"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"


class Task(BaseModel):
    title: str
    desc: str
    due_date: date
    status: TaskStatus
