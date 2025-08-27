import logging
from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession

from code.db.crud.base import CRUDBase
from code.db.models import Category, User


logger = logging.getLogger(__name__)


class CRUDCategory(CRUDBase):
    async def create(
            self,
            obj_in,
            session: AsyncSession,
            user: Optional[User] = None,
    ):
        logger.info(
            f"Attempting to create Category by user_id="
            f"{getattr(user, 'id', None)} with data={obj_in.dict()}",
        )

        obj_in_data = obj_in.dict()
        db_obj = self.model(**obj_in_data)
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)

        logger.info(
            f"Category created successfully id={db_obj.id} "
            f"by user_id={getattr(user, 'id', None)}",
        )

        return db_obj


category_crud = CRUDCategory(Category)
