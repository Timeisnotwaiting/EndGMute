from . import db

sudodb = db.sudo

async def add_sudo(b: int):
    sudo = sudodb.find_one({"b": b})
    if not sudo:
        return await sudodb.insert_one({"b": b})
    return

async def is_sudo(b: int):
    is_sudo = sudodb.find_one({"b": b})
    if is_sudo:
        return True
    return False

async def del_sudo(b: int):
    sudo = sudodb.find_one({"b": b})
    if sudo:
        return await sudodb.delete_one({"b": b})
    return

async def get_sudos():
    sudos = sudodb.find({"b": {"$gt": 0}})
    if not sudos:
        return []
    SUDOS = []
    async for sudo in await sudos.to_list(length=1000000000)
        SUDOS.append(sudo["b"])
    return SUDOS
