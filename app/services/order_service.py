from app.schemas.order import OrderCreate, OrderResponse, OrderUpdate
from app.db.conn import orders_collection  
from typing import List, Optional
from fastapi import HTTPException
from datetime import datetime
from bson import ObjectId
from pymongo import ReturnDocument

async def create_order(order: OrderCreate) -> OrderResponse:
    new_order = order.dict()
    new_order["_id"] = (ObjectId())  
    new_order["createdAt"] = datetime.utcnow()
    new_order["updatedAt"] = datetime.utcnow()

    result = await orders_collection.insert_one(new_order)  
    
    return OrderResponse(
        id=str(result.inserted_id),
        **order.dict(),
        createdAt=new_order["createdAt"],
        updatedAt=new_order["updatedAt"]
    )
async def get_orders() -> List[OrderResponse]:
    orders = await orders_collection.find().to_list(100)  
    return [
        OrderResponse(
            id=str(order["_id"]),
            items=order["items"],
            userId=order["userId"],
            orderStatus=order["orderStatus"],
            orderNumber=order["orderNumber"],
            refunded=order["refunded"],
            status=order["status"],
            createdAt=order["createdAt"],
            updatedAt=order["updatedAt"]
        )
        for order in orders
    ]
async def get_order_by_id(order_id: str) -> Optional[OrderResponse]:
    try:
        order = await orders_collection.find_one({"_id": ObjectId(order_id)})  
        if not order:
            return None  
        return OrderResponse(
            id=str(order["_id"]),  
            items=order["items"],
            userId=order["userId"],
            orderStatus=order["orderStatus"],
            orderNumber=order["orderNumber"],
            refunded=order["refunded"],
            status=order["status"],
            createdAt=order["createdAt"],
            updatedAt=order["updatedAt"]
        )
    except Exception as e:
        return None
    
    
async def update_order(order_id: str, update_data: OrderUpdate):
    if not ObjectId.is_valid(order_id):
        raise HTTPException(status_code=400, detail="Invalid order ID format")
    order_obj_id = ObjectId(order_id)
    existing_order = await orders_collection.find_one({"_id": order_obj_id})
    if not existing_order:
        raise HTTPException(status_code=404, detail="Order not found")
    update_dict = update_data.dict(exclude_unset=True)
    if not update_dict:
        raise HTTPException(status_code=400, detail="No fields provided for update")
    update_dict["updatedAt"] = datetime.utcnow()
    updated_order = await orders_collection.find_one_and_update(
        {"_id": order_obj_id},
        {"$set": update_dict},
        return_document=ReturnDocument.AFTER  
    )
    if not updated_order:
        raise HTTPException(status_code=404, detail="Order not found after update")
    updated_order["id"] = str(updated_order["_id"])
    del updated_order["_id"]

    return updated_order


