from typing import Optional, List

from sqlalchemy.ext.asyncio import AsyncSession

from code.db.models import Note, User


class CRUDNoteCategory:
    # async def create(
    #         self,
    #         note: int,
    #         categories: List[int],
    #         session: AsyncSession,
    # ):
    pass
    # obj_in_data = obj_in.dict()
    # if user is not None:
    #     obj_in_data['author_id'] = user.id
    # db_obj = self.model(**obj_in_data)
    # session.add(db_obj)
    # await session.commit()
    # await session.refresh(db_obj)
    # return db_obj


note_crud = CRUDNoteCategory()
