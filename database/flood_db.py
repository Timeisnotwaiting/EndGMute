from . import BASE, SESSION
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import BigInteger
import threading

class Flood(BASE):
    __tablename__ = "flood"

    value = Column(BigInteger, primary_key=True)
    chat_id = Column(BigInteger, primary_key=True)

    def __init__(self, value, chat_id):
        self.value = value
        self.chat_id = chat_id

Flood.__table__.create(checkfirst=True)

def get_flood(chat_id):
    get = SESSION.query(Flood).all()
    if not get:
        return None
    FLOOD_VALUE = []
    for x in get:
        FLOOD_VALUE.append((x.chat_id, x.value))
    a = -1
    for l in FLOOD_VALUE:
        a += 1
        if l == chat_id:
            return FLOOD_VALUE[a+1]
    

def set_flood(chat_id, value):
    get = SESSION.query(Flood).all()
    if get:
        SESSION.delete(get)
        SESSION.commit()
    chat_id = int(chat_id)
    value = int(value)
    SESSION.add(Flood(chat_id, value))
    SESSION.commit()
    return
    
