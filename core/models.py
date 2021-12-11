from pydantic import BaseModel


class AuthInfo(BaseModel):
    login: str
    password_hash: str


class Dish(BaseModel):
    title: str
    description: str
    recipe: str
    dish_photo_path: str


class RestaurantAddress(BaseModel):
    city: str
    street: str
    building: int
    dishes: [Dish]


class RestaurantInfo(BaseModel):
    title: str
    address: RestaurantAddress
    information: str
    restaurant_photo_path: str


class TablesConfiguration(BaseModel):
    tables_plan_photo_path: str
    maximum_tables: int


class Claim(BaseModel):
    claim_id: int
    timestamp: int
    user_prefers: [str]


class CurrentClaims:
    claims: [Claim]


class Restaurant(BaseModel):
    auth_info: AuthInfo
    restaurant_info: RestaurantInfo
