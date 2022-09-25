from . import db

flooddb = db.flood

async def get_flood(chat_id: int):
    get = await flooddb.find_one({"chat_id"})
    if not get:
        return 0
    return get["value"]

async def set_flood(chat_id: int, flood: int):
    try:
        await flooddb.delete_one({"chat_id": chat_id})
    except:
        pass
    return await flooddb.update_one({"chat_id": chat_id}, {"$set": {"value": flood}}, upsert=True)


    
        
