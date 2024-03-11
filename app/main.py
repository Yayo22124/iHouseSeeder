from fastapi import FastAPI
from .routes.homeworkRoutes import homework_router

app = FastAPI()

@app.get("/")
def read_root():
    return {"msg": "Hello World"}

app.include_router(homework_router)