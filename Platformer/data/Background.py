import pygame
from data import functions


class Background(pygame.sprite.Sprite):
    def __init__(self, group, background):
        super().__init__(group)
        self.rect = 0, 0
        self.image = functions.load_image(background)
