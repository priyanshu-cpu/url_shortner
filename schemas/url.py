from pydantic import BaseModel, Field, ValidationError
from datetime import datetime


class Url(BaseModel):
    original_url: str
    custom_code: str = Field(
        default=None,
        max_length=6,
        error_message={
            "String_too_long": "Custom code can not be greater than 6 characters!"
        },
    )


class UrlOut(BaseModel):
    original_url: str
    short_url: str
    short_code: str
    custom_code: str | None = None
    created_at: datetime
    expires_at: datetime
