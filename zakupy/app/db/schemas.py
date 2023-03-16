from typing import Optional

from app.db.models import Category, Source
from pydantic import BaseModel


class ProductList(BaseModel):
    product: Optional[str]
    source: Optional[Source]
    category: Optional[Category]
    target_amount: Optional[int]
    current_amount: Optional[int] = 0


class ProductListOut(ProductList):
    id: int
    product: str
    source: Source
    category: Category
    target_amount: int
    current_amount: int = 0
    missing_amount: int = 0


class ProductListAPI(BaseModel):
    product_list: list[ProductListOut] = []
    count: Optional[int] = None
