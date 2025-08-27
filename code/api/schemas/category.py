from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class CategoryCreate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


class CategoryUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


class CategoryDB(CategoryCreate):
    id: int  # noqa: A003
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
