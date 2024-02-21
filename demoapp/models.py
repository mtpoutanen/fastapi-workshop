from fastapi import Query
from pydantic import BaseModel, Field


class BaseDto(BaseModel):
    """
    Base data transfer objects model.
    Should be used as a base model for all others dto models
    """


class ItemByIdRequest(BaseDto):
    item_id: str


class ItemQuery(BaseDto):
    q: str | None = Field(Query(default="", max_length=5, description="Query string, scan item values for a partial match"))


class Item(BaseDto):
    value: str
