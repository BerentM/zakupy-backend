from typing import Optional

from pydantic import BaseModel


class ProductList(BaseModel):
    product: Optional[str]
    source: Optional[str]
    category: Optional[str]
    target_amount: Optional[int]
    current_amount: Optional[int] = 0


class ProductListOut(ProductList):
    id: int
    product: str
    source: str
    category: str
    target_amount: int
    current_amount: int = 0
    missing_amount: int = 0


class ProductListAPI(BaseModel):
    product_list: list[ProductListOut] = []
    count: Optional[int] = None