#checkers

import pygame
import sys

block_size = 20
GREY = (180, 180, 180)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WINDOW_HEIGHT = 800
WINDOW_WIDTH = 800

def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(WHITE)

    while True:
        drawGrid()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update() 

def drawGrid():
    blockSize = 100
    cnt = 0
    for i in range()
    
    
    
    '''
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range (0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, BLACK, rect, 1)
'''
class Container:
    def __init__(self, height, width):
            self.height = height
            self.width = width

main()