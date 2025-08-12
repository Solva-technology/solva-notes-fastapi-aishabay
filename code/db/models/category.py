from sqlalchemy import Column, String, Text
from sqlalchemy.orm import relationship

from code.core.constants import TITLE_MAX_LEN
from code.core.db import Base


class Category(Base):
    title = Column(String(TITLE_MAX_LEN), unique=True, nullable=False)
    description = Column(Text, nullable=True)

    notes = relationship(
        "Note",
        secondary="note_category_association",
        back_populates="categories"
    )

    def __repr__(self):
        return self.title
