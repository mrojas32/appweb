from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import date

import crud_user, crud_canchas
from database import engine, localSession
from schemas import UsuarioData, UsuarioID, ReservaData, CanchaID
from models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = localSession()
    try:
        yield db
    finally:
        db.close()

@app.get('/')
def root():
    return 'Hola mundo'

@app.get('/api/users', response_model = list[UsuarioID])
def get_users(db: Session = Depends(get_db)):
    return crud_user.get_users(db=db)

@app.get('/api/users/{id:int}', response_model=UsuarioID)
def get_user(id, db: Session = Depends(get_db)):
    user_by_id = crud_user.get_user_by_id(db=db, id=id)
    if user_by_id:
        return user_by_id
    raise HTTPException(status_code=404, detail='User not Found')

@app.get('/api/users/{nombre:str}', response_model=UsuarioID)
def get_user_by_name(nombre, db: Session = Depends(get_db)):
    user_by_name = crud_user.get_user_by_name(db=db, nombre=nombre)
    if user_by_name:
        return user_by_name
    raise HTTPException(status_code=404, detail='User not Found')

#

@app.post('/api/users/', response_model=UsuarioID)
def create_user(user: UsuarioData, db: Session = Depends(get_db)):
    check_name = crud_user.get_user_by_name(db=db, nombre=user.nombre)
    if check_name:
        raise HTTPException(status_code=400, detail='User already exits')
    return crud_user.create_user(db=db, user=user)

@app.delete('/api/delete_user/{nombre: str}', response_model=UsuarioID)
def delete_user(nombre, db: Session = Depends(get_db)):
    check_name = crud_user.get_user_by_name(db=db, nombre=nombre)
    if check_name:
        return crud_user.delete_user_by_name(db=db, user=check_name)
    else:
        raise HTTPException(status_code=400, detail='User doesnt exist')

@app.put('/api/update_nom_user/{new_nombre:str , nombre:str}', response_model = str)
def update_nom_user(new_nombre, nombre, db: Session = Depends(get_db)):
    check_name = crud_user.get_user_by_name(db=db, nombre=nombre)
    if check_name:
        return crud_user.update_user_name(db=db, user=check_name,nombre=new_nombre)
    else:
        raise HTTPException(status_code=400, detail='User doesnt exist')

@app.put('/api/update_nom_user/{new_passwd:str , nombre:str}', response_model = str)
def update_nom_user(new_passwd, nombre, db: Session = Depends(get_db)):
    check_name = crud_user.get_user_by_name(db=db, nombre=nombre)
    if check_name:
        return crud_user.update_user_passwd(db=db, user=check_name, passwd=new_passwd)
    else:
        raise HTTPException(status_code=400, detail='User doesnt exist')

#


@app.post('/api/canchas/', response_model=UsuarioID)
def create_reserva(ID_usuario: UsuarioID,ID_canchas: CanchaID, user: UsuarioData,reserva: ReservaData, db: Session = Depends(get_db)):
    check_reserva = crud_canchas.get_reserva_by_user(db=db, ID_usuario=ID_usuario)
    if check_reserva:
        raise HTTPException(status_code=400, detail='No hay reservas')
    return crud_canchas.create_reserva(db=db, user=user, reserva=reserva, id_user=ID_usuario, id_cancha=ID_canchas)


@app.get('/api/canchas/{ID_usuario:int}', response_model=UsuarioID)
def get_reserva_by_user(ID_usuario, db: Session = Depends(get_db)):
    reserva_by_user = crud_canchas.get_reserva_by_user(db=db, ID_usuario=ID_usuario)
    if reserva_by_user:
        return reserva_by_user
    raise HTTPException(status_code=404, detail='No hay reservas')

@app.delete('/api/delete_reserva/{ID_usuario: int}', response_model=UsuarioID)
def delete_reserva(ID_usuario, db: Session = Depends(get_db)):
    check_reserva = crud_canchas.get_reserva_by_user(db=db, ID_usuario=ID_usuario)
    if check_reserva:
        return crud_canchas.delete_reserva(db=db, UsuarioID=check_reserva)
    else:
        raise HTTPException(status_code=400, detail='Reserva doesnt exist')
    
@app.put('/api/update_reserva/{new_date:date , nombre:str}', response_model = str)
def update_reserva(new_date, nombre, db: Session = Depends(get_db)):
    check_reserva = crud_canchas.get_reserva_by_user(db=db, nombre=nombre)
    if check_reserva:
        return crud_canchas.update_reserva(db=db, user=check_reserva,date=new_date)
    else:
        raise HTTPException(status_code=400, detail='Reserva doesnt exist')