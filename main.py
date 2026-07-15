from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from calc.calc import add

app = FastAPI(
    title="Calculadora API y Presentación",
    description="API de ejemplo con FastAPI usando uv para gestión de dependencias"
)

# Montar la carpeta static para servir la presentación y archivos
app.mount("/static", StaticFiles(directory="static"), name="static")

class AddRequest(BaseModel):
    a: float
    b: float

@app.get("/")
def read_root():
    """
    Sirve la página de inicio atractiva que permite descargar
    la presentación (.pptx) y acceder a la API.
    """
    return FileResponse("static/index.html")

@app.post("/api/add")
def api_add(req: AddRequest):
    """
    Suma dos números utilizando la lógica de negocio en calc.ops
    """
    result = add(req.a, req.b)
    return {"a": req.a, "b": req.b, "result": result}