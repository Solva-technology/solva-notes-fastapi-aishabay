from code.core.config import settings
from code.core.db import AsyncSessionLocal, engine
from code.db.models import Category, Note, User

from fastapi import FastAPI
from fastapi_users.password import PasswordHelper
from sqladmin import Admin, ModelView
from sqladmin.authentication import AuthenticationBackend
from sqlalchemy import select
from starlette.requests import Request


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        email, password = form["username"], form["password"]

        async with AsyncSessionLocal() as session:
            user = await session.scalar(
                select(User).where(User.email == email)
            )

        if not user or not user.is_superuser:
            return False

        helper = PasswordHelper()

        if not helper.verify_and_update(password, user.hashed_password):
            return False

        request.session.update({"user_id": user.id})
        return True

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        user_id = request.session.get("user_id")
        if not user_id:
            return False
        async with AsyncSessionLocal() as session:
            return await session.get(User, user_id)


class UserAdmin(ModelView, model=User):
    name = "User"
    name_plural = "Users"
    column_list = [User.id, User.email]
    column_searchable_list = [User.email]
    form_excluded_columns = [User.notes, User.created_at, User.updated_at]
    form_widget_args = {
        "notes": {"readonly": True},
    }


class CategoryAdmin(ModelView, model=Category):
    name = "Category"
    name_plural = "Categories"
    column_list = [Category.title, Category.description]
    column_searchable_list = [Category.title, Category.description]
    column_sortable_list = [Category.title]
    form_excluded_columns = [
        Category.notes, Category.created_at, Category.updated_at
    ]
    form_widget_args = {
        "notes": {"readonly": True},
    }


class NoteAdmin(ModelView, model=Note):
    name = "Note"
    name_plural = "Notes"
    column_list = [Note.text, Note.author, Note.categories]
    column_searchable_list = [Note.text]
    column_sortable_list = [Note.text]
    column_formatters = {
        Note.author: lambda model, attr: model.author.email
        if model.author else "",
    }
    form_excluded_columns = [Note.created_at, Note.updated_at]


def init_admin(fastapi_app: FastAPI):
    admin = Admin(
        app=fastapi_app,
        engine=engine,
        authentication_backend=AdminAuth(
            secret_key=settings.ADMIN_AUTH_SECRET_KEY
        )
    )
    admin.add_view(UserAdmin)
    admin.add_view(CategoryAdmin)
    admin.add_view(NoteAdmin)

    return admin
