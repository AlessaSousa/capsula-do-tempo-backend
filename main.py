from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import auth, capsule
from database import engine, Base

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credential=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth")
app.include_router(capsule.router, prefix="/capsule")