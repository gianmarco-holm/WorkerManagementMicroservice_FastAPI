from pydantic import BaseModel, EmailStr, Field
from datetime import datetime, date
from typing import Optional

class EmpleadoSchema(BaseModel):
    # los 3 puntos significa que este campo es requerido
    idEmpleado: Optional[int] = Field(None, description="ID del empleado (opcional)")
    nombre: str = Field(..., description="Nombre del empleado")
    apellidoPaterno: str = Field(..., description="Apellido paterno del empleado")
    apellidoMaterno: str = Field(..., description="Apellido materno del empleado")
    dni: str = Field(..., min_length=8, max_length=8, description="DNI del empleado (8 caracteres)")
    correo: EmailStr = Field(..., description="Correo electrónico del empleado")
    telefono: Optional[str] = Field(None, pattern=r'^\d{9}$', description="Número de teléfono del empleado (opcional, 9 dígitos)")
    direccion: Optional[str] = Field(None, max_length=100, description="Dirección del empleado (opcional, hasta 100 caracteres)")
    cargo: str = Field(..., description="Cargo del empleado")
    estado: str = Field(..., description="Estado del empleado")
    fechaNacimiento: Optional[date] = Field(None, description="Fecha de nacimiento del empleado (sin hora)")
    sexo: Optional[str] = Field(None, description="Sexo del empleado")
    created_at: Optional[datetime] = Field(None, description="Fecha de creación del empleado")

    class Config:
        title = "Esquema de Empleado"
        description = "Modelo para representar un empleado"
        json_schema_extra = {
            "examples": [
                {
                    "nombre": "Marco",
                    "apellidoPaterno": "holgado",
                    "apellidoMaterno": "Vargas",
                    "dni": "47089367",
                    "correo": "marco@gmail.com",
                    "telefono": "935123456",
                    "direccion": "Av grau 115 - Ate",
                    "cargo": "Mercaderista",
                    "estado": "activo",
                    "fechaNacimiento": "1992-08-18",
                    "sexo": "masculino"
                }
            ]
        }
