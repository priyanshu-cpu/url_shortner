from database import Base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime, timezone

class Url(Base):
    __tablename__ = "url"
    
    id = Column(Integer, primary_key=True, index=True)
    original_url = Column(String, nullable=False)
    short_code = Column(String, unique=True, nullable=False)
    short_url = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    expires_at = Column(DateTime)
    click_count = Column(Integer, default=0)
    custom_code = Column(String, nullable=True)
