from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import SessionLocal
from models import campaigns
from sqlalchemy import select

app = FastAPI()

# Adding CORS to allow requests from frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/campaigns")
def get_campaigns():
    db = SessionLocal()
    query = select(campaigns)
    result = db.execute(query).mappings().all()
    return list(result)
