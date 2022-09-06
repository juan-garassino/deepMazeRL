import numpy as np
from deepMazeRL.params import *

def generate_maze(m, n, density=DENSITY):
    maze = np.random.choice([CODE_EMPTY, CODE_HOLE], m * n, p=[1.0 - density, density]).reshape((m, n))
    maze[m - 2, n - 2] = CODE_TREASURE
    maze[INITIAL_POSITION] = CODE_EMPTY
    for i in range(m):
        maze[i, 0] = CODE_HOLE
        maze[i, n - 1] = CODE_HOLE
    for j in range(n):
        maze[0, j] = CODE_HOLE
        maze[m - 1, j] = CODE_HOLE
    flip_horizontal = np.random.choice([-1, 1])
    flip_vertical = np.random.choice([-1, 1])
    
    return maze[::flip_horizontal, ::flip_vertical]

def show_maze(maze, position):
    s = ""
    convert = {CODE_EMPTY: '_', CODE_HOLE: 'X', CODE_TREASURE: '$'}
    for height in range(maze.shape[1]):
        for width in range(maze.shape[0]):
            if (width, height) == position:
                s += "8"
            else:
                s += convert[maze[width, height]]
        s += '\n'
    print(s)