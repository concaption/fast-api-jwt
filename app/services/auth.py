"""
path: app/services/auth.py
"""

from datetime import datetime, timedelta
from fastapi.exceptions import HTTPException

from app.models.user import UserModel
from app.core.security import verify_password, create_access_token, create_refresh_token
from app.core.config import settings
from app.schemas.token import Token
from app.core.security import decode_token

async def authenticate_user(db, email: str, password: str):
    """
    Authenticate user
    """
    user = db.query(UserModel).filter(UserModel.email == email).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found")

    # if not user.is_active:
    #     raise HTTPException(
    #         status_code=400,
    #         detail="User is not active")
    print("password", password)

    if not verify_password(password, user.password):
        raise HTTPException(
            status_code=400,
            detail="Incorrect password")
    return user

async def get_access_token(user: UserModel, refresh_token = None):
    """
    Get access token
    """
    access_token = await create_access_token(
        data={"sub": user.email},
        expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    if not refresh_token:
        refresh_token = await create_refresh_token({"sub": user.email})
    return Token(
        access_token=access_token,
        refresh_token=refresh_token,
        token_type="bearer",
        expires_in=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60
    )

async def get_refresh_token(refresh_token: str, db):
    """
    Get refresh token
    """
    try:
        payload = await decode_token(refresh_token)
        email: str = payload.get("sub")
        if email is None:
            raise HTTPException(
                status_code=400,
                detail="Invalid token")
        user = db.query(UserModel).filter(UserModel.email == email).first()
        if user is None:
            raise HTTPException(
                status_code=404,
                detail="User not found")
        return await get_access_token(user, refresh_token)
    except:
        raise HTTPException(
            status_code=400,
            detail="Invalid token")
