from passlib.context import CryptContext
from jose import jwt, JWTError
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from src.utils.db import get_db
from src.models.user import TaiKhoan
import os

SECRET_KEY = os.getenv("SECRET_KEY", "secret")
ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/auth/login")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict):
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Không xác thực được người dùng",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        role: str = payload.get("role")
        if email is None or role is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    if role == "admin":
        from src.models.admin import Admin  # tránh import vòng lặp
        user = db.query(Admin).filter(Admin.email == email).first()
        if user is None:
            raise credentials_exception
        user.role = "admin"  # gắn thuộc tính role cho object
        return user
    else:
        user = db.query(TaiKhoan).filter(TaiKhoan.email == email).first()
        if user is None:
            raise credentials_exception
        user.role = "user"
        return user

def get_current_admin(user: TaiKhoan = Depends(get_current_user)):
    if user.role != "admin":
        raise HTTPException(status_code=403, detail="Không có quyền quản trị")
    return user 