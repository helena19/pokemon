import api
from fastapi import FastAPI

def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(api.router)
    return app

app = create_app()
