from fastapi import FastAPI, Depends

from demoapp.routes import auth, items

app = FastAPI()


@app.get("/")
def root() -> dict[str, str]:
    return {"Hello": "World"}


app.include_router(items.router)
app.include_router(auth.router)
