from typing import List, Optional, Tuple

from fastapi import APIRouter, Depends

import app.db.schemas as s
from app.db.actions import ProductDAL
from app.db.db import get_async_session
from app.db.models import ProductList

from .utils import calc_missing

router = APIRouter(
    prefix="/productList",
    tags=["productList"],
)


@router.get("/all")
async def get_full_product_list(
    session=Depends(get_async_session),
) -> tuple[List[s.ProductListOut], int]:
    data = await ProductDAL.get_all(session=session)
    return [await calc_missing(item) for item in data[0]], data[1]


@router.get("/one")
async def get_single_product_list_element(
    id: int, session=Depends(get_async_session)
) -> s.ProductListOut:
    data = await ProductDAL.get_one(session=session, id=id)
    return await calc_missing(data)


@router.post("/create_item")
async def add_product_list_element(
    new_item: ProductList, session=Depends(get_async_session)
) -> ProductList:
    return await ProductDAL.create(session=session, new_item=new_item)


@router.delete("/delete_item")
async def remove_product_list_element(
    id: int, session=Depends(get_async_session)
) -> ProductList:
    return await ProductDAL.delete(session=session, delete_id=id)


@router.patch("/update_item")
async def update_product_list_element(
    id: int, new_data: s.ProductList, session=Depends(get_async_session)
) -> ProductList:
    return await ProductDAL.update(session=session, update_id=id, new_item=new_data)
