from sqlalchemy import Column, Integer, String
from src.models.base import Base

class Admin(Base):
    __tablename__ = "Admin"
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(100), unique=True, nullable=False)
    mat_khau = Column(String(256), nullable=False)
    ho_ten = Column(String(100))
    phan_quyen = Column(String(50)) 