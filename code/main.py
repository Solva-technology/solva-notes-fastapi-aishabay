from fastapi import FastAPI

from code.api.routers import main_router
from code.core.config import settings
from code.admin import init_admin

app = FastAPI(title=settings.APP_TITLE, description=settings.DESCRIPTION)
init_admin(app)

app.include_router(main_router)
