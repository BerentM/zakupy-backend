from typing import List, Tuple

from fastapi import APIRouter, Depends

import app.db.schemas as s
from app.db.actions import ShoppingListDAL
from app.db.db import get_async_session
from app.db.models import ShoppingList

router = APIRouter(
    prefix="/shoppingList",
    tags=["shoppingList"],
)


async def calc_missing(data: ShoppingList) -> s.ShoppingListOut:
    out = s.ShoppingListOut(**data.__dict__)
    out.missing_amount = max(out.target_amount - out.current_amount, 0)
    return out


@router.get("/all")
async def get_full_shopping_list(
    session=Depends(get_async_session),
) -> tuple[List[s.ShoppingListOut], int]:
    data = await ShoppingListDAL.get_all(session=session)
    return [await calc_missing(item) for item in data[0]], data[1]


@router.get("/one")
async def get_single_shopping_list_element(
    id: int, session=Depends(get_async_session)
) -> s.ShoppingListOut:
    data = await ShoppingListDAL.get_one(session=session, id=id)
    return await calc_missing(data)


@router.post("/create_item")
async def add_shopping_list_element(
    new_item: ShoppingList, session=Depends(get_async_session)
) -> ShoppingList:
    return await ShoppingListDAL.create(session=session, new_item=new_item)


@router.delete("/delete_item")
async def remove_shopping_list_element(
    id: int, session=Depends(get_async_session)
) -> ShoppingList:
    return await ShoppingListDAL.delete(session=session, delete_id=id)


@router.patch("/update_item")
async def update_shopping_list_element(
    id: int, new_data: s.ShoppingList, session=Depends(get_async_session)
) -> ShoppingList:
    return await ShoppingListDAL.update(
        session=session, update_id=id, new_item=new_data
    )
