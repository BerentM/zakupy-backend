from typing import Optional

from pydantic import BaseModel


class ShoppingList(BaseModel):
    product: Optional[str]
    source: Optional[str]
    category: Optional[str]
    target_amount: Optional[int]
    current_amount: Optional[int] = 0


class ShoppingListOut(ShoppingList):
    product: str
    source: str
    category: str
    target_amount: int
    current_amount: int = 0
    missing_amount: int = 0
