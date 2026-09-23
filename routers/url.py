from fastapi import APIRouter, Depends, HTTPException, status
from schemas.url import Url, UrlOut
from sqlalchemy.orm import Session
from database import get_db
from utils.short_code import generate_short_code
from models.url import Url as Model_url
from fastapi.responses import RedirectResponse
from datetime import datetime, timedelta, timezone

router = APIRouter(prefix="/url")

@router.post("/create")
def long_url(body: Url, db:Session = Depends(get_db)):
    short_code_ = generate_short_code(db)
    url = Model_url(
        original_url = body.original_url,
        short_code = short_code_,
        short_url  = f"localhost:8000/url/{short_code_}",
        expires_at = datetime.now(timezone.utc) + timedelta(minutes=5),
        custom_code = body.custom_code
        )
    db.add(url)
    db.commit()
    db.refresh(url)

    return{
        "message" : "short url created",
        "short_code" : short_code_,
        "short_url" : f"localhost:8000/url/{short_code_}"
    }

@router.get("/{short_code}")
def get_url(short_code: str, db : Session =Depends(get_db)):
    find_code = db.query(Model_url).filter(Model_url.short_code == short_code).first()
    if find_code is None:
        raise HTTPException(status_code=404, detail="short code not found!")

    if find_code.expires_at < datetime.now():
        raise HTTPException(status_code=404, detail="the code has expired!")
    
    find_code.click_count+=1
    db.commit()
    db.refresh(find_code)
    return RedirectResponse(url=find_code.original_url)

@router.get("/{short_code}/stats", response_model=UrlOut)
def get_url_stats(short_code: str, db: Session =Depends(get_db)):
    data = db.query(Model_url).filter(Model_url.short_code == short_code).first()
    if not data:
        raise HTTPException(status_code=404, detail="Not found!")
    return data