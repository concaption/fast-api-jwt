"""
path: app/core/security.py

"""

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    """
    Get password hash
    """
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    """
    Verify password
    """
    return pwd_context.verify(plain_password, hashed_password)
