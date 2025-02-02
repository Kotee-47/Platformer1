import pygame
from data import functions


class Environment(pygame.sprite.Sprite):
    def __init__(self, picture, group, grp2, x, y, cell_size=16, additional_group=None):
        self.image = functions.load_image(picture)
        self.image = pygame.transform.scale(self.image, (cell_size, cell_size))
        if additional_group:
            super().__init__(group, grp2, additional_group)
        else:
            super().__init__(group, grp2)
        self.startrect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
        self.rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
        self.mask = pygame.mask.from_surface(self.image)