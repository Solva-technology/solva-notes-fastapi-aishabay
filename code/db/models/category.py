from typing import Optional

from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from code.core.constants import TITLE_MAX_LEN
from code.core.db import Base


class Category(Base):
    title: Mapped[str] = mapped_column(
        String(TITLE_MAX_LEN), unique=True, nullable=False,
    )
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    notes: Mapped[list["Note"]] = relationship(  # noqa: F821
        secondary="notecategory",
        back_populates="categories",
        uselist=True,
    )

    def __repr__(self):
        return (
            f"id={self.id}, title={self.title},"
            f" description={self.description[:20]}"
        )
