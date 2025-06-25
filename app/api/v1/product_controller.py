"""
@Author: Abhishek Amar
@Date: 2025-06-25
@Description: This module defines the product-related API endpoints for the FastAPI application
"""
from fastapi import APIRouter 
from dotenv import load_dotenv
from app.schemas.pojo import AddProductRequest
load_dotenv()

product_router = APIRouter()

@product_router.post("/save")
async def save_product(product: AddProductRequest):
    pass

@product_router.get("/find-by-id/{product_id}")
async def find_product_by_id(product_id:int):
    pass