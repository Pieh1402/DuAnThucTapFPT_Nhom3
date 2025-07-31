from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

from src.models.user import TaiKhoan
from src.models.doanhnghiep import DoanhNghiep
from src.models.trangthaihoso import TrangThaiHoSo
from src.models.application import HoSo
from src.models.application_status_history import PhanHoiHoSo
from src.models.thongbao import ThongBao
from src.models.admin import Admin

# Import routes sau
from src.routes import auth, application, admin

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(application.router)
app.include_router(admin.router)

@app.get("/")
def read_root():
    return {"message": "Cổng đăng ký doanh nghiệp - FastAPI"}
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.main:app", host="127.0.0.1", port=8000, reload=True)
