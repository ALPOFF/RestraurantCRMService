from database.database import get_database
from typing import Dict
from core.models import *


def create_restaurant(restaurant):
    database = get_database()
    database.insert_one(restaurant)


def get_restaurant_by_login(login: str):
    database = get_database()
    login_filter = {"auth_info.login": login}
    target = database.find_one(filter=login_filter)
    return target


def get_restaurants():
    database = get_database()
    query_iterator = database["Restaurants"].find()
    restaurants = []
    for restaurant in query_iterator:
        restaurants.append(restaurant)
    return restaurants
