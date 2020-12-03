from datetime import datetime
from pydantic import BaseModel

#Definicion de TransactionInDB
class TransactionInDB(BaseModel):   #Extiende del Basemodel de Pydantic
    id_transaction: int = 0 #Se definen los atributos con su tipo de dato y su valor por defecto
    username: str
    date: datetime = datetime.now() #Se utiliza fecha y hora
    value: int
    actual_balance: int

#Definicion de la base de datos ficticia para las trx
database_transactions = []  #Lista vacia
generator = {"id":0}    #Diccionario que arranca con el ID 0

def save_transaction(transaction_in_db: TransactionInDB):   #Funcion que guarda la trx en la base de datos ficticia y es de tipo transactionInDB
    generator["id"] = generator["id"] + 1   #ID en el que vamos y lo guardamos en el diccionario de generator
    transaction_in_db.id_transaction = generator["id"]  #En transactionInDB se le pone en el Id_transaction, el ID que acabe de ver en el generator
    database_transactions.append(transaction_in_db)
    return transaction_in_db