from pydantic import BaseModel
from datetime import datetime
from typing import List, Dict

class Order(BaseModel):
    id: str
    items: List[Dict[str, int]]  
    userId: str
    orderStatus: str
    orderNumber: str
    refunded: bool
    status: str
    createdAt: datetime
    updatedAt: datetime