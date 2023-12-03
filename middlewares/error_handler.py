"""_summary_
Este middleware captura la excepción que pueda producirse en el cualquier lugar del codigo que maneja una
solicitud response o request y devuelve una respuesta JSON con información sobre el error.
Esto puede ser útil para proporcionar respuestas coherentes en caso de errores y facilitar la depuración.
"""

from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse

# Definición de un middleware para manejar errores
class ErrorHandler(BaseHTTPMiddleware):
    # Constructor del middleware, recibe la aplicación FastAPI como parámetro
    def __init__(self, app: FastAPI) -> None:
        super().__init__(app)

    # Método que se ejecuta cada vez que se procesa una solicitud
    async def dispatch(self, request: Request, call_next) -> Response | JSONResponse:
        try:
            # Intenta ejecutar la lógica de manejo de la solicitud utilizando call_next
            return await call_next(request)
        except Exception as e:
            # En caso de que ocurra una excepción, devuelve una respuesta JSON con un código de estado 500 y el mensaje de error
            return JSONResponse(status_code=500, content={'error': str(e)})
