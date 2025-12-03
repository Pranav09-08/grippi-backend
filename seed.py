#sample data for the mock api

from database import engine, SessionLocal
from models import campaigns

sample_data = [
    {"name": "Summer Sale", "status": "Active", "clicks": 150, "cost": 45.99, "impressions": 1000},
    {"name": "Black Friday", "status": "Paused", "clicks": 320, "cost": 89.50, "impressions": 2500},
    {"name": "Winter Blast", "status": "Active", "clicks": 220, "cost": 65.10, "impressions": 1500},
    {"name": "Diwali Promo", "status": "Paused", "clicks": 90, "cost": 25.00, "impressions": 700},
    {"name": "Holi Offer", "status": "Active", "clicks": 300, "cost": 55.20, "impressions": 1800},
    {"name": "Christmas Boost", "status": "Paused", "clicks": 110, "cost": 30.40, "impressions": 900},
    {"name": "Easter Deal", "status": "Active", "clicks": 75, "cost": 18.00, "impressions": 400},
    {"name": "New Year Blast", "status": "Paused", "clicks": 205, "cost": 70.75, "impressions": 1700},
    {"name": "Back to School", "status": "Active", "clicks": 260, "cost": 82.30, "impressions": 2400},
    {"name": "Monsoon Splash", "status": "Paused", "clicks": 130, "cost": 40.00, "impressions": 1000},
]


db = SessionLocal()
db.execute(campaigns.insert(), sample_data)
db.commit()

print("Sample data inserted!")
