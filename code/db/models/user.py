from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy.orm import Mapped, relationship

from code.core.base import Base


class User(SQLAlchemyBaseUserTable[int], Base):
    notes: Mapped[list["Note"]] = relationship(  # noqa: F821
        back_populates="author",
        cascade="all, delete-orphan",
    )

    def __repr__(self):
        return f"id={self.id}, email={self.email}"
