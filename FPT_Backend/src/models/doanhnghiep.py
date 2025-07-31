from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey
from sqlalchemy.orm import relationship
from src.models.base import Base

class DoanhNghiep(Base):
    __tablename__ = "DoanhNghiep"
    id = Column(Integer, primary_key=True, autoincrement=True)
    tai_khoan_id = Column(Integer, ForeignKey("TaiKhoan.id"))
    ten_doanh_nghiep = Column(String(255))
    dia_chi = Column(Text)
    ma_so_thue = Column(String(20))
    loai_hinh = Column(String(100))
    ngay_dang_ky = Column(Date)
    tai_khoan = relationship("TaiKhoan") 