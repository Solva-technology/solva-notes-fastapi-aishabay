from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession

from code.db.crud.category import category_crud
from code.db.crud.note import note_crud
from code.db.models import User


async def check_note_exist(
    note_id: int,
    session: AsyncSession,
    user: Optional[User] = None,
):
    return await note_crud.get_owned_or_403(note_id, session, user)


async def check_category_exist(
    category_id: int,
    session: AsyncSession,
    user: Optional[User] = None,
):
    return await category_crud.get_or_404(category_id, session, user)
