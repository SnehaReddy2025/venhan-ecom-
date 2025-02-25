from pydantic import BaseModel
from datetime import datetime
from typing import List, Dict, Any, Optional
class OrderCreate(BaseModel):
    items: List[Dict[str, Any]]
    userId: str
    orderStatus: str
    orderNumber: str
    refunded: bool
    status: str

class OrderResponse(OrderCreate):
    id: str
    createdAt: datetime
    updatedAt: datetime

class OrderUpdate(BaseModel):
    items: Optional[List[Dict[str, Any]]] = None
    orderStatus: Optional[str] = None
    refunded: Optional[bool] = None
    status: Optional[str] = None
