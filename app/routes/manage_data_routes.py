from fastapi import APIRouter
from ..config.database import db

Bedrooms = db["bedrooms"]
Livingrooms = db["livingrooms"]
Kitchens = db["kitchens"]
Bathrooms = db["bathrooms"]
Garages = db["garages"]

manage_data_router = APIRouter(prefix="/data", tags=["data", "management", "get", "delete"])

@manage_data_router.get("/")
async def getAll() -> dict:
    bedrooms_cursor = Bedrooms.find({})
    bedrooms_list = await bedrooms_cursor.to_list(None)
    return {
        "bedrooms": bedrooms_list
    }
