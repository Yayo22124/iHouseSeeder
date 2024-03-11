from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes.homework_routes import homework_router

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


app.include_router(homework_router)
