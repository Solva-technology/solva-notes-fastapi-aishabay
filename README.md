[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=20046194&assignment_repo_type=AssignmentRepo)
# [📒 Note App](https://github.com/Solva-technology/solva-notes-fastapi-aishabay.git)
CRUD-приложение для работы с заметками пользователей, разработанное на FastAPI с
использованием базы данных PostgreSQL. Проект поддерживает разграничение доступа
между пользователями и администраторами, хранение данных в БД с миграциями и
управление через админ-панель.

## Автор: [Aisha](https://www.linkedin.com/in/aisha-zhumagul/) | Python разработчик
## 🚀 Технологический стек
- Python + FastAPI
- PostgreSQL + SQLAlchemy
- Alembic - миграции
- SQLAdmin - админ-панель
- Docker + Docker Compose

## Инструкция по запуску
1. Введите в терминале
```
git clone git@github.com:Solva-technology/solva-notes-fastapi-aishabay.git
```

2. Перейдите в директорию данного проекта
```
cd solva-notes-fastapi-aishabay
```

3. Убедитесь что Docker запущен.
```
docker version
```

4. Добавьте `.env` файл в проект
#### Пример .env файла:
```
PRODUCTION=False
APP_TITLE=Solva Notes FastAPI
DESCRIPTION=Приложение для заметок
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DATABASE_URL=postgresql+asyncpg://postgres:postgres@db:5432/postgres
SECRET_WORD=SOLVA
ADMIN_AUTH_SECRET_KEY=supersecret
```

5. Создайте и запустите контейнеры
```
docker compose up -d
```

6. Загрузите данные из `data.sql` в базу данных
```
docker cp data.sql db:.
```
```
docker compose exec db psql -U postgres -d postgres -f data.sql
```

7. Креды суперпользователя/админа для доступа в админ-панель по ссылке `http://localhost:8000/admin` в браузере.
- Имя пользователя: ```root```
- Пароль: ```rootroot```

8. 🔗 Ссылки проекта

| Назначение                               | Ссылка                                                     |
| ---------------------------------------- | ---------------------------------------------------------- |
| Страница с эндпойнтами проекта (Swagger) | [http://localhost:8000/docs](http://localhost:8000/docs)   |
| Альтернативная документация (ReDoc)      | [http://localhost:8000/redoc](http://localhost:8000/redoc) |
| Админ-панель SQLAdmin                    | [http://localhost:8000/admin](http://localhost:8000/admin) |

8. Остановите и удалите контейнеры
```
docker compose down -v
```
