from sqlalchemy.orm import Session

from sqlalchemy import delete, update, and_

from models import *
from schemas import *

def get_users(db: Session):
    return db.query(Usuario).all()

def get_user_by_id(db: Session, id :int):
    return db.query(Usuario).filter(Usuario.ID_usuario == id).first()

def get_user_by_name(db: Session, nombre :str):
    return db.query(Usuario).filter(Usuario.nombre == nombre).first()

def create_user(db: Session, user: UsuarioData):
    new_user = Usuario(nombre = user.nombre, passwd = user.passwd, correo = user.correo, estudiante = user.estudiante)
    db.add(new_user)
    db.commit()
    db.flush(new_user)
    return new_user

def get_user_by_name_passwd(db: Session, nombre :str, passwd: str):
    return db.query(Usuario).filter( and_(Usuario.nombre == nombre, Usuario.passwd == passwd)).first()

def delete_user_by_name(db: Session, user: Usuario):
    db.delete(user)
    db.commit()
    db.flush()
    return user

def update_user_name(db: Session, user: Usuario, nombre:str):
    db.execute(update(Usuario).where(Usuario.ID_usuario == user.ID_usuario).values(nombre = nombre))
    db.commit()
    db.flush()
    return "Cambio realizado"

def update_user_passwd(db: Session, user: Usuario, passwd:str):
    db.execute(update(Usuario).where(Usuario.ID_usuario == user.ID_usuario).values(passwd = passwd))
    db.commit()
    db.flush()
    return "Cambio realizado"



##################################################################################################
##Canchas Solamente leer (canchas estaticas => no creamos, no actualizamos ni borramos canchas)
def get_cancha(db: Session):                                         #ok
    return db.query(Canchas).all()

def get_cancha_by_id(db: Session, id :int):
    return db.query(Canchas).filter(Canchas.ID_canchas == id).first()  

def get_cancha_by_name(db: Session, nombre :str):
    return db.query(Canchas).filter(Canchas.nombre == nombre).first()


#def get_cancha_by_type_ubication(db: Session, tipo :str, ubicacion: str):
#   return db.query(Canchas).filter(Canchas.tipo == tipo and Canchas.ubicacion == ubicacion).first()



##################################################################################################
##Reserva(s) / Como queremos buscar las reservas? ID reserva, fecha, fecha+bloque, usuario, cancha

def get_reservas(db: Session):                            #ok
    return db.query(Reserva).all()

def get_reservas_by_id_usuario(db: Session, id :int):
    return db.query(Reserva).filter(Reserva.ID_usuario == id).first()              #ok
 
def get_reservas_by_cancha(db: Session, id :int):
    return db.query(Reserva).filter(Reserva.ID_canchas == id).first()             #ok

def get_reservas_by_id(db: Session, id :int):
    return db.query(Reserva).filter(Reserva.ID_reserva == id).first()                #ok

def get_reservas_by_date(db: Session, fecha :str):                                #ok
    return db.query(Reserva).filter(Reserva.fecha == fecha).first()

#def get_user_by_date_bloq(db: Session, fecha :str, bloq: str):                                   #
#    return db.query(Reserva).filter(and_(Reserva.fecha == fecha, Reserva.bloq == bloq) ).first()



def create_reserva(db: Session, reserva: ReservaPost):
    new_reseva = Reserva(fecha = date.fromisoformat(reserva.fecha) , bloq = reserva.bloq, ID_usuario=reserva.ID_usuario, ID_canchas = reserva.ID_canchas)
    db.add(new_reseva)
    db.commit()
    db.flush(new_reseva)
    return new_reseva


def delete_reserva(db: Session, reserva: Reserva):
    db.delete(reserva)
    db.commit()
    db.flush()
    return reserva


##################################################################################################
##Admins

def get_admins(db: Session):
    return db.query(Administrador).all()

def get_admins_by_id(db: Session, id :int):
    return db.query(Administrador).filter(Administrador.ID_admin == id).first()

def get_admin_by_name(db: Session, nombre :str):
    return db.query(Administrador).filter(Administrador.nombre == nombre).first()

def create_admin(db: Session, admin: AdministradorData):
    new_admin = Administrador(nombre = admin.nombre, passwd = admin.passwd)
    db.add(new_admin)
    db.commit()
    db.flush(new_admin)
    return new_admin

def get_admin_by_name_passwd(db: Session, nombre :str, passwd: str):
    return db.query(Administrador).filter(Administrador.nombre == nombre and Administrador.passwd == passwd).first()

def delete_admin_by_name(db: Session, admin: Administrador):
    db.delete(admin)
    db.commit()
    db.flush()
    return admin

def update_admin_name(db: Session, admin: Administrador, nombre:str):
    db.execute(update(Administrador).where(Administrador.ID_admin == admin.ID_admin).values(nombre = nombre))
    db.commit()
    db.flush()
    return "Cambio realizado"


def update_admin_passwd(db: Session, admin: Administrador, passwd:str):
    db.execute(update(Administrador).where(Administrador.ID_admin == admin.ID_admin).values(passwd = passwd))
    db.commit()
    db.flush()
    return "Cambio realizado"
