from code.db.models import User
from http import HTTPStatus
from typing import Optional

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class CRUDBase:
    def __init__(self, model):
        self.model = model

    async def get(
        self,
        obj_id: int,
        session: AsyncSession,
    ):
        db_obj = await session.execute(
            select(self.model).where(self.model.id == obj_id)
        )
        return db_obj.scalars().first()

    async def get_or_404(self, obj_id: int, session: AsyncSession):
        obj = await self.get(obj_id, session)
        if obj is None:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND,
                detail=f"{self.model.__name__} not found"
            )
        return obj

    async def get_owned_or_403(
            self,
            obj_id: int,
            session: AsyncSession,
            user: Optional[User],
            owner_field: str = "author_id"
    ):
        obj = await self.get_or_404(obj_id, session)
        if getattr(obj, owner_field) != user.id and not user.is_superuser:
            raise HTTPException(
                status_code=HTTPStatus.FORBIDDEN,
                detail="Not authorized to access this resource",
            )
        return obj

    async def get_multi(
        self,
        skip: int,
        limit: int,
        session: AsyncSession,
    ):
        db_objs = await session.execute(
            select(self.model).offset(skip).limit(limit)
        )
        return db_objs.scalars().all()

    async def create(
            self,
            obj_in,
            session: AsyncSession,
            user: Optional[User] = None
    ):
        obj_in_data = obj_in.dict()
        if user is not None:
            obj_in_data["user_id"] = user.id
        db_obj = self.model(**obj_in_data)
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj

    async def update(
        self,
        db_obj,
        obj_in,
        session: AsyncSession
    ):
        update_data = obj_in.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_obj, field, value)
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj

    async def remove(
        self,
        db_obj,
        session: AsyncSession,
    ):
        await session.delete(db_obj)
        await session.commit()
        return db_obj
