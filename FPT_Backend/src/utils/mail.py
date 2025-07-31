from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from pydantic import EmailStr
import os

conf = ConnectionConfig(
    MAIL_USERNAME = os.getenv("MAIL_USERNAME"),
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD"),
    MAIL_FROM = os.getenv("MAIL_FROM"),
    MAIL_PORT = 587,
    MAIL_SERVER = os.getenv("MAIL_SERVER"),
    USE_CREDENTIALS = True
)

def send_application_status_email(email: EmailStr, status: str):
    # Hàm này có thể dùng sync hoặc async tùy cấu hình
    # Đơn giản hóa: chỉ in ra log hoặc gửi email thật nếu cấu hình SMTP
    print(f"Gửi email tới {email}: Trạng thái hồ sơ mới: {status}") 