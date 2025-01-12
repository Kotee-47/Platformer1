import os
import pygame
import sys


def load_image(name):
    fullname = os.path.join(name)
    if not os.path.isfile(fullname):
        print(f'Файл с изображением "{fullname}" не найден')
        sys.exit()

    image = pygame.image.load(fullname)
    image = image.convert_alpha()
    return image
