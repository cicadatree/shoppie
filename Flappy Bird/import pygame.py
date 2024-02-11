import pygame
import random

# initialize Pygame
pygame.init()

# set game window properties
screen_width = 288
screen_height = 512
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy Bird")

# load game assets
bg_surface = pygame.image.load('assets/background.png').convert()
bird_surface = pygame.image.load('assets/bird.png').convert_alpha()
pipe_surface = pygame.image.load('assets/pipe.png').convert_alpha()
flap_sound = pygame.mixer.Sound('assets/wing.wav')

# set game variables
gravity = 0.25
bird_velocity = 0
bird_x = 50
bird_y = screen_height / 2
pipe_speed = 4
pipe_gap = 100
pipe_x = screen_width
pipe_heights = [200, 250, 300]
score = 0
font = pygame.font.Font('assets/04B_19.ttf', 20)
game_over = False

# define function to draw score on screen
def draw_score():
    score_surface = font.render(f'Score: {score}', True, (255, 255, 255))
    score_rect = score_surface.get_rect(center=(screen_width/2, 30))
    screen.blit(score_surface, score_rect)

# define function to check for collision with pipes
def check_collision():
    if bird_y <= 0 or bird_y >= screen_height - bird_surface.get_height():
        return True
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return True
    return False

# create game loop
clock = pygame.time.Clock()
pipes = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = -8
                flap_sound.play()
        elif event.type == SPAWNPIPE:
            pipe_height = random.choice(pipe_heights)
            bottom_pipe = pipe_surface.get_rect(midtop=(pipe_x, pipe_height))
            top_pipe = pipe_surface.get_rect(midbottom=(pipe_x, pipe_height - pipe_gap))
            pipes.append(bottom_pipe)
            pipes.append(top_pipe)

    # update bird's position and velocity
    bird_velocity += gravity
    bird_y += bird_velocity
    bird_rect = bird_surface.get_rect(center=(bird_x, bird_y))

    # update pipes position and remove off-screen pipes
    pipes = [pipe for pipe in pipes if pipe.right > 0]
    for pipe in pipes:
        pipe.centerx -= pipe_speed

    # draw game assets on screen
    screen.blit(bg_surface, (0, 0))
    screen.blit(bird_surface, bird_rect)
    for pipe in pipes:
        if pipe.bottom >= screen_height:
            screen.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pipe, pipe)
    draw_score()

    # check for collision and update score
    if check_collision():
        game_over = True
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            score += 1

    # update game display
    pygame.display.update()
    clock.tick(60)

# quit Pygame
pygame.quit()
