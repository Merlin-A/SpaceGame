import pygame
import random
import math

# TODO: Make a single Bullet which comes from the back
# TODO : Make a single Missile to fire with Shift + Space and let it track the enemy

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


# Score

score_value = 0
font = pygame.font.SysFont("Britannic Bold", 32)
textX = 10
textY = 10


def showScore(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


# Enemy
enemyImage = []
enemy_X = []
enemy_Y = []
enemyX_change = []
enemyY_change = []
num_of_enemies = int(input("Enter the Number of Enemies -> "))

for i in range(num_of_enemies):
    enemyImage.append(pygame.image.load('./img/alien.png'))
    enemy_X.append(random.randint(0, 735))
    enemy_Y.append(random.randint(50, 250))
    enemyX_change.append(0.2)
    enemyY_change.append(40)


def enemy(x, y, i):
    screen.blit(enemyImage[i], (x, y))


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


# Collision Function

def isCollision(enemy_X, enemy_Y, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemy_X - bulletX, 2)) + (math.pow(enemy_Y - bulletY, 2)))

    if distance <= 32:
        return True
    else:
        return False


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
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

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

    for i in range(num_of_enemies):

        enemy_X[i] += enemyX_change[i]

        if enemy_X[i] <= 0:
            enemyX_change[i] = 0.2
            enemy_Y[i] += enemyY_change[i]

        elif enemy_X[i] > 736:
            enemyX_change[i] = -0.2
            enemy_Y[i] += enemyY_change[i]

        # Collision

        collision = isCollision(enemy_X[i], enemy_Y[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            print(score_value)
            enemy_X[i] = random.randint(0, 736)
            enemy_Y[i] = random.randint(50, 250)

        enemy(enemy_X[i], enemy_Y[i], i)

    # Bullet Movement

    if bulletY <= 0:
        bullet_state = "ready"
        bulletY = 480

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # if enemy_Y > 600:
    #     bullet_state = "fired"

    showScore(textX, textY)

    pygame.display.update()
