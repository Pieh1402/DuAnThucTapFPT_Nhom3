from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.schemas.user import UserLogin, UserCreate
from src.models.user import TaiKhoan
from src.utils.security import verify_password, create_access_token, pwd_context
from src.utils.db import get_db
from src.models.admin import Admin
from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
print(pwd_context.hash("admin123"))

router = APIRouter(prefix="/api/auth", tags=["auth"])

@router.get("/test")
def test_auth():
    return {"message": "Auth API hoạt động!"}

@router.post("/login")
def login(user_login: UserLogin, db: Session = Depends(get_db)):
    # Thử tìm trong bảng TaiKhoan (user)
    user = db.query(TaiKhoan).filter(TaiKhoan.email == user_login.email).first()
    if user and verify_password(user_login.password, user.mat_khau):
        access_token = create_access_token({"sub": user.email, "role": "user"})
        return {"access_token": access_token, "token_type": "bearer", "role": "user"}

    # Nếu không có user, thử tìm trong bảng Admin
    admin = db.query(Admin).filter(Admin.email == user_login.email).first()
    if admin and verify_password(user_login.password, admin.mat_khau):
        access_token = create_access_token({"sub": admin.email, "role": "admin"})
        return {"access_token": access_token, "token_type": "bearer", "role": "admin"}

    # Nếu không tìm thấy hoặc sai mật khẩu
    raise HTTPException(status_code=401, detail="Email hoặc mật khẩu không đúng")

@router.post("/register")
def register(user_create: UserCreate, db: Session = Depends(get_db)):
    # Kiểm tra email đã tồn tại chưa
    if db.query(TaiKhoan).filter(TaiKhoan.email == user_create.email).first():
        raise HTTPException(status_code=400, detail="Email đã được sử dụng")
    # Kiểm tra độ mạnh mật khẩu
    if len(user_create.password) < 6:
        raise HTTPException(status_code=400, detail="Mật khẩu phải có ít nhất 6 ký tự")
    # Hash mật khẩu
    hashed_password = pwd_context.hash(user_create.password)
    # Tạo tài khoản mới
    new_user = TaiKhoan(
        ten_dang_nhap=user_create.company_name,
        email=user_create.email,
        mat_khau=hashed_password,
        so_dien_thoai=user_create.phone,
        ngay_tao=None
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "Đăng ký thành công!"} 