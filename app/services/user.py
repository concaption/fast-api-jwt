"""
path: app/services/user.py
"""

from datetime import datetime
from fastapi.exceptions import HTTPException
from app.core.security import get_password_hash
from app.models.user import UserModel


async def create_user_account(db, data):
    """
    Create user service
    """
    user = db.query(UserModel).filter(UserModel.email == data.email).first()
    if user:
        raise HTTPException(status_code=409, detail="Email already registered")
    new_user = UserModel(
        first_name=data.first_name,
        last_name=data.last_name,
        email=data.email,
        password=get_password_hash(data.password),
        is_active=False,
        is_verified=False,
        registered_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
