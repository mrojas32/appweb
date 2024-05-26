from pydantic import BaseModel
from datetime import date

class UsuarioData(BaseModel):
    nombre: str
    passwd: str
    estudiante: bool
    correo: str

class UsuarioID(UsuarioData):
    ID_usuario: int

#

class CanchaData(BaseModel):
    nombre: str
    tipo: str
    ubicacion: str

class CanchaID(CanchaData):
    ID_canchas: int


class ReservaData(BaseModel):
    fecha: date
    bloq_ini: str
    bloq_final: str
    ID_usuario: int
    ID_canchas: int

class ReservaID(CanchaData):
    ID_reserva: int