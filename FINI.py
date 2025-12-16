from random import randint

class Cellule:
    def __init__(self, y: int, x: int, state: bool):
        self.x = x
        self.y = y
        self.state = state

    def __repr__(self):
        return f"({self.state},{self.x},{self.y})"

    def etat(self):
        return self.state == True

    def changeState(self):
        self.state = not self.state  # Inverse l'état

    def compter_voisins_vivants(self, grid):
        # Compter le nombre de voisins vivants autour de la cellule (self.x, self.y)
        voisins = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),         (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        compte = 0
        for dx, dy in voisins:
            nx, ny = self.x + dx, self.y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid):
                if grid[ny][nx].state:
                    compte += 1
        return compte

# Générer un grid avec des cellules mortes
def generateurBlankGrid(n):
    grid = []
    for i in range(n):
        row = []
        for j in range(n):
            c = Cellule(i, j, False)
            row.append(c)
        grid.append(row)
    return grid

# Générer des cellules vivantes pour la génération 0
def genererGeneration0(combien: int, grid: list):
    for _ in range(combien):
        genererCellule(grid)
    return grid

# Générer une seule cellule vivante sans doublon
def genererCellule(grid: list):
    x, y = randint(0, len(grid) - 1), randint(0, len(grid) - 1)
    while grid[y][x].state:  # Tant qu'on trouve une cellule vivante, on continue
        x, y = randint(0, len(grid) - 1), randint(0, len(grid) - 1)
    grid[y][x].state = True

# Calculer la prochaine génération
def prochaineGeneration(grid: list):
    # Créer une nouvelle grille pour stocker les états mis à jour
    newGrid = generateurBlankGrid(len(grid))
    for y in range(len(grid)):
        for x in range(len(grid)):
            cellule_actuelle = grid[y][x]
            voisins_vivants = cellule_actuelle.compter_voisins_vivants(grid)

            # Appliquer les règles du jeu
            if cellule_actuelle.state:  # Si la cellule est vivante
                if voisins_vivants < 2 or voisins_vivants > 3:
                    newGrid[y][x].state = False  # Meurt
                else:
                    newGrid[y][x].state = True  # Reste vivante
            else:  # Si la cellule est morte
                if voisins_vivants == 3:
                    newGrid[y][x].state = True  # Devient vivante
    return newGrid

# Afficher la grille de manière lisible
def afficher_grille(grid: list):
    for row in grid:
        print(" ".join(["1" if cell.state else "0" for cell in row]))
    print()

#//////////////////////////////////////////////////////////////////////////////

# Initialisation du jeu
grid = generateurBlankGrid(9)
grid = genererGeneration0(8, grid)

# Afficher la grille initiale
print("Grille initiale :")
afficher_grille(grid)

# Simuler les générations
for i in range(3):
    print(f"Génération {i + 1} :")
    grid = prochaineGeneration(grid)
    afficher_grille(grid)
