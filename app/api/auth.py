"""
path: app/api/auth.py

"""

from fastapi import APIRouter, status, Depends, Header
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services import auth as auth_service

router = APIRouter()

@router.post("/login/access-token", status_code=status.HTTP_200_OK)
async def login(
    db: Session = Depends(get_db),
    form_data: OAuth2PasswordRequestForm = Depends()
):
    """
    Login endpoint
    """
    user = await auth_service.authenticate_user(
        db, form_data.username, form_data.password
    )

    if not user:
        return {"error": "Invalid credentials"}

    return await auth_service.get_access_token(user)

@router.post("/login/refresh-token", status_code=status.HTTP_200_OK)
async def refresh_token(
    refresh_token: str = Header(),
    db: Session = Depends(get_db),
):
    """
    Refresh token endpoint
    """
    return await auth_service.get_refresh_token(refresh_token, db)
