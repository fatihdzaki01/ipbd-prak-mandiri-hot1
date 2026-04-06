import uuid

from sqlmodel import Session, select

from models.mahasiswa import Mahasiswa
from schemas.mahasiswa import MahasiswaCreate


class MahasiswaService:
    def create(self, db: Session, data: MahasiswaCreate):
        existing = db.exec(select(Mahasiswa).where(Mahasiswa.nim == data.nim)).first()

        if existing:
            raise ValueError("NIM already registered")

        token = str(uuid.uuid4())

        mahasiswa = Mahasiswa(
            nama=data.nama, nim=data.nim, kelas=data.kelas, access_token=token
        )

        db.add(mahasiswa)
        db.commit()
        db.refresh(mahasiswa)

        return {"access_token": token, "token_type": "bearer", "mahasiswa": mahasiswa}
