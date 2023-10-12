"""
path: app/schemas/users.py
"""

from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    """
    User base schema
    """
    first_name: str
    last_name: str
    email: EmailStr

class UserCreate(UserBase):
    """
    User create schema
    """
    password: str
