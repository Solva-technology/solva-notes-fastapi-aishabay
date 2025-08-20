from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from code.api.schemas.note import NoteCreate, NoteCreateRequest, NoteUpdate, NoteDB
from code.api.validators import check_note_exist
from code.core.db import get_async_session
from code.core.user import current_user, current_superuser
from code.db.crud.note import note_crud
from code.db.models import Category, Note
from code.db.models import User

router = APIRouter()


@router.post(
    '/',
    response_model=NoteDB
)
async def create_new_note(
    new_note: NoteCreateRequest,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user)
):
    stmt = select(Category).where(Category.id.in_(new_note.category_ids))
    result = await session.execute(stmt)
    categories = result.scalars().all()

    if len(categories) != len(new_note.category_ids):
        raise HTTPException(status_code=400, detail="One or more categories do not exist")

    db_obj = Note(
        text=new_note.text,
        author_id=user.id,
        categories=categories
    )
    session.add(db_obj)
    await session.commit()
    await session.refresh(db_obj)
    return db_obj

    # note_data = NoteCreate(
    #     text=new_note.text,
    #     # categories=categories
    # )
    # return await note_crud.create(note_data, session, user)


@router.patch(
    '/{id}',
    response_model=NoteDB
)
async def update_note_by_id(
    id: int,
    old_note: NoteUpdate,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user)
):
    db_note = await check_note_exist(note_id=id, session=session, user=user)
    # if db_note.author_id != user.id and not user.is_superuser:
    #     raise HTTPException(
    #         status_code=status.HTTP_403_FORBIDDEN,
    #         detail="Not authorized to update this note"
    #     )
    return await note_crud.update(db_note, old_note, session, user)


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
    user: User = Depends(current_user)
):
    return await check_note_exist(note_id=id, session=session, user=user)


@router.delete(
    '/{id}',
    response_model=NoteDB
)
async def delete_note_by_id(
        id: int,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user)
):
    db_note = await check_note_exist(note_id=id, session=session, user=user)
    return await note_crud.remove(db_note, session)
