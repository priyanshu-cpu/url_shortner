from pydantic import BaseModel

class Url(BaseModel):
    url = str

class UrlOut(BaseModel):
    pass 