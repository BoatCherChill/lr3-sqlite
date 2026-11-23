# LR3 — FastAPI + SQLite + SQLAlchemy

Лабораторная работа №3: бэкенд на FastAPI с хранением данных в SQLite через SQLAlchemy ORM.

## Стек
- Python 3.12
- FastAPI
- SQLAlchemy 2.x
- SQLite
- Pydantic v2
- Docker

## Эндпоинты
| Метод | Путь | Описание |
|---|---|---|
| POST | `/students` | Создать студента |
| GET | `/students` | Список всех студентов |
| GET | `/students/{id}` | Студент по id |
| PUT | `/students/{id}` | Изменить имя студента |
| DELETE | `/students/{id}` | Удалить студента |

Документация Swagger: `http://localhost:8000/docs`

## Запуск локально
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Запуск в Docker
```bash
docker build -t students-db-api .
docker run -d -p 8000:8000 --name students-db-api students-db-api
```