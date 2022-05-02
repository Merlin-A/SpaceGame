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

playerX_change = 0
playerY_change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


# Game Loop


running = True

while running:

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Quitting Program")
            running = False

        # if keystroke is pressed check whether its right of left

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                playerX_change = -0.5

            if event.key == pygame.K_RIGHT:
                playerX_change = 0.5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Doing this helps in making the cursor flow,
    # as the values of playerX is updated in a while loop
    playerX += playerX_change

    if playerX < 0:
        playerX = 0

    elif playerX > 725:
        playerX = 725

    player(playerX, playerY)

    pygame.display.update()
