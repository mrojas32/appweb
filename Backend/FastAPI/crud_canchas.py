from sqlalchemy.orm import Session
from sqlalchemy import select, delete, update
from datetime import date

from models import Usuario, Canchas, Reserva
from schemas import UsuarioData, CanchaData, ReservaData, UsuarioID, CanchaID

def get_reserva_by_user(db: Session, ID_usuario :int):
    return db.query(Reserva).filter(Usuario.ID_usuario == ID_usuario).first()

def create_reserva(db: Session, user: UsuarioData, reserva: ReservaData, id_user: UsuarioID, id_cancha: CanchaID):
    new_reserva = Reserva(fecha = reserva.fecha, bloq_ini = reserva.bloq_ini, bloq_final = reserva.bloq_final, ID_usuario = id_user, ID_canchas = id_cancha)
    db.add(new_reserva)
    db.commit()
    db.flush(new_reserva)
    return new_reserva


def delete_reserva(db: Session, reserva: Reserva):
    db.delete(reserva)
    db.commit()
    db.flush()
    return reserva

def update_reserva(db: Session, user: Usuario, nombre:str, reserva: Reserva, fecha:date):
    db.execute(update(Reserva).where(Reserva.ID_usuario == user.ID_usuario).values(fecha = fecha))
    db.commit()
    db.flush()
    return "Cambio realizado"