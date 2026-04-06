from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class Mahasiswa(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    nama: str
    nim: str = Field(index=True, unique=True)
    kelas: str

    access_token: Optional[str] = Field(default=None, index=True)

    created_at: datetime = Field(default_factory=datetime.utcnow)
