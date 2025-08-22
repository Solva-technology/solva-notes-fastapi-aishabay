from code.api.schemas.note import NoteCreateRequest, NoteDB, NoteUpdate
from code.api.validators import check_note_exist
from code.core.db import get_async_session
from code.core.user import current_superuser, current_user
from code.db.crud.note import note_crud
from code.db.models import User

from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


@router.post("/", response_model=NoteDB)
async def create_new_note(
    new_note: NoteCreateRequest,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    return await note_crud.create(new_note, session, user)


@router.patch("/{id}", response_model=NoteDB)
async def update_note_by_id(
    id: int,
    old_note: NoteUpdate,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    db_note = await check_note_exist(note_id=id, session=session, user=user)
    return await note_crud.update(db_note, old_note, session)


@router.get("/",
            response_model=list[NoteDB],
            dependencies=[Depends(current_superuser)])
async def get_all_notes(
    session: AsyncSession = Depends(get_async_session),
):
    return await note_crud.get_multi(session=session)


@router.get("/{id}", response_model=NoteDB)
async def get_note_by_id(
    id: int,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    return await check_note_exist(note_id=id, session=session, user=user)


@router.delete("/{id}", response_model=NoteDB)
async def delete_note_by_id(
    id: int,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    db_note = await check_note_exist(note_id=id, session=session, user=user)
    return await note_crud.remove(db_note, session)
