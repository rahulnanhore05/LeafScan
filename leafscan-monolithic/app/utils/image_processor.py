import cv2
import numpy as np
import torch
from albumentations import Compose, Resize, Normalize
from albumentations.pytorch import ToTensorV2

IMG_SIZE = 224
MEAN_IMAGENET = [0.485, 0.456, 0.406]
STD_IMAGENET = [0.229, 0.224, 0.225]

preprocess_transform = Compose([
    Resize(IMG_SIZE, IMG_SIZE),
    Normalize(mean=MEAN_IMAGENET, std=STD_IMAGENET),
    ToTensorV2()
])

def preprocess_image_for_ml(image_bytes: bytes) -> torch.Tensor:
    try:
        nparr = np.frombuffer(image_bytes, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        if img is None:
            raise ValueError("Unable to decode image bytes. File may be corrupted.")
        
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        augmented = preprocess_transform(image=img)
        img_tensor = augmented['image']
        
        img_tensor = img_tensor.unsqueeze(0)
        
        return img_tensor
    
    except Exception as e:
        raise Exception(f"Image preprocessing failed: {str(e)}")
