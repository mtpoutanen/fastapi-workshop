from fastapi import APIRouter, Depends

from demoapp.dependencies import get_query_token, get_database
from demoapp.models import ItemByIdRequest, ItemQuery, Item

router = APIRouter(prefix="/items", tags=["Items"], dependencies=[Depends(get_query_token)])


@router.get("/get_by_id")
def item_by_id(
        request: ItemByIdRequest = Depends(),
        fake_db: dict[str, Item] = Depends(get_database),
) -> Item:
    """
    Get item by id
    """
    return fake_db[request.item_id]


@router.get("/")
def items(
        request: ItemQuery = Depends(),
        fake_db: dict[str, Item] = Depends(get_database),
) -> list[Item]:
    """
    Get all items
    """
    print("Returning items")
    if request.q:
        return list(filter(lambda x: request.q in x.value, fake_db.values()))
    return list(fake_db.values())
