from typing import Optional, Dict, List
from pydantic import BaseModel, Field


# Schema meal filters
class Filters(BaseModel):
    servings: int
    calories: Optional[str] = None
    methods: Optional[str] = None
    time: Optional[str] = None


# Schema getting meal
class RecipeSchema(BaseModel):
    ingredients: List[str]
    filters: Filters
    cuisine: List[str]
    measurement: str
