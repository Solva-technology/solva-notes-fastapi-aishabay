from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy.orm import relationship

from app.core.base import Base


class User(SQLAlchemyBaseUserTable[int], Base):
    notes = relationship("Note", back_populates="author")
