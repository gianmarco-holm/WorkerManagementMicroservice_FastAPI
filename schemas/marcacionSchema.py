from pydantic import BaseModel, Field
from datetime import datetime, date
from typing import Optional

class MarcacionSchema(BaseModel):
    # los 3 puntos significa que este campo es requerido
    idMarcacion: Optional[int] = Field(None, description="ID de la marcación (opcional)")
    idEmpleado: int = Field(..., description="ID del empleado que hizo la marcación")
    fecha: date = Field(..., description="Fecha de la marcación")
    horaEntrada: datetime = Field(..., description="Hora de entrada de la marcación")
    horaSalida: Optional[datetime] = Field(None, description="Hora de salida de la marcación (opcional)")
    latitud: Optional[float] = Field(None, description="Latitud de la marcación (opcional)")
    longitud: Optional[float] = Field(None, description="Longitud de la marcación (opcional)")

    class Config:
        title = "Esquema de Marcación"
        description = "Modelo para representar una marcación"
        json_schema_extra = {
            "examples": [
                {
                    "idEmpleado": 1,
                    "fecha": "2023-08-02",
                    "horaEntrada": "2023-08-02T08:00:00",
                    "horaSalida": None,
                    "latitud": 12.546545,
                    "longitud": -77.321657
                }
            ]
        }
