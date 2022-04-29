
import pygame


pygame.init()
# Create the Screen
screen = pygame.display.set_mode((800, 600))

# Title & Icon
pygame.display.set_caption('Space Invader')
icon = pygame.image.load('./img/ufo.png')
pygame.display.set_icon(icon)


# Game Loop


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Quitting Program")
            running = False



