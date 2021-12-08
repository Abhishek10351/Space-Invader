import pygame
import pathlib
import random
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load(
    r"C:\Users\user\Pictures\Games\2D\alien-ufo-pack\shipBlue_manned.png")
pygame.display.set_icon(icon)
player_img = pygame.image.load("images/player.png")
player_x = 350
player_y = 500


def player(x, y):
    screen.blit(player_img, (x, y))


enemy_img = pygame.image.load("images/enemy.png")
enemy_x = random.randint(0, 736)
enemy_y = random.randint(50, 150)
enemy_x_change = 0.3


def enemy(x, y):
    screen.blit(enemy_img, (x, y))


run = True

player_x_change = 0
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -0.5
            elif event.key == pygame.K_RIGHT:
                player_x_change = 0.5
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                player_x_change = 0
    player_x += player_x_change
    
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736
    player_x += player_x_change

    if enemy_x <= 0:
        enemy_y += 64
        enemy_x = 0
    elif enemy_x >= 736:
        enemy_y += 64
        enemy_x = 0
    enemy_x += enemy_x_change
    screen.fill((0, 0, 0))  # change bg color
    player(player_x, player_y)
    enemy(enemy_x, enemy_y)
    pygame.display.update()
