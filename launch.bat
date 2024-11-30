@echo off

setlocal enabledelayedexpansion
if errorlevel 1 exit /b

echo Creating virtual environment...
python -m venv .venv
call .venv\Scripts\activate

echo Creating required directories...
if not exist artifacts mkdir artifacts
if not exist data mkdir data

echo Installing dependencies...
pip install -r requirements.txt

echo Downloading CIFAR-10 dataset...
python download_cifar10.py

echo generate_embeddings
python generate_embeddings.py

echo Training model...
python train_model.py

echo Starting Uvicorn server on port 8080...
start cmd /k "uvicorn serving.api:app --reload --host 0.0.0.0 --port 8080"

echo Starting Streamlit server on port 8502...
start cmd /k "streamlit run webapp/app.py --server.port 8502"

echo All servers are running. Press Ctrl+C in their respective windows to stop them.
pause