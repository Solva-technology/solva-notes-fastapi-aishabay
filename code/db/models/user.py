from code.core.base import Base

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy.orm import relationship


class User(SQLAlchemyBaseUserTable[int], Base):
    notes = relationship("Note", back_populates="author")

    def __repr__(self):
        return self.email
