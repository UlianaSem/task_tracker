from datetime import date
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class EmployeeBase(BaseModel):
    patronymic: Optional[str] = None


class EmployeeCreate(EmployeeBase):
    first_name: str
    last_name: str
    position: str


class EmployeeUpdate(EmployeeBase):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    position: Optional[str] = None


class Employee(EmployeeBase):
    id: int
    first_name: str
    last_name: str
    position: str

    class Config:
        orm_mode = True


class StatusEnum(Enum):
    created = "created"
    taken_to_work = 'taken to work'
    done = "done"


class TaskBase(BaseModel):
    parent_task: Optional[int] = None
    performer: Optional[int] = None


class TaskCreate(TaskBase):
    name: str
    deadline: date
    status: StatusEnum


class TaskUpdate(TaskBase):
    name: Optional[str] = None
    deadline: Optional[date] = None
    status: Optional[StatusEnum] = None


class Task(TaskBase):
    id: int
    name: str
    deadline: date
    status: StatusEnum

    class Config:
        orm_mode = True
