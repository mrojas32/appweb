from pydantic import BaseModel

from datetime import date

#date_object = datetime.fromisoformat('2024-10-27')

class UsuarioData(BaseModel):
    nombre: str
    passwd: str
    estudiante: bool
    correo: str

class UsuarioID(UsuarioData):
    ID_usuario: int


class AdministradorData(BaseModel):
    nombre: str
    passwd: str

class AdministradorID(AdministradorData):
    ID_admin: int


class ReservaData(BaseModel):
    fecha: date
    bloq: str
    ID_usuario: int
    ID_canchas: int

class ReservaPost(BaseModel):
    fecha: str
    bloq: str
    ID_usuario: int
    ID_canchas: int

class ReservaID(ReservaData):
    ID_reserva : int

class CanchasData(BaseModel):
    nombre: str
    tipo: str
    ubicacion: str

class CanchasID(CanchasData):
    ID_canchas : int
