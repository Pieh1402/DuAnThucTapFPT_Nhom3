from pydantic import BaseModel
from typing import Optional

class ApplicationCreate(BaseModel):
    company_info: str
    file_url: str
    signed_at: Optional[str]

class ApplicationUpdate(BaseModel):
    file_url: Optional[str]
    signed_at: Optional[str]

class ApplicationOut(BaseModel):
    id: int
    tai_khoan_id: int
    doanh_nghiep_id: int | None = None
    ten_ho_so: str
    duong_dan_pdf: str | None = None
    duong_dan_xml: str | None = None
    da_ky_so: bool
    trang_thai_id: int | None = None
    ngay_nop: str | None = None
    ten_trang_thai: str | None = None
    class Config:
        from_attributes = True 