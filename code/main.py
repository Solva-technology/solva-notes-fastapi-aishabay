from contextlib import asynccontextmanager

from fastapi import FastAPI

from code.admin import init_admin
from code.api.routers import main_router
from code.core.config import settings
from logging_config import setup_logging


@asynccontextmanager
async def lifespan(app: FastAPI):
    listener = setup_logging()
    listener.start()
    yield
    listener.stop()

app = FastAPI(
    title=settings.APP_TITLE,
    description=settings.DESCRIPTION,
    lifespan=lifespan,
)
init_admin(app)

app.include_router(main_router)
