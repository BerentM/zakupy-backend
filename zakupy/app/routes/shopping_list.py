from typing import List, Optional

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

import app.db.schemas as s
from app.db.actions import ProductDAL
from app.db.db import get_async_session

from .utils import calc_missing

router = APIRouter(
    prefix="/shoppingList",
    tags=["shoppingList"],
)


@router.get("/all")
async def get_missing_product_list(
    source: Optional[str] = None,
    missing_percent: Optional[float] = 0,
    session=Depends(get_async_session),
) -> tuple[List[s.ProductListOut], int]:
    data = await ProductDAL.get_all(
        session=session,
        missing_percent=missing_percent,
        source=source,
    )
    return [await calc_missing(item) for item in data[0]], data[1]


@router.patch("/fill_up")
async def fill_up_current_amount(
    ids: list[int],
    session: AsyncSession = Depends(get_async_session),
):
    for id in ids:
        product = await ProductDAL.get_one(session, id)
        product.current_amount = product.target_amount
        await ProductDAL.update(session, id, product)
