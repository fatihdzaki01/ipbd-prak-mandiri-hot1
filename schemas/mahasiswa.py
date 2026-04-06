from datetime import datetime

from pydantic import BaseModel


class MahasiswaCreate(BaseModel):
    nama: str
    nim: str
    kelas: str


class MahasiswaResponse(BaseModel):
    id: int
    nama: str
    nim: str
    kelas: str
    created_at: datetime


class RegisterResponse(BaseModel):
    access_token: str
    token_type: str
    mahasiswa: MahasiswaResponse
