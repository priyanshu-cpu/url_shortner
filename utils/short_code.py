import random
from database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends
from models.url import Url


chars_for_code = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

def generate_short_code(db):
    res = ""
    for _ in range(6):
        res += ''.join(random.choices(chars_for_code))
    data = db.query(Url).filter(Url.short_code == res).first()
    if data:
        return generate_short_code(db)
    return res
