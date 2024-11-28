import torch
from torchvision import models, transforms
from torchvision.datasets import CIFAR10
from torch.utils.data import DataLoader
import pandas as pd

# Charger ResNet préentraîné
from torchvision.models import resnet50, ResNet50_Weights

weights = ResNet50_Weights.DEFAULT
resnet = resnet50(weights=weights)
resnet.eval()

# Si GPU Metal est disponible, basculer sur le GPU
device = torch.device("mps") if torch.backends.mps.is_available() else torch.device("cpu")
resnet = resnet.to(device)

# Transformation pour ResNet
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# Charger CIFAR-10
dataset = CIFAR10(root="./data", train=True, transform=transform, download=False)
dataloader = DataLoader(dataset, batch_size=32, shuffle=False)

embeddings = []
labels = []

# Générer les embeddings
with torch.no_grad():
    for images, targets in dataloader:
        images = images.to(device)  # Envoie les images sur le GPU
        features = resnet(images)
        embeddings.append(features.cpu().numpy())  # Récupère les résultats sur le CPU
        labels.extend(targets.numpy())

# Sauvegarder dans un fichier CSV
embeddings_flat = [item for sublist in embeddings for item in sublist]  # Aplatir la liste
df = pd.DataFrame(embeddings_flat)
df['label'] = labels
df.to_csv("../data/ref_data.csv", index=False)

print("Embeddings générés et sauvegardés dans ML_deployement/data/ref_data.csv")