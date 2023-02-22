from typing import Optional

from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlmodel import Field, SQLModel

Base: DeclarativeMeta = declarative_base()
# Join metadata of SQLModel and SQLAlchemy Base model
SQLModel.metadata = Base.metadata


class ShoppingList(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    product: str
    source: str
    category: str
    target_amount: int
    current_amount: Optional[int] = 0


class User(SQLAlchemyBaseUserTableUUID, Base):
    pass
