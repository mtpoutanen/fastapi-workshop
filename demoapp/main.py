from fastapi import FastAPI, Path, Query, Depends
from typing import Annotated, Any
from pydantic import BaseModel, AfterValidator, Field

app = FastAPI()


class BaseDto(BaseModel):
    """
    Base data transfer objects model.
    Should be used as a base model for all others dto models
    """


class ItemByIdRequest(BaseDto):
    item_id: str


class ItemQuery(BaseDto):
    q: str = Field(Query(max_length=5, description="Query string, scan item values for a partial match"))


class Item(BaseDto):
    value: str


fake_db: dict[str, Item] = {"foo": Item(value="foo value"), "bar": Item(value="bar value")}


@app.get("/")
def root() -> dict[str, str]:
    return {"Hello": "World"}


@app.get("/items/get_by_id")
def item_by_id(request: ItemByIdRequest = Depends()) -> Item:
    """
    Get item by id
    """
    return fake_db[request.item_id]


@app.get("/items")
def items(request: ItemQuery = Depends()) -> dict[str, Item]:
    """
    Get all items
    """
    if request:
        return {item_id: item for item_id, item in fake_db.items() if request.q in item.value}
    return fake_db
