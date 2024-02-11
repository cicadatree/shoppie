import pygame as pg
import random

# Initialize pg
pg.init()

# Set up the game windowackgroundColour
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
backgroundSpeed = 1

# load the game assets
birdRect = pg.Rect(birdX, birdY, birdSize, birdSize)
birdColour = pg.Color (255, 255, 0)
pipeRect = pg.Rect(0, 0, pipeWidth, 0)
pipeColour = pg.Color(0, 255, 0)
backgroundRect = pg.Rect(0, 0, windowWidth, windowHeight)
backgroundColour = pg.Color(0, 0, 255)

clock = pg.time.Clock()
score = 0
pipes = []
backgroundX = 0

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                birdRect.top -= birdSize * 2

    birdRect.top += pipeSpeed

    for pipe in pipes:
        pipe.left -= pipeSpeed
    if pipes and pipes[0].left < -pipeWidth:
        pipes.pop(0)
        score += 1
    if not pipes or windowWidth - pipes[-1].right > pipeGapSize:
        gap_top = random.randint(birdSize * 4, windowHeight - birdSize * 4 - pipeGapSize)
        pipe_top = pg.Rect(windowWidth, 0, pipeWidth, gap_top - pipeGapSize // 2)
        pipe_bottom = pg.Rect(windowWidth, gap_top + pipeGapSize // 2, pipeWidth, windowHeight - gap_top - pipeGapSize // 2)
        pipes.append(pipe_top)
        pipes.append(pipe_bottom)

    # Scroll the background
    backgroundX -= backgroundSpeed
    if backgroundX < -windowWidth:
        background_x = 0

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                birdRect.top -= birdSize * 2

    # Check for collisions
    if birdRect.top < 0 or birdRect.bottom > windowHeight:
        running = False
    for pipe in pipes:
        if birdRect.colliderect(pipe):
            running = False

    # Draw the game elements
    screen.fill(backgroundColour)
    for pipe in pipes:
        pg.draw.rect(screen, pipeColour, pipe)
    pg.draw.rect(screen, birdColour, birdRect)
    pg.draw.rect(screen, backgroundColour, backgroundRect.move(backgroundX, 0))
    pg.display.set_caption(f"Flappy Bird - Score: {score}")
    pg.display.update()

    # Set the game's frame rate
    clock.tick(60)

# Quit pg
pg.quit()
