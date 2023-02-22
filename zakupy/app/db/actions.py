from sqlalchemy import func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Query
from sqlmodel import select

from .models import ShoppingList


class ShoppingListDAL:
    model = ShoppingList
    id_key = "id"

    @classmethod
    async def get_all(
        cls,
        session: AsyncSession,
        limit: int = 100,
        index: int = 0,
    ):
        q = select(cls.model)

        count: int = await cls.count(session, q)
        q = q.limit(limit).offset(index)

        ex = await session.execute(q)
        result = ex.scalars().all()
        return result, count

    @classmethod
    async def count(cls, session: AsyncSession, q: Query):
        c = func.count(getattr(q.c, cls.id_key))
        result = await session.execute(c)
        return result.scalar_one()
