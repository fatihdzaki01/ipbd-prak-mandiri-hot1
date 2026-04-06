from datetime import datetime

from sqlmodel import Session, select

from models.blog import Blog
from models.mahasiswa import Mahasiswa
from schemas.blog import BlogCreate, BlogUpdate


class BlogService:
    def create(self, db: Session, data: BlogCreate, user: Mahasiswa):
        blog = Blog(judul=data.judul, isi=data.isi, author_id=user.id)

        db.add(blog)
        db.commit()
        db.refresh(blog)

        author = db.get(Mahasiswa, blog.author_id)

        return {
            "id": blog.id,
            "judul": blog.judul,
            "isi": blog.isi,
            "author_id": blog.author_id,
            "author_nama": author.nama,
            "author_nim": author.nim,
            "author_kelas": author.kelas,
            "created_at": blog.created_at,
            "updated_at": blog.updated_at,
        }

    def get_all(self, db: Session):
        blogs = db.exec(select(Blog)).all()

        result = []

        for blog in blogs:
            author = db.get(Mahasiswa, blog.author_id)

            result.append(
                {
                    "id": blog.id,
                    "judul": blog.judul,
                    "isi": blog.isi,
                    "author_id": blog.author_id,
                    "author_nama": author.nama,
                    "author_nim": author.nim,
                    "author_kelas": author.kelas,
                    "created_at": blog.created_at,
                    "updated_at": blog.updated_at,
                }
            )

        return result

    def get_by_id(self, db: Session, blog_id: int):
        blog = db.get(Blog, blog_id)

        if not blog:
            return None

        author = db.get(Mahasiswa, blog.author_id)

        return {
            "id": blog.id,
            "judul": blog.judul,
            "isi": blog.isi,
            "author_id": blog.author_id,
            "author_nama": author.nama,
            "author_nim": author.nim,
            "author_kelas": author.kelas,
            "created_at": blog.created_at,
            "updated_at": blog.updated_at,
        }

    def update(self, db: Session, blog_id: int, data: BlogUpdate):
        blog = db.get(Blog, blog_id)

        if not blog:
            return None

        if data.judul is not None:
            blog.judul = data.judul
        if data.isi is not None:
            blog.isi = data.isi

        blog.updated_at = datetime.utcnow()

        db.add(blog)
        db.commit()
        db.refresh(blog)

        author = db.get(Mahasiswa, blog.author_id)

        return {
            "id": blog.id,
            "judul": blog.judul,
            "isi": blog.isi,
            "author_id": blog.author_id,
            "author_nama": author.nama,
            "author_nim": author.nim,
            "author_kelas": author.kelas,
            "created_at": blog.created_at,
            "updated_at": blog.updated_at,
        }

    def delete(self, db: Session, blog_id: int):
        blog = db.get(Blog, blog_id)

        if not blog:
            return False

        db.delete(blog)
        db.commit()

        return True
