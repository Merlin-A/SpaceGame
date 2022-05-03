import pygame
import random

pygame.init()
# Create the Screen
screen = pygame.display.set_mode((800, 600))

# Title & Icon
pygame.display.set_caption('Space Invader')
icon = pygame.image.load('./img/ufo.png')

pygame.display.set_icon(icon)

# Player

playerImg = pygame.image.load('./img/space-invaders.png')

o_X = 370
o_Y = 480

playerX = 370
playerY = 480

playerX_change = 0

playerY_change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


# Enemy

enemyImage = pygame.image.load('./img/alien.png')
enemy_X = random.randint(0, 736)
enemy_Y = random.randint(50, 250)
enemyX_change = 0.2
enemyY_change = 40


def enemy(x, y):
    screen.blit(enemyImage, (x, y))


# BackGround Image

bcImage = pygame.image.load('./img/space.jpg')

# Bullet
# Ready state - You can't see the bullet on the screen
# Fire - The Bullet is currently moving

bulletImg = pygame.image.load('./img/bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 0.5
bullet_state = "ready"


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 20, y - 20))


# Game Loop


running = True

while running:
    screen.blit(bcImage, (0, 0))

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

            if event.key == pygame.K_r and pygame.KMOD_CTRL:
                playerX = o_X
                playerY = o_Y

            if event.key == pygame.K_SPACE:
                fire_bullet(playerX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Doing this helps in making the cursor flow,
    # as the values of playerX is updated in a while loop
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0

    elif playerX > 736:
        playerX = 736

    player(playerX, playerY)

    # Enemy

    enemy_X += enemyX_change

    if enemy_X <= 0:
        enemyX_change = 0.2
        enemy_Y += enemyY_change

    elif enemy_X > 736:
        enemyX_change = -0.2
        enemy_Y += enemyY_change

    # Bullet Movement

    if bulletY <= 0:
        bullet_state = "ready"
        bulletY = 480

    if bullet_state == "fire":

        fire_bullet(playerX, bulletY)
        bulletY -= bulletY_change

    enemy(enemy_X, enemy_Y)

    pygame.display.update()
