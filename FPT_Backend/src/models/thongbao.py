from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from src.models.base import Base

class ThongBao(Base):
    __tablename__ = "ThongBao"
    id = Column(Integer, primary_key=True, autoincrement=True)
    tai_khoan_id = Column(Integer, ForeignKey("TaiKhoan.id"))
    noi_dung = Column(Text)
    thoi_gian_gui = Column(DateTime)
    loai_thong_bao = Column(String(50))
    da_doc = Column(Boolean, default=False)
    tai_khoan = relationship("TaiKhoan") 