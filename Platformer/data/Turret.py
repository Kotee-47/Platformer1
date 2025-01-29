import math
import random

import pygame
from data import functions


class Turret(pygame.sprite.Sprite):
    def __init__(self, picture, group, allgroup, x, y, cell_size):
        self.original_image = pygame.transform.scale(functions.load_image(picture), (cell_size, cell_size))
        self.image = self.original_image.copy()
        super().__init__(group, allgroup)
        self.x = x * cell_size
        self.y = y * cell_size
        self.rect = pygame.Rect(self.x, self.y, cell_size, cell_size)
        self.mask = pygame.mask.from_surface(self.image)
        self.degrees = 180

    def update(self, target_x, target_y):
        dx = target_x - self.x
        dy = target_y - self.y
        z = math.sqrt(dx ** 2 + dy ** 2)
        angle = math.degrees(math.acos(-dx / z) * math.copysign(1, math.asin(dy / z)))

        if angle != self.degrees:
            self.degrees = angle
            self.image = pygame.transform.rotate(self.original_image, self.degrees)
            self.rect = self.image.get_rect(center=self.rect.center)
            self.mask = pygame.mask.from_surface(self.image)
