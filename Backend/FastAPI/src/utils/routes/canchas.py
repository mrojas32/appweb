from fastapi import APIRouter, HTTPException, status


router = APIRouter(
    prefix='/canchas',
    tags=['Canchas'],
    responses={404: {"description": "Not found"}},
    dependencies=[]
)


@router.get('')
def test():
    return {'message': 'hello world'}
