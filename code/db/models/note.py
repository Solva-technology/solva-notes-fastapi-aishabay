from sqlalchemy import Column, ForeignKey, Integer, Table, Text
from sqlalchemy.orm import relationship

from code.core.db import Base


note_category_association = Table(
    "note_category_association",
    Base.metadata,
    Column(
        "note_id", Integer,
        ForeignKey("note.id"), primary_key=True,
    ),
    Column(
        "category_id", Integer,
        ForeignKey("category.id"), primary_key=True,
    ),
)


class Note(Base):
    text = Column(Text, nullable=True)
    author_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    author = relationship("User", back_populates="notes")

    categories = relationship(
        "Category",
        secondary=note_category_association,
        back_populates="notes",
    )

    def __repr__(self):
        return (
            f"id={self.id}, text={self.text[:20]}, "
            f"author_id={self.author_id}"
        )
