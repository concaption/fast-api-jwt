"""
path: app/core/api/users.py
"""

from fastapi import APIRouter, status, Depends, Request
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.user import UserCreate, UserBase
from app.services.user import create_user_account
from app.core.security import get_current_user, oauth2_scheme

router = APIRouter()
user_router = APIRouter(
    dependencies=[Depends(oauth2_scheme), Depends(get_current_user)]
)

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    """
    Create user endpoint
    """
    await create_user_account(db, user)

    return {"message": "User created successfully"}

@user_router.get("/me", status_code=status.HTTP_200_OK, response_model=UserBase)
async def get_user_me(request: Request):
    """
    Get user me endpoint
    """
    return request.user
