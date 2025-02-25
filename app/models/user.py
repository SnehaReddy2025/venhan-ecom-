from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    id: str
    username: str
    email: str
    hashed_password: str
    createdAt: datetime
    updatedAt: datetime