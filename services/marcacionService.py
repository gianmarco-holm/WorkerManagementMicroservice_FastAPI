from models.empleadoModel import EmpleadoModel
from models.marcacionModel import MarcacionModel
from schemas.empleadoSchema import EmpleadoSchema
from schemas.marcacionSchema import MarcacionSchema


class MarcacionService():

    def __init__(self, db) -> None:
        self.db = db

    def get_marcaciones(self):
        result = self.db.query(MarcacionModel).all()
        return result

    def get_marcacion(self, id):
        result = self.db.query(MarcacionModel).filter(MarcacionModel.idMarcacion == id).first()
        return result

    def get_marcaciones_por_fecha(self, fecha):
        result = self.db.query(MarcacionModel).filter(MarcacionModel.fecha == fecha).all()
        return result

    def crear_marcacion(self, marcacion: MarcacionSchema):
        nueva_marcacion = MarcacionModel(**marcacion.dict())
        self.db.add(nueva_marcacion)
        self.db.commit()
        return

    def actualizar_marcacion(self, id: int, datos: MarcacionSchema):
        marcacion = self.db.query(MarcacionModel).filter(MarcacionModel.idMarcacion == id).first()
        marcacion.fecha = datos.fecha
        marcacion.horaEntrada = datos.horaEntrada
        marcacion.horaSalida = datos.horaSalida
        marcacion.latitud = datos.latitud
        marcacion.longitud = datos.longitud
        self.db.commit()
        return

    def eliminar_marcacion(self, id: int):
        self.db.query(MarcacionModel).filter(MarcacionModel.idMarcacion == id).delete()
        self.db.commit()
        return