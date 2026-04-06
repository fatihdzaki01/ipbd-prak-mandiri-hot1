# mendefinisikan URL endpoint
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app.services.mahasiswa_service import MahasiswaService
from db.session import get_session
from schemas.mahasiswa import MahasiswaCreate, MahasiswaResponse, RegisterResponse

router = APIRouter(prefix="/api", tags=["Mahasiswa"])

service = MahasiswaService()


@router.post("/register", response_model=RegisterResponse, status_code=201)
def register(data: MahasiswaCreate, db: Session = Depends(get_session)):
    try:
        return service.create(db, data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
