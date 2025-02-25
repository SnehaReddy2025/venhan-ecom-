from fastapi import Request, HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.auth.jwt_handler import decode_jwt
import os
SECRET_KEY = os.getenv("JWT_SECRET_KEY", "3a492e79fa7efc1db96f9f8f2bb3e5cb6bdfeffd9044f7aa119d1dd4698dd8d0")

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super().__call__(request)
        if credentials:
            token = credentials.credentials
            payload = decode_jwt(token)
            if payload is None:
                raise HTTPException(status_code=403, detail="Invalid token or expired token")
            return payload
        raise HTTPException(status_code=403, detail="Invalid authorization")
