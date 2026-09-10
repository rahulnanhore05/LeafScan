from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from pydantic import BaseModel
from app.database.connection import get_db
from app.database.models import Image
from app.routers.auth import get_current_user, TokenData
from app.services.image_service import upload_to_cloudinary, delete_from_cloudinary
from app.config import settings

router = APIRouter(prefix="/api/image", tags=["Image"])

class ImageResponse(BaseModel):
    id: int
    user_id: int
    cloudinary_url: str
    original_filename: str
    file_size: int
    uploaded_at: datetime
    
    class Config:
        from_attributes = True

@router.post("/upload", response_model=ImageResponse)
async def upload_image(
    file: UploadFile = File(...),
    current_user: TokenData = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if file.content_type not in ["image/jpeg", "image/png", "image/jpg"]:
        raise HTTPException(status_code=400, detail="Only JPEG and PNG images allowed")
    
    image_bytes = await file.read()
    file_size = len(image_bytes)
    max_size = settings.MAX_FILE_SIZE_MB * 1024 * 1024
    
    if file_size > max_size:
        raise HTTPException(status_code=413, detail=f"File exceeds {settings.MAX_FILE_SIZE_MB}MB")
    
    result = upload_to_cloudinary(image_bytes, file.filename)
    
    image = Image(
        user_id=current_user.user_id,
        cloudinary_url=result["url"],
        cloudinary_public_id=result["public_id"],
        original_filename=file.filename,
        file_size=file_size
    )
    db.add(image)
    db.commit()
    db.refresh(image)
    
    return image

@router.get("/{image_id}", response_model=ImageResponse)
def get_image(
    image_id: int,
    current_user: TokenData = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    image = db.query(Image).filter(Image.id == image_id).first()
    
    if not image:
        raise HTTPException(status_code=404, detail="Image not found")
    
    if image.user_id != current_user.user_id:
        raise HTTPException(status_code=403, detail="Not authorized")
    
    return image

@router.delete("/{image_id}")
def delete_image(
    image_id: int,
    current_user: TokenData = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    image = db.query(Image).filter(Image.id == image_id).first()
    
    if not image:
        raise HTTPException(status_code=404, detail="Image not found")
    
    if image.user_id != current_user.user_id:
        raise HTTPException(status_code=403, detail="Not authorized")
    
    delete_from_cloudinary(image.cloudinary_public_id)
    db.delete(image)
    db.commit()
    
    return {"message": "Image deleted"}
