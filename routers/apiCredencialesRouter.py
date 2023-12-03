from fastapi import APIRouter
from fastapi.responses import JSONResponse
from utils.jwt_manager import create_token
from schemas.apiCredencialesSchema import ApiCredencialesSchema

apiCredenciales_router = APIRouter()

@apiCredenciales_router.post('/acceso', tags=['Autenticación'])
def acceso(apiCredencial:ApiCredencialesSchema):
    if apiCredencial.correo == "admin@gmail.com" and apiCredencial.contrasenia == "admin":
        token:str = create_token(apiCredencial.dict())
        return JSONResponse(status_code=200, content=token)