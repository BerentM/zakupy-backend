from sqlalchemy import func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Query
from sqlmodel import select

import app.db.schemas as s

from .models import ProductList


class ProductListDAL:
    model = ProductList
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
    async def get_one(
        cls,
        session: AsyncSession,
        id: int,
    ):
        q = select(cls.model)
        q = q.where(cls.model.id == id)

        ex = await session.execute(q)
        result = ex.scalars().first()

        return result

    @classmethod
    async def create(
        cls,
        session: AsyncSession,
        new_item: ProductList,
    ):
        session.add(new_item)
        await session.commit()

        return new_item

    @classmethod
    async def update(
        cls,
        session: AsyncSession,
        update_id: int,
        new_item: s.ProductList,
    ):
        obj = await cls.get_one(session=session, id=update_id)
        new_data = new_item.dict(exclude_unset=True)
        for key, value in new_data.items():
            setattr(obj, key, value)

        session.add(obj)
        await session.commit()
        await session.refresh(obj)

        return obj

    @classmethod
    async def delete(
        cls,
        session: AsyncSession,
        delete_id: int,
    ):
        obj = await cls.get_one(session=session, id=delete_id)
        await session.delete(obj)
        await session.commit()

        return obj

    @classmethod
    async def count(
        cls,
        session: AsyncSession,
        q: Query,
    ):
        c = func.count(getattr(q.c, cls.id_key))
        result = await session.execute(c)
        return result.scalar_one()
