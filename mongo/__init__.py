from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
import os

URL = os.getenv("MONGO_DB_URL", None)

mongo = MongoClient(URL)
db = mongo.EGM

