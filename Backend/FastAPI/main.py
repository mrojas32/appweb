from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import crud_user
from database import engine, localSession
from schemas import UsuarioData, UsuarioID, AdministradorID, ReservaID, ReservaData, AdministradorData, CanchasID
from models import Base
from datetime import date

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
        raise HTTPException(status_code=400, detail='User dont exist')

@app.put('/api/update_nom_user/{new_nombre:str , nombre:str}', response_model = str)
def update_nom_user(new_nombre, nombre, db: Session = Depends(get_db)):
    check_name = crud_user.get_user_by_name(db=db, nombre=nombre)
    if check_name:
        return crud_user.update_user_name(db=db, user=check_name,nombre=new_nombre)
    else:
        raise HTTPException(status_code=400, detail='User dont exist')

@app.put('/api/update_nom_user/{new_passwd:str , nombre:str}', response_model = str)
def update_nom_user(new_passwd, nombre, db: Session = Depends(get_db)):
    check_name = crud_user.get_user_by_name(db=db, nombre=nombre)
    if check_name:
        return crud_user.update_user_passwd(db=db, user=check_name, passwd=new_passwd)
    else:
        raise HTTPException(status_code=400, detail='User dont exist')

###########################################
## Canchas

@app.get('/api/canchas', response_model = list[CanchasID])
def get_canchas(db: Session = Depends(get_db)):
    return crud_user.get_cancha(db=db)

@app.get('/api/canchas/{id:int}', response_model=CanchasID)
def get_cancha_by_id(id, db: Session = Depends(get_db)):
    cancha_by_id = crud_user.get_cancha_by_id(db=db, id=id)
    if cancha_by_id:
        return cancha_by_id
    raise HTTPException(status_code=404, detail='Cancha not Found')

@app.get('/api/canchas/{nombre:str}', response_model=CanchasID)
def get_cancha_by_name(nombre, db: Session = Depends(get_db)):
    cancha_by_name = crud_user.get_cancha_by_name(db=db, nombre=nombre)
    if cancha_by_name:
        return cancha_by_name
    raise HTTPException(status_code=404, detail='User not Found')





###########################################
## Reservas

@app.get('/api/reservas', response_model = list[AdministradorID])
def get_reservas(db: Session = Depends(get_db)):
    return crud_user.get_reservas(db=db)

@app.get('/api/reservas/{id:int}', response_model=AdministradorID)
def get_reserva(id, db: Session = Depends(get_db)):
    reservas_by_id = crud_user.get_reservas_by_id(db=db, id=id)
    if reservas_by_id:
        return reservas_by_id
    raise HTTPException(status_code=404, detail='Admin not Found')

@app.get('/api/reservas/{id:int}', response_model=AdministradorID)
def get_reservas_by_id_usuario(id, db: Session = Depends(get_db)):
    reservas_by_id_usuario = crud_user.get_reservas_by_id_usuario(db=db, id=id)
    if reservas_by_id_usuario:
        return reservas_by_id_usuario
    raise HTTPException(status_code=404, detail='Admin not Found')

@app.get('/api/reservas/{id:int}', response_model=AdministradorID)
def  get_reservas_by_cancha(id, db: Session = Depends(get_db)):
    reservas_by_cancha = crud_user.get_reservas_by_cancha(db=db, id=id)
    if reservas_by_cancha:
        return reservas_by_cancha
    raise HTTPException(status_code=404, detail='Admin not Found')

@app.get('/api/reservas/{fecha:date}', response_model=AdministradorID)
def get_reservas_by_date(fecha, db: Session = Depends(get_db)):
    reservas_by_date = crud_user.get_reservas_by_date(db=db, fecha=fecha)
    if reservas_by_date:
        return reservas_by_date
    raise HTTPException(status_code=404, detail='Reserva not Found')

#@app.get('/api/reservas/{fecha:date}', response_model=AdministradorID)
#def get_user_by_date_bloq_ini(fecha, db: Session = Depends(get_db)):
#    reservas_by_date_bloq_ini = crud_user.get_user_by_date_bloq_ini(db=db, fecha=fecha)
#    if reservas_by_date_bloq_ini:
#       return reservas_by_date_bloq_ini
#   raise HTTPException(status_code=404, detail='Reserva not Found')



@app.post('/api/reservas/', response_model=ReservaID)
def create_reserva(reserva: ReservaData, db: Session = Depends(get_db)):
    check_name = crud_user.get_reserva_by_cancha(db=db, id=id)
    if check_name:
        raise HTTPException(status_code=400, detail='Reserva already exits')
    return crud_user.create_reserva(db=db, reserva=reserva)

@app.delete('/api/delete_reserva/{nombre: str}', response_model=ReservaID)
def delete_reserva_by_cancha(nombre, db: Session = Depends(get_db)):
    check_name = crud_user.get_reserva_by_cancha(db=db, id=id)
    if check_name:
        return crud_user.delete_reserva_by_cancha(db=db, admin=check_name)
    else:
        raise HTTPException(status_code=400, detail='Admin dont exist')





###########################################
## Admin

@app.get('/api/admins', response_model = list[AdministradorID])
def get_admins(db: Session = Depends(get_db)):
    return crud_user.get_admins(db=db)

@app.get('/api/admins/{id:int}', response_model=AdministradorID)
def get_admin(id, db: Session = Depends(get_db)):
    admins_by_id = crud_user.get_admins_by_id(db=db, id=id)
    if admins_by_id:
        return admins_by_id
    raise HTTPException(status_code=404, detail='Admin not Found')

@app.get('/api/admins/{nombre:str}', response_model=AdministradorID)
def get_admin_by_name(nombre, db: Session = Depends(get_db)):
    admin_by_name = crud_user.get_admin_by_name(db=db, nombre=nombre)
    if admin_by_name:
        return admin_by_name
    raise HTTPException(status_code=404, detail='Admin not Found')

@app.post('/api/admins/', response_model=AdministradorID)
def create_admin(admin: AdministradorData, db: Session = Depends(get_db)):
    check_name = crud_user.get_admin_by_name(db=db, nombre=admin.nombre)
    if check_name:
        raise HTTPException(status_code=400, detail='Admin already exits')
    return crud_user.create_admin(db=db, admin=admin)

@app.delete('/api/delete_admin/{nombre: str}', response_model=AdministradorID)
def delete_admin(nombre, db: Session = Depends(get_db)):
    check_name = crud_user.get_admin_by_name(db=db, nombre=nombre)
    if check_name:
        return crud_user.delete_admin_by_name(db=db, admin=check_name)
    else:
        raise HTTPException(status_code=400, detail='Admin dont exist')

@app.put('/api/update_nom_admin/{new_nombre:str , nombre:str}', response_model = str)
def update_nom_user(new_nombre, nombre, db: Session = Depends(get_db)):
    check_name = crud_user.get_admin_by_name(db=db, nombre=nombre)
    if check_name:
        return crud_user.update_admin_name(db=db, user=check_name,nombre=new_nombre)
    else:
        raise HTTPException(status_code=400, detail='Admin dont exist')

@app.put('/api/update_nom_admin/{new_passwd:str , nombre:str}', response_model = str)
def update_nom_admin(new_passwd, nombre, db: Session = Depends(get_db)):
    check_name = crud_user.get_admin_by_name(db=db, nombre=nombre)
    if check_name:
        return crud_user.update_admin_passwd(db=db, admin=check_name, passwd=new_passwd)
    else:
        raise HTTPException(status_code=400, detail='Admin dont exist')
