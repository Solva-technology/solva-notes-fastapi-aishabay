from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from code.api.schemas.category import (
    CategoryCreate,
    CategoryDB,
    CategoryUpdate,
)
from code.api.validators import check_category_exist
from code.core.constants import LIMIT, SKIP
from code.core.db import get_async_session
from code.core.user import current_superuser
from code.db.crud.category import category_crud
from code.db.models import User


router = APIRouter()


@router.post(
    "/",
    response_model=CategoryDB,
    dependencies=[Depends(current_superuser)],
)
async def create_new_category(
    new_category: CategoryCreate,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_superuser),
):
    return await category_crud.create(new_category, session, user=user)


@router.patch(
    "/{id}",
    response_model=CategoryDB,
    dependencies=[Depends(current_superuser)],
)
async def update_category_by_id(
    category_id: int,
    old_category: CategoryUpdate,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_superuser),
):
    db_category = await check_category_exist(
        category_id=category_id, session=session, user=user,
    )
    return await category_crud.update(
        db_category, old_category, session, user=user,
    )


@router.get(
    "/",
    response_model=list[CategoryDB],
    dependencies=[Depends(current_superuser)],
)
async def get_all_categories(
    skip: int = SKIP,
    limit: int = LIMIT,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_superuser),
):
    return await category_crud.get_multi(
        skip=skip, limit=limit, session=session, user=user,
    )


@router.get(
    "/{id}",
    response_model=CategoryDB,
    dependencies=[Depends(current_superuser)],
)
async def get_category_by_id(
    category_id: int,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_superuser),
):
    return await check_category_exist(
        category_id=category_id, session=session, user=user,
    )


@router.delete(
    "/{id}",
    response_model=CategoryDB,
    dependencies=[Depends(current_superuser)],
)
async def delete_category_by_id(
    category_id: int,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_superuser),
):
    db_category = await check_category_exist(
        category_id=category_id, session=session, user=user,
    )
    return await category_crud.remove(db_category, session, user)
