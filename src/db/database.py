from enum import Enum

import datetime
from sqlalchemy import Column, String, Date, Enum as EnumSQL, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column,
    Integer,
)

from src.db.utils import CustomBaseModel

Base = declarative_base(cls=CustomBaseModel)


class TaskStatus(Enum):
    Incomplete = "Incomplete"
    In_Progress = "In Progress"
    Completed = "Completed"


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True,autoincrement=True)
    title = Column(String,nullable=False)
    desc = Column(String,nullable=False)
    due_date = Column(DateTime, default=datetime.datetime.utcnow)
    status = Column(EnumSQL(TaskStatus))
