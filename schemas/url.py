from pydantic import BaseModel
from datetime import datetime

class Url(BaseModel):
    original_url : str

class UrlOut(BaseModel):
    original_url: str
    short_url:str
    short_code: str
    created_at : datetime
    expires_at :  datetime