from typing import Dict
from pydantic import BaseModel

# Definicion de UsesrInDB
class UserInDB(BaseModel):  #En los parentesis se hace la herencia en python ... userInDB extiende de Basemodel de Pydantic
    username: str   #Aqui estoy definiendo los atributos con su tipo de dato nombre:tipo
    password: str
    balance: int

#Definir la base de datos ficticia
database_users = Dict[str, UserInDB]    #Es un diccionario que tiene un string(llave) y un userInDB(valor)
database_users = {
    "camilo24": UserInDB(**{"username":"camilo24",  #Los ** hacen un mapeo con los atributos que defini arriba en UserInDB
                            "password":"root",
                            "balance":12000}),
    "andres18": UserInDB(**{"username":"andres18",
                            "password":"hola",
                            "balance":34000}),
}

#Definicion de funciones sobre la base de datos ficticia
#Para obtener los datos de usuario cuando me pregunten el username
def get_user(username: str):    #El usuario simplemente me envia el string de username (aqui no estoy diciendo que es el mismo parametro que defini en la clase, asi que puede tener cualquier otro nombre)
    if username in database_users.keys():   #la funcion .keys de los diccionarios es para traer todas las llaves 
        return database_users[username] #Si encuentra el username retorna el valor que esta en el diccionario bajo ese username (username, password y balance)
    else:
        return None #Si no lo encuentra pues no retorna nada

def update_user(user_in_db: UserInDB):  #Recibo un dato de tipo userInDB
    database_users[user_in_db.username] = user_in_db    
    return user_in_db