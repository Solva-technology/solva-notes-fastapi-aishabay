from typing import Optional

from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from code.core.db import Base


class NoteCategory(Base):
    note_fk = mapped_column(ForeignKey("note.id"), primary_key=True)
    category_fk = mapped_column(ForeignKey("category.id"), primary_key=True)

    id = None


class Note(Base):
    text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    author_id: Mapped[int] = mapped_column(
        ForeignKey("user.id", ondelete="CASCADE"),
        nullable=False,
    )
    author: Mapped["User"] = relationship(  # noqa: F821
        back_populates="notes",
        passive_deletes=True,
    )

    categories: Mapped[list["Category"]] = relationship(  # noqa: F821
        secondary="notecategory",
        back_populates="notes",
        uselist=True,
    )

    def __repr__(self):
        return (
            f"id={self.id}, text={self.text[:20]}, "
            f"author_id={self.author_id}"
        )
