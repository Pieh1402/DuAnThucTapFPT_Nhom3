from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from src.models.base import Base

class HoSo(Base):
    __tablename__ = "HoSo"
    id = Column(Integer, primary_key=True, autoincrement=True)
    tai_khoan_id = Column(Integer, ForeignKey("TaiKhoan.id"))
    doanh_nghiep_id = Column(Integer, ForeignKey("DoanhNghiep.id"), nullable=True)
    ten_ho_so = Column(String(255))
    duong_dan_pdf = Column(String(255))
    duong_dan_xml = Column(String(255))
    da_ky_so = Column(Boolean, default=False)
    trang_thai_id = Column(Integer, ForeignKey("TrangThaiHoSo.id"))
    ngay_nop = Column(DateTime)
    # Quan hệ
    tai_khoan = relationship("TaiKhoan")
    doanh_nghiep = relationship("DoanhNghiep")
    trang_thai = relationship("TrangThaiHoSo") 