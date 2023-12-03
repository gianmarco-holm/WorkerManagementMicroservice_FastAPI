# Si quisiera conectarme a postgresql de un contenedor, este sería el codigo
from sqlalchemy import create_engine

# Configuración para PostgreSQL
postgres_user = 'myuser'
postgres_password = 'mypassword'
postgres_db = 'mydatabase'
postgres_host = 'my_postgres_container'  # Nombre del contenedor según docker-compose.yml
postgres_port = '5432'

# Creación de la URL de la base de datos para PostgreSQL
database_url = f"postgresql://{postgres_user}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_db}"

# Creación del motor de la base de datos
engine = create_engine(database_url, echo=True)

# Y crearía un archivo docker-compose.yml
# version: '3'

# services:
#   postgres:
#     image: postgres
#     container_name: my_postgres_container
#     environment:
#       POSTGRES_USER: myuser
#       POSTGRES_PASSWORD: mypassword
#       POSTGRES_DB: mydatabase
#     ports:
#       - "5432:5432"

