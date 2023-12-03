
# DOCUMENTACIÓN: API Gestion de Trabajadores para Quasar People

Esta api tiene la logica de un servicio que se encarga del registro de nuevos trabajadores y de la marcación de entrada y salidad. 
Este servicio pertenece a una arquitectura SOA mas grande que se relaciona con los procesos de Ejecución de Estrategias de PDV y Recopilación de datos en tiempo real, 
estos procesos pertenecen a la empresa Quasar People, y la implementación de estos servicios es para optimizar y automatizar los procesos antes mencionados.

## Configuración del Entorno de Trabajo

1. **Clonar el Repositorio:**
    ```bash
    git clone https://github.com/gianmarco-holm/API-WorkerManagement-FastAPI.git
    cd tu-proyecto
    ```

2. **Crear y Activar el Entorno Virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Para sistemas basados en Unix
    # o
    .\venv\Scripts\activate  # Para sistemas basados en Windows
    ```

3. **Instalar Dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

## Ejecutar la API

1. **Ejecutar la Aplicación:**
    ```bash
    uvicorn main:app --reload
    ```

## Contribuir
¡Siéntete libre de contribuir al proyecto! Abre un problema o envía una solicitud de extracción.


## Tech Stack

**FastAPI:** El framework base

**Uvicorn:** Framework usado para el servidor

**Starlette:** Libreria para manejar errores en el middleware

**Pydantic:** Libreria para validar datos en esquema

**SQLalchemy:** ORM utilizado para comunicarse con la base de datos

**PyJWT:** Libreria para generar el token del API


