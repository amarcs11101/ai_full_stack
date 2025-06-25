"""
@Author: Abhishek Amar
@Date: 2025-06-25
@Description: This module defines the main router for the FastAPI application, including the product operations
"""

from fastapi import  APIRouter
from app.api.v1.product_controller import product_router
from app.api.v1.devices_controller import devices_router
from app.api.v1.module_controller import module_router
from app.api.v1.authentication_controller import authentication_router

app_router = APIRouter()

# Including routers for different functionalities
# Each router is prefixed with a version and a specific path for better organization and versioning

app_router.include_router(product_router,prefix="/api/v1/product", tags=["PRODUCT OPERATIONS"])
app_router.include_router(devices_router, prefix="/api/v1/devices",tags=["DEVICE CONTROLLER"])
app_router.include_router(module_router, prefix="/api/v1/module", tags=["MODULE CONTROLLER"] )
app_router.include_router(authentication_router, prefix="/api/v1/auth", tags=["AUTHENTICATION CONTROLLER"])

 