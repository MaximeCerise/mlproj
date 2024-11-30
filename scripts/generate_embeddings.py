import torch
from torchvision import transforms
from torchvision.datasets import CIFAR10
from torch.utils.data import DataLoader
import pandas as pd
from torchvision.models import resnet50, ResNet50_Weights
import json


weights = ResNet50_Weights.DEFAULT
resnet = resnet50(weights=weights)
resnet.eval()


device = torch.device("mps") if torch.backends.mps.is_available() else torch.device("cpu")
resnet = resnet.to(device)


transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])


dataset = CIFAR10(root="data", train=True, transform=transform, download=True)
dataloader = DataLoader(dataset, batch_size=32, shuffle=False)

embeddings = []
labels = []


with torch.no_grad():
    for images, targets in dataloader:
        images = images.to(device)  
        features = resnet(images)
        embeddings.extend(features.cpu().numpy().tolist())  
        labels.extend(targets.numpy())


df = pd.DataFrame({
    'embedding': [json.dumps(embedding) for embedding in embeddings],  
    'target': labels
})


df.to_csv("data/cifar10_emb.csv", index=False)

print("Embeddings générés et sauvegardés dans ML_deployement/data/ref_data.csv")