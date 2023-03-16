import app.db.schemas as s
from app.db.actions import ProductDAL
from app.db.db import get_async_session
from app.db.models import ProductList, User
from app.users.user_manager import current_active_verified_user
from fastapi import APIRouter, Depends

from .utils import calc_missing

router = APIRouter(
    prefix="/productList",
    tags=["productList"],
)


@router.get("/all", response_model=s.ProductListAPI)
async def get_full_product_list(
    session=Depends(get_async_session),
    user: User = Depends(current_active_verified_user),
) -> s.ProductListAPI:
    data = await ProductDAL.get_all(session=session)
    return s.ProductListAPI(
        product_list=[await calc_missing(item) for item in data[0]], count=data[1]
    )


@router.get("/one", response_model=s.ProductListOut)
async def get_single_product_list_element(
    id: int,
    session=Depends(get_async_session),
    user: User = Depends(current_active_verified_user),
) -> s.ProductListOut:
    data = await ProductDAL.get_one(session=session, id=id)
    return await calc_missing(data)


@router.post("/create_item", response_model=s.ProductListOut)
async def add_product_list_element(
    new_item: ProductList,
    session=Depends(get_async_session),
    user: User = Depends(current_active_verified_user),
) -> ProductList:
    new_data = await ProductDAL.create(session=session, new_item=new_item)
    data = await ProductDAL.get_one(session=session, id=new_data.id)
    return await calc_missing(data)


@router.delete("/delete_item", response_model=s.ProductListOut)
async def remove_product_list_element(
    id: int,
    session=Depends(get_async_session),
    user: User = Depends(current_active_verified_user),
) -> ProductList:
    data = await ProductDAL.delete(session=session, delete_id=id)
    return await calc_missing(data)


@router.patch("/update_item", response_model=s.ProductListOut)
async def update_product_list_element(
    id: int,
    new_data: ProductList,
    session=Depends(get_async_session),
    user: User = Depends(current_active_verified_user),
) -> ProductList:
    data = await ProductDAL.update(session=session, update_id=id, new_item=new_data)
    print(data)
    return await calc_missing(data)
