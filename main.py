from fastapi import FastAPI

# Crear una instancia de la aplicación FastAPI
app = FastAPI()

# Definir una ruta y su operación asociada
@app.get("/")
def read_root():
    return {"Hello": "World"}

# Definir otra ruta y operación
@app.get("/items/{item_id}")
def read_item(item_id: int, query_param: str = None):
    return {"item_id": item_id, "query_param": query_param}
