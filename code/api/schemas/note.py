from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class NoteCreate(BaseModel):
    text: Optional[str] = None


class NoteCreateRequest(BaseModel):
    text: Optional[str] = None
    category_ids: List[int]


class NoteUpdate(BaseModel):
    text: Optional[str] = None


class NoteDB(NoteCreate):
    id: int  # noqa: A003
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
