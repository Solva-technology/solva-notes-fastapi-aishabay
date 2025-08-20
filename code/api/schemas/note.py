from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class NoteCreate(BaseModel):
    text: Optional[str] = None
    # categories: List[Category] = []


class NoteCreateRequest(BaseModel):
    text: Optional[str] = None
    category_ids: List[int]


class NoteUpdate(BaseModel):
    text: Optional[str] = None


class NoteDB(NoteCreate):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
