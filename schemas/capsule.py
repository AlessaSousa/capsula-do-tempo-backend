from pydantic import BaseModel,  EmailStr
from datetime import datetime
from typing import Optional

class CapsuleCreate(BaseModel):
    title: str
    message: str
    delivery_email: EmailStr
    delivery_date: datetime
    image_url: Optional[str] = None
    
class CapsuleResponse(CapsuleCreate):
    id: int
    created_at: datetime
    sent: bool
    
    class Config:
        orm_mode = True