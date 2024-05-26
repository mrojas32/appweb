from sqlalchemy import Column, String, Integer, Date, ForeignKey

from database import Base

class Usuario(Base):
    __tablename__ = 'Usuario'
    ID_usuario = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), index=True, unique=True)
    passwd = Column(String(255))

class Canchas(Base):
    __tablename__ = 'Canchas'
    ID_canchas = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), index=True, unique=True)
    tipo = Column(String(255))
    ubicacion = Column(String(255))

class Administrador(Base):
    __tablename__ = 'Administrador'
    ID_admin = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), index=True, unique=True)
    passwd = Column(String(255))

class Reserva(Base):
    __tablename__ = 'Reserva'
    ID_reserva = Column(Integer, primary_key=True, index=True)
    fecha = Column(Date)
    bloq_ini = Column(String(10))
    bloq_final = Column(String(10))
    ID_usuario = Column(Integer, ForeignKey("Usuario.ID_usuario"), index=True)
    ID_canchas = Column(Integer, ForeignKey("Canchas.ID_canchas"), index=True)

