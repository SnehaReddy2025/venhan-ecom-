from fastapi import APIRouter, HTTPException, Depends, Query
from app.schemas.product import ProductCreate, ProductResponse
from app.services.product_service import (
    create_product,
    get_all_products,
    get_product_by_id,
    update_product,
    delete_product
)
from typing import List, Optional
from app.auth.auth_bearer import JWTBearer  # Auth middleware

router = APIRouter()

@router.post("/", response_model=ProductResponse, dependencies=[Depends(JWTBearer())])
async def add_product(product: ProductCreate):
    return await create_product(product)

@router.get("/", response_model=List[ProductResponse])
async def list_products(
    name: Optional[str] = Query(None, description="Search by product name"),
    category: Optional[str] = Query(None, description="Filter by category"),
    min_price: Optional[float] = Query(None, description="Minimum price filter"),
    max_price: Optional[float] = Query(None, description="Maximum price filter"),
    in_stock: Optional[str] = Query(None, description="Filter by stock availability"),
    sort_by: Optional[str] = Query("createdAt", description="Sort by field (price, stock, createdAt)"),
    order: Optional[str] = Query("desc", description="Sort order (asc, desc)")
):
    return await get_all_products(
        name=name,
        category=category,
        min_price=min_price,
        max_price=max_price,
        in_stock=in_stock,
        sort_by=sort_by,
        order=order
    )

@router.get("/{product_id}", response_model=ProductResponse)
async def get_product(product_id: str):
    product = await get_product_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.put("/{product_id}", response_model=ProductResponse, dependencies=[Depends(JWTBearer())])
async def edit_product(product_id: str, product: ProductCreate):
    updated_product = await update_product(product_id, product)
    if not updated_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated_product

@router.delete("/{product_id}", dependencies=[Depends(JWTBearer())])
async def remove_product(product_id: str):
    deleted = await delete_product(product_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted successfully"}
