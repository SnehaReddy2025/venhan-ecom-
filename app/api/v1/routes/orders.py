from fastapi import APIRouter, HTTPException, Depends
from app.services.order_service import create_order, get_orders, update_order
from app.schemas.order import OrderCreate, OrderResponse, OrderUpdate
from typing import List
from app.services.order_service import get_order_by_id
from bson import ObjectId

router = APIRouter()

@router.post("/", response_model=OrderResponse)
async def place_order(order: OrderCreate):
    return await create_order(order)

@router.get("/", response_model=List[OrderResponse])
async def list_orders():
    return await get_orders()


@router.get("/{order_id}", response_model=OrderResponse)
async def get_order(order_id: str):
    if not ObjectId.is_valid(order_id):
        raise HTTPException(status_code=400, detail="Invalid order ID format")

    order_data = await get_order_by_id(order_id)
    if not order_data:
        raise HTTPException(status_code=404, detail="Order not found")

    return order_data 


@router.put("/{order_id}", response_model=OrderResponse)
async def update_order_api(order_id: str, order_update: OrderUpdate):
    updated_order = await update_order(order_id, order_update)
    return OrderResponse(**updated_order)



