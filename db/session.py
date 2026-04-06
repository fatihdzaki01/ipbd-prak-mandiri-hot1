# membuat koneksi ke db
from sqlmodel import Session, SQLModel, create_engine

DATABASE_URL = "postgresql://postgres-ipbd:43210@localhost:5436/ipbd_db_tugasprak1"

# bikin engine (koneksi ke DB)
engine = create_engine(DATABASE_URL, echo=True)


# dependency untuk FastAPI
def get_session():
    with Session(engine) as session:
        yield session
