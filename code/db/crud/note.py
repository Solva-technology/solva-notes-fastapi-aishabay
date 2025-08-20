from code.db.crud.base import CRUDBase
from code.db.models import Note, User
from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession


class CRUDNote(CRUDBase):
    async def create(
            self,
            obj_in,
            session: AsyncSession,
            user: Optional[User] = None
    ):
        obj_in_data = obj_in.dict()
        if user is not None:
            obj_in_data['author_id'] = user.id
        db_obj = self.model(**obj_in_data)
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj


note_crud = CRUDNote(Note)
