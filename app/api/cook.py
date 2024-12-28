from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder

from app import chatgpt
from app.api import fake_ingredients
from app.schemas.cook import RecipeSchema

router = APIRouter()


@router.post("/cook/image")
def cook_image():
    # Create the new user record
    # response = chatgpt.ask_chatgpt(
    #     prompt='give me random list of 5 fruits, 10 vegetabes, 3 meet, 6 diaries, 5 seasoning and 2 oil in json format'
    # )
    # print(json.loads(response))
    return fake_ingredients


@router.post("/cook/recipes")
def get_meals(recipe: RecipeSchema):
    json_compatible_item_data = jsonable_encoder(recipe)
    response = chatgpt.ask_chatgpt(
        prompt=f'2 recipe with: short description of exact 3 sentences, list of ingredients with measures and '
               f'detail preparation in 5 steps, ingredients: {json_compatible_item_data}. In json format'
    )
    print(response)
    return response
