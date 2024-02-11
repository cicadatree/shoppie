import sys
import pygame 

#initialize pygame
pygame.init()

#initialize time
clock = pygame.time.Clock()

#dimensions for pygame.display.set_mode(())
X = 1000
Y = 1000

#create the display window 
screen = pygame.display.set_mode((X,Y))

#player position & gravity
playerY = 480
playerX = 370
playerY_change = 5 
playerX_change = 5
gravity = 5

#colours
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
red = (255, 0, 0)

#Title and Icon
pygame.display.set_caption("Little Fucking Fuckers")
icon = pygame.image.load('alien.png')
pygame.display.set_icon(icon)

#initialize the player; assign it to a rect() object 
playerImg = pygame.image.load('archer.png')
playerRect = playerImg.get_rect(topleft = (playerX, playerY))

print(playerRect)

#function that blits (draws) the playerImg on the the screen at the (X, Y) position of (playerX, playerY)
def player():
    # screen.blit() means "draw onto screen"
    screen.blit(playerImg, playerRect)

'''-------------------------------------------------------------------'''

######## MAIN GAME LOOP
mainGameLoop = True
while mainGameLoop:

    #set framerate to 60 FPS
    clock.tick(60)

    #colour the display's screen with RHB [i.e. .fill((R,G,B))]
    screen.fill(white)

    #TEST BOX for collision checking
    leftBox = pygame.Rect(50, 900, 900, 60)
    pygame.draw.rect(screen,red,leftBox)

    #event loop checking if the display window has been closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainGameLoop = False
        
    #call the player function 
    player()
    
    #apply gravity to player
    playerY = playerY + gravity

    #conditions for key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        playerY -= playerY_change
        if playerY == 0:
            playerY += playerY_change
    if keys[pygame.K_DOWN]:
        playerY += playerY_change
        if playerY == 970:
            playerY -= playerY_change
    if keys[pygame.K_LEFT]:
        playerX -= playerX_change
        if playerX == 0:
            playerX += playerX_change
    if keys[pygame.K_RIGHT]:
        playerX += playerX_change
        if playerX == 970:
            playerX -= playerX_change

    pygame.display.flip()

    #update the display with whatever is new 
    pygame.display.update()

if __name__ == '__main__':
    sys.exit()