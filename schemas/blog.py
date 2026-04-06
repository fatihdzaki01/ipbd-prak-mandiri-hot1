from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class BlogCreate(BaseModel):
    judul: str
    isi: str


class BlogResponse(BaseModel):
    id: int
    judul: str
    isi: str

    author_id: int
    author_nama: str
    author_nim: str
    author_kelas: str

    created_at: datetime
    updated_at: datetime


class BlogUpdate(BaseModel):
    judul: Optional[str] = None
    isi: Optional[str] = None
