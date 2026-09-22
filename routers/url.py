from fastapi import APIRouter, Depends, HTTPException, status
from schemas.url import Url, UrlOut
from sqlalchemy.orm import Session
from database import get_db
from utils.short_code import generate_short_code
from models.url import Url as Model_url
from fastapi.responses import RedirectResponse

router = APIRouter(prefix="/url")

@router.post("/create")
def long_url(body: Url, db:Session = Depends(get_db)):
    short_code_ = generate_short_code(db)
    url = Model_url(
        original_url = body.original_url,
        short_code = short_code_
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
    return RedirectResponse(url=find_code.original_url)
