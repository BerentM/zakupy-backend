from typing import List, Tuple

from fastapi import APIRouter, Depends

import app.db.schemas as s
from app.db.actions import ProductListDAL
from app.db.db import get_async_session
from app.db.models import ProductList

router = APIRouter(
    prefix="/productList",
    tags=["productList"],
)


async def calc_missing(data: ProductList) -> s.ProductListOut:
    out = s.ProductListOut(**data.__dict__)
    out.missing_amount = max(out.target_amount - out.current_amount, 0)
    return out


@router.get("/all")
async def get_full_product_list(
    session=Depends(get_async_session),
) -> tuple[List[s.ProductListOut], int]:
    data = await ProductListDAL.get_all(session=session)
    return [await calc_missing(item) for item in data[0]], data[1]


@router.get("/one")
async def get_single_product_list_element(
    id: int, session=Depends(get_async_session)
) -> s.ProductListOut:
    data = await ProductListDAL.get_one(session=session, id=id)
    return await calc_missing(data)


@router.post("/create_item")
async def add_product_list_element(
    new_item: ProductList, session=Depends(get_async_session)
) -> ProductList:
    return await ProductListDAL.create(session=session, new_item=new_item)


@router.delete("/delete_item")
async def remove_product_list_element(
    id: int, session=Depends(get_async_session)
) -> ProductList:
    return await ProductListDAL.delete(session=session, delete_id=id)


@router.patch("/update_item")
async def update_product_list_element(
    id: int, new_data: s.ProductList, session=Depends(get_async_session)
) -> ProductList:
    return await ProductListDAL.update(session=session, update_id=id, new_item=new_data)
