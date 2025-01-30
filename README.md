<h1> Projet de Machine Learning dans le cadre du cours <em> Machine Learning UCBL</em></h1>
<h4>Par MOREAU Maxime, ECL 2022</h4>

<h2>Présentation de l’application</h2>

Cette application permet de classifier des images dans l’une des 10 catégories du dataset CIFAR-10, telles que des avions, des chats ou des navires. Elle propose une interface intuitive pour télécharger des images, visualiser les prédictions et comprendre la confiance du modèle. 

L’objectif est de démontrer la puissance de l’apprentissage automatique appliqué à la classification d’images, tout en offrant une expérience utilisateur simple.

<h2>Fonctionnement du modèle</h2>

Le modèle de classification est construit à partir du dataset CIFAR-10, qui contient 60 000 images réparties en 10 catégories. 

Nous utilisons un modèle ResNet pré-entraîné pour générer des embeddings, simplifiant ainsi la complexité des images brutes. 

Ces embeddings servent ensuite à entraîner un modèle de type Random Forest, qui offre des prédictions robustes. L’ensemble d’entraînement comprend 50 000 images, tandis que l’ensemble de test en contient 10 000. Cette approche hybride combine les atouts du deep learning pour l’extraction de caractéristiques et ceux du machine learning traditionnel pour la classification.

<h3> Utiliser l'application </h3>
<ul> 
<li>Télercharger une image</li>
<li>Cliquer sur <b>obtenir une prédiction</b></li>
</ul>
 

<h3>Pour obtenir envoyer un feedback</h3>
<li>Entrer la classe correct (id entre 0 et 9 avec la table de correspondance)</li>
<li>Envoyer le feedback en cliquant sur <b>Envoyer un feedback</b></li>

<h3> Afficher le rapport d'entrainement, de test et de production </h3>
<li>Cliquer sur <b> Afficher le rapport</b>
</ul>

***

<u><h2> Installer et lancer l'application </h2></u>
<h3> 🐳 Depuis l'image Docker 🐳 (conseillé)</h3>
<ul>
<li>Télécharger l'image docker : </li>
<code>docker pull maxcerise/mlproj:latest</code>
<li>Créer un container : </li> <code>docker run --name proj -d -p 8080:8080 -p 8501:8501 -p 8502:8502 maxcerise/mlproj:latest</code>
<li>Lancer l'application : </li>
<code>docker exec proj /bin/bash -c "source pyenv/bin/activate && make run"</code>
<li>Se connecter à l'application : <a>http://localhost:8501/ </a></li>
</ul>

<h2>Source Build (pas conseillé)</h2>
<i>Peut prendre beaucoup de temps</i>
<br>
<br>
Clone le repo :
<code>git clone https://github.com/MaximeCerise/mlproj.git</code>


<h3> Sur MacOS </h3>

<code>cd mlproj</code>

<code>chmod +x launch.sh</code>

Se connecter à l'application : <a>http://localhost:8501/ </a>

<h2>🪟 Sur windows 🪟</h2>

<code>cd mlproj</code>

<code>launch.bat</code>

Se connecter à l'application : <a>http://localhost:8501/ </a>
***
<h2>Dépendances</h2>
Les dépendances sont dans le fichier <b>requirements.txt</b>

<b>PS : Ne pas oublier de bien fermer le container </b>
