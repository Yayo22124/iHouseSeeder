from fastapi import FastAPI;
from fastapi.middleware.cors import CORSMiddleware

from app.routes.manage_data_routes import manage_data_router; 
from app.routes.generate_data_routes import generate_actuator_data_router, generate_sensor_data_router;
from .routes.homework_routes import homework_router;
from .config.database import db;

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"msg": "Hello World"}


app.include_router(homework_router);
app.include_router(generate_sensor_data_router);
app.include_router(generate_actuator_data_router);
app.include_router(manage_data_router);
