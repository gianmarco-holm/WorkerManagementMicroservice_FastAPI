from pydantic import BaseModel, EmailStr, constr

class ApiCredencialesSchema(BaseModel):
    correo:EmailStr
    contrasenia:constr(min_length=4)