from typing import Optional

from pydantic import BaseModel


class ShoppingList(BaseModel):
    product: Optional[str]
    source: Optional[str]
    category: Optional[str]
    target_amount: Optional[int]
    current_amount: Optional[int] = 0
