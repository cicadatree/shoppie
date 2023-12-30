'''
Conway's Game of Life

The universe of the game is an infinite, 
two-dimensional orthogonal grid of square cells,
each of which is in one of two possible states - live or dead.

Every cell interacts with it's eight neighbours - the cells that are
horizantally, vertically, or diagonally adjacent.

At each step in time, the following transitions occur:

1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

The initial pattern constitutes the seed of the system.
The first generation is created by applying the above rules simultaneously
to every cell in the seed, live or dead; births and deaths occur simultaneously,
and the discrete momebnt at which this happens is sometings c
alled a tick. 

Each generation is a pure function of the preceding one. 
The rules continue to be applied repeatedly to create further generations.
'''

import pygame
import numpy as np

def get_heat_color(heat_level):
    # This function returns a color based on the heat level.
    # You can modify this function to use your preferred color gradient.
    if heat_level > 10:
        return (255, 0, 0)  # Hottest: Red
    elif heat_level > 7:
        return (255, 69, 0)  # Hotter: Dark Orange
    elif heat_level > 4:
        return (255, 165, 0)  # Hot: Orange
    elif heat_level > 1:
        return (255, 255, 0)  # Warm: Yellow
    else:
        return (0, 0, 0)  # No heat: Black


class GameOfLife:
    def __init__(self, size):
        self.size = size
        self.grid = np.zeros((self.size, self.size), dtype=int)
        self.heat_map = np.zeros((self.size, self.size), dtype=int)  # Heat map array

    def toggle_cell(self, row, col):
        self.grid[row, col] = 1 - self.grid[row, col]

    def update(self):
        new_grid = self.grid.copy()

        for row in range(self.size):
            for col in range(self.size):
                state = self.grid[row, col]
                neighbours = self.count_neighbours(row, col)

                if state == 0 and neighbours == 3:
                    # Dead cell with exactly 3 live neighbours becomes alive
                    new_grid[row, col] = 1
                elif state == 1 and (neighbours < 2 or neighbours > 3):
                    # Live cell with fewer than 2 or more than 3 lives nieghbours dies
                    new_grid[row, col] = 0
                    self.heat_map[row, col] += 1  # Increment heat level

        self.grid = new_grid

    def render(self, window : pygame.Surface):
        cell_size = window.get_width() // self.size
        for row in range(self.size):
            for col in range(self.size):
                color = get_heat_color(self.heat_map[row, col]) if self.grid[row, col] == 0 else (255, 255, 255)
                pygame.draw.rect(window, color, (col*cell_size, row*cell_size, cell_size, cell_size))

    def count_neighbours(self, row, col):
        # count the number of live nieghbours around a given cell
        total = 0 
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                new_row, new_col = row + i, col + j
                if 0 <= new_row < self.size and 0 <= new_col < self.size:
                    total += self.grid[new_row, new_col]
        return total

    def resize_grid(self, new_size):
        self.size = new_size
        self.grid = np.zeros((self.size, self.size), dtype=int)


def set_initial_seed(game : GameOfLife, window : pygame.Surface):
    seeding = True
    mouse_pressed = False # Variable to track the mouse button state
    cell_size = window.get_width() // game.size

    while seeding:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                seeding = False
                pygame.quit()
                exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pressed = True # Mouse button is pressed
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_pressed = False # Mouse button is released
            elif event.type == pygame.MOUSEMOTION:
                if mouse_pressed:
                    # get mouse position and convert to grid coordinates 
                    x, y = pygame.mouse.get_pos()
                    row, col = y // cell_size, x // cell_size
                    game.toggle_cell(row, col)

                    #render the updated grid
                    window.fill((0,0,0))
                    game.render(window)
                    pygame.display.flip()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    seeding = False

    window.fill((0, 0, 0))
    pygame.display.flip()

def reset_game(game : GameOfLife, window  : pygame.display):
    # reset the game state and enter seed mode
    game.grid = np.zeros((game.size, game.size), dtype=int) # reset the grid
    set_initial_seed(game, window) # enters seed mode

def window():
    pygame.init() # Initialize Pygame
    pygame.display.set_caption('Conway\'s Game of Life') # Set the window title
    window_size = (1600, 1200) # set the window dimensions
    game = GameOfLife(min(window_size)//10)
    window = pygame.display.set_mode(window_size, pygame.RESIZABLE) # create the window

    set_initial_seed(game, window) #set the initial seed

    running = True
    tick_count = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                tick_count = tick_count + 1
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                reset_game(game, window)
            elif event.type == pygame.VIDEORESIZE:
                window_size = event.size
                window = pygame.display.set_mode(window_size, pygame.RESIZABLE)
                new_grid_size = min(window_size) // 10
                game.resize_grid(new_grid_size)

        # update game state below:
        game.update()

        # render game state below:
        window.fill((0, 0, 0)) # clear screen
        game.render(window)

        # update the dispaly
        pygame.display.flip()
        pygame.time.delay(1) 

    pygame.quit()

if __name__ == "__main__":
    window()