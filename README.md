# Backend - Run Locally

## 1. Install dependencies
pip install -r requirements.txt

## 2. Start FastAPI server
uvicorn main:app --reload

## Backend will run at:
# http://127.0.0.1:8000

## Test endpoints:
# GET /           → health check
# GET /campaigns  → campaign data
