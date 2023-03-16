import app.db.schemas as s


async def calc_missing(data: s.SchemaProductList) -> s.ProductListOut:
    out = s.ProductListOut(id=data.id,product=data.product, category=data.category, source=data.source, target_amount=data.target_amount, current_amount=data.current_amount, )
    out.missing_amount = max(out.target_amount - out.current_amount, 0)
    return out
