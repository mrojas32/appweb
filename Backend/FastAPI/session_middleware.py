import jwt
from sqlalchemy.orm import Session
from models import Usuario
from database import engine
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from schemas import UserSessionDto

JWT_SECRET = 'jwt secret 123321'

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/auth')


def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
        with Session(engine) as db:
            user_id = payload.get('id')
            user = db.get_one(Usuario, user_id)
            print(f'retrieved user: {user.username}')
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid token'
        )

    return UserSessionDto(
        id=user.id,
        username=user.username
    )


session_middleware = Depends(get_current_user)
