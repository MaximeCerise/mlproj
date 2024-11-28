import streamlit as st
import requests
from PIL import Image
import io

# Configuration de la page
st.title("Prédiction d'images avec l'API ML")
st.text("Téléchargez une image et recevez la classe prédite.")

# Téléchargement de l'image
uploaded_file = st.file_uploader("Choisissez une image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Afficher l'image téléchargée
    image = Image.open(uploaded_file)
    st.image(image, caption="Image téléchargée", use_column_width=True)

    # Bouton pour envoyer la prédiction
    if st.button("Obtenir une prédiction"):
        # Envoi de l'image à l'API
        files = {"file": uploaded_file.getvalue()}
        response = requests.post("http://localhost:8080/predict", files=files)

        if response.status_code == 200:
            prediction = response.json()
            predicted_class_id = prediction["predicted_class_id"]
            predicted_class_name = prediction["predicted_class_name"]
            st.success(f"Classe prédite : {predicted_class_name} (ID : {predicted_class_id})")
        else:
            st.error("Erreur lors de l'appel à l'API.")
