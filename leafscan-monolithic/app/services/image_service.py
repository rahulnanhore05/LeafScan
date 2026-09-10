import cloudinary
import cloudinary.uploader
from app.config import settings

cloudinary.config(
    cloud_name=settings.CLOUDINARY_CLOUD_NAME,
    api_key=settings.CLOUDINARY_API_KEY,
    api_secret=settings.CLOUDINARY_API_SECRET
)

def upload_to_cloudinary(image_bytes: bytes, filename: str) -> dict:
    try:
        result = cloudinary.uploader.upload(
            image_bytes,
            folder="leafscan/uploads",
            resource_type="image",
            public_id=filename.replace(".", "_")[:50]
        )
        
        return {
            "url": result["secure_url"],
            "public_id": result["public_id"],
            "format": result["format"]
        }
    except Exception as e:
        raise Exception(f"Image upload failed: {str(e)}")

def delete_from_cloudinary(public_id: str) -> bool:
    try:
        result = cloudinary.uploader.destroy(public_id)
        return result.get("result") == "ok"
    except Exception as e:
        return False
