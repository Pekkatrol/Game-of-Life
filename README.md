# Game of Life — Processing (mode Python)

Une implémentation du célèbre "Conway's Game of Life" écrite pour Processing en mode Python.

Ce dépôt contient un sketch Processing (Python mode). Pour exécuter le projet vous devez lancer le sketch depuis l'IDE Processing en ayant activé le mode Python.

## Aperçu
Conway's Game of Life est un automate cellulaire où des cellules vivantes meurent ou naissent selon le nombre de voisins. Ce sketch vous permet de :
- lancer la simulation,
- régler la vitesse, effectuer des pas à pas et randomiser la grille.

## Prérequis

- Processing ( — téléchargez depuis https://processing.org/download/
- Python Mode pour Processing (processing.py)
  - Ouvrez Processing → Tools → Add Tool...
  - Dans l'onglet "Modes", installez "Python Mode" (ou "Python" / "processing.py").
  - Après installation, sélectionnez le mode Python dans la liste déroulante en haut à droite de l'IDE.

## Installation et exécution

1. Clonez le dépôt :
   ```
   git clone https://github.com/Pekkatrol/Game-of-Life.git
   ```
2. Ouvrez le sketch principal (.py) dans l'IDE Processing :
   - File → Open... → ouvrez le fichier `jeu_de_la_vie.pyde`.
3. En haut à droite de l'IDE, choisissez le mode "Python".
4. Appuyez sur le bouton Run (ou Ctrl/Cmd+R).

## Paramètres modifiables

Dans le haut du fichier principal vous trouverez probablement des constantes/modèles pour :
- taille de la grille (rows, cols)
- taille d'une cellule (cell_size)
- vitesse initiale (updates per second / frameRate)

Modifiez ces valeurs puis relancez le sketch pour tester différents comportements.

## Règles du jeu (rappel rapide)

Pour chaque cellule à chaque itération :
- Une cellule vivante avec moins de 2 voisins vivants meurt (sous-population).
- Une cellule vivante avec 2 ou 3 voisins vivants survit.
- Une cellule vivante avec plus de 3 voisins vivants meurt (surpopulation).
- Une cellule morte avec exactement 3 voisins vivants devient vivante (naissance).

## Crédits

Basé sur la règle originale de John Conway — implémenté ici pour Processing en mode Python.
Ceci est un projet réalisé en binôme avec Théo D. en terminale au lycée Masséna.
