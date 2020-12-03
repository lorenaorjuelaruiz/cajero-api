from pydantic import BaseModel

#Definicion de los modelos de estado
class UserIn(BaseModel):    #Userin hereda de Basemodel
    username: str
    password: str

class UserOut(BaseModel):   #Userout es cuando el usuario sale de la trx y tambien hereda de BaseModel
    username: str
    balance: int