from fastapi import APIRouter, Depends, UploadFile, File
from typing import List
from datetime import datetime
import os
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import os
from apscheduler.schedulers.background import BackgroundScheduler
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pydantic import BaseModel
from typing import Optional
from dotenv import load_dotenv

router = APIRouter()
load_dotenv()
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")


# banco de dados (SQLite ou PostgreSQL)
# acho que vou utilizar postgresql
capsules_db = []

UPLOAD_DIR = "app/static/uploads"
# para criar capsula
@router.post("/capsules/")
async def create_capsule(
    message: str,
    recipient_email: str,
    scheduled_date: str,
    image: UploadFile = File(None),
):
    image_path = None
    if image:
        upload_dir = "uploads"
        os.makedirs(upload_dir, exist_ok=True)
        image_path=f"{upload_dir}/{datetime.now().timestamp()}_{image.filename}"
        with open(image_path, "wb") as buffer:
            buffer.write(await image.read())
            
    new_capsule = {
        "id": len(capsules_db) + 1,
        "message": message,
        "recipient_email": recipient_email,
        "scheduled_date": scheduled_date,
        "image_path": image_path,
        "created_at": datetime.now().isoformat(),
        "is_sent": False,
    }
    capsules_db.append(new_capsule)
    return {"success": True, "capsule": new_capsule}

# para listar capsulas
@router.get("/capsules/")
def list_capsules():
    return capsules_db

# agora aqui que o bixo pega
#  tentar fazer o envio de e-email
def send_capsule_email(capsule):
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_USER
        msg['To'] = capsule['recipient_email']
        msg['Subject'] = "Sua Cápsula do Tempo chegou!"
        
        body = f"""
        Olá do passado!
        Em {capsule['created_at']}, você escreveu:
        {capsule['message']}
        """
        msg.attach(MIMEText(body, 'plain'))
        
        if capsule['image_path']:
            with open(capsule['image_path'], 'rb') as f:
                img = MIMEImage(f.read())
                msg.attach(img)
                
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login("seu-email@gmail.com", 'sua-senha-app')
            server.send_message(msg)
            
        capsule['is_sent'] = True
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")
        

# aqui configuro para verificar capsulas pendentes a cada hora
def check_pending_capsules():
    now = datetime.now()
    for capsule in capsules_db:
        if not capsule['is_sent'] and datetime.fromisoformat(capsule['scheduled_date']) <= now:
            send_capsule_email(capsule)
# inicia o agendador
scheduler = BackgroundScheduler()
scheduler.add_job(check_pending_capsules, 'interval', hours=1)
scheduler.start()
