from pydantic import BaseModel


class UsuarioData(BaseModel):
    nombre: str
    passwd: str
    estudiante: bool
    correo: str

class AdministradorData(BaseModel):
    nombre: str
    passwd: str

class ReservaData(BaseModel):
    fecha: str
    bloq_ini: str
    bloq_final: str
    ID_usuario: int
    ID_canchas: int

class CanchasData(BaseModel):
    nombre: str
    tipo: str
    ubicacion: str

class AdministradorID(AdministradorData):
    ID_admin: int

class UsuarioID(UsuarioData):
    ID_usuario: int

class ReservaID(ReservaData):
    ID_reserva : int

class CanchasID(CanchasData):
    c : int
