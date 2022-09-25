from . import db

fmdb = db.fm

async def get_flood_mode(chat_id: int):
    get = await fmdb.find_one({"chat_id"})
    if not get:
        return 0
    return get["value"]

async def set_flood_mode(chat_id: int, mode: int):
    try:
        await fmdb.delete_one({"chat_id": chat_id})
    except:
        pass
    return await fmdb.update_one({"chat_id": chat_id}, {"$set": {"value": mode}}, upsert=True)
