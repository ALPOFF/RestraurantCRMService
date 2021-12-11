from fastapi import APIRouter
from core.auth_engine import AuthEngine
from core.models import *
from database.crud import create_restaurant

auth_router = APIRouter()
auth_engine = AuthEngine()


@auth_router.post("/register")
def register_restaurant(restaurant_description: Restaurant):
    # At this moment we hardcode this route
    default_restaurant = {
        {
            "auth_info": {
                "login": "Alex",
                "password": auth_engine.hash_password("password_hash")
            },
            "restaurant_info": {
                "title": "Monday",
                "address": {
                    "city": "Moscow",
                    "street": "Moscow",
                    "building": 21
                },
                "information": "This is pretty place. You are welcome!",
                "restaurant_photo": "https://elitetraveler.com/wp-content/uploads/2021/06/photo-RESTAURANT-PIERRE"
                                    "-GAGNAIRE-par-Cyril-Carrere-23-RS-730x450.jpg",
                "dishes": [
                    {
                        "title": "Khinkali",
                        "description": "Хинка́ли (груз. ხინკალი) — блюдо грузинской кухни из горных областей Пшави,"
                                       "Мтиулети и Хевсурети в Грузии, получившее распространение в других районах "
                                       "Кавказа и по всему бывшему СССР.",
                        "recipe": "Начинка для хинкали готовится из говядины/телятины или свинины (частый вариант — "
                                  "говядина со свининой), реже — баранины или ягненка.",
                        "photo": "https://www.gastronom.ru/binfiles/images/20161118/b8ff63ec.jpg"
                    }
                ],
                "tables_configuration": {
                    "tables_plan_photo": "https://i.pinimg.com/originals/40/50/8f/40508fd7ede54ae72e3ce6d3ea08a20a.jpg",
                    "maximum_tables": 20
                },
                "current_claims": [
                    {
                        "claim_id": 0,
                        "timestamp": 1639213200,
                        "user_prefers": []
                    },
                    {
                        "claim_id": 1,
                        "timestamp": 1639216800,
                        "user_prefers": []
                    }
                ]
            }
        }
    }
    create_restaurant(default_restaurant)