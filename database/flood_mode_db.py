from . import BASE, SESSION
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import BigInteger
import threading

class FloodMode(BASE):
    __tablename__ = "floodmode"

    value = Column(BigInteger, primary_key=True)
    chat_id = Column(BigInteger, primary_key=True)

    def __init__(self, value, chat_id):
        self.value = value
        self.chat_id = chat_id

FloodMode.__table__.create(checkfirst=True)

def get_flood_mode(chat_id):
    get = SESSION.query(FloodMode).all()
    if not get:
        return None
    FLOOD_VALUE = []
    for x in get:
        if x.chat_id == chat_id:
            FLOOD_VALUE.append(x.value)
    return int(FLOOD_VALUE[0])

def set_flood_mode(chat_id, value):
    flood = get_flood(chat_id)
    if flood:
        get = SESSION.query(FloodMode).get((chat_id, flood))
        SESSION.delete(get)
        SESSION.commit()
    chat_id = int(chat_id)
    value = int(value)
    SESSION.add(FloodMode(chat_id, value))
    SESSION.commit()
    return
