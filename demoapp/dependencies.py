from fastapi import HTTPException

from demoapp.models import Item

_fake_db: dict[str, Item] = {"foo": Item(value="foo value"), "bar": Item(value="bar value")}


def get_database() -> dict[str, Item]:
    """
    Get fake database
    """
    print("Connect to database")
    yield _fake_db
    print("Disconnect from database")


async def get_query_token(token: str):
    if token != "demo-token":
        raise HTTPException(status_code=401, detail="Not authenticated")
    print("Token is valid")
