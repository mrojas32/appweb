from pydantic import BaseModel

class UsuarioData(BaseModel):
    nombre: str
    passwd: str
    estudiante: bool
    correo: str

class UsuarioID(UsuarioData):
    ID_usuario: int