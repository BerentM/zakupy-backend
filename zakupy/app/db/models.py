from typing import Any, Dict, Optional, Type

from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase
from sqlalchemy import UniqueConstraint
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlmodel import Field, SQLModel

Base: DeclarativeMeta = declarative_base()
# Join metadata of SQLModel and SQLAlchemy Base model
SQLModel.metadata = Base.metadata


class ShoppingList(SQLModel, table=True):
    __tablename__: str = "shopping_list"
    __table_args__ = (UniqueConstraint("product"),)
    id: Optional[int] = Field(
        default=None,
        primary_key=True,
    )
    product: str
    source: str
    category: str
    target_amount: int
    current_amount: Optional[int] = 0

    class Config:
        @staticmethod
        def schema_extra(schema: Dict[str, Any], model: Type["ShoppingList"]) -> None:
            del schema.get("properties")["id"]


class User(SQLAlchemyBaseUserTableUUID, Base):
    pass
