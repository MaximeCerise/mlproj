from fastapi import FastAPI, UploadFile, File, Form
import pandas as pd
import joblib
from PIL import Image
from narwhals import DataFrame
from torchvision import transforms
import numpy as np
import torch

app = FastAPI()

CLASS_NAMES = {
    0: "airplane",
    1: "automobile",
    2: "bird",
    3: "cat",
    4: "deer",
    5: "dog",
    6: "frog",
    7: "horse",
    8: "ship",
    9: "truck"
}


model = joblib.load("artifacts/model.pkl")


transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])


import pandas as pd
from datetime import datetime
import os


PROD_DATA_PATH = "data/prod_data.csv"

@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    image = Image.open(file.file).convert("RGB")
    image_tensor = transform(image).unsqueeze(0)  # Préparer l'image


    from torchvision.models import resnet50, ResNet50_Weights
    weights = ResNet50_Weights.DEFAULT
    resnet = resnet50(weights=weights).eval()


    with torch.no_grad():
        embedding = resnet(image_tensor).numpy()


    predicted_class_id = model.predict(embedding)[0]
    predicted_class_name = CLASS_NAMES[predicted_class_id]

    return {
        "predicted_class_id": int(predicted_class_id),
        "predicted_class_name": predicted_class_name
    }



@app.post("/feedback")
async def feedback(file: UploadFile = File(...), target: int = Form(...)):

    image = Image.open(file.file).convert("RGB")
    image_tensor = transform(image).unsqueeze(0)


    from torchvision.models import resnet50, ResNet50_Weights
    weights = ResNet50_Weights.DEFAULT
    resnet = resnet50(weights=weights).eval()


    with torch.no_grad():
        embedding = resnet(image_tensor).numpy()


    predicted_class_id = model.predict(embedding)[0]
    predicted_class_name = CLASS_NAMES[predicted_class_id]



    data_to_save = {
        'embedding': embedding.tolist(),
        'target': [target],
        'prediction': predicted_class_id
    }

    df = pd.DataFrame(data_to_save)

    if not os.path.exists(PROD_DATA_PATH): 
        df.to_csv(PROD_DATA_PATH, index=False)
    else:
        df.to_csv(PROD_DATA_PATH, mode="a", header=False, index=False)
    return {
        "predicted_class_id": int(predicted_class_id),
        "predicted_class_name": predicted_class_name
    }

    return {"message": "Feedback enregistré"}