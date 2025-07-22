from apscheduler.schedulers.background import BackgroundScheduler
from sqlalchemy.orm import Session
from database import SessionLocal
from models.capsule import Capsule
from datetime import datetime
from services.email import send_capsule_email

def check_capsules():
    db: Session = SessionLocal()
    now = datetime.utcnow()
    capsules = db.query(Capsule).filter(
        Capsule.delivery_date <= now,
        Capsule.image_url == None,
        Capsule.sent == False
    ).all()
    
    for capsule in capsules:
        send_capsule_email(
            to_email=capsule.delivery_email,
            subject=f"Cápsula do Tempo: {capsule.title}",
            body=capsule.message,
            image_path=capsule.image_url
        )
        capsule.sent = True
        db.commit()
        db.refresh(capsule)
    db.close()
    
def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(check_capsules, "interval", minutes=1)
    scheduler.start()