from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional

class Url(BaseModel):
    original_url : str = Field( max_length=6, error_message = {"String_too_long" : "Custom code can not be greater than 6 characters!"})
    custom_code : Optional[str] = None

class UrlOut(BaseModel):
    original_url: str
    short_url:str
    short_code: str
    custom_code: str | None = None
    created_at : datetime
    expires_at :  datetime