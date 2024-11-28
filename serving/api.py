from fastapi import FastAPI, UploadFile, File
import pandas as pd
import joblib
from PIL import Image
from torchvision import transforms
import numpy as np
import torch
# Initialisation de l'application FastAPI
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

# Charger le modèle et le scaler
model = joblib.load("../artifacts/model.pkl")

# Transformation pour les images (comme pour ResNet)
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# Endpoint de prédiction
import pandas as pd
from datetime import datetime
import os

# Chemin vers prod_data.csv
PROD_DATA_PATH = "../data/prod_data.csv"

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # Charger l'image
    image = Image.open(file.file).convert("RGB")
    image_tensor = transform(image).unsqueeze(0)  # Préparer l'image

    # Charger ResNet pour les embeddings
    from torchvision.models import resnet50, ResNet50_Weights
    weights = ResNet50_Weights.DEFAULT
    resnet = resnet50(weights=weights).eval()

    # Générer l'embedding
    with torch.no_grad():
        embedding = resnet(image_tensor).numpy()

    # Prédire la classe
    predicted_class_id = model.predict(embedding)[0]
    predicted_class_name = CLASS_NAMES[predicted_class_id]

    # Sauvegarder la prédiction dans prod_data.csv
    data_to_save = {
        "timestamp": [datetime.now().isoformat()],
        "embedding": [embedding.tolist()],
        "predicted_class_id": [int(predicted_class_id)],
        "predicted_class_name": [predicted_class_name]
    }

    # Convertir en DataFrame et append au fichier
    df = pd.DataFrame(data_to_save)
    if not os.path.exists(PROD_DATA_PATH):  # Créer le fichier s'il n'existe pas
        df.to_csv(PROD_DATA_PATH, index=False)
    else:
        df.to_csv(PROD_DATA_PATH, mode="a", header=False, index=False)

    return {
        "predicted_class_id": int(predicted_class_id),
        "predicted_class_name": predicted_class_name
    }

# Endpoint de feedback
@app.post("/feedback")
async def feedback(file: UploadFile = File(...), true_label: int = 0):
    # Charger l'image et générer l'embedding
    image = Image.open(file.file).convert("RGB")
    image_tensor = transform(image).unsqueeze(0)
    from torchvision.models import resnet50, ResNet50_Weights
    weights = ResNet50_Weights.DEFAULT
    resnet = resnet50(weights=weights).eval()
    with torch.no_grad():
        embedding = resnet(image_tensor).numpy()

    # Ajouter au dataset de production
    prod_data_path = "../data/prod_data.csv"
    new_data = pd.DataFrame([np.append(embedding, true_label)])
    new_data.to_csv(prod_data_path, mode="a", header=False, index=False)

    return {"message": "Feedback enregistré"}