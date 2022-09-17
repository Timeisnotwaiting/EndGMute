from . import BASE, SESSION
from .mute_db import Column, BigInteger, threading

class Sudo(BASE):
    __tablename__ = "sudo"

    id = Column(BigInteger, primary_key=True)

    def __init__(self, id):
        self.id = id

Sudo.__table__.create(checkfirst=True)





    
