# Projet Python : Feux d'Artifice Géométriques

Ce projet graphique a été développé en Python en utilisant la bibliothèque interactive `turtle` ainsi que le module `random`. Il simule des explosions de feux d'artifice sous forme de motifs géométriques et radiaux, mettant en pratique des concepts clés de la programmation modulaire.
## Concepts de programmation appliqués

* **Initialisation et personnalisation de l'environnement :** Le programme configure un espace de travail visuel avec un fond noir profond (`bgcolor("black")`) pour accentuer l'effet lumineux, couplé à une vitesse d'exécution maximale (`t.speed(0)`) permettant un rendu instantané.
* **Modularité et réutilisabilité du code :** Le dessin complexe est encapsulé dans une fonction dédiée (`dessiner_feu_artifice(x, y, rayon_max)`). Cela permet de répéter l'opération à différentes coordonnées sans dupliquer les lignes de code.
* **Gestion de l'aléa (`random`) :** Le module `random` est utilisé pour sélectionner de manière dynamique et imprévisible les couleurs de chaque feu d'artifice parmi une palette prédéfinie de teintes vives.
* **Boucles de répétition et géométrie circulaire :** Une boucle `for` s'exécutant 36 fois pilote les déplacements de la tortue. À chaque itération, un angle de rotation fixe de 10 degrés est appliqué (`t.left(10)`), couvrant ainsi les 360 degrés d'un cercle complet pour dessiner les rayons de l'explosion.
* **Gestion de la fenêtre graphique :** La méthode finale `turtle.done()` permet de figer le résultat à l'écran afin de l'analyser ou de le présenter.