from sqlalchemy import func, desc
from sqlalchemy.orm import Session
from sqlalchemy.sql.operators import or_

from app import models


def get_busy_employees(db: Session, skip: int = 0, limit: int = 20):
    """Запрашивает из БД список сотрудников и их задачи, отсортированный по количеству активных задач."""

    query = (db.query(models.Employee).
             join(models.Task).
             filter(or_(models.Task.status == 'created', models.Task.status == 'taken_to_work')).
             group_by(models.Employee.id).
             order_by(desc(func.count(models.Employee.tasks))).
             offset(skip).
             limit(limit))

    return query


def get_major_tasks(db: Session, skip: int = 0, limit: int = 20):
    """ 1) запрашивает из БД задачи не взятые в работу, и от которых зависят другие задачи, взятые в работу.
    2) реализует поиск по сотрудникам, которые могут взять такие задачи (наименее загруженный сотрудник или сотрудник
    выполняющий родительскую задачу если ему назначено максимум на 2 задачи больше, чем у наименее загруженного сотрудника).
    3) возвращает Список объектов [{Важная задача, Срок, [ФИО сотрудника]}]."""
    pass
