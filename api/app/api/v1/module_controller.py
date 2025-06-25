"""
Module Controller for handling module-related operations, 
Using this we can give access of a module to a specific role or a user and also assign then some of the modules
with read , write or delete permissions.
"""

from fastapi import APIRouter 

module_router = APIRouter()

@module_router.get("/find-all/{module_id}")
async def find_details_by_module(module_id:str):
    pass

@module_router.get("/find-by-role/{role_id}")
async def find_details_by_role(role_id:str):
    pass

