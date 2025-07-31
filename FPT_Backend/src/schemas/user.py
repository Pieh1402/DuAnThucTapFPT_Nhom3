from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    company_name: str
    email: EmailStr
    phone: str
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    company_name: str
    email: EmailStr
    phone: str
    role: str
    is_verified: bool
    class Config:
        from_attributes = True 