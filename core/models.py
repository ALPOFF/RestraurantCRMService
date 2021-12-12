from pydantic import BaseModel
from typing import List


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


class TablesConfiguration(BaseModel):
    tables_plan_photo_path: str
    current_tables: int
    maximum_tables: int


class Claim(BaseModel):
    table_number: int
    timestamp: int


class RestaurantInfo(BaseModel):
    title: str
    address: RestaurantAddress
    information: str
    restaurant_photo_path: str
    dishes: List[Dish]
    tables_configuration: TablesConfiguration
    current_claims: List[Claim]


class Restaurant(BaseModel):
    auth_info: AuthInfo
    restaurant_info: RestaurantInfo
