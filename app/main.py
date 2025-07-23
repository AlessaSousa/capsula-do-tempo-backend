from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import auth, capsule
from app.database import engine, Base
from app.models import user
from app.services.scheduler import start_scheduler

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
app.include_router(capsule.router, prefix="/capsule", tags=["Capsule"])

start_scheduler()