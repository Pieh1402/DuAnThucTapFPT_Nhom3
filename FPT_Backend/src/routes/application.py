import os
from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session


from src.models.application import HoSo
from src.schemas.application import ApplicationOut
from src.utils.db import get_db
from src.utils.mail import send_application_status_email
from src.utils.security import get_current_user

router = APIRouter(prefix="/api/applications", tags=["applications"])

@router.get("/test")
def test_api():
    return {"message": "API hoạt động bình thường!"}

@router.post("/", response_model=ApplicationOut)
def create_application(company_info: str = None, file: UploadFile = File(...), db: Session = Depends(get_db), user=Depends(get_current_user)):
    # Kiểm tra định dạng file
    if not (file.filename.lower().endswith('.pdf') or file.filename.lower().endswith('.xml')):
        raise HTTPException(status_code=400, detail="Chỉ chấp nhận file PDF hoặc XML")
    # Lưu file (ví dụ: lưu vào thư mục uploads, ở đây chỉ demo đường dẫn)
    file_path = f"uploads/{file.filename}"
    os.makedirs("uploads", exist_ok=True)
    with open(file_path, "wb") as f:
        f.write(file.file.read())
    hoso = HoSo(tai_khoan_id=user.id, ten_ho_so=company_info, duong_dan_pdf=file_path if file.filename.lower().endswith('.pdf') else None, duong_dan_xml=file_path if file.filename.lower().endswith('.xml') else None, ngay_nop=datetime.now(), trang_thai_id=1)
    db.add(hoso)
    db.commit()
    db.refresh(hoso)
    send_application_status_email(user.email, "Đã tiếp nhận hồ sơ")
    
    # Convert datetime to string for response
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
        'ten_trang_thai': None
    }
    return hoso_dict

@router.get("/{id}/status")
def get_application_status(id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    hoso = db.query(HoSo).filter(HoSo.id == id, HoSo.tai_khoan_id == user.id).first()
    if not hoso:
        raise HTTPException(status_code=404, detail="Không tìm thấy hồ sơ")
    return {"status": hoso.trang_thai_id}  

@router.put("/{id}", response_model=ApplicationOut)
def update_application(id: int, file: UploadFile = File(...), db: Session = Depends(get_db), user=Depends(get_current_user)):
    # Kiểm tra định dạng file
    if not (file.filename.lower().endswith('.pdf') or file.filename.lower().endswith('.xml')):
        raise HTTPException(status_code=400, detail="Chỉ chấp nhận file PDF hoặc XML")
    file_path = f"uploads/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(file.file.read())
    hoso = db.query(HoSo).filter(HoSo.id == id, HoSo.tai_khoan_id == user.id).first()
    if not hoso:
        raise HTTPException(status_code=404, detail="Không tìm thấy hồ sơ")
    if file.filename.lower().endswith('.pdf'):
        hoso.duong_dan_pdf = file_path
    else:
        hoso.duong_dan_xml = file_path
    db.commit()
    db.refresh(hoso)
    send_application_status_email(user.email, "Đã bổ sung hồ sơ")
    
    # Convert datetime to string for response
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
        'ten_trang_thai': None
    }
    return hoso_dict 