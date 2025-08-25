from typing import Optional

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from code.db.crud.base import CRUDBase
from code.db.models import Category, Note, User


class CRUDNote(CRUDBase):
    async def create(
            self,
            obj_in,
            session: AsyncSession,
            user: Optional[User] = None,
    ):
        stmt = select(Category).where(Category.id.in_(obj_in.category_ids))
        result = await session.execute(stmt)
        categories = result.scalars().all()

        if len(categories) != len(obj_in.category_ids):
            raise HTTPException(
                status_code=400, detail="One or more categories do not exist",
            )

        db_obj = self.model(
            text=obj_in.text,
            author_id=user.id,
            categories=categories,
        )
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj


note_crud = CRUDNote(Note)
