import pygame
import numpy as np


class GameOfLife


def window():

    # Initialize Pygame
    pygame.init()

    # set the window dimensions
    window_size = (800, 600)

    # create the window
    window = pygame.display.set_mode(window_size)

    # Set the window title
    pygame.display.set_caption('Conway\'s Game of Life')

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # update game state below:

        # render game state below:

        # update the dispaly
        pygame.display.flip()

    pygame.quit()

window()