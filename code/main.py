from fastapi import FastAPI
from sqladmin import Admin

from code.api.routers import main_router
from code.core.config import settings
from code.admin import AdminAuth, UserAdmin, CategoryAdmin, NoteAdmin
from code.core.db import engine

app = FastAPI(title=settings.APP_TITLE, description=settings.DESCRIPTION)

app.include_router(main_router)


admin = Admin(
    app=app,
    engine=engine,
    authentication_backend=AdminAuth(secret_key="supersecret")
)
admin.add_view(UserAdmin)
admin.add_view(CategoryAdmin)
admin.add_view(NoteAdmin)
