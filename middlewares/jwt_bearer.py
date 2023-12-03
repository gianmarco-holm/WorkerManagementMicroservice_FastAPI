from fastapi import HTTPException  # Importar la clase HTTPException para manejar errores
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer  # Importar las clases de seguridad necesarias
from starlette.requests import Request  # Importar la clase Request para acceder a los detalles de la solicitud
from utils.jwt_manager import validate_token  # Importar la función validate_token para validar los tokens JWT

class JWTBearer(HTTPBearer):  # Crear una clase HTTPBearer personalizada llamada JWTBearer
    async def __call__(self, request: Request) -> HTTPAuthorizationCredentials | None:  # Override the __call__ method to handle token validation
        auth = await super().__call__(request)  # Llamar al método __call__ original de HTTPBearer para extraer las credenciales de autorización
        data = validate_token(auth.credentials)  # Validar el token JWT extraído
        if data['correo'] != "admin@gmail.com":  # Comprobar si el correo electrónico del token validado no es "admin@gmail.com"
            raise HTTPException(status_code=403, detail="Credencial inválida")  # Lanzar una excepción HTTP con código de estado 403 (Prohibido) y un mensaje que indica credenciales inválidas
