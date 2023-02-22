from fastapi import APIRouter, Depends

from app.db.actions import ShoppingListDAL
from app.db.db import get_async_session

router = APIRouter(
    prefix="/shoppingList",
    tags=["shoppingList"],
)


@router.get("/all")
async def get_full_shopping_list(session=Depends(get_async_session)):
    return await ShoppingListDAL.get_all(session=session)
