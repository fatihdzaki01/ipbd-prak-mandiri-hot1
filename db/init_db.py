from sqlmodel import SQLModel

from db.session import engine
from models.blog import Blog

# import model biar ke-detect
from models.mahasiswa import Mahasiswa


def init_db():
    SQLModel.metadata.create_all(engine)
