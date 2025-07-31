from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from src.models.base import Base

class PhanHoiHoSo(Base):
    __tablename__ = "PhanHoiHoSo"
    id = Column(Integer, primary_key=True, autoincrement=True)
    ho_so_id = Column(Integer, ForeignKey("HoSo.id"))
    ghi_chu = Column(Text)
    duong_dan_file = Column(String(255))
    da_ky_so = Column(Boolean, default=False)
    thoi_gian_gui = Column(DateTime)
    ho_so = relationship("HoSo") 