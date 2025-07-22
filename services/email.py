import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import os
from dotenv import load_dotenv
from email import encoders

load_dotenv()

def send_capsule_email(to_email: str, subject: str, body: str, image_path: str = None ):
    smtp_server = os.getenv("SMTP_SERVER")
    smtp_port = int(os.getenv("SMTP_PORT"))
    smtp_user = os.getenv("SMTP_USER")
    smtp_password = os.getenv("SMTP_PASSWORD")
    
    msg = MIMEMultipart()
    msg["From"] = smtp_user
    msg["To"] = to_email
    msg["Subject"] = subject
    
    msg.attach(MIMEText(body, "plain"))
    
    if image_path and os.path.exists(image_path):
        with open(image_path, 'rb') as file:
            mime = MIMEBase('application', 'octet-stream')
            mime.set_payload(file.read())
            encoders.encode_base64(mime)
            mime.add_header('Content_Disposition', f'attachment; filename="{os.path.basename(image_path)}"')
            msg.attach(mime)
    
    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        server.login(smtp_user, smtp_password)
        server.send_message(msg)
        