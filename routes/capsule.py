from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import SessionLocal
from models.capsule import Capsule
from models.user import User
from schemas.capsule import CapsuleCreate, CapsuleResponse
from uuid import uuid4
from datetime import datetime
from utils.dependencies import get_current_user 

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter()

@router.post("/", response_model=CapsuleResponse, status_code=status.HTTP_201_CREATED)
def create_capsule(capsule: CapsuleCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    new_capsule = Capsule(
        title = capsule.title,
        message = capsule.message,
        delivery_email = capsule.delivery_email,
        delivery_date = capsule.delivery_date,
        image_url = capsule.image_url,
        created_at = datetime.utcnow(),
        user_id = current_user.id
    )
    db.add(new_capsule)
    db.commit()
    db.refresh(new_capsule)
    return new_capsule

@router.get("/", response_model=list[CapsuleResponse])
def list_capsules(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(Capsule).filter(Capsule.user_id == current_user.id).all()
