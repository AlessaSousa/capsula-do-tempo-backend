from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.capsule import Capsule
from app.models.user import User
from app.schemas.capsule import CapsuleCreate, CapsuleResponse
from uuid import uuid4
from datetime import datetime
from app.core.dependencies import get_current_user 
from app.crud.capsule import create_capsule, get_capsules
from app.core.dependencies import get_db

router = APIRouter()

@router.post("/", response_model=CapsuleResponse, status_code=status.HTTP_201_CREATED)
def create_cpsule(
    capsule: CapsuleCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return create_capsule(capsule, db, current_user)

@router.get("/", response_model=list[CapsuleResponse])
def list_capsules(
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user)
):
    return get_capsules(db, current_user)
