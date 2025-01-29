import pygame
from data import functions

class HealthBar(pygame.sprite.Sprite):
    def __init__(self, width, height, healthgrp):
        super().__init__(healthgrp)
        self.rect = pygame.Rect(0, 0, 256, 64)
        self.rect.x = width // 50
        self.rect.y = height // 50

        self.zero = functions.load_image('images/player/health_bar/0_hp.png')
        self.one = functions.load_image('images/player/health_bar/1_hp.png')
        self.two = functions.load_image('images/player/health_bar/2_hp.png')
        self.three = functions.load_image('images/player/health_bar/3_hp.png')
        self.four = functions.load_image('images/player/health_bar/4_hp.png')
        self.five = functions.load_image('images/player/health_bar/5_hp.png')
        self.six = functions.load_image('images/player/health_bar/6_hp.png')
        self.seven = functions.load_image('images/player/health_bar/7_hp.png')
        self.eight = functions.load_image('images/player/health_bar/8_hp.png')

        self.image = self.eight

    def update(self, health):
        if health == 0:
            self.image = self.zero
        elif 0 < health < 12.5:
            self.image = self.one
        elif 12.5 <= health < 25:
            self.image = self.two
        elif 25 <= health < 37.5:
            self.image = self.three
        elif 37.5 <= health < 50:
            self.image = self.four
        elif 50 <= health < 62.5:
            self.image = self.five
        elif 62.5 <= health < 75:
            self.image = self.six
        elif 75 <= health < 87.5:
            self.image = self.seven
        elif 87.5 <= health <= 100:
            self.image = self.eight