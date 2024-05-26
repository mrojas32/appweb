from sqlalchemy.orm import Session

from sqlalchemy import delete, update

from models import Usuario
from schemas import UsuarioData, UsuarioID

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
    return db.query(Usuario).filter(Usuario.nombre == nombre and Usuario.passwd == passwd).first()

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
