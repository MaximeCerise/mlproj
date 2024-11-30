#!/bin/bash
set -e

python3 -m venv .venv
source .venv/bin/activate

mkdir -p artifacts
mkdir -p data

pip install -r requirements.txt

python3 download_cifar10.py
python3 generate_embeddings.py
python3 train_model.py

echo "Starting Uvicorn server on port 8080..."
uvicorn serving.api:app --reload --host 0.0.0.0 --port 8080 &
echo "Starting Streamlit server on port 8502..."
streamlit run webapp/app.py --server.port 8502 &

wait