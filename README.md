# Tasks tracker

## Описание проекта

Проект трекера задач сотрудников, который включает в себя работу с сотрудниками и задачами. Реализован поиск наиболее занятых сотрудников, а также важных задач и сотрудников, которые могут взять эти задачи.

В рамках проекта реализована бэкенд-часть SPA веб-приложения. 

## Технологии

- Linux
- Python
- Poetry
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- Docker
- Docker Compose

## Зависимости

Зависимости, необходимые для работы проекта, указаны в файле pyproject.toml.
Чтобы установить зависимости, используйте команду `poetry install`

## Документация

Документация находится по ссылкам:
1. Swagger `docs/`
2. Redoc `redoc/`

## Как запустить проект

Для запуска проекта необходимо выполнить следующие шаги:
1. При необходимости установите Docker и Docker Compose на компьютер с помощью инструкции https://docs.docker.com/engine/install/
2. Cклонируйте репозиторий себе на компьютер
3. Создайте файл .env и заполните его, используя образец из файла .env.example
4. Соберите образ с помощью команды `docker-compose build`
5. Создайте БД командой `docker-compose exec db psql -U <postgres_user>`, а затем командой `CREATE DATABASE <database_name>;`
6. Запустите контейнеры с помощью команды `docker-compose up`

## Файл .env.example

1. `DATABASES_NAME` - название БД
2. `POSTGRES_USER` - имя пользователя
3. `POSTGRES_PASSWORD` - пароль
4. `DATABASES_HOST` - хост БД

## Авторы

UlianaSem

## Связь с авторами

https://github.com/UlianaSem/
