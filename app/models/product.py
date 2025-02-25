from pydantic import BaseModel, Field
from datetime import datetime
from bson import ObjectId

class Product(BaseModel):
    id: str = Field(default_factory=lambda: str(ObjectId()), alias="_id")
    name: str
    description: str
    image: str
    stock: int
    mrp: float
    salePrice: float
    status: str
    createdAt: datetime = Field(default_factory=datetime.utcnow)
    updatedAt: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        populate_by_name = True  
        from_attributes = True  
