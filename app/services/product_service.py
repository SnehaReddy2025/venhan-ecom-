from app.schemas.product import ProductCreate, ProductResponse
from app.db.conn import db
from typing import List, Optional
from datetime import datetime
from bson import ObjectId
from pymongo import ASCENDING, DESCENDING

products_collection = db["products"]

async def create_product(product: ProductCreate) -> ProductResponse:
    new_product = product.dict()
    new_product["createdAt"] = datetime.utcnow()
    new_product["updatedAt"] = datetime.utcnow()
    
    await products_collection.insert_one(new_product)
    return ProductResponse(id=new_product["_id"], **product.dict(), createdAt=new_product["createdAt"], updatedAt=new_product["updatedAt"])

async def get_all_products(
    name: Optional[str] = None,
    category: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    in_stock: Optional[str] = None,
    sort_by: Optional[str] = "createdAt",
    order: Optional[str] = "desc"
) -> List[ProductResponse]:
    query = {}
    if name:
        query["name"] = {"$regex": name, "$options": "i"} 
    if category:
        query["category"] = category
    if min_price is not None or max_price is not None:
        query["salePrice"] = {}
        if min_price is not None:
            query["salePrice"]["$gte"] = min_price
        if max_price is not None:
            query["salePrice"]["$lte"] = max_price
    if in_stock is not None:
        query["stock"] = {"$gt": 0} if in_stock == '1' else {"$lte": 0}
        print(query)
    order_direction = ASCENDING if order == "asc" else DESCENDING
    sort_fields = {
        "price": "salePrice",
        "stock": "stock",
        "createdAt": "createdAt"
    }
    sort_field = sort_fields.get(sort_by, "createdAt")
    products = await products_collection.find(query).sort(sort_field, order_direction).to_list(None)
    return [ProductResponse(id=str(prod["_id"]), **prod) for prod in products]

async def get_product_by_id(product_id: str) -> Optional[ProductResponse]:
    product = await products_collection.find_one({"_id": ObjectId(product_id)})
    if product:
        return ProductResponse(id=str(product["_id"]), **product)
    return None
async def update_product(product_id: str, product_data: ProductCreate) -> Optional[ProductResponse]:
    updated_data = {**product_data.dict(), "updatedAt": datetime.utcnow()}
    result = await products_collection.find_one_and_update(
        {"_id": ObjectId(product_id)}, {"$set": updated_data}, return_document=True
    )
    if result:
        return ProductResponse(id=str(result["_id"]), **result)
    return None
async def delete_product(product_id: str) -> bool:
    result = await products_collection.delete_one({"_id": product_id})
    return result.deleted_count > 0
