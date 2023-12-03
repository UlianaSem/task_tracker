from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.dialects.postgresql import ENUM

from app.database import Base
from app.schemas import StatusEnum


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(150), nullable=False)
    last_name = Column(String(150), nullable=False)
    patronymic = Column(String(150), nullable=True)
    position = Column(String(200), nullable=False)


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    parent_task = Column(Integer, ForeignKey('tasks.id', ondelete='CASCADE'), nullable=True, index=True)
    performer = Column(Integer, ForeignKey('employees.id', ondelete='SET NULL'), nullable=True, index=True)
    deadline = Column(Date, nullable=False)
    status = Column(ENUM(StatusEnum, name='status_enum', create_type=False), default=StatusEnum.created, nullable=False)
