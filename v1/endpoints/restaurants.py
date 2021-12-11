from fastapi import APIRouter
from fastapi import HTTPException
from database.crud import get_restaurant_by_login
from core.models import AuthInfo

restaurant_router = APIRouter()


# На этапе прототипирования получаем инфу напрямую по логину без авторизации
# и различных веселых секурных штук

@restaurant_router.get("/restaurant_info")
async def restaurant_info(login: str):
    restaurant = get_restaurant_by_login(login=login)
    if not restaurant:
        raise HTTPException(status_code=401, detail="Bad login")
    return restaurant["restaurant_info"]


@restaurant_router.get("/dishes_list")
async def dishes_list(login: str):
    restaurant = get_restaurant_by_login(login=login)
    if not restaurant:
        raise HTTPException(status_code=401, detail="Bad login")
    return restaurant["restaurant_info"]["dishes"]


@restaurant_router.get("/tables_configuration")
async def tables_configuration(login: str):
    restaurant = get_restaurant_by_login(login=login)
    if not restaurant:
        raise HTTPException(status_code=401, detail="Bad login")
    return restaurant["restaurant_info"]["tables_configuration"]


@restaurant_router.get("/claims")
async def current_claims(login: str):
    restaurant = get_restaurant_by_login(login=login)
    if not restaurant:
        raise HTTPException(status_code=401, detail="Bad login")
    return restaurant["restaurant_info"]["current_claims"]
