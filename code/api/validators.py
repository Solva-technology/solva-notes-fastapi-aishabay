from code.db.crud.category import category_crud
from code.db.crud.note import note_crud
from code.db.models import User
from http import HTTPStatus
from typing import Optional

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status


async def check_note_exist(
    note_id: int, session: AsyncSession, user: Optional[User] = None
):
    note = await note_crud.get(note_id, session)
    if note is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="Note not found!"
        )
    if note.author_id != user.id and not user.is_superuser:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to access this note",
        )
    return note


async def check_category_exist(category_id: int, session: AsyncSession):
    category = await category_crud.get(category_id, session)
    if category is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="Category not found!"
        )
    return category
