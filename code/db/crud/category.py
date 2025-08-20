from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession

from code.db.crud.base import CRUDBase
from code.db.models import Category, User


class CRUDCategory(CRUDBase):
    async def create(
            self,
            obj_in,
            session: AsyncSession,
            user: Optional[User] = None
    ):
        obj_in_data = obj_in.dict()
        db_obj = self.model(**obj_in_data)
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj


category_crud = CRUDCategory(Category)
