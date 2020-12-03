from db.user_db import UserInDB #Importar la clase
from db.user_db import update_user, get_user    #Importar las funciones

from db.transaction_db import TransactionInDB
from db.transaction_db import save_transaction

from models.user_models import UserIn, UserOut
from models.transaction_models import TransactionIn,TransactionOut

import datetime #Para trabajar con fecha y hora
from fastapi import FastAPI #Asi le digo que voy a crear una Apirest
from fastapi import HTTPException
api = FastAPI()

@api.post("/user/auth/")    #Decorador post y en parentesis la url
async def auth_user(user_in: UserIn):   #Async es que a penas llegue la peticion la pone a correr ... como un hilo ... puede hacer varias solicitudes al tiempo
    user_in_db = get_user(user_in.username)
    if user_in_db == None:  #No encontro el usuario en la db
        raise HTTPException(status_code=404, 
                            detail="El usuario no existe")
    if user_in_db.password != user_in.password: #Si la clave en la bd es diferente al que ingreso el usuario no se puede autenticar
        return {"Autenticado": False}
    return {"Autenticado": True}    #Si las claves son iguales se deja autenticar

@api.get("/user/balance/{username}")
async def get_balance(username: str):
    user_in_db = get_user(username)
    if user_in_db == None:
        raise HTTPException(status_code=404,
                            detail="El usuario no existe")
    user_out = UserOut(**user_in_db.dict()) #El ** es para mapear para que filtre solo los campos que necesita userout del listado que tiene el diccionario de userin
    return user_out

@api.put("/user/transaction/")
async def make_transaction(transaction_in: TransactionIn):
    user_in_db = get_user(transaction_in.username)
    if user_in_db == None:
        raise HTTPException(status_code=404,
                            detail="El usuario no existe")
    if user_in_db.balance < transaction_in.value:
        raise HTTPException(status_code=400,
                            detail="Sin fondos suficientes")
    user_in_db.balance = user_in_db.balance - transaction_in.value
    update_user(user_in_db)
    transaction_in_db = TransactionInDB(**transaction_in.dict(),
                                        actual_balance = user_in_db.balance)
    transaction_in_db = save_transaction(transaction_in_db)
    transaction_out = TransactionOut(**transaction_in_db.dict())
    return transaction_out