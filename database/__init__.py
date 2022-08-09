from motor.motor_asyncio import AsyncIOMotorClient as MongoClient 
from config import MONGO_DB_URL

mongo = MongoClient(MONGO_DB_URL)

db = mongo.GMUTE
