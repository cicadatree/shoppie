import pygame as pg

# Initialize pg
pg.init()

# Set up the game window
windowWidth = 640
windowHeight = 480
screen = pg.display.set_mode((windowWidth, windowHeight))
pg.display.set_caption("Flappy Bird")

# Define the game element sizes and positions
birdSize = 20
birdX = windowWidth // 3
birdY = windowHeight // 2
pipeWidth = 50
pipeGapSize = 100
pipeSpeed = 2
backgroundColour = 1

# load the game assets
birdRect = pg.Rect(birdX, birdY, birdSize, birdSize)
birdColour = pg.Color (255, 255, 0)
pipeRect = pg.Rect(0, 0, pipeWidth, 0)
pipeColour = pg.Color(0, 255, 0)
backgroundRect = pg.Rect(0, 0, windowWidth, windowHeight)
backgroundColour = pg.Color(0, 0, 255)
