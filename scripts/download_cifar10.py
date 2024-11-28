import torchvision.transforms as transforms
from torchvision.datasets import CIFAR10

transform = transforms.Compose([
    transforms.ToTensor()
])

dataset = CIFAR10(root="../data", train=True, download=True, transform=transform)
print("Dataset CIFAR-10 téléchargé dans le dossier ./data")