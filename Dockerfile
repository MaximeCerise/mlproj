# Utiliser une image Ubuntu comme base
FROM ubuntu:latest

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Mise à jour des paquets et installation de Python + pip
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    curl \
    unzip && \
    rm -rf /var/lib/apt/lists/*

RUN apt-get install make
# Création et configuration d'un environnement virtuel
RUN python3 -m venv /app/pyenv

# Activer l'environnement virtuel et installer pip dans une couche séparée pour maximiser le cache
RUN /app/pyenv/bin/pip install --upgrade pip

# Copier uniquement le fichier requirements.txt pour installer les dépendances en premier
COPY requirements.txt /app/requirements.txt

# Installer les dépendances Python
RUN /app/pyenv/bin/pip install -r /app/requirements.txt

# Copier le reste de l'application dans le conteneur
COPY . /app/

RUN unzip model.pkl.zip -d temp_dir && mkdir -p artifacts && cp -r temp_dir/* artifacts/ && rm -rf temp_dir

RUN cd artifacts && ls

RUN export STREAMLIT_BROWSER_GATHERUSAGESTATS=false
# Activer l'environnement virtuel par défaut et exécuter une commande
CMD ["sh", "-c", "tail -f /dev/null"]