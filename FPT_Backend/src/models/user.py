from sqlalchemy import Column, Integer, String, Boolean, DateTime
from src.models.base import Base
import datetime

class TaiKhoan(Base):
    __tablename__ = "TaiKhoan"
    id = Column(Integer, primary_key=True, autoincrement=True)
    ten_dang_nhap = Column(String(50), unique=True)
    email = Column(String(100), unique=True, nullable=False)
    mat_khau = Column(String(256), nullable=False)
    so_dien_thoai = Column(String(20))
    trang_thai = Column(Integer, default=1)
    ngay_tao = Column(DateTime) 