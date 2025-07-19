# from pydantic import BaseModel, EmailStr
# from datetime import datetime
# from typing import Optional

# class UserBase(BaseModel):
#     email: EmailStr
#     username: str
    
# class UserCreate(UserBase):
#     password: str

# class User(UserBase):
#     id: int
#     is_active: bool
    
#     class Config:
#         orm_mode = True

# class CapsuleBase(BaseModel):
#     recipient_email: EmailStr
#     delivery_date: datetime
#     message: str
#     is_opened: bool = False

# class Capsule(CapsuleBase):
#     id: int
#     created_at: datetime
#     owner_id: int
#     image_path: Optional[str] = None
    
#     class Config:
#         orm_mode = True