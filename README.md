# LR3

Лабораторная работа №3: бэкенд на FastAPI с хранением данных в SQLite через SQLAlchemy ORM.

## Стек

- Python 3.12
- FastAPI
- SQLAlchemy 2.x
- SQLite
- Pydantic v2
- Docker

## Структура проекта
```
lr3-sqlite/
├── app/
│ ├── init.py
│ ├── main.py # эндпоинты FastAPI
│ ├── schemas.py # Pydantic-модели
│ ├── models.py # SQLAlchemy-модели
│ └── database.py # подключение к SQLite, get_db()
├── requirements.txt
├── Dockerfile
├── .gitignore
└── README.md
```

## Эндпоинты

| Метод | Путь | Описание | Коды ответа |
|---|---|---|---|
| POST | `/students` | Создать студента | 201, 400, 422 |
| GET | `/students` | Список всех студентов | 200 |
| GET | `/students/{id}` | Студент по id | 200, 404, 422 |
| PUT | `/students/{id}` | Изменить имя студента | 200, 404, 422 |
| DELETE | `/students/{id}` | Удалить студента | 204, 404, 422 |

Swagger UI: `http://localhost:8000/docs`

## Модель данных

Таблица `students` в файле `students.db` (создаётся при первом запуске через `Base.metadata.create_all`).

| Столбец | Тип | Ограничения |
|---|---|---|
| `id` | INTEGER | PRIMARY KEY, индекс |
| `name` | VARCHAR | индекс |
| `email` | VARCHAR | UNIQUE, индекс |

Пример запроса POST:

```json
{ "name": "Ivan", "email": "ivan@example.com" }
```
Пример ответа (201):

```json
{ "id": 1, "name": "Ivan", "email": "ivan@example.com" }
```
Запуск локально
```bash
python -m venv .venv
source .venv/bin/activate        # Linux/macOS
.venv\Scripts\Activate.ps1       # Windows PowerShell
```
```
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Запуск в Docker
```bash
docker build -t students-db-api .
docker run -d -p 8000:8000 --name students-db-api students-db-api
```
Открыть: http://localhost:8000/docs
