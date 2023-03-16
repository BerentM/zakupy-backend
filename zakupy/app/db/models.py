from typing import Any, Dict, Optional, Type

from fastapi_users.db import (SQLAlchemyBaseUserTableUUID,
                              SQLAlchemyUserDatabase)
from sqlalchemy import UniqueConstraint
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlmodel import Field, Relationship, SQLModel

Base: DeclarativeMeta = declarative_base()
# Join metadata of SQLModel and SQLAlchemy Base model
SQLModel.metadata = Base.metadata


class ProductList(SQLModel, table=True):
    __tablename__: str = "product_list"
    __table_args__ = (UniqueConstraint("product"),)
    id: Optional[int] = Field(
        default=None,
        primary_key=True,
    )
    product: str
    target_amount: int
    current_amount: Optional[int] = 0

    source_id: Optional[int] = Field(default=None, foreign_key="sources.id")
    source: Optional["Source"] = Relationship(
        back_populates="product_list",
        sa_relationship_kwargs=dict(lazy="selectin"),
    )
    category_id: Optional[int] = Field(default=None, foreign_key="categories.id")
    category: Optional["Category"] = Relationship(
        back_populates="product_list",
        sa_relationship_kwargs=dict(lazy="selectin"),
    )

    class Config:
        @staticmethod
        def schema_extra(schema: Dict[str, Any], model: Type["ProductList"]) -> None:
            del schema.get("properties")["id"]


class Source(SQLModel, table=True):
    __tablename__: str = "sources"
    __table_args__ = (UniqueConstraint("name"),)
    id: Optional[int] = Field(
        default=None,
        primary_key=True,
    )
    name: str

    product_list: list[ProductList] = Relationship(back_populates="source")


class Category(SQLModel, table=True):
    __tablename__: str = "categories"
    __table_args__ = (UniqueConstraint("name"),)
    id: Optional[int] = Field(
        default=None,
        primary_key=True,
    )
    name: str

    product_list: list[ProductList] = Relationship(back_populates="category")


class User(SQLAlchemyBaseUserTableUUID, Base):
    pass
