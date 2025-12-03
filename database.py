from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

# sqlite database URL
DATABASE_URL = "sqlite:///./campaigns.db"


#engine to connect the database
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
meta = MetaData()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
