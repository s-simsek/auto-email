# models.py
import datetime
import os

from sqlalchemy import Column, DateTime, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create a base class
Base = declarative_base()

# Define the EmailRecord model
class EmailRecord(Base):
    __tablename__ = 'email_records'
    id = Column(Integer, primary_key=True)
    time_sent = Column(DateTime, default=datetime.datetime.utcnow)
    subject = Column(String)
    body = Column(String)
    to_email = Column(String)

# Database setup
DB_URL = 'sqlite:///emails.db'
engine = create_engine(DB_URL, connect_args={'check_same_thread': False})
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
