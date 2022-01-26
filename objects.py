import pygame


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
