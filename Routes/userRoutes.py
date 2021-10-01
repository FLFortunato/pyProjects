
from fastapi import APIRouter
from json import *
from Controllers.usersController import getUserById, getUsers, createUser
from pydantic import BaseModel

class User(BaseModel):
    name:str
    email:str
    password:str

router = APIRouter()



@router.post('/user')
async def create(data: User):
    return await createUser(data)

@router.get('/user')
async def get():
    try:
        return await getUsers()
    except:
        return "Error"


@router.get('/user/{id}')
async def getByID(id:str):
    try:
        return await getUserById(id)
    except:    
        return "Errro"