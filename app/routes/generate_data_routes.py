from fastapi import APIRouter;
from ..config.database import db;

Bedrooms = db["bedrooms"];
Livingrooms = db["livingrooms"];
Kitchens = db["kitchens"];
Bathrooms = db["bathrooms"];
Garages = db["garages"];

generate_sensor_data_router = APIRouter(prefix="/sensor", tags=["sensors", "fake data", "generate", "random"]);
generate_actuator_data_router = APIRouter(prefix="/actuator", tags=["actuators", "fake data", "generate", "random"]);

@generate_sensor_data_router.get("/")
def generate_sensor_data() :
    return