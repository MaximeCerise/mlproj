import subprocess
import os

# Lancer l'API
api_process = subprocess.Popen(["python3", "serving/api.py"])
print("API lancée...")

# Lancer l'application Streamlit
streamlit_process = subprocess.Popen(["streamlit", "run", "webapp/app.py"])
print("Application Streamlit lancée...")

# Maintenir les processus actifs
try:
    api_process.wait()
    streamlit_process.wait()
except KeyboardInterrupt:
    print("Arrêt des applications...")
    api_process.terminate()
    streamlit_process.terminate()