from . import BASE, SESSION
from .mute_db import Column, BigInteger, threading

class Sudo(BASE):
    __tablename__ = "sudo"

    id = Column(BigInteger, primary_key=True)

    def __init__(self, id):
        self.id = id

Sudo.__table__.create(checkfirst=True)

def add_sudo(id):
    sudo = SESSION.query(Sudo).get(id)
    if sudo:
        return SESSION.close()
    with threading.RLock():
        SESSION.add(Sudo(id))
        return SESSION.commit()

def del_sudo(id):
    sudo = SESSION.query(Sudo).get(id)
    if not sudo:
        return SESSION.close()
    with threading.RLock():
        SESSION.delete(sudo)
        return SESSION.commit()

def is_sudo(id):
    sudo = SESSION.query(Sudo).get(id)
    if sudo:
        return True
    return False

def get_sudos():
    sudos = SESSION.query(Sudo).all()
    if not sudos:
        return []
    Lmao = []
    for sudo in sudos:
        Lmao.append(sudo["id"])
    return Lmao


    
