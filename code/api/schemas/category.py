from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class CategoryCreate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


class CategoryUpdate(BaseModel):
    text: Optional[str] = None
    description: Optional[str] = None


class CategoryDB(CategoryCreate):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
