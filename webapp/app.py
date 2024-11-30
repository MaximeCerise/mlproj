import streamlit as st
import requests
from PIL import Image
import streamlit.components.v1 as components
import io

from litestar.plugins.flash import FlashConfig
from sympy import false


st.set_page_config(layout="wide")
st.title("Prédiction d'images avec l'API")
st.markdown("""
### Correspondances des Classes :
- **0** : Airplane
- **1** : Automobile
- **2** : Bird
- **3** : Cat
- **4** : Deer
- **5** : Dog
- **6** : Frog
- **7** : Horse
- **8** : Ship
- **9** : Truck
""")
st.text("Téléchargez une image, recevez une prédiction et donnez un feedback.")

uploaded_file = st.file_uploader("Choisissez une image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:

    image = Image.open(uploaded_file)
    st.image(image, caption="Image téléchargée", use_container_width=True)


    if st.button("Obtenir une prédiction"):

        files = {"file": uploaded_file.getvalue()}
        response = requests.post("http://localhost:8080/predict", files=files)

        if response.status_code == 200:
            prediction = response.json()
            predicted_class_id = prediction["predicted_class_id"]
            predicted_class_name = prediction["predicted_class_name"]
            st.success(f"Classe prédite : {predicted_class_name} (ID : {predicted_class_id})")
        else:
            st.error("Erreur lors de l'appel à l'API.")


    st.subheader("Donner un feedback")
    target_class = st.number_input("Entrez la classe correcte (ID)", min_value=0, max_value=9, step=1)

    if st.button("Envoyer le feedback"):

        files = {"file": uploaded_file.getvalue()}
        data = {"target": target_class}
        response = requests.post("http://localhost:8080/feedback", files=files, data=data)

        if response.status_code == 200:
            st.success("Feedback enregistré avec succès.")
        else:
            st.error("Erreur lors de l'envoi du feedback.")
import subprocess

if st.button("Afficher le rapport de production"):

    try:
        subprocess.run(["python3", "reporting/report.py"], check=True)
        st.success("Rapport généré avec succès !")
    except subprocess.CalledProcessError as e:
        st.error(f"Erreur lors de l'exécution du rapport : {str(e)}")
    else:

        html_path = "webapp/evidently_report.html"
        try:
            with open(html_path, 'r', encoding='utf-8') as HtmlFile:
                source_code = HtmlFile.read()

            components.html(source_code, height=1200, scrolling=True)
        except FileNotFoundError:
            st.error(f"Fichier HTML introuvable : {html_path}")