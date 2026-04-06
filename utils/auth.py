from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlmodel import Session, select

from db.session import get_session
from models.mahasiswa import Mahasiswa

security = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_session),
):
    token = credentials.credentials

    user = db.exec(select(Mahasiswa).where(Mahasiswa.access_token == token)).first()

    if not user:
        raise HTTPException(status_code=401, detail="Unauthorized")

    return user
