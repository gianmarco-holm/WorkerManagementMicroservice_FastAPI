from fastapi import APIRouter
from fastapi import Depends, Path
from fastapi.responses import JSONResponse
from typing import Optional, List
from config.database import Session
from models.empleadoModel import EmpleadoModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from services.empleadoService import EmpleadoService
from schemas.empleadoSchema import EmpleadoSchema

empleado_router = APIRouter()


@empleado_router.get('/empleados', tags=['Empleados'], response_model=List[EmpleadoSchema], status_code=200, dependencies=[Depends(JWTBearer())])
def get_empleados() -> List[EmpleadoSchema]:
    db = Session()
    result = EmpleadoService(db).get_empleados()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@empleado_router.get('/empleados/{idEmpleado}', tags=['Empleados'], response_model=EmpleadoSchema)
def get_empleado(idEmpleado: int = Path(ge=1, le=2000)) -> EmpleadoSchema:
    db = Session()
    result = EmpleadoService(db).get_empleado(idEmpleado)
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@empleado_router.get('/empleados/por-cargo/{cargo}', tags=['Empleados'], response_model=List[EmpleadoSchema])
def get_empleados_por_cargo(cargo: str = Path(min_length=5, max_length=15)) -> List[EmpleadoSchema]:
    db = Session()
    result = EmpleadoService(db).get_empleados_por_cargo(cargo)
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@empleado_router.get("/empleados/{idEmpleado}/marcaciones", tags=['Empleados'], response_model=dict)
def get_marcaciones_por_empleado(idEmpleado: int) -> dict:
    db = Session()
    empleado_con_marcaciones = EmpleadoService(db).get_marcaciones_por_empleado(idEmpleado)

    if empleado_con_marcaciones:
        return JSONResponse(content=jsonable_encoder(empleado_con_marcaciones))
    else:
        return JSONResponse(status_code=404, content={"message": "Empleado no encontrado"})


@empleado_router.post('/empleados', tags=['Empleados'], response_model=dict, status_code=201)
def create_empleado(empleado: EmpleadoSchema) -> dict:
    db = Session()
    EmpleadoService(db).crear_empleado(empleado)
    return JSONResponse(status_code=201, content={"message": "Se registro el empleado con exito"})


@empleado_router.put('/empleados/{idEmpleado}', tags=['Empleados'], response_model=dict, status_code=200)
def update_empleado(idEmpleado: int, empleado: EmpleadoSchema)-> dict:
    db = Session()
    result: EmpleadoModel = db.query(EmpleadoModel).filter(EmpleadoModel.idEmpleado == idEmpleado).first()
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})

    EmpleadoService(db).actualizar_empleado(idEmpleado, empleado)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el empleado"})


@empleado_router.delete('/empleados/{idEmpleado}', tags=['Empleados'], response_model=dict, status_code=200)
def delete_empleado(idEmpleado: int)-> dict:
    db = Session()
    result: EmpleadoModel = db.query(EmpleadoModel).filter(EmpleadoModel.idEmpleado == idEmpleado).first()
    if not result:
        return JSONResponse(status_code=404, content={"message": "No se encontró"})

    EmpleadoService(db).eliminar_empleado(idEmpleado)
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el empleado"})
