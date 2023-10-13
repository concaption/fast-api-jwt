"""
path: app/schemas/token.py
"""

from pydantic import BaseModel

class Token(BaseModel):
    """
    Token schema
    """
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    expires_in: int
