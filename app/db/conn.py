
from motor.motor_asyncio import AsyncIOMotorClient
import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://snehareddy2025:vScoTf9pcsxkkSsL@cluster0.8h1l2.mongodb.net/")
DB_NAME = os.getenv("DB_NAME", "e-com-task")

client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]  

users_collection = db["users"]
products_collection = db["products"]
orders_collection = db["orders"]

async def init_db():
    print(f"Connected to MongoDB: {DB_NAME}")
