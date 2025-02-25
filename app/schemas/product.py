from pydantic import BaseModel
from datetime import datetime

class ProductCreate(BaseModel):
    name: str
    description: str
    image: str
    stock: int
    mrp: float
    salePrice: float
    status: str

class ProductResponse(ProductCreate):
    createdAt: datetime
    updatedAt: datetime
