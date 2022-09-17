from . import BASE, SESSION
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import BigInteger
import threading

class Mute(BASE):
    __tablename__ = "mute"

    id = Column(BigInteger, primary_key=True)

    def __init__(self, id):
        self.id = id

Mute.__table__.create(checkfirst=True)


    
    
