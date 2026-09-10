import torch
import torch.nn as nn
import timm
from pathlib import Path
import numpy as np
import logging

logger = logging.getLogger(__name__)

DISEASE_CLASSES = [
    "Apple___Apple_scab",
    "Apple___Black_rot",
    "Apple___Cedar_apple_rust",
    "Apple___healthy",
    "Background___without_leaves",  
    "Blueberry___healthy",
    "Cherry___Powdery_mildew",
    "Cherry___healthy",
    "Corn___Cercospora_leaf_spot Gray_leaf_spot",
    "Corn___Common_rust_",
    "Corn___Northern_Leaf_Blight",
    "Corn___healthy",
    "Grape___Black_rot",
    "Grape___Esca",
    "Grape___Leaf_blight",
    "Grape___healthy",
    "Orange___Haunglongbing",
    "Peach___Bacterial_spot",
    "Peach___healthy",
    "Pepper___Bacterial_spot",
    "Pepper___healthy",
    "Potato___Early_blight",
    "Potato___Late_blight",
    "Potato___healthy",
    "Raspberry___healthy",
    "Soybean___healthy",
    "Squash___Powdery_mildew",
    "Strawberry___Leaf_scorch",
    "Strawberry___healthy",
    "Tomato___Bacterial_spot",
    "Tomato___Early_blight",
    "Tomato___Late_blight",
    "Tomato___Leaf_Mold",
    "Tomato___Septoria_leaf_spot",
    "Tomato___Spider_mites Two-spotted_spider_mite",
    "Tomato___Target_Spot",
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus",
    "Tomato___Tomato_mosaic_virus",
    "Tomato___healthy"
]

_model = None
_device = None

def get_device():
    global _device
    if _device is None:
        _device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    return _device

def build_model(num_classes, pretrained=False):
    model = timm.create_model('efficientnet_b0', pretrained=pretrained)
    
    num_features = model.classifier.in_features
    
    model.classifier = nn.Sequential(
        nn.Dropout(p=0.3),
        nn.Linear(num_features, 512),
        nn.BatchNorm1d(512),
        nn.ReLU(inplace=True),
        nn.Dropout(p=0.2),
        nn.Linear(512, num_classes)
    )
    
    return model

def load_model():
    global _model
    
    if _model is not None:
        return _model
    
    device = get_device()
    model_path = Path(__file__).parent / "models" / "plant_disease_model_final.pth"
    
    try:
        model = build_model(len(DISEASE_CLASSES), pretrained=False)
        
        if model_path.exists():
            checkpoint = torch.load(model_path, map_location=device, weights_only=False)
            
            if isinstance(checkpoint, dict):
                if 'model_state_dict' in checkpoint:
                    model.load_state_dict(checkpoint['model_state_dict'])
                elif 'state_dict' in checkpoint:
                    model.load_state_dict(checkpoint['state_dict'])
                else:
                    model.load_state_dict(checkpoint)
            else:
                model.load_state_dict(checkpoint)
            
        else:
            raise Exception(f"Model file not found at {model_path}")
        
        model.to(device)
        model.eval()
        _model = model
        
        return _model
    
    except Exception as e:
        raise Exception(f"Failed to load model: {str(e)}")

def predict(image_tensor: torch.Tensor) -> np.ndarray:
    model = load_model()
    device = get_device()
    
    try:
        with torch.no_grad():
            image_tensor = image_tensor.to(device)
            outputs = model(image_tensor)
            probabilities = torch.softmax(outputs, dim=1)
            predictions = probabilities.cpu().numpy()
        
        return predictions
    
    except Exception as e:
        raise Exception(f"Prediction failed: {str(e)}")
