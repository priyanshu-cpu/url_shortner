from database import Base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

class Url(Base):
    __tablename__ = "url"
    
    id = Column(Integer, primary_key=True, index=True)
    original_url = Column(String, nullable=False)
    short_code = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    click_count = Column(Integer, default=0)
