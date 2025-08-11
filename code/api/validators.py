from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from code.db.crud.note import note_crud


async def check_note_exist(
    note_id: int,
    session: AsyncSession
):
    note = await note_crud.get(note_id, session)
    if note is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Заметка не найдена!'
        )
    return note
