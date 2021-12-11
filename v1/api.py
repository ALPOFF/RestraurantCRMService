from fastapi import FastAPI
from v1.endpoints.restaurants import restaurant_router
from v1.endpoints.auth import auth_router

prefix = "/api/v1"


def get_api_v1():
    app = FastAPI()
    app.include_router(prefix=prefix, router=restaurant_router)
    app.include_router(prefix=prefix, router=auth_router)
    return app
