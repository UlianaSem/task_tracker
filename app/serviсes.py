from sqlalchemy import func, desc
from sqlalchemy.orm import Session, aliased
from sqlalchemy.sql.operators import or_, and_

from app import models


def get_busy_employees(db: Session, skip: int = 0, limit: int = 20):
    """Запрашивает из БД список сотрудников и их задачи, отсортированный по количеству активных задач."""

    query = db.query(
        models.Employee
    ).join(
        models.Task
    ).filter(
        or_(models.Task.status == 'created', models.Task.status == 'taken_to_work')
    ).group_by(
        models.Employee.id
    ).order_by(
        desc(func.count(models.Employee.tasks))
    ).offset(skip).limit(limit)

    return query


def get_major_tasks(db: Session, skip: int = 0, limit: int = 20):
    """ Запрашивает из БД важные задачи, реализует поиск по сотрудникам, которые могут взять такие задачи и возвращает
    список объектов [{Важная задача, Срок, [ФИО сотрудника]}]"""

    task = aliased(models.Task)
    employee = aliased(models.Employee)

    min_tasks_number = db.query(
        func.count(task.id)
    ).outerjoin(
        employee, full=True
    ).group_by(
        employee.id
    ).order_by(
        func.count(task.id)
    ).limit(1).scalar_subquery()

    employee_query = db.query(
        employee
    ).outerjoin(
        task
    ).group_by(
        employee.id
    ).having(
        func.count(task.id) == min_tasks_number
    ).subquery()

    query_1 = db.query(
        task
    ).filter(
        and_(task.status == 'created', task.parent_task.in_(
            db.query(task.id).filter(
                task.status == 'taken_to_work'
            )
        ))
    ).subquery()

    query_2 = db.query(
        query_1.c.id, task.performer
    ).join(
        query_1, task.id == query_1.c.parent_task
    ).subquery()

    query_3 = db.query(
        employee
    ).join(
        query_2, employee.id == query_2.c.performer
    ).outerjoin(
        task, query_2.c.performer == task.performer, full=True
    ).group_by(
        employee.id
    ).having(
        func.count(task.id) <= min_tasks_number + 2
    ).subquery()

    query_4 = db.query(
        query_1.c.name.label('name'), query_1.c.deadline.label('deadline'),
        func.concat_ws(' ', query_3.c.first_name, query_3.c.last_name, query_3.c.patronymic).label('employees')
    ).join(
        query_2, query_1.c.id == query_2.c.id
    ).join(
        query_3, query_2.c.performer == query_3.c.id
    )

    query_5 = db.query(
        query_1.c.name.label('name'), query_1.c.deadline.label('deadline'),
        func.concat_ws(' ', employee_query.c.first_name, employee_query.c.last_name, employee_query.c.patronymic).label(
            'employees')
    )

    main_query = query_4.union(
        query_5
    ).cte(name="main_query")

    main = db.query(
        main_query.c.name, main_query.c.deadline, func.array_agg(main_query.c.employees).label('employees')
    ).group_by(
        main_query.c.name, main_query.c.deadline
    ).offset(skip).limit(limit)

    return main
