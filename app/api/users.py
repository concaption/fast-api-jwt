"""
path: app/core/api/users.py
"""

from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.user import UserCreate
from app.services.user import create_user_account

router = APIRouter()

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

