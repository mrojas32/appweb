from sqlalchemy.orm import Session

from models import Usuario
from schemas import UsuarioData

def get_users(db: Session):
    return db.query(Usuario).all()

def get_user_by_id(db: Session, id :int):
    return db.query(Usuario).filter(Usuario.ID_usuario == id).first()

def get_user_by_name(db: Session, nombre :str):
    return db.query(Usuario).filter(Usuario.nombre == nombre).first()

def create_user(db: Session, user: UsuarioData):
    new_user = Usuario(nombre = user.nombre, passwd = user.passwd)
    db.add(new_user)
    db.commit()
    db.flush(new_user)
    return new_user