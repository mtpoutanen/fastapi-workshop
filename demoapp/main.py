from fastapi import FastAPI, Depends

from demoapp.dependencies import Item, get_database
from demoapp.models import ItemByIdRequest, ItemQuery

app = FastAPI()


@app.get("/")
def root() -> dict[str, str]:
    return {"Hello": "World"}


@app.get("/items/get_by_id")
def item_by_id(request: ItemByIdRequest = Depends(), fake_db: dict[str, Item] = Depends(get_database)) -> Item:
    """
    Get item by id
    """
    return fake_db[request.item_id]


@app.get("/items")
def items(request: ItemQuery = Depends(), fake_db: dict[str, Item] = Depends(get_database)) -> list[Item]:
    """
    Get all items
    """
    print("Returning items")
    if request.q:
        return list(filter(lambda x: request.q in x.value, fake_db.values()))
    return list(fake_db.values())
