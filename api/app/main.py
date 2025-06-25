"""
@Author: Abhishek Amar
@Date: 2025-06-25
@Description: Main entry point for the FastAPI application.

"""
import uvicorn
from fastapi import FastAPI 
from app.routes.router import app_router
app = FastAPI()
app.include_router(app_router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1",port=8000,reload=True)