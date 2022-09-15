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
    muted_list = mutedb.find({"a": {"$gt": 0}})
    if not muted_list:
        return []
    LIST = []
    for _ in await muted_list.to_list(length=1000000000):
        LIST.append(_["a"])
    return LIST
    
