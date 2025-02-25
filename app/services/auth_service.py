from datetime import datetime, timedelta
from motor.motor_asyncio import AsyncIOMotorClient
from app.core.security import create_access_token, hash_password, verify_password
from app.db.conn import db

users_collection = db["users"]

async def authenticate_user(email: str, password: str, signup=False):
    """
    - If `signup=True`, register the user.
    - If `signup=False`, check credentials for login.
    """
    existing_user = await users_collection.find_one({"email": email})

    if signup:
        if existing_user:
            return None  
        hashed_password = hash_password(password)
        user_data = {"email": email, "password": hashed_password, "created_at": datetime.utcnow()}
        await users_collection.insert_one(user_data)
        return user_data  

    
    if existing_user and verify_password(password, existing_user["password"]):
        return existing_user 

    return None  