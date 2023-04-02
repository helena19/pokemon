from fastapi import FastAPI

from pokemon import api

def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(api.router)
    return app

app = create_app()
