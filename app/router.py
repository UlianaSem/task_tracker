from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import schemas, crud, database, serviсes


employees_router = APIRouter(prefix="/employee", tags=['Employee'])
tasks_router = APIRouter(prefix="/task", tags=['Task'])


@employees_router.get('/{employee_id}', response_model=schemas.Employee)
def get_employee(employee_id: int, db: Session = Depends(database.get_db)):
    db_employee = crud.get_employee(db, employee_id=employee_id)

    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")

    return db_employee


@employees_router.get('/', response_model=list[schemas.Employee])
def get_employees(skip: int = 0, limit: int = 20, db: Session = Depends(database.get_db)):
    employees = crud.get_employees(db, skip=skip, limit=limit)

    return employees


@employees_router.post('/', response_model=schemas.Employee)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(database.get_db)):
    return crud.create_employee(db=db, employee=employee)


@employees_router.patch('/{employee_id}', response_model=schemas.Employee)
def update_employee(employee_id: int, employee: schemas.EmployeeUpdate, db: Session = Depends(database.get_db)):
    db_employee = crud.get_employee(db, employee_id=employee_id)

    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")

    return crud.update_employee(db=db, employee_id=employee_id, employee=employee)


@employees_router.delete('/{employee_id}', response_model=schemas.Employee)
def delete_employee(employee_id: int, db: Session = Depends(database.get_db)):
    db_employee = crud.get_employee(db, employee_id=employee_id)

    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")

    return crud.delete_employee(db=db, employee_id=employee_id)


@tasks_router.get('/{task_id}', response_model=schemas.Task)
def get_task(task_id: int, db: Session = Depends(database.get_db)):
    db_task = crud.get_task(db, task_id=task_id)

    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return db_task


@tasks_router.get('/', response_model=list[schemas.Task])
def get_tasks(skip: int = 0, limit: int = 20, db: Session = Depends(database.get_db)):
    tasks = crud.get_tasks(db, skip=skip, limit=limit)

    return tasks


@tasks_router.post('/', response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(database.get_db)):
    return crud.create_task(db=db, task=task)


@tasks_router.patch('/{task_id}', response_model=schemas.Task)
def update_task(task_id: int, task: schemas.TaskUpdate, db: Session = Depends(database.get_db)):
    db_task = crud.get_task(db, task_id=task_id)

    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return crud.update_task(db=db, task_id=task_id, task=task)


@tasks_router.delete('/{task_id}', response_model=schemas.Task)
def delete_task(task_id: int, db: Session = Depends(database.get_db)):
    db_task = crud.get_task(db, task_id=task_id)

    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return crud.delete_task(db=db, task_id=task_id)


@employees_router.get('/busy/', response_model=list[schemas.BusyEmployee])
def get_busy_employees(skip: int = 0, limit: int = 20, db: Session = Depends(database.get_db)):
    return serviсes.get_busy_employees(skip=skip, limit=limit, db=db)


@tasks_router.get('/major/', response_model=list[schemas.MajorTask])
def get_major_tasks(skip: int = 0, limit: int = 20, db: Session = Depends(database.get_db)):
    return serviсes.get_major_tasks(skip=skip, limit=limit, db=db)
