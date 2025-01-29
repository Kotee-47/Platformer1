import random
import os
from data import functions
import math
import pygame


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


class Board:
    def __init__(self, envgroup, decgroup, allgroup, dangroup, cell_size=16):
        self.cell_size = cell_size
        self.dangroup = dangroup
        self.envgroup = envgroup
        self.decgroup = decgroup
        self.allgroup = allgroup
        file = open('files/levels/yara_test_field.txt', 'rt')
        self.board = file.read().split('p')
        for i in range(0, len(self.board)):
            self.board[i] = self.board[i].split()
        file.close()
        self.width = len(self.board[0])
        self.height = len(self.board)
        self.left = 10
        self.top = 10

    def render(self, screen):
        objects = {}
        for x in range(self.width):
            for y in range(self.height):
                if self.board[y][x] == '0':
                    pass
                elif self.board[y][x] == '1':
                    sprite = Environment('images/blocks/environment/1_stone_surface.png',
                                         self.envgroup, self.allgroup, x, y,
                                         self.cell_size)
                elif self.board[y][x] == '2':
                    sprite = Environment('images/blocks/environment/2_stone.png',
                                         self.envgroup, self.allgroup, x, y,
                                         self.cell_size)
                elif self.board[y][x] == '3':
                    sprite = Environment('images/blocks/environment/3_stone_corner.png',
                                         self.envgroup, self.allgroup, x, y,
                                         self.cell_size)
                elif self.board[y][x] == '4':
                    sprite = Environment('images/blocks/decor/4_moss.png',
                                         self.decgroup, self.allgroup, x, y,
                                         self.cell_size)
                elif self.board[y][x] == '5':
                    sprite = Environment('images/blocks/environment/5_stone_surface_moss.png',
                                         self.envgroup, self.allgroup,
                                         x, y, self.cell_size)
                elif self.board[y][x] == '6':
                    sprite = Environment('images/blocks/decor/6_grass.png',
                                         self.decgroup, self.allgroup,
                                         x, y, self.cell_size)
                elif self.board[y][x] == '7':
                    sprite = Environment('images/blocks/environment/7_stone_surface_grass.png',
                                         self.envgroup, self.allgroup,
                                         x, y, self.cell_size)
                elif self.board[y][x] == '8':
                    sprite = Environment('images/blocks/environment/8_dead_bush.png',
                                         self.decgroup, self.allgroup,
                                         x, y, self.cell_size)
                elif self.board[y][x] == '9':
                    sprite = Environment('images/blocks/environment/9_dirt.png',
                                         self.envgroup, self.allgroup,
                                         x, y, self.cell_size)
                elif self.board[y][x] == '10':
                    sprite = Environment('images/blocks/danger/10_spikes.png',
                                         self.dangroup, self.allgroup,
                                         x, y, self.cell_size)
                elif self.board[y][x] == '11':
                    sprite = Environment('images/turret/turret_base.png',
                                         self.dangroup, self.allgroup,
                                         x, y, self.cell_size)
                elif self.board[y][x] == '12':
                    sprite = Turret('images/turret/turret_cannon.png', self.dangroup, self.allgroup, x, y, self.cell_size)
                    if 'turrets' in objects:
                        objects['turrets'].append(sprite)
                    else:
                        objects['turrets'] = [sprite]
        return objects


class firstBoard:
    def __init__(self, envgroup, decgroup, allgroup, dangroup, cell_size=16):
        self.cell_size = cell_size
        self.dangroup = dangroup
        self.envgroup = envgroup
        self.decgroup = decgroup
        self.allgroup = allgroup
        file = open('files/levels/first_level.txt', 'rt')
        self.board = file.read().split('p')
        for i in range(0, len(self.board)):
            self.board[i] = self.board[i].split()
        file.close()
        self.width = len(self.board[0])
        self.height = len(self.board)
        self.left = 10
        self.top = 10

    def render(self, screen):
        objects = {}
        for x in range(self.width):
            for y in range(self.height):
                if self.board[y][x] == '0':
                    pass
                elif self.board[y][x] == '1':
                    sprite = Environment('images/blocks/environment/1_stone_surface.png',
                                         self.envgroup, self.allgroup, x, y,
                                         self.cell_size)
                elif self.board[y][x] == '2':
                    sprite = Environment('images/blocks/environment/2_stone.png',
                                         self.envgroup, self.allgroup, x, y,
                                         self.cell_size)
                elif self.board[y][x] == '3':
                    sprite = Environment('images/blocks/environment/3_stone_corner.png',
                                         self.envgroup, self.allgroup, x, y,
                                         self.cell_size)
                elif self.board[y][x] == '4':
                    sprite = Environment('images/blocks/decor/4_moss.png',
                                         self.decgroup, self.allgroup, x, y,
                                         self.cell_size)
                elif self.board[y][x] == '5':
                    sprite = Environment('images/blocks/environment/5_stone_surface_moss.png',
                                         self.envgroup, self.allgroup,
                                         x, y, self.cell_size)
                elif self.board[y][x] == '6':
                    sprite = Environment('images/blocks/decor/6_grass.png',
                                         self.decgroup, self.allgroup,
                                         x, y, self.cell_size)
                elif self.board[y][x] == '7':
                    sprite = Environment('images/blocks/environment/7_stone_surface_grass.png',
                                         self.envgroup, self.allgroup,
                                         x, y, self.cell_size)
                elif self.board[y][x] == '8':
                    sprite = Environment('images/blocks/environment/8_dead_bush.png',
                                         self.decgroup, self.allgroup,
                                         x, y, self.cell_size)
                elif self.board[y][x] == '9':
                    sprite = Environment('images/blocks/environment/9_dirt.png',
                                         self.envgroup, self.allgroup,
                                         x, y, self.cell_size)
                elif self.board[y][x] == '10':
                    sprite = Environment('images/blocks/danger/10_spikes.png',
                                         self.dangroup, self.allgroup,
                                         x, y, self.cell_size)
                elif self.board[y][x] == '11':
                    sprite = Environment('images/turret/turret_base.png',
                                         self.dangroup, self.allgroup,
                                         x, y, self.cell_size)
                elif self.board[y][x] == '12':
                    sprite = Turret('images/turret/turret_cannon.png', self.dangroup, self.allgroup, x, y, self.cell_size)
                    if 'turrets' in objects:
                        objects['turrets'].append(sprite)
                    else:
                        objects['turrets'] = [sprite]
        return objects



class Player(pygame.sprite.Sprite):
    def __init__(self, picture, group, allgroup, healthgrp, x, y, width, height, cell_size=16):
        self.image = functions.load_image(picture)
        self.image = pygame.transform.scale(self.image, (cell_size * 2, cell_size))
        super().__init__(group, allgroup)
        self.rect = pygame.Rect(x * cell_size, y * cell_size, cell_size * 2, cell_size)
        self.newrect = pygame.Rect(x * cell_size, y * cell_size, 2 * cell_size + 2, cell_size)
        self.mask = pygame.mask.from_surface(self.image)
        self.x = 3 * 64
        self.y = 8 * 64
        self.y_speed = 0
        self.x_speed = 0
        self.left_player = False
        self.left_move = False
        self.right_move = False
        self.on_surf = False
        self.facing_right = True
        self.cell_size = cell_size
        self.healthbar = HealthBar(width, height, healthgrp)
        self.health = 100

    def update(self, env, dang, dt):
        self.on_surf = False
        spd1 = (3.125 * self.cell_size) // 1

        self.newrect.x = self.rect.x + self.x_speed * dt
        self.newrect.y = self.rect.y + self.y_speed * dt
        temp_srf = pygame.surface.Surface((self.newrect[2], self.newrect[3] - 6))
        temp_msk = pygame.mask.from_surface(temp_srf)
        tcat = TempCat(self.newrect, temp_msk)
        can_move = True

        if pygame.sprite.spritecollideany(self, env):
            self.on_surf = True
        for i in env:
            if pygame.sprite.collide_mask(tcat, i):
                can_move = False
        for i in dang:
            if pygame.sprite.collide_mask(self, i):
                self.y_speed -= 400
                self.health -= 12.5
        if not self.on_surf:
            if self.y_speed < spd1 * 3:
                self.y_speed += spd1 // 10
            else:
                self.y_speed = spd1 * 3
        else:
            if self.y_speed > 0:
                self.y_speed = 0

        if self.x_speed > spd1 * 2:
            self.x_speed = spd1 * 2
        elif self.x_speed < -spd1 * 2:
            self.x_speed = -spd1 * 2

        if self.left_move:
            self.x_speed -= spd1 // 10
        elif self.right_move:
            self.x_speed += spd1 // 10
        elif self.x_speed > spd1 // 10:
            self.x_speed -= spd1 // 20
        elif self.x_speed < -spd1 // 10:
            self.x_speed += spd1 // 20
        else:
            self.x_speed = 0

        if can_move:
            self.rect.x += self.x_speed * dt
            self.x += self.x_speed * dt
        self.rect.y += self.y_speed * dt
        self.y += self.y_speed * dt
        self.healthbar.update(self.health)

    def left(self, player):
        self.left_move = True
        self.right_move = False
        if self.facing_right:
            self.image = pygame.transform.flip(self.image, True, False)
            self.facing_right = False

    def right(self, player):
        self.left_move = False
        self.right_move = True
        if not self.facing_right:
            self.image = pygame.transform.flip(self.image, True, False)
            self.facing_right = True

    def jump(self):
        spd1 = (3.125 * self.cell_size) // 1
        if self.on_surf:
            if self.y_speed != 4 * spd1:
                self.y_speed = -4 * spd1


class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self, width, height, cell_size):
        self.width = width
        self.height = height
        self.dx = 0
        self.dy = 0
        self.cell_size = cell_size

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.x = obj.rect.x + self.dx - self.cell_size // 2
        obj.rect.y = obj.rect.y + self.dy - self.cell_size // 4

    # позиционировать камеру на объекте target
    def update(self, target):
        self.dx = -(target.rect.x + self.cell_size // 2 - self.width // 2)
        self.dy = -(target.rect.y + self.cell_size // 2 - self.height // 2)


class TempCat:
    def __init__(self, rect, mask):
        self.rect = rect
        self.mask = mask


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


class Background(pygame.sprite.Sprite):
    def __init__(self, group, background):
        super().__init__(group)
        self.rect = 0, 0
        self.image = functions.load_image(background)


class Turret(pygame.sprite.Sprite):
    cell_size = 16
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