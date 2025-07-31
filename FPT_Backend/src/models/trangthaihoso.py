from sqlalchemy import Column, Integer, String
from src.models.base import Base

class TrangThaiHoSo(Base):
    __tablename__ = "TrangThaiHoSo"
    id = Column(Integer, primary_key=True, autoincrement=True)
    ten_trang_thai = Column(String(100), nullable=False) 