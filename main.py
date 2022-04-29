
import pygame


pygame.init()
# Create the Screen
screen = pygame.display.set_mode((800, 600))

# Title & Icon
pygame.display.set_caption('Space Invader')
icon = pygame.image.load('./img/ufo.png')
pygame.display.set_icon(icon)

# Player

playerImg = pygame.image.load('./img/space-invaders.png')
playerX = 370
playerY = 480


def player():
    screen.blit(playerImg, (playerX, playerY))


# Game Loop


running = True

while running:

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Quitting Program")
            running = False

    player()

    pygame.display.update()







