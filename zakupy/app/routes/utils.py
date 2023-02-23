import app.db.schemas as s
from app.db.models import ProductList


async def calc_missing(data: ProductList) -> s.ProductListOut:
    out = s.ProductListOut(**data.__dict__)
    out.missing_amount = max(out.target_amount - out.current_amount, 0)
    return out
