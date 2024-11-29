<h1> MOREAU Maxime</h1>
<h1> Projet de Machine Learning dans le cadre du cours <em> Machine Learning UCBL</em>


<h1> From Docker Image </h1>
<ul>
<li>Télécharger l'image docker : docker pull maxcerise/mlproj:latest</li>
<li>Créer un container : docker run --name proj -d -p 8080:8080 -p 8501:8501 -p 8502:8502 maxcerise/mlproj:latest</li>
<li>Lancer l'application : docker exec proj /bin/bash -c "source pyenv/bin/activate && make run"</li>
<li>Se connecter à l'application : <a>http://localhost:8501/ </a></li>
</ul>


<h1>Source Build</h1>
<h2> Launch app with : </h2>
source .venv/bin/activate
streamlit run webapp/app.py --server.port 8502

<h2>Launch api with : </h2>
source .venv/bin/activate
uvicorn serving.api:app --reload --host 0.0.0.0 --port 8080
<h2> Connect to the application : </h2>
<a>http://localhost:8501/</a>

<h2>Dépendances</h2>
Les dépendances sont dans le fichier requirements (bibliothèques python à télécharger sur pip).


