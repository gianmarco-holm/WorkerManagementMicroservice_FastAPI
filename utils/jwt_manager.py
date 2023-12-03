from jwt import encode, decode

def create_token(data: dict) -> str:
    # Recibe la data para generar el token junto con el key y con el algoritmo escogido
    token: str = encode(payload=data, key="holm", algorithm="HS256")
    return token

def validate_token(token: str) -> dict:
    data: dict = decode(token, key="holm", algorithms=['HS256'])
    return data