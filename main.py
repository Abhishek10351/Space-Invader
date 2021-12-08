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
enemy_x_change = random.choice([3, -3])


def enemy(x, y):
    screen.blit(enemy_img, (x, y))


background_img = pygame.image.load("images/background.png")
laser_img = pygame.image.load("images/laser.png")
laser_x = 0
laser_y = 500
laser_y_change = 0
laser_state = "static"


def fire_laser(x, y):
    global laser_state
    laser_state = "dynamic"
    
    screen.blit(laser_img, (x, y))


run = True

player_x_change = 0
while run:
    screen.blit(background_img, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -5
            elif event.key == pygame.K_RIGHT:
                player_x_change = 5
            elif event.key == pygame.K_SPACE:
                laser_y_change = -20
                laser_y = 490
                laser_x = player_x + 15
                lasersound = pygame.mixer.Sound(r"C:\Users\user\Music\Digital Audio\laser1.ogg")
                lasersound.play()
                fire_laser(laser_x, laser_y)
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
        enemy_x_change = 3
    elif enemy_x >= 736:
        enemy_y += 64
        enemy_x_change = -3
    enemy_x += enemy_x_change

    if laser_y == 0:
        pass
    elif laser_y >=0:
        laser_y += laser_y_change
    else:  
        laser_state = "static"
    
    player(player_x, player_y)
    enemy(enemy_x, enemy_y)
    if laser_state == "dynamic":
        fire_laser(laser_x, laser_y)
    pygame.display.update()
