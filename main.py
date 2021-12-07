import pygame
import pathlib

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load(r"C:\Users\user\Pictures\Games\2D\alien-ufo-pack\shipBlue_manned.png")
pygame.display.set_icon(icon)
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
