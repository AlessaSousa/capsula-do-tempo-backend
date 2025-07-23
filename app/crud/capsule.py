from datetime import datetime
from fastapi import Depends
from app.core.dependencies import get_current_user
from app.database import SessionLocal
from app.models.capsule import Capsule
from app.models.user import User
from app.schemas.capsule import CapsuleCreate
from sqlalchemy.orm import Session
from app.core.dependencies import get_db

def create_capsule(capsule: CapsuleCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    new_capsule = Capsule(
        **capsule.dict(exclude_unset=True),
        user_id = current_user.id
    )
    db.add(new_capsule)
    db.commit()
    db.refresh(new_capsule)
    return new_capsule

def get_capsules(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(Capsule).filter(Capsule.user_id == current_user.id).all()
