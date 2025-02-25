from fastapi import APIRouter, HTTPException, status
from datetime import timedelta
from app.schemas.user import UserCreate, UserLogin, Token
from app.services.auth_service import authenticate_user, create_access_token
from app.core.security import ACCESS_TOKEN_EXPIRE_MINUTES
from app.auth.jwt_handler import sign_jwt

router = APIRouter()

@router.post("/signup", response_model=Token)
async def signup(user: UserCreate):
    user_in_db = await authenticate_user(user.email, user.password, signup=True)
    if not user_in_db:
        raise HTTPException(status_code=400, detail="User already exists")
    
    user_id = str(user_in_db["_id"]) 
    print(user_id)
    access_token = sign_jwt(user_id)    
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/login", response_model=Token)
async def login(user: UserLogin):
    user_in_db = await authenticate_user(email=user.email, password=user.password, signup=False)
    if not user_in_db:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    user_id = str(user_in_db["_id"]) 
    print(user_id)
    access_token = sign_jwt(user_id)
    return {"access_token": access_token, "token_type": "bearer"}
