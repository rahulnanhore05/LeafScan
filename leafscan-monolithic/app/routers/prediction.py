from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
import numpy as np
from pydantic import BaseModel
from typing import Optional
from app.database.connection import get_db
from app.database.models import User, Image, Prediction
from app.routers.auth import get_current_user, TokenData
from app.ml.model_loader import predict, DISEASE_CLASSES
from app.services.email_service import send_prediction_email
from app.services.image_service import upload_to_cloudinary
from app.services.disease_service import format_disease_response, parse_disease_class
from app.utils.image_processor import preprocess_image_for_ml
import asyncio


router = APIRouter(prefix="/api/prediction", tags=["Prediction"])

class DiseaseAdvice(BaseModel):
    title: str
    why: str


class DiseaseData(BaseModel):
    plant_name: str
    disease_name: str
    description: Optional[str] = None
    symptoms: Optional[list[str]] = []
    causes: Optional[list[str]] = []
    spread_mechanisms: Optional[list[str]] = []
    care_advices: list[DiseaseAdvice] = []


class PredictionResponse(BaseModel):
    id: int
    disease_data: DiseaseData
    confidence: float
    cloudinary_url: str
    image_url: str
    created_at: datetime
    
    class Config:
        from_attributes = True


@router.post("/predict", response_model=PredictionResponse)
async def predict_disease(
    file: UploadFile = File(...),
    current_user: TokenData = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    try:
        
        if file.content_type not in ["image/jpeg", "image/jpg", "image/png"]:
            raise HTTPException(
                status_code=400,
                detail="Invalid file type. Only JPEG and PNG images are supported."
            )
        
        image_bytes = await file.read()        
        cloudinary_result = upload_to_cloudinary(image_bytes, file.filename)
        
        image_obj = Image(
            user_id=current_user.user_id,
            cloudinary_url=cloudinary_result["url"],
            cloudinary_public_id=cloudinary_result["public_id"],
            original_filename=file.filename,
            file_size=len(image_bytes)
        )
        db.add(image_obj)
        db.flush()

        processed_image = preprocess_image_for_ml(image_bytes)
        predictions = predict(processed_image)
        
        if predictions.shape[1] != len(DISEASE_CLASSES):
            raise HTTPException(
                status_code=500,
            )
        
        predicted_idx = int(np.argmax(predictions[0]))
        confidence = float(predictions[0][predicted_idx])
        
        disease_full = DISEASE_CLASSES[predicted_idx]
        
        plant_type, disease_name = parse_disease_class(disease_full)
        
        disease_data_dict = format_disease_response(disease_name, plant_type)
        
        care_advices = [
            DiseaseAdvice(title=advice['title'], why=advice['why']) 
            for advice in disease_data_dict.get('care_advices', [])
        ]
        
        disease_data = DiseaseData(
            plant_name=disease_data_dict.get('plant_name', plant_type),
            disease_name=disease_data_dict.get('disease_name', disease_name),
            description=disease_data_dict.get('description', ''),
            symptoms=disease_data_dict.get('symptoms', []),
            causes=disease_data_dict.get('causes', []),
            spread_mechanisms=disease_data_dict.get('spread_mechanisms', []),
            care_advices=care_advices
        )
        
        if "healthy" in disease_name.lower():
            severity = "none"
        elif confidence > 0.8:
            severity = "severe"
        elif confidence > 0.6:
            severity = "moderate"
        else:
            severity = "mild"
        
        prediction = Prediction(
            user_id=current_user.user_id,
            image_id=image_obj.id,
            disease_name=disease_name,
            plant_type=plant_type,
            confidence=confidence,
            severity=severity,
            care_advice=care_advices[0].title if care_advices else "No specific advice available."
        )
        db.add(prediction)
        db.commit()
        db.refresh(prediction)
        
        user = db.query(User).filter(User.id == current_user.user_id).first()
        if user and user.email:
            try:
                disease_data_for_email = format_disease_response(disease_name, plant_type)
        
                asyncio.create_task(send_prediction_email(
                to_email=user.email,
                disease_name=disease_name,
                confidence=confidence,
                plant_type=plant_type,
                severity=severity,
                disease_data=disease_data_for_email 
                ))
            except Exception as e:
                logger.warning(f"Email task creation failed: {e}")

        return {
            "id": prediction.id,
            "disease_data": disease_data,
            "confidence": confidence,
            "cloudinary_url": cloudinary_result["url"],
            "image_url": cloudinary_result["url"],
            "created_at": prediction.created_at
        }
    
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(e)}"
        )
