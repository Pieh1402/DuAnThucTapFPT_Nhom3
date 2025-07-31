from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.models.application import HoSo
from src.models.user import TaiKhoan
from src.models.admin import Admin
from src.models.trangthaihoso import TrangThaiHoSo
from src.schemas.application import ApplicationOut
from src.utils.db import get_db
from src.utils.security import get_current_admin
from src.utils.mail import send_application_status_email
from typing import List
from sqlalchemy import func
from fastapi.encoders import jsonable_encoder
from datetime import datetime

router = APIRouter(prefix="/api/admin", tags=["admin"])

@router.get("/applications", response_model=List[ApplicationOut])
def list_applications(db: Session = Depends(get_db), admin=Depends(get_current_admin)):
    data = db.query(HoSo, TrangThaiHoSo.ten_trang_thai).join(TrangThaiHoSo, HoSo.trang_thai_id == TrangThaiHoSo.id).all()
    result = []
    for hoso, ten_trang_thai in data:
        hoso_dict = {
            'id': hoso.id,
            'tai_khoan_id': hoso.tai_khoan_id,
            'doanh_nghiep_id': hoso.doanh_nghiep_id,
            'ten_ho_so': hoso.ten_ho_so,
            'duong_dan_pdf': hoso.duong_dan_pdf,
            'duong_dan_xml': hoso.duong_dan_xml,
            'da_ky_so': hoso.da_ky_so,
            'trang_thai_id': hoso.trang_thai_id,
            'ngay_nop': hoso.ngay_nop.strftime("%d/%m/%Y %H:%M:%S") if hoso.ngay_nop else None,
            'ten_trang_thai': ten_trang_thai
        }
        result.append(hoso_dict)
    return result

@router.put("/applications/{id}/approve")
def approve_application(id: int, db: Session = Depends(get_db), admin=Depends(get_current_admin)):
    hoso = db.query(HoSo).filter(HoSo.id == id).first()
    if not hoso:
        raise HTTPException(status_code=404, detail="Không tìm thấy hồ sơ")
    hoso.trang_thai_id = 4
    db.commit()
    return {"message": "Đã duyệt hồ sơ"}

@router.put("/applications/{id}/reject")
def reject_application(id: int, db: Session = Depends(get_db), admin=Depends(get_current_admin)):
    hoso = db.query(HoSo).filter(HoSo.id == id).first()
    if not hoso:
        raise HTTPException(status_code=404, detail="Không tìm thấy hồ sơ")
    hoso.trang_thai_id = 5
    db.commit()
    return {"message": "Đã từ chối hồ sơ"}

@router.delete("/applications/{id}")
def delete_application(id: int, db: Session = Depends(get_db), admin=Depends(get_current_admin)):
    hoso = db.query(HoSo).filter(HoSo.id == id).first()
    if not hoso:
        raise HTTPException(status_code=404, detail="Không tìm thấy hồ sơ")
    db.delete(hoso)
    db.commit()
    return {"message": "Đã xóa hồ sơ thành công"}

@router.get("/users")
def list_users(db: Session = Depends(get_db), admin=Depends(get_current_admin)):
    return db.query(TaiKhoan).all()

@router.put("/config")
def update_config():
    return {"message": "Cập nhật cấu hình hệ thống thành công"}

@router.get("/stats")
def get_statistics(db: Session = Depends(get_db), admin=Depends(get_current_admin)):
    total_applications = db.query(HoSo).count()
    total_users = db.query(TaiKhoan).count()
    # Thống kê hồ sơ theo trạng thái
    status_counts = db.query(HoSo.trang_thai_id, func.count(HoSo.id)).group_by(HoSo.trang_thai_id).all()
    stats = {
        "total_applications": total_applications,
        "total_users": total_users,
        "by_status": {str(s[0]): s[1] for s in status_counts}
    }
    return stats 