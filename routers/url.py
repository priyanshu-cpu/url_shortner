from fastapi import APIRouter, Depends, HTTPException, status
from schemas.url import Url, UrlOut
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter(prefix="/url")

@router.post("/url", response_model=UrlOut)
def long_url(body: Url, db:Session = Depends(get_db)):
    url = Url(original_url = body.original_url)