from fastapi import APIRouter, Depends, HTTPException, status
from schemas.url import Url, UrlOut
from sqlalchemy.orm import Session
from database import get_db
from utils.short_code import generate_short_code
from models.url import Url as Model_url

router = APIRouter(prefix="/url")

@router.post("/url")
def long_url(body: Url, db:Session = Depends(get_db)):
    short_code_ = generate_short_code()
    url = Model_url(
        original_url = body.original_url,
        short_code = short_code_
        )
    db.add(url)
    db.commit()
    db.refresh(url)

    return{
        "message" : "short url created success",
        "short_code" : short_code_
    }
