import os
import time
import jwt
from dotenv import load_dotenv
from datetime import datetime, timedelta
from typing import Optional

# Load environment variables
load_dotenv()

SECRET_KEY = os.getenv("JWT_SECRET_KEY", "3a492e79fa7efc1db96f9f8f2bb3e5cb6bdfeffd9044f7aa119d1dd4698dd8d0")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60  # Token expires in 1 hour

def sign_jwt(user_id: str) -> str:
    """Generates a JWT token"""
    expiration = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = {
        "sub": user_id,
        "iat": datetime.utcnow()
    }
    print(SECRET_KEY)
    print('SECRET_KEY')

    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

def decode_jwt(token: str) -> Optional[dict]:
    """Decodes JWT token"""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload  # Contains user_id (sub) and expiration
    except jwt.ExpiredSignatureError:
        return None  # Token expired
    except jwt.InvalidTokenError:
        return None  # Invalid token
