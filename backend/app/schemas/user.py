from pydantic import BaseModel, EmailStr

# 共通属性
class UserBase(BaseModel):
    name: str
    email: EmailStr

# ユーザ登録時のスキーマ
class UserCreate(UserBase):
    password: str