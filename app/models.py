from sqlalchemy import Column, Integer, String, ForeignKey, Date, Enum

from app.database import Base


class StatusEnum(Enum):
    created = "created"
    done = "done"


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
    performer = Column(Integer, ForeignKey('employees.id', ondelete='CASCADE'), nullable=False, index=True)
    deadline = Column(Date, nullable=False)
    status = Column(StatusEnum(name='status_enum', create_type=False), default=StatusEnum.created, nullable=False)
