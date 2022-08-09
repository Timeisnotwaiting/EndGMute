from . import db

mutedb = db.mute

async def mute_user(a: int):
    muted = mutedb.find_one({"a": a})
    if not muted:
        return await mutedb.insert_one({"a": a})
    return 

async def unmute_user(a: int):
    muted = mutedb.find_one({"a": a})
    if muted:
        return await mutedb.delete_one({"a": a})
    return

async def is_muted(a: int):
    muted = mutedb.find_one({"a": a})
    if muted:
        return True
    return False

async def get_muted():
