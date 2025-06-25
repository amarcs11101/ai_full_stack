from fastapi import APIRouter
from app.schemas.pojo import AddDeviceRequest
devices_router = APIRouter()


@devices_router.post("/save")
async def save_device_details(request:AddDeviceRequest):
    pass

@devices_router.get("/find-by-id/{device_id}")
async def find_device_details_by_id(device_id:int):
    pass

@devices_router.get("/find-all")
async def find_all_devices_details():
    pass