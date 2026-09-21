from database import Base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime, UTC, timedelta

class Url(Base):
    __tablename__ = "url"
    
    id = Column(Integer, primary_key=True, index=True)
    original_url = Column(String)
    short_code = Column(String)
    created_at = Column(DateTime, default=datetime.now(UTC))
    click_amount = Column(Integer)
