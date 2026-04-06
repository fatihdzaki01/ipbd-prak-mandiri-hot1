# entry point aplikasi
from fastapi import FastAPI

from app.routes import blog, mahasiswa
from db.init_db import init_db

app = FastAPI(
    title="Praktikum Mahasiswa API",
    description="replikasi Replikasi Website Live Blog dengan Implementasi API",
    version="1.0.0",
)

app.include_router(mahasiswa.router)
app.include_router(blog.router)


@app.on_event("startup")
def on_startup():
    init_db()


@app.get("/")
def root():
    return {"message": "Praktikum Mahasiswa API"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
