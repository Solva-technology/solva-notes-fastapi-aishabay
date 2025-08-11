from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from code.api.schemas.note import NoteCreate, NoteDB
from code.api.validators import check_note_exist
from code.core.db import get_async_session
from code.core.user import current_user, current_superuser
from code.db.crud.note import note_crud
from code.db.models import User

router = APIRouter()


@router.post(
    '/',
    response_model=NoteDB
)
async def create_new_note(
    new_note: NoteCreate,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user)
):
    return await note_crud.create(new_note, session, user)


@router.get(
    '/all',
    response_model=list[NoteDB],
    dependencies=[Depends(current_superuser)]
)
async def get_all_notes(
    session: AsyncSession = Depends(get_async_session),
):
    return await note_crud.get_multi(session=session)


@router.get(
    '/{id}',
    response_model=NoteDB
)
async def get_note_by_id(
    id: int,
    session: AsyncSession = Depends(get_async_session),
):
    return await check_note_exist(note_id=id, session=session)
