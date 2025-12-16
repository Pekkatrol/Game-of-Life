grid_size = 60      # Taille de la grille (nombre de cellules par ligne/colonne)
cell_size = 15           # Taille de chaque cellule en pixels
initial_live_cells = 500  # Nombre de cellules vivantes dans la génération initiale
frameS = 5

# Initialiser la grille
grid = []

def setup():
    global grid,frameS
    size(grid_size * cell_size, grid_size * cell_size)
    grid = create_blank_grid(grid_size)
    generate_initial_generation(grid, initial_live_cells)
    frameRate(frameS)  # Régler la vitesse d'animation (générations par seconde)

def draw():
    global grid
    background(255)
    display_grid(grid)
    grid = next_generation(grid)

class Cellule:
    def __init__(self, x, y, state):
        self.x = x
        self.y = y
        self.state = state

    # Compte les voisins vivants autour de cette cellule
    def count_living_neighbors(self, grid):
        if self.x == 0:
            neighbors = [ ( grid_size,-1),(grid_size, 0), (grid_size, 1), 
                              (0, -1),                        (0, 1),
                              (1, -1),       (1, 0),          (1, 1)
                              ]
        elif self.x == grid_size:
            neighbors = [ ( -1,-1),     (-1, 0),        (-1, 1), 
                           (0, -1),                       (0, 1),
                        (-grid_size, -1),(-grid_size, 0),(-grid_size, 1)
                              ]
        elif self.y == 0:
            neighbors = [ ( -1,grid_size),(-1, 0),(-1, 1), 
                          (0, grid_size),         (0, 1),
                          (1, grid_size),(1, 0), (1, 1)
                          ]
        
        elif self.y == grid_size:
            neighbors = [ ( -1,-1),(-1, 0),(-1, -grid_size), 
                          (0, -1),         (0, -grid_size),
                          (1, -1),(1, 0), (1, -grid_size)
                          ]
        else:
            neighbors = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),          (0, 1),
            (1, -1), (1, 0), (1, 1)
            ]
        count = 0
        
        for dx, dy in neighbors:
            nx, ny = self.x + dx, self.y + dy
            if 0 <= nx < grid_size and 0 <= ny < grid_size:
                if grid[ny][nx].state:
                    count += 1
        return count

# Créer une grille vide avec toutes les cellules mortes
def create_blank_grid(n):
    return [[Cellule(x, y, False) for x in range(n)] for y in range(n)]

# Générer une génération initiale avec des cellules vivantes aléatoires
def generate_initial_generation(grid, num_cells):
    from random import randint
    for _ in range(num_cells):
        x = randint(0, grid_size - 1)
        y = randint(0, grid_size - 1)
        while grid[y][x].state:  # S'assurer de ne pas créer de doublon
            x = randint(0, grid_size - 1)
            y = randint(0, grid_size - 1)
        grid[y][x].state = True

# Calculer la génération suivante
def next_generation(grid):
    new_grid = create_blank_grid(grid_size)
    
    for y in range(grid_size):
        for x in range(grid_size):
            current = grid[y][x]
            neighbors = current.count_living_neighbors(grid)
            
            # Appliquer les règles du jeu
            if current.state:
                new_grid[y][x].state = (neighbors == 2 or neighbors == 3)
            else:
                new_grid[y][x].state = (neighbors == 3)
    
    return new_grid

# Afficher la grille graphique
def display_grid(grid):
    for y in range(grid_size):
        for x in range(grid_size):
            if grid[y][x].state:
                fill(0)  # Cellule vivante (noire)
            else:
                fill(255)  # Cellule morte (blanche)
            stroke(200)  # Couleur des bordures de cellules
            rect(x * cell_size, y * cell_size, cell_size, cell_size)
