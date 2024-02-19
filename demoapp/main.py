from fastapi import FastAPI, Path, Query
from typing import Annotated, Any

app = FastAPI()

fake_db: dict[str, dict[str, Any]] = {"foo": {"value": "foo value"}, "bar": {"value": "bar value"}}


@app.get("/")
def root() -> dict[str, str]:
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def item_by_id(item_id: Annotated[str, Path(title="Item ID", description="The ID of the item")]) -> dict[str, Any]:
    """
    Get item by id
    """
    return fake_db[item_id]


@app.get("/items")
def items(q: Annotated[str | None, Query(
    title="Query string",
    description="Query string, scan item values for a partial match",
    max_length=5)] = None) -> dict[str, dict[str, Any]]:
    """
    Get all items
    """
    if q:
        return {item_id: item for item_id, item in fake_db.items() if q in item["value"]}
    return fake_db
