import sys
import pygame

# Initialize the Pygame window.
pygame.init()
screen = pygame.display.set_mode((800, 600))

# create the player object
player = pygame.Rect(200, 200, 50, 50)

# create the enemy objects
enemies = []
for i in range(10):
    enemies.append(pygame.Rect(i * 100, 0, 50, 50))

# create the bullets objects
bullets = []

# add a background image
background = pygame.image.load("background.png")

# add a sound effect for when the player shoots.
shoot_sound = pygame.mixer.Sound(r"C:Users\brend\python projectstop_down_shooter\shoot.mp3")

# add a sound effect for when the player is hit.
hit_sound = pygame.mixer.Sound("enemy_hitmarker.mp3")

# add a game loop that controls the flow of the game.
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

     # Update the player position.
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        player.x -= 5
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        player.x += 5
    if pygame.key.get_pressed()[pygame.K_UP]:
        player.y -= 5
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        player.y += 5

    # Update the enemy positions.
    for enemy in enemies:
        enemy.x += 1

    # Update the bullet positions.
    for bullet in bullets:
        bullet.y -= 5

    # Check for collisions between the player and the enemies.
    for enemy in enemies:
        if enemy.colliderect(player):
            hit_sound.play()
            break

    # Check for collisions between the bullets and the enemies.
    for bullet in bullets:
        for enemy in enemies:
            if bullet.colliderect(enemy):
                enemies.remove(enemy)
                bullets.remove(bullet)
                shoot_sound.play()
                break

    # Draw the background image.
    screen.blit(background, (0, 0))

    # Draw the player object.
    pygame.draw.rect(screen, (255, 0, 0), player)

    # Draw the enemy objects.
    for enemy in enemies:
        pygame.draw.rect(screen, (0, 0, 255), enemy)

    # Draw the bullet objects.
    for bullet in bullets:
        pygame.draw.circle(screen, (255, 255, 0), bullet.center, 5)

    # Update the display.
    pygame.display.update()



