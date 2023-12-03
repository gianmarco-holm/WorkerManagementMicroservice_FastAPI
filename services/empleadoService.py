from models.empleadoModel import EmpleadoModel
from models.marcacionModel import MarcacionModel
from schemas.empleadoSchema import EmpleadoSchema


class EmpleadoService():

    def __init__(self, db) -> None:
        self.db = db

    def get_empleados(self):
        result = self.db.query(EmpleadoModel).all()
        return result

    def get_empleado(self, id):
        result = self.db.query(EmpleadoModel).filter(EmpleadoModel.idEmpleado == id).first()
        return result

    def get_empleados_por_cargo(self, cargo):
        result = self.db.query(EmpleadoModel).filter(EmpleadoModel.cargo == cargo).all()
        return result

    def get_marcaciones_por_empleado(self, id):
        # Obtener el empleado por su ID
        empleado = self.db.query(EmpleadoModel).filter(EmpleadoModel.idEmpleado == id).first()

        if empleado:
            # Obtener las marcaciones asociadas al empleado
            marcaciones = empleado.marcaciones.all()  # Esto supone que la relación se llama 'marcaciones'

            # Crear un diccionario con la información del empleado y sus marcaciones
            empleado_con_marcaciones = {
                "empleado": empleado,
                "marcaciones": marcaciones
            }

            return empleado_con_marcaciones
        else:
            return None

    def crear_empleado(self, empleado: EmpleadoSchema):
        nuevo_empleado = EmpleadoModel(**empleado.dict())
        self.db.add(nuevo_empleado)
        self.db.commit()
        return

    def actualizar_empleado(self, id: int, datos: EmpleadoSchema):
        empleado = self.db.query(EmpleadoModel).filter(EmpleadoModel.idEmpleado == id).first()
        empleado.nombre = datos.nombre
        empleado.apellidoPaterno = datos.apellidoPaterno
        empleado.apellidoMaterno = datos.apellidoMaterno
        empleado.dni = datos.dni
        empleado.correo = datos.correo
        empleado.telefono = datos.telefono
        empleado.direccion = datos.direccion
        empleado.cargo = datos.cargo
        empleado.estado = datos.estado
        empleado.fechaNacimiento = datos.fechaNacimiento
        empleado.sexo = datos.sexo
        self.db.commit()
        return

    def eliminar_empleado(self, id: int):
        self.db.query(EmpleadoModel).filter(EmpleadoModel.idEmpleado == id).delete()
        self.db.commit()
        return