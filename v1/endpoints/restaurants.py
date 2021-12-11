from fastapi import APIRouter

restaurant_router = APIRouter()


@restaurant_router.get("/restaurant_info")
def restaurant_info():
    return [
        {
            "title": "test_title",
            "address": {
                "city": "test_city",
                "street": "test_street",
                "building": 10
            },
            "information": "test_information"
        }
    ]


@restaurant_router.get("/dishes_list")
def dishes_list():
    return [
        {
            "title": "dish_title1",
            "description": "description1",
            "recipe": "recipe1",
            "photo_path": "path_to_photo1"
        },
        {
            "title": "dish_title2",
            "description": "description2",
            "recipe": "recipe2",
            "photo_path": "path_to_photo2"
        },
    ]


@restaurant_router.get("/tables_configuration")
def tables_configuration():
    return {
        "table_plan_photo": "photo_to_plan",
        "restaurant_photo": "photo_to_restaurant",
        "maximum_tables": 6
    }


@restaurant_router.get("/claims")
def current_claims():
    return [
        {
            "claim_id": 0,
            "timestamp": 100000,
            "user_prefers": []
        },
        {
            "claim_id": 1,
            "timestamp": 90000,
            "user_prefers": []
        }
    ]