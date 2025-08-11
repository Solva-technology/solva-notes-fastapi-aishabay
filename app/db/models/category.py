from sqlalchemy import Column, String, Text
from sqlalchemy.orm import relationship

from app.core.constants import TITLE_MAX_LEN
from app.core.db import Base


class Category(Base):
    title = Column(String(TITLE_MAX_LEN), unique=True, nullable=False)
    description = Column(Text, nullable=True)

    notes = relationship(
        "Note",
        secondary="note_category_association",
        back_populates="categories"
    )
