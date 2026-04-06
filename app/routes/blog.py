from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app.services.blog_service import BlogService
from db.session import get_session
from schemas.blog import BlogCreate, BlogResponse, BlogUpdate
from utils.auth import get_current_user

router = APIRouter(prefix="/api/blogs", tags=["Blogs"])

service = BlogService()


@router.post("/", status_code=201)
def create_blog(
    data: BlogCreate, db: Session = Depends(get_session), user=Depends(get_current_user)
):
    return service.create(db, data, user)


@router.get("/", response_model=list[BlogResponse])
def get_blogs(db: Session = Depends(get_session)):
    return service.get_all(db)


@router.get("/{blog_id}", response_model=BlogResponse)
def get_blog(blog_id: int, db: Session = Depends(get_session)):
    blog = service.get_by_id(db, blog_id)

    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")

    return blog


@router.put("/{blog_id}")
def update_blog(
    blog_id: int,
    data: BlogUpdate,
    db: Session = Depends(get_session),
    user=Depends(get_current_user),
):
    blog = service.update(db, blog_id, data)

    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")

    return blog


@router.delete("/{blog_id}")
def delete_blog(
    blog_id: int, db: Session = Depends(get_session), user=Depends(get_current_user)
):
    success = service.delete(db, blog_id)

    if not success:
        raise HTTPException(status_code=404, detail="Blog not found")

    return {"message": "Blog deleted"}
