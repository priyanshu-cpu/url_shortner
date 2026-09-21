from pydantic import BaseModel

class Url(BaseModel):
    original_url : str

class UrlOut(BaseModel):
    original_url: str
    short_url:str
    short_code: str
