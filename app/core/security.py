"""
path: app/core/security.py

"""
from datetime import datetime, timedelta
from fastapi import HTTPException, Depends
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from starlette.authentication import AuthCredentials, UnauthenticatedUser
from jose import jwt, JWTError
from app.core.database import get_db
from app.schemas.token import Token
from app.models.user import UserModel
from app.core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/login/access-token")


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

async def create_access_token(data: dict, expires_delta: timedelta = None):
    """
    Create access token
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

async def create_refresh_token(data: dict):
    """
    Create refresh token
    """
    return await create_access_token(data, expires_delta=timedelta(days=7))

async def decode_token(token: str):
    """
    Decode token
    """
    try:
        return jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
    except JWTError:
        return None
    
async def get_current_user(token: str = Depends(oauth2_scheme), db = None):
    """
    Get current user
    """
    payload = await decode_token(token)
    email: str = payload.get("sub")
    if email is None:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    if db is None:
        db = next(get_db())
    user = db.query(UserModel).filter(UserModel.email == email).first()
    print(user)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

class JWTAuthentication():
    """
    JWT Authentication class
    """
    def __init__(self):
        self.realm = "Authentication required"
    
    async def authenticate(self, request):
        """
        Authenticate
        """
        guest = AuthCredentials(["unauthenticated"]), UnauthenticatedUser()
        authorization: str = request.headers.get("Authorization")
        if not authorization:
            return guest
        scheme, token = authorization.split()
        print(token)
        if scheme.lower() != "bearer":
            return guest
        try:
            user = await get_current_user(token)
        except:
            print("failed at geting user")
            return guest
        return AuthCredentials(["authenticated"]), user
