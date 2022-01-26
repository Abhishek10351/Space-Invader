import pygame
import pathlib
import random
from objects import Player, Enemy, Laser
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load(
    "images/icon.png")
pygame.display.set_icon(icon)


player = Player()


def show_player(x, y):
    screen.blit(player.image, (x, y))


def collision_occurred(lx, ly, ex, ey):
    a = not set(range(lx, lx+32)).isdisjoint(range(ex, ex+64))
    b = not set(range(ly, ly+32)).isdisjoint(range(ey, ey+64))
    return a and b


no_of_enemies = 5
enemies = [Enemy() for i in range(no_of_enemies)]


def show_enemy(x, y):
    screen.blit(enemy.image, (x, y))


background_img = pygame.image.load("images/background.png")
laser = Laser()

def fire_laser(x, y):
    global laser
    laser.state = "dynamic"
    screen.blit(laser.image, (x, y))


score_value = 0

score_font = pygame.font.Font("freesansbold.ttf", 32)


def update_score():
    font = score_font.render(f"Score: {score_value}", True, 0X06F3A3)
    screen.blit(font, (10, 10))


game_over = False
game_over_font = pygame.font.Font("freesansbold.ttf", 64)


def show_game_over():
    font = game_over_font.render("Game Over", True, (255, 0, 0))
    screen.blit(font, (250, 250))


run = True

player.x_change = 0

while run:
    screen.blit(background_img, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.x_change = -5
            elif event.key == pygame.K_RIGHT:
                player.x_change = 5
            elif event.key == pygame.K_SPACE:
                if laser.state == "static" and not game_over:
                    laser.y_change = -20
                    laser.y = 495
                    laser.x = player.x + 15
                    lasersound = pygame.mixer.Sound("sounds/laser1.ogg")
                    lasersound.play()
                    fire_laser(laser.x, laser.y)
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                player.x_change = 0

    player.x += player.x_change

    if player.x <= 0:
        player.x = 736
        player.x_change = -5
    elif player.x >= 736:
        player.x = 0
        player.x_change = 5
    player.x += player.x_change

    for enemy in enemies:
        if enemy.y >= 532:
            game_over = True
        if enemy.x <= 0:
            enemy.y += 64
            enemy.x_change = 3
        elif enemy.x >= 736:
            enemy.y += 64
            enemy.x_change = -3
        enemy.x += enemy.x_change
        if laser.state == "dynamic":
            if collision_occurred(laser.x, laser.y, enemy.x, enemy.y) and laser.state == "dynamic":
                score_value += 1
                enemy.x = random.randint(0, 736)
                enemy.y = random.randint(50, 150)

    if laser.y >= 0:
        laser.y += laser.y_change
    else:
        laser.state = "static"

    show_player(player.x, player.y)
    if not game_over:
        for enemy in enemies:
            show_enemy(enemy.x, enemy.y)
        if laser.state == "dynamic":
            fire_laser(laser.x, laser.y)
    else:
        show_game_over()
    update_score()
    pygame.display.update()
