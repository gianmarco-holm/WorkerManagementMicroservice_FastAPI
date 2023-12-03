from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
from config.database import Base

class EmpleadoModel(Base):
    __tablename__ = 'empleados'

    idEmpleado = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    apellidoPaterno = Column(String(100), nullable=False, name= 'apellido_paterno')
    apellidoMaterno = Column(String(100), nullable=False, name='apellido_materno')
    dni = Column(String(8), nullable=False, unique=True)
    correo = Column(String(100), nullable=False, unique=True)
    telefono = Column(String(9), nullable=True)
    direccion = Column(String(100), nullable=True)
    cargo = Column(String(100), nullable=False)
    estado = Column(String(10), nullable=False, default='activo')
    fechaNacimiento = Column(DateTime, nullable=True, name='fecha_nacimiento')
    sexo = Column(String(1), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relacion de uno a muchos con la tabla MarcacionModel
    marcaciones = relationship('MarcacionModel', backref='empleado_backref', lazy='dynamic')
