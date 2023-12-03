from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from config.database import Session, Base, engine
from middlewares.error_handler import ErrorHandler
from routers.empleadoRouter import empleado_router
from routers.marcacionRouter import marcacion_router
from routers.apiCredencialesRouter import apiCredenciales_router

app = FastAPI()
app.title = "Servicio Gestión de Empleados"
app.version = "0.0.1"

templates = Jinja2Templates(directory="templates")

app.add_middleware(ErrorHandler)
app.include_router(empleado_router)
app.include_router(marcacion_router)
app.include_router(apiCredenciales_router)

Base.metadata.create_all(bind=engine)

# @app.get('/', tags=['Home'])
# def home():
#     return HTMLResponse('<h1>API DE GIANMARCO</h1>')

@app.get('/', response_class=HTMLResponse, tags=['Home'])
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})