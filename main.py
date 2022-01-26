import pygame
import pathlib
import random
from math import pow

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load(
    "images/icon.png")
pygame.display.set_icon(icon)


class Enemy:
    def __init__(self):
        self.started = False
        self.x = random.randint(0, 736)
        self.y = random.randint(50, 150)
        self.image = pygame.image.load("images/enemy.png")
        self.x_change = random.choice([3, -3])
    started = True


class Player:
    def __init__(self):
        self.x = 300
        self.y = 500
        self.x_change = 0
        self.image = pygame.image.load("images/player.png")


player = Player()


def show_player(x, y):
    screen.blit(player.image, (x, y))


def collision_occurred(lx, ly, ex, ey):
    a = not set(range(lx, lx+32)).isdisjoint(range(ex, ex+64))
    b = not set(range(ly, ly+32)).isdisjoint(range(ey, ey+64))
    return a and b


number_of_enemies = 20
enemies = [Enemy() for i in range(number_of_enemies)]
print(len(enemies))

def show_enemy(x, y):
    screen.blit(enemy.image, (x, y))


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
                if laser_state == "static" and not game_over:
                    laser_y_change = -20
                    laser_y = 495
                    laser_x = player.x + 15
                    lasersound = pygame.mixer.Sound("sounds/laser1.ogg")
                    lasersound.play()
                    fire_laser(laser_x, laser_y)
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
        if collision_occurred(laser_x, laser_y, enemy.x, enemy.y) and laser_state == "dynamic":
            score_value += 1
            enemy.x = random.randint(0, 736)
            enemy.y = random.randint(50, 150)

    if laser_y >= 0:
        laser_y += laser_y_change
    else:
        laser_state = "static"

    show_player(player.x, player.y)
    if not game_over:
        for enemy in enemies:
            show_enemy(enemy.x, enemy.y)
        if laser_state == "dynamic":
            fire_laser(laser_x, laser_y)
    else:
        show_game_over()
    update_score()
    pygame.display.update()
