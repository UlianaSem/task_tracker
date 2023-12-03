from fastapi import FastAPI

from app.router import tasks_router, employees_router

app = FastAPI()

app.include_router(employees_router)

app.include_router(tasks_router)
