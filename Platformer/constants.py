import pygame


WIDTH = 1080
HEIGHT = 720

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

ALL_SPRITES = pygame.sprite.Group()
ENVIRONMENT_SPRITES = pygame.sprite.Group()
DECOR_SPRITES = pygame.sprite.Group()
DANGER_SPRITES = pygame.sprite.Group()
PLAYER = pygame.sprite.Group()
JUMP_PADS = pygame.sprite.Group()
HEALTH = pygame.sprite.Group()
BACKGROUND = pygame.sprite.Group()
FINISH = pygame.sprite.Group()
FINISH_SCREEN = pygame.sprite.Group()
PAUSE = pygame.sprite.Group()
CELL_SIZE = 64
screen = pygame.display.set_mode((WIDTH, HEIGHT))
