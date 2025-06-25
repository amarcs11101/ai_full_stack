from fastapi import APIRouter 

authentication_router = APIRouter()

@authentication_router.post("/generate-token")
async def generate_token(username:str,password:str):
    pass

