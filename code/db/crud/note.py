import logging
from typing import Optional

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from code.db.crud.base import CRUDBase
from code.db.models import Category, Note, User


logger = logging.getLogger(__name__)


class CRUDNote(CRUDBase):
    async def create(
            self,
            obj_in,
            session: AsyncSession,
            user: Optional[User] = None,
    ):
        logger.info(
            f"Attempting to create Note for user_id="
            f"{getattr(user, 'id', None)} with categories="
            f"{obj_in.category_ids}",
        )

        stmt = select(Category).where(Category.id.in_(obj_in.category_ids))
        result = await session.execute(stmt)
        categories = result.scalars().all()

        if len(categories) != len(obj_in.category_ids):
            logger.warning(
                f"Category validation failed for user_id="
                f"{getattr(user, 'id', None)}. "
                f"Provided={obj_in.category_ids}, found="
                f"{[c.id for c in categories]}",
            )
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

        logger.info(
            f"Note created successfully id={db_obj.id} "
            f"by user_id={db_obj.author_id} "
            f"with categories={[c.id for c in categories]}",
        )

        return db_obj


note_crud = CRUDNote(Note)
