
from os import name
from Models.userModel import User_Pydantic, Users
from json import *

async def createUser(data):
    user = await Users.create(name=data.name, password=data.password, email=data.email)
    return user


async def getUsers():
    try:
        print("passou aqui")
        users = await Users.all()
        return users
    except:
        return "Error"


async def getUserById(id: str):
    try:
        user = await Users.get(id=id)
        return user
    except:
        return "Error"


async def updateUser(data:User_Pydantic, id: str):
    
    return


async def deleteUser(id: str):
    return
