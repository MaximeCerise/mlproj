# Utiliser une image Python légère
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY ..

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Exposer les ports nécessaires
EXPOSE 8080 8502

# Commande de démarrage
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8080"]