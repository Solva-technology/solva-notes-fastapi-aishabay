from fastapi import FastAPI
from sqladmin import Admin, ModelView

from code.db.models import Category, Note, User
from code.core.db import engine


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.email]


class CategoryAdmin(ModelView, model=Category):
    column_list = [Category.title, Category.description]


class NoteAdmin(ModelView, model=Note):
    column_list = [Note.text, Note.author]


app: FastAPI = None

admin = None


def init_admin(fastapi_app: FastAPI):
    global app, admin
    app = fastapi_app
    admin = Admin(app=app, engine=engine)
    admin.add_view(UserAdmin)
    admin.add_view(CategoryAdmin)
    admin.add_view(NoteAdmin)
