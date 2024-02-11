import pygame
pygame.init()

#set color with rgb
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

#set display
gameDisplay = pygame.display.set_mode((800,600))

#caption
pygame.display.set_caption("ChessBoard")

size = 20
white=(0,0,0)
boardLength = 8
gameDisplay.fill(white)

def main():

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        cnt = 0
        for i in range(1,boardLength+1):
            for z in range(1,boardLength+1):
                if cnt % 2 == 0:
                    pygame.draw.rect(gameDisplay, white, [size*z,size*i,size,size])
                else:
                    pygame.draw.rect(gameDisplay, black, [size*z,size*i,size,size])
                cnt +=1
            cnt -=1
        pygame.draw.rect(gameDisplay,black,[size,size,boardLength*size,boardLength*size],1)

        pygame.display.update()

main()