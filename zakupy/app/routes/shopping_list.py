from typing import Optional

import app.db.schemas as s
from app.db.actions import ProductDAL
from app.db.db import get_async_session
from app.db.models import User
from app.users.user_manager import current_active_verified_user
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

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
    user: User = Depends(current_active_verified_user), 
) -> s.ProductListAPI:
    data = await ProductDAL.get_all(
        session=session,
        missing_percent=missing_percent,
        source=source,
    )
    return s.ProductListAPI(product_list=[await calc_missing(item) for item in data[0]], count=data[1])


@router.patch("/fill_up")
async def fill_up_current_amount(
    ids: list[int],
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_active_verified_user), 
):
    for id in ids:
        product = await ProductDAL.get_one(session, id)
        product.current_amount = product.target_amount
        await ProductDAL.update(session, id, product)
