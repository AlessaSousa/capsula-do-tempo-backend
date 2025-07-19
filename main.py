from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import auth, capsule
from database import engine, Base
from models import user

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

user.Base.metadata.create_all(bind=engine)
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
# app.include_router(capsule.router, prefix="/capsule")