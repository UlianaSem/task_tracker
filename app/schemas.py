from datetime import date
from typing import Optional

from pydantic import BaseModel

from app.models import StatusEnum


class EmployeeBase(BaseModel):
    first_name: str
    last_name: str
    patronymic: Optional[str]
    position: str


class EmployeeCreate(EmployeeBase):
    pass


class Employee(EmployeeBase):
    id: int

    class Config:
        orm_mode = True


class TaskBase(BaseModel):
    name: str
    parent_task: Optional[int]
    performer: Optional[int]
    deadline: date
    status: StatusEnum


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: int

    class Config:
        orm_mode = True
