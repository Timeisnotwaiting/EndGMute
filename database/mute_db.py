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

def mute_user(id):
    muted = SESSION.query(Mute).get(id)
    if muted:
        return SESSION.close()
    with threading.RLock():
        SESSION.add(Mute(id))
        return SESSION.commit()

def unmute_user(id):
    muted = SESSION.query(Mute).get(id)
    if not muted:
        return SESSION.close()
    with threading.RLock():
        SESSION.delete(muted)
        return SESSION.commit()

def is_muted(id):
    muted = SESSION.query(Mute).get(id)
    if muted:
        return True
    return False

def get_muted():
    all = SESSION.query(Mute).all()
    if not all:
        return []
    Hehe = []
    for x in all:
        Hehe.append(x.id)
    return Hehe


    
