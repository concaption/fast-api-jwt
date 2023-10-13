"""
path: main.py

"""

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from starlette.middleware.authentication import AuthenticationMiddleware

from app.api import users, auth 
from app.core.database import Base, engine
from app.models.user import UserModel
from app.core.security import JWTAuthentication


app = FastAPI(title="FastAPI JWT Auth", version="0.0.1")

Base.metadata.create_all(bind=engine)

app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
app.include_router(users.user_router, prefix="/api/v1/users", tags=["users"])
app.include_router(auth.router, prefix="/api/v1", tags=["auth"])

# Middleware
app.add_middleware(
    AuthenticationMiddleware,
    backend=JWTAuthentication()
)

@app.get("/")
async def health_check():
    """
    Health check endpoint
    """
    return JSONResponse(status_code=200, content={"message": "OK"})
