from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import crud_user
from database import engine, localSession
from schemas import UsuarioData, UsuarioID
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
