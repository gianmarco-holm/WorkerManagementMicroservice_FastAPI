from sqlalchemy import Column, Integer, String, DateTime, Float, func, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base

class MarcacionModel(Base):
    __tablename__ = 'marcaciones'

    idMarcacion = Column(Integer, primary_key=True, autoincrement=True)
    idEmpleado = Column(Integer, ForeignKey('empleados.idEmpleado'), nullable=False)
    fecha = Column(DateTime, nullable=False)
    horaEntrada = Column(DateTime, nullable=False)
    horaSalida = Column(DateTime, nullable=True)
    latitud = Column(Float, nullable=True)
    longitud = Column(Float, nullable=True)

    # Relación de uno a muchos con la tabla EmpleadoModel
    empleado = relationship('EmpleadoModel', backref='marcaciones_backref')
