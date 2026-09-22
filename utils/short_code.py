import random
from database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends
from models.url import Url


chars_for_code = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

def generate_short_code(db: Session = Depends(get_db)):
    res = ""
    for _ in range(6):
        res += ''.join(random.choices(chars_for_code))
    data = db.query(Url).all()

    return res
