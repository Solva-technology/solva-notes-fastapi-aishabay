from fastapi import FastAPI
from sqladmin import Admin, ModelView

from code.db.models import Category, Note, User, note_category_association
from code.core.db import engine


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.email]
    name = "User"
    name_plural = "Users"


class CategoryAdmin(ModelView, model=Category):
    column_list = [Category.title, Category.description]
    name = "Category"
    name_plural = "Categories"


class NoteAdmin(ModelView, model=Note):
    column_list = [Note.text, "author_email", "category_titles"]
    # column_list = [Note.text, Note.author, Note.categories]
    name = "Note"
    name_plural = "Notes"

    def author_email(self, obj):
        return obj.author.email if obj.author else None

    def category_titles(self, obj):
        return ", ".join(cat.title for cat in obj.categories) if obj.categories else None

    author_email.__name__ = "Author"
    category_titles.__name__ = "Categories"

    # column_formatters = {
    #     Note.author: lambda model, attr: model.author.email if model.author else "",
    #     # Note.categories: lambda model, attr: ", ".join(c.title for c in model.categories) if model.categories else "",
    # }


# class NoteCategoryAssociationAdmin(ModelView, model=note_category_association):
#     column_list = "__all__"


app: FastAPI = None

admin = None


def init_admin(fastapi_app: FastAPI):
    global app, admin
    app = fastapi_app
    admin = Admin(app=app, engine=engine)
    admin.add_view(UserAdmin)
    admin.add_view(CategoryAdmin)
    admin.add_view(NoteAdmin)
