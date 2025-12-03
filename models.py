# required imports
from sqlalchemy import Table, Column, Integer, String, Float
from database import meta, engine


#the campaign database table with required field
campaigns = Table(
    "campaigns",
    meta,
    Column("id", Integer, primary_key=True),
    Column("name", String(255)),
    Column("status", String(50)),
    Column("clicks", Integer),
    Column("cost", Float),
    Column("impressions", Integer),
)

meta.create_all(engine)
