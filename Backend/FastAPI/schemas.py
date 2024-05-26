from pydantic import BaseModel

class UsuarioData(BaseModel):
    nombre: str
    passwd: str

class UsuarioID(UsuarioData):
    id: int