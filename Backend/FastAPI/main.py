from fastapi import FastAPI, Depends, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
import jwt

import crud
from database import engine, localSession
from schemas import *
from models import Base
from session_middleware import session_middleware, JWT_SECRET

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = localSession()
    try:
        yield db
    finally:
        db.close()

@app.get('/')
def root():
    return 'Hola mundo'

@app.get('/api/auth')
def get_session(user=session_middleware):
    return {
        'user': user
    }

@app.post('/api/auth')
def login(
            form_data: OAuth2PasswordRequestForm = Depends(),
            db: Session = Depends(get_db)
        ):
    print('login', form_data.username, form_data.password)
    user = crud.get_user_by_correo(db=db, correo=form_data.username)
    if (not user):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='invalid credentials'
        )
    
    valid_credentials = str(user.passwd) == form_data.password

    if (valid_credentials):
        token = jwt.encode({
            'id': user.ID_usuario,
            'username': user.correo
        }, JWT_SECRET)
        return {
            'access_token': token,
            'token_type': 'bearer'
        }
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='invalid credentials'
        )

@app.get('/api/users', response_model = list[UsuarioID])
def get_users(db: Session = Depends(get_db)):
    return crud.get_users(db=db)

@app.get('/api/users/{id:int}', response_model=UsuarioID)
def get_user(id, db: Session = Depends(get_db)):
    user_by_id = crud.get_user_by_id(db=db, id=id)
    if user_by_id:
        return user_by_id
    raise HTTPException(status_code=404, detail='User not Found')

@app.get('/api/users/{nombre:str}', response_model=UsuarioID)
def get_user_by_name(nombre, db: Session = Depends(get_db)):
    user_by_name = crud.get_user_by_name(db=db, nombre=nombre)
    if user_by_name:
        return user_by_name
    raise HTTPException(status_code=404, detail='User not Found')

@app.post('/api/users/', response_model=UsuarioID)
def create_user(user: UsuarioData, db: Session = Depends(get_db)):
    check_name = crud.get_user_by_name(db=db, nombre=user.nombre)
    if check_name:
        raise HTTPException(status_code=400, detail='User already exits')
    return crud.create_user(db=db, user=user)

@app.delete('/api/delete_user/{nombre: str}', response_model=UsuarioID)
def delete_user(nombre, db: Session = Depends(get_db)):
    check_name = crud.get_user_by_name(db=db, nombre=nombre)
    if check_name:
        return crud.delete_user_by_name(db=db, user=check_name)
    else:
        raise HTTPException(status_code=400, detail='User dont exist')

@app.put('/api/update_nom_user/{new_nombre:str , nombre:str}', response_model = str)
def update_nom_user(new_nombre, nombre, db: Session = Depends(get_db)):
    check_name = crud.get_user_by_name(db=db, nombre=nombre)
    if check_name:
        return crud.update_user_name(db=db, user=check_name,nombre=new_nombre)
    else:
        raise HTTPException(status_code=400, detail='User dont exist')

@app.put('/api/update_psw_user/{new_passwd:str , nombre:str}', response_model = str)
def update_pw_user(new_passwd, nombre, db: Session = Depends(get_db)):
    check_name = crud.get_user_by_name(db=db, nombre=nombre)
    if check_name:
        return crud.update_user_passwd(db=db, user=check_name, passwd=new_passwd)
    else:
        raise HTTPException(status_code=400, detail='User dont exist')







###########################################
## Canchas

@app.get('/api/canchas', response_model = list[CanchasID])
def get_canchas(db: Session = Depends(get_db)):
    return crud.get_cancha(db=db)

@app.get('/api/canchas/{id:int}', response_model=CanchasID)
def get_cancha_by_id(id, db: Session = Depends(get_db)):
    cancha_by_id = crud.get_cancha_by_id(db=db, id=id)
    if cancha_by_id:
        return cancha_by_id
    raise HTTPException(status_code=404, detail='Cancha not Found')

@app.get('/api/canchas/{nombre:str}', response_model=CanchasID)
def get_cancha_by_name(nombre, db: Session = Depends(get_db)):
    cancha_by_name = crud.get_cancha_by_name(db=db, nombre=nombre)
    if cancha_by_name:
        return cancha_by_name
    raise HTTPException(status_code=404, detail='User not Found')








###########################################
## Reservas

@app.get('/api/reservas', response_model = list[ReservaID])
def get_reservas(db: Session = Depends(get_db)):
    return crud.get_reservas(db=db)

@app.get('/api/reservas/{id:int}', response_model=ReservaID)
def get_reserva(id, db: Session = Depends(get_db)):
    reservas_by_id = crud.get_reservas_by_id(db=db, id=id)
    if reservas_by_id:
        return reservas_by_id
    raise HTTPException(status_code=404, detail='Reserva not Found')

@app.get('/api/reservas/{id:int}', response_model=ReservaID)
def get_reservas_by_id_usuario(id, db: Session = Depends(get_db)):
    reservas_by_id_usuario = crud.get_reservas_by_id_usuario(db=db, id=id)
    if reservas_by_id_usuario:
        return reservas_by_id_usuario
    raise HTTPException(status_code=404, detail='Reserva not Found')

@app.get('/api/reservas/{id:int}', response_model=ReservaID)
def  get_reservas_by_cancha(id, db: Session = Depends(get_db)):
    reservas_by_cancha = crud.get_reservas_by_cancha(db=db, id=id)
    if reservas_by_cancha:
        return reservas_by_cancha
    raise HTTPException(status_code=404, detail='Reserva not Found')

@app.get('/api/reservas/{fecha:str}', response_model=ReservaID)
def get_reservas_by_date(fecha, db: Session = Depends(get_db)):
    reservas_by_date = crud.get_reservas_by_date(db=db, fecha=fecha)
    if reservas_by_date:
        return reservas_by_date
    raise HTTPException(status_code=404, detail='Reserva not Found')

#@app.get('/api/reservas/{fecha:str, bloq:str}', response_model=ReservaID)
#def get_user_by_date_bloq(fecha, bloq, db: Session = Depends(get_db)):
#    reservas_by_date_bloq = crud.get_user_by_date_bloq(db=db, fecha=fecha, bloq=bloq)
#    if reservas_by_date_bloq:
#       return reservas_by_date_bloq
#    raise HTTPException(status_code=404, detail='Reserva not Found')



@app.post('/api/reservas/', response_model=ReservaID)
def create_reserva(reserva: ReservaPost, db: Session = Depends(get_db)):
    return crud.create_reserva(db=db, reserva=reserva)

@app.delete('/api/delete_reserva/{ID_reserva:int}', response_model=ReservaID)
def delete_reservas_by_id(ID_reserva, db: Session = Depends(get_db)):
    check_name = crud.get_reservas_by_id(db=db, id=ID_reserva)
    if check_name:
        return crud.delete_reserva(db=db, reserva = check_name)
    else:
        raise HTTPException(status_code=400, detail='Reserva dont exist')





###########################################
## Admin

@app.get('/api/admins', response_model = list[AdministradorID])
def get_admins(db: Session = Depends(get_db)):
    return crud.get_admins(db=db)

@app.get('/api/admins/{id:int}', response_model=AdministradorID)
def get_admin(id, db: Session = Depends(get_db)):
    admins_by_id = crud.get_admins_by_id(db=db, id=id)
    if admins_by_id:
        return admins_by_id
    raise HTTPException(status_code=404, detail='Admin not Found')

@app.get('/api/admins/{nombre:str}', response_model=AdministradorID)
def get_admin_by_name(nombre, db: Session = Depends(get_db)):
    admin_by_name = crud.get_admin_by_name(db=db, nombre=nombre)
    if admin_by_name:
        return admin_by_name
    raise HTTPException(status_code=404, detail='Admin not Found')

@app.post('/api/admins/', response_model=AdministradorID)
def create_admin(admin: AdministradorData, db: Session = Depends(get_db)):
    check_name = crud.get_admin_by_name(db=db, nombre=admin.nombre)
    if check_name:
        raise HTTPException(status_code=400, detail='Admin already exits')
    return crud.create_admin(db=db, admin=admin)

@app.delete('/api/delete_admin/{nombre: str}', response_model=AdministradorID)
def delete_admin(nombre, db: Session = Depends(get_db)):
    check_name = crud.get_admin_by_name(db=db, nombre=nombre)
    if check_name:
        return crud.delete_admin_by_name(db=db, admin=check_name)
    else:
        raise HTTPException(status_code=400, detail='Admin dont exist')

@app.put('/api/update_nom_admin/{new_nombre:str , nombre:str}', response_model = str)
def update_nom_admin(new_nombre, nombre, db: Session = Depends(get_db)):
    check_name = crud.get_admin_by_name(db=db, nombre=nombre)
    if check_name:
        return crud.update_admin_name(db=db, admin=check_name,nombre=new_nombre)
    else:
        raise HTTPException(status_code=400, detail='Admin dont exist')


@app.put('/api/update_pw_admin/{new_passwd:str , nombre:str}', response_model = str)
def update_pw_admin(new_passwd, nombre, db: Session = Depends(get_db)):
    check_name = crud.get_admin_by_name(db=db, nombre=nombre)
    if check_name:
        return crud.update_admin_passwd(db=db, admin=check_name, passwd=new_passwd)
    else:
        raise HTTPException(status_code=400, detail='Admin dont exist')
