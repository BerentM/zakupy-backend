from typing import List, Optional, Tuple

import app.db.schemas as s
from app.db.actions import ProductDAL
from app.db.db import get_async_session
from app.db.models import ProductList
from fastapi import APIRouter, Depends

from .utils import calc_missing

router = APIRouter(
    prefix="/productList",
    tags=["productList"],
)


@router.get("/all")
async def get_full_product_list(
    session=Depends(get_async_session),
) -> s.ProductListAPI:
    data = await ProductDAL.get_all(session=session)
    return s.ProductListAPI(product_list=[await calc_missing(item) for item in data[0]], count=data[1])


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
    data = await ProductDAL.create(session=session, new_item=new_item)
    return await calc_missing(data)


@router.delete("/delete_item")
async def remove_product_list_element(
    id: int, session=Depends(get_async_session)
) -> ProductList:
    data = await ProductDAL.delete(session=session, delete_id=id)
    return await calc_missing(data)


@router.patch("/update_item")
async def update_product_list_element(
    id: int, new_data: s.ProductList, session=Depends(get_async_session)
) -> ProductList:
    data = await ProductDAL.update(session=session, update_id=id, new_item=new_data)
    return await calc_missing(data)
