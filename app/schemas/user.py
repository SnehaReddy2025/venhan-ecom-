from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    username: str
    email: str  
    password: str

class UserResponse(BaseModel):
    id: str
    username: str
    email: str
    createdAt: datetime
    updatedAt: datetime

class Token(BaseModel):
    access_token: str
    token_type: str
