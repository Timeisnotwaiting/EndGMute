from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
import os

URL = os.getenv("MONGO_DB_URL", None)

if not URL:
    URL = "mongodb+srv://alpha:<password>@cluster0.9wc7qib.mongodb.net/?retryWrites=true&w=majority"

mongo = MongoClient(URL)
db = mongo.EGM

