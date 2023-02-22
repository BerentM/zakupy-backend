from fastapi import APIRouter, Depends

import app.db.schemas as s
from app.db.actions import ShoppingListDAL
from app.db.db import get_async_session
from app.db.models import ShoppingList

router = APIRouter(
    prefix="/shoppingList",
    tags=["shoppingList"],
)


@router.get("/all")
async def get_full_shopping_list(session=Depends(get_async_session)):
    return await ShoppingListDAL.get_all(session=session)


@router.get("/one")
async def get_single_shopping_list_element(id: int, session=Depends(get_async_session)):
    return await ShoppingListDAL.get_one(session=session, id=id)


@router.post("/create_item")
async def add_shopping_list_element(
    new_item: ShoppingList, session=Depends(get_async_session)
):
    return await ShoppingListDAL.create(session=session, new_item=new_item)


@router.delete("/delete_item")
async def remove_shopping_list_element(id: int, session=Depends(get_async_session)):
    return await ShoppingListDAL.delete(session=session, delete_id=id)


@router.patch("/update_item")
async def update_shopping_list_element(
    id: int, new_data: s.ShoppingList, session=Depends(get_async_session)
):
    return await ShoppingListDAL.update(
        session=session, update_id=id, new_item=new_data
    )
