from pydantic import BaseModel
from datetime import datetime

#Definicion de los modelos de estado
class TransactionIn(BaseModel): #La clase hereda de BaseModel, cuando igresa solo necesito username y value
    username: str
    value: int

class TransactionOut(BaseModel):    #La clase hereda de basemodel y necesito mas componentes que en TransactionIn
    id_transaction: int
    username: str
    date: datetime
    value: int
    actual_balance: int