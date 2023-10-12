"""
path: main.py

"""

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.api import users
from app.core.database import Base, engine
from app.models.user import UserModel

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
@app.get("/")
async def health_check():
    """
    Health check endpoint
    """
    return JSONResponse(status_code=200, content={"message": "OK"})
