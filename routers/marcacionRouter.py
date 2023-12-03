from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from models.marcacionModel import MarcacionModel
from services.marcacionService import MarcacionService
from schemas.marcacionSchema import MarcacionSchema

marcacion_router = APIRouter()


@marcacion_router.get('/marcaciones', tags=['Marcaciones'], response_model=List[MarcacionSchema], status_code=200, dependencies=[Depends(JWTBearer())])
def get_marcaciones() -> List[MarcacionSchema]:
    db = Session()
    result = MarcacionService(db).get_marcaciones()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@marcacion_router.get('/marcaciones/{idMarcacion}', tags=['Marcaciones'], response_model=MarcacionSchema)
def get_marcacion(idMarcacion: int = Path(ge=1, le=2000)) -> MarcacionSchema:
    db = Session()
    result = MarcacionService(db).get_marcacion(idMarcacion)
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@marcacion_router.post('/marcaciones', tags=['Marcaciones'], response_model=dict, status_code=201)
def create_marcacion(marcacion: MarcacionSchema) -> dict:
    db = Session()
    MarcacionService(db).crear_marcacion(marcacion)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado la marcación"})


@marcacion_router.put('/marcaciones/{idMarcacion}', tags=['Marcaciones'], response_model=dict, status_code=200)
def update_marcacion(idMarcacion: int, marcacion: MarcacionSchema)-> dict:
    db = Session()
    result: MarcacionModel = db.query(MarcacionModel).filter(MarcacionModel.idMarcacion == idMarcacion).first()
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})

    MarcacionService(db).actualizar_marcacion(idMarcacion, marcacion)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado la marcación"})


@marcacion_router.delete('/marcaciones/{idMarcacion}', tags=['Marcaciones'], response_model=dict, status_code=200)
def delete_marcacion(idMarcacion: int)-> dict:
    db = Session()
    result: MarcacionModel = db.query(MarcacionModel).filter(MarcacionModel.idMarcacion == idMarcacion).first()
    if not result:
        return JSONResponse(status_code=404, content={"message": "No se encontró"})

    MarcacionService(db).eliminar_marcacion(idMarcacion)
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado la marcación"})
